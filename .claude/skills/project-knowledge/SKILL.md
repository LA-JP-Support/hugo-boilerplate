---
name: hugo-boilerplate-project-knowledge
description: "SmartWeb Hugo Boilerplateプロジェクトの基本ルール、ディレクトリ構造、禁止事項。全作業の前提知識として自動的に適用される。"
user-invocable: false
---

# SmartWeb Hugo Boilerplate プロジェクト知識

## プロジェクト概要

SmartWeb（smartweb.jp）のHugo静的サイト。日本語（主言語）＋英語のバイリンガル構成。
AI/カスタマーサポート関連のBlog、Glossary（用語集）、Service、Support、YouTube記事を運用。

## 絶対遵守ルール（5大ルール）

1. **`public/` は都度生成する成果物** -- Git管理しない、手編集しない
2. **内部リンクは全てHTML後処理で作成** -- Markdownに直接リンクを挿入しない
3. **Markdownを書き換えるスクリプトは原則禁止** -- `--dry-run` → 少数テスト → 全体適用の3段階
4. **内部リンクのリンク先は `/glossary/` に統一** -- `/services/` にはリンクしない
5. **編集前にバックアップを取る** -- `git commit` またはディレクトリコピー

## ディレクトリ構成

!`ls -la`

### 主要ディレクトリ

| ディレクトリ | 層 | 説明 |
|------------|------|------|
| `content/{en,ja}/` | Source | Markdownコンテンツ（Git管理） |
| `layouts/` | Source | Hugoテンプレート |
| `data/linkbuilding/` | Source | 内部リンクキーワード辞書（JSON/YAML） |
| `databases/` | Source | CSV管理データ（リンクDB、禁止用語等） |
| `docs/` | Source | プロジェクトドキュメント（22件） |
| `scripts/` | Source | Python/Bashスクリプト（90+） |
| `static/images/` | Source | 画像ファイル |
| `archetypes/` | Source | Hugo記事テンプレート |
| `public/` | Artifact | 生成HTML（Git管理しない） |
| `support-docs/` | Source | サポートドキュメントサイト（独立Hugoプロジェクト） |

### コンテンツタイプ一覧

| タイプ | パス | フロントマター形式 | 特記 |
|--------|------|-----------------|------|
| Blog | `content/{en,ja}/blog/` | YAML (`---`) | 標準ブログ記事 |
| Blog YouTube | `content/{en,ja}/blog/` | YAML + `layout: single-youtube` | YouTube動画紹介 |
| Glossary | `content/{en,ja}/glossary/` | YAML (`---`) | 用語集。JA版は `e-title`, `term`, `url` が追加 |
| Service | `content/{en,ja}/services/` | YAML (`---`) | サービスページ |
| Support | `content/{en,ja}/support/` | YAML (`---`) | ヘルプ記事。`type: support`, `weight` 必須 |

## 禁止スクリプト（使用禁止）

以下は `scripts/archived_markdown_based/` に移動済み:
- `add_internal_links.py` -- Markdown直接編集方式（廃止）
- `add_links_from_database.py` -- 同上
- `remove_internal_links.py` -- 同上

破壊的スクリプト（バックアップ必須、通常は使用しない）:
- `sanitize_markdown.py` -- リンクを全て剥がす
- `scrub_blog_posts.py` -- 同上
- `clean_en_content.py` -- `<strong>` タグ再導入の副作用あり

## 参考見出し規約

- 英語版: `## References`
- 日本語版: `## 参考資料`

## 詳細ドキュメント索引

!`cat docs/00_START_HERE.md`
