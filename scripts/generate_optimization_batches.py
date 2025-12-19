#!/usr/bin/env python3
"""
Generate batch lists for glossary optimization
全記事を5記事ずつのバッチに分割
"""

import os
from pathlib import Path

GLOSSARY_EN = Path("/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary")

# 除外するファイル
EXCLUDE = [
    "_index.md",
    "AI-chatbot.md",  # 既に最適化済み
    "RAG.md",         # 既に最適化済み
    "LiveAgent.md",   # 既に最適化済み
]

# -OLDファイルも除外
def should_process(filename):
    if filename in EXCLUDE:
        return False
    if filename.endswith("-OLD.md"):
        return False
    if filename.endswith("-OPTIMIZED.md"):
        return False
    if filename.endswith("-REVISED.md"):
        return False
    return filename.endswith(".md")

# ファイルリスト取得
files = sorted([f.name for f in GLOSSARY_EN.glob("*.md") if should_process(f.name)])

# バッチに分割
batch_size = 5
batches = [files[i:i+batch_size] for i in range(0, len(files), batch_size)]

# 出力
print(f"# Glossary Optimization Batches")
print(f"# Total files: {len(files)}")
print(f"# Total batches: {len(batches)}")
print()

for i, batch in enumerate(batches, 1):
    print(f"## Batch {i}")
    for file in batch:
        print(f"- {file}")
    print()
