# コンテンツ作成ワークフロー

コンテンツタイプごとの作成手順を統合したガイドです。各タイプの必須フロントマター、作成手順、品質チェックリストをまとめています。

---

## 共通ルール（全コンテンツタイプ共通）

- **Markdownに内部リンクを直接挿入しない**（HTML後処理方式: `linkbuilding_parallel.py`）
- **`public/` は都度生成する成果物**（Git管理しない / 手編集しない）
- **Markdownを書き換えるスクリプトは原則禁止**（`--dry-run` → 少数テスト → 全体適用）
- **編集前にバックアップを取る**（`git commit` または `cp -r`）
- **参考資料の見出しは固定**: 英語 `## References` / 日本語 `## 参考資料`

### フロントマター検証（全タイプ共通）

```bash
# 単一ファイルを検証
python scripts/validate_frontmatter.py content/ja/blog/my-article.md

# ディレクトリ単位で検証
python scripts/validate_frontmatter.py content/ja/glossary/

# 全コンテンツを検証
python scripts/validate_frontmatter.py --all

# translationKey の EN/JA 整合性チェック
python scripts/validate_frontmatter.py --check-translations
```

---

## A. Glossary用語集

### 必須フロントマター

```yaml
---
title: "用語名"
date: 2026-01-01
lastmod: 2026-01-01
draft: false
translationKey: "term-name"
url: "/ja/glossary/term-name/"
description: "1-2文、最大100文字以内の簡潔な説明"
keywords:
  - キーワード1
  - キーワード2
tags:
  - Tag1
categories:
  - Category
type: glossary
e-title: "English Title"        # 英語の正式名称
term: "たーむねーむ"              # 読み/表記揺れ対策（ひらがな）
---
```

### 作成手順（完全版: 10ステップ）

詳細は `docs/SCRIPTS_USAGE_GUIDE.md` の「推奨ワークフロー」セクション参照。

```bash
# 1. CSVから記事作成（英語）
python scripts/batch_create_from_csv.py --workers 5

# 2. description最適化（英語）
python scripts/optimize_glossary_descriptions.py --lang en --workers 5

# 3. 翻訳（英語→日本語）
python scripts/translate_glossary_en_to_ja.py --workers 5

# 4. description最適化（日本語）
python scripts/optimize_glossary_descriptions.py --lang ja --workers 5

# 5. 用語読み修正（日本語）
python scripts/fix_term_readings_ja.py --ja-dir content/ja/glossary

# 6. Hugoビルド
hugo --destination public --cleanDestinationDir

# 7. かなインデックス追加（日本語）
python scripts/add_kana_index.py --glossary-dir content/ja/glossary

# 8. 内部リンク追加（HTML後処理）
python3 scripts/linkbuilding_parallel.py \
    --linkbuilding-dir data/linkbuilding \
    --public-dir public \
    --denylist-dir databases \
    --max-workers 4

# 10. 最終確認
hugo server -D
```

### クイックスタート（5記事テスト）

```bash
python scripts/batch_create_from_csv.py --start 0 --end 5 --workers 3
python scripts/translate_glossary_en_to_ja.py --start 0 --end 5 --workers 3
```

### 品質チェックリスト

- [ ] `title` が適切（タイトル翻訳ガイドに準拠）
- [ ] `translationKey` が EN/JA で一致
- [ ] `description` が簡潔（冗長な前置き禁止）
- [ ] `keywords` リストが設定済み
- [ ] `e-title` と `term` が日本語版に設定済み
- [ ] `## References` / `## 参考資料` 見出しが統一

---

## B. Blog記事（通常）

### 必須フロントマター

```yaml
---
title: "記事タイトル"
date: 2026-01-01
lastmod: 2026-01-01
draft: false
translationKey: "unique-slug"
url: "blog/unique-slug/"
description: "記事の概要"
image: "/images/blog/image-name.jpg"
keywords:
  - キーワード1
  - キーワード2
tags:
  - Tag1
  - Tag2
categories:
  - Category
---
```

### 作成手順

```bash
# 1. 記事作成
hugo new content/ja/blog/my-article.md

# 2. 画像配置
cp my-image.jpg static/images/blog/

# 3. 画像最適化
bash scripts/preprocess-images.sh

# 4. ローカル確認
hugo server -D
# → http://localhost:1313/ja/blog/my-article/

# 5. 翻訳（必要な場合）
python scripts/translate_blog_with_flowhunt.py

# 6. commit → dev → 確認 → main
```

### 品質チェックリスト

- [ ] `date` が実際の作成日
- [ ] `description` が簡潔
- [ ] `image` パスが正しい
- [ ] 画像に `width` / `height` 属性あり
- [ ] `translationKey` が EN/JA で一致
- [ ] 太字の助詞が正しい（`**単語**の` ✅ / `**単語の**` ❌）
- [ ] `## References` / `## 参考資料` 見出しが統一

---

## C. Blog記事（YouTube動画紹介）

### 必須フロントマター

```yaml
---
title: "記事のタイトル"
date: 2026-01-01
lastmod: 2026-01-01
draft: false
translationKey: "unique-translation-key"
url: "blog/unique-translation-key/"
layout: single-youtube                    # 必須
youtubeTitle: "動画のタイトル"
youtubeVideoID: "VIDEO_ID"                # 例: 5KTHvKCrQ00
description: "記事の概要"
image: "https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg"
keywords: ["keyword1", "keyword2"]
tags: ["Tag1", "Tag2"]
categories: ["Category"]
showCTA: true
ctaHeading: "CTAの見出し"
ctaDescription: "CTAの説明文"
---
```

### 動画埋め込み（レスポンシブ）

```html
<div style="max-width: 768px; margin: 2rem auto 3rem;">
  <div style="position: relative; width: 100%; padding-top: 56.25%; border-radius: 18px; overflow: hidden; box-shadow: 0 25px 60px rgba(0,0,0,0.25); background: #000;">
    <iframe
      style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;"
      src="https://www.youtube.com/embed/VIDEO_ID"
      title="動画タイトル"
      frameborder="0"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen>
    </iframe>
  </div>
</div>
```

### FAQ セクション（Markdownで記述）

```markdown
## よくある質問（FAQ）

### Q1: 質問テキスト？

回答テキスト。

### Q2: 質問テキスト？

回答テキスト。
```

### 役割分担

- **ユーザー**: ドラフト原稿、動画情報の提供、最終レビュー
- **AI（Cascade）**: ファイル名正規化、フロントマター設定、動画埋め込み、FAQ整形

### 品質チェックリスト

- [ ] `layout: single-youtube` が設定済み
- [ ] `youtubeVideoID` が正しい
- [ ] iframe 埋め込みがレスポンシブ
- [ ] FAQがMarkdown形式で記述
- [ ] 内部リンクはHTML後処理で適用（Markdown直接編集しない）

詳細: `docs/youtube-article-workflow.md`

---

## D. Serviceページ

### サービス名定義（JP/EN対応表）

| 日本語名 | 英語名 | ファイル |
| --- | --- | --- |
| AIチャットボット | AI Chatbot | `content/ja/services/ai-chatbot.md` |
| AI連携チケットシステム | AI-Integrated Ticket System | `content/ja/services/ticket-system.md` |
| AIメール回答作成 | AI Answer Composer | `content/ja/services/email-automation.md` |
| AI回答アシスト | AI Answer Improver | `content/ja/services/ai-answer-assistant.md` |

### 必須フロントマター

```yaml
---
title: "サービス名"
description: "サービスの説明"
type: services
draft: false
translationKey: "service-slug"
badge: "バッジテキスト"
hero_heading: "ヒーロー見出し"
hero_description: "ヒーロー説明文"
cta_primary:
  text: "CTAボタンテキスト"
  url: "/contact/"
introduction:
  heading: "紹介見出し"
  text: "紹介テキスト"
features:
  - icon: "icon-name"
    title: "機能名"
    description: "機能説明"
---
```

### 作成手順

```bash
# 1. 記事作成（archetype を使用）
hugo new content/ja/services/new-service.md
# → archetypes/services.md をテンプレートとして生成

# 2. フロントマターと本文を編集

# 3. 画像配置
mkdir -p static/images/services/new-service/
cp images/* static/images/services/new-service/

# 4. 画像最適化
bash scripts/preprocess-images.sh

# 5. 対訳ファイルを作成（translationKeyで紐付け）
cp content/en/services/ai-chatbot.md content/en/services/new-service.md

# 6. ローカル確認
hugo server -D
# → http://localhost:1313/ja/services/new-service/

# 7. commit → dev → 確認 → main
```

### 品質チェックリスト

- [ ] `type: services` が設定済み
- [ ] `translationKey` が EN/JA で一致
- [ ] `features` リストが正しい構造
- [ ] 画像パスが正しい
- [ ] EN/JA 両方のファイルが存在

---

## E. Supportセクション（/support）

### 必須フロントマター

#### カテゴリー（_index.md）

```yaml
---
title: "カテゴリー名"
description: "説明"
weight: 25
type: support
---
```

#### 個別記事

```yaml
---
title: "記事タイトル"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "unique-key"
description: "記事の説明"
keywords: ["keyword1", "keyword2"]
type: support
category: "category-name"
weight: 10
---
```

### カテゴリー一覧（weight順）

| 順序 | カテゴリー | フォルダ名 | weight |
|------|-----------|-----------|--------|
| 1 | はじめに | `getting-started/` | 10 |
| 2 | AI機能の基礎知識 | `ai-fundamentals/` | 15 |
| 3 | AIチャットボット | `ai-chatbot/` | 25 |
| 4 | AIメール回答作成 | `email-composer/` | 30 |
| 5 | AI回答アシスト | `ai-answer-assist/` | 35 |
| 6 | AI連携チケットシステム | `ticket-system/` | 40 |
| 7 | 設定・カスタマイズ | `settings/` | 50 |
| 8 | セキュリティ | `security/` | 60 |
| 9 | 料金・契約 | `pricing/` | 70 |

### 記事内 weight の推奨範囲

| グループ | weight | 例 |
|---------|--------|---|
| 導入・概要 | 10-30 | サービス紹介、概要説明 |
| 主要機能 | 40-60 | 機能説明、設定方法 |
| 応用・活用 | 70-100 | 活用事例、連携方法 |
| リファレンス | 150-200 | 用語集、FAQ |

### 作成手順

```bash
# 1. カテゴリーの _index.md を作成（新規カテゴリーの場合）
mkdir -p content/ja/support/new-category/
# _index.md を作成（weight を適切に設定）

# 2. 記事を作成
# content/ja/support/category-name/article-slug.md

# 3. ローカル確認
hugo server -D
# → http://localhost:1313/ja/support/

# 4. 英語版も作成（translationKeyで紐付け）

# 5. commit → dev → 確認 → main
```

### 品質チェックリスト

- [ ] `type: support` が設定済み
- [ ] `weight` が適切
- [ ] カテゴリーの `_index.md` が存在
- [ ] `translationKey` が設定済み
- [ ] サイドバーナビに正しく表示される

詳細: `docs/SUPPORT_SECTION_GUIDE.md`

---

## 共通: デプロイフロー

```bash
# 1. ローカルビルド確認
hugo --minify

# 2. ローカルサーバーで目視確認
hugo server
# → /ja/ と /en/ を確認

# 3. dev ブランチにpush（ステージング）
git checkout dev
git merge feature-branch
git push

# 4. Amplify dev デプロイ確認
# → noindex, robots.txt, canonical を検証

# 5. main ブランチにpush（本番）
git checkout main
git merge dev
git push

# 6. PageSpeed Insights 確認（デプロイ後10分以内）
# → モバイル Performance 75+, CLS < 0.1, TBT < 200ms
```

詳細: `docs/DEPLOYMENT_CHECKLIST.md`

---

## 翻訳時の注意事項

全コンテンツタイプ共通の翻訳ルール（詳細は `docs/TRANSLATION_GUIDELINES.md`）:

- **太字の助詞**: `**Anthropic**のClaude` ✅ / `**Anthropicの**Claude` ❌
- **太字 + 日本語句読点**: `**「強調表示」**&#8203;と` （ZWS を使用）
- **技術用語・ブランド名**: 英語のまま保持
- **用語の一貫性**: `docs/TRANSLATION_GLOSSARY.md` を参照
- **用語集タイトル翻訳判定**: `docs/GLOSSARY_TITLE_TRANSLATION_GUIDE.md` を参照

---

## 関連ドキュメント

| ドキュメント | 内容 |
|---|---|
| `docs/00_START_HERE.md` | 入口・ナビゲーション |
| `docs/SCRIPTS_USAGE_GUIDE.md` | スクリプト総合ガイド |
| `docs/INTERNAL_LINK_SYSTEM_GUIDE.md` | 内部リンクシステム |
| `docs/TRANSLATION_GUIDELINES.md` | 翻訳フォーマットルール |
| `docs/TRANSLATION_GLOSSARY.md` | 翻訳用語集 |
| `docs/GLOSSARY_TITLE_TRANSLATION_GUIDE.md` | 用語集タイトル翻訳判定 |
| `docs/DEPLOYMENT_CHECKLIST.md` | デプロイチェックリスト |
| `docs/PAGESPEED_OPTIMIZATION.md` | PageSpeed最適化 |
| `docs/IMAGE_OPTIMIZATION.md` | 画像最適化 |
| `docs/SUPPORT_SECTION_GUIDE.md` | Supportセクション実装 |
| `docs/youtube-article-workflow.md` | YouTube記事ワークフロー（詳細版） |

---

## 更新履歴

- **2026-02-07 (v1.0)**: 初版作成
  - Blog/Glossary/Service/YouTube/Support の統合ワークフロー
  - SERVICE_NAME_DEFINITIONS.md と reference-heading-guidelines.md の内容を統合
