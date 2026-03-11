"""
Feature Importance Analysis
Identifies which technical indicators and sentiment features matter most
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import warnings
warnings.filterwarnings('ignore')

STOCKS = ['TSLA', 'NVDA', 'META', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'SPY', 'QQQ']
DATA_DIR = 'data/processed'

def load_and_merge_data(stock):
    """Load indicators and sentiment, merge on date."""
    ind_df = pd.read_csv(f'{DATA_DIR}/{stock}_indicators.csv')
    sen_df = pd.read_csv(f'{DATA_DIR}/{stock}_sentiment.csv')
    
    ind_df['Date'] = pd.to_datetime(ind_df['Date'])
    sen_df['Date'] = pd.to_datetime(sen_df['date'])
    sen_df = sen_df.drop(columns=['date'])
    
    merged = pd.merge(ind_df, sen_df, on='Date', how='left')
    merged = merged.sort_values('Date').reset_index(drop=True)
    
    sentiment_cols = ['positive_score', 'negative_score', 'neutral_score', 'article_count']
    for col in sentiment_cols:
        if col in merged.columns:
            if col == 'article_count':
                merged[col] = merged[col].fillna(0)
            else:
                merged[col] = merged[col].fillna(0.33)
    
    return merged

def prepare_features(df):
    """Prepare features for modeling."""
    df = df.copy()
    df['Target'] = df['Close'].shift(-1)
    df = df.dropna(subset=['Target'])
    
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 
                'RSI', 'MACD', 'MACD_Signal', 
                'SMA_20', 'SMA_50', 'SMA_200',
                'EMA_20', 'EMA_50',
                'BB_Upper', 'BB_Lower', 'BB_Width',
                'Momentum_10', 'Returns_1d', 'Returns_5d',
                'positive_score', 'negative_score', 'neutral_score', 'article_count']
    
    # Categorize features
    price_features = ['Open', 'High', 'Low', 'Close', 'Volume']
    tech_indicators = ['RSI', 'MACD', 'MACD_Signal', 
                       'SMA_20', 'SMA_50', 'SMA_200',
                       'EMA_20', 'EMA_50',
                       'BB_Upper', 'BB_Lower', 'BB_Width',
                       'Momentum_10', 'Returns_1d', 'Returns_5d']
    sentiment_features = ['positive_score', 'negative_score', 'neutral_score', 'article_count']
    
    feature_categories = {}
    for f in features:
        if f in price_features:
            feature_categories[f] = 'Price'
        elif f in tech_indicators:
            feature_categories[f] = 'Technical'
        elif f in sentiment_features:
            feature_categories[f] = 'Sentiment'
    
    df_clean = df.dropna(subset=features + ['Target'])
    return df_clean[features], df_clean['Target'], feature_categories

def analyze_feature_importance():
    """Analyze which features matter most."""
    all_importances = []
    
    models = [
        ('Random Forest', RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)),
        ('XGBoost', XGBRegressor(n_estimators=100, max_depth=5, random_state=42, verbosity=0)),
    ]
    
    for stock in STOCKS:
        print(f"\n{'='*50}")
        print(f"Stock: {stock}")
        print('='*50)
        
        df = load_and_merge_data(stock)
        X, y, feature_cats = prepare_features(df)
        
        # Train/test split
        split_idx = int(len(X) * 0.8)
        X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
        y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
        
        for model_name, model in models:
            model.fit(X_train, y_train)
            
            # Get feature importances
            importances = model.feature_importances_
            feature_imp = pd.DataFrame({
                'feature': X.columns,
                'importance': importances,
                'category': [feature_cats.get(f, 'Other') for f in X.columns]
            }).sort_values('importance', ascending=False)
            
            # Store
            for _, row in feature_imp.iterrows():
                all_importances.append({
                    'stock': stock,
                    'model': model_name,
                    'feature': row['feature'],
                    'importance': row['importance'],
                    'category': row['category']
                })
            
            # Print top 10
            print(f"\n{model_name} - Top 10 Features:")
            for i, row in feature_imp.head(10).iterrows():
                print(f"  {row['feature']:20s} {row['importance']:.4f} ({row['category']})")
    
    # Aggregate across all stocks
    print(f"\n\n{'='*60}")
    print("AGGREGATE FEATURE IMPORTANCE (Average Across All Stocks)")
    print('='*60)
    
    imp_df = pd.DataFrame(all_importances)
    
    # Average importance per feature
    avg_imp = imp_df.groupby(['feature', 'category'])['importance'].mean().reset_index()
    avg_imp = avg_imp.sort_values('importance', ascending=False)
    
    print("\n--- Top 15 Features Overall ---")
    for i, row in avg_imp.head(15).iterrows():
        print(f"  {row['feature']:20s} {row['importance']:.4f} ({row['category']})")
    
    # By category
    print("\n--- Importance by Category ---")
    cat_imp = imp_df.groupby('category')['importance'].mean().sort_values(ascending=False)
    total = cat_imp.sum()
    for cat, imp in cat_imp.items():
        print(f"  {cat:15s}: {imp:.4f} ({imp/total*100:.1f}%)")
    
    # Per model
    print("\n--- Top 5 by Model ---")
    for model in ['Random Forest', 'XGBoost']:
        model_imp = imp_df[imp_df['model'] == model].groupby('feature')['importance'].mean()
        model_imp = model_imp.sort_values(ascending=False).head(5)
        print(f"\n{model}:")
        for f, v in model_imp.items():
            print(f"  {f}: {v:.4f}")
    
    # Save
    imp_df.to_csv('reports/feature_importance.csv', index=False)
    avg_imp.to_csv('reports/feature_importance_avg.csv', index=False)
    print(f"\nResults saved to reports/feature_importance.csv")
    
    return imp_df, avg_imp

if __name__ == '__main__':
    analyze_feature_importance()