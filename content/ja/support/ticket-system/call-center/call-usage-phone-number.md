---
title: "現在利用している電話番号を使えますか？"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "call-usage-phone-number"
description: "現在お使いの電話番号をそのままLiveAgentで使用することは、その番号がSIPトランクに対応している場合のみ可能です。LiveAgentのコールセンター機能は、SIP（Session Initiation Protocol）トランクをサポートするVoIP（Voice Over Internet Pr..."
keywords: ["電話", "番号", "利用", "LiveAgent", "コールセンター"]
type: support
category: "ticket-system/call-center"
e-title: "Usage - Phone - Number"
---

現在お使いの電話番号をそのままLiveAgentで使用することは、その番号がSIPトランクに対応している場合のみ可能です。LiveAgentのコールセンター機能は、SIP（Session Initiation Protocol）トランクをサポートするVoIP（Voice Over Internet Protocol）プロバイダーからの番号を接続することで動作します。

重要なポイント：

- LiveAgentは電話番号を提供・販売していません
- SIPトランクに対応していない通常の電話番号は統合できません
- VoIPプロバイダーから番号を購入し、SIP接続情報を取得する必要があります

現在お使いの番号がVoIPプロバイダーのものでSIPトランクに対応している場合は、そのプロバイダーから以下の情報を取得してLiveAgentに設定できます：

- 電話番号
- SIPホスト（URLまたはIPアドレス）
- SIPポート
- ユーザー名
- パスワード

以下は、日本におけるTwilioによる電話番号の移行についての情報です。固定番号の利用が可能になるようです。
詳しくは以下のリンクを参照下さい。

[https://www.twilio.com/ja-jp/press/releases/0ABJ-Number-Porting](https://www.twilio.com/ja-jp/press/releases/0ABJ-Number-Porting)

### **日本における固定電話（0ABJ番号）のポートイン**

- 2025年1月31日から、**ソフトバンクとの連携により、日本全国の固定電話番号（いわゆる「0ABJ番号」＝03、06など）がTwilio上でそのまま利用可能**になりました。通信設備を追加することなく、クラウド化され、TwilioのAIエージェントや他サービスとの統合が可能です 
- また、Twilioのブログでも、既存の固定電話番号を同じ番号でクラウド移行できることが紹介されています 。