---
title: "Google AppsメールアカウントへのPOP3アクセス"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "google-email-account"
description: "Google AppsがホストするメールアカウントをLiveAgentと連携するには、次の手順に従ってください。"
keywords: ["Google", "アカウント", "アクセス", "LiveAgent", "Agent"]
category: "ticket-system/tickets"
---
## Google AppsメールアカウントへのPOP3アクセス設定ガイド

### 概要
Google AppsがホストするメールアカウントをLiveAgentと連携するには、次の手順に従ってください。

### 手順1: Google Appsアカウントでアクセス許可を設定する
Google Appsアカウントにログインし、メールアカウントへのアクセスの許可を行います。

詳細な手順は以下をご参照ください：
https://support.google.com/a/answer/105694?hl=ja

### 手順2: Gmail アカウントでPOP3アクセスを有効化
1. LiveAgentに接続したいGmailのメールアカウントにログインします。
2. 「設定」＞ 「メール転送とPOP / IMAP」から設定を行います。

#### 注意事項
Googleがこれらの設定を複製するまで約30分お待ちください。

### 手順3: LiveAgentでメールアカウントを追加
1. LiveAgent管理者アカウントにログインします。
2. 「設定」＞「電子メール」＞「メールアカウント」＞「メールアカウントの追加」を選択します。

### 統合後の動作
今後Google Appsのメールアカウントに届くすべての受信メールは、チケットに変換されてLiveAgentに格納されます。