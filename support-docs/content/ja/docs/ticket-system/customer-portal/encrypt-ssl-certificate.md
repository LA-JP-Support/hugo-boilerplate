---
title: "「Let’s Encrypt」のSSL証明書を使用する"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "encrypt-ssl-certificate"
description: "私たちは「Let's Encrypt」の直接的なサポートはしませんが、使い方をご案内します。https://www.sslforfree.com から無料の証明書を入手し、LiveAgentで使用できます。"
keywords: ["Encrypt", "SSL", "証明書", "Let's Encrypt", "LiveAgent"]
category: "ticket-system/customer-portal"
---
## はじめに

私たちは「Let's Encrypt」の直接的なサポートはしませんが、使い方をご案内します。https://www.sslforfree.com から無料の証明書を入手し、LiveAgentで使用できます。

## SSL証明書の生成手順

### SSL For FREEでの証明書作成

1. [https://www.sslforfree.com/](https://www.sslforfree.com/) ウェブサイトに行き、SSL証明書を生成するドメイン名を入力して、「Create Free SSL Certificate」ボタンをクリックします。

### ドメイン所有者の確認方法

2. ドメインの所有者であることを確認する方法は3つあります。いずれかを選択できますが、「Manual Verification(DNS)」について説明します。

### DNSレコードの更新

3. 「SSL For FREE」で提供されている指示に従う必要があります。この場合、DNSレコードを更新する必要があるため、ドメインで使用するDNS管理ページに移動する必要があります。

#### DNSレコード追加の詳細手順
- 「SSL For FREE」のウェブサイトで生成したTXTレコードをDNSレコード（TTL（Time to Live）フィールドに「1」を入力）に追加します
- name/host_acme-challenge.yourdomain.com をxxxにしてTXTレコードを追加します
- TXTレコードがWebサイトのリンクに移動していることを確認します
- DNS TXTレコードが伝播するまで数分（最大24時間）待つ

**重要な注意**：DNSリフレッシュを待っている間は、ページを離れないでください！

### 証明書のダウンロード

4. 「Download SSL Certificate」ボタンをクリックすると、「Generate SSL certificate」ページに遷移します。「Certificate Successfully Generated」ページに達すると、証明書、証明書バンドル、および秘密鍵をコピーしてLiveAgentに貼り付けることができます。

### 証明書の適用

ドメインパーキングガイドの記事を使用して、LiveAgentで証明書を適用することができます。

## 注意事項

- 検証中に「JWSが無効な再生防止ナンスを持っている」というエラーが表示された場合は、ページをリフレッシュしてください
- 必要に応じて、「Download all SSL Certificate Files」ボタンを使用してzipパッケージでファイルをダウンロードできます