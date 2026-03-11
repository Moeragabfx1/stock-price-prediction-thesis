# Proposal Outline

## Working Title
**Evaluating the Incremental Predictive Value of Technical Indicators and News Sentiment for Next-Day Stock Price Forecasting: Evidence from Nine US Stocks and Indices**

---

## 1. Introduction
This dissertation examines whether technical indicators and news sentiment provide incremental predictive value for next-day stock price forecasting across nine large-cap US stocks and benchmark indices. Stock prediction remains an important but difficult problem in financial research because highly liquid markets are noisy, adaptive, and difficult to outperform consistently. While prior studies often report improved performance from combining sentiment analysis with technical indicators, such findings are not always stable across datasets, model classes, or validation frameworks. This study therefore evaluates whether those reported gains remain under a more rigorous and practically constrained design.

The dissertation focuses on three model classes—Linear Regression, Random Forest, and XGBoost—and compares technical-indicator-only models with sentiment-enhanced variants. Performance is evaluated using baseline comparison and walk-forward validation in order to assess not only predictive accuracy but also robustness. The study is motivated by the need to distinguish between apparent in-sample improvement and genuine out-of-sample predictive value.

---

## 2. Research Problem
A persistent issue in financial forecasting literature is that improved predictive performance is often reported without sufficiently rigorous validation or without clear evidence that additional features provide meaningful incremental value over simple baselines. Sentiment-enhanced forecasting models are a clear example of this problem. Although many studies suggest that sentiment extracted from financial news or social media can improve stock prediction, the practical value of sentiment may depend heavily on data quality, coverage, preprocessing decisions, and market context.

This creates a gap between published claims and realistic application. The central problem addressed in this dissertation is therefore whether technical indicators and news sentiment genuinely improve next-day forecasting performance when tested across multiple assets, against simple benchmarks, and under walk-forward validation.

---

## 3. Research Aim
To evaluate whether technical indicators and news sentiment provide incremental predictive value for next-day stock price forecasting across selected US equities and benchmark indices under rigorous out-of-sample testing conditions.

---

## 4. Research Objectives
1. To construct a next-day stock price forecasting dataset using price-based variables, technical indicators, and aggregated daily news sentiment for nine selected US stocks and indices.
2. To compare the predictive performance of Linear Regression, Random Forest, and XGBoost models using technical indicators alone and using technical indicators combined with sentiment features.
3. To assess whether sentiment features add incremental predictive value beyond technical indicators under both standard train-test and walk-forward validation settings.
4. To evaluate model performance against simple baselines, including naive forecasting and buy-and-hold benchmarks.
5. To identify which features contribute most to model performance and examine whether raw price variables dominate engineered indicators and sentiment variables.
6. To critically analyse the limitations of sentiment-enhanced forecasting in the context of data quality, market efficiency, and model complexity.

---

## 5. Research Questions
### Main Research Question
Do technical indicators and news sentiment provide incremental predictive value over simple baselines for next-day stock price forecasting across selected US stocks and indices?

### Sub-Questions
**RQ1.** How do Linear Regression, Random Forest, and XGBoost compare in forecasting next-day stock prices using technical indicators?

**RQ2.** Which technical indicators and price-based features contribute most to predictive performance?

**RQ3.** Does the inclusion of aggregated daily news sentiment improve predictive performance relative to technical-indicator-only models?

**RQ4.** How robust are the observed results under walk-forward validation and baseline comparison?

---

## 6. Hypotheses
**H1.** Technical-indicator-based machine learning models will produce lower forecast error than buy-and-hold benchmarks, but will not consistently outperform naive next-day forecasts.

**H2.** Linear Regression will demonstrate greater out-of-sample robustness than Random Forest and XGBoost under walk-forward validation.

**H3.** The inclusion of aggregated daily news sentiment will not produce substantial incremental predictive improvement over technical-indicator-only models under the current data coverage and aggregation design.

**H4.** Raw price-based variables will contribute more strongly to predictive performance than most engineered technical indicators and sentiment features.

---

## 7. Brief Literature Positioning
Existing literature suggests three broad themes. First, financial sentiment can improve prediction under some conditions, particularly when sentiment signals are rich, frequent, and domain-specific. Second, technical indicators remain widely used in financial prediction, although several studies report weak out-of-sample generalisation and overfitting. Third, more complex models do not necessarily outperform simpler methods, particularly in noisy financial environments.

This dissertation contributes to that discussion by testing these claims under a more cautious and realistic design. Rather than assuming sentiment improves prediction, it asks whether such improvement remains visible after introducing baseline comparison, walk-forward validation, and a multi-asset sample.

---

## 8. Methodology
### 8.1 Research Design
The study adopts a quantitative comparative design. It evaluates multiple forecasting models across two feature configurations:
1. technical indicators only
2. technical indicators plus sentiment features

The analysis is conducted across nine assets:
- TSLA
- NVDA
- META
- AAPL
- MSFT
- GOOGL
- AMZN
- SPY
- QQQ

### 8.2 Data Sources
**Market data:** Yahoo Finance (`yfinance`) daily historical data from 2020 onwards.

**News data:** free-source news collection assembled from available news files, GDELT, and Yahoo/yfinance recovery where available.

### 8.3 Variables
**Dependent variable:** next-day closing price.

**Independent variables:**
- Raw price variables: Open, High, Low, Close, Volume
- Technical indicators: RSI_14, MACD, MACD_Signal, SMA_20, SMA_50, SMA_200, EMA_20, EMA_50, Bollinger Band measures, Momentum_10, Returns_1d, Returns_5d, ATR_14
- Sentiment variables: positive score, negative score, neutral score, article count

### 8.4 Sentiment Construction
News items are cleaned, filtered, dated, and aggregated to daily ticker-level sentiment signals. The sentiment pipeline uses a lightweight reproducible scoring method and combines title and description text where available. Daily mean sentiment scores and article counts are then merged with the price dataset.

### 8.5 Modelling Approach
The dissertation compares:
- Linear Regression
- Random Forest
- XGBoost

### 8.6 Evaluation Strategy
Performance is evaluated using:
- standard time-ordered train-test split
- naive baseline forecast
- buy-and-hold benchmark
- walk-forward validation across multiple test windows

### 8.7 Evaluation Metrics
- RMSE
- MAE
- Directional Accuracy

### 8.8 Feature Analysis
Feature-importance analysis is used to identify which variables contribute most strongly to prediction and to assess whether raw price features dominate engineered indicators and sentiment variables.

---

## 9. Expected Findings / Current Direction
The current results suggest that Linear Regression is the most robust model, while Random Forest and XGBoost show signs of overfitting. Preliminary analysis also indicates that sentiment features provide little additional predictive value in the current setup. Rather than weakening the dissertation, these findings support a more critical and academically valuable conclusion: sentiment-enhanced forecasting may be less effective than often claimed when tested under realistic data limitations and stronger validation standards.

---

## 10. Significance of the Study
This dissertation is significant for three reasons.

First, it contributes to the practical evaluation of whether sentiment features genuinely improve short-horizon stock forecasting.

Second, it provides evidence on the comparative robustness of simple and complex models in noisy financial settings.

Third, it offers a critical perspective on the gap between optimistic literature claims and real-world performance under constrained data conditions.

---

## 11. Limitations
The study has several limitations that should be acknowledged explicitly.

1. Sentiment coverage is uneven across assets and limited in time span.
2. News quality is constrained by free-source availability.
3. Market data begins in 2020 rather than covering a longer historical horizon.
4. The study focuses on large-cap US technology stocks and two benchmark indices, which limits broader generalisation.
5. Predictive gains over naive baselines may remain small, reflecting the difficulty of short-horizon financial forecasting.

---

## 12. Provisional Chapter Structure
### Chapter 1 - Introduction
- Background
- Research problem
- Aim and objectives
- Research questions
- Dissertation structure

### Chapter 2 - Literature Review
- Financial forecasting literature
- Technical indicators in prediction
- Sentiment analysis in finance
- Model complexity and robustness
- Research gap

### Chapter 3 - Methodology
- Research design
- Data sources
- Feature engineering
- Sentiment construction
- Model design
- Validation strategy
- Evaluation metrics

### Chapter 4 - Results
- Descriptive data summary
- Baseline comparison
- Standard model comparison
- Walk-forward validation
- Feature-importance analysis

### Chapter 5 - Discussion
- Interpretation of findings
- Why Linear Regression performed best
- Why sentiment underperformed
- Relation to prior literature
- Theoretical and practical implications
- Limitations

### Chapter 6 - Conclusion
- Summary of findings
- Contribution
- Limitations
- Future research

---

## 13. Immediate Writing Priorities
1. Strengthen the literature review so that it supports critical discussion, not just background summary.
2. Convert current experimental findings into formal tables and narrative suitable for the Results chapter.
3. Expand discussion around why sentiment failed to deliver measurable gains.
4. Ensure all methodological choices are justified clearly and concisely.
5. Maintain formal, evidence-led academic writing throughout.
