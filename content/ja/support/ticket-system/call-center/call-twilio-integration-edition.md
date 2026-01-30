---
title: "「Twilio」 との連携（ソフトウェア版/クラウド版）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "call-twilio-integration-edition"
description: "設定方法はこちらのページをご参照ください。**"
keywords: ["Twilio", "連携", "版", "LiveAgent", "ダッシュボード"]
type: support
category: "ticket-system/call-center"
e-title: "Twilio - Integration - Edition"
---

**【ご注意】**

**下記の旧Twilio webhookによるLiveAgentとの連携は2023年6月30日にサポートを終了いたします。****Twilio SIP Trunkに変更していただくようお願いいたします。

設定方法は[こちら](https://support.smartweb.jp/liveagent/067219-Twilio%E3%82%A4%E3%83%B3%E3%83%86%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E7%89%88)[のページ](https://support.smartweb.jp/liveagent/067219-Twilio%E3%82%A4%E3%83%B3%E3%83%86%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E7%89%88)をご参照ください。**

 

[クラウド型音声通話サービスTwilio](http://twilio.kddi-web.com/)と[ LiveAgent ](http://liveagent.jp)を連携すると、電話機能が利用できるようになります。

トライアルアカウントでのご試用も可能です。

※クラウド版では[**別方式での連携**](https://support.smartweb.jp/liveagent/067219-Twilio%E3%82%A4%E3%83%B3%E3%83%86%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E7%89%88)をお勧めします。IVRなどの高度な機能が利用できるほか、Twilio以外の電話プロバイダとの連携も可能です。

 

顧客が電話回線（固定電話や携帯電話、IP フォン）を利用した場合でも、LiveAgentにログインしたPCで受信・応対が可能です。また、LiveAgent から Twilio を経由して電話を発信することもできます。

※ブラウザ経由の音声会話を利用するには、[PC 同士の音声会話](http://support.smartweb.jp/liveagent/417447-PC-%E5%90%8C%E5%A3%AB%E3%81%AE%E9%9F%B3%E5%A3%B0%E4%BC%9A%E8%A9%B1%E3%82%92%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E3%81%AB%E3%81%AF)を設定してください。

 

**LiveAgent へ Twilio を設定する**

**■Twilio側の設定**

LiveAgent側から「リクエストURL」を取得して設定。

**■LiveAgent側の設定**

Twilioで電話番号を取得し、「ACCOUNT SID」「AUTH TOKEN」「発信者ID（Twilioで取得した電話番号）」を設定。

連携の設定はそれだけです。それでは以下で設定の手順を詳しくご案内しましょう。

 

**まず、LiveAgentにエージェントログインして　「****設定」‐「Twilio」‐「Twilioの連携」の画面を開いておきます。**

![](/liveagent/scripts/file.php?view=Y&file=ddb984c552bd290ee40a0bebea588b8d)

 

**Twilioで電話番号を取得します。**

**1.　ブラウザで別途TwilioのWebサイト（[https://jp.twilio.com/try-twilio/kddi-web](https://jp.twilio.com/try-twilio/kddi-web)）を開き、トライアル申し込み**

**2.　電話番号を入力して認証**

![](/liveagent/scripts/file.php?view=Y&file=db37509d0e9a64e40d3fad436abc5486)

 

**3.　Twilio管理画面のダッシュボード内、「電話番号」をクリック**

![](/liveagent/scripts/file.php?view=Y&file=e6b00421addca3b8341d5bcef6edace8)

 

**4.　「始めましょう」～「最初のTwilio番号を取得」～番号を決定**

![](/liveagent/scripts/file.php?view=Y&file=50bd629d37dc470644d812b3409475e5)

![](/liveagent/scripts/file.php?view=Y&file=7e1a6bcb5b6f8f49d531bf8eaa7b8615)

 

**5.　「電話番号」～「アクティブな電話番号」に表示された番号をクリック**

![](/liveagent/scripts/file.php?view=Y&file=543b3be3ebe03b7742b03ad91b147371)

 

**6.　設定画面の「音声通話」の「A CALL COMES IN」と「CALL STATUS CHANGES」のところにLiveAgentの「Twilioの連携」ページに表示されている「リクエストURL」を転記して「保存」**

![](/liveagent/scripts/file.php?view=Y&file=aca82fc2874e20bdea111c8c6e511a5e)

 

**これでTwilio側の設定は完了です。**

 

**7.　ダッシュボードに戻って「APIクレデンシャルを表示する」をクリック**

![](/liveagent/scripts/file.php?view=Y&file=5aa94dc8075369edfa4a7d539829d5fd)

 

**8.　表示された 「ACCOUNT SID」  「AUTH TOKEN」  「電話番号（発信者ID）」 の情報を取得**

![](/liveagent/scripts/file.php?view=Y&file=f2a4074db2c27db18c6f88ffba4a3573)

 

**9.　LiveAgentの「Twilioの連携」 の画面で、取得した上記3点の情報を転記して「保存」**

 

 

![](/liveagent/scripts/file.php?view=Y&file=ddb4d6fb633a4c6e8c6c652b805579b6)

 

**10.　最後に「チームの電話」に電話番号を追加します。発信側の番号はTwilio側で「検証済み電話番号」リストにある番号が追加可能です。**

 

![](/liveagent/scripts/file.php?view=Y&file=1306ddbf0d48fe128d0857dbbfe905b5)

 

 

![](/liveagent/scripts/file.php?view=Y&file=054d952c50f544a236a06a0a5ffadd20)

 

 

![](/liveagent/scripts/file.php?view=Y&file=7c114fd320d6675dfc927c7994a3332a)

 

**「チームの電話」で発信番号を追加すると、発信する際に番号を選択できます。

※受信電話番号（Twilio番号）は発信番号としても使用できます。**

**以上でLiveAgent側の設定も完了です。**

 

**＜ご注意点＞

Twilioのトライアルアカウントでの発信は、「検証済み電話番号」に対してのみ可能です。

それ以外の番号へ発信することはできません。**