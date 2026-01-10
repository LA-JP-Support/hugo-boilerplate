# FlowHunt → HUGO Glossary ワークフロー

FlowHunt生成記事をHUGO Glossaryに配置するまでの完全ガイドです。

## 📂 ディレクトリ構造

```
hugo-boilerplate/
├── content-drafts/              ← FlowHunt生成ファイル（クリーンアップ前）
│   ├── en/                      ← 英語記事
│   └── ja/                      ← 日本語記事
├── content/
│   ├── en/
│   │   └── glossary/            ← ✅ 英語記事（公開用・クリーンアップ済み）
│   └── ja/
│       └── glossary/            ← ✅ 日本語記事（公開用・クリーンアップ済み）
└── cleanup_flowhunt_output.py
```

---

## 🚀 基本ワークフロー

### ステップ1: FlowHuntファイルを配置

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

# FlowHuntからダウンロードしたファイルをcontent-draftsに配置
cp ~/Downloads/Conversation-Drift.md ./content-drafts/en/
```

### ステップ2: クリーンアップして直接glossaryに配置

#### 🎯 方法A: 単一ファイルを処理（推奨）

```bash
# 英語記事を処理
python3 cleanup_flowhunt_output.py \
  ./content-drafts/en/Conversation-Drift.md \
  ./content/en/glossary/conversation-drift.md

# 日本語記事を処理
python3 cleanup_flowhunt_output.py \
  ./content-drafts/ja/Conversation-Drift.md \
  ./content/ja/glossary/conversation-drift.md
```

#### 🎯 方法B: 複数ファイルを一括処理

```bash
# content-drafts/en/内の全ファイルを直接glossaryに配置
python3 cleanup_flowhunt_output.py \
  ./content-drafts/en/ \
  --output ./content/en/glossary/

# 日本語版
python3 cleanup_flowhunt_output.py \
  ./content-drafts/ja/ \
  --output ./content/ja/glossary/
```

### ステップ3: プレビュー確認
 
```bash
hugo server
# http://localhost:1313/en/glossary/ で確認
```

**注意**:
- `hugo server` は **HTML後処理（内部リンク付与）を自動実行しません**。
- 内部リンク付きで確認したい場合は、Hugoで静的ビルドした `public/` に対して `scripts/linkbuilding_parallel.py` を実行し、静的サーバで `public/` を配信して確認してください。
- 手順は `docs/INTERNAL_LINKING_QUICK_START.md` の「ローカルで内部リンク付き」を参照。

### ステップ4: Gitにコミット
 
```bash
# 新しい記事を追加
git add content/en/glossary/conversation-drift.md
git commit -m "Add glossary: Conversation Drift"
git push
```

---

## 📋 詳細コマンド一覧

### 単一ファイル処理

```bash
# 基本形
python3 cleanup_flowhunt_output.py <入力ファイル> <出力ファイル>

# 例
python3 cleanup_flowhunt_output.py \
  ./content-drafts/en/API-Endpoint.md \
  ./content/en/glossary/api-endpoint.md
```

### 一括処理

```bash
# 基本形
python3 cleanup_flowhunt_output.py <入力ディレクトリ> --output <出力ディレクトリ>

# 例：英語記事を一括処理
python3 cleanup_flowhunt_output.py \
  ./content-drafts/en/ \
  --output ./content/en/glossary/

# 例：日本語記事を一括処理
python3 cleanup_flowhunt_output.py \
  ./content-drafts/ja/ \
  --output ./content/ja/glossary/
```

### デフォルト動作（/cleanに出力）

```bash
# 出力先を指定しない場合、/cleanサブディレクトリに出力
python3 cleanup_flowhunt_output.py ./content-drafts/en/

# 出力先: ./content-drafts/en/clean/
```

---

## 💡 実践例

### 例1: 新規記事を1つ追加

```bash
# 1. FlowHuntファイルをダウンロード
# 2. content-draftsに配置
cp ~/Downloads/Chatbot-Testing.md ./content-drafts/en/

# 3. クリーンアップしてglossaryに配置
python3 cleanup_flowhunt_output.py \
  ./content-drafts/en/Chatbot-Testing.md \
  ./content/en/glossary/chatbot-testing.md

# 4. 確認
hugo server

# 5. コミット
git add content/en/glossary/chatbot-testing.md
git commit -m "Add glossary: Chatbot Testing"
git push
```

### 例2: 複数記事を一度に追加

```bash
# 1. FlowHuntファイルを複数ダウンロードしてcontent-drafts/en/に配置
cp ~/Downloads/*.md ./content-drafts/en/

# 2. 一括クリーンアップ
python3 cleanup_flowhunt_output.py \
  ./content-drafts/en/ \
  --output ./content/en/glossary/

# 3. 確認
hugo server

# 4. 一括コミット
git add content/en/glossary/
git commit -m "Add multiple glossary articles"
git push
```

### 例3: 既存のFlowHunt-Dataから処理

```bash
# FlowHunt-Dataディレクトリから直接glossaryに配置
python3 cleanup_flowhunt_output.py \
  /Users/TM-MBP1/Documents/FlowHunt-Data/Conversation-Drift.md \
  ./content/en/glossary/conversation-drift.md
```

---

## 🔧 ファイル命名のベストプラクティス

### FlowHuntファイル名（例）
```
Conversation-Drift.md
API-Endpoint-Configuration.md
Conversational-AI.md
```

### HUGO用ファイル名（推奨）
```
conversation-drift.md         ← 小文字・ハイフン区切り
api-endpoint-configuration.md
conversational-ai.md
```

**理由**: 
- URLが読みやすくなる
- SEOに有利
- 一貫性が保たれる

---

## 🎨 処理内容

スクリプトが自動的に行う処理：

### ✅ 変換
- フロントマター: TOML → YAML
- `draft: true` → `draft: false`
- 日付フィールドの自動挿入 (`date: 2025-12-02`)

### ✅ 削除
- H1見出し（`# Glossary: XXX`）
- フロントマター直後の重複メタデータ
- `## Table of Contents` セクション
- 本文中の区切り線（`---`）

### ✅ 保持
- 最初の `##` 見出し以降の全コンテンツ
- 本文中の `**Definition:**`、`**Analogy:**` など

---

## 📊 処理前後の比較

### 処理前（FlowHunt生成）
```markdown
---
title = "Conversation Drift"
draft = true
---

---
# Glossary: Conversation Drift
---
**Category:** AI Chatbot & Automation
**Definition:** ...
---

## Table of Contents
- [What is...]

---

## What is Conversation Drift?
Content...
```

### 処理後（HUGO用）
```markdown
---
title: "Conversation Drift"
date: 2025-12-02
draft: false
---

## What is Conversation Drift?
Content...
```

---

## 🔍 トラブルシューティング

### ファイルが見つからない

```bash
# ファイルの存在確認
ls -la ./content-drafts/en/
ls -la ./content/en/glossary/
```

### 出力ディレクトリが作成されない

```bash
# ディレクトリを手動で作成
mkdir -p ./content/en/glossary/
```

### 権限エラー

```bash
# 実行権限を付与
chmod +x cleanup_flowhunt_output.py
```

---

## 📚 関連ドキュメント

- [cleanup_flowhunt_output.py 詳細ガイド](./CLEANUP_README.md)
- [content-drafts の使い方](./content-drafts/README.md)

---

**更新日**: 2025-12-02
