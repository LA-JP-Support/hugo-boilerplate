# Support Docs 内部リンク（用語集へのリンク）

## 概要

support-docs のHTMLファイルに、メインサイトの用語集（glossary）への外部リンクを自動追加するスクリプトです。

## 使用方法

### 1. Hugoビルド

```bash
cd support-docs
hugo --gc --minify
```

### 2. リンク追加

```bash
# プロジェクトルートから実行
python3 scripts/linkbuilding_support_docs.py
```

### オプション

| オプション | デフォルト | 説明 |
|-----------|-----------|------|
| `--linkbuilding-yaml` | `data/linkbuilding/ja.yaml` | キーワード辞書ファイル |
| `--public-dir` | `support-docs/public` | HTMLファイルのディレクトリ |
| `--base-url` | `https://smartweb.co.jp` | 外部リンクのベースURL |
| `--language` | `ja` | 処理する言語 |
| `--dry-run` | - | 変更を書き込まない（テスト用） |
| `--max-links` | `30` | 1ページあたりの最大リンク数 |
| `--max-keyword` | `2` | 1キーワードあたりの最大リンク数 |

### 例

```bash
# ドライラン（テスト）
python3 scripts/linkbuilding_support_docs.py --dry-run

# 最大リンク数を変更
python3 scripts/linkbuilding_support_docs.py --max-links 50 --max-keyword 3
```

## 仕組み

1. `data/linkbuilding/ja.yaml` から用語集キーワードのみを抽出
2. `support-docs/public/ja/` 内のHTMLファイルを処理
3. キーワードにマッチするテキストを `<a href="https://smartweb.co.jp/ja/glossary/...">` でラップ
4. リンクには `target="_blank"` と `rel="noopener"` を付与

## キーワード辞書

メインサイトと同じ `data/linkbuilding/ja.yaml` を使用します。
用語集URL（`/glossary/` を含むURL）のみが対象です。

## 注意事項

- Hugoビルド後に実行する必要があります
- `public/` ディレクトリのHTMLを直接編集します
- 再ビルドするとリンクは消えるので、デプロイ前に再実行が必要です

## Amplify/CI統合

`amplify.yml` に以下を追加：

```yaml
build:
  commands:
    # support-docs ビルド
    - cd support-docs && hugo --gc --minify
    # リンク追加
    - python3 scripts/linkbuilding_support_docs.py
```
