---
name: internal-linking
description: "HTML後処理方式による内部リンクパイプライン。キーワード辞書更新、Hugoビルド、リンク付与、検証までの全工程。"
---

# 内部リンクパイプライン

HTML後処理方式（`linkbuilding_parallel.py`）による内部リンク管理。
**Markdownへの直接リンク挿入は禁止。**

## 重要ルール

- リンク先は **`/glossary/` のみ**（`/services/` にはリンクしない）
- `content/` のMarkdownはクリーンに保つ（リンクなし）
- `public/` は生成物（Git管理しない、手編集しない）
- 禁止スクリプト: `add_internal_links.py`, `add_links_from_database.py`, `remove_internal_links.py`（全て archived）

## 現在のキーワード辞書状態

!`ls -la data/linkbuilding/`

## 現在のDenylist（除外語）

### EN
!`cat databases/danger_terms_en.csv`

### JA
!`cat databases/danger_terms_ja.csv`

## 標準ワークフロー

### ステップ1: キーワード辞書更新（新記事追加後）
```bash
# EN
python3 scripts/extract_automatic_links.py \
  --content-dir content/en/ \
  --output data/linkbuilding/en_automatic.json

# JA
python3 scripts/extract_automatic_links.py \
  --content-dir content/ja/ \
  --output data/linkbuilding/ja_automatic.json
```

### ステップ2: Hugoビルド
```bash
hugo --destination public --cleanDestinationDir
```

### ステップ3: 内部リンク付与
```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --max-workers 4
```

### ステップ4: 検証
```bash
# リンク数確認
grep -r 'data-lb="1"' public/en/ | wc -l
grep -r 'data-lb="1"' public/ja/ | wc -l

# リンク切れチェック
python3 scripts/check_internal_links.py --public-dir public --language ja
python3 scripts/check_internal_links.py --public-dir public --language en
```

## Dry-run（テスト実行）
```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --dry-run
```

## 単一言語のみ処理
```bash
# ENのみ
python3 scripts/linkbuilding.py \
  -k data/linkbuilding/en.yaml \
  -a data/linkbuilding/en_automatic.json \
  -d public/en \
  --language EN \
  --denylist databases/danger_terms_en.csv \
  --max-links 15 --max-keyword 1 --max-url 3

# JAのみ
python3 scripts/linkbuilding.py \
  -k data/linkbuilding/ja.yaml \
  -a data/linkbuilding/ja_automatic.json \
  -d public/ja \
  --language JA \
  --denylist databases/danger_terms_ja.csv \
  --max-links 15 --max-keyword 1 --max-url 3
```

## ローカルで内部リンク付きページを確認
```bash
# 1. 静的ビルド
hugo --baseURL http://localhost:1313/ --destination public --cleanDestinationDir

# 2. リンク付与
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases

# 3. 静的サーバで配信
python3 -m http.server 1313 --bind 127.0.0.1 --directory public
```

## Denylist管理

誤リンクを防止する除外語を追加:
```bash
# databases/danger_terms_ja.csv に手動追加
echo "用語,normalized,reason,score,source" >> databases/danger_terms_ja.csv

# 自動判定で再生成
python3 scripts/generate_danger_terms.py --lang en
python3 scripts/generate_danger_terms.py --lang ja
```

## 詳細ドキュメント

!`cat docs/INTERNAL_LINKING_QUICK_START.md`

## トラブルシューティング

- **リンクが増えない**: キーワード辞書が古い → `extract_automatic_links.py` 再実行
- **リンクが重複**: 同じHTMLに複数回処理 → `hugo --cleanDestinationDir` で再生成してから再実行
- **ENだけリンクが少ない**: ENは `public/en/` 配下のため、`linkbuilding.py -d public/en` を別途実行
- **`What? faq already exists?`**: TOMLフロントマターのFAQを `[[faq]]` に修正
- **処理が遅い**: `--max-workers 2` でワーカー数を減らす
