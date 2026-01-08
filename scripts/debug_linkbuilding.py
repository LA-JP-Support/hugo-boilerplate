
import sys
import os
import re
from bs4 import BeautifulSoup, NavigableString
from pathlib import Path
import json

# Add scripts directory to path to import linkbuilding
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from linkbuilding import LinkBuilder, Keyword, LinkConfig

def main():
    # Mock keywords
    keywords_data = [
        {"Keyword": "検索拡張生成", "URL": "/glossary/rag/", "Title": "RAG definition"},
        {"Keyword": "RAG", "URL": "/glossary/rag/", "Title": "RAG definition"},
        {"Keyword": "キャッシュ拡張生成", "URL": "/glossary/cag/", "Title": "CAG definition"},
        {"Keyword": "CAG", "URL": "/glossary/cag/", "Title": "CAG definition"},
        {"Keyword": "シナリオ", "URL": "/glossary/scenario/", "Title": "Scenario"},
        {"Keyword": "機械学習", "URL": "/glossary/ml/", "Title": "ML"},
        {"Keyword": "人工知能", "URL": "/glossary/ai/", "Title": "AI"},
    ]
    
    keywords = []
    for k in keywords_data:
        keywords.append(Keyword(
            keyword=k["Keyword"],
            url=k["URL"],
            title=k["Title"],
            priority=10,
            exact_match=False
        ))
    
    # Configure LinkBuilder
    config = LinkConfig(
        max_replacements_per_page=100,
        max_replacements_per_paragraph=10,
        max_replacements_per_keyword=10,
        max_replacements_per_url=10,
        max_replacements_per_keyword_url=10,
        min_chars_between_links=0,  # Set to 0 for testing dense links
        min_paragraph_length=30      # Restore standard length check
    )
    
    builder = LinkBuilder(keywords, config, language='JA')
    
    # Test cases
    test_htmls = [
        '<p><strong>検索拡張生成(RAG)とキャッシュ拡張生成(CAG)</strong></p>',
        '<p><strong>これはCAGシナリオです。</strong></p>',
        '<p><strong>これは明らかにRAGシナリオです。</strong></p>',
        '<p><strong>機械学習(ML)</strong>は<strong>人工知能(AI)</strong></p>'
    ]
    
    print("--- Debugging LinkBuilder ---")
    
    for html in test_htmls:
        print(f"\nInput:  {html}")
        soup = BeautifulSoup(html, 'html.parser')
        builder.current_file = "test.html"
        builder.reset_page_counters()
        
        # Manually process the soup to mimic process_file
        # We need to find the strong tags and process them
        for element in soup.find_all(['p', 'div', 'li']):
             builder.process_element(element)
             
        print(f"Output: {str(soup)}")

if __name__ == "__main__":
    main()
