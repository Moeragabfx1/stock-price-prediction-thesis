# Chapter 3: Methodology

## 3.1 Introduction
This chapter explains the methodological design used to evaluate whether technical indicators and news sentiment provide incremental predictive value for next-day stock price forecasting. The study adopts a quantitative empirical design and compares three supervised learning models—Linear Regression, Random Forest, and XGBoost—across two feature configurations: technical indicators only, and technical indicators combined with daily aggregated news sentiment.

The methodological emphasis of this dissertation is not merely predictive performance, but robust evaluation. For that reason, the analysis does not rely on a single random split. Instead, model performance is examined through time-ordered train-test separation, explicit baseline comparison, and walk-forward validation. This design is intended to reduce the risk of overstating predictive performance in a domain where overfitting, data leakage, and unstable generalisation are persistent concerns.

## 3.2 Research Design
The study uses a quantitative comparative forecasting design. Its purpose is to test whether the addition of sentiment-derived variables improves next-day price prediction relative to technical-indicator-only models and simple benchmarks.

The design has four main components.

First, a multi-asset dataset was constructed using daily market data for nine US equities and benchmark indices: Tesla (TSLA), NVIDIA (NVDA), Meta (META), Apple (AAPL), Microsoft (MSFT), Alphabet (GOOGL), Amazon (AMZN), SPY, and QQQ. This selection was intended to provide variation across large-cap technology equities while also including two broad benchmark exchange-traded funds for comparison.

Second, technical indicators were calculated from historical price data and combined with raw market variables. This provided a feature set that reflects common practice in financial forecasting research.

Third, daily sentiment variables were generated from collected news data and merged with the market dataset by date. This allowed direct comparison between technical-only and sentiment-enhanced models.

Fourth, multiple model classes and validation procedures were used in order to assess both predictive performance and robustness. Rather than assuming that more complex models would outperform simpler ones, the study explicitly compares a linear model with two non-linear ensemble-based methods.

## 3.3 Data Sources
### 3.3.1 Market Data
Daily historical market data were collected using the `yfinance` Python library from Yahoo Finance. For each asset, the dataset included the following variables:
- Open
- High
- Low
- Close
- Volume

The market data covered the period from January 2020 to March 2026, depending on availability at the time of extraction. The final dataset contained approximately 1,547 to 1,554 daily observations per asset.

Yahoo Finance was selected for two reasons. First, it provides accessible historical data for both individual equities and benchmark ETFs, making it suitable for student-level empirical work. Second, its use is common in academic and applied finance projects where large-scale proprietary data are unavailable. The choice nevertheless introduces limitations, particularly because the dataset is restricted to publicly available daily observations and does not include intraday information, order-book variables, or proprietary institutional data.

### 3.3.2 News Data
News data were assembled from available free-source news files, supplemented where possible by GDELT and Yahoo/yfinance-derived article metadata. The original intention was to use a more advanced financial-language sentiment approach; however, in practice, the final pipeline prioritised reproducibility and data availability over model complexity.

The final news corpus was uneven across assets and limited in temporal depth. This is an important limitation of the study and is addressed explicitly in the discussion chapter. Nevertheless, sufficient dated news coverage was obtained to construct ticker-level daily sentiment signals for all nine assets.

## 3.4 Variable Construction
### 3.4.1 Dependent Variable
The dependent variable in this study is the next-day closing price. For each observation at time *t*, the prediction target is the closing price at time *t+1*. This was implemented by shifting the close-price series forward by one trading day.

A next-day forecasting horizon was selected for two reasons. First, it keeps the scope manageable within the constraints of a Master's dissertation. Second, one-day-ahead forecasting is a sufficiently demanding benchmark in liquid equity markets, where short-horizon predictability is generally weak.

### 3.4.2 Price-Based Variables
The raw market variables used as predictors were Open, High, Low, Close, and Volume. These variables were retained as direct model inputs rather than being treated only as inputs to technical-indicator engineering. This decision was motivated by the possibility that original market variables may contain stronger predictive information than transformed indicators, a possibility that was later supported by feature-importance analysis.

### 3.4.3 Technical Indicators
The following technical indicators were calculated from the market data:
- Relative Strength Index (RSI_14)
- Moving Average Convergence Divergence (MACD)
- MACD Signal
- Simple Moving Average (SMA_20, SMA_50, SMA_200)
- Exponential Moving Average (EMA_20, EMA_50)
- Bollinger Band Upper, Lower, and Width measures
- Momentum_10
- Returns_1d and Returns_5d
- Average True Range (ATR_14)

These indicators were selected because they represent commonly used trend, momentum, volatility, and smoothing measures in technical-analysis-based forecasting studies. Including a broad but recognisable set of indicators also made it possible to assess whether such engineered variables contribute meaningful information beyond raw market prices.

### 3.4.4 Sentiment Variables
Ticker-level daily sentiment variables were constructed from the collected news data. The final sentiment pipeline used a lightweight VADER-based scoring approach, applied to article titles and descriptions after basic filtering and cleaning.

For each article, sentiment scores were generated and classified into positive, negative, and neutral components. These article-level scores were then aggregated to the daily ticker level. The resulting sentiment variables were:
- positive_score
- negative_score
- neutral_score
- article_count

The sentiment design prioritised reproducibility and transparency. This was preferable to relying on a heavier transformer-based pipeline that could not be consistently executed within the working environment. Although this decision may reduce domain-specific language sensitivity compared with specialised financial-language models, it improved the replicability of the final workflow.

## 3.5 Data Preprocessing
### 3.5.1 Date Alignment and Merging
Market and sentiment data were merged by trading date after date normalisation. The market dataset was retained as the primary timeline, and sentiment variables were merged onto this structure using a left join. This ensured that all market observations remained available even when sentiment coverage was absent for a given day.

### 3.5.2 Handling Missing Values
Missing values arose primarily from two sources.

First, rolling technical indicators generate expected missing values at the beginning of the time series because sufficient prior observations are required before the indicator can be computed. For example, SMA_200 cannot be calculated until 200 prior observations are available.

Second, sentiment coverage was incomplete and uneven across assets and dates.

These forms of missingness were handled differently. Technical-indicator warm-up rows were excluded naturally when model training required complete predictor sets. Missing sentiment values were filled using neutral defaults in order to preserve the full market timeline for comparison across models. This choice reflects the assumption that absence of news should not automatically be interpreted as either strongly positive or strongly negative sentiment.

### 3.5.3 Avoiding Data Leakage
Because the dissertation concerns time-series forecasting, preventing data leakage was essential. The following precautions were used:
- target values were defined strictly as next-day close
- train-test splits preserved temporal order
- no random shuffling was used during evaluation
- walk-forward validation ensured that each test period was predicted using only prior observations

These steps were taken to reduce the risk of inflated performance estimates caused by future information entering the training process.

## 3.6 Model Selection
Three models were selected for comparison.

### 3.6.1 Linear Regression
Linear Regression was included as the simplest benchmark among the machine learning models. It provides an interpretable baseline and is useful for determining whether a relatively simple linear mapping between predictors and next-day price is sufficient. In financial prediction tasks, simpler models are often dismissed too quickly, despite evidence that they can remain competitive under noisy and low-signal conditions.

### 3.6.2 Random Forest
Random Forest was selected as a non-linear ensemble model capable of capturing more complex feature interactions. It is widely used in financial prediction studies because it is comparatively robust and less sensitive to scaling assumptions than many alternative methods. However, it can still overfit when the signal-to-noise ratio is weak or when many related predictors are included.

### 3.6.3 XGBoost
XGBoost was selected because gradient boosting methods are frequently reported as strong performers in structured tabular prediction tasks. Its inclusion allows direct comparison between a simple linear model and more flexible boosted-tree modelling. At the same time, the model’s flexibility makes it especially important to evaluate under robust out-of-sample procedures rather than relying on apparent in-sample fit.

## 3.7 Feature Configurations
Two feature configurations were evaluated.

### Technical-only configuration
This configuration included raw price variables and technical indicators, but excluded sentiment variables.

### Technical-plus-sentiment configuration
This configuration included the same market and technical features, with the addition of positive_score, negative_score, neutral_score, and article_count.

This two-configuration design directly addresses the central research question by isolating the incremental contribution of sentiment.

## 3.8 Evaluation Strategy
### 3.8.1 Standard Time-Ordered Train-Test Split
The first evaluation step used an 80/20 time-ordered split. Earlier observations were used for training, while later observations were reserved for testing. No shuffling was applied.

This provides an initial view of out-of-sample performance, but by itself it is insufficient for strong claims in time-series forecasting. For this reason, additional validation procedures were also used.

### 3.8.2 Baseline Comparison
Model performance was compared with two simple benchmarks:
- **Naive forecast:** tomorrow’s close is assumed to equal today’s close
- **Buy-and-hold benchmark:** included as a practical reference point for persistent position-based comparison

These baselines were included because machine learning forecasts in finance are only meaningful if they can be interpreted relative to simple alternatives. In particular, the naive forecast is difficult to beat in short-horizon liquid markets and therefore provides a realistic benchmark for predictive value.

### 3.8.3 Walk-Forward Validation
Walk-forward validation was used as the most rigorous evaluation procedure in the dissertation. Under this approach, models were trained on all observations available up to a given point and tested on a subsequent forward window. This process was repeated across multiple test-window lengths.

The use of walk-forward validation is methodologically important because it better reflects how forecasting models would operate in practice and reduces the risk of overstating model performance based on a single historical split.

## 3.9 Evaluation Metrics
Three metrics were used.

### RMSE
Root Mean Square Error was used to assess the magnitude of prediction error while penalising larger deviations more heavily.

### MAE
Mean Absolute Error was used as a complementary measure of average prediction error that is less sensitive than RMSE to extreme individual errors.

### Directional Accuracy
Directional Accuracy was included to assess whether the model correctly predicted the direction of price movement, rather than only its numerical distance from the true value. This is useful because a model may have moderate regression error while still capturing directional movement reasonably well.

The use of multiple metrics was intended to avoid over-reliance on any single evaluation criterion.

## 3.10 Feature Importance Analysis
Feature-importance analysis was conducted in order to identify which variables contributed most strongly to model predictions. This was particularly important for answering Research Question 2 and for assessing whether raw market variables, engineered indicators, or sentiment-derived variables carried the strongest predictive signal.

The feature-importance results were interpreted cautiously. Such measures indicate how a model distributed importance within the fitted feature space, but they do not establish causal influence. They are therefore used in this dissertation as interpretive tools rather than proof of market mechanisms.

## 3.11 Reliability, Validity, and Limitations
This study improves reliability by using a reproducible Python-based workflow, clear feature definitions, and explicit evaluation procedures. Internal validity is strengthened through time-aware validation and baseline comparison. However, several limitations remain.

First, the sentiment data are constrained by free-source availability and uneven coverage across assets. Second, the study uses daily data rather than higher-frequency market observations. Third, the selected assets are concentrated in large-cap US technology and benchmark index contexts, which limits broader generalisation.

These limitations do not invalidate the study, but they do restrict the strength of claims that can be made. For that reason, the findings are interpreted as evidence within a defined empirical setting rather than as universal conclusions about sentiment or stock prediction more broadly.

## 3.12 Chapter Summary
This chapter has outlined the methodological framework used to evaluate technical indicators and news sentiment in next-day stock price forecasting. The study combines multi-asset market data, engineered technical indicators, daily aggregated sentiment signals, and three model classes under time-aware validation procedures. By comparing model performance against simple baselines and by using walk-forward evaluation, the methodology is designed to prioritise robustness over headline performance. The following chapter presents the empirical results generated from this framework.
