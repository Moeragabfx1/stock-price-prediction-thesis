# Project Status - Thesis Working Summary

## Current Thesis Direction
**Working title:** Stock Price Prediction Using Technical Indicators and News Sentiment: A Comparative Study Across 9 Stocks and Indices

## Current Dataset
### Assets
- TSLA
- NVDA
- META
- AAPL
- MSFT
- GOOGL
- AMZN
- SPY
- QQQ

### Market data
- Source: Yahoo Finance (`yfinance`)
- Period: 2020-01 to 2026-03
- Features: Open, High, Low, Close, Volume

### Technical indicators
- RSI_14
- MACD / MACD_Signal / MACD_Hist
- SMA_20 / SMA_50 / SMA_200
- EMA_20 / EMA_50
- Bollinger Bands
- Momentum_10
- Returns_1d / Returns_5d
- ATR_14

### Sentiment pipeline
- Source mix: existing scraped news + GDELT + Yahoo/yfinance recovery for missing coverage
- Current sentiment model: VADER-based daily aggregation
- Cleaning applied:
  - title + description scoring
  - junk filtering
  - date parsing normalization
  - daily aggregation by ticker

## Current Sentiment Coverage
| Ticker | Coverage Days |
|--------|---------------|
| TSLA | 2 |
| NVDA | 10 |
| META | 28 |
| AAPL | 25 |
| MSFT | 20 |
| GOOGL | 21 |
| AMZN | 21 |
| SPY | 22 |
| QQQ | 33 |

## What the results say now
### Strong findings
1. **Linear Regression is the most robust model overall**
2. **Random Forest and XGBoost generally overfit**
3. **Naive baseline remains difficult to beat**
4. **Sentiment adds negligible predictive value in the current setup**
5. **Expanding from 5 to 9 tickers did not change the main conclusion**

### Best thesis-safe interpretation
This study finds that simpler linear models are more robust than more complex ensemble methods under walk-forward validation, while news sentiment features contribute limited incremental predictive value under the current data coverage and preprocessing setup.

## Current academic position
### Strengths
- 9-ticker dataset instead of 5
- baseline comparison included
- walk-forward validation included
- feature importance completed
- sentiment pipeline exists and is testable
- conclusion is realistic, not exaggerated

### Limitations to state explicitly
- sentiment coverage is short-window and uneven
- sentiment source quality is mixed
- analysis focuses on large-cap tech stocks and US equity indices
- predictive gains over naive baseline are limited

## Next document updates needed
1. Align literature review with actual findings
2. Update proposal/thesis framing so RQ3 is honest
3. Emphasize robustness over hype
4. Present sentiment as tested but weak, not assumed beneficial
5. Build feature-importance findings into a formal academic analysis section (see `FEATURE_ANALYSIS.md`)
