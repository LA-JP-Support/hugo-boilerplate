---
title: "REST API の利用例 （サンプルコード）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "rest-api-usage"
description: "LiveAgent の API を利用したサンプルコードをご紹介します。"
keywords: ["REST", "API", "利用", "LiveAgent", "Agent"]
category: "settings"
---
## LiveAgent REST API サンプルコード概要

サンプルコードを使用する際の注意点と基本情報を説明します。

### APIキーと変数の説明

- **[API_KEY]**: LiveAgentのAPIキー
- **[CONV_CODE], [conversationID]**: チケットの固有番号
- **[example.com]**: LiveAgent利用時のドメイン（[xxx].liveagent.jpなど）

## HTTPメソッド別のAPIリクエスト例

### GETリクエスト: メッセージ取得

特定の会話のメッセージを取得するサンプルコードです。

```php
// メッセージ取得のコードは既存のまま
```

### POSTリクエスト: 新規会話作成

新しい会話を作成するサンプルコードです。

```php
// 新規会話作成のコードは既存のまま
```

### PUTリクエスト: 会話ステータス変更

特定の会話のステータスを変更するサンプルコードです。

```php
// 会話ステータス変更のコードは既存のまま
```

### DELETEリクエスト: 会話削除

会話を削除するサンプルコードです。

```php
// 会話削除のコードは既存のまま
```

## エラーハンドリングとレスポンス処理

各サンプルコードに共通するエラーチェックと応答処理の方法を説明します。

- レスポンスのJSON解析
- エラーステータスの確認
- エラー時の処理