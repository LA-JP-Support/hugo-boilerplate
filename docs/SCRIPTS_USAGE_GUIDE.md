# スクリプト使用ガイド

このドキュメントでは、Hugo用語集サイトで使用する主要なスクリプトの使い方をまとめています。

## 目次

1. [環境設定](#環境設定)
2. [記事作成](#記事作成)
3. [翻訳](#翻訳)
4. [内部リンク](#内部リンク)
5. [その他の便利なスクリプト](#その他の便利なスクリプト)

---

## 環境設定

### 必須: .envファイルの設定

すべてのスクリプトは`.env`ファイルからAPI Keyを読み込みます。

**ファイルパス**: `/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/.env`

**内容**:
```bash
# Claude API Key (Anthropic)
ANTHROPIC_API_KEY="your-api-key-here"
# または
CLAUDE_API_KEY="your-api-key-here"
```

### 必要なPythonパッケージ

```bash
pip install anthropic python-dotenv pyyaml
```

---

## 記事作成

### 1. 最新版: CSVから一括作成（推奨）

**スクリプト**: `scripts/batch_create_from_csv.py`

**特徴**:
- CSVファイル（`docs/prioritized_keywords.csv`）から用語を読み込み
- 並列処理で高速作成
- 自動的に冠詞（a/an）を判定
- ステータス管理機能付き

**使用方法**:

```bash
# 全ての未作成記事を作成（5並列）
python scripts/batch_create_from_csv.py --workers 5

# 特定のカテゴリのみ作成
python scripts/batch_create_from_csv.py --category "AI Companies & Products"

# テストモード（実際には作成しない）
python scripts/batch_create_from_csv.py --test

# 特定の範囲を作成
python scripts/batch_create_from_csv.py --start 0 --end 10
```

**CSV形式**:
```csv
Keyword,Description,Category,Filename,Status_EN,Status_JA
Baidu,"Chinese technology company...",AI Companies & Products,Baidu.md,completed,pending
```

### 2. 単一記事作成

**スクリプト**: `scripts/api_batch_create_v3.py`

**使用方法**:

```bash
# 単一キーワードで記事作成
python scripts/api_batch_create_v3.py "Machine Learning"

# 複数キーワードを並列作成
python scripts/api_batch_create_v3.py "AI" "ML" "NLP" --workers 3
```

### 3. 記事の最適化

**スクリプト**: `scripts/optimize_glossary_descriptions.py`

**特徴**:
- descriptionフィールドを最適化（SEO対応）
- 冗長な前置き（"Comprehensive guide to..."）を削除
- 本文から簡潔な要約を抽出

**使用方法**:

```bash
# 英語版を最適化（5並列）
python scripts/optimize_glossary_descriptions.py --lang en --workers 5

# 日本語版を最適化
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# 特定のファイルのみ
python scripts/optimize_glossary_descriptions.py --lang en --file "Machine-Learning.md"
```

---

## 翻訳

### 1. 最新版: 統合翻訳パイプライン（推奨）

**スクリプト**: `scripts/pipeline_translate.py`

**特徴**:
- 自動検出・クリーンアップ・翻訳・エンリッチメントを一括実行
- ステップごとの実行も可能
- ドラフト管理機能

**使用方法**:

```bash
# 新規ファイルを自動検出して全工程実行
python scripts/pipeline_translate.py --auto

# 特定ファイルを処理
python scripts/pipeline_translate.py --file Copilot.md

# ドライラン（変更なし）
python scripts/pipeline_translate.py --auto --dry-run

# 特定ステップから開始
python scripts/pipeline_translate.py --file Copilot.md --from-step translate

# 特定ステップのみ実行
python scripts/pipeline_translate.py --file Copilot.md --only-step translate
```

**パイプラインステップ**:
1. `detect` - 新規/更新ファイル検出
2. `cleanup` - FlowHunt出力のクリーンアップ
3. `enrich-en` - 英語版にキーワード・リンク追加
4. `copy` - content/en/glossary/にコピー
5. `translate` - 日本語翻訳
6. `enrich-ja` - 日本語版にキーワード・リンク追加
7. `kana` - かなインデックス追加
8. `fix-readings` - 用語読みの修正
9. `compare` - アウトライン比較
10. `publish` - 公開（draft: false）

### 2. 単純翻訳

**スクリプト**: `scripts/translate_glossary_en_to_ja.py`

**使用方法**:

```bash
# 単一ファイル翻訳
python scripts/translate_glossary_en_to_ja.py --one-file Active-Learning.md

# 全ファイル翻訳（5並列）
python scripts/translate_glossary_en_to_ja.py --workers 5

# CSVステータスを自動更新
python scripts/translate_glossary_en_to_ja.py --one-file Active-Learning.md
# → CSV内のStatus_JAが自動的に"completed"に更新される
```

### 3. 並列翻訳（高速）

**スクリプト**: `scripts/parallel_translate_continuous.py`

**使用方法**:

```bash
# 未翻訳ファイルを自動検出して並列翻訳（5並列）
python scripts/parallel_translate_continuous.py --workers 5

# 特定ファイルを並列翻訳
python scripts/parallel_translate_continuous.py File1.md File2.md File3.md --workers 3
```

### 4. 日本語用語の読み修正

**スクリプト**: `scripts/fix_term_readings_ja.py`

**特徴**:
- 漢字で始まる`term`フィールドをかな読みに変換
- 五十音順ソート用

**使用方法**:

```bash
python scripts/fix_term_readings_ja.py --ja-dir content/ja/glossary
```

---

## 内部リンク

### 1. 最新版: 並列リンク構築（推奨）

**スクリプト**: `scripts/linkbuilding_parallel.py`

**特徴**:
- 並列処理で高速
- 用語集へのリンクを自動挿入
- バリエーション対応（複数形、大文字小文字など）

**使用方法**:

```bash
# 英語ブログ記事にリンク追加（5並列）
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/blog \
    --glossary-dir content/en/glossary \
    --workers 5

# 日本語ブログ記事にリンク追加
python scripts/linkbuilding_parallel.py \
    --content-dir content/ja/blog \
    --glossary-dir content/ja/glossary \
    --workers 5

# 用語集記事同士のリンク
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/glossary \
    --glossary-dir content/en/glossary \
    --workers 5
```

### 2. 用語集エンリッチメント

**スクリプト**: `scripts/enrich_glossary_blog_v3.py`

**特徴**:
- キーワード追加
- 内部リンク追加
- メタデータ最適化

**使用方法**:

```bash
# 英語用語集をエンリッチ
python scripts/enrich_glossary_blog_v3.py \
    --content-dir content/en/glossary \
    --glossary-dir content/en/glossary \
    --lang en

# 日本語用語集をエンリッチ
python scripts/enrich_glossary_blog_v3.py \
    --content-dir content/ja/glossary \
    --glossary-dir content/ja/glossary \
    --lang ja
```

### 3. ツールチップからリンクへ変換

**スクリプト**: `scripts/convert_tooltips_to_links.py`

**特徴**:
- ツールチップ構文を通常のリンクに変換
- `{{< tooltip "term" >}}text{{< /tooltip >}}` → `[text](/glossary/term/)`

**使用方法**:

```bash
# 英語記事を変換
python scripts/convert_tooltips_to_links.py \
    --content-dir content/en/blog \
    --lang en

# 日本語記事を変換
python scripts/convert_tooltips_to_links.py \
    --content-dir content/ja/blog \
    --lang ja
```

---

## その他の便利なスクリプト

### 1. CSVステータス管理

**スクリプト**: `scripts/manage_glossary_status.py`

```bash
# 現在のステータスを確認
python scripts/manage_glossary_status.py --status

# 特定ファイルのステータスを更新
python scripts/manage_glossary_status.py --update-file Baidu.md --status-en completed

# 一括ステータス更新
python scripts/manage_glossary_status.py --bulk-update-en completed
```

### 2. 記事比較

**スクリプト**: `scripts/compare_articles.py`

```bash
# 英語版と日本語版のアウトライン比較
python scripts/compare_articles.py \
    --en-file content/en/glossary/Machine-Learning.md \
    --ja-file content/ja/glossary/Machine-Learning.md
```

### 3. かなインデックス追加

**スクリプト**: `scripts/add_kana_index.py`

```bash
# 日本語用語集にかなインデックスを追加
python scripts/add_kana_index.py --glossary-dir content/ja/glossary
```

---

## 推奨ワークフロー

### 新規記事作成から公開まで

```bash
# 1. CSVから記事作成（英語）
python scripts/batch_create_from_csv.py --workers 5

# 2. descriptionを最適化（英語）
python scripts/optimize_glossary_descriptions.py --lang en --workers 5

# 3. 内部リンク追加（英語）
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/glossary \
    --glossary-dir content/en/glossary \
    --workers 5

# 4. 翻訳（英語→日本語）
python scripts/translate_glossary_en_to_ja.py --workers 5

# 5. descriptionを最適化（日本語）
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# 6. 用語読み修正（日本語）
python scripts/fix_term_readings_ja.py --ja-dir content/ja/glossary

# 7. 内部リンク追加（日本語）
python scripts/linkbuilding_parallel.py \
    --content-dir content/ja/glossary \
    --glossary-dir content/ja/glossary \
    --workers 5

# 8. かなインデックス追加（日本語）
python scripts/add_kana_index.py --glossary-dir content/ja/glossary
```

### FlowHunt記事の処理

```bash
# 統合パイプラインで一括処理
python scripts/pipeline_translate.py --auto
```

---

## トラブルシューティング

### API Keyエラー

```
エラー: ANTHROPIC_API_KEY または CLAUDE_API_KEY が設定されていません
```

**解決方法**: `.env`ファイルにAPI Keyを設定してください。

### 並列処理でエラー

並列数を減らしてください：
```bash
# 5並列 → 3並列に変更
python scripts/batch_create_from_csv.py --workers 3
```

### ファイルが見つからない

絶対パスを確認してください：
```bash
# プロジェクトルートから実行
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
python scripts/batch_create_from_csv.py
```

---

## 更新履歴

- 2025-12-20: 初版作成
  - 記事作成、翻訳、内部リンクの最新スクリプトを整理
  - .env対応を追加
  - 推奨ワークフローを追加
