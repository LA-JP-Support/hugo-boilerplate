---
title: "モバイルアプリのチャットとインラインチャット"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "mobile-app"
description: "GETパラメータを使用すると、チャットウィンドウがブラウザで開きます （ポップアップモード）。"
keywords: ["チャット", "モバイル", "アプリ", "LiveAgent", "メールアドレス"]
category: "ticket-system/live-chat"
---
## モバイルアプリへのLiveAgentチャット統合

### GETパラメーターの使用

GETパラメータを使用すると、チャットウィンドウがブラウザで開きます（ポップアップモード）。

#### 利用可能なGETパラメーター

*cwid* - 必須 - LiveAgentのチャットウィジェットのID。

「*設定」 ->「** チャット」 -> 「チャットボタン」 -> 「チャットボタンの編集（チャットボタン名をクリック）」 -> 「チャットボタンの編集」 -> 「連携」*にあるチャットボタン統合スクリプトで見つけることができます。

ここでは、値71e8b44fのウィジェットIDの例を示します。

function(e){ LiveAgent.createButton('71e8b44f', e); }); 

利用可能なパラメーター：
- *firstName* - 顧客の名
- *lastName* - 顧客の姓
- *phone* - 顧客の電話番号
- *email* - 顧客のメールアドレス
- *note* - チャット受付時に表示されるメモ（任意のテキスト）
- *pt* - チャット受付時に表示される件名（任意のテキスト）

#### ウィジェットID使用例

ウィジェットIDのみを使用した基本的な呼び出しの例：  [https：//URL_to_LiveAgent/scripts/inline_chat.php？cwid = 71e8b44f](https://localhost/scripts/inline_chat.php?cwid=71e8b44f)

### チャットウィンドウのスタイルカスタマイズ

チャットウィンドウのスタイルは、使用しようとしているチャットウィジェットの設定で編集することができます。また、カスタムCSSコードで独自のスタイルを追加することも可能です。

## インラインチャットの実装方法

### URLとパラメーターの直接利用

同じURLとパラメータをブラウザで直接使用してチャットを開始することができます。ウェブサイトや電子メールのテンプレートにリンク/ボタンとして追加することができます。インラインチャットではチャット事前フォームは使用できません。

## ページ内チャットの設定

### iframeを使用したチャットウィンドウの埋め込み

チャットウィンドウは、<iframe>タグで別の要素に埋め込むことができます。ページが読み込まれると自動的にチャットが開始されますが、この場合はチャット事前フォームは使用できません。

#### 実装例

<iframe src="https://URL_to_LiveAgent/scripts/inline_chat.php?cwid=widgetID" style="width: 350px;height: 450px;"></iframe>

**"URL_to_LiveAgent"**をLiveAgentの正しいURL（yourdomain.liveagent.jp）に、**"widgetID"**をチャットボタンのIDに置き換えてください。