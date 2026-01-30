---
title: "カスタマーポータルの記事一覧のリード文を非表示または短縮したい"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "portal-customer-portal-list-display"
description: "「カテゴリ」内の記事一覧を表示するときに、記事タイトルの下に表示されるリード文（記事本文の抜粋）を、タイトルだけの表示にしたい（リード文を完全に非表示にしたい）、または短縮して表示したい場合には「カスタムCSS」を使って調整可能です。以下に3つの例をご案内します。"
keywords: ["カスタマーポータル", "ポータル", "表示", "カスタマイズ", "カスタム"]
type: support
category: "ticket-system/customer-portal"
e-title: "Customer Portal - List - Display"
---

[カスタマーポータル](https://www.liveagent.jp/function/supportportal/customer-portal/)の「テーマ」に「Montana」を選択した場合のtipsです。

「カテゴリ」内の記事一覧を表示するときに、記事タイトルの下に表示されるリード文（記事本文の抜粋）を、タイトルだけの表示にしたい（リード文を完全に非表示にしたい）、または短縮して表示したい場合には「カスタムCSS」を使って調整可能です。以下に3つの例をご案内します。

 

**※カスタムCSS

「カスタマーポータル」‐「設定」‐「デザインをカスタマイズ」‐「デザイン」‐「カスタムCSS」**

 

![](/liveagent/scripts/file.php?view=Y&file=8fa8f4817643e9bc8a0309779b7285ae)

 

それぞれ以下のCSSを追記します。

**1) リード文をすべて非表示（記事タイトルのみ表示）**

/*カテゴリーページのリード文を非表示にする*/

.article-preview {

display: none;

}

**2) リード文を1行にして末尾に…あり**

/*カテゴリーページのリード文を1行にする（…あり）*/

.article-preview {

word-wrap: break-word;

text-overflow: ellipsis;

white-space: nowrap;

overflow: hidden;

}

**3) リード文を2行にして末尾に…なし**

/*カテゴリーページのリード文を2行にする（…なし）*/

.article-preview {

word-wrap: break-word;

overflow: hidden;

height: 3em;

}

 

 

**デフォルト**

![](/liveagent/scripts/file.php?view=Y&file=365386b7c35a2a5f91d28dbc67e1e68d)

 

**タイトルのみ表示**

![](/liveagent/scripts/file.php?view=Y&file=ddf5ed35490b44036fff413e292bf134)

 

**リード文を一行表示**

![](/liveagent/scripts/file.php?view=Y&file=53eb0e1ac3df372c248634da0f1efdd1)

 

**リード文を二行表示**

![](/liveagent/scripts/file.php?view=Y&file=a9f66378a8d81c903baecc7ba3bd1255)

 

**＜ご注意＞**

このCSSは「テーマ」が「Montana」の場合のみ有効です。

「テーマ」ごとに独自のカスタムCSSがあるため、別の「テーマ」に切り替えるときはコードを再適用する必要があります。