---
title: "How to export data from LiveAgent"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "ticket-liveagent-2"
description: "エージェントパネルの一部のセクションで利用可能なCSVエクスポートオプションの他に、LiveAgentからデータをエクスポートする方法が2つあります。"
keywords: ["LiveAgent", "Agent", "ライブチャット", "tickets", "Google"]
type: support
category: "ticket-system/tickets"
e-title: "Liveagent"
---

エージェントパネルの一部のセクションで利用可能なCSVエクスポートオプションの他に、LiveAgentからデータをエクスポートする方法が2つあります。

	- APIを使用してチケットをエクスポート

	- DBダンプを作成

**APIを使用してチケットをエクスポートする**

APIを使用してデータをエクスポートすることもできます。例えば、このAPI v3コールでは、1ページにつき10件のチケットが取得でき、エクスポートするチケットを定義するためにチケットが作成された時間範囲を設定することができます。特定の日付のページで10件未満の結果が表示されたら、次の日に進むことができます。

https://youraccount.ladesk.com/api/v3/tickets?_perPage=10&_page=1&_filters=[["date_created","D>","2017-06-11 00:00:00"],["date_created","D<","2017-06-11 23:59:59"]]&_sortField=date_created

API v1のリファレンスは[こちら](https://support.liveagent.com/840770-Complete-API-reference)、API v3のリファレンスは[こちら](https://support.liveagent.com/567924-Documentation--examples)をご覧ください。（英文になります）

**DBダンプを作成する**

すべてのデータは複数の場所に保存されており、主にSQLデータベースを主に使用して、AWS S3ストレージにも保存されています。お客様の代わりにDBダンプを作成することも可能ですが、AWS S3からのデータはファイルおよびフォルダ構造としてのみ共有できます。フォルダ構造およびファイルの内容については、次の記事の最後に説明されています。  [Amazon S3 File Archive plugin](https://support.liveagent.com/214341-Amazon-S3-File-Archive-plugin)　(英文)

APIを使用してすべてのチケットをエクスポートするよりも、DBダンプを希望される場合は、弊社がファイルをアップロードできるストレージへの安全なアクセス権をご提供いただく必要があります。例えば、弊社のプライベートキーで認証されたSSH/SCPアクセス（弊社管理者より、転送専用の公開キーを提供いたします）などです。この場合、接続先のホストを認証するためのホスト公開キーも必要となります。

あるいは、GoogleドライブのダウンロードリンクからDBダンプを共有することもできます。これを行うには、ファイルへのアクセス権限を持つGoogleアカウントが必要です。この場合、パスワードの交換は必要ありません。

ダンプファイルにはデータベースの生データが含まれていますのでご注意ください。このため、API での作業をお勧めします。すべてのアカウントに適用される API のレート制限は、[こちら](https://support.liveagent.com/217359-Request-rate-limits)でご確認いただけます。

パスワードをメールで送信しないでください。その代わり、https://liveagent.comのライブチャットをご利用ください。XXX-XXX-XXX（お客様のチケットID）のチケットに関連する内容であることをお伝えください。

Updated: Jul 22, 2022