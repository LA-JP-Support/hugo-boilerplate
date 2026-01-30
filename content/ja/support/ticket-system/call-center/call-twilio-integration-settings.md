---
title: "Twilio の連携設定をしても、電話の発着信ができません"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "call-twilio-integration-settings"
description: "LiveAgent へ Twilio 設定をした後も電話の発着信ができない場合、次のようなことが原因として考えられます。"
keywords: ["Twilio", "設定", "電話", "LiveAgent", "アップグレード"]
type: support
category: "ticket-system/call-center"
e-title: "Twilio - Integration - Settings - Phone"
---

LiveAgent へ Twilio 設定をした後も電話の発着信ができない場合、次のようなことが原因として考えられます。

- #### エージェントの PC に音声デバイス（マイク/スピーカー/ヘッドセットなど）が接続されていない

音声デバイスを接続後に再度お試しください。

- #### Twilio で認証された電話番号以外の番号から発信をした（Twilioがトライアル版の場合）

Twilioのトライアル版では、通話テストの可能な電話番号に制限があります。アカウント取得時にTwilioへ登録された電話番号をご利用ください。登録された電話番号はTwilio管理画面の「検証済み電話番号」からご確認いただけます。

なお、Twilioのアカウントをアップグレードいただくことで、通話制限が解除されます。

- #### Twilio の管理画面上で正しいアプリケーションが設定されていない

LiveAgentとTwilioをつなぐプラグインが正しく設定されていない可能性があります。設定方法など詳細は以下のFAQ記事を参照ください。

→ [
音声通話サービス「Twilio」を利用するには](http://support.smartweb.jp/liveagent/957760-%E9%9F%B3%E5%A3%B0%E9%80%9A%E8%A9%B1%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9-Twilio-%E3%82%92%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E3%81%AB%E3%81%AF)

上記内容をご確認いただき、問題が解決しない場合は、大変お手数ですが弊社サポートと窓口までお問い合わせください。