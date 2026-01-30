---
title: "Gmail でシステムからのメールを受信できません"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-gmail-system-email"
description: "エージェントの新規作成やパスワードのリマインダーなど、LiveAgent のシステムから送信されるメールを Gmail で受信できないことがあります。この場合は、以下の手順に従って「システムメール」を任意のメールサーバより配信するよう設定変更をお願いいたします。"
keywords: ["Gmail", "システム", "メール", "LiveAgent", "メールアドレス"]
type: support
category: "settings"
e-title: "Gmail - System - Email"
---

エージェントの新規作成やパスワードのリマインダーなど、LiveAgent のシステムから送信されるメールを Gmail で受信できないことがあります。この場合は、以下の手順に従って「システムメール」を任意のメールサーバより配信するよう設定変更をお願いいたします。

 

### LiveAgent システムメール配信元の変更手順

 

	- 
	所有者または管理者アカウントでログイン後、エージェント画面左メニューより「設定」＞「システム」＞「システムメールアカウント」を選択します。

	
![](/liveagent/scripts/file.php?view=Y&file=9b0d34ab2aa2e24d1bb905cbfb2081d7)

	 

	

	- 
	LiveAgent から送信されるシステムメールは、デフォルトでは「内部のメール機能を使用する」が設定されています。こちらのラジオボタンを「SMTP サーバを使用」へ切り替えます。

	
![](/liveagent/scripts/file.php?view=Y&file=03bab0d0f3535092718dc3674455e80d)

	 

	

	- 
	ラジオボタンを切り替えると、システム送信メールの設定画面が表示されます。利用したいメールアドレスと SMTP サーバの情報を入力してください。

	
![](/liveagent/scripts/file.php?view=Y&file=bccd8951b7412ae6bd82e0f0621190ec)

	 

	

	- 
	上記設定後、「設定のテスト」をクリックします。「OK」と表示されたら「保存」してください。設定完了です。