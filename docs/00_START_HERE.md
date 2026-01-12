# 00. Start Here（最初にお読みください）

このドキュメントは、AI支援で作業する際に「今どれが最新で正しい手順か」「どのファイルが権威（source of truth）か」を最短で把握するための入口です。

---

## リポジトリの3層（固定）

- **Source（編集対象 / 権威）**
  - 人間が編集し、Gitで管理する “正” の情報。
  - 例: `content/`, `layouts/`, `data/`, `databases/`, `docs/`

- **Derived（中間生成物）**
  - 作業に応じて生成する中間物。
  - 例: `content-clean/`（クリーンなMarkdown）

- **Artifact（ビルド成果物）**
  - 毎回生成し直す成果物。**Git管理しない**（`.gitignore` で除外）。
  - 例: `public/`（内部リンク後のHTML、`data-lb="1"` マーカー付き）

---

## 重要ルール（これだけ先に読む）

- **`public/` は都度生成する成果物**（Git管理しない / 手編集しない）
- **内部リンクの標準方式はHTML後処理**
  - `public/` のHTMLに対してリンク付与する
- **用語集検索は `index.json` + Fuse.js（クライアント検索）**

---

## 運用ルール（固定）

1. **Markdown（`content/.../*.md`）は、本文やフロントマターを更新する必要がある場合のみ編集する**
2. **ツールチップは「用語集キーワードを使った通常の内部リンク」に統一する**
   - ネストしたリンクや、title 属性付きの旧ツールチップ形式は使用しない
3. **内部リンクは全てHTML後処理で作成する**
   - Hugoビルド後の `public/` に対して `scripts/linkbuilding_parallel.py` を実行する
   - Markdown（`content/` / `content-clean/`）に内部リンクを直接挿入しない
   - 内部リンクのリンク先は **用語集（`/ja/glossary/` / `/en/glossary/`）に統一**し、`/ja/services/` にはリンクしない
4. **Markdownを書き換えるスクリプトは原則使用しない。例外的に使う場合は安全柵を必須とする**
   - `--dry-run` がある場合は必ず先に実行
   - まず1ファイル、次に少数ファイルで検証してから全体適用
   - `git` で確実に戻せる状態（コミット/ブランチ/restore）を作ってから実行
   - 参考: `docs/SCRIPTS_USAGE_GUIDE.md` の「Markdown（.md）を書き換えるスクリプト一覧（事故防止）」

補足:

- `public-test/` を使う検証フローは廃止（アーカイブ）
  - `docs/HTML_LINKBUILDING_TEST_GUIDE.md`

---

## 作業別ナビ（まずここから）

### A. 内部リンクを作り直したい（EN/JA + blog/glossary）

- **クイックスタート**: `docs/INTERNAL_LINKING_QUICK_START.md`
- **システム全体**: `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`

標準フロー（要点）:

1. （必要なら）辞書再生成: `scripts/extract_automatic_links.py`
2. Hugoビルド: `hugo --contentDir content-clean --destination public --cleanDestinationDir`
3. リンク付与: `python3 scripts/linkbuilding_parallel.py --linkbuilding-dir data/linkbuilding --public-dir public --denylist-dir databases`
4. 確認: `data-lb="1"` 件数

### B. 用語集検索（/search）を改善したい（AGI/NLP等の表記揺れ）

- **ガイド**: `docs/GLOSSARY_OPTIMIZATION_GUIDE.md`

権威ファイル:

- `layouts/_default/index.json`（検索インデックス）
- `layouts/partials/search_field.html`（ヘッダー検索）
- `layouts/_default/search.html`（検索ページ）

### C. 用語集を追加/更新したい（検索に強くする）

- **ガイド**: `docs/GLOSSARY_OPTIMIZATION_GUIDE.md`
- **入力（編集対象）**: `content/{en,ja}/glossary/*.md`

### D. CSV（リンクDB）を更新したい

- **ガイド**: `docs/CSV_DATABASE_SYSTEM_GUIDE.md`

### E. 翻訳ルールを確認したい（太字/助詞など）

- `docs/TRANSLATION_GUIDELINES.md`
- `docs/TRANSLATION_GLOSSARY.md`

### F. サービスページの名称定義（JP/EN対応表）を確認したい

- `docs/SERVICE_NAME_DEFINITIONS.md`

---

## ディレクトリ新設時のルール（必須）

新しいディレクトリを追加した場合は、**そのディレクトリ直下に `README.md` を作成**し、最低限以下を記載します。

- **目的/役割**（何のためのディレクトリか）
- **3層のどれか**（Source / Derived / Artifact）
- **権威（source of truth）**かどうか
- **生成手順**（入力→出力、使うスクリプト/コマンド）
- **削除条件**（いつ削除してよいか、再生成できるか）
- **Git管理**（含める/除外する）

また、作業ログ（例: `docs/WORK_SUMMARY_YYYY-MM-DD.md`）に、追加したディレクトリと目的を追記します。

---

## AIに作業依頼するときのテンプレ（コピペ用）

- **目的**:
- **対象言語**: EN / JA
- **対象範囲**: blog / glossary / search / internal linking / csv
- **権威ファイル（必ず参照）**:
- **成功条件（確認方法）**:
- **禁止事項**:
  - `public/` を手編集しない（生成物）
  - Markdownへ内部リンクを直接挿入しない（標準はHTML後処理）
