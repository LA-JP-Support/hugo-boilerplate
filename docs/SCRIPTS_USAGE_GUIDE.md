# スクリプト使用ガイド（最新版）

このドキュメントでは、Hugo用語集サイトで使用する主要なスクリプトの使い方をまとめています。

**最終更新**: 2025-12-21  
**バージョン**: 2.0

## 目次

1. [環境設定](#環境設定)
2. [記事作成](#記事作成)
3. [翻訳](#翻訳)
4. [内部リンク](#内部リンク)
5. [ブログ記事メンテナンス](#ブログ記事メンテナンス)
6. [その他の便利なスクリプト](#その他の便利なスクリプト)
7. [推奨ワークフロー](#推奨ワークフロー)
8. [トラブルシューティング](#トラブルシューティング)

---

## 環境設定

### 必須: .envファイルの設定

すべてのスクリプトは`.env`ファイルからAPI Keyを読み込みます。

**ファイルパス**: `/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/.env`

**内容**:
```bash
# Claude API Key (Anthropic) - 両方設定推奨
ANTHROPIC_API_KEY="sk-ant-api03-your-key-here"
CLAUDE_API_KEY="sk-ant-api03-your-key-here"
```

### 必要なPythonパッケージ

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
pip install -r scripts/requirements.txt

# または個別インストール
pip install anthropic python-dotenv pyyaml
```

---

## 記事作成

### 🌟 推奨: CSVから一括作成

**スクリプト**: `scripts/batch_create_from_csv.py`

**特徴**:
- CSVファイル（`docs/prioritized_keywords.csv`）から用語を自動読み込み
- 並列処理で高速作成（デフォルト3スレッド）
- 自動的に冠詞（a/an）を判定
- ステータス管理機能付き（Status_ENフィールド更新）
- 文法チェック機能
- コスト・語数・処理時間の詳細レポート

**目標品質**:
- **語数**: 2,700-2,900語/記事
- **構成**: 30%散文 / 70%構造化コンテンツ
- **セクション数**: 11セクション（固定）

**使用方法**:

```bash
# 1. 全ての未作成記事を作成（3並列）
python scripts/batch_create_from_csv.py --workers 3

# 2. 特定のカテゴリのみ作成
python scripts/batch_create_from_csv.py --category "AI Companies & Products"

# 3. 特定の範囲を作成（最初の10件）
python scripts/batch_create_from_csv.py --start 0 --end 10

# 4. テストモード（実際には作成しない、コスト見積もりのみ）
python scripts/batch_create_from_csv.py --test

# 5. 並列数を増やして高速化（推奨: 5まで）
python scripts/batch_create_from_csv.py --workers 5
```

**出力例**:

```
======================================================================
🚀 CSV一括記事生成開始 (v3)
======================================================================
CSV: docs/prioritized_keywords.csv
未作成記事: 15件
並列数: 3
目標語数: 2,700-2,900語/記事
======================================================================

✅ Customer Segmentation: 2,745語, 15,234 tokens, $0.2234, 43.2s
✅ Sentiment Analysis: 2,812語, 16,123 tokens, $0.2456, 47.8s
⚠️ Recommendation Systems: 2,654語, 14,876 tokens, $0.2187, 41.5s

======================================================================
📊 完了サマリー
======================================================================
成功:         15/15
語数達成:     13/15 (2,700-2,900語)
文法OK:       15/15
平均語数:     2,756語/記事
合計トークン: 234,567
合計コスト:   $3.4567
平均時間:     45.3秒/記事
総時間:       11.3分
======================================================================
```

**CSV形式**:
```csv
Keyword,Description,Category,Filename,Status_EN,Status_JA
Active Learning,"Machine learning approach...",AI & ML Core,Active-Learning.md,pending,pending
Baidu,"Chinese technology company...",AI Companies & Products,Baidu.md,completed,pending
```

**ステータス自動更新**:
- 記事作成成功 → `Status_EN`が自動的に`completed`に更新
- 失敗時は`pending`のまま

---

### シンプル版: 手動キーワード指定

**スクリプト**: `scripts/api_batch_create_v3.py`

**用途**: テスト・単発実行・CSVにない用語

**使用方法**:

```bash
# 1. 単一キーワード
python scripts/api_batch_create_v3.py --keywords "Machine Learning"

# 2. 複数キーワードを並列作成
python scripts/api_batch_create_v3.py \
  --keywords "AI" "Deep Learning" "NLP" \
  --workers 3

# 3. テストモード（別ディレクトリに出力）
python scripts/api_batch_create_v3.py \
  --keywords "Test Topic" \
  --test

# 4. カスタム出力先
python scripts/api_batch_create_v3.py \
  --keywords "Custom Topic" \
  --output-dir /path/to/output
```

---

### 記事品質チェック

作成後、以下を確認：

```bash
# 1. 語数確認
for file in content/en/glossary/*.md; do
  words=$(grep -v '^---' "$file" | wc -w)
  echo "$(basename $file): ${words}語"
done

# 2. フロントマター確認
head -20 content/en/glossary/Active-Learning.md

# 3. References確認
tail -20 content/en/glossary/Active-Learning.md
```

---

### 記事の最適化

**スクリプト**: `scripts/optimize_glossary_descriptions.py`

**特徴**:
- descriptionフィールドを最適化（SEO対応）
- 冗長な前置き（"Comprehensive guide to..."）を削除
- 本文から簡潔な要約を抽出（150-160文字）

**使用方法**:

```bash
# 1. 英語版を最適化（5並列）
python scripts/optimize_glossary_descriptions.py --lang en --workers 5

# 2. 日本語版を最適化
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# 3. 特定のファイルのみ
python scripts/optimize_glossary_descriptions.py \
  --lang en \
  --file "Machine-Learning.md"

# 4. ドライラン（変更なし、プレビューのみ）
python scripts/optimize_glossary_descriptions.py --lang en --dry-run
```

---

## 翻訳

### 🌟 推奨: シンプル翻訳

**スクリプト**: `scripts/translate_glossary_en_to_ja.py`

**特徴**:
- 英語→日本語翻訳
- フロントマター自動生成（e-title, term, url）
- 内部リンク自動変換（/en/glossary/ → /ja/glossary/）
- CSVステータス自動更新（Status_JA → completed）

**使用方法**:

```bash
# 1. 単一ファイル翻訳
python scripts/translate_glossary_en_to_ja.py --one-file Active-Learning.md

# 2. 全ファイル翻訳（5並列）
python scripts/translate_glossary_en_to_ja.py --workers 5

# 3. 特定範囲を翻訳
python scripts/translate_glossary_en_to_ja.py --start 0 --end 10 --workers 3

# 4. ドライラン
python scripts/translate_glossary_en_to_ja.py --dry-run
```

**自動追加されるフィールド**:

```yaml
# 英語版
title: "Active Learning"
translationKey: active-learning

# 日本語版（自動生成）
title: "Active Learning（アクティブラーニング）"
translationKey: active-learning
e-title: "Active Learning"  # ✅ 自動追加
term: "あくてぃぶらーにんぐ"  # ✅ 自動追加（Claude API生成）
url: "/ja/glossary/Active-Learning/"  # ✅ 自動追加
```

---

### 並列翻訳（高速）

**スクリプト**: `scripts/parallel_translate_continuous.py`

**使用方法**:

```bash
# 未翻訳ファイルを自動検出して並列翻訳（5並列）
python scripts/parallel_translate_continuous.py --workers 5

# 特定ファイルを並列翻訳
python scripts/parallel_translate_continuous.py \
  File1.md File2.md File3.md \
  --workers 3
```

---

### 翻訳パイプライン（FlowHunt用）

**スクリプト**: `scripts/pipeline_translate.py`

**特徴**:
- FlowHunt出力のクリーンアップ
- 翻訳
- エンリッチメント
- ステップごとの実行可能

**使用方法**:

```bash
# 新規ファイルを自動検出して全工程実行
python scripts/pipeline_translate.py --auto

# 特定ファイルを処理
python scripts/pipeline_translate.py --file Copilot.md

# 特定ステップから開始
python scripts/pipeline_translate.py --file Copilot.md --from-step translate

# ドライラン
python scripts/pipeline_translate.py --auto --dry-run
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

---

### 日本語用語の読み修正

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

### 🌟 推奨: 並列リンク構築

**スクリプト**: `scripts/linkbuilding_parallel.py`

**特徴**:
- 並列処理で高速
- 用語集へのリンクを自動挿入
- バリエーション対応（複数形、大文字小文字など）
- 既存リンクは保持

**使用方法**:

```bash
# 1. 英語ブログ記事にリンク追加（5並列）
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/blog \
    --glossary-dir content/en/glossary \
    --workers 5

# 2. 日本語ブログ記事にリンク追加
python scripts/linkbuilding_parallel.py \
    --content-dir content/ja/blog \
    --glossary-dir content/ja/glossary \
    --workers 5

# 3. 用語集記事同士のリンク
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/glossary \
    --glossary-dir content/en/glossary \
    --workers 5

# 4. ドライラン（変更なし）
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/blog \
    --glossary-dir content/en/glossary \
    --dry-run
```

---

### 危険用語（Danger Terms）denylist（自動内部リンク除外）

用語集の自動リンクで、一般語（例: make / did など）が誤リンクするのを防ぐための除外リストです。

**編集する場所（権威）**:
- `databases/danger_terms_en.csv`
- `databases/danger_terms_ja.csv`

**レポート（生成物）**:
- `docs/danger_terms.md`

**レポート再生成（CSVはマージ更新）**:

```bash
# 英語
python3 scripts/generate_danger_terms.py --lang en

# 日本語
python3 scripts/generate_danger_terms.py --lang ja

# 例: 自動判定を厳しく/緩くしたい場合（スコア閾値）
python3 scripts/generate_danger_terms.py --lang en --min-score 70
```

**リンク挿入スクリプトでの扱い**:
- `scripts/enrich_glossary_blog.py` / `scripts/add_links_from_database.py` は、デフォルトで `databases/danger_terms_{en,ja}.csv` を読み込みます。
- 任意のdenylistを使う場合は `--denylist /path/to/custom.csv` を指定します。

---

### 用語集エンリッチメント

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

---

## ブログ記事メンテナンス

### ツールチップ削除

**課題**: 日本語ブログ記事に残っている複雑なツールチップ構文

**ツールチップ例**:
```markdown
[ナレッジベース](/ja/glossary/Knowledge-Base/[顧客リスク評価](/ja/glossary/Risk-Assessment--Customer-/ "tooltip") "tooltip")
```

**手動削除方法**:

```bash
# 1. ファイルを開く
vim content/ja/blog/knowledge-base-faq-guide-2025.md

# 2. ツールチップを検索
/\[.*\](/.*/ ".*")

# 3. 修正
# Before: [text](/path/[nested](/nested-path/ "tooltip")](/path/ "tooltip"))
# After:  [text](/path/)
```

**一括修正スクリプト**: `scripts/remove_tooltips.py`

```bash
# 日本語ブログのツールチップを削除
python scripts/remove_tooltips.py \
    --content-dir content/ja/blog

# 英語ブログのツールチップを削除
python scripts/remove_tooltips.py \
    --content-dir content/en/blog
```

---

### ファイル名とリンク修正

**例**: `Risk-Assessment--Customer-.md` → `Risk-Assessment.md`

**手順**:

```bash
# 1. 新ファイル作成（フロントマター修正）
# - title: "Risk Assessment (Customer)" → "Risk Assessment"
# - translationKey: "Risk-Assessment--Customer-" → "Risk-Assessment"
# - url: "/ja/glossary/Risk-Assessment--Customer-/" → "/ja/glossary/Risk-Assessment/"

# 2. 全ファイルのリンクを置換
grep -r "Risk-Assessment--Customer-" content/ | cut -d: -f1 | sort -u

# 3. 一括置換（macOS）
find content -name "*.md" -type f -exec \
  sed -i '' 's|/glossary/Risk-Assessment--Customer-/|/glossary/Risk-Assessment/|g' {} \;

# 4. 一括置換（Linux）
find content -name "*.md" -type f -exec \
  sed -i 's|/glossary/Risk-Assessment--Customer-/|/glossary/Risk-Assessment/|g' {} \;

# 5. 古いファイル削除
rm content/en/glossary/Risk-Assessment--Customer-.md
rm content/ja/glossary/Risk-Assessment--Customer-.md
```

---

### ツールチップからリンクへ変換

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

### CSVステータス管理

**スクリプト**: `scripts/manage_glossary_status.py`

```bash
# 現在のステータスを確認
python scripts/manage_glossary_status.py --status

# 特定ファイルのステータスを更新
python scripts/manage_glossary_status.py \
  --update-file Baidu.md \
  --status-en completed

# 一括ステータス更新
python scripts/manage_glossary_status.py --bulk-update-en completed

# 未作成記事をリスト
python scripts/manage_glossary_status.py --list-pending
```

---

### 記事比較

**スクリプト**: `scripts/compare_articles.py`

```bash
# 英語版と日本語版のアウトライン比較
python scripts/compare_articles.py \
    --en-file content/en/glossary/Machine-Learning.md \
    --ja-file content/ja/glossary/Machine-Learning.md
```

---

### かなインデックス追加

**スクリプト**: `scripts/add_kana_index.py`

```bash
# 日本語用語集にかなインデックスを追加
python scripts/add_kana_index.py --glossary-dir content/ja/glossary
```

---

### 重複記事の検出と統合

**スクリプト**: `scripts/merge_duplicate_glossaries.py`

```bash
# 重複検出
python scripts/merge_duplicate_glossaries.py --detect

# 統合実行
python scripts/merge_duplicate_glossaries.py --merge
```

---

## 推奨ワークフロー

### 🎯 新規記事作成から公開まで（完全版）

```bash
# ===============================================
# 1. CSVから記事作成（英語）
# ===============================================
python scripts/batch_create_from_csv.py --workers 5

# ===============================================
# 2. descriptionを最適化（英語）
# ===============================================
python scripts/optimize_glossary_descriptions.py --lang en --workers 5

# ===============================================
# 3. 内部リンク追加（英語用語集同士）
# ===============================================
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/glossary \
    --glossary-dir content/en/glossary \
    --workers 5

# ===============================================
# 4. 翻訳（英語→日本語）
# ===============================================
python scripts/translate_glossary_en_to_ja.py --workers 5

# ===============================================
# 5. descriptionを最適化（日本語）
# ===============================================
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# ===============================================
# 6. 用語読み修正（日本語）
# ===============================================
python scripts/fix_term_readings_ja.py --ja-dir content/ja/glossary

# ===============================================
# 7. 内部リンク追加（日本語用語集同士）
# ===============================================
python scripts/linkbuilding_parallel.py \
    --content-dir content/ja/glossary \
    --glossary-dir content/ja/glossary \
    --workers 5

# ===============================================
# 8. かなインデックス追加（日本語）
# ===============================================
python scripts/add_kana_index.py --glossary-dir content/ja/glossary

# ===============================================
# 9. ブログ記事にリンク追加
# ===============================================
# 英語ブログ
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/blog \
    --glossary-dir content/en/glossary \
    --workers 5

# 日本語ブログ
python scripts/linkbuilding_parallel.py \
    --content-dir content/ja/blog \
    --glossary-dir content/ja/glossary \
    --workers 5

# ===============================================
# 10. 最終確認
# ===============================================
# Hugoビルドテスト
hugo server -D

# リンク切れチェック
# （ブラウザで確認）
```

---

### 🚀 クイックスタート（5記事のテスト）

```bash
# 1. 記事作成（5件）
python scripts/batch_create_from_csv.py --start 0 --end 5 --workers 3

# 2. 翻訳（5件）
python scripts/translate_glossary_en_to_ja.py --start 0 --end 5 --workers 3

# 3. 確認
ls -l content/en/glossary/*.md | tail -5
ls -l content/ja/glossary/*.md | tail -5
```

---

### 📊 バッチ処理（100記事）

```bash
# 1. 記事作成（100件、並列5）
python scripts/batch_create_from_csv.py --start 0 --end 100 --workers 5

# 推定時間: 約75分（45秒/記事 × 100 ÷ 5並列）
# 推定コスト: 約$20-25（$0.20-0.25/記事）

# 2. 翻訳（100件、並列5）
python scripts/translate_glossary_en_to_ja.py --start 0 --end 100 --workers 5

# 推定時間: 約60分（30秒/記事 × 100 ÷ 5並列）
# 推定コスト: 約$15-20（$0.15-0.20/記事）

# 3. 最適化・リンク構築
python scripts/optimize_glossary_descriptions.py --lang en --workers 5
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5
python scripts/linkbuilding_parallel.py \
    --content-dir content/en/glossary \
    --glossary-dir content/en/glossary \
    --workers 5
python scripts/linkbuilding_parallel.py \
    --content-dir content/ja/glossary \
    --glossary-dir content/ja/glossary \
    --workers 5
```

---

## トラブルシューティング

### API Keyエラー

```
エラー: ANTHROPIC_API_KEY または CLAUDE_API_KEY が設定されていません
```

**解決方法**:

```bash
# 1. .envファイル確認
cat .env | grep API_KEY

# 2. 環境変数確認
echo $ANTHROPIC_API_KEY

# 3. .envファイル作成（存在しない場合）
cat > .env << 'EOF'
ANTHROPIC_API_KEY="sk-ant-api03-your-key-here"
CLAUDE_API_KEY="sk-ant-api03-your-key-here"
EOF

# 4. 権限確認
chmod 600 .env
```

---

### 並列処理でエラー

**症状**: `Rate limit exceeded`

**解決方法**:

```bash
# 並列数を減らす
# 5並列 → 3並列
python scripts/batch_create_from_csv.py --workers 3

# または2並列
python scripts/batch_create_from_csv.py --workers 2
```

---

### ファイルが見つからない

**症状**: `FileNotFoundError: content/en/glossary/`

**解決方法**:

```bash
# プロジェクトルートから実行
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
python scripts/batch_create_from_csv.py

# ディレクトリ作成（存在しない場合）
mkdir -p content/en/glossary
mkdir -p content/ja/glossary
```

---

### 語数が目標に達しない

**症状**: 記事が2,000語程度で止まる

**解決方法**:

```python
# スクリプトの max_tokens を増やす
# 現在: max_tokens=16000
# 変更: max_tokens=20000

# または temperature を下げる
# 現在: temperature=0.1
# 変更: temperature=0.05
```

---

### 文法チェック失敗

**症状**: `⚠️ 文法警告: 'What is a/an Topic?' が見つかりません`

**原因**: 冠詞判定ロジックの誤作動

**解決方法**:

```python
# scripts/batch_create_from_csv.py の needs_article() 関数を確認
# 特定のキーワードを uncountable リストに追加

uncountable = ['forecasting', 'analysis', 'learning', 'intelligence', 
               'processing', 'management', 'optimization', 'automation', 
               'segmentation', 'modeling', 'mining', 'clustering',
               'your-keyword-here']  # ← 追加
```

---

### CSVステータスが更新されない

**症状**: 記事作成成功後も`Status_EN`が`pending`のまま

**解決方法**:

```bash
# 手動でステータス更新
python scripts/manage_glossary_status.py \
  --update-file Active-Learning.md \
  --status-en completed

# または一括更新
python scripts/manage_glossary_status.py --bulk-update-en completed
```

---

### 翻訳で e-title, term, url が追加されない

**症状**: 日本語版フロントマターにフィールドが不足

**解決方法**:

```bash
# 最新の翻訳スクリプトを使用
python scripts/translate_glossary_en_to_ja.py --one-file Active-Learning.md

# フィールド確認
head -25 content/ja/glossary/Active-Learning.md | grep -E "(e-title|term|url):"

# 期待される出力:
# e-title: "Active Learning"
# term: "あくてぃぶらーにんぐ"
# url: "/ja/glossary/Active-Learning/"
```

---

## コスト見積もり

### 1記事あたりのコスト

| 項目 | トークン数 | コスト |
|------|-----------|--------|
| 記事作成（英語） | 15,000-16,000 | $0.20-0.25 |
| 翻訳（日本語） | 12,000-13,000 | $0.15-0.20 |
| 合計 | 27,000-29,000 | $0.35-0.45 |

### バッチ処理コスト

| 記事数 | 記事作成 | 翻訳 | 合計 |
|--------|---------|------|------|
| 10記事 | $2.00-2.50 | $1.50-2.00 | $3.50-4.50 |
| 50記事 | $10-12.50 | $7.50-10.00 | $17.50-22.50 |
| 100記事 | $20-25 | $15-20 | $35-45 |
| 500記事 | $100-125 | $75-100 | $175-225 |

---

## パフォーマンス最適化

### 並列数の推奨値

| タスク | 推奨並列数 | 理由 |
|--------|-----------|------|
| 記事作成 | 3-5 | API制限とコスト最適化 |
| 翻訳 | 5-7 | 翻訳はトークン数が少ない |
| リンク構築 | 5-10 | APIを使わないため制限なし |

### 処理時間の見積もり

```bash
# 記事作成: 45秒/記事
# 100記事 ÷ 5並列 = 20記事/並列 × 45秒 = 15分

# 翻訳: 30秒/記事
# 100記事 ÷ 5並列 = 20記事/並列 × 30秒 = 10分

# リンク構築: 5秒/記事
# 100記事 ÷ 10並列 = 10記事/並列 × 5秒 = 50秒
```

---

## 関連ドキュメント

- **翻訳マニュアル**: `docs/GLOSSARY_CREATION_TRANSLATION_MANUAL.md`
- **最適化ガイド**: `GLOSSARY_OPTIMIZATION_GUIDE.md`
- **プロジェクト概要**: `README.md`

---

## 更新履歴

- **2025-12-21 (v2.0)**: 大規模改訂
  - 記事作成スクリプトの詳細追加（batch_create_from_csv.py, api_batch_create_v3.py）
  - ブログメンテナンスセクション追加
  - ファイル名修正手順追加
  - コスト見積もりとパフォーマンス最適化を追加
  - トラブルシューティング拡張

- **2025-12-20 (v1.0)**: 初版作成
  - 記事作成、翻訳、内部リンクの最新スクリプトを整理
  - .env対応を追加
  - 推奨ワークフローを追加
