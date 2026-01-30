---
title: "返信後に自動的にチケットをエージェントに割り当てる方法"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "ticket-reply-auto-agent"
description: "実現するルールの作成方法はいくつかあると思いますが例を示します。追加の条件やアクションを使用してルールをカスタマイズすることができます。"
keywords: ["エージェント", "チケット", "割り当て", "カスタマイズ", "ステータス"]
type: support
category: "ticket-system/tickets"
e-title: "Reply - Auto - Ticket - Agent"
---

実現するルールの作成方法はいくつかあると思いますが例を示します。追加の条件やアクションを使用してルールをカスタマイズすることができます。

 

![](/liveagent/scripts/file.php?view=Y&file=a32a728c2e810d9d0fbd9f70b4db42ba)

上記のルールではチケットに返信した時だけでなく、メモを追加したり「解決する」ボタンでチケットを完了するなどのアクションを行なったエージェントに自動的にチケットを割り当てます。

 

 

 

![](/liveagent/scripts/file.php?view=Y&file=4ff1e56918c09a77953c6ca0257bf7de)

 

このルールではステータスが「新規」または「オープン」のチケットに返信した場合のみ、返信したエージェントにチケットを自動で割り当てます。