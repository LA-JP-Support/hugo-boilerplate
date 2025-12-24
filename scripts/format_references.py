#!/usr/bin/env python3
"""
Format References in Markdown files.
Convert Markdown links in References section to text-based bibliographic format or explicit URL format.
"""

import os
import argparse
import re
from pathlib import Path
import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_API_KEY")
# Using a cost-effective model for text formatting
MODEL = "claude-3-5-haiku-20241022"

PROMPT_TEMPLATE = """You are an expert technical editor. 
Reformat the following list of references according to these STRICT rules.

RULES:
1. Identify whether each item is an **Article/Report/Book/Video** or a **Service/Tool**.
2. Format accordingly:
   - **Article/Report/Book/Video**: 
     Format: [Index]. Author/Organization. (Year). Title. Source Name.
     * Constraint: REMOVE ALL HYPERLINKS. Text only.
     * If year is unknown, use (n.d.).
     * Maintain the original language (English or Japanese).
     * Examples: 
       1. IBM. (2024). What is Customer Support?. IBM Think Topics.
       2. Zendesk. (2025). カスタマーサポートとは. Zendesk Blog.
   
   - **Service/Tool**: 
     Format: [Index]. Name of Service. Description. URL: <URL>
     * Constraint: EXPLICITLY WRITE THE URL.
     * Example: 
       3. Help Scout. Help Desk Software. URL: https://www.helpscout.com/

3. Keep the original numbering if possible, or re-number sequentially starting from 1.
4. Return ONLY the formatted list. No intro/outro text.

INPUT REFERENCES:
{content}
"""

def process_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    
    # Robust regex to find References section
    # Matches "## References" or Japanese equivalents followed by content until the next "## " or end of file
    match = re.search(r'(## (?:References|Reference|参考文献|参考資料|Reference Links)\s*\n)(.*?)(?=\n## |\Z)', content, re.DOTALL)
    
    if not match:
        # Try case-insensitive for English
        match = re.search(r'(## (?:references|reference)\s*\n)(.*?)(?=\n## |\Z)', content, re.DOTALL | re.IGNORECASE)
        if not match:
            # print(f"⚪️ Skipping {file_path.name}: No '## References' section found.")
            return

    header = match.group(1)
    ref_content = match.group(2).strip()
    
    if not ref_content:
         # print(f"⚪️ Skipping {file_path.name}: Empty References section.")
         return

    # Check if there are markdown links to convert [text](url)
    # We want to process it if it has links like [Title](url)
    if not re.search(r'\[.*?\]\(.*?\)', ref_content):
        # print(f"⚪️ Skipping {file_path.name}: No markdown links found in References.")
        return

    print(f"🔄 Processing {file_path.name}...")
    
    if not API_KEY:
        print("❌ Error: ANTHROPIC_API_KEY not found in environment variables.")
        return

    client = anthropic.Anthropic(api_key=API_KEY)
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            temperature=0,
            messages=[{
                "role": "user",
                "content": PROMPT_TEMPLATE.format(content=ref_content)
            }]
        )
        
        new_ref_content = message.content[0].text.strip()
        
        # Replace the old section with new section
        # We use strict string replacement for safety
        original_section = f"{header}{ref_content}"
        new_section = f"{header}\n{new_ref_content}\n"
        
        # Calculate start/end based on match groups to avoid replacing wrong occurrences
        start_idx = match.start()
        end_idx = match.end()
        
        new_full_content = content[:start_idx] + new_section + content[end_idx:]
        
        file_path.write_text(new_full_content, encoding="utf-8")
        print(f"✅ Updated {file_path.name}")
        print("-" * 40)
        print(new_ref_content)
        print("-" * 40)
        
    except Exception as e:
        print(f"❌ Error processing {file_path.name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Format References in Markdown files.")
    parser.add_argument("path", help="File or directory path")
    args = parser.parse_args()
    
    path = Path(args.path)
    if not path.exists():
        print(f"Error: Path {path} does not exist.")
        return

    if path.is_file():
        process_file(path)
    elif path.is_dir():
        # Process all .md files in the directory
        for f in sorted(path.glob("**/*.md")):
            process_file(f)

if __name__ == "__main__":
    main()
