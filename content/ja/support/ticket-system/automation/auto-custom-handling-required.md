---
title: "カスタムフィールドの値に応じて緊急対応が必要なチケットにタグを付ける方法"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "auto-custom-handling-required"
description: "フォームから寄せられたユーザからの問い合わせで、緊急対応を求めるマークが付いていた場合に、チケットにタグを付けるルールを作成することができます。そのシナリオをご案内します。"
keywords: ["チケット", "カスタム", "必要", "問い合わせ", "フォーム"]
type: support
category: "ticket-system/automation"
e-title: "Custom - Handling - Required - Ticket"
---

フォームから寄せられたユーザからの問い合わせで、緊急対応を求めるマークが付いていた場合に、チケットにタグを付けるルールを作成することができます。そのシナリオをご案内します。

 

1. 事前にタグを作成しておきます。ここでは** 「要緊急対応」** というタグ名にします。

2. フォームの作成/編集時に新たなカスタムフィールドを追加します。

![](/liveagent/scripts/file.php?view=Y&file=94f603470775a8cd6f6d8e468b40a7a1)

3. フィールドを追加した後、”チェックボックス”を選択し、説明の文章を入力します。

![](/liveagent/scripts/file.php?view=Y&file=88086eb8f30085fe840754785ac1c32c)

4. フォームに目的のカスタムフィールドが設定されたら、フォームに追加したカスタムフィールドがアプリケーションによってチケットフィールドのリストに追加されるように、「プレビューとテスト」からテストチケットを送信する必要があります。このステップは必須です。

![](/liveagent/scripts/file.php?view=Y&file=a5e8fa213e95aa35dc9f7fa0a9c19f28)

5. ルールを作成します。

　　・条件：フォームのカスタムフィールドで「緊急」にチェックが入っていた時

　　・アクション：チケットの「要緊急対応」のタグを追加する

![](/liveagent/scripts/file.php?view=Y&file=2d4daf3f5e9514c769c10dfe5e4003f1)

ユーザが次のような内容でフォームを送信した場合：

![](/liveagent/scripts/file.php?view=Y&file=a56bc9a06991b078d45a89710724dce6)

チケット作成時にで自動的に「要緊急対応」としてマークされます。

![](/liveagent/scripts/file.php?view=Y&file=31ad77cf8240f877e127f0f4d050ef75)

チケットの詳細では次の値を参照ください。 

isUrgentのチェックボックス（isUrgentは先ほど定義したチェックボックスのシステム名）、Y（チェックボックスがチェックされた）

![](/liveagent/scripts/file.php?view=Y&file=6a31256136a50dfe2f72e9987e44e1cd)