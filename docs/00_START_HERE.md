# 00. Start Here（最初にお読みください）

このドキュメントは、AI支援で作業する際に「今どれが最新で正しい手順か」「どのファイルが権威（source of truth）か」を最短で把握するための入口です。

---

## リポジトリの3層（固定）

| 層 | 説明 | 例 |
|---|---|---|
| **Source** | 人間が編集し、Gitで管理する "正" の情報 | `content/`, `layouts/`, `data/`, `databases/`, `docs/` |
| **Artifact** | 毎回生成し直す成果物（**Git管理しない**） | `public/`（内部リンク後のHTML） |

---

## 重要ルール（これだけ先に読む）

1. **`public/` は都度生成する成果物**（Git管理しない / 手編集しない）
2. **内部リンクは全てHTML後処理で作成する**（Markdownに直接挿入しない）
3. **Markdownを書き換えるスクリプトは原則禁止**（`--dry-run` → 少数テスト → 全体適用）
4. **内部リンクのリンク先は用語集（`/glossary/`）に統一**し、`/services/` にはリンクしない
5. **編集前にバックアップを取る**（`git commit` またはディレクトリコピー）

---

## ドキュメント一覧（カテゴリ別）

### 📝 コンテンツ作成

| ドキュメント | 内容 |
|---|---|
| **[CONTENT_CREATION_WORKFLOWS.md](CONTENT_CREATION_WORKFLOWS.md)** | **⭐ Blog/Glossary/Service/YouTube/Support の統合ワークフロー** |
| [SCRIPTS_USAGE_GUIDE.md](SCRIPTS_USAGE_GUIDE.md) | スクリプト総合ガイド（記事作成・翻訳・リンク・メンテナンス） |
| [youtube-article-workflow.md](youtube-article-workflow.md) | YouTube動画紹介記事の詳細ワークフロー |

### 🌐 翻訳

| ドキュメント | 内容 |
|---|---|
| [TRANSLATION_GUIDELINES.md](TRANSLATION_GUIDELINES.md) | 翻訳フォーマットルール（太字・助詞・ZWS・プロンプト） |
| [TRANSLATION_GLOSSARY.md](TRANSLATION_GLOSSARY.md) | 翻訳用語集（165+ 用語の EN↔JA 対応表） |
| [GLOSSARY_TITLE_TRANSLATION_GUIDE.md](GLOSSARY_TITLE_TRANSLATION_GUIDE.md) | 用語集タイトル翻訳判定（Decision Tree） |

### 🔗 内部リンク

| ドキュメント | 内容 |
|---|---|
| [INTERNAL_LINKING_QUICK_START.md](INTERNAL_LINKING_QUICK_START.md) | クイックスタート（5分で開始） |
| [INTERNAL_LINK_SYSTEM_GUIDE.md](INTERNAL_LINK_SYSTEM_GUIDE.md) | システム全体ガイド（v2.2.0、Janome統合） |
| [INTERNAL_LINKING_ADOPTION_GUIDE.md](INTERNAL_LINKING_ADOPTION_GUIDE.md) | 他プロジェクトへの導入手順 |
| [CSV_DATABASE_SYSTEM_GUIDE.md](CSV_DATABASE_SYSTEM_GUIDE.md) | CSV/JSONリンクデータベースの管理 |

### ⚡ パフォーマンス・デプロイ

| ドキュメント | 内容 |
|---|---|
| [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) | デプロイ前後チェックリスト（PageSpeed基準値） |
| [PAGESPEED_OPTIMIZATION.md](PAGESPEED_OPTIMIZATION.md) | Core Web Vitals 最適化（CLS/LCP/TBT） |
| [IMAGE_OPTIMIZATION.md](IMAGE_OPTIMIZATION.md) | 画像最適化（WebP変換、レスポンシブ、CLS対策） |
| [AMPLIFY_MONOREPO_GUIDE.md](AMPLIFY_MONOREPO_GUIDE.md) | AWS Amplify モノレポ構成・dev/main分岐 |

### 🔍 検索・用語集品質

| ドキュメント | 内容 |
|---|---|
| [GLOSSARY_OPTIMIZATION_GUIDE.md](GLOSSARY_OPTIMIZATION_GUIDE.md) | 用語集フロントマター品質・Fuse.js検索最適化 |

### 🧩 機能ガイド

| ドキュメント | 内容 |
|---|---|
| [SUPPORT_SECTION_GUIDE.md](SUPPORT_SECTION_GUIDE.md) | /support セクション実装（3カラムレイアウト） |
| [SUPPORT_DOCS_LOTUSDOCS_GUIDE.md](SUPPORT_DOCS_LOTUSDOCS_GUIDE.md) | support-docs サイト運用（LotusDocs） |
| [LIVEAGENT_MULTIWIDGET_GUIDE.md](LIVEAGENT_MULTIWIDGET_GUIDE.md) | LiveAgent ウィジェット（お問い合わせ・チャット） |

---

## 内部リンク標準フロー（要点）

```bash
# 1.（必要なら）辞書再生成
python3 scripts/extract_automatic_links.py

# 2. Hugoビルド
hugo --destination public --cleanDestinationDir

# 3. リンク付与
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases

# 4. 確認
grep -r 'data-lb="1"' public/ | wc -l
```

---

## ディレクトリ新設時のルール（必須）

新しいディレクトリを追加した場合は、**そのディレクトリ直下に `README.md` を作成**し、以下を記載:

- **目的/役割** / **3層のどれか** / **権威かどうか**
- **生成手順**（入力→出力、使うスクリプト）
- **削除条件** / **Git管理**（含める/除外する）

---

## 🤖 Claude Code Agent Skills

Claude Code で使えるカスタムスラッシュコマンド。`.claude/skills/` に定義。
Windsurf など他のツールには影響しない（`.claude/` は Claude Code 専用）。

### スキル一覧

| コマンド | 内容 | 関連ドキュメント |
|---------|------|----------------|
| `/create-content` | Blog/Glossary/YouTube/Support/Service の新規作成 | [CONTENT_CREATION_WORKFLOWS.md](CONTENT_CREATION_WORKFLOWS.md) |
| `/translate` | EN→JA 翻訳（5大ルール + 165語の用語集を自動適用） | [TRANSLATION_GUIDELINES.md](TRANSLATION_GUIDELINES.md), [TRANSLATION_GLOSSARY.md](TRANSLATION_GLOSSARY.md) |
| `/internal-linking` | HTML後処理リンクパイプライン（辞書更新→ビルド→リンク→検証） | [INTERNAL_LINKING_QUICK_START.md](INTERNAL_LINKING_QUICK_START.md) |
| `/validate` | フロントマター/テーブル/翻訳/画像参照の品質チェック | [SCRIPTS_USAGE_GUIDE.md](SCRIPTS_USAGE_GUIDE.md) |
| `/deploy` | デプロイ前後チェックリスト（品質チェック→ビルド→PageSpeed） | [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) |
| `/glossary-pipeline` | 用語集バッチ作成の10ステップ一括実行（CSV→作成→翻訳→リンク） | [SCRIPTS_USAGE_GUIDE.md](SCRIPTS_USAGE_GUIDE.md) |
| *(自動参照)* | プロジェクトの5大ルール・禁止事項を全作業で自動適用 | この文書 |

### ディレクトリ構造

```
.claude/skills/
├── project-knowledge/SKILL.md   ← 背景知識（自動参照、ユーザー呼び出し不可）
├── create-content/SKILL.md
├── translate/SKILL.md
├── internal-linking/SKILL.md
├── validate/SKILL.md
├── deploy/SKILL.md
└── glossary-pipeline/SKILL.md
```

### 使い方

Claude Code のプロンプトで `/create-content AIエージェントのブログ記事` のように入力すると、対応するスキルが呼び出される。各スキルは既存の `docs/` ドキュメントを動的に参照するため、ドキュメントを更新すればスキルにも自動反映される。

---

## AIに作業依頼するときのテンプレ（コピペ用）

```
- 目的:
- 対象言語: EN / JA
- 対象範囲: blog / glossary / service / support / search / internal linking
- 権威ファイル（必ず参照）:
- 成功条件（確認方法）:
- 禁止事項:
  - public/ を手編集しない（生成物）
  - Markdownへ内部リンクを直接挿入しない（標準はHTML後処理）
```
