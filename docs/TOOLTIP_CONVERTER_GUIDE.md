# Tooltip to Internal Link Converter - User Guide
## ツールチップから内部リンクへの変換スクリプト - 使用方法

**バージョン**: v4 (prompts→prompting対応)  
**作成日**: 2025-12-20  
**スクリプト**: `scripts/convert_tooltips_to_links.py`

---

## 📋 概要

Hugoのツールチップショートコードを内部グロッサリーリンクに自動変換するスクリプトです。

### 変換例
```markdown
# 変換前
{{< tooltip text="An AI technique" >}}Zero-shot{{< /tooltip >}}

# 変換後
[Zero-shot](/en/glossary/Zero-Shot-Learning/ "An AI technique")
```

---

## 🎯 主な機能

### v4の全機能
1. **複数形/単数形の自動対応**
   - `tickets` ⟷ `ticket`
   - `workflows` ⟷ `workflow`

2. **括弧付き略語の柔軟な対応**
   - `Customer Satisfaction (CSAT)` ⟷ `CSAT`
   - `NPS (Net Promoter Score)` ⟷ `Net Promoter Score`

3. **ダッシュ区切り形式の対応**
   - `ITIL – Information Technology Infrastructure Library` ⟷ `ITIL`

4. **接尾辞削除による部分一致**
   - `Zero-shot` → `Zero-Shot Learning`
   - `Few-shot` → `Few-Shot Learning`
   - `hallucination problem` → `Hallucination`
   - `RAG technology` → `RAG`

5. **特別変換: prompts → prompting**
   - `Chain-of-Thought prompts` → `Chain-of-Thought Prompting`

---

## 💻 使用方法

### 基本コマンド

#### 1. Dry-run（プレビュー）
```bash
python3 scripts/convert_tooltips_to_links.py content/en/blog/ --dry-run
```

#### 2. 本番実行
```bash
python3 scripts/convert_tooltips_to_links.py content/en/blog/
```

#### 3. 日本語ブログ処理
```bash
python3 scripts/convert_tooltips_to_links.py content/ja/blog/
```

#### 4. カスタムグロッサリーディレクトリ指定
```bash
python3 scripts/convert_tooltips_to_links.py content/en/blog/ --glossary-dir /path/to/glossary
```

---

## 📊 出力例

```
Loading glossary from content/en/glossary
Loaded 1221 glossary entries
Generated 3071 keyword variations

============================================================
Processing 12 blog files
Mode: LIVE
============================================================

  ai-chatbot-types-guide.md: No tooltips found
  ✓ Converted: Zero-shot
  ✓ Converted: Chain-of-Thought prompts
✅ ai-evaluation-japanese-benchmarks.md: 2 tooltips converted

============================================================
Summary:
  Files processed: 12
  Files modified: 1
============================================================
```

---

## 🔧 トラブルシューティング

### Q1: "No match for: XXX" と表示される

**原因**: グロッサリーに該当する用語が存在しない

**解決策**:
1. グロッサリーファイルが存在するか確認
2. タイトルのスペルを確認
3. 必要に応じてグロッサリーファイルを作成

### Q2: 一部のツールチップが変換されない

**原因**: タイトルの形式が一致しない

**解決策**:
- ブログ: `AI answer assistant`
- グロッサリー: `AI Answer Assistant`
→ 大文字/小文字は自動正規化されるので問題なし

### Q3: 括弧付きの用語がマッチしない

**例**: `ITIL (IT Infrastructure Library)` がマッチしない

**解決策**: グロッサリータイトルを確認
- グロッサリー: `ITIL – Information Technology Infrastructure Library`
→ v4では自動対応済み

---

## 📁 ファイル構成

```
hugo-boilerplate/
├── scripts/
│   ├── convert_tooltips_to_links.py      # メインスクリプト (v4)
│   └── convert_tooltips_to_links_v4.py   # バックアップ
├── content/
│   ├── en/
│   │   ├── blog/      # 英語ブログ
│   │   └── glossary/  # 英語グロッサリー
│   └── ja/
│       ├── blog/      # 日本語ブログ
│       └── glossary/  # 日本語グロッサリー
└── docs/
    └── TOOLTIP_CONVERTER_GUIDE.md  # このファイル
```

---

## 📈 実績

### 英語ブログ (2025-12-20時点)
- **処理ファイル数**: 12件
- **変換済みツールチップ**: 180件
- **成功率**: 98.9%

### 対応した主な用語
- Zero-shot, Few-shot → Learning追加
- Chain-of-Thought → Prompting追加
- ITIL, CSAT, NPS → 括弧/ダッシュ対応
- Hallucination phenomena → 接尾辞削除
- RAG technology → 接尾辞削除

---

## 🔄 更新履歴

### v4 (2025-12-20)
- ✅ prompts → prompting 特別変換を追加
- ✅ 部分一致機能を強化
- ✅ 接尾辞削除リストを拡張

### v3 (2025-12-20)
- ✅ ダッシュ区切り形式対応
- ✅ カンマ区切り対応
- ✅ コロン付き括弧対応

### v2 (2025-12-20)
- ✅ 括弧と略語の柔軟な対応
- ✅ 複数形の自動生成

### v1 (2025-12-20)
- ✅ 基本的なツールチップ変換機能

---

## 💡 ベストプラクティス

1. **必ず dry-run で確認**
   ```bash
   python3 scripts/convert_tooltips_to_links.py content/en/blog/ --dry-run
   ```

2. **バッチ処理前にバックアップ**
   ```bash
   cp -r content/en/blog content/en/blog-backup
   ```

3. **Git でコミット**
   ```bash
   git add content/en/blog/
   git commit -m "Convert tooltips to internal links (batch X)"
   ```

4. **変換後の確認**
   - 生成されたリンクが正しいパスになっているか
   - 定義文が正しく引用符内に収まっているか
   - 内部リンクが機能するか（Hugoサーバーで確認）

---

## 🎓 技術詳細

### 正規表現パターン
```python
tooltip_pattern = re.compile(
    r'\{\{<\s*tooltip\s+text="([^"]*)"\s*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}',
    re.DOTALL
)
```

### キーワード正規化
```python
def _normalize_keyword(self, text: str) -> str:
    return ' '.join(text.lower().strip().split())
```

### 接尾辞削除リスト
```python
suffixes = [
    'learning', 'prompting', 'prompts', 'problem', 'problems', 
    'technology', 'technologies', 'system', 'systems',
    'assistant', 'assistants', 'phenomena', 'phenomenon'
]
```

---

## 📞 サポート

問題が発生した場合：
1. dry-run で詳細なエラーメッセージを確認
2. グロッサリーファイルのタイトルを確認
3. バックアップから復元
4. このガイドのトラブルシューティングセクションを参照

---

**最終更新**: 2025-12-20  
**メンテナンス**: Takazumi
