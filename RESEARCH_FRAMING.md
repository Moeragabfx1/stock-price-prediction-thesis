# Research Framing

## Proposed Title
**Evaluating the Incremental Predictive Value of Technical Indicators and News Sentiment for Next-Day Stock Price Forecasting: Evidence from Nine US Stocks and Indices**

## Research Aim
To evaluate whether technical indicators and news sentiment provide incremental predictive value for next-day stock price forecasting across selected US equities and benchmark indices under rigorous out-of-sample testing conditions.

## Research Objectives
1. To construct a next-day stock price forecasting dataset using price-based variables, technical indicators, and aggregated daily news sentiment for nine selected US stocks and indices.
2. To compare the predictive performance of Linear Regression, Random Forest, and XGBoost models using technical indicators alone and using technical indicators combined with sentiment features.
3. To assess whether sentiment features add incremental predictive value beyond technical indicators under both standard train-test and walk-forward validation settings.
4. To evaluate model performance against simple baselines, including naive forecasting and buy-and-hold benchmarks.
5. To identify which features contribute most to model performance and examine whether raw price variables dominate engineered indicators and sentiment variables.
6. To critically analyse the limitations of sentiment-enhanced forecasting in the context of data quality, market efficiency, and model complexity.

## Main Research Question
Do technical indicators and news sentiment provide incremental predictive value over simple baselines for next-day stock price forecasting across selected US stocks and indices?

## Sub-Questions
### RQ1
How do Linear Regression, Random Forest, and XGBoost compare in forecasting next-day stock prices using technical indicators?

### RQ2
Which technical indicators and price-based features contribute most to predictive performance?

### RQ3
Does the inclusion of aggregated daily news sentiment improve predictive performance relative to technical-indicator-only models?

### RQ4
How robust are the observed results under walk-forward validation and baseline comparison?

## Hypotheses
### H1
Technical-indicator-based machine learning models will produce lower forecast error than buy-and-hold benchmarks, but will not consistently outperform naive next-day forecasts.

### H2
Linear Regression will demonstrate greater out-of-sample robustness than Random Forest and XGBoost under walk-forward validation.

### H3
The inclusion of aggregated daily news sentiment will not produce substantial incremental predictive improvement over technical-indicator-only models under the current data coverage and aggregation design.

### H4
Raw price-based variables will contribute more strongly to predictive performance than most engineered technical indicators and sentiment features.

## Proposal Framing Paragraph
This dissertation examines whether technical indicators and news sentiment provide incremental predictive value for next-day stock price forecasting across nine large-cap US stocks and benchmark indices. Using Linear Regression, Random Forest, and XGBoost, the study compares technical-only and sentiment-enhanced models under baseline comparison and walk-forward validation. Rather than assuming sentiment improves prediction, the study evaluates whether such gains persist under realistic data constraints and noisy market conditions. The research therefore focuses not only on predictive performance, but also on model robustness, feature relevance, and the limitations of sentiment-based forecasting in financial markets.

## Why This Framing Is Stronger
- It does not overclaim predictive success.
- It matches the actual evidence already produced.
- It supports a rigorous discussion of both positive and negative findings.
- It creates a clearer bridge between methodology, results, and critical analysis.
- It is more defensible at Master's level than a broad 'AI predicts stocks' framing.
