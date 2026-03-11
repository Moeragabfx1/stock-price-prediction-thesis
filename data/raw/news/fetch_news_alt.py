#!/usr/bin/env python3
"""
Fetch historical news from Yahoo Finance.
Yahoo Finance has no date restrictions for news.
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import time
from datetime import datetime, timedelta
import re

OUTPUT_DIR = "/Users/moefx/.openclaw/workspace/thesis-stock-prediction/data/raw/news"

STOCKS = {
    "TSLA": "TSLA",
    "NVDA": "NVDA", 
    "META": "META",
    "AAPL": "AAPL",
    "MSFT": "MSFT",
    "GOOGL": "GOOGL",
    "AMZN": "AMZN",
    "SPY": "SPY",
    "QQQ": "QQQ"
}

def fetch_yahoo_news(ticker, max_pages=20):
    """Fetch news from Yahoo Finance RSS feed and search."""
    articles = []
    seen_urls = set()
    
    # Method 1: RSS feed
    rss_url = f"https://finance.yahoo.com/rss/headline?s={ticker}"
    
    try:
        response = requests.get(rss_url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'xml')
            items = soup.find_all('item')
            
            for item in items:
                link = item.find('link')
                if link and link.text and link.text not in seen_urls:
                    seen_urls.add(link.text)
                    articles.append({
                        "title": item.find('title').text if item.find('title') else "",
                        "publishedAt": item.find('pubDate').text if item.find('pubDate') else "",
                        "source": "Yahoo Finance",
                        "description": item.find('description').text if item.find('description') else "",
                        "url": link.text
                    })
    except Exception as e:
        print(f"  RSS error: {e}")
    
    print(f"  RSS feed: {len(articles)} articles")
    
    # Method 2: Yahoo Finance news page (more comprehensive)
    news_url = f"https://finance.yahoo.com/quote/{ticker}/news"
    
    try:
        response = requests.get(news_url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find news articles - Yahoo uses various selectors
            article_links = soup.find_all('a', href=re.compile(r'/news/'))
            
            for link in article_links:
                href = link.get('href', '')
                if href and 'yahoo.com' in href and href not in seen_urls:
                    seen_urls.add(href)
                    parent = link.find_parent('div')
                    title = link.text.strip()
                    
                    if title and len(title) > 10:  # Filter out empty/short
                        articles.append({
                            "title": title,
                            "publishedAt": "",
                            "source": "Yahoo Finance",
                            "description": "",
                            "url": href if href.startswith('http') else f"https://finance.yahoo.com{href}"
                        })
    except Exception as e:
        print(f"  News page error: {e}")
    
    # Dedupe
    unique_articles = []
    seen = set()
    for a in articles:
        if a['url'] not in seen:
            seen.add(a['url'])
            unique_articles.append(a)
    
    return unique_articles

def fetch_via_search(ticker, company_name):
    """Try to get news via web search and scraping."""
    articles = []
    seen_urls = set()
    
    # Use DuckDuckGo news search (no API key needed)
    search_url = f"https://html.duckduckgo.com/html/?q={ticker}+{company_name}+stock+news"
    
    try:
        response = requests.get(search_url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('a', class_='result__a')
            
            for r in results:
                href = r.get('href', '')
                title = r.text.strip()
                
                # Only include if it looks like news
                if title and href and href not in seen_urls:
                    # Filter for news sources
                    news_indicators = ['news', 'article', 'report', 'update', 'earnings', 'stock', 'market']
                    if any(ind in title.lower() for ind in news_indicators):
                        seen_urls.add(href)
                        articles.append({
                            "title": title,
                            "publishedAt": "",
                            "source": "Web Search",
                            "description": "",
                            "url": href
                        })
    except Exception as e:
        print(f"  Search error: {e}")
    
    return articles

def main():
    print("Fetching news using alternative methods...")
    print("Note: Yahoo Finance RSS is limited to recent articles")
    
    results = {}
    
    for ticker, company_name in STOCKS.items():
        print(f"\n{ticker}:")
        
        # Method 1: Yahoo RSS
        articles = fetch_yahoo_news(ticker)
        
        # Method 2: Try search
        search_articles = fetch_via_search(ticker, company_name)
        
        # Combine
        all_articles = articles + search_articles
        
        # Dedupe by URL
        seen = set()
        unique = []
        for a in all_articles:
            if a['url'] not in seen:
                seen.add(a['url'])
                unique.append(a)
        
        results[ticker] = unique
        
        # Save
        output_file = os.path.join(OUTPUT_DIR, f"{ticker}_news.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(unique, f, indent=2, ensure_ascii=False)
        
        print(f"  Total: {len(unique)} unique articles")
    
    print(f"\n{'='*50}")
    print("SUMMARY")
    print(f"{'='*50}")
    for ticker, articles in results.items():
        print(f"  {ticker}: {len(articles)} articles")
    print(f"\nTotal: {sum(len(a) for a in results.values())} articles")

if __name__ == "__main__":
    main()