#!/usr/bin/env python3
"""
Weekly Literature Search Script
Searches for relevant academic papers on stock prediction + sentiment + ML
"""
import subprocess
import json
from datetime import datetime

SEARCH_QUERIES = [
    "stock price prediction machine learning technical indicators",
    "sentiment analysis stock prediction BERT FinBERT",
    "XGBoost stock prediction financial markets",
    "random forest stock price prediction time series",
    "deep learning LSTM stock prediction returns",
    "financial sentiment analysis methodology",
    "stock market prediction hybrid models technical sentiment",
    "machine learning stock prediction feature engineering",
    "stock price prediction cross validation time series",
    "LLM GPT stock market sentiment prediction 2024"
]

def search_arxiv(query, max_results=5):
    """Search arXiv API for papers"""
    import urllib.parse
    import urllib.request
    
    base_url = "http://export.arxiv.org/api/query"
    params = f"search_query=all:{query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    
    try:
        url = f"{base_url}?{params}"
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode()
    except Exception as e:
        return f"Error: {e}"

def extract_papers(xml_data):
    """Extract paper info from arXiv XML"""
    papers = []
    import re
    
    # Extract entry blocks
    entries = re.findall(r'<entry>(.*?)</entry>', xml_data, re.DOTALL)
    
    for entry in entries:
        title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
        summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
        published = re.search(r'<published>(.*?)</published>', entry)
        arxiv_id = re.search(r'<id>http://arxiv.org/abs/(.*?)</id>', entry)
        
        if title and arxiv_id:
            papers.append({
                'title': title.group(1).strip().replace('\n', ' '),
                'id': arxiv_id.group(1),
                'published': published.group(1)[:10] if published else 'Unknown',
                'summary': summary.group(1).strip()[:300] if summary else ''
            })
    
    return papers

def main():
    print(f"=== Literature Search: {datetime.now().strftime('%Y-%m-%d')} ===\n")
    
    all_papers = []
    seen_ids = set()
    
    for query in SEARCH_QUERIES[:5]:  # Search top 5 queries
        print(f"Searching: {query}")
        xml = search_arxiv(query)
        papers = extract_papers(xml)
        
        for p in papers:
            if p['id'] not in seen_ids:
                seen_ids.add(p['id'])
                all_papers.append(p)
                print(f"  - {p['id']}: {p['title'][:60]}...")
    
    print(f"\n=== Found {len(all_papers)} unique papers ===")
    
    # Save to file
    output_file = "data/literature/weekly_findings.md"
    import os
    os.makedirs("data/literature", exist_ok=True)
    
    with open(output_file, 'a') as f:
        f.write(f"\n## Week of {datetime.now().strftime('%Y-%m-%d')}\n\n")
        for p in all_papers[:10]:
            f.write(f"### {p['id']}\n")
            f.write(f"**Title:** {p['title']}\n")
            f.write(f"**Published:** {p['published']}\n")
            f.write(f"**Summary:** {p['summary']}...\n\n")
    
    print(f"Saved to {output_file}")
    return all_papers

if __name__ == '__main__':
    main()