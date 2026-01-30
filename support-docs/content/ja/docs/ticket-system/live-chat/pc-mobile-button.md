---
title: "PC/モバイルサイトでのチャットボタンの出し分けについて"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "pc-mobile-button"
description: "PCサイト向け/モバイルサイト向けでチャットボタンの表示を切り替えることができます。"
keywords: ["チャット", "モバイル", "について", "LiveAgent", "ライブチャット"]
category: "ticket-system/live-chat"
---
## チャットボタンの表示設定概要

チャットボタンは、PCサイトとモバイルサイトで異なる設定が可能です。デバイスに最適化された表示を実現するための方法を説明します。

## LiveAgentのチャットボタン表示設定

### モバイル環境での外観設定

「設定」‐「チャット」‐「チャットボタン」‐（該当ボタン名をクリックして）「オンラインボタン」ページで、モバイル環境での表示をカスタマイズできます。

#### 表示サイズの調整例
- 「変更なし」
- 「スケールダウン」
- テキスト部分のみ表示

#### デザインのカスタマイズ
- オリジナル画像の使用
- サイトデザインに合わせた調整可能
  - デザイン
  - 表示方法
  - 位置
  - サイズ

## PC/モバイルサイトでのボタン出し分け方法

### 実装手順

1. LiveAgentでボタン設定
   - PC用チャットボタン
   - スマホ用チャットボタン

2. Webサイトへのソースコード貼り付け

### CSSによる表示制御

#### スマートフォンサイズ時の設定
- PC用チャットボタンを非表示
- モバイル用チャットボタンを表示

#### タブレット/PC サイズ時の設定
- PC用チャットボタンを表示
- モバイル用チャットボタンを非表示

### 実装コード例

#### HTMLでのクラス指定
```html
<div class="livechat_pc">
  <!-- PC用チャットボタンソースコード -->
</div>

<div class="livechat_mobile">
  <!-- モバイル用チャットボタンソースコード -->
</div>
```

#### CSSでの表示制御
```css
@media only screen and (max-width: 679px) {
  .livechat_pc { display: none; }
  .livechat_mobile { display: block; }
}

@media only screen and (min-width: 679px) {
  .livechat_pc { display: block; }
  .livechat_mobile { display: none; }
}
```