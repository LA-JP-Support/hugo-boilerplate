# YouTube動画紹介記事作成ワークフロー

このドキュメントは、YouTube動画を紹介するブログ記事を作成する際の手順と、ユーザー（あなた）とAIアシスタント（Cascade）の役割分担をまとめたものです。

## 1. 役割分担

### 👤 ユーザー（あなた）の役割
*   **原稿の用意**: 記事の元となるテキストまたはMarkdownファイルを作成し、プロジェクトに追加する。
*   **動画情報の提供**: 紹介するYouTube動画のURLまたはID、タイトルを共有する。
*   **最終確認**: AIが修正した記事の内容、動画の表示、レイアウトを確認する。

### 🤖 Cascade（AI）の役割
*   **ファイル名の正規化**: ファイル名をURLに適した形式（半角小文字、ハイフン区切り）に修正する。
*   **Frontmatterの整備**: Hugo用のメタデータ（YAML形式）を適切に設定する。
*   **動画埋め込みの適用**: 指定されたHTML形式でYouTube動画を埋め込む。
*   **FAQの整形**: Frontmatterではなく、本文末尾にMarkdown形式でFAQセクションを作成する。

---

## 2. 作業手順

### ステップ 1: 原稿のアップロード
ユーザーは、`content/en/blog/`（英語記事の場合）または`content/ja/blog/`（日本語記事の場合）に原稿ファイルを配置します。
ファイル名は一時的なものでも構いませんが、内容はMarkdown形式が望ましいです。

### ステップ 2: AIへの依頼
ユーザーはAIに対して、「この記事をYouTube動画紹介記事として修正してください」と依頼します。動画のURLやIDも併せて伝えます（原稿に含まれている場合は不要）。

### ステップ 3: 記事の修正（AI作業）
AIは以下のルールに従って記事を修正します。

#### 3.1 ファイル名
*   **ルール**: すべて小文字、単語間はハイフン(`-`)で区切る。
*   **例**: `Project Vend- How Claude AI....md` -> `project-vend-claude-ai-autonomous-agents.md`

#### 3.2 Frontmatter (YAML)
以下の項目を必須として設定します。`layout: single-youtube`が特に重要です。

**重要**: 日付が未設定だと `Created: January 1, 0001` のような不正な表示になるため、`date`（作成日）は必ず設定してください。更新を行った場合は `lastmod` も更新してください。

```yaml
---
title: "記事のタイトル"
date: 2025-01-01
lastmod: 2025-01-01
draft: false
translationKey: "unique-translation-key"  # ファイル名と同じものを推奨
layout: single-youtube                    # 必須：これにより「Staff-Selected Featured Video」が表示される
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

**注意**: `faq`セクションはFrontmatterには記述しません。

#### 3.3 動画の埋め込み (HTML)
本文の冒頭（Introductionの後など）に、以下のHTML形式で動画を埋め込みます。Hugoのショートコード（`{{< youtubevideo ... >}}`）ではなく、以下のレスポンシブHTMLを使用してください。

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

*   `VIDEO_ID` と `動画タイトル` を適切な値に置き換えてください。

#### 3.4 FAQセクション
FAQはFrontmatterではなく、**記事の最後（Conclusionの後）にMarkdownの見出しとして**追加します。

```markdown
## FAQ

### Q1. 質問内容は？
回答内容をここに記述します。

### Q2. 次の質問は？
次の回答をここに記述します。
```

#### 3.5 内部リンクの適用
記事内のキーワードを用語集（Glossary）への内部リンクに変換します。以下のコマンドを実行してください。

```bash
python3 scripts/add_internal_links.py content/en/blog --glossary-dir content/en/glossary --lang en
```

※日本語記事の場合はパスと言語コード（`--lang ja`）を変更してください。

**重要**: スクリプト実行後、YouTube埋め込みコード（`<iframe>`）内のURLが変更されていないことを必ず確認してください。特に `src` 属性内のURLがMarkdownリンク形式（`[YouTube](...)`）に変換されてしまっていないか注意が必要です。

### ステップ 4: 確認
修正が完了したら、ユーザーはローカルサーバー（http://localhost:1313/）で記事を表示し、以下の点を確認します。
1.  記事上部に「Staff-Selected Featured Video」（または日本語訳）の注釈が表示されているか。
2.  YouTube動画が正しく表示・再生されるか（内部リンク適用によりURLが破損していないか）。
3.  FAQが記事の末尾に正しく表示されているか。
4.  記事内の重要キーワードに内部リンクが設定されているか。

---

## 3. チェックリスト (AI用)

修正を行う前に、AIはこのチェックリストを確認してください。

- [ ] ファイル名は `kebab-case.md` になっているか？
- [ ] Frontmatterは YAML (`---`) 形式か？
- [ ] Frontmatterに `layout: single-youtube` が含まれているか？
- [ ] Frontmatterから `faq` 配列が削除されているか？
- [ ] 動画埋め込みは `<iframe>` を含むレスポンシブHTML形式か？
- [ ] FAQは記事末尾にMarkdown形式 (`## FAQ`) で記述されているか？
- [ ] 日付 (`date`) は適切か？（未来の日付になっていないか確認）
- [ ] `lastmod` が設定されているか？（更新した場合は `lastmod` を更新）
- [ ] 内部リンク適用スクリプト (`scripts/add_internal_links.py`) を実行したか？
- [ ] 内部リンク適用後、YouTube埋め込み (`<iframe>`) のURLが破損していないか確認したか？

