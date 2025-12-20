# 内部リンク設定システム - クイックリファレンス

## ⚡ クイックスタート

### 初回セットアップ
```bash
chmod +x scripts/batch_enrich.sh
chmod +x scripts/test_enrichment.sh
```

### テスト実行
```bash
./scripts/test_enrichment.sh
```

### 本番実行
```bash
# 英語コンテンツ
./scripts/batch_enrich.sh en

# 日本語コンテンツ
./scripts/batch_enrich.sh ja

# 両言語
./scripts/batch_enrich.sh all
```

---

## 📊 3つのスクリプト

| スクリプト | 用途 | 実行例 |
|-----------|------|--------|
| `analyze_tooltips_vs_glossary.py` | ツールチップ分析 | `python3 scripts/analyze_tooltips_vs_glossary.py --lang en` |
| `enrich_glossary_blog.py` | メイン処理 | `python3 scripts/enrich_glossary_blog.py content/en/blog/ --convert-tooltips` |
| `batch_enrich.sh` | 一括実行 | `./scripts/batch_enrich.sh en` |

---

## 🎯 処理内容

### 1️⃣ ツールチップ分析
- ブログ記事のツールチップを抽出
- 用語集と照合
- レポート生成（`docs/tooltip_analysis_{lang}.json`）

### 2️⃣ 用語集エンリッチメント
- 用語集記事に内部リンク追加
- マウスオーバーでDescription表示

### 3️⃣ ブログエンリッチメント
- ツールチップ → 内部リンク変換
- 新規内部リンク追加
- マウスオーバーでDescription表示

---

## 🔄 変換例

### ツールチップ → 内部リンク

**変換前**:
```markdown
{{< tooltip text="AI technology for natural conversation" >}}AI chatbot{{< /tooltip >}}
```

**変換後**:
```markdown
[AI chatbot](/en/glossary/ai-chatbot/ "AI technology for natural conversation")
```

### 自動リンク追加

**処理前**:
```markdown
AI chatbots use machine learning to improve responses.
```

**処理後**:
```markdown
[AI chatbot](/en/glossary/ai-chatbot/ "AI-powered conversational software") use [machine learning](/en/glossary/machine-learning/ "AI technique for pattern recognition") to improve responses.
```

---

## 📁 出力ファイル

| ファイル | 内容 |
|---------|------|
| `docs/tooltip_analysis_en.json` | 英語ツールチップ分析結果 |
| `docs/tooltip_analysis_ja.json` | 日本語ツールチップ分析結果 |

---

## 🛡️ 保護される要素

スクリプトは以下を**変更しません**：

- ✅ 既存のMarkdownリンク
- ✅ コードブロック（` ```code``` `）
- ✅ インラインコード（`` `code` ``）
- ✅ 数式（`$$ math $$`）
- ✅ 見出し（`# Heading`）
- ✅ 太字/斜体（`**bold**`, `*italic*`）

---

## ⚙️ オプション

### Dry Run（変更せず確認のみ）
```bash
./scripts/batch_enrich.sh en --dry-run
```

### 単一ファイルの処理
```bash
# 用語集
python3 scripts/enrich_glossary_blog.py content/en/glossary/AI-chatbot.md

# ブログ（ツールチップ変換）
python3 scripts/enrich_glossary_blog.py content/en/blog/start-using-ai-today.md --convert-tooltips
```

---

## 🔍 レポートの確認

### ツールチップ分析結果
```bash
# JSONを整形表示
cat docs/tooltip_analysis_en.json | python3 -m json.tool

# 用語集にないキーワードを抽出
cat docs/tooltip_analysis_en.json | python3 -m json.tool | grep -A 3 "missing_details"
```

---

## 📋 標準ワークフロー

### 新しいブログ記事追加時
```bash
# 1. ツールチップ分析
python3 scripts/analyze_tooltips_vs_glossary.py --lang en

# 2. レポート確認
cat docs/tooltip_analysis_en.json | python3 -m json.tool

# 3. 必要に応じて用語集エントリ作成
# （missing_glossaryのキーワードを確認）

# 4. ブログエンリッチメント実行
python3 scripts/enrich_glossary_blog.py content/en/blog/ --convert-tooltips

# 5. 変更確認
git diff content/en/blog/
```

### 既存記事の一括更新
```bash
# 1. Dry runで確認
./scripts/batch_enrich.sh en --dry-run

# 2. 実行
./scripts/batch_enrich.sh en

# 3. 変更確認
git diff content/en/
```

---

## ⚠️ トラブルシューティング

### 権限エラー
```bash
chmod +x scripts/batch_enrich.sh
chmod +x scripts/test_enrichment.sh
```

### Python依存関係
```bash
pip install pyyaml
```

### ツールチップが変換されない
- `--convert-tooltips` フラグを確認
- ツールチップ形式が正しいか確認
- 対応する用語集エントリが存在するか確認

---

## 📊 レポート項目の説明

| 項目 | 説明 |
|------|------|
| `total_tooltips` | ユニークなツールチップキーワード総数 |
| `has_glossary` | 用語集エントリが存在するキーワード数 |
| `missing_glossary` | 用語集にないキーワード数（新規作成候補） |
| `missing_details` | 用語集にないキーワードの詳細リスト |

---

## 🎯 重要な機能

### ✅ 実装済み
1. ツールチップ → 内部リンク変換
2. 自動内部リンク追加（最初の出現のみ）
3. マウスオーバーでDescription表示
4. 既存コンテンツの保護
5. 自己参照の防止
6. ツールチップ分析レポート

### 📌 制限事項
- 各キーワードは最初の出現のみリンク化
- 最小キーワード長: 4文字
- 見出し内にはリンク追加しない

---

**最終更新**: 2025-12-20  
**バージョン**: 1.0
