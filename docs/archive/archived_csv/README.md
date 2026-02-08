# Archived CSV Files

**アーカイブ日**: 2026-01-08

このディレクトリには、現在使用されていないCSVファイルが保存されています。

## アーカイブされたファイル

### 1. target_generation.csv
- **用途**: コンテンツ生成ターゲットリスト
- **アーカイブ理由**: 現在のシステムで使用されていない
- **代替**: 新しいコンテンツ生成システムに移行

### 2. blog-words.csv
- **用途**: ブログキーワードリスト
- **アーカイブ理由**: 現在のシステムで使用されていない
- **代替**: `data/linkbuilding/*.json`で管理

### 3. all-words.csv
- **用途**: 全キーワードリスト
- **アーカイブ理由**: 現在のシステムで使用されていない
- **代替**: `databases/link_database_*.csv`で管理

### 4. glossaries_flowhunt.csv
- **用途**: FlowHunt用語集
- **アーカイブ理由**: 特定ツール用のデータ
- **代替**: 必要に応じて復元可能

### 5. prioritized_keywords.csv
- **用途**: 優先キーワードリスト
- **アーカイブ理由**: 現在のシステムで使用されていない
- **代替**: `data/linkbuilding/*.json`のPriorityフィールドで管理

## 現在使用中のCSVファイル

### databases/
- ✅ `link_database_en.csv` - 英語用語集データベース（1,222エントリ）
- ✅ `link_database_ja.csv` - 日本語用語集データベース（1,223エントリ）
- ✅ `danger_terms_en.csv` - 英語禁止用語リスト
- ✅ `danger_terms_ja.csv` - 日本語禁止用語リスト
- ✅ `translation_glossary.csv` - 翻訳用語対応表

### config/
- ✅ `translation_glossary.csv` - 翻訳用語対応表（databases/と同期）

## 復元方法

必要に応じて、このディレクトリから元の場所に復元できます：

```bash
# 例: target_generation.csvを復元
cp docs/archived_csv/target_generation.csv docs/
```

## 参照

- [CSV Database System Guide](../CSV_DATABASE_SYSTEM_GUIDE.md)
- [Internal Link System Guide](../INTERNAL_LINK_SYSTEM_GUIDE.md)
