---
title: "不達メール（送信エラーメール）を受信するには"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "ticket-email-send-error"
description: "問い合わせフォームなどにお客様が入力したメールアドレスが間違っていると、受け取ったチケットからの返信がお客様に届 きません。 その際に届く不達の通知メール（MAILER-DAEMON や Mail Delivery Subsystem）を受け取るには、LiveAgent側で 設定が必要です。"
keywords: ["メール", "エラー", "送信", "LiveAgent", "メールアドレス"]
type: support
category: "ticket-system/tickets"
e-title: "Email - Send - Error"
---

問い合わせフォームなどにお客様が入力したメールアドレスが間違っていると、受け取ったチケットからの返信がお客様に届 きません。 その際に届く不達の通知メール（MAILER-DAEMON や Mail Delivery Subsystem）を受け取るには、LiveAgent側で 設定が必要です。

 

 ■不達メールを受信するには

「設定」‐「電子メール」‐「メールの設定」で以下項目のチェックをONにしてください。

・「バルクメールを取得」

・「ジャンクメールを取得」

・「リターンパスが空白のメールを取得」

![](/liveagent/scripts/file.php?view=Y&file=e84dedd16caf45232135bc34e68efbaa)

 

**↓↓↓↓↓↓↓↓↓　不達のメールをチケットとして受信できるようになります 。**

  

![](/liveagent/scripts/file.php?view=Y&file=bea368d388c7e89dad121a196b1528a6)

 

さらに、「タグ」と「ルール」を作成することにより、チケットビュー（フォルダ）に仕分けることができます。

■設定 手順

1. 「設定」‐「自動化」‐「タグ」にて、[不達メール]などの名称でタグを作成します。

2. 「設定」‐「自動化」‐「ルール」にて、例2のようなルールを作成して 、チケットに自動的にタグを付けます。

3. 例3のようなチケットビュー（フォルダ）を作成して、「不達メール」のタグが付いたチケットを仕分けます。

これにより、チケットからの返信メールが不達だった場合には、 電話など別の方法で連絡をとるなどの代替策がとれます。

例2

![](/liveagent/scripts/file.php?view=Y&file=a78b5e58e35da5ce437e8afff802a234)

例 3

![](/liveagent/scripts/file.php?view=Y&file=d8d3689d64c63299ac97317691fc7bfc)