---
title: "スマートチケットのレポート"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "report-ticket"
description: "LiveAgentから発行されたチケットに関するレポートを、直近 30日間分表示します。チケットの処理が適切な経過時間内（SLA）に行われたか、応対エージェント数は適切であるか、などの確認に活用できます。レポートの各項目は CSV 形式で出力も可能です。"
keywords: ["スマートチケット", "チケット", "レポート", "LiveAgent", "ライブチャット"]
type: support
category: "ticket-system/reports"
e-title: "Ticket - Report"
---

LiveAgentから発行された[チケット](http://support.smartweb.jp/liveagent/517810-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E3%81%A8%E3%81%AF)に関するレポートを、直近 30日間分表示します。チケットの処理が適切な経過時間内（SLA）に行われたか、応対エージェント数は適切であるか、などの確認に活用できます。レポートの各項目は CSV 形式で出力も可能です。

このレポートを閲覧するには、エージェント画面左メニューから 「レポート」＞「チケット」 を選択します。

![](/liveagent/scripts/file.php?view=Y&file=cc8a522a2a010aed17c8ab9492c4f80c)

## チケットのレポート項目

- ### チケットの負荷 (Ticket load)

チケット処理にあたるエージェントの人数は充分なのか、または各人の対応スキルに問題があるのか、などを分析するために利用します。この項目では、対応可能なエージェント数、チケット発行数とライブチャットの順番待ち数を、最小値、最大値、平均値でそれぞれ比較します。

- ### エージェントの可用性 (Agent availability)

各エージェントのログイン履歴を一覧で表示します。ログオン・ログアウト日時のほか、オンライン時間も計測しています。

- ### SLA コンプライアンス (SLA Compliance)

「[SLA ルール](http://support.smartweb.jp/liveagent/283033-SLA-%E3%81%AE%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95)」で設定した SLA を順守できているか、を時間単位の一覧で表示します。

- ### SLA ログ (SLA log)

「SLA ルール」を順守できなかった場合にログが記録されます。