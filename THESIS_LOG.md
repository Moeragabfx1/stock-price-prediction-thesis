# Thesis Development Log

## Project: LLM-Enhanced Sentiment + Technical Indicators for Stock Price Prediction

**Student:** Moe (University of East London)  
**Course:** DS-7010 Data Science Dissertation  
**Date Started:** 2026-03-11

---

## Phase 1: Setup & Literature Review

### Step 1.1: Topic Selection
- **Date:** 2026-03-11
- **Final Topic:** "LLM-Enhanced Sentiment + Technical Indicators for Stock Price Prediction"
- **Research Question:** "Can combining LLM-based financial sentiment analysis with traditional technical indicators improve stock price prediction accuracy compared to using either method alone?"
- **Outcome:** Topic approved based on literature review

### Step 1.2: Literature Review
- **Date:** 2026-03-11
- **Papers Analyzed:** 12 academic papers (2023-2026)
- **Key References:**
  1. FinBERT + LSTM (2023) - High relevance
  2. FinBERT-LSTM (2024) - High relevance
  3. FinBERT + GPT-4 + LogReg (2024) - 81.83% accuracy
  4. Technical Indicators Impact (2024) - Overfitting warning
  5. LSTM Fusion Sentiment + Technical (2025) - High relevance

- **Key Findings:**
  - Combining sentiment + technical indicators improves prediction
  - Simpler models (LogReg) can outperform complex LLMs
  - Technical indicators alone show overfitting issues
  - Sentiment adds value across sectors

### Step 1.3: GitHub Repository
- **Created:** https://github.com/Moeragabfx1/stock-price-prediction-thesis
- **Commits:**
  - Initial setup with requirements.txt
  - Literature Review added

---

## Phase 2: Data Collection

### Step 2.1: Stock Price Data
- **Date:** 2026-03-11
- **Source:** Yahoo Finance (`yfinance`)
- **Stocks:** TSLA, NVDA, META, AAPL, MSFT, GOOGL, AMZN, SPY, QQQ
- **Time Range:** 2020-01 to 2026-03
- **Records:** ~1,547 to 1,554 daily rows per ticker
- **Columns:** Open, High, Low, Close, Volume
- **Data Quality:** No duplicate rows, no zero prices, no zero volumes

### Step 2.2: News Data
- **Date:** 2026-03-11
- **Attempted Sources:** NewsAPI, GDELT, Yahoo/yfinance, web search
- **Outcome:** Built uneven but usable sentiment coverage across all 9 tickers
- **Current sentiment coverage days:**
  - TSLA: 2
  - NVDA: 10
  - META: 28
  - AAPL: 25
  - MSFT: 20
  - GOOGL: 21
  - AMZN: 21
  - SPY: 22
  - QQQ: 33
- **Key limitation:** sentiment coverage is short-window and inconsistent across tickers

### Step 2.3: Cron Job Setup
- **Date:** 2026-03-11
- **Job:** Weekly literature search cron (Sunday 10 AM ICT)
- **Purpose:** Expand academic references for thesis writing

---

## Phase 3: Feature Engineering (Completed)

### Step 3.1: Technical Indicators
- **Completed:** RSI_14, MACD, SMA_20/50/200, EMA_20/50, Bollinger Bands, Momentum_10, Returns_1d/5d, ATR_14
- **Note:** missing early rows are expected due to rolling-window lookback periods

### Step 3.2: Sentiment Analysis
- **Completed:** Daily sentiment scoring pipeline built and rerun for all 9 tickers
- **Final approach:** VADER-based sentiment scoring with title+description aggregation
- **Cleaning applied:** junk filtering, date normalization, daily aggregation
- **Important revision:** initial FinBERT plan was dropped because the host environment lacked the required transformer stack and the lighter pipeline was more reproducible for this project

### Step 3.3: Feature Combination
- **Completed:** Technical indicators merged with daily sentiment signals per ticker
- **Fallback logic:** missing sentiment days filled neutrally to preserve aligned stock timelines

---

## Phase 4: Model Building (Completed - Initial Experimental Round)

### Models Compared:
1. **Linear Regression**
2. **Random Forest**
3. **XGBoost**

### Evaluation Design:
- Standard train/test split
- Baseline comparison (naive, buy-and-hold)
- Walk-forward validation

### Evaluation Metrics:
- RMSE
- MAE
- Directional Accuracy

### Current Result Summary:
- **Best overall model:** Linear Regression
- **Complex models:** Random Forest and XGBoost generally overfit
- **Sentiment effect:** negligible under current coverage and setup
- **Naive baseline:** still difficult to beat consistently, which is realistic in financial prediction
---

## Key Decisions & Rationale

| Decision | Rationale |
|----------|-----------|
| 9 stocks + indices | Improves generalization beyond the original 5-stock design |
| 1-Day Prediction | Manageable scope for 3-month thesis |
| Walk-forward validation | More rigorous and academically defensible than a simple split |
| Linear Regression kept as primary benchmark | Most robust model in actual experiments |
| Compare Tech-only vs Tech+Sentiment | Directly answers the core research question |
| Use lightweight reproducible sentiment pipeline | Practical and repeatable within environment constraints |

---

## Known Limitations

1. **Sentiment coverage:** short-window and uneven across tickers
2. **News quality:** mixed source quality due free-source constraints
3. **Time Range:** market data begins in 2020
4. **Domain scope:** emphasis remains on large-cap tech stocks plus two US indices
5. **Predictive ceiling:** naive baseline remains hard to beat consistently

---

## Next Steps

1. [ ] Update proposal / thesis outline to reflect the real 9-stock results
2. [ ] Rewrite literature review summary so it matches findings, not hopes
3. [ ] Strengthen critical analysis section around why sentiment underperformed
4. [ ] Expand academic references toward 30+
5. [ ] Draft methodology chapter
6. [ ] Draft results chapter

---

*Log started: 2026-03-11*
*Last updated: 2026-03-11 14:50 ICT*