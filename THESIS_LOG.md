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
- **Source:** Yahoo Finance (yfinance)
- **Stocks:** TSLA, NVDA, META, AAPL, MSFT, GOOGL, AMZN, SPY, QQQ
- **Time Range:** 2020-01-02 to 2026-02-27
- **Records:** 1,547 days × 5 stocks = 7,735 total records
- **Columns:** Open, High, Low, Close, Volume
- **Data Quality:** No missing values

### Step 2.2: News Data
- **Date:** 2026-03-11
- **Initial Attempt:** NewsAPI.io (failed - free tier only allows past month)
- **Alternative Source:** GDELT + web search
- **Total Articles:** 3,075

| Stock | Articles |
|-------|----------|
| TSLA | 178 |
| NVDA | 735 |
| META | 798 |
| AAPL | 645 |
| MSFT | 719 |

- **Limitation:** NewsAPI free tier restricts historical data. GDELT provides partial coverage.
- **Lesson Learned:** For full historical coverage, consider paid NewsAPI ($75/month) or Bloomberg/Reuters.

### Step 2.3: Cron Job Setup
- **Date:** 2026-03-11
- **Job:** Weekly news scan (Every Wednesday 8 AM ICT)
- **Purpose:** Keep news data updated for thesis

---

## Phase 3: Feature Engineering (In Progress)

### Step 3.1: Technical Indicators
- **To Do:** Calculate RSI, MACD, Moving Averages, Bollinger Bands
- **Tools:** pandas-ta library

### Step 3.2: Sentiment Analysis
- **To Do:** Run FinBERT on all 3,075 news articles
- **Model:** ProsusAI/finbert (HuggingFace)
- **Classes:** positive, negative, neutral

### Step 3.3: Feature Combination
- **To Do:** Merge technical indicators + daily sentiment scores

---

## Phase 4: Model Building (Pending)

### Models to Compare:
1. **Baseline:** Linear Regression (technical indicators only)
2. **Model A:** XGBoost (technical indicators only)
3. **Model B:** Random Forest (technical + sentiment)
4. **Model C:** LSTM (if time permits)

### Evaluation Metrics:
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- R² (Coefficient of Determination)

---

## Key Decisions & Rationale

| Decision | Rationale |
|----------|-----------|
| 5 Tech Stocks | High volume, well-documented, good for comparison |
| 1-Day Prediction | Manageable scope for 3-month thesis |
| FinBERT | Proven performance on financial text |
| Compare Tech-only vs Tech+Sentiment | Answer the core research question |

---

## Known Limitations

1. **News Data:** Historical news limited by API restrictions
2. **Time Range:** Stock data starts 2020 (not 2015-2020)
3. **Single Sector:** All tech stocks (generalization limited)

---

## Next Steps

1. [ ] Run FinBERT sentiment analysis on news
2. [ ] Calculate technical indicators
3. [ ] Build and train models
4. [ ] Compare results
5. [ ] Write methodology chapter
6. [ ] Write results chapter

---

*Log started: 2026-03-11*
*Last updated: 2026-03-11 14:48 ICT*