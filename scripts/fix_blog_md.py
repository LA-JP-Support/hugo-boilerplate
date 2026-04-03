#!/usr/bin/env python3
"""
ブログMDファイルの一括修正スクリプト
- 壊れた外部リンクの修正
- 重複テキストの修正
- FlowHunt/LiveAgentの外部リンクをテキストに変換
- 壊れた用語集リンクの削除
"""

import re
from pathlib import Path

def fix_content(content: str, filename: str) -> tuple[str, list[str]]:
    """コンテンツを修正し、変更点のリストを返す"""
    changes = []
    original = content
    
    # 1. 重複テキストの修正
    duplicates = [
        ('ChatGPTChatGP', 'ChatGPT'),
        ('OpenAIOpenA', 'OpenAI'),
        ('GoogleGoogl', 'Google'),
        ('AnthropicAnthropi', 'Anthropic'),
        ('FlowHuntFlowHun', 'FlowHunt'),
        ('YouTubeYouTub', 'YouTube'),
        ('LiveAgentLiveAgent', 'LiveAgent'),
        ('FacebookFacebook', 'Facebook'),
        ('InstagramInstagram', 'Instagram'),
        ('CAGRCAG', 'CAGR'),
        ('GDPRGDP', 'GDPR'),
        ('APIAPI', 'API'),
        ('FAQFAQ', 'FAQ'),
        ('WhatsAppWhatsApp', 'WhatsApp'),
    ]
    
    for old, new in duplicates:
        if old in content:
            content = content.replace(old, new)
            changes.append(f"重複修正: {old} → {new}")
    
    # 2. FlowHunt/LiveAgentの外部リンクをテキストに変換
    # パターン: [FlowHunt](https://...) や [LiveAgent](https://...)
    external_link_patterns = [
        (r'\[FlowHunt\]\(https?://[^)]+\)', 'FlowHunt'),
        (r'\[LiveAgent\]\(https?://[^)]+\)', 'LiveAgent'),
    ]
    
    for pattern, replacement in external_link_patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            changes.append(f"外部リンク削除: {pattern[:30]}... → {replacement}")
    
    # 3. 壊れた外部リンク（不完全なURL）
    broken_links = [
        (r'\[FlowHunt\]\(https://www\.flowhunt\.i(?!o)[^)]*', 'FlowHunt'),
        (r'\[LiveAgent\]\(https://www\.liveagent\.co(?!m)[^)]*', 'LiveAgent'),
    ]
    
    for pattern, replacement in broken_links:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"壊れたリンク修正: → {replacement}")
    
    # 4. 用語集リンクの残骸パターン
    # パターン: テキストSlug/) や テキストSlug/) **
    glossary_remnants = [
        # 日本語+英語スラッグ+/) パターン
        (r'([ぁ-んァ-ヶー一-龯A-Za-z]+)[A-Za-z0-9_-]+/\)\s*\*\*', r'\1'),
        (r'([ぁ-んァ-ヶー一-龯A-Za-z]+)[A-Za-z0-9_-]+/\)', r'\1'),
        # [text](/ja/glossary/...) パターン
        (r'\[([^\]]+)\]\(/ja/glossary/[^)]+\)', r'\1'),
    ]
    
    for pattern, replacement in glossary_remnants:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            changes.append(f"用語集残骸削除: {len(matches)}件")
    
    # 5. 壊れた内部リンク（用語集の説明文が混入）
    # パターン: TextText/ "説明文") や artificial-intelligence/ "説明...
    broken_internal_patterns = [
        # AIartificial-intelligence/ "人工知能... パターン
        (r'AI(?:artificial-intelligence/[^)]+\)){1,}', 'AI'),
        # FAQよくある質問FAQ/ "説明..." パターン  
        (r'FAQ[^F]*FAQ/[^)]+\)\)', 'FAQ'),
        (r'FAQ[、,][^「」\n]+「[^」]+」\)', 'FAQ'),
        # LiveAgentLiveAgent/ "説明..." パターン
        (r'LiveAgent/ "[^"]+"[)\s]*', 'LiveAgent'),
        # FlowHuntFlowHunt/ "説明..." パターン
        (r'FlowHunt/ "[^"]+"[)\s]*', 'FlowHunt'),
        # FacebookFacebook/ "説明..." パターン
        (r'Facebook/ "[^"]+"[)\s]*', 'Facebook'),
        # InstagramInstagram/ "説明..." パターン
        (r'Instagram/ "[^"]+"[)\s]*', 'Instagram'),
        # YouTubeYouTube/ "説明..." パターン  
        (r'YouTube/ "[^"]+"[)\s]*', 'YouTube'),
    ]
    
    for pattern, replacement in broken_internal_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"壊れた内部リンク修正: → {replacement}")
    
    # 6. 壊れた太字パターン
    # パターン: テキスト** 型** → **テキスト型**
    bold_fixes = [
        (r'ルールベース\*\* 型\*\*', '**ルールベース型**'),
        (r'業務効率\*\* 化\*\*', '**業務効率化**'),
        (r'ハルシネーション対策\*\* -', '**ハルシネーション対策** -'),
        (r'\*\*業務効率化\*\* -', '**業務効率化** -'),
    ]
    
    for pattern, replacement in bold_fixes:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"太字修正: → {replacement[:20]}...")
    
    # 7. 複雑な壊れたリンクパターン（FAQなど）
    # FAQ、カスタマーサポート、...のような長い説明文
    complex_faq_pattern = r'FAQ[、,][^「」\n]{10,}[「」][^」\n]+[」][)]*[)]*'
    if re.search(complex_faq_pattern, content):
        content = re.sub(complex_faq_pattern, 'FAQ', content)
        changes.append("複雑なFAQリンク修正")
    
    # 8. 画像リンクの壊れたパターン
    # <img src="/images/blog/AIartificial-intelligence/...
    img_pattern = r'<img src="[^"]*artificial-intelligence/[^"]*"'
    if re.search(img_pattern, content):
        # この場合は手動確認が必要なのでログだけ
        changes.append("⚠️ 壊れた画像リンクあり（手動確認推奨）")
    
    # 9. status.liveagentLiveAgent/ パターン
    status_pattern = r'status\.liveagentLiveAgent/ "[^"]+"'
    if re.search(status_pattern, content):
        content = re.sub(status_pattern, 'status.liveagent', content)
        changes.append("status.liveagentリンク修正")
    
    # 10. 「と」で終わる不完全な文
    incomplete_patterns = [
        (r'「FlowHunt」と「', '「FlowHunt」と「LiveAgent」'),
        (r'LiveAgentと\nを組み合わせ', 'LiveAgentとFlowHuntを組み合わせ'),
        (r'LiveAgentとを組み合わせ', 'LiveAgentとFlowHuntを組み合わせ'),
        (r'FlowHuntとを組み合わせ', 'FlowHuntとLiveAgentを組み合わせ'),
    ]
    
    for pattern, replacement in incomplete_patterns:
        if pattern in content or re.search(pattern, content):
            content = content.replace(pattern, replacement) if pattern in content else re.sub(pattern, replacement, content)
            changes.append(f"不完全文修正: → {replacement[:30]}...")
    
    # 11. WhatsAppを活用した → WhatsAppを活用した
    whatsapp_pattern = r'を活用したチャットボット'
    if 'WhatsApp' not in content and whatsapp_pattern in content:
        # 文脈確認が必要
        pass
    
    return content, changes


def main():
    blog_dir = Path('/Users/TM-MBP1/Documents/GitHub/smartweb/content/ja/blog')
    
    print("=" * 60)
    print("ブログMDファイル一括修正")
    print("=" * 60)
    
    total_changes = 0
    
    for md_file in sorted(blog_dir.glob('*.md')):
        if md_file.name == '.DS_Store':
            continue
            
        content = md_file.read_text(encoding='utf-8')
        fixed_content, changes = fix_content(content, md_file.name)
        
        if changes:
            print(f"\n📄 {md_file.name}")
            for change in changes:
                print(f"   ✓ {change}")
            total_changes += len(changes)
            
            # ファイルを更新
            md_file.write_text(fixed_content, encoding='utf-8')
    
    print("\n" + "=" * 60)
    print(f"完了: {total_changes}件の修正を適用しました")
    print("=" * 60)


if __name__ == '__main__':
    main()
