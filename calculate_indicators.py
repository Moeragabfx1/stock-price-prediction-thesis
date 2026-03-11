import pandas as pd
import ta
from ta.volatility import BollingerBands
import os
from pathlib import Path

# Paths
RAW_DIR = Path("/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/raw")
RAW_DIR_STOCKS = Path("/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/raw/stocks")
PROCESSED_DIR = Path("/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Stock files
STOCKS = ["TSLA", "NVDA", "META", "AAPL", "MSFT", "GOOGL", "AMZN", "SPY", "QQQ"]

def calculate_indicators(df):
    """Calculate technical indicators using ta library"""
    
    # Ensure numeric columns are numeric
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Handle Date column
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')
        df.set_index('Date', inplace=True)
    
    # Use 'Close' column for calculations
    close = df['Close'].dropna()
    
    if len(close) == 0:
        return df
    
    # RSI (14-day)
    df['RSI_14'] = ta.momentum.RSIIndicator(close, window=14).rsi()
    
    # MACD (12, 26, 9)
    macd = ta.trend.MACD(close, window_fast=12, window_slow=26, window_sign=9)
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    df['MACD_Hist'] = macd.macd_diff()
    
    # SMA - correct method name
    df['SMA_20'] = ta.trend.SMAIndicator(close, window=20).sma_indicator()
    df['SMA_50'] = ta.trend.SMAIndicator(close, window=50).sma_indicator()
    df['SMA_200'] = ta.trend.SMAIndicator(close, window=200).sma_indicator()
    
    # EMA
    df['EMA_20'] = ta.trend.EMAIndicator(close, window=20).ema_indicator()
    df['EMA_50'] = ta.trend.EMAIndicator(close, window=50).ema_indicator()
    
    # Bollinger Bands (20, 2)
    bbands = BollingerBands(close, window=20, window_dev=2)
    df['BB_Upper'] = bbands.bollinger_hband()
    df['BB_Middle'] = bbands.bollinger_mavg()
    df['BB_Lower'] = bbands.bollinger_lband()
    df['BB_Width'] = (df['BB_Upper'] - df['BB_Lower']) / df['BB_Middle']
    
    # Price Momentum (10-day)
    df['Momentum_10'] = ta.momentum.ROCIndicator(close, window=10).roc()
    
    # Returns (1-day, 5-day)
    df['Returns_1d'] = close.pct_change(periods=1)
    df['Returns_5d'] = close.pct_change(periods=5)
    
    # ATR (Average True Range) - volatility
    high = df['High'].dropna()
    low = df['Low'].dropna()
    if len(high) > 0 and len(low) > 0:
        df['ATR_14'] = ta.volatility.AverageTrueRange(high, low, close, window=14).average_true_range()
    
    return df

def find_stock_file(ticker):
    """Find the CSV file for a stock in either directory"""
    for directory in [RAW_DIR, RAW_DIR_STOCKS]:
        filepath = directory / f"{ticker}.csv"
        if filepath.exists():
            return filepath
    return None

def process_stock(ticker):
    """Process a single stock file"""
    filepath = find_stock_file(ticker)
    if filepath is None:
        raise FileNotFoundError(f"Cannot find {ticker}.csv")
    
    # Read CSV
    df = pd.read_csv(filepath)
    
    # Clean column names
    df.columns = [c.strip() for c in df.columns]
    
    # Remove rows where Close is not numeric (header/data rows)
    df = df[pd.to_numeric(df['Close'], errors='coerce').notna()].copy()
    
    # Keep only the columns we need
    cols_to_keep = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df[[c for c in cols_to_keep if c in df.columns]].copy()
    
    # Calculate indicators
    df = calculate_indicators(df)
    
    # Save to processed directory
    output_path = PROCESSED_DIR / f"{ticker}_indicators.csv"
    df.to_csv(output_path)
    
    return ticker, df

# Process all stocks and report
print("=" * 60)
print("TECHNICAL INDICATORS CALCULATION REPORT")
print("=" * 60)

for stock in STOCKS:
    try:
        ticker, df = process_stock(stock)
        rows = len(df)
        
        # Count missing values in indicator columns
        indicator_cols = [col for col in df.columns if col not in ['Open', 'High', 'Low', 'Close', 'Volume']]
        missing = df[indicator_cols].isna().sum()
        total_missing = missing.sum()
        
        print(f"\n{ticker}:")
        print(f"  Rows: {rows}")
        print(f"  Total missing values in indicators: {total_missing}")
        
        # Show missing per indicator
        if total_missing > 0:
            missing_pct = (missing / rows * 100).round(1)
            print(f"  Missing breakdown:")
            for col in indicator_cols:
                if missing[col] > 0:
                    print(f"    - {col}: {missing[col]} ({missing_pct[col]}%)")
                    
    except Exception as e:
        print(f"\n{stock}: ERROR - {e}")

print("\n" + "=" * 60)
print("DONE - Files saved to:", PROCESSED_DIR)
print("=" * 60)