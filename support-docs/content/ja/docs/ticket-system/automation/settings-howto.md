---
title: "自動BCCの設定方法"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-howto"
description: "エージェントがLiveAgentからユーザに送信するメールにBCCのアドレスを追加するための直接的なオプションはありませんが、「ルール」により同等の動作を設定することができます。チケットIDとメール本文は変数を使って引用します。"
keywords: ["設定", "自動", "方法", "LiveAgent", "エージェント"]
category: "ticket-system/automation"
---
## 概要
LiveAgentでメールにBCCアドレスを追加する方法について説明します。

### BCCの追加制限
エージェントがLiveAgentからユーザに送信するメールにBCCのアドレスを追加するための直接的なオプションはありませんが、「ルール」により同等の動作を設定することができます。チケットIDとメール本文は変数を使って引用します。

## ルールの設定方法

### ルール作成手順
***「設定」＞「自動化」＞「ルール」***  で、下記のスクリーンショットのようにルールを作成します。

 

![](/liveagent/scripts/file.php?view=Y&file=6509a69bcb3aac53c691f1343ddd31b0)

## 注意点

### アクション名の表記
※アクションの「send mail」は、「右の宛先へメールを送る」という翻訳が適用されているケースもあります。