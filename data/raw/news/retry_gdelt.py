#!/usr/bin/env python3
"""
Retry GDELT with better rate limiting for failed stocks.
"""

import requests
import json
import os
import time

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

def query_gdelt(query, max_records=250):
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": query,
        "mode": "artlist",
        "maxrecords": max_records,
        "format": "json",
        "sort": "DateDesc"
    }
    
    for attempt in range(5):
        try:
            response = requests.get(url, params=params, timeout=60)
            
            if response.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
                
            if response.status_code == 200:
                data = response.json()
                return data.get('articles', [])
            else:
                print(f"    Error: {response.status_code}")
                return []
        except Exception as e:
            print(f"    Exception: {e}")
            time.sleep(10)
    
    return []

def parse_gdelt(articles):
    parsed = []
    seen = set()
    for a in articles:
        url = a.get('url', '')
        if url and url not in seen:
            seen.add(url)
            parsed.append({
                "title": a.get('title', ''),
                "publishedAt": a.get('seendate', ''),
                "source": a.get('domain', ''),
                "description": a.get('socialimage', ''),
                "url": url
            })
    return parsed

def main():
    print("Retrying with longer delays...")
    
    for ticker, company in STOCKS.items():
        print(f"\n{ticker}:")
        
        # Load existing
        output_file = os.path.join(OUTPUT_DIR, f"{ticker}_news.json")
        existing = []
        if os.path.exists(output_file):
            with open(output_file) as f:
                existing = json.load(f)
        
        existing_urls = {a['url'] for a in existing}
        
        queries = [
            f'{ticker} stock',
            f'{company} stock',
            f'{ticker} earnings',
            f'{ticker} news',
        ]
        
        new_articles = []
        
        for query in queries:
            print(f"  Query: {query}")
            articles = query_gdelt(query)
            parsed = parse_gdelt(articles)
            
            # Filter new ones
            for p in parsed:
                if p['url'] not in existing_urls:
                    new_articles.append(p)
                    existing_urls.add(p['url'])
            
            print(f"    -> {len(parsed)} found, {len(new_articles)} new")
            time.sleep(15)  # Longer delay between queries
        
        # Save combined
        combined = existing + new_articles
        with open(output_file, "w") as f:
            json.dump(combined, f, indent=2)
        
        print(f"  Total: {len(combined)} articles")

if __name__ == "__main__":
    main()