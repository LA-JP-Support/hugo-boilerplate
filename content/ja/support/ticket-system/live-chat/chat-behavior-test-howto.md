---
title: "チャットの動作テストを簡単に行う方法が知りたい"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "chat-behavior-test-howto"
description: "LiveAgentの標準機能の一部であるカスタマーポータルページにチャットボタンを貼り付けて動作テストすることができます。"
keywords: ["チャット", "テスト", "方法", "カスタマーポータル", "LiveAgent"]
type: support
category: "ticket-system/live-chat"
e-title: "Chat - Behavior - Test - Howto"
---

LiveAgentの標準機能の一部であるカスタマーポータルページにチャットボタンを貼り付けて動作テストすることができます。

まず[チャットボタンを作成](https://support.smartweb.jp/liveagent/717046-%E3%83%81%E3%83%A3%E3%83%83%E3%83%88%E3%83%9C%E3%82%BF%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95)し、「連携」のコードをコピーします。

コピーしたコードを以下の場所にペーストして「保存」すれば準備は完了です。

**⇒「カスタマーポータル」‐「設定」‐「デザインをカスタマイズ」‐「トラッキングコード」のBefore </BODY>**

 

![](/liveagent/scripts/file.php?view=Y&file=b9a8d716fafedeadbea57bd2766635cb)

 

 

![](/liveagent/scripts/file.php?view=Y&file=29d1a49dd1f6266252a89259098d7dac)

 

 

![](/liveagent/scripts/file.php?view=Y&file=ceeb6f39b4145de6e832e819608fcbee)

 

カスタマーポータルのURL　：　https://**あなたが設定したドメイン**.liveagent.jp/