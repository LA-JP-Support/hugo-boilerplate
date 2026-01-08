# CSV Database System Guide

**バージョン**: 2.1.0  
**最終更新**: 2026-01-08  
**ステータス**: ✅ Active

## 概要

このドキュメントは、Hugo BoilerplateプロジェクトにおけるCSVデータベースシステムの役割、構造、使用方法、および最新の移行状況を説明します。

## CSVデータベースの役割

### 1. 用語集リンクデータベース

**ファイル**:
- `databases/link_database_en.csv` (1,222エントリ)
- `databases/link_database_ja.csv` (1,223エントリ)

**目的**: 全用語集ページのメタデータを一元管理し、内部リンクシステムや他のツールで利用可能にする。

**フォーマット**:
```csv
keyword,normalized,title,url,description,priority,variation_type,exact_match
A/B Testing,a/b testing,A/B Testing,/en/glossary/A-B-Testing/,"A method of comparing...",100,exact,true
```

**カラム説明**:
- `keyword`: 用語のタイトル（完全一致）
- `normalized`: 小文字に正規化されたキーワード（検索用）
- `title`: 表示用タイトル（通常はkeywordと同じ）
- `url`: 用語集ページのURL
- `description`: 簡潔な説明文（マウスオーバー表示用）
- `priority`: 優先度スコア（現在は100で統一）
- `variation_type`: バリエーションタイプ（`exact`）
- `exact_match`: 完全一致フラグ（`true`）

### 2. 翻訳用語対応表

**ファイル**:
- `databases/translation_glossary.csv`
- `config/translation_glossary.csv`（同期コピー）

**目的**: 英語と日本語の用語対応、翻訳方針の管理。

**フォーマット**:
```csv
english,japanese,type,category,notes,usage_context
AI,AI,keep_english,ai_ml,Universal acronym,Always use English
```

### 3. 内部リンク禁止用語リスト

**ファイル**:
- `databases/danger_terms_en.csv`
- `databases/danger_terms_ja.csv`

**目的**: 一般的すぎる単語や誤爆しやすい用語を内部リンク化から除外。

**例**: customer, platform, workflow, scenario（日本語版）

## システムアーキテクチャ

### v2.0.0以降の構成

```
┌─────────────────────────────────────────────────────────────┐
│                    Glossary Markdown Files                   │
│              content/{en,ja}/glossary/*.md                   │
│         (title, description, keywords in frontmatter)        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ 1. Extract metadata
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              CSV Database Generation                         │
│    databases/link_database_{en,ja}.csv                      │
│    (keyword, url, description, priority)                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ 2. Convert to JSON (optional)
                     ▼
┌─────────────────────────────────────────────────────────────┐
│           JSON Linkbuilding Database                         │
│    data/linkbuilding/{en,ja}_automatic.json                 │
│    (Keyword, URL, Title, Exact, Priority)                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ 3. HTML Post-processing
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Internal Link Insertion                         │
│         public/{en,ja}/**/*.html                            │
│         (data-lb="1" marker on links)                        │
└─────────────────────────────────────────────────────────────┘
```

## CSV生成ワークフロー

### 自動生成（推奨）

```bash
# 英語用語集CSVを生成
python3 -c "
import frontmatter
from pathlib import Path
import csv

glossary_dir = Path('content/en/glossary')
output_file = 'databases/link_database_en.csv'
entries = []

for md_file in sorted(glossary_dir.glob('*.md')):
    with open(md_file, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    
    entries.append({
        'keyword': post.get('title', ''),
        'normalized': post.get('title', '').lower(),
        'title': post.get('title', ''),
        'url': f'/en/glossary/{md_file.stem}/',
        'description': post.get('description', ''),
        'priority': 100,
        'variation_type': 'exact',
        'exact_match': 'true'
    })

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['keyword', 'normalized', 'title', 'url', 'description', 'priority', 'variation_type', 'exact_match'])
    writer.writeheader()
    writer.writerows(entries)

print(f'Generated {len(entries)} entries')
"

# 日本語用語集CSVを生成（同様の処理）
```

### 旧スクリプト（非推奨）

```bash
# build_link_database.py（キーワードバリエーション生成機能付き）
python3 scripts/build_link_database.py \
  --glossary-dir content/en/glossary \
  --output databases/link_database_en.csv \
  --lang en
```

**注意**: `build_link_database.py`はキーワードバリエーション（頭字語、略語など）を生成しますが、現在のHTML後処理システム（v2.0.0）では**使用されていません**。

## CSV → JSON変換

CSVデータベースをJSON形式に変換して、`linkbuilding.py`で使用できます。

```bash
# 英語
python3 scripts/convert_link_database_csv_to_json.py \
  --input databases/link_database_en.csv \
  --output data/linkbuilding/en_automatic.json

# 日本語
python3 scripts/convert_link_database_csv_to_json.py \
  --input databases/link_database_ja.csv \
  --output data/linkbuilding/ja_automatic.json

# または言語指定で自動パス検出
python3 scripts/convert_link_database_csv_to_json.py --language en
python3 scripts/convert_link_database_csv_to_json.py --language ja
```

## Description最適化

### Claude API使用

用語集のdescriptionフィールドを簡潔でわかりやすい説明に最適化します。

```bash
# 英語用語集を最適化
python3 scripts/optimize_glossary_descriptions.py --lang en --workers 5

# 日本語用語集を最適化
python3 scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# ドライラン（プレビューのみ）
python3 scripts/optimize_glossary_descriptions.py --lang en --dry-run --limit 10
```

**要件**:
- Claude API Key（`.env`ファイルに`ANTHROPIC_API_KEY`を設定）
- モデル: `claude-haiku-4-5-20251001`
- 出力: 1-2文、最大100文字以内、一般の人にもわかりやすい説明

**改善例**:
- **改善前**: "Comprehensive guide to A/B Testing..."
- **改善後**: "A method of comparing two versions of something (like a website or email) by showing each to different groups of people to see which one works better."

## 使用状況

### 現在のシステム（v2.0.0～）

**主要な使用箇所**:
1. **内部リンクシステム**: `data/linkbuilding/*.json`（CSV→JSON変換後）
2. **統計・分析**: `scripts/analyze_keyword_sources.py`
3. **ドキュメント生成**: 用語集リスト、統計レポート

**非推奨の使用箇所**:
- `scripts/archived_markdown_based/add_links_from_database.py`（Markdown直接編集方式、v2.0.0で非推奨）

### CSV vs JSON

| 形式 | 用途 | メリット | デメリット |
|------|------|---------|----------|
| CSV | データ管理、エクスポート、統計 | 人間が読みやすい、Excelで編集可能 | 階層構造に不向き |
| JSON | プログラム処理、API連携 | 階層構造に対応、パース高速 | 人間が読みにくい |

**推奨**: CSVをマスターデータとして管理し、必要に応じてJSONに変換。

## メンテナンス

### 定期更新タイミング

1. **新規用語集追加時**: 即座にCSV再生成
2. **Description最適化後**: CSV再生成
3. **週次**: 定期的な整合性チェック

### 更新手順

```bash
# 1. Description最適化（オプション）
python3 scripts/optimize_glossary_descriptions.py --lang en --workers 5
python3 scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# 2. CSV再生成
python3 -c "..." # 上記の自動生成スクリプト

# 3. JSON変換（内部リンクシステム用）
python3 scripts/convert_link_database_csv_to_json.py --language en
python3 scripts/convert_link_database_csv_to_json.py --language ja

# 4. Hugoビルド
hugo --cleanDestinationDir

# 5. 内部リンク再生成
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

## トラブルシューティング

### Q1: CSVとJSONの内容が一致しない

**原因**: CSV更新後にJSON変換を忘れた。

**解決**:
```bash
python3 scripts/convert_link_database_csv_to_json.py --language en
python3 scripts/convert_link_database_csv_to_json.py --language ja
```

### Q2: Descriptionが古い

**原因**: Description最適化後にCSV再生成を忘れた。

**解決**:
```bash
# 最適化実行
python3 scripts/optimize_glossary_descriptions.py --lang en --workers 5

# CSV再生成
python3 -c "..." # 自動生成スクリプト
```

### Q3: 用語集ページが見つからない

**原因**: ファイル名とURL slugが一致していない、またはYAMLパースエラー。

**確認**:
```bash
# YAMLエラーチェック
python3 -c "
import frontmatter
from pathlib import Path

for md_file in Path('content/en/glossary').glob('*.md'):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            frontmatter.load(f)
    except Exception as e:
        print(f'Error: {md_file.name}: {e}')
"
```

## バージョン履歴

### v2.1.0 (2026-01-08)
- ✅ Description最適化機能追加（Claude API使用）
- ✅ CSV自動生成スクリプト改善
- ✅ 英語1,222件、日本語1,223件のCSV生成完了
- ✅ ドキュメント整備

### v2.0.0 (2026-01-07)
- ✅ HTML後処理方式への移行
- ✅ CSV→JSON変換スクリプト追加
- ⚠️ Markdown直接編集方式を非推奨化

### v1.0.0 (2025-12-20)
- ✅ 初期CSV Database System構築
- ✅ `build_link_database.py`作成

## 関連ドキュメント

- [Internal Link System Guide](INTERNAL_LINK_SYSTEM_GUIDE.md) - 内部リンクシステム全体
- [Quick Start Guide](INTERNAL_LINKING_QUICK_START.md) - クイックスタート
- [Changelog](../CHANGELOG_INTERNAL_LINKING.md) - 変更履歴

## まとめ

CSVデータベースシステムは、用語集メタデータの一元管理と、内部リンクシステムへのデータ供給を担う重要なコンポーネントです。

**ベストプラクティス**:
1. ✅ CSVをマスターデータとして管理
2. ✅ Description最適化を定期的に実行
3. ✅ CSV更新後は必ずJSON変換
4. ✅ 新規用語集追加時は即座にCSV再生成
5. ✅ YAMLパースエラーに注意
