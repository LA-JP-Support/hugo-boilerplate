---
name: glossary-pipeline
description: "用語集（Glossary）のバッチ作成パイプライン。CSV→英語記事作成→最適化→翻訳→読み修正→ビルド→かなインデックス→内部リンクの10ステップ一括ワークフロー。"
---

# 用語集バッチパイプライン（10ステップ）

CSVから用語集記事を一括作成し、翻訳・最適化・内部リンクまで完了するフルパイプライン。
対象: $ARGUMENTS

## 現在のCSV/コンテンツ状態

!`python3 scripts/manage_glossary_status.py --status 2>/dev/null || echo "ステータススクリプト未対応 - 以下のファイル数を参照"`
!`echo "EN glossary: $(find content/en/glossary -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files"`
!`echo "JA glossary: $(find content/ja/glossary -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files"`

## 10ステップパイプライン

### ステップ 1: CSVから記事作成（英語）
```bash
python scripts/batch_create_from_csv.py --workers 5

# テスト（5件のみ）
python scripts/batch_create_from_csv.py --start 0 --end 5 --workers 3

# 特定カテゴリのみ
python scripts/batch_create_from_csv.py --category "AI Companies & Products"

# ドライラン（コスト見積もりのみ）
python scripts/batch_create_from_csv.py --test
```

### ステップ 2: description最適化（英語）
```bash
python scripts/optimize_glossary_descriptions.py --lang en --workers 5

# ドライラン
python scripts/optimize_glossary_descriptions.py --lang en --dry-run
```

### ステップ 3: 翻訳（英語→日本語）
```bash
python scripts/translate_glossary_en_to_ja.py \
  --skip-existing \
  --max-workers 5 \
  --model claude-sonnet-4-5-20250929 \
  --style-guide docs/TRANSLATION_GUIDELINES.md

# 単一ファイル
python scripts/translate_glossary_en_to_ja.py --one-file {filename}.md
```

### ステップ 4: description最適化（日本語）
```bash
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5
```

### ステップ 5: 用語読み修正（日本語）
```bash
python scripts/fix_term_readings_ja.py --ja-dir content/ja/glossary
```

### ステップ 6: Hugoビルド
```bash
hugo --destination public --cleanDestinationDir
```

### ステップ 7: かなインデックス追加（日本語）
```bash
python scripts/add_kana_index.py --glossary-dir content/ja/glossary
```

### ステップ 8: キーワード辞書更新
```bash
python3 scripts/extract_automatic_links.py \
  --content-dir content/en/ \
  --output data/linkbuilding/en_automatic.json

python3 scripts/extract_automatic_links.py \
  --content-dir content/ja/ \
  --output data/linkbuilding/ja_automatic.json
```

### ステップ 9: 内部リンク追加（HTML後処理）
```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --max-workers 4
```

### ステップ 10: 最終確認
```bash
# ビルド確認
hugo server -D

# フロントマター検証
python scripts/validate_frontmatter.py --all --errors-only

# 翻訳キー整合性
python scripts/validate_frontmatter.py --check-translations

# リンク数確認
grep -r 'data-lb="1"' public/en/ | wc -l
grep -r 'data-lb="1"' public/ja/ | wc -l
```

## クイックスタート（5記事テスト）

```bash
# 1. 作成
python scripts/batch_create_from_csv.py --start 0 --end 5 --workers 3

# 2. 翻訳
python scripts/translate_glossary_en_to_ja.py --start 0 --end 5 --workers 3

# 3. 確認
ls -l content/en/glossary/*.md | tail -5
ls -l content/ja/glossary/*.md | tail -5
```

## コスト見積もり

| 記事数 | 作成（EN） | 翻訳（JA） | 合計 | 時間（5並列） |
|--------|-----------|-----------|------|-------------|
| 5 | $1.00-1.25 | $0.75-1.00 | ~$2 | ~5分 |
| 50 | $10-12.50 | $7.50-10 | ~$20 | ~25分 |
| 100 | $20-25 | $15-20 | ~$40 | ~50分 |

## 注意事項

- **`--dry-run`を先に実行**: 特にdescription最適化と読み修正は必ず先にドライランで確認
- **APIレート制限**: workers数は3-5を推奨（5超はレート制限リスク）
- **バックアップ**: パイプライン開始前に `git commit` で現状を保存
- **ステップ6前にステップ5まで完了**: ビルドはcontent/の最終状態で行う

## スクリプト詳細リファレンス

!`cat docs/SCRIPTS_USAGE_GUIDE.md`
