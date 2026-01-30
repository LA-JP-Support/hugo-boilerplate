---
title: "チャットや問合せフォームで SSL 通信を利用できますか"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "contact-form-ssl-usage"
description: "LiveAgent の標準ウィジェット （ライブチャットや問合せフォームのボタン、ウィンドウなど） から送信される入力データは、HTTP プロトコル（ \"http://\" から始まるウェブサイトの URL）で通信した場合、暗号化されずにデータの送受信を行います。"
keywords: ["問合せフォーム", "チャット", "フォーム", "LiveAgent", "ライブチャット"]
category: "ticket-system/live-chat"
---
## SSL 通信とLiveAgentウィジェット

### SSL通信の必要性
LiveAgent の標準ウィジェット （ライブチャットや問合せフォームのボタン、ウィンドウなど） から送信される入力データは、HTTP プロトコル（ "http://" から始まるウェブサイトの URL）で通信した場合、暗号化されずにデータの送受信を行います。

通信データの暗号化をするには、「ウィジェットのスクリプトを SSL 対応にする」または「ウィジェットを設置するウェブページを SSL 対応にする」のどちらかを実施する必要があります。

## SSL対応の方法

### ウィジェットスクリプトをSSLに変更する
埋め込みスクリプトの以下の部分をSSLに対応したスクリプトに変更します。

"URL_TO_LiveAgent" 以降の部分は設定されているURLそのままです

- liveagent.jp 以外の自社サーバやドメイン設定をしている場合には、そのサーバがSSLを利用できる環境になっていなければなりません。

- この方法の場合、ボタンでポップアップした問合せフォームやチャットのフレームのウインドウ部分のみが SSL 通信となるため、ブラウザの URL には SSL 通信の表示が出ません。確認するにはフレーム部分の情報を表示する必要があります。

`//URL_TO_LiveAgent/scripts/track.js

//URL_TO_LiveAgent/scripts/pix.gif`

↓　先頭に "https:" を追加する

`https://URL_TO_LiveAgent/scripts/track.js

https://URL_TO_LiveAgent/scripts/pix.gif`

### ウェブページ全体をSSL対応にする
ウィジェットを配置するページを全て SSL のウェブページに変更すると、ウィジェットを用いた通信は自動的に暗号化されます。

- ご利用のウェブサイトに SSL を設定されていない場合にはご利用いただけません。

- この方法の場合には、ブラウザの URL には SSL 通信の表示が出ます。