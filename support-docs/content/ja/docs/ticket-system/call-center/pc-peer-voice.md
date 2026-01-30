---
title: "PC 同士の音声会話を利用するには"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "pc-peer-voice"
description: "LiveAgent の音声会話を利用すると、 顧客はウェブサイト上からエージェントへ電話発信することが可能になります。音声会話を有効とするには、呼び出し窓口となるボタンを任意のウェブページに設置します。"
keywords: ["PC", "音声", "利用", "LiveAgent", "Twilio"]
category: "ticket-system/call-center"
---
## LiveAgent 音声会話の概要

LiveAgent の音声会話を利用すると、顧客はウェブサイト上からエージェントへ電話発信することが可能になります。音声会話を有効とするには、呼び出し窓口となるボタンを任意のウェブページに設置します。

※音声会話の「呼び出しボタン」の利用は、twilio との連携設定があらかじめ必要となります。

## 音声会話の設定手順

### Twilioボタンの作成

- エージェント画面より 「設定」＞「Twilio」＞「Twilioボタン」 を選択します。

![](/liveagent/scripts/file.php?view=Y&file=297d7bda43632dc1be7dfba92f3eef50)

### ボタンの詳細設定

- 詳細画面で新規のボタン名、部署とデザインを設定します。

#### ボタンのデザイン

![](/liveagent/scripts/file.php?view=Y&file=1b2901236ca5889d6055c572f1efe0d2)

#### 通話ウィンドウのカスタマイズ

![](/liveagent/scripts/file.php?view=Y&file=caf58a10b49bbb5a01dba170b145012a)

### 呼び出しボタンの設定

![](/liveagent/scripts/file.php?view=Y&file=409520f254ee3849768bfd53269ae01f)

## ボタンの実装と管理

- 入力が完了したら変更を保存し、作成した呼び出しボタンの HTML コードをコピーします。
- このコードを、ボタンを表示させたいページに追加することで音声会話が利用できるようになります。
- ボタン設置後にデザイン等を変更する場合は、LiveAgent 内の設定を変更するのみで、HTML コードの差し替えは不要です。

![](/liveagent/scripts/file.php?view=Y&file=2a625615c387880ef5bfde60a3b3e869)