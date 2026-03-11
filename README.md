# Stock Price Prediction Using Machine Learning

## Master's Thesis - UEL DS-7010 Data Science Dissertation

### Overview

This project investigates the application of machine learning regression models to predict short-term stock price movements. The study compares multiple algorithms (Linear Regression, Random Forest, XGBoost) using technical indicators as features.

### Research Question

To what extent can machine learning regression models predict short-term stock price movements, and how do they compare to traditional technical analysis methods?

### Stocks Analyzed

1. **TSLA** (Tesla) - Volatile, growth stock
2. **NVDA** (NVIDIA) - Tech growth stock
3. **META** (Meta Platforms) - Tech, volatile
4. **AAPL** (Apple) - Blue-chip, stable
5. **MSFT** (Microsoft) - Blue-chip, stable

### Methodology

- **Data Source:** Yahoo Finance (yfinance)
- **Prediction Horizon:** 1 day ahead (next day's closing price)
- **Features:** Technical indicators (Moving Averages, RSI, MACD, Momentum)
- **Models:** Linear Regression, Random Forest, XGBoost
- **Evaluation Metrics:** RMSE, MAE, Directional Accuracy

### Project Structure

```
thesis-stock-prediction/
├── data/
│   ├── raw/           # Raw stock data from yfinance
│   └── processed/    # Cleaned data with features
├── notebooks/         # Jupyter notebooks for analysis
├── src/              # Python scripts
├── reports/          # Generated reports and visualizations
├── thesis/           # Thesis document (LaTeX/Word)
└── README.md         # This file
```

### Setup

```bash
# Create virtual environment
python -m venv thesis-env
source thesis-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Jupyter notebooks
jupyter notebook
```

### Timeline

- **Phase 1:** Topic & Research Design (Week 1)
- **Phase 2:** Literature Review (Weeks 2-3)
- **Phase 3:** Data Collection & Preprocessing (Weeks 4-5)
- **Phase 4:** Feature Engineering (Week 6)
- **Phase 5:** Model Development & Training (Weeks 7-8)
- **Phase 6:** Analysis & Results (Weeks 9-10)
- **Phase 7:** Writing - Findings (Weeks 11-12)
- **Phase 8:** Writing - Discussion (Weeks 13-14)
- **Phase 9:** Writing - Introduction (Weeks 15-16)
- **Phase 10:** Writing - Methodology (Weeks 17-18)
- **Phase 11:** Review, Edit, Formatting (Weeks 19-20)
- **Phase 12:** Final Polish & Submission Prep (Weeks 21-22)
- **Phase 13:** Final Submission (Weeks 23-24)

### Requirements

- Python 3.9+
- 10,000 words (+/- 10%)
- APA 7th Edition referencing
- Secondary data only

### Author

- **Student:** Moe
- **Institution:** University of East London
- **Course:** DS-7010 Data Science Dissertation

---
*Last Updated: 2026-03-11*