# Proposal Direction

## Working Title
**Evaluating the Incremental Predictive Value of Technical Indicators and News Sentiment for Next-Day Stock Price Forecasting: Evidence from Nine US Stocks and Indices**

## Core Research Question
Do technical indicators and news sentiment provide incremental predictive value over simple baselines for next-day stock price forecasting across selected US stocks and indices?

## Refined Position
This thesis does **not** assume sentiment will help. It tests whether sentiment adds incremental predictive value under realistic data constraints.

That is a stronger academic position than promising a gain and then trying to justify it after the fact.

## Scope
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

### Prediction task
- Next-day closing price prediction

### Feature sets
1. **Technical-only**
2. **Technical + sentiment**

### Models
- Linear Regression
- Random Forest
- XGBoost

### Evaluation
- Standard train/test split
- Baseline comparison:
  - Naive forecast (tomorrow = today)
  - Buy-and-hold baseline
- Walk-forward validation
- Metrics:
  - RMSE
  - MAE
  - Directional Accuracy

## Current Findings
### Robust findings
- Linear Regression is the most robust overall model
- Random Forest and XGBoost generally overfit
- Naive baseline remains difficult to beat consistently
- Sentiment features add negligible predictive value in the current setup
- Expanding from 5 to 9 tickers did not change the core conclusion

### Why this is still a good thesis
Negative or limited results are still valid if:
- the question is clear
- the method is sound
- the evaluation is rigorous
- the interpretation is honest

That is exactly where this project is heading.

## Key Methodological Strengths
- Multi-asset dataset instead of single-stock cherry-picking
- Walk-forward validation instead of a weak static split only
- Explicit baseline comparison
- Feature importance analysis already completed
- Real discussion of sentiment-data limitations

## Key Limitations to state openly
- Sentiment coverage is short-window and uneven across tickers
- Free-source news quality is mixed
- Market data begins in 2020
- Focus is primarily on large-cap US tech plus benchmark indices
- Gains over naive baseline are limited

## Best Thesis Framing
A strong framing is:

> This study evaluates whether news sentiment provides incremental predictive value beyond technical indicators for next-day stock price prediction across 9 major stocks and indices. Results indicate that simpler linear models are more robust than more complex ensemble methods, while sentiment contributes little additional predictive power under the current data and coverage conditions.

## What to emphasize in writing
### Emphasize
- robustness
- realism
- reproducibility
- baseline difficulty
- why complex models failed
- why sentiment underperformed

### Do not overclaim
- do not claim sentiment improves prediction unless the results show it clearly
- do not pretend complex models are better just because they are more advanced
- do not frame a negative result as failure; frame it as evidence

## Immediate writing implications
### Methodology chapter
Explain:
- data collection pipeline
- indicator engineering
- sentiment construction
- handling missing/rolling-window values
- baseline design
- walk-forward validation

### Results chapter
Show:
- model comparison tables
- baseline comparison tables
- walk-forward summary
- feature importance findings
- limited impact of sentiment features

### Discussion chapter
Interpret:
- why Linear Regression remained strongest
- why Random Forest/XGBoost overfit
- why sentiment may have underperformed
- how this compares with prior literature
- what data quality constraints likely affected RQ3
