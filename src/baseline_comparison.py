"""
Baseline Comparison: Our Models vs Naive vs Buy & Hold
"""
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

STOCKS = ['TSLA', 'NVDA', 'META', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'SPY', 'QQQ']
DATA_DIR = 'data/processed'
SENTIMENT_COLS = ['positive_score', 'negative_score', 'neutral_score', 'article_count']
FEATURES = [
    'Open', 'High', 'Low', 'Close', 'Volume',
    'RSI_14', 'MACD', 'MACD_Signal',
    'SMA_20', 'SMA_50', 'SMA_200',
    'EMA_20', 'EMA_50',
    'BB_Upper', 'BB_Lower', 'BB_Width',
    'Momentum_10', 'Returns_1d', 'Returns_5d', 'ATR_14',
    'positive_score', 'negative_score', 'neutral_score', 'article_count'
]

def _load_indicator_df(stock):
    df = pd.read_csv(f'{DATA_DIR}/{stock}_indicators.csv')
    if 'Date' not in df.columns:
        df = df.rename(columns={df.columns[0]: 'Date'})
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
                sen_df = sen_df.rename(columns={sen_df.columns[0]: 'Date'})
                sen_df['Date'] = pd.to_datetime(sen_df['Date'], errors='coerce')
    else:
        sen_df = pd.DataFrame({'Date': []})

    for col in SENTIMENT_COLS:
        if col not in sen_df.columns:
            sen_df[col] = np.nan
    return sen_df[['Date'] + SENTIMENT_COLS]

def load_and_merge_data(stock):
    ind_df = _load_indicator_df(stock)
    sen_df = _load_sentiment_df(stock)

    merged = pd.merge(ind_df, sen_df, on='Date', how='left')
    merged = merged.sort_values('Date').reset_index(drop=True)

    for col in SENTIMENT_COLS:
        merged[col] = merged[col].ffill()
        if col == 'article_count':
            merged[col] = merged[col].fillna(0)
        elif col == 'neutral_score':
            merged[col] = merged[col].fillna(1.0)
        else:
            merged[col] = merged[col].fillna(0.0)
    return merged

def prepare_features(df):
    df = df.copy()
    df['Target'] = df['Close'].shift(-1)
    df = df.dropna(subset=['Target'])
    df_clean = df.dropna(subset=FEATURES + ['Target'])
    return df_clean[FEATURES], df_clean['Target'], df_clean['Close']

def calculate_metrics(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    if len(y_true) > 1:
        actual_diff = np.diff(y_true)
        pred_diff = np.diff(y_pred)
        dir_acc = np.mean((actual_diff * pred_diff) > 0) * 100
    else:
        dir_acc = 0
    return rmse, mae, mape, dir_acc

def run_baseline_comparison():
    results = []
    models = [
        ('Linear Regression', LinearRegression, {}),
        ('Random Forest', RandomForestRegressor, {'n_estimators': 100, 'max_depth': 10, 'random_state': 42}),
        ('XGBoost', XGBRegressor, {'n_estimators': 100, 'max_depth': 5, 'random_state': 42, 'verbosity': 0}),
    ]

    for stock in STOCKS:
        print(f"\n{'='*60}")
        print(f"Stock: {stock}")
        print('='*60)

        try:
            df = load_and_merge_data(stock)
            X, y, close_prices = prepare_features(df)
        except Exception as e:
            print(f"Error: {e}")
            continue

        split_idx = int(len(X) * 0.8)
        X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
        y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
        close_test = close_prices.iloc[split_idx:]

        if len(X_test) < 20:
            print("Skipped: not enough test samples")
            continue

        naive_pred = close_test.iloc[:-1].values
        naive_actual = close_test.iloc[1:].values
        naive_rmse, naive_mae, naive_mape, naive_dir = calculate_metrics(naive_actual, naive_pred)
        print(f"Naive (tomorrow=today): RMSE={naive_rmse:.4f}, MAE={naive_mae:.4f}, Dir Acc={naive_dir:.2f}%")

        initial_price = close_test.iloc[0]
        bh_pred = np.full(len(close_test), initial_price)
        bh_rmse, bh_mae, bh_mape, bh_dir = calculate_metrics(close_test.values, bh_pred)
        print(f"Buy & Hold: RMSE={bh_rmse:.4f}, MAE={bh_mae:.4f}, Dir Acc={bh_dir:.2f}%")

        for model_name, model_class, params in models:
            model = model_class(**params)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            rmse, mae, mape, dir_acc = calculate_metrics(y_test.values, y_pred)
            beat_naive = rmse < naive_rmse
            beat_bh = rmse < bh_rmse
            results.append({
                'stock': stock,
                'model': model_name,
                'rmse': rmse,
                'mae': mae,
                'mape': mape,
                'directional_accuracy': dir_acc,
                'beat_naive': beat_naive,
                'beat_buy_hold': beat_bh
            })
            print(f"{model_name}: RMSE={rmse:.4f}, MAE={mae:.4f}, Dir Acc={dir_acc:.2f}% [{'✓' if beat_naive else '✗'} naive, {'✓' if beat_bh else '✗'} B&H]")

    print(f"\n\n{'='*70}")
    print("BASELINE COMPARISON SUMMARY")
    print('='*70)

    results_df = pd.DataFrame(results)
    if len(results_df) > 0:
        print("\n--- Average Performance ---")
        summary = results_df.groupby('model').agg({
            'rmse': 'mean',
            'mae': 'mean',
            'mape': 'mean',
            'directional_accuracy': 'mean',
            'beat_naive': 'mean',
            'beat_buy_hold': 'mean'
        }).round(4)
        summary['beat_naive'] = (summary['beat_naive'] * 100).round(1).astype(str) + '%'
        summary['beat_buy_hold'] = (summary['beat_buy_hold'] * 100).round(1).astype(str) + '%'
        print(summary)

    results_df.to_csv('reports/baseline_comparison.csv', index=False)
    print("\nResults saved to reports/baseline_comparison.csv")
    return results_df

if __name__ == '__main__':
    run_baseline_comparison()
