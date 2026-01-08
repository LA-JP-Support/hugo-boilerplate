# Glossary Optimization Guide（用語集最適化ガイド）

## 概要

このドキュメントは、用語集（Glossary）の品質・検索性を維持するための運用ルールをまとめたものです。

対象:

- 用語集（`content/{en,ja}/glossary/*.md`）のフロントマター品質
- サイト内検索（`/search`）でのヒット精度（日本語/英語/略語/カタカナ）

---

## 1. Glossary追加/更新時の必須チェック（検索に効く項目）

日本語用語集（`content/ja/glossary/*.md`）で、最低限以下を揃えると検索・表示が安定します。

- `title`
- `translationKey`
- `description`
- `keywords`（リスト）
- `e-title`（英語タイトル。英語の正式名称がある場合）
- `term`（読み/表記揺れ対策用の主要表記。例: ひらがな、カタカナ、読み）

---

## 2. サイト内検索の仕組み（どこを直すか）

検索は **クライアント側でFuse.js** を使って `index.json` を検索します。

- **検索インデックス生成**: `layouts/_default/index.json`
- **ヘッダー検索（ポップアップ）**: `layouts/partials/search_field.html`
- **検索ページ（/search）**: `layouts/_default/search.html`

`index.json` には `searchText` を含めており、`title`/`eTitle`/`translationKey`/`term`/`keywords`/`description` 等を結合して検索精度を上げています。

---

## 3. 表記揺れ（略語/カタカナ/日本語）対応を増やす方法

AGI / NLP のように、

- 英字略語
- 日本語訳
- カタカナ読み

を相互に検索できるようにするために、検索UI側でクエリを展開しています。

追加・調整する箇所:

- `layouts/partials/search_field.html` の `expandQuery()`
- `layouts/_default/search.html` の `expandQuery()`

追加例（概念）:

- `AGI` ↔ `エージーアイ`, `汎用人工知能`
- `NLP` ↔ `自然言語処理`, `エヌエルピー`

新しい略語・別名を追加した場合は、上記の同義語ペアへ追記してください。

---

## 4. 動作確認（追加後に必ずやる）

- `http://localhost:1313/ja/index.json` を開き、対象ページの
  - `title` / `eTitle` / `translationKey` / `term` / `keywords` / `searchText`
  が入っているか確認

- `http://localhost:1313/ja/search` とヘッダー検索の両方で確認
  - 例: `AGI`, `エージーアイ`, `汎用人工知能`
  - 例: `NLP`, `自然言語処理`, `エヌエルピー`

---

## 5. トラブルシューティング（反映されない/検索できない）

- `index.json` の内容が更新されない場合
  - HugoのFast Renderやキャッシュが原因になりやすいので、サーバを再起動して確認

- 追加した用語が検索に出ない場合
  - その用語ページが `index.json` に含まれているか（`lang`/`permalink`/`dir` など）を確認
  - フロントマターの `term` / `keywords` / `e-title` の不足を確認

---

## 関連ドキュメント

- `docs/00_START_HERE.md`
- `docs/SCRIPTS_USAGE_GUIDE.md`
- `docs/GLOSSARY_TITLE_TRANSLATION_GUIDE.md`
- `docs/TRANSLATION_GUIDELINES.md`
- `docs/CSV_DATABASE_SYSTEM_GUIDE.md`
- `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`
