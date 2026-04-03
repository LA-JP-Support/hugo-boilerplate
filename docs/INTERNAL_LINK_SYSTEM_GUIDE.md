# Internal Link System Guide - 内部リンクシステムガイド

**バージョン**: v2.2.0  
**作成日**: 2025-01-06  
**最終更新**: 2026-01-09  
**メンテナンス**: Takazumi

**⚠️ 重要な変更**: 
1. v2.2.0より、同一セクション内での重複リンクを防止するロジックを導入しました。
2. 英語版の自動キーワード抽出（`en_automatic.json`）が1,900語以上に拡張されました。
3. HTML後処理方式を標準とし、Janomeによる形態素解析（日本語）を統合しています。

---

## 📋 目次

1. [システム概要](#システム概要)
2. [ディレクトリ構成](#ディレクトリ構成)
3. [データベースファイル](#データベースファイル)
4. [スクリプト詳細](#スクリプト詳細)
5. [ワークフロー](#ワークフロー)
6. [コマンドリファレンス](#コマンドリファレンス)
7. [技術詳細](#技術詳細)
8. [トラブルシューティング](#トラブルシューティング)
9. [ベストプラクティス](#ベストプラクティス)
10. [更新履歴](#更新履歴)

---

## システム概要

### 目的

Hugo静的サイトのブログ記事やグロッサリーページに、関連する用語集（グロッサリー）への内部リンクを自動的に挿入するシステムです。

### 主な機能

- **重複リンク防止**: 同一セクション（段落等）内で同じ単語が複数出現しても、最初の1回のみリンクを付与 (v2.2.0)
- **HTML後処理方式**: Hugoビルド後のHTMLファイルに対してリンクを追加
- **日本語形態素解析**: `Janome` を使用し、複合語の一部（例：「交通信号」内の「通信」）への誤リンクを防止 (v2.1.1)
- **太字レンダリング修正**: Markdownの太字記法（`**`）が記号と隣接して崩れる問題を自動修正 (v2.1.1)
- **クリーンなMarkdown**: ソースファイル（`content/`）にリンクを含めず、可読性を維持
- **重複除外**: キーワード辞書から自動的に重複を除外
- **Denylist統合**: 除外語（danger_terms）を自動適用し、誤リンクを防止
- **glossary URL小文字統一**: `/glossary/` 配下のリンク（既存 `href` を含む）を後処理で小文字に正規化し、ケースセンシティブ環境での404を防止 (v2.1.3)
- **太字処理改善**: 太字タグ（`<strong>`）内のテキストもピンポイントでリンク化
- **多言語対応**: 英語（EN）と日本語（JA）の並列処理をサポート

### システム構成図

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  HTML後処理方式 - 内部リンクシステム                       │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────────┐
│ content/             │  Markdownソース（リンクなし）
│  ├── en/blog/        │
│  ├── en/glossary/    │
│  ├── ja/blog/        │
│  └── ja/glossary/    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  Markdown事前処理（オプション）                                             │
│  ───────────────────────────────                                         │
│  fix_bold_syntax_to_html.py                                              │
│  ・Markdown内の太字記法（**）を <strong> タグに変換                          │
│  ・レンダリングエラー（記号隣接時の崩れ）を防止                              │
└──────────┬───────────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  extract_automatic_links.py                                              │
│  ─────────────────────────                                               │
│  ・Markdownフロントマターからキーワード抽出                                 │
│  ・重複除外ロジック適用                                                    │
│  ・data/linkbuilding/*_automatic.json 生成                               │
└──────────┬───────────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────┐     ┌─────────────────────┐
│ data/linkbuilding/               │     │ databases/          │
│  ├── en_automatic.json           │     │  ├── danger_terms_  │
│  ├── ja_automatic.json           │     │  │   en.csv         │
│  ├── en.yaml                     │     │  └── danger_terms_  │
│  └── ja.yaml                     │     │      ja.csv         │
└──────────┬───────────────────────┘     └──────────┬──────────┘
           │                                        │
           │  ┌─────────────────────────────────────┘
           │  │
           ▼  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  hugo --destination public --cleanDestinationDir                         │
│  ────────────────────────────────────────────────                        │
│  ・MarkdownからHTMLを生成                                                │
│  ・public/ ディレクトリに出力                                              │
└──────────┬───────────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  linkbuilding_parallel.py                                                │
│  ───────────────────────                                                 │
│  ・EN/JAを並列処理                                                         │
│  ・Janomeによる形態素解析（日本語）                                          │
│  ・denylist自動適用                                                        │
│  ・太字処理改善（Granular Link Injection）                                 │
│  ・BeautifulSoupで安全にHTML編集                                           │
└──────────┬───────────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────┐
│  public/             │  内部リンク付きHTML（公開用）
│  ├── en/             │  ・data-lb="1" マーカー付き
│  │   ├── blog/       │
│  │   └── glossary/   │
│  └── ja/             │
│      ├── blog/       │
│      └── glossary/   │
└──────────────────────┘
```

---

## ディレクトリ構成

```
smartweb/
├── databases/                          # Denylist（除外語）
│   ├── danger_terms_en.csv            # 英語禁止用語
│   └── danger_terms_ja.csv            # 日本語禁止用語
│
├── scripts/                            # 処理スクリプト
│   ├── linkbuilding.py                # ★ HTML後処理（メイン・Janome統合）
│   ├── linkbuilding_parallel.py       # ★ 並列実行ラッパー（推奨）
│   ├── fix_bold_syntax_to_html.py     # ★ 太字記法修正（Markdown用）
│   ├── detect_bold_render_errors.py   # ★ 太字エラー検出
│   ├── extract_automatic_links.py     # 自動キーワード抽出
│   ├── generate_linkbuilding_yaml_from_glossary.py  # YAML生成
│   ├── convert_link_database_csv_to_json.py  # CSV→JSON変換
│   ├── analyze_keyword_sources.py     # キーワード分析
│   ├── generate_danger_terms.py       # Denylist生成
│   └── archived_markdown_based/       # 非推奨スクリプト
│
├── data/linkbuilding/                 # リンク設定ファイル
│   ├── en_automatic.json              # EN自動キーワード
│   ├── ja_automatic.json              # JA自動キーワード
│   ├── en.yaml                        # EN手動キーワード
│   └── ja.yaml                        # JA手動キーワード
│
├── content/
│   ├── en/
│   └── ja/
│
└── docs/
    └── INTERNAL_LINK_SYSTEM_GUIDE.md  # このファイル
```


---

## データベースファイル

### link_database_*.csv - リンクキーワードデータベース

グロッサリー記事から抽出されたキーワードとそのバリエーションを格納します。

#### カラム定義

| カラム | 型 | 説明 | 例 |
|--------|-----|------|-----|
| `keyword` | string | マッチング対象のキーワード | `RAG (Retrieval-Augmented Generation)` |
| `normalized` | string | 正規化されたキーワード（小文字） | `rag (retrieval-augmented generation)` |
| `title` | string | グロッサリーの元タイトル | `RAG (Retrieval-Augmented Generation)` |
| `url` | string | リンク先URL | `/en/glossary/RAG/` |
| `description` | string | 説明文（最大200文字） | `An AI technology that retrieves...` |
| `priority` | int | 優先度スコア（参考値）※現在未使用 | `1072` |
| `variation_type` | string | バリエーション種別 | `exact`, `acronym`, `without_parens` |
| `exact_match` | bool | 完全一致フラグ（参考値）※現在未使用 | `true` / `false` |

#### バリエーション種別（variation_type）

| 種別 | 説明 | 例 |
|------|------|-----|
| `exact` | 元タイトルそのまま | `Natural Language Processing (NLP)` |
| `acronym` | 括弧内の略語 | `NLP` |
| `without_parens` | 括弧を除いた部分 | `Natural Language Processing` |
| `parens_content` | 括弧内の内容（非略語） | `カリフォルニア州消費者プライバシー法` |
| `slash_part` | スラッシュ区切りの各部分 | `AI`, `ML` (from `AI/ML`) |
| `without_hyphens` | ハイフンをスペースに | `Zero Shot Learning` |
| `singular` | 単数形 | `chatbot` (from `chatbots`) |
| `without_toha` | 「とは」を除去（日本語） | `チャットボット` |
| `fullwidth_parens_content` | 全角括弧内の内容 | `コンテンツ要約` |

#### 優先度スコアの計算（参考情報）

> ⚠️ **注意**: `priority` と `exact_match` カラムは `build_link_database.py` で生成されますが、
> 現在の `add_links_from_database.py` では**使用されていません**。
> 実際のマッチングは**キーワードの文字数（長い順）**で優先度が決まります。

```python
# build_link_database.py での基本スコア計算（参考）
base_scores = {
    'exact': 1000,
    'acronym': 950,
    'without_parens': 900,
    'without_fullwidth_parens': 880,
    'without_ai_ml': 850,
    'parens_content': 800,
    'fullwidth_parens_content': 780,
    'parens_part': 750,
    'slash_part': 700,
    'without_hyphens': 600,
    'without_toha': 500,
    'singular': 400
}

# 調整スコア = 基本スコア + (キーワード文字数 × 2)
adjusted_priority = base_score + (len(keyword) * 2)

# ただし add_links_from_database.py では以下のソートを使用：
self.link_database.sort(key=lambda x: len(x['keyword']), reverse=True)
```

---

### danger_terms_*.csv - 禁止用語リスト

誤ってリンクされやすい一般的な単語をフィルタリングします。

#### カラム定義

| カラム | 型 | 説明 | 例 |
|--------|-----|------|-----|
| `keyword` | string | 禁止キーワード | `Make` |
| `normalized` | string | 正規化されたキーワード | `make` |
| `reason` | string | 禁止理由 | `Common English verb; clashes with Make (Integromat)` |
| `score` | int | 危険度スコア（高いほど危険） | `100` |
| `source` | string | 追加元 | `seed`, `auto`, `manual` |

#### 英語の禁止用語例

| キーワード | 理由 | スコア |
|-----------|------|--------|
| `Make` | 動詞「作る」とMake (Integromat)が衝突 | 100 |
| `did` | DID略語と一般動詞が衝突 | 100 |
| `Token` | AI/tech文脈で頻出しすぎる | 60 |
| `Platform` | 汎用名詞として多用 | 60 |
| `Workflow` | 一般的なビジネス用語 | 60 |

#### 日本語の禁止用語例

| キーワード | 理由 | スコア |
|-----------|------|--------|
| `トークン` | 一般的なAI用語 | 60 |
| `プロンプト` | 頻出しすぎる | 60 |
| `精度` | 汎用的な単語 | 60 |
| `メタ` | 短すぎる、汎用的 | 60 |

---

## スクリプト詳細

### 1. build_link_database.py - データベース生成

グロッサリーディレクトリからキーワードデータベースを生成します。

#### 機能

- グロッサリーファイルからタイトル・URL・説明文を抽出
- キーワードバリエーションを自動生成
- 優先度スコアを計算
- CSVファイルとして出力

#### 使用方法

```bash
python3 scripts/build_link_database.py \
  --glossary-dir content/en/glossary \
  --output databases/link_database_en.csv \
  --lang en
```

#### オプション

| オプション | 必須 | 説明 |
|-----------|------|------|
| `--glossary-dir` | ✅ | グロッサリーディレクトリのパス |
| `--output` | ✅ | 出力CSVファイルのパス |
| `--lang` | ❌ | 言語コード（デフォルト: `ja`） |

#### 出力例

```
============================================================
Building link database from: content/en/glossary
Output: databases/link_database_en.csv
Language: en
============================================================

============================================================
✅ Link database created successfully!
   Glossary entries: 1221
   Total keyword variations: 3071
   Output file: databases/link_database_en.csv
============================================================

Top 20 keywords by priority:
   1. ITIL – Information Technology Infrastructure Library (priority: 1104, type: exact)
   2. Entity Extraction (Named Entity Recognition, NER)    (priority: 1098, type: exact)
   ...
```

---

### 2. add_links_from_database.py - リンク挿入（推奨）

CSVデータベースを使用してMarkdownファイルにリンクを挿入します。

#### 機能

- CSVデータベースからキーワードを読み込み
- 禁止用語リストでフィルタリング
- 安全なコンテンツ保護（コードブロック、既存リンク等）
- 日本語・英語両対応
- 同一キーワードのリンク数制限

#### 使用方法

```bash
# プレビュー（dry-run）
python3 scripts/add_links_from_database.py \
  content/en/blog/ \
  --database databases/link_database_en.csv \
  --dry-run

# 本番実行
python3 scripts/add_links_from_database.py \
  content/en/blog/ \
  --database databases/link_database_en.csv
```

#### オプション

| オプション | 必須 | 説明 |
|-----------|------|------|
| `content_dir` | ✅ | 処理対象ディレクトリ |
| `--database` | ✅ | リンクデータベースCSVのパス |
| `--denylist` | ❌ | 禁止用語CSVのパス（自動検出） |
| `--dry-run` | ❌ | プレビューモード（ファイル変更なし） |
| `--debug` | ❌ | デバッグログを有効化 |

#### コンテンツ保護

以下の領域はリンク挿入から保護されます：

1. **コードブロック**: ` ```...``` `
2. **インラインコード**: `` `...` ``
3. **既存リンク**: `[text](url)`
4. **HTMLタグ**: `<tag>...</tag>`
5. **ショートコード**: `{{< ... >}}`
6. **見出し**: `# Heading`

#### リンク制限

| 制限項目 | デフォルト値 |
|---------|-------------|
| 同一キーワードの最大リンク数 | 3 |
| ページ全体の最大リンク数 | 100 |

---

### 3. add_internal_links.py - リンク挿入（シンプル版）

グロッサリーを直接読み込んでリンクを挿入するシンプルなスクリプトです。

#### 使用方法

```bash
python3 scripts/add_internal_links.py \
  content/en/blog/ \
  --glossary-dir content/en/glossary \
  --lang en \
  --dry-run
```

#### 特徴

- CSVデータベース不要
- グロッサリーを直接読み込み
- シンプルな処理フロー
- 禁止用語フィルタリングなし

---

### 4. generate_danger_terms.py - 禁止用語生成

リンクデータベースから危険な用語を自動検出し、禁止用語リストを生成します。

#### 機能

- 短いASCII単語の検出
- 一般的な英単語の検出
- 短いカタカナ語の検出（日本語）
- 既存リストとのマージ

#### 使用方法

```bash
# 英語禁止用語を生成
python3 scripts/generate_danger_terms.py --lang en --min-score 60

# 日本語禁止用語を生成
python3 scripts/generate_danger_terms.py --lang ja --min-score 60
```

#### オプション

| オプション | 必須 | 説明 |
|-----------|------|------|
| `--lang` | ✅ | 言語コード（`en` または `ja`） |
| `--database` | ❌ | リンクデータベースのパス |
| `--output` | ❌ | 出力CSVのパス |
| `--report` | ❌ | レポートMarkdownのパス |
| `--min-score` | ❌ | 最小危険度スコア（デフォルト: 60） |

#### 自動検出ルール

**英語:**
- 一般的な動詞: `make`, `do`, `get`, `set`, `use` (+50)
- 短いASCII単語（4文字以下）: (+30)
- ASCII単語全般: (+10)
- `without_parens`バリエーション: (+15)

**日本語:**
- 一般的な用語: `トークン`, `プロンプト`, `精度` (+60)
- 非常に短い語（2文字以下）: (+25)
- 短いカタカナ語（6文字以下）: (+10)

---

## スクリプト詳細（旧方式）

### 1. build_link_database.py - データベース生成

グロッサリーディレクトリからキーワードデータベースを生成します。

**⚠️ 注意**: 現行の内部リンクはHTML後処理方式が標準です。このセクションは旧方式（CSV DB中心）の説明として残しています。

**推奨**: `extract_automatic_links.py`（`data/linkbuilding/*_automatic.json` 生成）と `linkbuilding_parallel.py`（`public/` HTML後処理）を使用してください。

#### 機能

- グロッサリーファイルからタイトル・URL・説明文を抽出
- キーワードバリエーションを自動生成
- 優先度スコアを計算
- CSVファイルとして出力

#### 使用方法

```bash
python3 scripts/build_link_database.py \
  --glossary-dir content/en/glossary \
  --output databases/link_database_en.csv \
  --lang en
```

#### オプション

| オプション | 必須 | 説明 |
|-----------|------|------|
| `--glossary-dir` | ✅ | グロッサリーディレクトリのパス |
| `--output` | ✅ | 出力CSVファイルのパス |
| `--lang` | ❌ | 言語コード（デフォルト: `ja`） |

#### 出力例

```
============================================================
Building link database from: content/en/glossary
Output: databases/link_database_en.csv
Language: en
============================================================

============================================================
✅ Link database created successfully!
   Glossary entries: 1221
   Total keyword variations: 3071
   Output file: databases/link_database_en.csv
============================================================

Top 20 keywords by priority:
   1. ITIL – Information Technology Infrastructure Library (priority: 1104, type: exact)
   2. Entity Extraction (Named Entity Recognition, NER)    (priority: 1098, type: exact)
   ...
```

---

### 2. add_links_from_database.py - リンク挿入（非推奨）

CSVデータベースを使用してMarkdownファイルにリンクを挿入します。

**⚠️ 注意**: Markdownへ直接リンクを挿入する方式は現在は非推奨です（HTML後処理方式が標準）。

#### 機能

- CSVデータベースからキーワードを読み込み
- 禁止用語リストでフィルタリング
- 安全なコンテンツ保護（コードブロック、既存リンク等）
- 日本語・英語両対応
- 同一キーワードのリンク数制限

#### 使用方法

```bash
# プレビュー（dry-run）
python3 scripts/add_links_from_database.py \
  content/en/blog/ \
  --database databases/link_database_en.csv \
  --dry-run

# 本番実行
python3 scripts/add_links_from_database.py \
  content/en/blog/ \
  --database databases/link_database_en.csv
```

#### オプション

| オプション | 必須 | 説明 |
|-----------|------|------|
| `content_dir` | ✅ | 処理対象ディレクトリ |
| `--database` | ✅ | リンクデータベースCSVのパス |
| `--denylist` | ❌ | 禁止用語CSVのパス（自動検出） |
| `--dry-run` | ❌ | プレビューモード（ファイル変更なし） |
| `--debug` | ❌ | デバッグログを有効化 |

#### コンテンツ保護

以下の領域はリンク挿入から保護されます：

1. **コードブロック**: ` ```...``` `
2. **インラインコード**: `` `...` ``
3. **既存リンク**: `[text](url)`
4. **HTMLタグ**: `<tag>...</tag>`
5. **ショートコード**: `{{< ... >}}`
6. **見出し**: `# Heading`

#### リンク制限

| 制限項目 | デフォルト値 |
|---------|-------------|
| 同一キーワードの最大リンク数 | 3 |
| ページ全体の最大リンク数 | 100 |

---

### 3. add_internal_links.py - リンク挿入（シンプル版）

グロッサリーを直接読み込んでリンクを挿入するシンプルなスクリプトです。

**⚠️ 注意**: Markdownへ直接リンクを挿入する方式は現在は非推奨です（HTML後処理方式が標準）。

#### 使用方法

```bash
python3 scripts/add_internal_links.py \
  content/en/blog/ \
  --glossary-dir content/en/glossary \
  --lang en \
  --dry-run
```

#### 特徴

- CSVデータベース不要
- グロッサリーを直接読み込み
- シンプルな処理フロー
- 禁止用語フィルタリングなし

---

## ワークフロー

### 基本ワークフロー

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 1: グロッサリー更新後、データベースを再生成                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 2: 禁止用語リストを更新（必要に応じて）                              │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 3: dry-runでプレビュー確認                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 4: 本番実行                                                        │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Step 5: Gitコミット                                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

### 詳細手順

#### Step 1: データベース再生成

```bash
# 自動キーワード辞書を再生成（必要に応じて）
# EN
python3 scripts/extract_automatic_links.py \
  --content-dir content/en/ \
  --output data/linkbuilding/en_automatic.json

# JA
python3 scripts/extract_automatic_links.py \
  --content-dir content/ja/ \
  --output data/linkbuilding/ja_automatic.json
```

#### Step 2: 禁止用語更新（オプション）

```bash
# 新しい危険用語を自動検出
python3 scripts/generate_danger_terms.py --lang en
python3 scripts/generate_danger_terms.py --lang ja

# 手動で追加する場合はCSVを直接編集
# databases/danger_terms_en.csv
# databases/danger_terms_ja.csv
```

#### Step 3: プレビュー確認

```bash
# HugoでHTMLを生成（テスト用ディレクトリに出力）
hugo --destination public-test --cleanDestinationDir

# HTML後処理で内部リンク追加（プレビュー用）
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public-test \
  --denylist-dir databases
```

#### Step 4: 本番実行

```bash
# HugoでHTMLを生成（公開用）
hugo --destination public --cleanDestinationDir

# HTML後処理で内部リンク追加（公開用）
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

#### Step 5: Gitコミット

```bash
# public/ は成果物のためコミットしない（.gitignore）
# 辞書やdenylistを更新した場合のみそれらをコミット
git add data/linkbuilding/ databases/
git commit -m "Update internal linking data"
git push
```

---

## コマンドリファレンス

### クイックリファレンス

```bash
# ========================================
# 自動キーワード辞書の更新（必要に応じて）
# ========================================

# EN
python3 scripts/extract_automatic_links.py \
  --content-dir content/en/ \
  --output data/linkbuilding/en_automatic.json

# JA
python3 scripts/extract_automatic_links.py \
  --content-dir content/ja/ \
  --output data/linkbuilding/ja_automatic.json

# ========================================
# Hugoビルド + HTML後処理（推奨）
# ========================================

# 1) Hugoビルド
hugo --destination public --cleanDestinationDir

# 2) 内部リンク追加（HTML後処理）
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases

# ========================================
# 禁止用語生成
# ========================================

python3 scripts/generate_danger_terms.py --lang en
python3 scripts/generate_danger_terms.py --lang ja

# ========================================
# 単一言語のみ処理（必要に応じて）
# ========================================

python3 scripts/linkbuilding.py \
  -k data/linkbuilding/ja.yaml \
  -a data/linkbuilding/ja_automatic.json \
  -d public/ja \
  --language JA \
  --denylist databases/danger_terms_ja.csv \
  --max-links 15 --max-keyword 1 --max-url 3
```

---

## 技術詳細

### キーワードマッチングのロジック

#### 英語キーワード

```python
# ASCII境界チェック（前後が英数字でないことを確認）
pattern = r'(?<![a-zA-Z0-9_])(' + escaped_keyword + r')(?![a-zA-Z0-9_])'
```

- `AI` は `AIカスタマー` にマッチ（日本語境界）
- `AI` は `MAIL` にマッチしない（英語境界）

#### 日本語キーワード

```python
# CJKキーワードはそのままマッチ
pattern = f'({escaped_keyword})'
```

### コンテンツ保護の実装

```python
def mask_content(self, text: str) -> Tuple[str, Dict[str, str]]:
    placeholders = {}
    
    def create_placeholder(content):
        key = f"__MASKED_{uuid.uuid4().hex}__"
        placeholders[key] = content
        return key

    # 1. コードブロック
    text = re.sub(r'```[\s\S]*?```', lambda m: create_placeholder(m.group(0)), text)
    
    # 2. インラインコード
    text = re.sub(r'`[^`\n]+`', lambda m: create_placeholder(m.group(0)), text)
    
    # 3. ショートコード
    text = re.sub(r'{{<[\s\S]*?>}}', lambda m: create_placeholder(m.group(0)), text)
    
    # 4. HTMLタグ
    text = re.sub(r'<[^>]+>', lambda m: create_placeholder(m.group(0)), text)

    # 5. 見出し
    text = re.sub(r'^#+ .*$', lambda m: create_placeholder(m.group(0)), text, flags=re.MULTILINE)

    # 6. 既存リンク（パーサーで処理）
    # ...
    
    return text, placeholders
```

### 優先度ソート

キーワードは**文字数の長い順**に処理されます（`priority` カラムは使用されません）：

```python
# 長いキーワードを先にマッチさせることで、
# "Natural Language Processing" が "Natural" より先にリンクされる
# ※ priority カラムではなく、文字数でソート
self.link_database.sort(key=lambda x: len(x['keyword']), reverse=True)
```

> 💡 **設計意図**: 長いフレーズを先にマッチさせることで、
> 「Natural Language Processing」全体がリンクされた後に
> 「Natural」が別途リンクされることを防ぎます。

---

## トラブルシューティング

### Q1: リンクが追加されない

**原因と対策:**

1. **キーワードが辞書にない**
   ```bash
   # 手動辞書を確認（YAML）
   grep -n "keyword:" data/linkbuilding/en.yaml
   
   # 自動辞書を確認（JSON）
   grep -i "keyword" data/linkbuilding/en_automatic.json
   ```

2. **禁止用語リストに含まれている**
   ```bash
   # 禁止用語を確認
   grep -i "keyword" databases/danger_terms_en.csv
   ```

3. **保護領域内にある**
   - コードブロック、既存リンク、ショートコード内はスキップされます

4. **同一キーワードの制限に達した**
   - デフォルトで同一キーワードは3回までリンク

### Q2: 誤ったリンクが追加される

**対策:**

1. 禁止用語リストに追加
   ```csv
   # databases/danger_terms_en.csv に追加
   keyword,normalized,reason,score,source
   NewKeyword,newkeyword,Too generic,80,manual
   ```

2. `generate_danger_terms.py` を再実行
   ```bash
   python3 scripts/generate_danger_terms.py --lang en --min-score 50
   ```

### Q3: 日本語キーワードがマッチしない

**原因と対策:**

1. **全角・半角の不一致**
   - `data/linkbuilding/ja.yaml` と `data/linkbuilding/ja_automatic.json` の表記を確認してください。

2. **辞書側にキーワードがない**
   - `data/linkbuilding/ja.yaml`（手動） / `data/linkbuilding/ja_automatic.json`（自動）を確認し、必要なら `extract_automatic_links.py` を再実行してください。

### Q4: 処理が遅い

**対策:**

1. 辞書サイズを確認
   ```bash
   wc -l data/linkbuilding/*_automatic.json
   ```

2. 禁止用語でフィルタリングを強化

3. `--debug` オプションでボトルネックを特定

---

## ベストプラクティス

### 1. 定期的なデータベース更新

グロッサリー追加後は必要に応じて自動辞書を再生成：

```bash
# 週次または新規グロッサリー追加時
python3 scripts/extract_automatic_links.py --content-dir content/en/ --output data/linkbuilding/en_automatic.json
python3 scripts/extract_automatic_links.py --content-dir content/ja/ --output data/linkbuilding/ja_automatic.json
```

### 2. 必ずdry-runで確認

本番実行前に必ずプレビュー：

```bash
hugo --destination public-test --cleanDestinationDir
python3 scripts/linkbuilding_parallel.py --linkbuilding-dir data/linkbuilding --public-dir public-test --denylist-dir databases --dry-run
```

### 3. バックアップの作成

大量処理前はバックアップ：

```bash
cp -r content/en/blog content/en/blog-backup-$(date +%Y%m%d)
```

### 4. Gitでの差分確認

実行後は差分を確認：

```bash
git diff content/en/blog/
```

### 5. 禁止用語の定期レビュー

月次で禁止用語リストをレビュー：

```bash
python3 scripts/generate_danger_terms.py --lang en --min-score 50
python3 scripts/generate_danger_terms.py --lang ja --min-score 50
```

---

## 更新履歴

### v5.1 (2025-01-06)

- ✅ `priority` カラムが現在未使用であることを明記
- ✅ `exact_match` カラムが現在未使用であることを明記
- ✅ 実際のソートロジック（文字数順）を正確に記載

### v5.0 (2025-01-06)

- ✅ 包括的なドキュメントとして再構成
- ✅ 全スクリプトの詳細説明を追加
- ✅ データベースファイル構造の詳細を追加
- ✅ ワークフロー図を追加
- ✅ コマンドリファレンスを整備
- ✅ 技術詳細セクションを追加
- ✅ トラブルシューティングを拡充
- ✅ 旧ツールチップ変換機能の記述を削除（移行完了のため）

### v4.0 (2025-12-20)

- ツールチップ→リンク変換スクリプト（現在は廃止）
- prompts → prompting 特別変換
- 部分一致機能

### v3.0 (2025-12-20)

- ダッシュ区切り形式対応
- カンマ区切り対応

### v2.0 (2025-12-20)

- 括弧と略語の柔軟な対応
- 複数形の自動生成

### v1.0 (2025-12-20)

- 基本的なリンク変換機能

---

## 関連ドキュメント

- [00_START_HERE.md](00_START_HERE.md) - 最初にお読みください（入口）
- [SCRIPTS_USAGE_GUIDE.md](SCRIPTS_USAGE_GUIDE.md) - スクリプト使用ガイド（運用の入口）
- [CSV_DATABASE_SYSTEM_GUIDE.md](CSV_DATABASE_SYSTEM_GUIDE.md) - CSV Database System（CSV→JSON変換含む）
- [INTERNAL_LINKING_QUICK_START.md](INTERNAL_LINKING_QUICK_START.md) - クイックスタート
- [GLOSSARY_OPTIMIZATION_GUIDE.md](GLOSSARY_OPTIMIZATION_GUIDE.md) - 用語集最適化（検索/表記揺れ含む）
- [danger_terms.md](danger_terms.md) - 禁止用語レポート（自動生成）

---

**最終更新**: 2026-01-08  
**メンテナンス**: Takazumi
