"""
Model Builder: Compare Tech-Only vs Tech+Sentiment Performance
"""
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

try:
    from xgboost import XGBRegressor
    HAS_XGB = True
except ImportError:
    HAS_XGB = False
    print("XGBoost not available, skipping...")

STOCKS = ['TSLA', 'NVDA', 'META', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'SPY', 'QQQ']
DATA_DIR = 'data/processed'
SENTIMENT_COLS = ['positive_score', 'negative_score', 'neutral_score', 'article_count']
TECH_FEATURES = [
    'Open', 'High', 'Low', 'Close', 'Volume',
    'RSI_14', 'MACD', 'MACD_Signal',
    'SMA_20', 'SMA_50', 'SMA_200',
    'EMA_20', 'EMA_50',
    'BB_Upper', 'BB_Lower', 'BB_Width',
    'Momentum_10', 'Returns_1d', 'Returns_5d', 'ATR_14'
]

def _load_indicator_df(stock):
    df = pd.read_csv(f'{DATA_DIR}/{stock}_indicators.csv')
    if 'Date' not in df.columns:
        first_col = df.columns[0]
        df = df.rename(columns={first_col: 'Date'})
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

def _load_sentiment_df(stock):
    path = f'{DATA_DIR}/{stock}_sentiment.csv'
    if os.path.exists(path):
        sen_df = pd.read_csv(path)
        if 'Date' not in sen_df.columns:
            if 'date' in sen_df.columns:
                sen_df['Date'] = pd.to_datetime(sen_df['date'], errors='coerce')
                sen_df = sen_df.drop(columns=['date'])
            else:
                first_col = sen_df.columns[0]
                sen_df = sen_df.rename(columns={first_col: 'Date'})
                sen_df['Date'] = pd.to_datetime(sen_df['Date'], errors='coerce')
    else:
        sen_df = pd.DataFrame({'Date': []})

    for col in SENTIMENT_COLS:
        if col not in sen_df.columns:
            sen_df[col] = np.nan
    return sen_df[['Date'] + SENTIMENT_COLS]

def load_and_merge_data(stock):
    """Load indicators and sentiment, merge on date with graceful fallback."""
    ind_df = _load_indicator_df(stock)
    sen_df = _load_sentiment_df(stock)

    merged = pd.merge(ind_df, sen_df, on='Date', how='left')
    merged = merged.sort_values('Date').reset_index(drop=True)

    # Forward-fill sentiment if present, then fill remaining with neutral defaults
    for col in SENTIMENT_COLS:
        merged[col] = merged[col].ffill()
        if col == 'article_count':
            merged[col] = merged[col].fillna(0)
        elif col == 'neutral_score':
            merged[col] = merged[col].fillna(1.0)
        else:
            merged[col] = merged[col].fillna(0.0)

    return merged

def prepare_features(df, include_sentiment=True):
    """Prepare features for modeling."""
    df = df.copy()
    df['Target'] = df['Close'].shift(-1)
    df = df.dropna(subset=['Target'])

    features = TECH_FEATURES + (SENTIMENT_COLS if include_sentiment else [])
    df_clean = df.dropna(subset=features + ['Target'])

    X = df_clean[features]
    y = df_clean['Target']
    return X, y, features

def calculate_directional_accuracy(y_true, y_pred):
    y_true_diff = np.diff(y_true)
    y_pred_diff = np.diff(y_pred)
    if len(y_true_diff) == 0:
        return 0.0
    correct = np.sum((y_true_diff * y_pred_diff) > 0)
    return correct / len(y_true_diff) * 100

def train_and_evaluate(X, y, model_name, model):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    if len(X_train) < 50 or len(X_test) < 10:
        return None

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    dir_acc = calculate_directional_accuracy(y_test.values, y_pred)

    return {
        'model': model_name,
        'rmse': rmse,
        'mae': mae,
        'directional_accuracy': dir_acc,
        'train_size': len(X_train),
        'test_size': len(X_test)
    }

def run_comparison():
    results = []

    for stock in STOCKS:
        print(f"\n{'='*50}")
        print(f"Processing: {stock}")
        print('='*50)

        try:
            df = load_and_merge_data(stock)
            print(f"Merged data: {len(df)} rows")
        except Exception as e:
            print(f"Error loading {stock}: {e}")
            continue

        print(f"\n--- Tech-Only Features ---")
        X_tech, y_tech, tech_feat = prepare_features(df, include_sentiment=False)
        print(f"Features: {len(tech_feat)}, Samples: {len(X_tech)}")

        base_models = [
            ('Linear Regression', LinearRegression()),
            ('Random Forest', RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42))
        ]
        for name, model in base_models:
            result = train_and_evaluate(X_tech, y_tech, f"{stock} - {name} (Tech)", model)
            if result:
                results.append(result)
                print(f"{name}: RMSE={result['rmse']:.4f}, MAE={result['mae']:.4f}, Dir Acc={result['directional_accuracy']:.2f}%")

        if HAS_XGB:
            result = train_and_evaluate(
                X_tech, y_tech, f"{stock} - XGBoost (Tech)",
                XGBRegressor(n_estimators=100, max_depth=5, random_state=42, verbosity=0)
            )
            if result:
                results.append(result)
                print(f"XGBoost: RMSE={result['rmse']:.4f}, MAE={result['mae']:.4f}, Dir Acc={result['directional_accuracy']:.2f}%")

        print(f"\n--- Tech + Sentiment Features ---")
        X_full, y_full, full_feat = prepare_features(df, include_sentiment=True)
        print(f"Features: {len(full_feat)}, Samples: {len(X_full)}")

        for name, model in base_models:
            result = train_and_evaluate(X_full, y_full, f"{stock} - {name} (Tech+Sent)", model)
            if result:
                results.append(result)
                print(f"{name}: RMSE={result['rmse']:.4f}, MAE={result['mae']:.4f}, Dir Acc={result['directional_accuracy']:.2f}%")

        if HAS_XGB:
            result = train_and_evaluate(
                X_full, y_full, f"{stock} - XGBoost (Tech+Sent)",
                XGBRegressor(n_estimators=100, max_depth=5, random_state=42, verbosity=0)
            )
            if result:
                results.append(result)
                print(f"XGBoost: RMSE={result['rmse']:.4f}, MAE={result['mae']:.4f}, Dir Acc={result['directional_accuracy']:.2f}%")

    print(f"\n\n{'='*60}")
    print("SUMMARY: Tech-Only vs Tech+Sentiment")
    print('='*60)

    results_df = pd.DataFrame(results)
    if len(results_df) > 0:
        results_df['feature_set'] = results_df['model'].apply(
            lambda x: 'Tech-Only' if '(Tech)' in x else 'Tech+Sent'
        )
        summary = results_df.groupby('feature_set').agg({
            'rmse': 'mean',
            'mae': 'mean',
            'directional_accuracy': 'mean'
        }).round(4)
        print(summary)

        print("\n--- By Model ---")
        model_summary = results_df.groupby(['feature_set', 'model']).agg({
            'rmse': 'mean',
            'mae': 'mean',
            'directional_accuracy': 'mean'
        }).round(4)
        print(model_summary)

    results_df.to_csv('reports/model_comparison_results.csv', index=False)
    print("\nResults saved to reports/model_comparison_results.csv")
    return results_df

if __name__ == '__main__':
    run_comparison()
