---
title: "LiveAgentをGmail/G Suiteに接続する"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "ticket-liveagent-gmail-connect"
description: "クラウド版のLiveAgentアカウントは、GoogleのOAuth認証を使用してGmailアカウントに接続します。ポップアップウィンドウでこの接続を認証するとGmailメールボックスが接続され、これ以上設定する必要はありません。"
keywords: ["LiveAgent", "Agent", "Gmail", "メールアドレス", "Google"]
type: support
category: "ticket-system/tickets"
e-title: "Liveagent - Gmail - Connect"
---

**■GmailアカウントとLiveAgent（クラウド版）を接続する**

クラウド版のLiveAgentアカウントは、GoogleのOAuth認証を使用してGmailアカウントに接続します。ポップアップウィンドウでこの接続を認証するとGmailメールボックスが接続され、これ以上設定する必要はありません。

 

LiveAgentにログインし、メールアカウントの設定画面を開きます。「**設定」＞ 「電子メール」＞「メールアカウント」**

**「メールアカウントの追加**」をクリックして、Gmailアカウントを接続するために事前に定義されたGmailのコネクタを選択します。

 

![](/liveagent/scripts/file.php?view=Y&file=c8ae1b895d8443805f7bae3b3333e9cf)

 

新しいポップアップウインドウが開きます。すでにGmailアカウントにログインしている場合は、Gmailアカウントの接続を承認するよう求められます。ログインしていない場合は、ログインするように求められます。

 

 

![](/liveagent/scripts/file.php?view=Y&file=2c178b3f3b06bbc48c34bde802704048)

 

Gmailアカウントを承認した後、このメールボックスの割り当て先**「チーム」**を指定し、保存します。設定は以上です。

 

![](/liveagent/scripts/file.php?view=Y&file=e3af7c50fd608ac03e04b23c8a97ad21)

 

**■GmailアカウントとLiveAgent（ソフトウェア版）を接続する**

LiveAgent（ソフトウェア版）では、Gmailのユーザー名とパスワードを使用して、Google IMAP / POP3とSMTPサーバを経由して接続します。Gmailのユーザー名/メールアドレスとパスワードを尋ねられ、その後LiveAgentは、指定されたユーザー名とパスワードでGoogleメールサーバーに接続しようとします。ほとんどの場合、最初の接続は不成功に終わります。この場合、Gmailアカウントのセキュリティ機能をいくつか変更する必要があります。下記のセクションをご確認ください。

 

![](/liveagent/scripts/file.php?view=Y&file=e57563a5499318e892e124db3cf8c49f)

 

	- LiveAgentにログインし、メールアカウントの設定画面を開きます。**「設定」＞「電子メール」＞「メールアカウント」**

	- **「メールアカウントの追加」**をクリックして、Gmailと接続するために事前に定義されたGmailのコネクタを選択します。

	- Gmailのメールアドレスとパスワードが尋ねられます。情報を入力して接続ボタンをクリックします。

	- エラーのメッセージが表示される場合は、下記のトラブルシューティングのセクションをご覧ください。

	- Gmailアカウントの承認テストに成功すると、このメールボックスの割り当て先**「チーム」**を指定し、保存します。設定は以上です。

 

**■GmailアカウントとLiveAgent（ソフトウェア版）を接続するための要件**

最初のステップはGmailアカウントへのIMAP接続を有効にすることです。まず通常通りブラウザでGmailにログインしてください。

次に**「設定」＞「メール転送とPOP/IMAP」**セクションで、IMAPアクセスのステータスを確認します。有効でない場合は「IMAPを有効にする」にチェックを入れて「変更を保存」をクリックします。この手順については次のリンクに記載されています。[https://support.google.com/mail/answer/7126229](https://support.google.com/mail/answer/7126229)

もしまだGoogleアカウントに接続できない場合は、Googleアカウントのセキュリティ通知に関する次のページをご確認ください。[https://security.google.com/settings/security/notifications](https://security.google.com/settings/security/notifications)　

GoogleがGmailアカウントに接続するためのLiveAgentソフトウェアを許可する必要があります。次のページ（[https://accounts.google.com/DisplayUnlockCaptcha](https://accounts.google.com/DisplayUnlockCaptcha)）でGoogleアカウントへのアクセスを許可します。その後10分以内にもう一度LiveAgentでGmailのアカウントに接続してみてください。成功すればGmailはこの接続を覚え、パスワードを変更しない限り、LiveAgentがGmailアカウントにアクセスできるようにします。 

Gmailアカウントの接続にまだ成功しない場合は、Googleの2段階認証プロセスに切り替えるか、次のページ（[https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps)）で安全性の低いアプリへのアクセスを許可する設定を行います。この設定に関する記述は[こちら](https://support.google.com/accounts/answer/6010255)です。LiveAgentサーバとGoogleサーバ間の通信はSSL / TLSを用いて保護されていますが、Googleでは簡単なユーザー名とパスワードのログインは、OAuthソリューションと比べて安全性が低いと考えています。

この後も接続エラーが発生している場合は、弊社サポートにお問い合わせください。

 

**■Gmailのパスワードを変更した場合**

Gmailアカウントのパスワードが変更された場合、あなたのGmailとLiveAgentとの間の接続は完全に動作を停止します。あなたのLiveAgentアカウントでこのGmailアカウントの接続を編集する必要があります。**「設定」＞「電子メール」＞「メールアカウント」＞「編集」**

 

![](/liveagent/scripts/file.php?view=Y&file=96f93f460fb0368a8e097b9c173f17fd)

 

 

![](/liveagent/scripts/file.php?view=Y&file=62b922e7a28705b14dedf1f0e32f443e)

 

クラウド版では、編集画面で「無効にする」をクリックしてから再度「有効にする」をクリックします。LiveAgentアカウントを再度承認するように求められるので、それを有効にするとGmailは再接続されます。

ソフトウェア版のアカウントでは、「無効にする」をクリックしてからパスワードフィールドに新しいGmailのパスワードを設定します。変更を保存して、「有効にする」をクリックするとGmailは再接続されます。LiveAgentはメールアカウントを有効化する際にあらためて接続テストをします。エラーが表示されなければ、メールアカウントの再設定は完了です。

 

**■G SuiteビジネスメールアカウントとLiveAgentを接続する**

G SuiteビジネスメールアカウントとLiveAgentクラウド版の接続には、特別な設定は必要ありません。上記でご案内したGmailアカウントと同じ手順で設定できます。

G SuiteビジネスメールアカウントとLiveAgentソフトウェア版を接続するには、以下の手順に従ってください。

	- G Suiteアカウントにログインし、次のガイド（[https://support.google.com/a/answer/105694?hl=ja](https://support.google.com/a/answer/105694?hl=ja)）に従って、あなたのメールアカウントへのIMAP / POP3アクセスを有効にします。詳細設定を行なった後、その設定が個々のユーザーアカウントに反映されるまでに最大1時間ほどかかる場合があります。

	- 次のステップでは、このビジネスメールアカウントに使用する個人のGmailアカウントへのIMAP接続を有効にします。通常通りブラウザであなたのGmailにログインします。

	- **「設定」＞「メール転送とPOP/IMAP」**セクションで、IMAPアクセスのステータスを確認します。有効でない場合は「IMAPを有効にする」にチェックを入れて「変更を保存」をクリックします。この手順については次のリンクに記載されています。[https://support.google.com/mail/answer/7126229](https://support.google.com/mail/answer/7126229)

	- ：IMAPが有効になっている状態で、あなたのLiveAgentアカウントにログインしてメールアカウントの設定画面に行きます。**「設定」＞「電子メール」＞「メールアカウント」**

	- **「メールアカウントの追加」**をクリックして、Gmailと接続するために事前に定義されたGmailのコネクタを選択します。

	- Gmailのメールアドレスとパスワードが尋ねられます。情報を入力して接続ボタンをクリックします。

	- LiveAgentは提供された資格情報で接続をテストします。エラーのメッセージが表示される場合は、上記のトラブルシューティングのセクションをご覧ください。テストが成功すると、このメールボックスの割り当て先**「チーム」**を指定し、保存します。設定は以上です。