# FlowHunt Glossary Translation Pipeline Manual / FlowHunt 用語集翻訳パイプライン マニュアル

**Version / バージョン:** 1.2.1  
**Last Updated / 最終更新:** 2025-12-04  
**Author / 作成者:** Development Team

---

## Table of Contents / 目次

1. [Overview / 概要](#overview--概要)
2. [System Requirements / システム要件](#system-requirements--システム要件)
3. [Directory Structure / ディレクトリ構成](#directory-structure--ディレクトリ構成)
4. [Configuration Files / 設定ファイル](#configuration-files--設定ファイル)
5. [Pipeline Workflow / パイプラインワークフロー](#pipeline-workflow--パイプラインワークフロー)
6. [Script Reference / スクリプトリファレンス](#script-reference--スクリプトリファレンス)
7. [Operation Guide / 操作ガイド](#operation-guide--操作ガイド)
8. [Troubleshooting / トラブルシューティング](#troubleshooting--トラブルシューティング)
9. [Changelog / 変更履歴](#changelog--変更履歴)

---

## Overview / 概要

### English

The FlowHunt Glossary Translation Pipeline is an automated system for translating English glossary articles to Japanese. It handles the entire workflow from draft cleanup to publication, including:

- Cleaning up FlowHunt-generated content
- Adding keywords and internal links
- Translating content using Claude API
- Adding Japanese reading metadata (kana index)
- Validating translation completeness

### 日本語

FlowHunt用語集翻訳パイプラインは、英語の用語集記事を日本語に翻訳するための自動化システムです。ドラフトのクリーンアップから公開まで、以下を含むワークフロー全体を処理します：

- FlowHunt生成コンテンツのクリーンアップ
- キーワードと内部リンクの追加
- Claude APIを使用したコンテンツの翻訳
- 日本語読み仮名メタデータ（かなインデックス）の追加
- 翻訳完全性の検証

---

## System Requirements / システム要件

### Dependencies / 依存関係

| Package | Version | Purpose / 用途 |
|---------|---------|----------------|
| Python | 3.9+ | Script execution / スクリプト実行 |
| Hugo | 0.152+ | Static site generation / 静的サイト生成 |
| anthropic | latest | Claude API client / Claude APIクライアント |
| python-dotenv | latest | Environment variable management / 環境変数管理 |
| pykakasi | latest | Japanese reading conversion / 日本語読み変換 |

### Environment Variables / 環境変数

Create a `.env` file in the project root:
プロジェクトルートに `.env` ファイルを作成：

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Directory Structure / ディレクトリ構成

```
hugo-boilerplate/
├── content/
│   ├── en/glossary/          # Published English articles / 公開済み英語記事
│   └── ja/glossary/          # Published Japanese articles / 公開済み日本語記事
├── content-drafts/
│   └── en/                   # English drafts / 英語ドラフト
│       └── clean/            # Cleaned drafts / クリーンアップ済みドラフト
├── config/
│   ├── keyword_dictionary.json      # EN keyword dictionary / 英語キーワード辞書
│   └── keyword_dictionary_ja.json   # JA keyword dictionary / 日本語キーワード辞書
├── scripts/
│   ├── pipeline_translate.py        # Main pipeline script / メインパイプライン
│   ├── enrich_glossary.py           # Keyword & link enrichment / キーワード・リンク追加
│   ├── translate_glossary_en_to_ja.py  # Translation script / 翻訳スクリプト
│   ├── cleanup_flowhunt_output.py   # Content cleanup / コンテンツクリーンアップ
│   ├── add_kana_index.py            # Kana index addition / かなインデックス追加
│   ├── fix_term_readings_ja.py      # Term reading fix / term読み修正
│   └── compare_outline.py           # Outline comparison / アウトライン比較
├── logs/                     # Pipeline logs / パイプラインログ
└── docs/
    └── MANUAL.md             # This manual / このマニュアル
```

---

## Configuration Files / 設定ファイル

### Keyword Dictionary / キーワード辞書

#### English (`config/keyword_dictionary.json`)

```json
{
  "bot avatar": {
    "keywords": ["bot avatar", "chatbot persona", "digital human"],
    "link": "/en/glossary/bot-avatar/",
    "aliases": ["bot avatar", "bot avatars"]
  }
}
```

#### Japanese (`config/keyword_dictionary_ja.json`)

```json
{
  "AIコパイロット": {
    "keywords": ["AIコパイロット", "コパイロット", "AI支援"],
    "link": "/ja/glossary/copilot/",
    "aliases": ["AIコパイロット", "コパイロット", "AI Copilot"]
  }
}
```

### Dictionary Entry Fields / 辞書エントリフィールド

| Field | Description (EN) | 説明 (JA) |
|-------|------------------|-----------|
| `keywords` | Keywords to add to frontmatter | フロントマターに追加するキーワード |
| `link` | Internal link URL | 内部リンクURL |
| `aliases` | Text patterns to match for linking | リンク対象のテキストパターン |

**Important / 重要:**  
Links are only added if the target page exists. Non-existent pages are automatically skipped.  
リンクは対象ページが存在する場合のみ追加されます。存在しないページは自動的にスキップされます。

---

## Pipeline Workflow / パイプラインワークフロー

### Pipeline Steps / パイプラインステップ

| Step | Name | Description (EN) | 説明 (JA) |
|------|------|------------------|-----------|
| 1 | `cleanup` | Clean FlowHunt output | FlowHunt出力のクリーンアップ |
| 2 | `enrich_en` | Add EN keywords & links | 英語キーワード・リンク追加 |
| 3 | `copy_to_content` | Copy to content/en/glossary/ | content/en/glossary/へコピー |
| 4 | `translate` | Translate to Japanese via Claude API | Claude APIで日本語翻訳 |
| 5 | `enrich_ja` | Add JA keywords & links | 日本語キーワード・リンク追加 |
| 6 | `add_kana` | Add kana reading metadata | 読み仮名メタデータ追加 |
| 7 | `fix_term` | Fix term readings (kanji → kana) | term読み修正（漢字→かな） |
| 8 | `compare` | Compare EN/JA outlines | EN/JA見出し差分チェック |
| 9 | `refresh_links` | Refresh all internal links | 全記事の内部リンク更新 |
| 10 | `publish` | Set draft: false | draft: falseに設定 |

### Workflow Diagram / ワークフロー図

```
content-drafts/en/*.md
        │
        ▼ [cleanup]
content-drafts/en/clean/*.md
        │
        ▼ [enrich_en]
        │
        ▼ [copy_to_content]
content/en/glossary/*.md
        │
        ▼ [translate]
content/ja/glossary/*.md
        │
        ▼ [enrich_ja]
        │
        ▼ [add_kana]
        │
        ▼ [fix_term]
        │
        ▼ [compare]
        │
        ▼ [refresh_links] ← Updates ALL articles
        │
        ▼ [publish]
    Published!
```

---

## Script Reference / スクリプトリファレンス

### pipeline_translate.py

Main orchestration script for the entire translation workflow.  
翻訳ワークフロー全体のメインオーケストレーションスクリプト。

**Usage / 使用方法:**

```bash
# Auto-detect and process new files / 新規ファイルを自動検出して処理
python scripts/pipeline_translate.py --auto

# Process specific file / 特定ファイルを処理
python scripts/pipeline_translate.py --file Copilot.md

# Dry run (no changes) / ドライラン（変更なし）
python scripts/pipeline_translate.py --auto --dry-run

# Start from specific step / 特定ステップから開始
python scripts/pipeline_translate.py --file Copilot.md --from-step translate

# Run only a specific step (debugging) / 特定ステップのみ実行（デバッグ用）
python scripts/pipeline_translate.py --file Copilot.md --only-step translate

# Cleanup temp files after processing / 処理後に一時ファイルを削除
python scripts/pipeline_translate.py --auto --cleanup

# Include publish step / 公開ステップを含む
python scripts/pipeline_translate.py --auto --publish
```

**Options / オプション:**

| Option | Description (EN) | 説明 (JA) |
|--------|------------------|-----------|
| `--auto` | Auto-detect new/updated files | 新規/更新ファイルを自動検出 |
| `--file` | Process specific file | 特定ファイルを処理 |
| `--dry-run` | Show changes without applying | 変更を適用せずに表示 |
| `--from-step` | Start from specific step | 特定ステップから開始 |
| `--only-step` | Run only this specific step | 特定ステップのみ実行（デバッグ用） |
| `--cleanup` | Delete temp files after processing | 処理後に一時ファイルを削除 |
| `--skip-existing` | Skip files with existing JA translations | 既存の日本語翻訳があるファイルをスキップ |
| `--publish` | Set draft: false after processing | 処理後にdraft: falseを設定 |

### backfill_e_titles.py

Ensures every Japanese glossary file retains its original English title for display and search.

日本語用語記事に英語タイトル(`e-title`)を自動付与し、検索と表示の整合性を保ちます。

```bash
python scripts/backfill_e_titles.py
```

| Option | Description (EN) | 説明 (JA) |
|--------|------------------|-----------|
| `--ja-dir` | Japanese glossary directory (default `content/ja/glossary`) | 日本語用語ディレクトリ |
| `--en-dir` | English glossary directory (default `content/en/glossary`) | 英語用語ディレクトリ |

### enrich_glossary.py

Adds keywords to frontmatter and internal links to content body.  
フロントマターにキーワードを追加し、本文に内部リンクを追加。

**Usage / 使用方法:**

```bash
# Enrich English articles / 英語記事をエンリッチ
python scripts/enrich_glossary.py content/en/glossary/

# Enrich Japanese articles / 日本語記事をエンリッチ
python scripts/enrich_glossary.py content/ja/glossary/ --dict config/keyword_dictionary_ja.json

# Dry run / ドライラン
python scripts/enrich_glossary.py content/ja/glossary/ --dict config/keyword_dictionary_ja.json --dry-run
```

**Features / 機能:**

- Automatically detects language from path / パスから言語を自動検出
- Only links to existing pages / 存在するページへのみリンク
- Skips text already inside markdown links / 既存リンク内のテキストをスキップ
- Preserves YAML frontmatter formatting / YAMLフロントマターの書式を保持

### translate_glossary_en_to_ja.py

Translates English articles to Japanese using Claude API.  
Claude APIを使用して英語記事を日本語に翻訳。

**Usage / 使用方法:**

```bash
python scripts/translate_glossary_en_to_ja.py content/en/glossary/Copilot.md
```

**Features / 機能:**

- Uses Claude claude-sonnet-4-5-20250929 model / Claude claude-sonnet-4-5-20250929モデルを使用
- Includes translation style guide / 翻訳スタイルガイドを含む
- Validates translation completeness / 翻訳完全性を検証
- Max tokens: 16000 / 最大トークン: 16000

### update_lastmod.py

Automatically updates the `lastmod` field in Markdown frontmatter based on the current date for files you have modified.  
変更したMarkdownファイルの frontmatter にある `lastmod` を自動的に今日の日付へ更新します。

```bash
# Update lastmod for all modified files under content/
python scripts/update_lastmod.py

# (Optional) Call from git pre-commit hook
echo "python scripts/update_lastmod.py" >> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**Tips / ヒント**

- Runs quickly before committing to keep `lastmod` fresh. / コミット前に実行して最終更新日を最新に保つ。
- Safe to run repeatedly; files already up to date are skipped. / 既に最新のファイルはスキップされるため繰り返し実行しても安全。

---

## Operation Guide / 操作ガイド

### Adding New Articles / 新規記事の追加

#### Step 1: Place English Draft / 英語ドラフトを配置

Place the English markdown file in `content-drafts/en/`:
英語のMarkdownファイルを `content-drafts/en/` に配置：

```bash
cp NewArticle.md content-drafts/en/
```

#### Step 2: Run Pipeline / パイプラインを実行

```bash
python scripts/pipeline_translate.py --auto

# After processing, refresh bilingual titles
python scripts/backfill_e_titles.py

# Refresh lastmod values for modified content
python scripts/update_lastmod.py
```

#### Step 3: Verify Results / 結果を確認

```bash
hugo server
# Check http://localhost:1313/en/glossary/
# Check http://localhost:1313/ja/glossary/
```

### Updating Keyword Dictionary / キーワード辞書の更新

#### Step 1: Edit Dictionary / 辞書を編集

Edit `config/keyword_dictionary_ja.json`:
`config/keyword_dictionary_ja.json` を編集：

```json
{
  "新しい用語": {
    "keywords": ["新しい用語", "関連キーワード"],
    "link": "/ja/glossary/new-term/",
    "aliases": ["新しい用語", "New Term"]
  }
}
```

#### Step 2: Refresh Links / リンクを更新

```bash
python scripts/enrich_glossary.py content/ja/glossary/ --dict config/keyword_dictionary_ja.json
```

### Manual Translation / 手動翻訳

For articles requiring manual review:
手動レビューが必要な記事の場合：

```bash
# Translate only / 翻訳のみ
python scripts/translate_glossary_en_to_ja.py content/en/glossary/Article.md

# Then enrich / その後エンリッチ
python scripts/enrich_glossary.py content/ja/glossary/Article.md --dict config/keyword_dictionary_ja.json
```

---

## Troubleshooting / トラブルシューティング

### Common Issues / よくある問題

#### Issue: `\u0026` displayed instead of `&`
#### 問題: `&` の代わりに `\u0026` が表示される

**Cause / 原因:**  
YAML frontmatter `&` not properly quoted.  
YAMLフロントマターの `&` が適切にクォートされていない。

**Solution / 解決策:**  
Wrap values containing `&` in quotes:  
`&` を含む値をクォートで囲む：

```yaml
title: "AIチャットボット&自動化"
```

#### Issue: Links to non-existent pages
#### 問題: 存在しないページへのリンク

**Cause / 原因:**  
Dictionary contains entries for pages not yet created.  
辞書にまだ作成されていないページのエントリが含まれている。

**Solution / 解決策:**  
The enrichment script automatically skips non-existent pages. Run `refresh_links` after adding new pages.  
エンリッチメントスクリプトは存在しないページを自動的にスキップします。新しいページを追加した後に `refresh_links` を実行してください。

#### Issue: Translation truncated
#### 問題: 翻訳が途中で切れる

**Cause / 原因:**  
Article too long for single API call.  
記事が1回のAPI呼び出しには長すぎる。

**Solution / 解決策:**  
The script uses max_tokens=16000. For very long articles, consider splitting or manual translation.  
スクリプトはmax_tokens=16000を使用しています。非常に長い記事の場合は、分割または手動翻訳を検討してください。

#### Issue: Hugo build error "value is not allowed in this context"
#### 問題: Hugoビルドエラー「value is not allowed in this context」

**Cause / 原因:**  
Malformed YAML frontmatter, often missing newline after `keywords` field.  
YAMLフロントマターの形式が不正、多くの場合 `keywords` フィールド後の改行が欠落。

**Solution / 解決策:**  
Check frontmatter formatting. Each field should be on its own line.  
フロントマターの書式を確認。各フィールドは独自の行にある必要があります。

---

## Changelog / 変更履歴

### Version 1.2.1 (2025-12-04)

#### Added / 追加
- Title sanitization integrated into `cleanup_flowhunt_output.py` for early-stage processing
- Parenthesized patterns: `(AI Chatbot & Automation)`, `(AIチャットボット&自動化)`

#### Changed / 変更
- Stop words expanded with: `technical`, `reference`, `overview`, `resource`, `chatbots`
- Japanese keywords expanded: `ようごしゅう`, `かいせつ`, `リソース`, `がいよう`, `ぎじゅつ`

### Version 1.2.0 (2025-12-04)

#### Added / 追加
- `title_sanitizer.py` to remove redundant suffixes from titles, translation keys, term, and reading fields
- `sanitize_titles` step added to pipeline (runs after cleanup, before enrich_en)

#### Changed / 変更
- Stop words expanded: `glossary`, `guide`, `comprehensive`, `complete`, `deep`, `dive`, `practical`

### Version 1.1.0 (2025-12-04)

#### Added / 追加
- Bilingual title support (`title` + `e-title`) for Japanese listings and detail pages
- Search index + Fuse.js keys updated to include English titles, translation keys, and kana terms
- `backfill_e_titles.py` to retroactively populate English titles in JA articles

#### Changed / 変更
- Glossary typography (titles, body, list section headers) aligned with blog styling for consistent UI

### Version 1.0.0 (2025-12-03)

#### Added / 追加
- Initial release of translation pipeline / 翻訳パイプラインの初期リリース
- `pipeline_translate.py` - Main orchestration script / メインオーケストレーションスクリプト
- `enrich_glossary.py` - Keyword and link enrichment with existing page validation / 既存ページ検証付きキーワード・リンクエンリッチメント
- `translate_glossary_en_to_ja.py` - Claude API translation / Claude API翻訳
- Japanese keyword dictionary (`keyword_dictionary_ja.json`) / 日本語キーワード辞書
- `refresh_links` step for updating all internal links / 全内部リンク更新用の `refresh_links` ステップ
- Automatic language detection from file path / ファイルパスからの自動言語検出
- Protection against linking to non-existent pages / 存在しないページへのリンク防止

#### Fixed / 修正
- YAML frontmatter `&` character escaping in Hugo templates / HugoテンプレートでのYAMLフロントマター `&` 文字エスケープ
- Nested markdown links issue / ネストされたMarkdownリンクの問題
- Missing newline after `keywords` field causing Hugo build errors / `keywords` フィールド後の改行欠落によるHugoビルドエラー

---

## Support / サポート

For issues or questions, check the logs in `logs/` directory or review this manual.  
問題や質問がある場合は、`logs/` ディレクトリのログを確認するか、このマニュアルを参照してください。

---

*This manual is maintained as part of the FlowHunt Glossary Translation Pipeline project.*  
*このマニュアルはFlowHunt用語集翻訳パイプラインプロジェクトの一部として管理されています。*
