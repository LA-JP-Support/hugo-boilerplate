---
title: "カスタマーポータルの記事一覧のリード文を非表示または短縮したい"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "customer-portal-list-display"
description: "「カテゴリ」内の記事一覧を表示するときに、記事タイトルの下に表示されるリード文（記事本文の抜粋）を、タイトルだけの表示にしたい（リード文を完全に非表示にしたい）、または短縮して表示したい場合には「カスタムCSS」を使って調整可能です。以下に3つの例をご案内します。"
keywords: ["カスタマーポータル", "ポータル", "表示", "カスタマイズ", "カスタム"]
category: "ticket-system/customer-portal"
---
## カスタマーポータルのリード文表示カスタマイズ

カスタマーポータルの「Montana」テーマにおける記事一覧のリード文表示をカスタマイズする方法を説明します。

### カスタムCSS設定方法

カスタムCSSは以下の手順で追加できます：
- カスタマーポータル
- 「設定」
- 「デザインをカスタマイズ」
- 「デザイン」
- 「カスタムCSS」

### リード文表示カスタマイズの3つの方法

#### 1. リード文を完全に非表示

```css
/*カテゴリーページのリード文を非表示にする*/
.article-preview {
    display: none;
}
```

#### 2. リード文を1行に省略

```css
/*カテゴリーページのリード文を1行にする（…あり）*/
.article-preview {
    word-wrap: break-word;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
}
```

#### 3. リード文を2行に制限

```css
/*カテゴリーページのリード文を2行にする（…なし）*/
.article-preview {
    word-wrap: break-word;
    overflow: hidden;
    height: 3em;
}
```

### 注意事項

- このCSSは「Montana」テーマでのみ有効
- 他のテーマに切り替える際は、CSSコードを再適用する必要がある