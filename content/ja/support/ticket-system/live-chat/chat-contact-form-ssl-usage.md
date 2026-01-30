---
title: "チャットや問合せフォームで SSL 通信を利用できますか"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "chat-contact-form-ssl-usage"
description: "LiveAgent の標準ウィジェット （ライブチャットや問合せフォームのボタン、ウィンドウなど） から送信される入力データは、HTTP プロトコル（ \"http://\" から始まるウェブサイトの URL）で通信した場合、暗号化されずにデータの送受信を行います。"
keywords: ["問合せフォーム", "チャット", "フォーム", "LiveAgent", "ライブチャット"]
type: support
category: "ticket-system/live-chat"
e-title: "Chat - Contact Form - Ssl - Usage"
---

LiveAgent の標準ウィジェット （[ライブチャット](http://support.smartweb.jp/liveagent/763704-LiveAgent-%E3%81%AE%E3%83%A9%E3%82%A4%E3%83%96%E3%83%81%E3%83%A3%E3%83%83%E3%83%88)や[問合せフォーム](http://support.smartweb.jp/liveagent/141694-%E5%95%8F%E5%90%88%E3%81%9B%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%81%AE%E6%A6%82%E8%A6%81%E3%81%A8%E5%88%A9%E7%94%A8%E6%89%8B%E9%A0%86)のボタン、ウィンドウなど） から送信される入力データは、HTTP プロトコル（ "http://" から始まるウェブサイトの URL）で通信した場合、暗号化されずにデータの送受信を行います。

通信データの暗号化をするには、「ウィジェットのスクリプトを SSL 対応にする」または「ウィジェットを設置するウェブページを SSL 対応にする」のどちらかを実施する必要があります。

- ### ウェブページに埋め込むウィジェットのスクリプトを SSL に変更する

埋め込みスクリプトの以下の部分をSSLに対応したスクリプトに変更します。

"URL_TO_LiveAgent" 以降の部分は設定されているURLそのままです

- liveagent.jp 以外の自社サーバやドメイン設定をしている場合には、そのサーバがSSLを利用できる環境になっていなければなりません。

- この方法の場合、ボタンでポップアップした問合せフォームやチャットのフレームのウインドウ部分のみが SSL 通信となるため、ブラウザの URL には SSL 通信の表示が出ません。確認するにはフレーム部分の情報を表示する必要があります。

`//URL_TO_LiveAgent/scripts/track.js

//URL_TO_LiveAgent/scripts/pix.gif`

↓　先頭に "https:" を追加する

`https://URL_TO_LiveAgent/scripts/track.js

https://URL_TO_LiveAgent/scripts/pix.gif`

- ### ウィジェットを配置するページを SSL のページにする

ウィジェットを配置するページを全て SSL のウェブページに変更すると、ウィジェットを用いた通信は自動的に暗号化されます。

- ご利用のウェブサイトに SSL を設定されていない場合にはご利用いただけません。

- この方法の場合には、ブラウザの URL には SSL 通信の表示が出ます。