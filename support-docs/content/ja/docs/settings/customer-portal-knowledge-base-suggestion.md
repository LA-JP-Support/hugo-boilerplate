---
title: "「カスタマーポータル（ナレッジベース/提案）」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "customer-portal-knowledge-base-suggestion"
description: "※ LiveAgent version 4.7.3.0 以降に対応します。"
keywords: ["カスタマーポータル", "ナレッジベース", "ナレッジ", "Suggestions", "LiveAgent"]
category: "settings"
---
## カスタマーポータル API リファレンス

### 目次
- [ナレッジベース検索](#ナレッジベース検索)
- [提案カテゴリー一覧](#提案カテゴリー一覧)

### ナレッジベース検索

#### API概要
- **対応バージョン**: LiveAgent version 4.7.3.0 以降

#### リクエスト方法
GET `http://example.com/api/knowledgebase/search?query=[value]&apikey=[value]`

#### 必須パラメータ
| パラメータ名 | 形式 | 内容 |
|--------------|------|------|
| query | text | 検索クエリの文字列 |
| apikey | text | API キー |

#### オプションパラメータ
| パラメータ名 | 形式 | 内容 |
|--------------|------|------|
| top_article_id | text | Top article ID。指定されたIDから検索を開始 |

#### レスポンスフィールド
- `articles`: ナレッジベース記事リスト
  - `kb_entry_id`: 記事ID
  - `urlcode`: 記事URL ID
  - `title`: タイトル
  - その他詳細フィールド参照

#### レスポンス例
- XML、JSONフォーマットのサンプルレスポンスあり

### 提案カテゴリー一覧

#### API概要
- **対応バージョン**: LiveAgent version 2.8.2.1 以降

#### リクエスト方法
GET `http://example.com/api/suggestioncategories?apikey=[value]`

#### 必須パラメータ
| パラメータ名 | 形式 | 内容 |
|--------------|------|------|
| apikey | text | API キー |

#### レスポンスフィールド
- `suggestioncategories`: 提案カテゴリーリスト
  - `id`: カテゴリーID
  - `title`: カテゴリータイトル
  - `path`: カテゴリーパス

#### レスポンス例
- XML、JSONフォーマットのサンプルレスポンスあり