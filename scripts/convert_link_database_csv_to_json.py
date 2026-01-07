#!/usr/bin/env python3
"""
Convert link_database CSV to linkbuilding JSON format.

This script converts databases/link_database_*.csv files into
data/linkbuilding/*_automatic.json format compatible with linkbuilding.py.

Usage:
    python scripts/convert_link_database_csv_to_json.py --input databases/link_database_ja.csv --output data/linkbuilding/ja_automatic.json
    python scripts/convert_link_database_csv_to_json.py --language ja  # Auto-detect paths
    python scripts/convert_link_database_csv_to_json.py --language en  # Auto-detect paths
"""

import csv
import json
import argparse
from pathlib import Path
from typing import List, Dict


def convert_csv_to_json(csv_path: Path, output_path: Path) -> int:
    """
    Convert link_database CSV to linkbuilding JSON format.
    
    CSV format:
        keyword,normalized,title,url,description,priority,variation_type,exact_match
    
    JSON format:
        [
            {
                "Keyword": "...",
                "URL": "...",
                "Title": "...",
                "Exact": true/false,
                "Priority": 1000
            },
            ...
        ]
    
    Returns:
        Number of entries converted
    """
    entries: List[Dict] = []
    
    with csv_path.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keyword = row.get('keyword', '').strip()
            url = row.get('url', '').strip()
            title = row.get('title', '').strip()
            exact_match = row.get('exact_match', 'false').strip().lower() == 'true'
            priority = int(row.get('priority', '1000'))
            
            if not keyword or not url:
                continue
            
            entry = {
                "Keyword": keyword,
                "URL": url,
                "Title": title or keyword,
                "Exact": exact_match,
                "Priority": priority
            }
            entries.append(entry)
    
    # Write JSON output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    
    return len(entries)


def main():
    parser = argparse.ArgumentParser(
        description='Convert link_database CSV to linkbuilding JSON format'
    )
    parser.add_argument('-i', '--input', type=str,
                       help='Input CSV file path (e.g., databases/link_database_ja.csv)')
    parser.add_argument('-o', '--output', type=str,
                       help='Output JSON file path (e.g., data/linkbuilding/ja_automatic.json)')
    parser.add_argument('-l', '--language', type=str,
                       help='Language code (e.g., ja, en) - auto-detects input/output paths')
    parser.add_argument('--overwrite', action='store_true',
                       help='Overwrite existing output file without prompting')
    
    args = parser.parse_args()
    
    # Determine input and output paths
    if args.language:
        input_path = Path(f'databases/link_database_{args.language}.csv')
        output_path = Path(f'data/linkbuilding/{args.language}_automatic.json')
    elif args.input and args.output:
        input_path = Path(args.input)
        output_path = Path(args.output)
    else:
        parser.error('Either --language or both --input and --output must be provided')
    
    # Validate input file exists
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    
    # Check if output exists
    if output_path.exists() and not args.overwrite:
        print(f"Warning: Output file already exists: {output_path}")
        response = input("Overwrite? [y/N]: ").strip().lower()
        if response not in ('y', 'yes'):
            print("Aborted.")
            return 0
    
    # Convert
    print(f"Converting: {input_path} -> {output_path}")
    count = convert_csv_to_json(input_path, output_path)
    print(f"✓ Converted {count} entries")
    print(f"✓ Output written to: {output_path}")
    
    return 0


if __name__ == '__main__':
    exit(main())
