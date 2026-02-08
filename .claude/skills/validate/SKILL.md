---
name: validate
description: "コンテンツ品質検証。フロントマター検証、翻訳整合性チェック、テーブル構文チェック、Hugoビルドテスト、内部リンク検証を実行。"
---

# バリデーション・品質チェック

コンテンツの品質を検証する各種スクリプトとチェック手順。
対象: $ARGUMENTS

## 検証対象の現在の状態

### コンテンツファイル数
!`echo "EN glossary: $(find content/en/glossary -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files"`
!`echo "JA glossary: $(find content/ja/glossary -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files"`
!`echo "EN blog: $(find content/en/blog -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files"`
!`echo "JA blog: $(find content/ja/blog -name '*.md' 2>/dev/null | wc -l | tr -d ' ') files"`

## 1. フロントマター検証

最も頻繁に使用する検証。コンテンツタイプを自動判定。

```bash
# 単一ファイル
python scripts/validate_frontmatter.py {filepath}

# ディレクトリ単位
python scripts/validate_frontmatter.py content/ja/glossary/

# 全コンテンツ
python scripts/validate_frontmatter.py --all

# translationKey の EN/JA 整合性
python scripts/validate_frontmatter.py --check-translations

# エラーのみ表示
python scripts/validate_frontmatter.py --errors-only content/ja/blog/
```

### 検証内容
- 必須フィールドの有無（タイプ別）
- フィールドの型チェック（str/list/bool/int）
- JA glossary 固有フィールド（`e-title`, `term`, `url`）
- `type`/`layout` の値検証
- `description` 長さ警告（160文字超）
- `translationKey` EN↔JA 整合性

## 2. テーブル構文検証

Markdownテーブルの構文エラーを検出・修正。

```bash
# 検証のみ
python scripts/validate_tables.py --path content/ja/glossary/

# 修正も実行
python scripts/validate_tables.py --fix --path content/ja/glossary/
```

## 3. 翻訳整合性検証

```bash
python scripts/validate_translation.py databases/glossary-keywords-ja.csv content/ja/glossary
```

## 4. Hugoビルドテスト

```bash
# エラーチェック
hugo --minify 2>&1 | head -50

# ローカルサーバで目視確認
hugo server -D
```

## 5. 内部リンク検証（ビルド後）

```bash
python3 scripts/check_internal_links.py --public-dir public --language ja
python3 scripts/check_internal_links.py --public-dir public --language en

# リンク数確認
grep -r 'data-lb="1"' public/en/ | wc -l
grep -r 'data-lb="1"' public/ja/ | wc -l
```

## 6. 太字構文検証（日本語翻訳品質）

```bash
python scripts/detect_bold_render_errors.py
python scripts/detect_bold_issues.py
```

## 7. CSVステータス確認

```bash
python scripts/manage_glossary_status.py --status
python scripts/manage_glossary_status.py --list-pending
```

## 推奨: 全体検証フロー

全体を一括検証する場合:

```bash
# 1. フロントマター全体検証
python scripts/validate_frontmatter.py --all --errors-only

# 2. 翻訳キー整合性
python scripts/validate_frontmatter.py --check-translations

# 3. テーブル構文
python scripts/validate_tables.py --path content/ja/

# 4. Hugoビルドテスト
hugo --minify

# 5. 内部リンク検証（ビルド後のみ）
python3 scripts/check_internal_links.py --public-dir public --language ja
```
