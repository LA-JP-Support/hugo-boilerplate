---
title: "電話のレポート"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "report-phone"
description: "このレポートを閲覧するには、エージェント画面左メニューから  「レポート」＞「通話（Calls）」  を選択します。"
keywords: ["レポート", "電話", "LiveAgent", "Twilio", "エージェント"]
type: support
category: "ticket-system/reports"
e-title: "Phone - Report"
---

[Twilio 電話や音声会話の対応 ](http://support.smartweb.jp/liveagent/485766-LiveAgent-%E3%81%A7%E9%9B%BB%E8%A9%B1%E3%81%AE%E7%9D%80%E4%BF%A1%E7%99%BA%E4%BF%A1%E3%82%92%E3%81%99%E3%82%8B)に関するレポートを、直近 30日間分の表示します。 電話の待ち人数と応対エージェントの人数を比較して、適切なサポート体制を維持しているか、などの検証に活用できます。 レポートの各項目は CSV 形式で出力も可能です。

このレポートを閲覧するには、エージェント画面左メニューから  「レポート」＞「通話（Calls）」  を選択します。

## 電話・音声会話のレポート項目

- ### 通話の負荷 (Call load)

電話対応にあたる[エージェント](http://support.smartweb.jp/liveagent/542606-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88-%E3%81%A8-%E3%83%81%E3%83%BC%E3%83%A0)の人員は充分か、などを分析するために利用します。この項目では、通話数とスロット数（応答可能な窓口の数）、電話の順番待ち数を、最小値、最大値、平均値でそれぞれ比較します。

- ### 通話稼働率 (Call availability)

電話の稼働状況を時間単位で表示します。例えば、エージェントが待機状態を 1時間継続すれば、利用可能率 100% / 60分 とレポートされます。

- ### エージェントの可用性 (Agent availability)

各エージェントのログイン履歴を一覧で表示します。ログオン・ログアウト日時のほか、オンライン時間も計測しています。

- ### SLA コンプライアンス (SLA Compliance)

「[SLA ルール](http://support.smartweb.jp/liveagent/283033-SLA-%E3%81%AE%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95)」で設定した SLA を順守できているか、を時間単位の一覧で表示します。

- ### SLA ログ (SLA log)

「SLA ルール」を順守できなかった場合にログが記録されます。