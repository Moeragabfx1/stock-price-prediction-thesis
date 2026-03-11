#!/usr/bin/env python3
"""
Sentiment Analysis for Stock News
Lightweight, reproducible pipeline using VADER with better text/date cleaning.
Generates daily aggregated sentiment scores for all tracked tickers.
"""

import json
import os
import re
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse

import pandas as pd
from tqdm import tqdm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

DATA_DIR = "/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/raw/news"
OUTPUT_DIR = "/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/processed"
STOCKS = ['TSLA', 'NVDA', 'META', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'SPY', 'QQQ']

os.makedirs(OUTPUT_DIR, exist_ok=True)
analyzer = SentimentIntensityAnalyzer()

# Small finance-oriented lexicon tweaks
analyzer.lexicon.update({
    'beat': 1.5,
    'beats': 1.7,
    'upgrade': 2.0,
    'bullish': 2.3,
    'outperform': 2.1,
    'miss': -1.8,
    'misses': -2.0,
    'downgrade': -2.3,
    'bearish': -2.3,
    'underperform': -2.1,
    'selloff': -2.4,
    'rally': 2.2,
    'surge': 2.1,
    'plunge': -2.5,
    'slump': -2.1,
    'profit warning': -2.4,
    'guidance cut': -2.1,
    'record high': 2.0,
})

JUNK_PATTERNS = [
    r'latest stock news & headlines',
    r'stock price, quote and news',
    r'stock price & overview',
    r'news today \| why did .* stock go down today',
    r'news headlines \| nasdaq',
]


def parse_date(value):
    """Parse multiple common date formats into YYYY-MM-DD."""
    if not value or str(value).strip() == "":
        return None
    value = str(value).strip()

    # GDELT format like 20260311T024500Z
    if re.match(r'^\d{8}T\d{6}Z$', value):
        return f"{value[:4]}-{value[4:6]}-{value[6:8]}"

    # Try RFC822 / RSS pubDate
    try:
        dt = parsedate_to_datetime(value)
        return dt.date().isoformat()
    except Exception:
        pass

    # Generic pandas parsing fallback
    try:
        dt = pd.to_datetime(value, utc=True, errors='coerce')
        if pd.notna(dt):
            return dt.date().isoformat()
    except Exception:
        pass

    return None


def is_junk_article(title, url):
    title_l = (title or '').strip().lower()
    if len(title_l) < 15:
        return True
    for pat in JUNK_PATTERNS:
        if re.search(pat, title_l):
            return True
    parsed = urlparse(url or '')
    domain = parsed.netloc.lower()
    # Drop obvious search redirect wrappers
    if 'duckduckgo.com' in domain and 'uddg=' in (url or ''):
        return True
    return False


def build_text(article):
    title = (article.get('title') or '').strip()
    desc = (article.get('description') or '').strip()
    # GDELT sometimes stores image urls in description; discard those
    if desc.startswith('http') and any(desc.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp']):
        desc = ''
    text = f"{title}. {desc}".strip('. ').strip()
    return text if text else title


def analyze_sentiment(text):
    if not text or not text.strip():
        return {'label': 'neutral', 'positive': 0.0, 'negative': 0.0, 'neutral': 1.0, 'compound': 0.0}

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    label = 'neutral'
    if compound >= 0.05:
        label = 'positive'
    elif compound <= -0.05:
        label = 'negative'

    return {
        'label': label,
        'positive': scores['pos'],
        'negative': scores['neg'],
        'neutral': scores['neu'],
        'compound': compound,
    }


def process_stock(stock):
    print(f"\nProcessing {stock}...")
    input_path = f"{DATA_DIR}/{stock}_news.json"
    if not os.path.exists(input_path):
        print(f"  No news file found for {stock}, writing empty neutral file")
        daily = pd.DataFrame(columns=['date', 'positive_score', 'negative_score', 'neutral_score', 'compound_score', 'article_count'])
        daily.to_csv(f"{OUTPUT_DIR}/{stock}_sentiment.csv", index=False)
        return 0, 0, 0

    with open(input_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    print(f"  Loaded {len(articles)} raw articles")

    results = []
    filtered = 0
    undated = 0

    for article in tqdm(articles, desc="  Scoring"):
        title = article.get('title', '')
        url = article.get('url', '')
        if is_junk_article(title, url):
            filtered += 1
            continue

        text = build_text(article)
        if not text or len(text.strip()) < 10:
            filtered += 1
            continue

        date = parse_date(article.get('publishedAt', ''))
        if date is None:
            undated += 1
            continue  # drop undated items rather than poisoning timeline

        sentiment = analyze_sentiment(text)
        results.append({
            'date': date,
            'title': title,
            'positive': sentiment['positive'],
            'negative': sentiment['negative'],
            'neutral': sentiment['neutral'],
            'compound': sentiment['compound'],
            'label': sentiment['label'],
        })

    if results:
        df = pd.DataFrame(results)
        daily = df.groupby('date').agg({
            'positive': 'mean',
            'negative': 'mean',
            'neutral': 'mean',
            'compound': 'mean',
            'title': 'count'
        }).reset_index()
        daily.columns = ['date', 'positive_score', 'negative_score', 'neutral_score', 'compound_score', 'article_count']
        daily = daily.sort_values('date')
    else:
        daily = pd.DataFrame(columns=['date', 'positive_score', 'negative_score', 'neutral_score', 'compound_score', 'article_count'])

    output_path = f"{OUTPUT_DIR}/{stock}_sentiment.csv"
    daily.to_csv(output_path, index=False)
    print(f"  Saved {output_path} ({len(daily)} days)")
    print(f"  Kept: {len(results)} | Filtered: {filtered} | Undated dropped: {undated}")
    return len(articles), filtered, undated


def main():
    total_articles = 0
    total_filtered = 0
    total_undated = 0

    for stock in STOCKS:
        articles, filtered, undated = process_stock(stock)
        total_articles += articles
        total_filtered += filtered
        total_undated += undated

    print(f"\n{'='*50}")
    print("COMPLETED")
    print(f"Total raw articles: {total_articles}")
    print(f"Filtered junk: {total_filtered}")
    print(f"Dropped undated: {total_undated}")
    print(f"Output files saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
