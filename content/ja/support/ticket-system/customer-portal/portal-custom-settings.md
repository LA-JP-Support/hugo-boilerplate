---
title: "ドメインパーキングガイド（カスタムドメインの設定）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "portal-custom-settings"
description: "クラウド版で使用するデフォルトのドメイン（xxx*.liveagent.jp）を*独自のドメイン/サブドメインに置き換えることが可能です。（例：https://support.yourdomain.com　や　*https://www.companysupport.com）*"
keywords: ["カスタム", "設定", "LiveAgent", "Encrypt", "IPアドレス"]
type: support
category: "ticket-system/customer-portal"
e-title: "Custom - Settings"
---

クラウド版で使用するデフォルトのドメイン（xxx*.liveagent.jp）を*独自のドメイン/サブドメインに置き換えることが可能です。（例：https://support.yourdomain.com　や　*https://www.companysupport.com）*

設定の手順は以下の通りです。

 

**1. CNAMEレコードを作成する**

CNAMEレコードは、使用する希望のカスタムドメイン/サブドメイン（例：*support.yourdomain.com*）からLiveAgentアカウントのドメイン（例：*example.ladesk.com*）をポイントする必要があります。

使用するドメイン/サブドメインはカスタムドメインである必要があります。WebサイトではなくLiveAgentアカウントにドメインをパークするとLiveAgentだけが表示されるため、Webサイトでは使用しないでください。

CNAMEレコードの設定方法がわからない場合は、ホスティングプロバイダに相談し、設定を依頼してください。ゴールはカスタムドメインからLiveAgentにポイントすることです。

**2. CNAMEレコードが既に適用されているかどうかを確認する**

CNAMEが設定されたら、それが既に世界中に適用され伝播されていることを確認する必要があります。伝播には最大24時間かかることがありますが、通常は数分です。[whatsmydns.net](https://www.whatsmydns.net/#CNAME/)のようなDNS伝播チェッカーサイトで確認できます。LiveAgentアカウントのURLがすべての場所に表示されたら、次の手順に進むことができます。

別の確認方法としては、ブラウザでカスタムドメインを開き、「Your account has been suspended」というメッセージが表示*されている*場合は、CNAMEがすでにLiveAgentのサーバをポイントしており、次の手順に進むことができます。

**3. LiveAgent管理パネルでカスタムドメインを設定する**

LiveAgentに管理者権限でログインし、「設定」 - >「システム」 - >「ドメインの設定」セクションに移動し、プロトコルなしでカスタムドメインを「カスタムドメイン」フィールドに挿入して「保存」します。

保存すると、数分でカスタムドメインにLiveAgentが表示され、通常どおりに使用できます。この時点で、あなたとすべてのエージェントはLiveAgentを操作するためのカスタムドメインのみを使用する必要があります。

代わりに「*ドメインDNSでCNAMEレコードを見つけることができませんでした*」などのメッセージが表示された場合は、入力したドメイン/サブドメインのCNAMEが正しく設定されていないため、手順1に戻ってください。

**4.（オプション）SSL証明書を追加する**

LiveAgent の問い合わせフォームボタンをHTTPSのセキュリティ保護されたWebサイトに配置する場合は、LiveAgentをHTTPS経由でも利用できるようにする必要があります。カスタムドメイン/サブドメインにSSL証明書を追加する必要があります。

パーキングした特定のサブドメインに対して直接作成した証明書またはトップドメインのワイルドカード証明書を使用できます。もちろん、あなたが持っている場合に限ります。

これが何を意味するのかわからない場合は、ホスティングプロバイダのサポートまたはサーバー管理者にお問い合わせください。

 

SSL証明書の費用を支払いをしたくない場合は、無料のLets暗号化SSL証明書を使用して作業することができます。こちらの[ガイド](https://support.smartweb.jp/liveagent/798219-Lets-Encrypt%E3%81%AESSL%E8%A8%BC%E6%98%8E%E6%9B%B8%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B)を使って証明書を適用することができます。

 

証明書キーファイルの内容を「SSLキー」の欄に配置し、実際の証明書（およびその他の中間証明書）の内容を「SSL証明書」の欄に配置する必要があります。あなたの証明書が、エンドユーザ、中間、ルートの証明書からなるより長い証明チェーンで構成されている場合は、指定された順序で別の証明書を追加する必要があります。

SSL証明書は保存後数分以内に適用され、カスタムドメイン/サブドメインが警告なしでHTTPSプロトコルで動作するかどうかを確認できます。

 

ドメイン設定の画面

![](/liveagent/scripts/file.php?view=Y&file=962c1efa209037be2914106656da6211)

 

 

## **考えられる問題**

カスタムドメインまたは独自のSSL証明書の設定中に、以下の問題に直面する可能性があります。

**"ドメイン構成が進行中です。しばらくお待ちください...（Domain configuration in progress.Please wait...）"**

LiveAgentのシステムはあなたのリクエストを処理していますのでお待ちください。12時間たってもこのメッセージが表示される場合は、[サポート窓口](https://www.liveagent.jp/contact/)にご連絡ください。

**"カスタムドメイン形式が無効です（The custom domain format is invalid）"**

ドメインが有効かどうかを再度確認します。ドメインには、プロトコル、エンドスラッシュ、ページ/ディレクトリを含めないでください。WRONG入力の例を次に示します。

	- *http://mydomain.com*

	- *https://www.domain.com/*

	- *mydomain.com/*

	- *mydomain.com/agent*

	- *domain*

	- *.domain*

	- *domain/agent*

**"ドメインは既に使用されています。" または"ドメインは既に別のアカウントで使用されています。"（"Domain is already used." or "Domain is already used by another account" ）**

あなたが選んだドメインはすでに他のユーザによって使用されています。別のものを指定する必要があります。間違いだと思われる場合は、お問い合わせください。

**"ドメインは予約済みのドメインです。" または "ドメインは予約済みドメインとして使用できません。" （"Domain is　reserved domain." or "Domain can not be used as it is reserved domain."）**

このメッセージが表示されるのは以下の場合です。

・「something.liveagent.jp」をカスタムドメインとして使用しようとしたとき

・以下の予約語を使用しようとしたとき

*localhost, dev, www, ftp, http, https, mailhost, mail, host, api, newweb, static, signup, support, demo, geo, iso, ios, members, addons, qualityunit*

**"カスタムドメインをIPアドレスに設定することはできません（You can not set custom domain to an IP address）"**

IPアドレスをカスタムドメインとして使用することはできません。代わりに第2または第3レベルのドメインを使用してください。 

**"ドメイン名は空ではありません。（Domain name cannot be empty）" **

カスタムドメインを入力してもう一度お試しください。

**" '*your.liveagent.jp*'ドメインをターゲットとするドメインDNSでCNAMEレコードを見つけることができませんでした。（Could not find CNAME record in domain DNS targeting 'your liveagent.jp' domain）" **

このメッセージは、あなたのDNS（CNAME）ターゲティングがまだ設定または適用されていない（世界中に伝播されていない）という事実に関する通知です。オンラインツール（[https://www.whatsmydns.net/#CNAME/）](https://www.whatsmydns.net/#CNAME/)を使用してカスタムドメインのCNAMEレコードを確認することができます。CNAMEが正しく設定されており、時間がかかることがわかっている場合は、この警告を無視してください。それがLiveAgentのサーバーに伝播するのを待ちます。

**"両方の証明書フィールドを入力する必要があります。（You need to fill both certificate fields or none of them）"**

カスタムドメインにSSL証明書を使用する場合は、両方のフィールド（SSLキーとSSL証明書）を必ず入力してください。

**"カスタム証明書はカスタムドメインでのみ使用できます。（Custom certificate can only be used with custom domain）" **

カスタムドメインを使用していない場合は、SSL証明書を設定する必要はありません。LiveAgentのクラウドアカウントは保護されており、DigiCert認証会社の共有ワイルドカード証明書を使用しています。

**"証明書を認識できません。" または "CAバンドルを認識できません。"（"Certificate can not be recognized." or "CA bundle can not be recognized."） **

入力した証明書を解析できません。有効なx509証明書を入力する必要があります。