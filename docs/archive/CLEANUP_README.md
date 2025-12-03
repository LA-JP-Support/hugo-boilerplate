# FlowHunt Article Cleanup Script

FlowHunt AIが生成したGlossary記事をHUGO対応形式に自動変換するPythonスクリプトです。

## 機能

### 自動変換
- ✅ フロントマター: TOML → YAML形式
- ✅ `draft: true` → `draft: false`
- ✅ 日付フィールドの自動挿入 (`date: 2025-12-02`)

### 不要コンテンツの削除
- ✅ H1見出し（`# Glossary: XXX`）
- ✅ フロントマター直後の重複メタデータ（`**Category:**`、`**Definition:**`）
- ✅ 目次セクション（`## Table of Contents`）
- ✅ 本文中の区切り線（`---`）

### 本文の保持
- ✅ 最初の `##` 見出し以降の全コンテンツ
- ✅ 本文中の `**Definition:**`、`**Analogy:**` など

## 使用方法

### 基本コマンド

```bash
# 1. 特定のディレクトリ内の全.mdファイルを処理
python3 cleanup_flowhunt_output.py /path/to/articles/

# 2. カレントディレクトリの全.mdファイルを処理
python3 cleanup_flowhunt_output.py .

# 3. 単一ファイルを処理
python3 cleanup_flowhunt_output.py article.md

# 4. 出力先を明示的に指定
python3 cleanup_flowhunt_output.py input.md output.md
```

### HUGOサイトでの使用例

```bash
# FlowHunt-Dataディレクトリの記事を処理
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
python3 cleanup_flowhunt_output.py /Users/TM-MBP1/Documents/FlowHunt-Data/

# 処理済みファイルは /FlowHunt-Data/clean/ に保存されます
```

### contentディレクトリに直接配置する場合

```bash
# FlowHunt-Dataディレクトリの記事を処理してcontent/en/glossary/に出力
python3 cleanup_flowhunt_output.py /Users/TM-MBP1/Documents/FlowHunt-Data/article.md ./content/en/glossary/article.md
```

## 処理例

### 変換前
```markdown
---
title = "Conversation Drift"
draft = true
---

---

# Glossary: Conversation Drift

---
**Category:** AI Chatbot & Automation
**Definition:**
Conversation drift is...
---

## Table of Contents
- [What is...]

---

## What is Conversation Drift?

Content here...
```

### 変換後
```markdown
---
title: "Conversation Drift"
date: 2025-12-02
draft: false
---

## What is Conversation Drift?

Content here...
```

## 依存関係

- Python 3.6+
- 標準ライブラリのみ（追加インストール不要）

## 出力先

デフォルトでは元のディレクトリに `/clean` サブディレクトリを作成して保存します。

```
FlowHunt-Data/
├── article1.md
├── article2.md
└── clean/           ← 処理済みファイルの出力先
    ├── article1.md
    └── article2.md
```

## トラブルシューティング

### ファイルが見つからない
```bash
# パスを確認
ls -la /path/to/directory/
```

### 権限エラー
```bash
# スクリプトに実行権限を付与
chmod +x cleanup_flowhunt_output.py
```

### エンコーディングエラー
ファイルがUTF-8エンコーディングであることを確認してください。

## ライセンス

MIT License

## 更新履歴

- 2025-12-02: 初版リリース
  - TOML→YAML変換
  - 日付自動挿入
  - 不要コンテンツの削除
  - 本文中の`---`削除
