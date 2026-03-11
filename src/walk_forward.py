"""
Walk-Forward Validation + Baseline Comparison
More rigorous evaluation for academic standards
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

def prepare_features(df, include_sentiment=True):
    df = df.copy()
    df['Target'] = df['Close'].shift(-1)
    df = df.dropna(subset=['Target'])
    features = TECH_FEATURES + (SENTIMENT_COLS if include_sentiment else [])
    df_clean = df.dropna(subset=features + ['Target', 'Date'])
    return df_clean[features], df_clean['Target'], df_clean['Date']

def walk_forward_evaluation(X, y, dates, model_class, model_params):
    results = []
    if len(X) < 260:
        return results

    for test_days in [30, 60, 90]:
        min_train = 200
        train_end = len(X) - test_days
        if train_end < min_train:
            continue

        X_train = X.iloc[:train_end]
        y_train = y.iloc[:train_end]
        X_test = X.iloc[train_end:]
        y_test = y.iloc[train_end:]

        if len(X_test) < 10:
            continue

        model = model_class(**model_params)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)

        if len(y_test) > 1:
            actual_diff = np.diff(y_test.values)
            pred_diff = np.diff(y_pred)
            dir_acc = np.mean((actual_diff * pred_diff) > 0) * 100
            naive_pred = y_test.iloc[:-1].values
            naive_actual = y_test.iloc[1:].values
            naive_rmse = np.sqrt(mean_squared_error(naive_actual, naive_pred))
            naive_mae = np.mean(np.abs(naive_actual - naive_pred))
        else:
            dir_acc = 0.0
            naive_rmse = rmse
            naive_mae = mae

        results.append({
            'test_days': test_days,
            'train_size': len(X_train),
            'test_size': len(X_test),
            'rmse': rmse,
            'mae': mae,
            'directional_accuracy': dir_acc,
            'naive_rmse': naive_rmse,
            'naive_mae': naive_mae,
            'beat_naive': rmse < naive_rmse
        })
    return results

def run_walk_forward():
    all_results = []
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
        except Exception as e:
            print(f"Error: {e}")
            continue

        for model_name, model_class, params in models:
            for include_sentiment in [False, True]:
                feature_set = 'Tech+Sent' if include_sentiment else 'Tech-Only'
                X, y, dates = prepare_features(df, include_sentiment)
                wf_results = walk_forward_evaluation(X, y, dates, model_class, params)

                if wf_results:
                    for r in wf_results:
                        all_results.append({
                            'stock': stock,
                            'model': model_name,
                            'feature_set': feature_set,
                            **r
                        })
                    avg_rmse = np.mean([r['rmse'] for r in wf_results])
                    avg_naive = np.mean([r['naive_rmse'] for r in wf_results])
                    beat_pct = np.mean([r['beat_naive'] for r in wf_results]) * 100
                    print(f"{model_name} ({feature_set}):")
                    print(f"  Avg RMSE: {avg_rmse:.4f} vs Naive: {avg_naive:.4f}")
                    print(f"  Beat Naive: {beat_pct:.1f}%")

    print(f"\n\n{'='*70}")
    print("WALK-FORWARD VALIDATION SUMMARY")
    print('='*70)

    results_df = pd.DataFrame(all_results)
    if len(results_df) > 0:
        summary = results_df.groupby(['model', 'feature_set']).agg({
            'rmse': 'mean',
            'naive_rmse': 'mean',
            'directional_accuracy': 'mean',
            'beat_naive': 'mean'
        }).round(4)
        print("\n--- Average Across All Stocks ---")
        print(summary)

        print("\n--- Best Model Per Stock ---")
        best_per_stock = results_df.loc[results_df.groupby('stock')['rmse'].idxmin(),
                                        ['stock', 'model', 'feature_set', 'rmse', 'directional_accuracy', 'beat_naive']]
        print(best_per_stock.to_string(index=False))

    results_df.to_csv('reports/walk_forward_results.csv', index=False)
    print("\nResults saved to reports/walk_forward_results.csv")
    return results_df

if __name__ == '__main__':
    run_walk_forward()
