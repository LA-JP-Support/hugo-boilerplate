---
title: カノニカルURL
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Canonical-URL
description: カノニカルURLは、複数のURLが同じコンテンツを含む場合に、検索エンジンが優先すべき正式なURLを指定するSEO技術です。
keywords:
- カノニカルURL
- 重複コンテンツ
- SEO最適化
- rel canonical
- 検索エンジン最適化
category: コンテンツ・マーケティング
type: glossary
draft: false
e-title: Canonical URL
url: /ja/glossary/canonical-url/
aliases:
- /ja/glossary/Canonical-URL/
term: かのにかるゆーあーるえる
---

## カノニカルURLとは?

**カノニカルURLは、複数のURLが存在する場合に「これが正式なページです」と検索エンジンに教える指定方法です。** eコマースサイトで同じ商品ページが「?color=red」「?sort=price」など、異なるパラメータでアクセスできる場合があります。このように重複するURLが存在すると、検索エンジンが「どのURLを検索結果に表示すべきか」迷ってしまい、ランキングが分散してしまいます。カノニカルURLを指定することで、この問題を解決します。

> **ひとことで言うと：** 複数の入口がある同じ商品の陳列棚で「この入口からが正式です」と表示するようなものです。お客様がどこから入っても、検索エンジンは「公式入口」でカウントします。

**ポイントまとめ：**

- **何をするものか：** 同じコンテンツの複数のURLの中から「正式なURL」を指定し、検索エンジンに伝える
- **なぜ必要か：** 重複コンテンツによるランキング分散を防ぎ、SEO効果を集中させるため
- **誰が使うか：** eコマースサイト、CMS管理ブログ、複数の案内URLを持つWebサイト

## なぜ重要か

検索エンジンは限られたクローラー予算（Webサイト訪問時間）を持っています。重複ページばかり訪問していると、新しいページの発見が遅れてしまいます。また、ランキングシグナル（バックリンク数など）が分散すれば、それぞれのURLのランキングが下がります。カノニカルURLを正しく設定すれば、これらの問題が解決し、SEO効果が高まります。

## 仕組みをわかりやすく解説

HTMLの`<head>`タグの中に`<link rel="canonical" href="https://example.com/正式なURL">`という1行を追加するだけです。こうすることで、検索エンジンに「この正式なURLを検索結果に載せて、ランキング評価はこのURLに統合してください」と伝わります。HTTPヘッダーやサイトマップで指定することもできます。複数のパラメータを持つページ全てに、同じカノニカルURLを指定することが重要です。

## 実際の活用シーン

**eコマース** 商品ページが「色」「サイズ」「ソート順」など、複数の条件でアクセスできます。カノニカルURLで「基本のURL」を指定することで、ランキング分散を防ぎます。

**ブログ記事** 記事が「カテゴリー」と「タグ」の2つのパスでアクセスできる場合、どちらを正式とするか指定します。

**トラッキングパラメータ** Google Analytics用の「?utm_source=」などのパラメータ付きURLがランキングに悪影響を与えるのを防ぎます。

**モバイル対応** モバイル版とデスクトップ版が別URLの場合、どちらを「正式」とするか指定できます。

## メリットと注意点

カノニカルURLのメリットは、重複による悪影響を防ぎ、SEO効果を集中させられることです。設定も簡単です。

注意点として、間違ったURLを指定すると、本来評価されるべきページが検索結果から消えてしまいます。また、複数のページに異なるカノニカルURLを指定しても、検索エンジンは無視する場合があります。「絶対的な指示」ではなく「提案」という扱いのため、慎重な運用が必要です。

## よくある質問

**Q: 複数のカノニカルURLを指定できますか？**
A: いいえ。1ページには1つのカノニカルURLだけを指定すべきです。複数指定すると、検索エンジンが混乱します。

**Q: カノニカルURLとリダイレクトの違いは何ですか？**
A: リダイレクトは「このページを訪問した人を他のページに自動移動させる」もの。カノニカルURLは「検索エンジン向けの指示」で、訪問者には影響しません。恒久的な変更はリダイレクト、パラメータ違いはカノニカルURLが目安です。

**Q: 異なるドメインをカノニカルURLに指定できますか？**
A: はい、できます。ただし、検索エンジンが信頼していないドメインへのカノニカル指定は無視されることがあります。権威あるサイトへの指定に限定するほうが安全です。

## 参考資料

- [Google Search Central: Canonical URLs](https://developers.google.com/search/docs/beginner/canonicalization)
- [Moz: Canonical Tags](https://moz.com/learn/seo/canonicalization)
- [Search Engine Land: Canonical URLs Guide](https://searchengineland.com/)
- [SEOM.ru: Rel Canonical](https://seom.ru/)
- [Ahrefs: Canonical URL](https://ahrefs.com/blog/)
- [Yoast SEO: Canonical URLs](https://yoast.com/canonical-urls/)
- [Brian Dean: SEO Best Practices](https://backlinko.com/)
- [Schema.org: Structured Data](https://schema.org/)
