# Chapter 1: Introduction

## 1.1 Background
Forecasting stock prices has long occupied a central position in finance, economics, and quantitative trading. The problem remains attractive because even modest predictive improvements may have practical value in portfolio management, risk assessment, and trading strategy design. At the same time, stock-price forecasting remains difficult because financial markets are noisy, adaptive, and highly sensitive to new information. In liquid equity markets in particular, short-horizon prediction is challenging because public information may be incorporated rapidly into prices, reducing the opportunity for persistent predictive advantage.

The development of machine learning has renewed interest in this problem. Compared with traditional statistical approaches, machine learning models offer greater flexibility in modelling non-linear relationships and interactions among predictors. As a result, recent studies have explored a wide range of forecasting approaches, including tree-based ensemble models, deep learning architectures, and sentiment-enhanced prediction frameworks. Within this literature, two classes of predictors appear frequently. The first consists of technical indicators derived from historical market data, such as moving averages, momentum measures, and volatility bands. The second consists of sentiment variables extracted from financial news or social media, motivated by the view that market prices may respond not only to past price behaviour but also to the informational tone of public discourse.

Although both approaches have been widely studied, the empirical evidence remains mixed. Some studies report that sentiment features improve predictive performance, particularly when combined with technical indicators or deep learning architectures. Other studies suggest that such gains may be unstable, highly context-dependent, or sensitive to data quality and evaluation design. Similarly, although technical indicators remain widely used in applied forecasting, their out-of-sample value has been questioned in recent work that highlights overfitting and weak generalisation. These tensions indicate that the problem is not simply whether more features or more complex models can be added, but whether they provide genuine incremental predictive value under realistic testing conditions.

## 1.2 Research Context and Motivation
This dissertation is motivated by two related concerns. The first is methodological. A substantial proportion of financial forecasting research reports model improvements without sufficiently rigorous evaluation against simple baselines or without validation procedures that reflect the temporal structure of market data. In time-series forecasting, apparent predictive success may be overstated when models are assessed using weak train-test designs or when feature sets introduce redundancy without improving genuine out-of-sample performance.

The second concern is substantive. News sentiment is often presented as a promising enhancement to price-based forecasting, particularly in recent machine learning and language-model research. However, the practical usefulness of sentiment may depend heavily on article coverage, source quality, preprocessing decisions, aggregation methods, and market conditions. In other words, sentiment may appear powerful in some research settings while offering little additional value in others. This raises a question that is both practically and academically relevant: does sentiment still improve next-day stock price prediction when tested across multiple liquid assets, under constrained real-world data conditions, and against simple but difficult benchmarks?

This dissertation addresses that question through a comparative study of nine US stocks and benchmark indices: TSLA, NVDA, META, AAPL, MSFT, GOOGL, AMZN, SPY, and QQQ. The study compares technical-indicator-only models with sentiment-enhanced models using Linear Regression, Random Forest, and XGBoost. Crucially, the analysis does not assume that sentiment will improve forecasting performance. Instead, it treats that claim as an empirical question to be tested.

## 1.3 Research Problem
The core problem addressed in this dissertation is the gap between optimistic claims in stock prediction literature and the more difficult reality of robust short-horizon forecasting. Many studies report gains from combining sentiment and technical indicators, yet it is often unclear whether those gains remain when models are evaluated against simple baselines, tested across multiple assets, and assessed using walk-forward validation rather than a single train-test split.

This issue is especially important in liquid equity markets, where next-day prediction is a demanding task and naive forecasts are often difficult to beat consistently. If sentiment and technical indicators do not provide meaningful incremental value under such conditions, then claims regarding their predictive usefulness should be interpreted more cautiously. Conversely, if improvements persist under stricter evaluation, then the case for sentiment-enhanced forecasting becomes stronger.

The dissertation therefore addresses not only a predictive problem, but also a methodological and interpretive one: how should the value of engineered technical and sentiment-derived features be judged in a noisy financial setting where overfitting is a constant risk?

## 1.4 Aim and Objectives
The aim of this dissertation is to evaluate whether technical indicators and news sentiment provide incremental predictive value for next-day stock price forecasting across selected US equities and benchmark indices under rigorous out-of-sample testing conditions.

To achieve this aim, the dissertation pursues the following objectives:

1. To construct a next-day stock price forecasting dataset using price-based variables, technical indicators, and aggregated daily news sentiment for nine selected US stocks and indices.
2. To compare the predictive performance of Linear Regression, Random Forest, and XGBoost models using technical indicators alone and using technical indicators combined with sentiment features.
3. To assess whether sentiment features add incremental predictive value beyond technical indicators under both standard train-test and walk-forward validation settings.
4. To evaluate model performance against simple baselines, including naive forecasting and buy-and-hold benchmarks.
5. To identify which features contribute most to model performance and examine whether raw price variables dominate engineered indicators and sentiment variables.
6. To critically analyse the limitations of sentiment-enhanced forecasting in the context of data quality, market efficiency, and model complexity.

## 1.5 Research Questions
The central research question guiding this dissertation is as follows:

**Do technical indicators and news sentiment provide incremental predictive value over simple baselines for next-day stock price forecasting across selected US stocks and indices?**

This main question is addressed through four sub-questions:

**RQ1.** How do Linear Regression, Random Forest, and XGBoost compare in forecasting next-day stock prices using technical indicators?

**RQ2.** Which technical indicators and price-based features contribute most to predictive performance?

**RQ3.** Does the inclusion of aggregated daily news sentiment improve predictive performance relative to technical-indicator-only models?

**RQ4.** How robust are the observed results under walk-forward validation and baseline comparison?

## 1.6 Hypotheses
The dissertation tests the following hypotheses:

**H1.** Technical-indicator-based machine learning models will produce lower forecast error than buy-and-hold benchmarks, but will not consistently outperform naive next-day forecasts.

**H2.** Linear Regression will demonstrate greater out-of-sample robustness than Random Forest and XGBoost under walk-forward validation.

**H3.** The inclusion of aggregated daily news sentiment will not produce substantial incremental predictive improvement over technical-indicator-only models under the current data coverage and aggregation design.

**H4.** Raw price-based variables will contribute more strongly to predictive performance than most engineered technical indicators and sentiment features.

These hypotheses are intentionally cautious. Rather than assuming that more complex models or richer feature sets will necessarily improve performance, they reflect the possibility that simple models may remain more robust in low-signal financial environments.

## 1.7 Significance of the Study
This dissertation is significant in three respects.

First, it contributes to ongoing debate about whether sentiment features genuinely improve stock-price forecasting, or whether their apparent usefulness is contingent on specific datasets and modelling conditions. This is relevant because sentiment-based prediction has received growing attention in machine learning and financial NLP research, yet its practical value remains uneven.

Second, the dissertation contributes methodologically by emphasising baseline comparison and walk-forward validation. In a field where overfitting and weak generalisation are common, this focus on robust evaluation is important in its own right.

Third, the study contributes to discussion of model complexity in financial prediction. If simpler models perform as well as or better than more flexible ensemble methods, then this has implications for both model selection and the interpretation of financial ML results more broadly.

The contribution of the dissertation therefore lies not in claiming a breakthrough forecasting system, but in providing a more disciplined assessment of what technical indicators and sentiment can, and cannot, contribute under realistic conditions.

## 1.8 Scope and Delimitations
The study focuses on next-day price forecasting for nine large-cap US stocks and benchmark indices. It is therefore limited in several ways.

First, the analysis uses daily data rather than intraday observations. This means that the study cannot assess very short-horizon market reactions or intra-day information dynamics.

Second, the sentiment dataset is constrained by the availability and quality of free-source news data. Sentiment coverage is uneven across assets and limited in temporal depth.

Third, the selected assets are concentrated in large-cap US technology equities together with two benchmark ETFs. Although this supports a coherent comparative design, it limits the extent to which the results can be generalised to smaller firms, other sectors, or non-US markets.

Fourth, the study focuses on three model classes—Linear Regression, Random Forest, and XGBoost—and does not attempt to exhaust the full range of deep learning or transformer-based forecasting approaches. This delimitation is intentional: the aim is comparative evaluation under manageable dissertation scope, not exhaustive model enumeration.

These delimitations are not incidental. They define the empirical setting within which the study’s claims should be interpreted.

## 1.9 Dissertation Structure
The remainder of the dissertation is organised as follows.

**Chapter 2** reviews the literature on stock-price forecasting, technical indicators, financial sentiment analysis, and model complexity in machine learning-based prediction. It identifies the research gap addressed by the dissertation.

**Chapter 3** explains the methodology, including data collection, variable construction, sentiment aggregation, model selection, feature design, and evaluation procedures.

**Chapter 4** presents the empirical results, including baseline comparison, standard model comparison, walk-forward validation, and feature-importance analysis.

**Chapter 5** discusses the findings in relation to prior literature, with particular attention to why Linear Regression performed robustly, why sentiment provided limited incremental value, and what these findings imply for financial forecasting research.

**Chapter 6** concludes the dissertation by summarising the principal findings, outlining the contribution of the study, acknowledging limitations, and suggesting directions for future research.

## 1.10 Chapter Summary
This chapter has introduced the dissertation by establishing the background, motivation, research problem, aim, objectives, questions, hypotheses, significance, and scope of the study. The central argument is that the value of technical indicators and sentiment features should not be assumed, but tested under robust out-of-sample conditions and against simple baselines. The next chapter situates this argument within the wider literature on financial forecasting and sentiment-enhanced machine learning.
