---
title: "チャットの動作テストを簡単に行う方法が知りたい"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "behavior-test-howto"
description: "LiveAgentの標準機能の一部であるカスタマーポータルページにチャットボタンを貼り付けて動作テストすることができます。"
keywords: ["チャット", "テスト", "方法", "カスタマーポータル", "LiveAgent"]
category: "ticket-system/live-chat"
---
## チャットボタンのカスタマーポータルへの設置方法

### チャットボタンの作成手順

LiveAgentの標準機能の一部であるカスタマーポータルページにチャットボタンを貼り付けて動作テストすることができます。

まずチャットボタンを作成し、「連携」のコードをコピーします。

### コードの設置場所

コピーしたコードを以下の場所にペーストして「保存」すれば準備は完了です。

**⇒「カスタマーポータル」‐「設定」‐「デザインをカスタマイズ」‐「トラッキングコード」のBefore </BODY>**

![](/liveagent/scripts/file.php?view=Y&file=b9a8d716fafedeadbea57bd2766635cb)

![](/liveagent/scripts/file.php?view=Y&file=29d1a49dd1f6266252a89259098d7dac)

![](/liveagent/scripts/file.php?view=Y&file=ceeb6f39b4145de6e832e819608fcbee)

### アクセス用URL

カスタマーポータルのURL　：　https://**あなたが設定したドメイン**.liveagent.jp/