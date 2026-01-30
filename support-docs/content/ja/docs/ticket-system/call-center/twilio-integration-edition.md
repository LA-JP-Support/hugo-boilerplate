---
title: "「Twilio」 との連携（ソフトウェア版/クラウド版）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "twilio-integration-edition"
description: "設定方法はこちらのページをご参照ください。**"
keywords: ["Twilio", "連携", "版", "LiveAgent", "ダッシュボード"]
category: "ticket-system/call-center"
---
## Twilioとの連携概要

### サービス概要
[クラウド型音声通話サービスTwilio](http://twilio.kddi-web.com/)と[ LiveAgent ](http://liveagent.jp)を連携すると、電話機能が利用できるようになります。

### 利用上の注意点
- トライアルアカウントでの試用可能
- クラウド版では別方式での連携を推奨
- IVRなどの高度な機能利用可能

### 主な機能
顧客が電話回線（固定電話や携帯電話、IP フォン）を利用した場合でも、LiveAgentにログインしたPCで受信・応対が可能です。また、LiveAgent から Twilio を経由して電話を発信することもできます。

## Twilioの設定手順

### Twilioアカウントの取得

#### トライアル申し込み
1. Twilioのウェブサイトにアクセス
2. 電話番号を入力して認証

#### 電話番号の取得
1. Twilio管理画面のダッシュボードから「電話番号」を選択
2. 最初のTwilio番号を取得

### Twilioウェブフック設定

#### リクエストURLの設定
1. 「音声通話」設定画面で、LiveAgentから提供されるリクエストURLを入力
2. 設定を保存

### APIクレデンシャル取得
1. ダッシュボードで「APIクレデンシャルを表示」
2. ACCOUNT SID、AUTH TOKEN、電話番号（発信者ID）を取得

## LiveAgentでの設定

### 基本設定
1. LiveAgentにエージェントとしてログイン
2. 「設定」→「Twilio」→「Twilioの連携」画面を開く
3. 取得したTwilioのクレデンシャル情報を入力

### チームの電話設定
1. 発信番号を追加
2. 発信時に番号を選択可能

## 注意事項

### トライアルアカウントの制限
- 発信は「検証済み電話番号」のみ可能
- それ以外の番号への発信は不可

**【重要】**
旧Twilio webhookによるLiveAgentとの連携は2023年6月30日にサポート終了。Twilio SIP Trunkへの変更を推奨。