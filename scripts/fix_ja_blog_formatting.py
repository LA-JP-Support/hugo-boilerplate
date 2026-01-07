#!/usr/bin/env python3
"""
日本語ブログ記事の修正スクリプト
1. 太字の助詞問題を修正（**単語の** → **単語**の）
2. 英語版から内部リンクのマッピングを作成して日本語版に適用
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple

# 日本語の助詞リスト
PARTICLES = ['の', 'が', 'を', 'に', 'へ', 'と', 'から', 'まで', 'より', 'で', 'や', 'は']

def fix_bold_particles(content: str) -> str:
    """
    太字の中に助詞が含まれている場合、助詞を太字の外に出す
    例: **Googleの** → **Google**の
    """
    fixed_content = content
    
    for particle in PARTICLES:
        # **単語助詞** のパターンを **単語**助詞 に修正
        pattern = r'\*\*([^\*]+?)(' + re.escape(particle) + r')\*\*'
        replacement = r'**\1**\2'
        fixed_content = re.sub(pattern, replacement, fixed_content)
    
    return fixed_content

def extract_internal_links_from_en(en_file: Path) -> Dict[str, str]:
    """
    英語版ファイルから内部リンクを抽出
    返り値: {表示テキスト: リンクURL}
    """
    if not en_file.exists():
        return {}
    
    content = en_file.read_text(encoding='utf-8')
    links = {}
    
    # [text](/en/glossary/term/) 形式のリンクを抽出
    pattern = r'\[([^\]]+?)\]\((/en/glossary/[^\)]+?/)\)'
    matches = re.findall(pattern, content)
    
    for text, url in matches:
        # 英語のテキストをキーとして保存
        links[text] = url
    
    return links

def create_term_mapping() -> Dict[str, Tuple[str, str]]:
    """
    英語用語から日本語用語へのマッピングを作成
    返り値: {英語用語: (日本語用語, glossary_url)}
    """
    mapping = {
        'ChatGPT': ('ChatGPT', '/en/glossary/ChatGPT/'),
        'neural networks': ('ニューラルネットワーク', '/en/glossary/neural-networks/'),
        'token': ('トークン', '/en/glossary/Token/'),
        'Token': ('トークン', '/en/glossary/Token/'),
        'pre-training': ('事前トレーニング', '/en/glossary/Pre-Training/'),
        'Pre-Training': ('事前トレーニング', '/en/glossary/Pre-Training/'),
        'computational resources': ('計算リソース', '/en/glossary/computational-resources/'),
        'GPT': ('GPT', '/en/glossary/GPT/'),
        'knowledge base': ('ナレッジベース', '/en/glossary/knowledge-base/'),
        'Google': ('Google', '/en/glossary/Google/'),
        'Gemini': ('Gemini', '/en/glossary/Gemini/'),
        'Microsoft': ('Microsoft', '/en/glossary/Microsoft/'),
        'Meta': ('Meta', '/en/glossary/Meta/'),
        'Anthropic': ('Anthropic', '/en/glossary/Anthropic/'),
        'OpenAI': ('OpenAI', '/en/glossary/OpenAI/'),
        'Claude': ('Claude', '/en/glossary/Claude/'),
        'Chatbot': ('チャットボット', '/en/glossary/Chatbot/'),
        'Tokenization': ('トークン化', '/en/glossary/Tokenization/'),
        'tokenization': ('トークン化', '/en/glossary/Tokenization/'),
        'Conversation-History': ('会話履歴', '/en/glossary/Conversation-History/'),
        'conversation history': ('会話履歴', '/en/glossary/Conversation-History/'),
        'Text-Generation': ('テキスト生成', '/en/glossary/Text-Generation/'),
        'text generation': ('テキスト生成', '/en/glossary/Text-Generation/'),
        'hallucination': ('幻覚', '/en/glossary/hallucination/'),
        'prompts': ('プロンプト', '/en/glossary/prompts/'),
    }
    
    return mapping

def add_internal_links_to_ja(content: str, term_mapping: Dict[str, Tuple[str, str]]) -> str:
    """
    日本語コンテンツに内部リンクを追加
    既存のリンク、HTML タグ、コードブロック内は除外
    """
    # コードブロックとインラインコードを一時的に保護
    code_blocks = []
    inline_codes = []
    html_tags = []
    
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"___CODE_BLOCK_{len(code_blocks)-1}___"
    
    def save_inline_code(match):
        inline_codes.append(match.group(0))
        return f"___INLINE_CODE_{len(inline_codes)-1}___"
    
    def save_html_tag(match):
        html_tags.append(match.group(0))
        return f"___HTML_TAG_{len(html_tags)-1}___"
    
    # コードブロックを保護
    content = re.sub(r'```[\s\S]*?```', save_code_block, content)
    # インラインコードを保護
    content = re.sub(r'`[^`]+`', save_inline_code, content)
    # HTMLタグを保護（YouTubeのiframeなど）
    content = re.sub(r'<[^>]+>', save_html_tag, content)
    content = re.sub(r'\{\{<.*?>\}\}', save_html_tag, content)
    
    # 各用語についてリンクを追加
    for en_term, (ja_term, url) in term_mapping.items():
        # 太字の中の用語を処理 **用語** → **[用語](url)**
        pattern_bold = r'\*\*(' + re.escape(ja_term) + r')\*\*'
        
        def replace_bold(match):
            return f'**[{match.group(1)}]({url})**'
        
        content = re.sub(pattern_bold, replace_bold, content)
        
        # 通常のテキスト中の用語を処理（最初の出現のみ）
        # 既にリンクになっていない、かつHTMLタグ内でない箇所
        if f'[{ja_term}]' not in content:
            # 最初の出現を探してリンク化
            pattern_plain = r'(?<!\[)(?<!\*)(?<!\*\*)(' + re.escape(ja_term) + r')(?!\]|</|>|\*)'
            content = re.sub(pattern_plain, f'[{ja_term}]({url})', content, count=1)
    
    # 保護した要素を復元
    for i, code in enumerate(code_blocks):
        content = content.replace(f"___CODE_BLOCK_{i}___", code)
    for i, code in enumerate(inline_codes):
        content = content.replace(f"___INLINE_CODE_{i}___", code)
    for i, tag in enumerate(html_tags):
        content = content.replace(f"___HTML_TAG_{i}___", tag)
    
    return content

def process_ja_blog_file(ja_file: Path, en_file: Path, term_mapping: Dict[str, Tuple[str, str]]) -> bool:
    """
    日本語ブログファイルを処理
    """
    if not ja_file.exists():
        print(f"⚠️  ファイルが存在しません: {ja_file}")
        return False
    
    print(f"📝 処理中: {ja_file.name}")
    
    # ファイルを読み込み
    content = ja_file.read_text(encoding='utf-8')
    original_content = content
    
    # 1. 太字の助詞問題を修正
    content = fix_bold_particles(content)
    
    # 2. 内部リンクを追加
    content = add_internal_links_to_ja(content, term_mapping)
    
    # 変更があった場合のみ書き込み
    if content != original_content:
        ja_file.write_text(content, encoding='utf-8')
        print(f"✅ 修正完了: {ja_file.name}")
        return True
    else:
        print(f"ℹ️  変更なし: {ja_file.name}")
        return False

def main():
    # パスの設定
    base_dir = Path(__file__).parent.parent
    ja_blog_dir = base_dir / 'content' / 'ja' / 'blog'
    en_blog_dir = base_dir / 'content' / 'en' / 'blog'
    
    if not ja_blog_dir.exists():
        print(f"❌ 日本語ブログディレクトリが見つかりません: {ja_blog_dir}")
        return
    
    # 用語マッピングを作成
    term_mapping = create_term_mapping()
    
    # 日本語ブログファイルを処理
    ja_files = sorted(ja_blog_dir.glob('*.md'))
    total_files = len(ja_files)
    modified_files = 0
    
    print(f"\n🚀 日本語ブログ記事の修正を開始します")
    print(f"📊 対象ファイル数: {total_files}\n")
    
    for ja_file in ja_files:
        # 対応する英語ファイルを探す
        en_file = en_blog_dir / ja_file.name
        
        if process_ja_blog_file(ja_file, en_file, term_mapping):
            modified_files += 1
    
    print(f"\n✨ 完了!")
    print(f"📊 修正したファイル: {modified_files}/{total_files}")

if __name__ == '__main__':
    main()
