---
title: "Twilioインテグレーション（クラウド版）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "call-twilio-edition"
description: "この記事はクラウド版をご利用のお客様向けです。ソフトウェア版をご利用のお客様はTwilioとこのように接続することはできませんので、代わりにこのガイドをご参照ください。"
keywords: ["Twilio", "版", "LiveAgent", "データセンター", "Agent"]
type: support
category: "ticket-system/call-center"
e-title: "Twilio - Edition"
---

この記事はクラウド版をご利用のお客様向けです。ソフトウェア版をご利用のお客様はTwilioとこのように接続することはできませんので、代わりにこの**[ガイド](https://support.smartweb.jp/liveagent/957760-%E9%9F%B3%E5%A3%B0%E9%80%9A%E8%A9%B1%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9-Twilio-%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B%E3%81%AB%E3%81%AF)**をご参照ください。

Twilioインテグレーションは、他のSIPプロバイダの場合と同様に、2つのパートから構成されています。最初のパートはプロバイダ側の設定です。2番目のパートであるLiveAgent管理パネルでの設定で使用する重要な情報を書き留めるように求められます。設定は次のステップで行います：

	- SIPトランクを作成する

	- ターミネーションURIとクレデンシャルを設定する

	- オリジネーションURIを設定する

	- SIPトランクに番号を追加する

	- LiveAgentで番号を作成する

**１．SIPトランクを作成する**

Twilioコンソールにログインし、Elastic SIP Trunksに移動することから始めましょう。コンソールの右上隅にあるバーで検索して、表示されたページで「Create new SIP Trunk」ボタンをクリックします。

![](/liveagent/scripts/file.php?view=Y&file=d5f86495a20bcb52d81f886740cb58b6)

 

新しいトランクに「Friendly Name」を付ける必要があります。たとえば、LiveAgentを使用してみましょう。

 

![](/liveagent/scripts/file.php?view=Y&file=cb01ba86f82b28ddae7b24d86389e2ac)

SIPトランクが作成されたら、[General]タブでSECURE TRUNKINGが無効になっていることを確認します。

 

**２．ターミネーションURIとクレデンシャルを設定する**

トランクを作成したら、Terminationの画面に移動して固有の「Termination SIP URI」を入力し、Credentialsリストの隣にある「＋」アイコンをクリックしてトランクの新しい「CREDENTIAL LISTS」を追加する必要があります。「Termination SIP URI」とCREDENTIALはLiveAgent設定のパートで両方が必要になりますので、後で使用するために保存してください。

「Termination SIP URI」は、固有の文字列を何でも使用できます。例えば、あなたのLiveAgentアカウントのドメイン（ドットなしで）を使用することができます。つまり、あなたのLiveAgentアカウントドメインが「something.liveagent.jp」だとすれば、「somethingliveagentjp」を「Termination SIP URI」として追加できるということです。あとで使用するために「somethingliveagentjp.pstn.twilio.com」を保存する必要があります。もしあなたの望むURIが利用できない場合は、別のものを試してください。

 

![](/liveagent/scripts/file.php?view=Y&file=98e4c4fb5d3b0348f80a055180d72501)

 

CREDENTIALを追加するときには、もう一度「Friendly Name」、ユーザー名、およびパスワードが必要になります。パスワードジェネレータなどを使用して強力なパスワードを設定してください。あとでLiveAgentの設定のフェーズで使用できるように、ユーザー名とパスワードを保存します。

注意：  

Twilioのユーザー名とパスワードには特殊文字を使用できません（例：@＃$％）

「CREDENTIAL LISTS」と「Termination SIP URI」の設定が完了したら**「Termination」画面全体を保存**します。「SIPトランクを保存できません：無効です（Unable to save SIP trunk: is invalid）」というエラーが表示されることがあります。その場合は、次の手順3.と4.に進んでから、この手順に戻ってもう一度やり直してください。

 

![](/liveagent/scripts/file.php?view=Y&file=9d02760b2110515869518f5e9c1f614f)

 

**３．オリジネーションURIを設定する**

「Origination」画面の「Add new Origination URI」に進みます。

現在、liveagent.jpで発行した日本アカウントの「Origination SIP URI」は、**「sip:1-sip-la-sg.ladesk.com」**です。

※2020年2月にデータセンターが移行されるまでは、「sip:1-sip-la-us-tx.ladesk.com」でした。

 

![](/liveagent/scripts/file.php?view=Y&file=a54a41696ba4cb1b5f4bdf6bcacfaa65)

 

**Pro tip - **

Origination画面では、何らかの理由で元のOrigination URIに到達できない場合に呼び出されるDisaster recovery URIを指定することもできます。このような場合、このトランクに接続されていない他の番号にコールを転送できます。

これを行うには、Disaster recovery URIをhttps://twimlets.com/forward?PhoneNumber=0018008112345に設定します。ここでは、+の代わりにゼロを持つ国際プレフィックスを追加する番号を追加します。

 

**４．SIPトランクに番号を追加する**

「電話番号(Numbers)」セクションに進み、既存のTwilio番号を追加するか、LiveAgent SIPトランクに追加する新しい番号を購入します。追加した番号は、この時点からLiveAgentアカウントにルーティングされます。LiveAgentに設定する番号を書き留め、国際プレフィックスも含めて区切り記号を削除します。下図の番号のところには+81234567890のように保存する必要があります。

 

![](/liveagent/scripts/file.php?view=Y&file=a0a079ed11ead35b815ef26156b92e95)

 

**５．LiveAgentで番号を作成する**

Termination SIP URI、Termination Credentials、および番号を書き留めて、LiveAgent管理パネルにログインして、

「設定」-「通話」-「番号」-「電話番号を追加」のSIPから電話番号プロバイダの一覧に遷移し、Twilioを選択します。

 

![](/liveagent/scripts/file.php?view=Y&file=c1348b85d2786d9e8081a12ef8487735)

 

![](/liveagent/scripts/file.php?view=Y&file=cea4822c30514d2dfd846f516d98c119)

 

次の画面では、複数のフィールドを入力する必要があります。

**・名前**

　あなたが追加している番号のフレンドリーネーム

**・割当先**

　着信をルーティングするチーム

**・電話番号**

　+、国際プレフィックス、区切り記号なしの完全な番号（例／+815012345678）

**・短縮番号でダイヤル**

このプレフィックスは、ハードウェアフォンでLiveAgentを設定する場合に使用します（例：01など）。その場合は、まずハードウェアフォンでこのプレフィックスをダイヤルしてから、実際に呼び出す番号をダイヤルする必要があります。また、LiveAgentパネルからコールを開始して、ハードウェアフォンに応答して実際の通話を開始することもできます。

**・ホスト**

ここでは前の手順で設定した「Termination SIP URI」（somethingliveagentjp.pstn.twilio.com）を記述する必要があります。

※Twilioの仕様としてリージョン（jp1）を指定していないと非通知で発信されることがあります。TERMINATION SIP URIにjp1が指定されていれば、必ず日本ルートを経由します。そのため、非通知となる場合はリージョンを指定して（somethingliveagentjp.pstn.jp1.twilio.com）と入力します。

**・ユーザ名**

Termination画面でクレデンシャルを作成するときに追加したユーザ名 - somethingliveagentjp

**・パスワード**

Termination画面でクレデンシャルを作成するときに追加したパスワード

 

![](/liveagent/scripts/file.php?view=Y&file=7ab8502b0a7f8ff393151090c32a1f3c)

 

番号を保存すると、発信通話と着信通話をテストする準備が整います。発信コールの場合は、Twilioコンソールの「Voice Geographic Permissions」セクションをチェックして、他の国への発信を許可する必要があります。

あなたの番号が追加されたら、挨拶メッセージ、オフラインメッセージ、順番待ちの案内メッセージ、そしてIVRオプションを設定することができます。これらのオプションについては、[**IVRガイド**](https://support.smartweb.jp/liveagent/975126-IVR)を参照してください。