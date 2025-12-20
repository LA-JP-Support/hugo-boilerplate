# Glossary & Blog Internal Linking System

## 📋 概要

このシステムは、用語集とブログ記事の内部リンクを自動化し、ツールチップを内部リンクに変換します。

### 主な機能

1. **ツールチップ分析** - ブログ記事の既存ツールチップを抽出し、用語集と照合
2. **用語集エンリッチメント** - 用語集記事に内部リンクを自動追加
3. **ブログエンリッチメント** - ブログ記事のツールチップを内部リンクに変換＋新規リンク追加

## 🚀 クイックスタート

### 一括処理（推奨）

```bash
# 英語コンテンツのみ
./scripts/batch_enrich.sh en

# 日本語コンテンツのみ
./scripts/batch_enrich.sh ja

# 両言語
./scripts/batch_enrich.sh all

# Dry run（実際には変更しない）
./scripts/batch_enrich.sh en --dry-run
```

### 個別実行

#### 1. ツールチップ分析

```bash
# 英語
python3 scripts/analyze_tooltips_vs_glossary.py --lang en

# 日本語
python3 scripts/analyze_tooltips_vs_glossary.py --lang ja
```

**出力**: `docs/tooltip_analysis_{lang}.json`

#### 2. 用語集のエンリッチメント

```bash
# 英語用語集
python3 scripts/enrich_glossary_blog.py content/en/glossary/

# 日本語用語集
python3 scripts/enrich_glossary_blog.py content/ja/glossary/
```

#### 3. ブログのエンリッチメント（ツールチップ変換）

```bash
# 英語ブログ
python3 scripts/enrich_glossary_blog.py content/en/blog/ --convert-tooltips

# 日本語ブログ
python3 scripts/enrich_glossary_blog.py content/ja/blog/ --convert-tooltips
```

## 📊 処理内容の詳細

### ツールチップ → 内部リンクの変換

**変換前**:
```markdown
{{< tooltip text="Technology that enables computers to think" >}}artificial intelligence{{< /tooltip >}}
```

**変換後**:
```markdown
[artificial intelligence](/en/glossary/artificial-intelligence/ "Technology that enables computers to think")
```

### マウスオーバーでの説明表示

内部リンクに `title` 属性を追加することで、マウスオーバー時に用語集のDescriptionを表示：

```markdown
[RAG](/en/glossary/rag/ "Retrieval-Augmented Generation enhances LLMs by integrating external data sources")
```

### 自動内部リンク追加

用語集に存在するキーワードを自動検出し、内部リンクを追加：

- 各キーワードの**最初の出現のみ**リンク化（過度なリンクを防止）
- 既存のリンク、コードブロック、数式は保護
- 見出し内にはリンク追加しない
- 自己参照を防止（記事自身へのリンクは作成しない）

## 📁 ファイル構成

```
scripts/
├── analyze_tooltips_vs_glossary.py   # ツールチップ分析
├── enrich_glossary_blog.py          # メインエンリッチメントスクリプト
└── batch_enrich.sh                   # 一括実行スクリプト

docs/
├── tooltip_analysis_en.json          # 英語ツールチップ分析結果
├── tooltip_analysis_ja.json          # 日本語ツールチップ分析結果
└── GLOSSARY_BLOG_ENRICHMENT.md      # このファイル
```

## 🔍 ツールチップ分析レポートの見方

分析実行後、以下のレポートが生成されます：

```json
{
  "language": "en",
  "total_tooltips": 45,
  "has_glossary": 32,
  "missing_glossary": 13,
  "missing_details": [
    {
      "keyword": "machine learning",
      "definition": "Technology that learns by finding patterns in data",
      "usage_count": 3,
      "files": ["ai-chatbot-types-guide.md", "start-using-ai-today.md"]
    }
  ]
}
```

### 重要な指標

- **total_tooltips**: ブログ記事内のユニークなツールチップキーワード数
- **has_glossary**: すでに用語集エントリが存在するキーワード数
- **missing_glossary**: 用語集にないキーワード数（新規作成候補）

## ⚙️ 設定とカスタマイズ

### 内部リンクの制限

`enrich_glossary_blog.py`内で調整可能：

```python
# 最小キーワード長（デフォルト: 4文字）
if len(title) >= 4:
    sorted_entries.append((title, entry, slug))
```

### ツールチップパターン

現在対応しているツールチップ形式：

```markdown
{{< tooltip text="定義" >}}キーワード{{< /tooltip >}}
{{< tooltip text="定義" >}}[キーワード](/url/){{< /tooltip >}}
```

## 🎯 ワークフロー例

### 新しいブログ記事を追加した場合

```bash
# 1. ツールチップ分析（用語集にない用語を確認）
python3 scripts/analyze_tooltips_vs_glossary.py --lang en

# 2. 必要に応じて新しい用語集エントリを作成
# （missing_glossaryのキーワードを確認）

# 3. ブログ記事をエンリッチ
python3 scripts/enrich_glossary_blog.py content/en/blog/new-article.md --convert-tooltips

# 4. 結果を確認
git diff content/en/blog/new-article.md
```

### 既存記事の一括更新

```bash
# Dry runで確認
./scripts/batch_enrich.sh en --dry-run

# 問題なければ実行
./scripts/batch_enrich.sh en

# 変更を確認
git diff content/en/
```

## ⚠️ 注意事項

### 既存リンクの保護

スクリプトは以下を自動的に保護し、変更しません：

- 既存のMarkdownリンク `[text](url)`
- コードブロック ` ```code``` `
- インラインコード `` `code` ``
- 数式 `$$ math $$`
- 見出し `# Heading`
- 太字/斜体 `**bold**`, `*italic*`

### 自己参照の防止

記事が自身へリンクすることを防ぎます：

```markdown
<!-- AI-chatbot.md 内では "AI Chatbot" へのリンクは作成されない -->
```

### 過度なリンクの防止

各用語は**最初の出現のみ**リンク化されます。

## 🐛 トラブルシューティング

### スクリプトが実行できない

```bash
# 実行権限を付与
chmod +x scripts/batch_enrich.sh
```

### Python依存関係エラー

```bash
# 必要なパッケージをインストール
pip install pyyaml
```

### ツールチップが変換されない

- ツールチップの形式が正しいか確認
- 対応する用語集エントリが存在するか確認
- `--convert-tooltips` フラグを付けているか確認

## 📈 今後の拡張予定

- [ ] 複数形/単数形の自動マッチング
- [ ] 同義語対応
- [ ] カスタムリンク優先度設定
- [ ] HTMLエクスポートの統計レポート

## 📞 サポート

問題が発生した場合は、以下を確認してください：

1. `docs/tooltip_analysis_{lang}.json` のレポート
2. Git diffで変更内容を確認
3. Dry runモードでテスト実行

---

**作成日**: 2025-12-20  
**バージョン**: 1.0  
**保存先**: `docs/GLOSSARY_BLOG_ENRICHMENT.md`
