---
title: "Twilioインテグレーション（クラウド版）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "twilio-edition"
description: "この記事はクラウド版をご利用のお客様向けです。ソフトウェア版をご利用のお客様はTwilioとこのように接続することはできませんので、代わりにこのガイドをご参照ください。"
keywords: ["Twilio", "版", "LiveAgent", "データセンター", "Agent"]
category: "ticket-system/call-center"
---
## Twilioインテグレーション（クラウド版）概要

この記事はクラウド版をご利用のお客様向けです。ソフトウェア版をご利用のお客様はTwilioとこのように接続することはできませんので、代わりにこの**ガイド**をご参照ください。

Twilioインテグレーションは、他のSIPプロバイダの場合と同様に、2つのパートから構成されています。最初のパートはプロバイダ側の設定です。2番目のパートであるLiveAgent管理パネルでの設定で使用する重要な情報を書き留めるように求められます。設定は次のステップで行います：

- SIPトランクを作成する
- ターミネーションURIとクレデンシャルを設定する
- オリジネーションURIを設定する
- SIPトランクに番号を追加する
- LiveAgentで番号を作成する

## Twilioセットアップの詳細手順

### 1. SIPトランクの作成

Twilioコンソールにログインし、Elastic SIP Trunksに移動することから始めましょう。コンソールの右上隅にあるバーで検索して、表示されたページで「Create new SIP Trunk」ボタンをクリックします。

[画像1: SIP Trunk作成画面]

新しいトランクに「Friendly Name」を付ける必要があります。たとえば、LiveAgentを使用してみましょう。

[画像2: Friendly Name設定画面]

SIPトランクが作成されたら、[General]タブでSECURE TRUNKINGが無効になっていることを確認します。

### 2. ターミネーションURIとクレデンシャルの設定

#### ターミネーションSIP URIの設定
トランクを作成したら、Terminationの画面に移動して固有の「Termination SIP URI」を入力します。

#### クレデンシャルリストの追加
Credentialsリストの隣にある「＋」アイコンをクリックしてトランクの新しい「CREDENTIAL LISTS」を追加します。

注意点：
- 「Termination SIP URI」は固有の文字列を使用
- ユーザー名とパスワードを安全に保管
- 特殊文字は使用不可

[画像3: クレデンシャル設定画面]

### 3. オリジネーションURIの設定

「Origination」画面の「Add new Origination URI」に進みます。

現在の日本アカウントの「Origination SIP URI」：
- **「sip:1-sip-la-sg.ladesk.com」**

#### 災害復旧URIのヒント
Disaster recovery URIを設定することで、予期せぬ障害時にコールを転送できます。

### 4. SIPトランクへの番号追加

「電話番号(Numbers)」セクションで：
- 既存のTwilio番号を追加
- 新しい番号を購入
- 国際プレフィックス付きの番号を保存

[画像4: 番号追加画面]

### 5. LiveAgentでの番号作成

LiveAgent管理パネルで：
1. 「設定」-「通話」-「番号」に移動
2. 「電話番号を追加」
3. SIP電話番号プロバイダから「Twilio」を選択

[画像5: LiveAgent番号設定画面]