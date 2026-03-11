# Literature Review: LLM-Enhanced Sentiment + Technical Indicators for Stock Price Prediction

## Chapter 2: Literature Review

### 2.1 Introduction

Stock price prediction has been a central research topic in financial markets for decades. Traditional approaches relied heavily on fundamental analysis (examining financial statements, earnings, and economic indicators) and technical analysis (using historical price patterns and indicators). However, the emergence of machine learning (ML) and deep learning (DL) has revolutionized this field, enabling researchers to process vast amounts of data and identify complex patterns that traditional methods miss.

This literature review examines the current state of research in using Large Language Models (LLMs) for financial sentiment analysis combined with technical indicators for stock price prediction. We analyze key papers from 2023-2025, identify methodological approaches, and highlight gaps that this thesis aims to address.

---

### 2.2 Machine Learning in Financial Prediction

The application of machine learning to stock market prediction has grown exponentially in recent years. Various approaches have been explored, ranging from traditional ML algorithms like Random Forest and XGBoost to deep learning models such as LSTM (Long Short-Term Memory) networks and Transformers.

**Key Finding from Literature:** Research by Patel et al. (2024) evaluated Random Forest models enhanced with 13 technical indicators (Bollinger Bands, EMA, Fibonacci retracement) for high-frequency stock prediction using minute-level SPY data. Their findings revealed that technical indicators "struggled with out-of-sample generalization" - primary price features consistently outperformed technical indicators, and significant overfitting challenges were observed (arXiv:2412.15448v1).

This finding is critical for our thesis as it suggests that while technical indicators are widely used in practice, their predictive power may be limited when used in isolation. This supports our research question: can combining sentiment analysis with technical indicators overcome these limitations?

---

### 2.3 Sentiment Analysis in Finance

Financial sentiment analysis involves extracting subjective information from news articles, social media, and other textual sources to gauge market sentiment. The introduction of FinBERT (a BERT model pre-trained on financial text) has significantly improved sentiment classification accuracy in the financial domain.

**Key Paper 1: Financial sentiment analysis using FinBERT (2023)**
- Authors: Research team (arXiv:2306.02136)
- Methodology: Combined FinBERT for sentiment analysis with LSTM networks to predict stock market movements
- Data: Stock market news datasets
- Models: FinBERT-LSTM, compared against standard BERT, standalone LSTM, and ARIMA
- Results: Incorporating sentiment analysis "significantly enhances the model's ability to anticipate market fluctuations"
- Relevance: **HIGH** - Direct methodology we can replicate

---

### 2.4 Combining Sentiment with Technical Indicators

A growing body of research explores combining sentiment analysis with traditional technical indicators. This hybrid approach aims to leverage the strengths of both: technical indicators capture historical price patterns while sentiment analysis captures market mood from news and social media.

**Key Paper 2: Predicting Stock Prices with FinBERT-LSTM (2024)**
- Authors: Research team (arXiv:2407.16150)
- Methodology: Used FinBERT for extracting sentiment from financial news (market/industry/stock categories), combined with previous week's stock prices, fed into LSTM
- Data: NASDAQ-100 index + Benzinga news articles
- Models: FinBERT-LSTM, LSTM, DNN
- Results: FinBERT-LSTM performed best, followed by LSTM, then DNN - evaluated using MAE, MAPE, Accuracy
- Relevance: **HIGH** - Our primary reference methodology

---

### 2.5 The Role of Model Complexity

An important finding in recent literature challenges the assumption that more complex models always perform better. This has significant implications for thesis methodology.

**Key Paper 3: Innovative Sentiment Analysis Using FinBERT, GPT-4 and Logistic Regression (2024)**
- Authors: Research team (arXiv:2412.06837)
- Methodology: Compared three approaches for sentiment analysis and stock index prediction using financial news
- Data: Financial news + Nigerian Exchange (NGX) All-Share Index
- Models: FinBERT, GPT-4 (predefined approach), Logistic Regression
- Results: **Logistic Regression outperformed with 81.83% accuracy and 89.76% ROC AUC**. GPT-4 got 54.19% accuracy. FinBERT was "resource-demanding with moderate performance"
- Relevance: **HIGH** - Proves simpler models can beat complex LLMs

This finding is particularly valuable for our thesis as it provides evidence that we can achieve strong results with more interpretable and computationally efficient models.

---

### 2.6 Multi-Stock and Multi-Sector Approaches

Several studies have explored predicting stock prices across multiple stocks and sectors, which aligns with our thesis approach of using 5 major tech stocks.

**Key Paper 4: Neural Network Fundamental+Technical+Sentiment (2025)**
- Authors: Research team (Computational Economics)
- Methodology: Uses Multilayer Perceptron (MLP) neural network combining fundamental indicators, technical indicators, and market sentiment to forecast stock prices across 33 S&P 500 stocks across 11 sectors
- Data: 33 representative S&P 500 stocks, fundamental indicators, technical indicators, market sentiment data
- Models: Multilayer Perceptron (MLP) artificial neural network
- Results: **7 out of 11 sectors achieved highest coefficient of determination (R²) in models that include market sentiment**, demonstrating sentiment adds predictive value to existing models
- Relevance: **HIGH** - Multi-stock approach similar to our thesis

---

### 2.7 Fusion-Based Approaches

**Key Paper 5: Fusion of Technical Indicators and Sentiment Analysis in Hybrid Deep Learning (IEEE 2024)**
- Authors: Research team (IEEE)
- Methodology: Combines technical indicators (RSI, MACD, moving averages) with sentiment scores from Twitter/social media using a hybrid deep learning framework to predict stock price movements
- Data: Stock price data + Twitter sentiment data
- Models: Deep learning models (LSTM, CNN, or hybrid architecture combining technical and sentiment features)
- Results: Improved prediction accuracy compared to using either technical or sentiment alone
- Relevance: **HIGH** - Direct fusion methodology

---

### 2.8 Summary and Research Gap

Based on the literature review, the following key insights emerge:

1. **Sentiment analysis adds value**: Combining sentiment with traditional features improves prediction accuracy across multiple studies
2. **Simpler models can outperform**: Logistic Regression achieved 81.83% accuracy, outperforming FinBERT and GPT-4
3. **Technical indicators have limitations**: Studies show overfitting issues with technical indicators alone
4. **Multi-stock approaches are viable**: Studies across 33 stocks and 11 sectors show consistent value from sentiment
5. **Hybrid fusion works**: Combining technical and sentiment features outperforms either alone

**Research Gap:** While previous studies have shown the value of combining sentiment and technical indicators, there is limited research comparing:
- The incremental value of adding sentiment to technical-indicator-only models
- Different model complexities (LogReg vs XGBoost vs LSTM) when using the same feature set
- Multiple stocks from the same sector (tech stocks) to assess generalization

This thesis aims to address these gaps by systematically comparing models with and without sentiment features across 9 major stocks and indices (TSLA, NVDA, META, AAPL, MSFT, GOOGL, AMZN, SPY, QQQ).

---

### References

1. Financial sentiment analysis using FinBERT with application in predicting stock movement (2023). arXiv:2306.02136.

2. Predicting Stock Prices with FinBERT-LSTM: Integrating News Sentiment Analysis (2024). arXiv:2407.16150.

3. Innovative Sentiment Analysis and Prediction of Stock Price Using FinBERT, GPT-4 and Logistic Regression (2024). arXiv:2412.06837.

4. Stock Market Forecasting Using a Neural Network Through Fundamental, Technical Indicators and Market Sentiment Analysis (2025). Computational Economics.

5. Fusion of Technical Indicators and Sentiment Analysis in a Hybrid Framework of Deep Learning Models for Stock Price Movement Prediction (2024). IEEE.

6. Assessing the Impact of Technical Indicators on Machine Learning Models for Stock Price Prediction (2024). arXiv:2412.15448v1.

7. FinGPT: Enhancing Sentiment-Based Stock Movement Prediction with Dissemination-Aware and Context-Enriched LLMs (2024). arXiv:2412.10823.

8. Enhancing Trading Performance Through Sentiment Analysis with Large Language Models: Evidence from the S&P 500 (2025). arXiv:2507.09739.