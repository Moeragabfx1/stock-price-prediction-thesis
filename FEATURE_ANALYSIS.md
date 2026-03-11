# Feature Analysis

## Purpose
This section interprets the feature-importance results in relation to Research Question 2:

**RQ2: Which technical indicators and price-based features contribute most to predictive performance?**

The aim is not only to identify highly ranked features, but also to assess what the distribution of feature importance implies for the broader thesis argument.

## Summary of Results
The aggregate feature-importance results indicate that **raw price-based variables dominate predictive performance**, while most engineered technical indicators contribute only modestly and sentiment variables contribute negligibly.

### Average importance across models and assets
| Feature | Category | Average Importance |
|---|---|---:|
| Close | Price | 0.4757 |
| Low | Price | 0.2051 |
| High | Price | 0.1213 |
| SMA_20 | Technical | 0.0762 |
| Open | Price | 0.0300 |
| SMA_200 | Technical | 0.0237 |
| BB_Upper | Technical | 0.0196 |
| EMA_20 | Technical | 0.0146 |
| SMA_50 | Technical | 0.0140 |
| EMA_50 | Technical | 0.0100 |

At category level, the pattern is clear:
- **Price-based features dominate overall importance**
- **Technical indicators add some explanatory value, but substantially less than price variables**
- **Sentiment features contribute effectively zero importance in the current setup**

## Main Interpretation
### 1. Raw prices drive the models
The most important variables are overwhelmingly **Close, Low, and High**, with **Close** alone accounting for almost half of average feature importance. This suggests that the next-day forecasting task is being driven primarily by **recent price structure**, rather than by more abstract transformed indicators.

This result matters because it weakens the common assumption that adding many technical indicators necessarily strengthens predictive performance. In this dataset, the strongest predictive signal appears to remain embedded in the original market variables themselves.

### 2. Technical indicators are not irrelevant, but they are secondary
Several technical indicators retain non-trivial importance, particularly:
- SMA_20
- SMA_200
- BB_Upper
- EMA_20
- SMA_50
- EMA_50

This suggests that some trend-following and volatility-related indicators still contain useful information. However, their contribution is **supplementary rather than dominant**. The evidence therefore supports a more restrained interpretation: technical indicators may enrich the feature space, but they do not displace raw price variables as the main source of predictive power.

### 3. Short-horizon momentum indicators contributed little
Indicators such as MACD, MACD_Signal, Returns_1d, Returns_5d, Momentum_10, and RSI showed very low average importance in the aggregate results. This may indicate that, for one-day-ahead forecasting, these derived short-horizon transformations add limited new information beyond what is already captured by the underlying price variables.

A plausible explanation is feature redundancy. Many technical indicators are deterministic transformations of the same underlying series. When the underlying price variables are already included, the model may assign little marginal value to those transformations.

### 4. Sentiment contributed no measurable importance
All sentiment variables in the aggregate report recorded effectively zero importance. This is consistent with the broader model-comparison results, where adding sentiment did not materially improve predictive performance.

This does **not** prove that market sentiment is universally irrelevant. A more defensible interpretation is that, within the present study design, sentiment failed to add measurable incremental predictive value. Several explanations are possible:
- limited and uneven article coverage across tickers
- noisy or heterogeneous news sources
- daily aggregation that may dilute short-lived reactions
- mismatch between headline tone and next-day price movement
- efficient incorporation of public news into liquid large-cap assets

This is therefore best interpreted as a **context-specific negative finding**, not a universal rejection of sentiment-based forecasting.

## Cross-Model Interpretation
The individual-stock results also indicate that the relative importance of technical indicators varies across assets and models. For example:
- For some assets, Random Forest distributed importance more broadly across moving averages and Bollinger features.
- For others, XGBoost concentrated importance sharply on a small subset of variables, sometimes overwhelmingly on one technical feature.

However, the broader pattern still holds: **price variables remained dominant in the majority of cases**, and sentiment features did not emerge as meaningful contributors.

This variation across models reinforces an important methodological point: feature-importance results should not be interpreted as stable causal rankings. Rather, they are model-dependent indicators of how the fitted model used the available information. For this reason, the thesis should interpret feature importance cautiously and in conjunction with out-of-sample performance.

## Theoretical Implications
These findings align with strands of the literature that question the out-of-sample value of large technical-indicator sets in financial prediction. If raw price variables dominate and most transformed features add little incremental value, then the practical benefit of extensive indicator engineering may be limited.

The results also support the broader thesis argument that **model simplicity may be advantageous in noisy financial settings**. If the strongest signals are already embedded in a small set of price features, then more complex models and feature sets may increase the risk of overfitting without delivering proportionate gains in predictive performance.

## Contribution to the Dissertation
The feature-analysis results strengthen the dissertation in three ways.

### First,
they provide a direct answer to RQ2 by identifying which features contribute most to predictive performance.

### Second,
they support the empirical finding that **Linear Regression remained competitive or superior despite its simplicity**, because the predictive structure appears to be dominated by a limited set of strong price-based features.

### Third,
they reinforce the interpretation that sentiment underperformed not only at model level, but also at feature level.

## Thesis-Safe Conclusion
A defensible academic conclusion is as follows:

> Feature-importance analysis indicates that next-day stock price forecasting in this study is driven primarily by raw price-based variables, particularly closing, low, and high prices. Technical indicators such as moving averages and Bollinger-based measures provide some additional information, but their contribution is clearly secondary. Sentiment variables do not exhibit meaningful predictive importance under the current data and aggregation design. These findings suggest that, in this setting, model performance depends more on recent market prices than on engineered technical or sentiment-derived features.

## How to Use This in the Final Thesis
This section should be used in:
- **Results chapter**: to report which variables mattered most
- **Discussion chapter**: to explain why simple models outperformed more complex methods
- **Critical analysis section**: to question the assumption that more engineered features necessarily improve financial forecasting

## Writing Notes
When this is transferred into the dissertation:
- do not present feature importance as causal proof
- do not overclaim that technical indicators are useless
- do not state that sentiment is irrelevant in all markets
- frame the findings as specific to this dataset, horizon, and validation design
