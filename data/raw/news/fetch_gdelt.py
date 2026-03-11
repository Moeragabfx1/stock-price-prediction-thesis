#!/usr/bin/env python3
"""
Fetch news from GDELT - Global Database of Events, Language, and Tone.
GDELT has historical data going back decades and is free.
"""

import requests
import json
import os
import time
from datetime import datetime, timedelta

OUTPUT_DIR = "/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/raw/news"

STOCKS = {
    "TSLA": "Tesla",
    "NVDA": "Nvidia",
    "META": "Meta Facebook",
    "AAPL": "Apple Inc",
    "MSFT": "Microsoft",
    "GOOGL": "Google Alphabet",
    "AMZN": "Amazon",
    "SPY": "S&P 500",
    "QQQ": "NASDAQ"
}

def query_gdelt(query, mode="artlist", max_records=250):
    """
    Query GDELT API.
    mode can be: artlist (article list), tlartlist (timeline), geo (geographic)
    """
    base_url = "https://api.gdeltproject.org/api/v2"
    
    url = f"{base_url}/doc/doc"
    params = {
        "query": query,
        "mode": mode,
        "maxrecords": max_records,
        "format": "json",
        "sort": "DateDesc"
    }
    
    try:
        response = requests.get(url, params=params, timeout=60)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('articles', [])
        else:
            print(f"  GDELT error: {response.status_code}")
            return []
    except Exception as e:
        print(f"  GDELT exception: {e}")
        return []

def parse_gdelt_articles(articles, domain_filter=None):
    """Parse GDELT articles into our format."""
    parsed = []
    seen_urls = set()
    
    for article in articles:
        url = article.get('url', '')
        if not url or url in seen_urls:
            continue
        
        # Optionally filter by domain
        if domain_filter:
            if not any(d in url.lower() for d in domain_filter):
                continue
        
        seen_urls.add(url)
        parsed.append({
            "title": article.get('title', ''),
            "publishedAt": article.get('seendate', ''),
            "source": article.get('domain', ''),
            "description": article.get('socialimage', ''),  # Use social image as proxy
            "url": url
        })
    
    return parsed

def fetch_stock_gdelt(ticker, company_name):
    """Fetch news for a stock using GDELT."""
    print(f"\n{ticker} ({company_name}):")
    
    all_articles = []
    
    # Try multiple query variations
    queries = [
        f'{ticker} stock',
        f'{company_name} stock market',
        f'{ticker} earnings',
    ]
    
    domain_filter = ['reuters', 'bloomberg', 'cnbc', 'wsj', 'ft.com', 'marketwatch', 
                    'seekingalpha', 'investing', 'yahoo.com/finance', 'finance.yahoo',
                    'techcrunch', 'theverge', 'wired', 'engadget', 'arstechnica']
    
    for query in queries:
        print(f"  Query: {query}")
        articles = query_gdelt(query)
        
        if articles:
            parsed = parse_gdelt_articles(articles, domain_filter)
            print(f"    -> {len(parsed)} articles")
            all_articles.extend(parsed)
        else:
            print(f"    -> 0 articles")
        
        time.sleep(1)
    
    # Dedupe
    seen = set()
    unique = []
    for a in all_articles:
        if a['url'] not in seen:
            seen.add(a['url'])
            unique.append(a)
    
    return unique

def main():
    print("Fetching news via GDELT (free historical database)")
    print("GDELT updates every 15 minutes with global news")
    
    results = {}
    
    for ticker, company_name in STOCKS.items():
        articles = fetch_stock_gdelt(ticker, company_name)
        results[ticker] = articles
        
        # Save
        output_file = os.path.join(OUTPUT_DIR, f"{ticker}_news.json")
        
        # Load existing and merge if any
        existing = []
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                existing = json.load(f)
        
        # Combine and dedupe
        combined = existing + articles
        seen = set()
        unique = []
        for a in combined:
            if a['url'] not in seen:
                seen.add(a['url'])
                unique.append(a)
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(unique, f, indent=2, ensure_ascii=False)
        
        print(f"  Total saved: {len(unique)} articles")
    
    print(f"\n{'='*50}")
    print("SUMMARY")
    print(f"{'='*50}")
    for ticker, articles in results.items():
        print(f"  {ticker}: {len(articles)} articles")
    print(f"\nTotal new: {sum(len(a) for a in results.values())} articles")

if __name__ == "__main__":
    main()