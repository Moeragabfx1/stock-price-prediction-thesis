#!/usr/bin/env python3
"""
Fetch historical news for stocks using NewsAPI.
Handles pagination, rate limits, and saves incrementally.
"""

import requests
import time
import json
import os
from datetime import datetime, timedelta

API_KEY = "87ed1a6a4649479a93cd27548b2ea124"
BASE_URL = "https://newsapi.org/v2/everything"

STOCKS = {
    "TSLA": "Tesla",
    "NVDA": "NVIDIA",
    "META": "Meta OR Facebook",
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "GOOGL": "Google OR Alphabet",
    "AMZN": "Amazon",
    "SPY": "S&P 500 ETF",
    "QQQ": "NASDAQ ETF"
}

OUTPUT_DIR = "/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/raw/news"

# Date range
START_DATE = "2020-01-01"
END_DATE = "2026-03-10"

def fetch_news_for_query(query, from_date, to_date, page=1, max_retries=5):
    """Fetch news for a specific query with retry logic."""
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 100,
        "page": page,
        "apiKey": API_KEY
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(BASE_URL, params=params, timeout=30)
            
            if response.status_code == 429:
                wait_time = 60 * (attempt + 1)
                print(f"  Rate limited. Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
                continue
                
            if response.status_code != 200:
                print(f"  Error {response.status_code}: {response.text}")
                return None
                
            return response.json()
            
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
    
    return None

def extract_articles(data):
    """Extract relevant fields from articles."""
    if not data or "articles" not in data:
        return [], 0
    
    articles = []
    for article in data["articles"]:
        articles.append({
            "title": article.get("title", ""),
            "publishedAt": article.get("publishedAt", ""),
            "source": article.get("source", {}).get("name", ""),
            "description": article.get("description", ""),
            "url": article.get("url", "")
        })
    
    total_results = data.get("totalResults", 0)
    return articles, total_results

def fetch_stock_news_yearly(ticker, company_name):
    """Fetch all news for a stock, year by year."""
    print(f"\n{'='*50}")
    print(f"Fetching news for {ticker} ({company_name})")
    print(f"{'='*50}")
    
    all_articles = []
    
    # Parse start and end years
    start_year = 2020
    end_year = 2026
    
    for year in range(start_year, end_year + 1):
        if year == 2026:
            from_date = f"{year}-01-01"
            to_date = "2026-03-10"
        else:
            from_date = f"{year}-01-01"
            to_date = f"{year}-12-31"
        
        query = f"{ticker} OR {company_name}"
        year_articles = []
        page = 1
        total_for_year = 0
        
        print(f"\n  {year}: ", end="", flush=True)
        
        while True:
            data = fetch_news_for_query(query, from_date, to_date, page)
            
            if data is None:
                break
            
            articles, total = extract_articles(data)
            year_articles.extend(articles)
            total_for_year = total
            
            print(f"p{page}({len(articles)})", end=" ", flush=True)
            
            # Check if there are more pages
            if len(year_articles) >= total or len(articles) == 0:
                break
                
            page += 1
            time.sleep(0.5)  # Small delay between pages
        
        print(f"-> {len(year_articles)} articles")
        all_articles.extend(year_articles)
    
    # Remove duplicates based on URL
    seen_urls = set()
    unique_articles = []
    for article in all_articles:
        if article["url"] and article["url"] not in seen_urls:
            seen_urls.add(article["url"])
            unique_articles.append(article)
    
    return unique_articles

def main():
    print(f"Starting news fetch from {START_DATE} to {END_DATE}")
    print(f"API Key: {API_KEY[:10]}...")
    
    results = {}
    
    for ticker, company_name in STOCKS.items():
        articles = fetch_stock_news_yearly(ticker, company_name)
        results[ticker] = articles
        
        # Save incrementally
        output_file = os.path.join(OUTPUT_DIR, f"{ticker}_news.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
        
        print(f"  Saved {len(articles)} articles to {output_file}")
        
        # Small delay between stocks
        time.sleep(2)
    
    # Summary
    print(f"\n{'='*50}")
    print("SUMMARY")
    print(f"{'='*50}")
    for ticker, articles in results.items():
        print(f"  {ticker}: {len(articles)} articles")
    
    print(f"\nTotal: {sum(len(a) for a in results.values())} articles")

if __name__ == "__main__":
    main()