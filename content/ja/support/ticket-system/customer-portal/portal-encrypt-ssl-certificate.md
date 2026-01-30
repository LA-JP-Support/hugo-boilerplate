---
title: "「Let’s Encrypt」のSSL証明書を使用する"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "portal-encrypt-ssl-certificate"
description: "私たちは「Let's Encrypt」の直接的なサポートはしませんが、使い方をご案内します。https: //www.sslforfree.com/ から無料の証明書を入手し、LiveAgentで使用できます。"
keywords: ["Encrypt", "SSL", "証明書", "Let's Encrypt", "LiveAgent"]
type: support
category: "ticket-system/customer-portal"
e-title: "Encrypt - Ssl - Certificate - Usage"
---

私たちは「Let's Encrypt」の直接的なサポートはしませんが、使い方をご案内します。[https:](http://https: //www.sslforfree.com/)[ //www.sslforfree.com/](http://https: //www.sslforfree.com/) から無料の証明書を入手し、LiveAgentで使用できます。

 

「SSL For FREE」を使用して「Let's Encrypt」SSL証明書を生成する方法

 

1.  [https://www.sslforfree.com/](https://www.sslforfree.com/)  ウェブサイトに行き、SSL証明書を生成するドメイン名を入力して、「Create Free SSL Certificate」ボタンをクリックします。

 

![](/liveagent/scripts/file.php?view=Y&file=c7fe4df3eeba8415843af8592535d1c5)

 

2.ドメインの所有者であることを確認する方法は3つあります。いずれかを選択できますが、「Manual Verification(DNS)」について説明します。 

 

![](/liveagent/scripts/file.php?view=Y&file=639a36c31f9da840e2de0ae588517432)3. 「SSL For FREE」で提供されている指示に従う必要があります。この場合、DNSレコードを更新する必要があるため、ドメインで使用するDNS管理ページに移動する必要があります（[このリンク](https://support.google.com/a/answer/183895?hl=ja)は、TXTレコードを設定するのに役立ちます[Googleの特定の部分を無視する]）。

 

	- 「SSL For FREE」のウェブサイトで生成したTXTレコードをDNSレコード（TTL（Time to Live）フィールドに「1」を入力）に追加します  ：  

	**-**  name/host_acme-challenge.yourdomain.com  をxxxにしてTXTレコードを追加します（サイトはユニークな値を生成します）。  

	- TXTレコードがWebサイトのリンクに移動していることを確認します。

	- DNS TXTレコードが伝播するまで数分（最大24時間）待たなければならない場合があります。検証中に「JWSが無効な再生防止ナンスを持っている（JWS has invalid anti-replay nonce）」というエラーが表示された場合は、それが動作するまでページをリフレッシュ（プロンプトが表示されたらポストデータを再送）するだけです。

	- 完了後、確認に成功したら「Download SSL Certificate」ボタンをクリックします。

**重要な注意**：DNSリフレッシュを待っている間は、ページを離れないでください！離れるとシステムは新しい値を生成し、最初からやり直すことになります。

 

![](/liveagent/scripts/file.php?view=Y&file=bfb5edfcc6618f49397001e06a6708e4)

 

4.「Download SSL Certificate」ボタンをクリックすると、「Generate SSL certificate」ページに遷移します。「Certificate Successfully Generated」ページに達すると、*証明*書、証明書バンドル、および秘密鍵をコピーしてLiveAgentに貼り付けることができます。または、「Download all SSL Certificate Files」ボタンをクリックして、SSL証明書、証明書バンドル、および秘密鍵をzipパッケージで*ダウンロード*でき*ます*。

[ドメインパーキングガイド](https://support.smartweb.jp/liveagent/390000-%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%91%E3%83%BC%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%AC%E3%82%A4%E3%83%89%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A)の記事を使用して、LiveAgentで証明書を適用することができます。