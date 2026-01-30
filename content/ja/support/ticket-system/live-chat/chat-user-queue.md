---
title: "ユーザのチャット順番待ち"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "chat-user-queue"
description: "オンラインのエージェントがすべて対応中で空きスロットがない場合、順番待ちのメッセージが表示されます。"
keywords: ["順番待ち", "チャット", "ユーザ", "LiveAgent", "エージェント"]
type: support
category: "ticket-system/live-chat"
e-title: "User - Chat - Queue"
---

オンラインのエージェントがすべて対応中で空きスロットがない場合、順番待ちのメッセージが表示されます。

空きが出たタイミングで自動的にエージェントに着信します。

 

**▼ユーザ側チャットウインドウの待機画面**

![](/liveagent/scripts/file.php?view=Y&file=7dae6a0b712f06a5e1caa85c7139bd77)

※上記例で は待機順位が１番目であることを示しています。

※ユーザは 待機中に質問内容を入力して送信しておくことができます。（エージェントが応答したと同時に質問内容が届きます）

※ユーザは待つのを止めてオフラインメッセージを残すこともできます。（要「チャットウインドウ」 の設定） 

 

**▼「中止して、メッセージを残す」をクリックするとオフラインメッセージ画面に切り替わります**

![](/liveagent/scripts/file.php?view=Y&file=d2109b51ed26c1171c4823e6c1758f84)

※オフラインメッセージが送信されるとLiveAgentで新規チケットが発行されます。

 

**▼オフラインメッセージを残すことを有効にする設定 **

「設定」‐「チャット」‐「チャットボタン」‐（ボタン名をクリックして編集画面を開き）「チャットウインドウ」

 ![](/liveagent/scripts/file.php?view=Y&file=2d47307eedce7d8b2149aef7f884f4de)

 

**▼チャット待機中のユーザの状況はエージェントパネルで確認できます**

「チャット」‐「チャットの概要」

![](/liveagent/scripts/file.php?view=Y&file=15249517a5242346b2248a7acabcc4ce)