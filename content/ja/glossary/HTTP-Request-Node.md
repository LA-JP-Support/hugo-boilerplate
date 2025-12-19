---
title: HTTPリクエストノード
translationKey: http-request-node
description: HTTPリクエストノードについて学びましょう。n8nやNode-REDなどの自動化プラットフォームにおいて、外部APIへのHTTPリクエスト送信やシステム統合を行うための重要なコンポーネントです。
keywords:
- HTTPリクエストノード
- API統合
- 自動化プラットフォーム
- n8n
- Node-RED
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: HTTP Request Node
term: エイチティーティーピーリクエストノード
url: "/ja/glossary/HTTP-Request-Node/"
---
## HTTP Request Nodeとは?
HTTP Request Nodeは、自動化・統合プラットフォーム(n8n、Node-RED、Node.js)における中核コンポーネントであり、外部サーバーやAPIに対してHTTPリクエスト(GET、POST、PUT、PATCH、DELETE)を送信し、自動化ワークフロー内でレスポンスを処理します。このノードは、システム統合、サードパーティサービスの利用、Webhookのトリガー、アプリケーション間のデータ交換において不可欠です。

## 主要機能

**対応HTTPメソッド:**

- **GET** – 指定されたリソースからデータを取得
- **POST** – リソースの作成または更新のためにデータを送信
- **PUT** – リソースの置換または更新
- **PATCH** – リソースの部分的な更新
- **DELETE** – リソースの削除
- **HEAD** – レスポンスボディなしでヘッダーのみを取得
- **OPTIONS** – サポートされている通信オプションを照会

**認証オプション:**

- 認証なし(オープンエンドポイント)
- Basic認証(ユーザー名/パスワード、Base64エンコード)
- Digest認証(ハッシュ化された認証情報)
- Bearer Token(AuthorizationヘッダーのJWT)
- OAuth1 & OAuth2(委譲型、トークンベースのアクセス)
- Header認証(APIキー用のカスタムヘッダー)
- カスタム認証(ユーザー定義ロジック)
- Query認証(クエリパラメータ経由の認証情報)

**対応データ形式:**

- application/json(JSONペイロード)
- application/x-www-form-urlencoded(キー/値ペア)
- multipart/form-data(ファイルアップロード、複雑なデータ)
- Raw(指定されたコンテンツタイプの任意のコンテンツ)
- Plain Text(非構造化テキスト)
- Binary(ファイルおよびバイナリデータ転送)

**追加機能:**

- カスタムヘッダー(Content-Type、Authorization)
- クエリパラメータ(動的フィルタリング)
- プロキシサポート(HTTPプロキシ)
- タイムアウト(リクエストおよび接続の制御)
- SSL検証制御(証明書エラーの無視)
- 自動および手動ページネーション
- リダイレクト処理
- レスポンス処理(JSON、テキスト、バイナリ、ファイル)
- バッチ処理(並列または順次リクエスト)

## プラットフォーム別の設定

### n8n HTTP Request Node

**基本パラメータ:**

- **Method** – HTTPメソッドを選択(DELETE、GET、HEAD、OPTIONS、PATCH、POST、PUT)
- **URL** – APIエンドポイント(静的または式を使用した動的)
- **Authentication** – 事前定義された認証情報を選択、または手動で設定
- **Send Query Parameters** – キー/値ペアまたはJSONとして定義
- **Send Headers** – カスタムヘッダーを指定
- **Send Body** – POST、PUT、PATCHリクエストで有効化
- **Output Variables** – ステータスコード、ボディ、ヘッダーをワークフロー変数にマッピング

**詳細オプション:**

- クエリパラメータの配列形式
- バッチ処理(バッチあたりのアイテム数、バッチ間の遅延)
- SSL問題の無視(信頼できるエンドポイントのみ)
- ヘッダーの小文字化トグル
- リダイレクト(有効/無効、最大リダイレクト数)
- レスポンス処理(ヘッダー/ステータスの含有、形式)
- ページネーション(オフ、パラメータ更新、次のURL)
- プロキシ指定
- タイムアウト(リクエストタイムアウト、ミリ秒)

**POSTリクエストの例:**
```json
{
  "method": "POST",
  "url": "https://api.example.com/resource",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Node-RED HTTP Request Node

**設定:**

- **Method** – GET、POST、PUT、DELETE、PATCH
- **URL** – 静的またはMustache構文を使用した動的(`{{variable}}`)
- **Payload** – 無視、クエリ文字列に追加、またはボディとして送信
- **Authentication** – なし、Basic、Digest、Bearer Token
- **Proxy** – 必要に応じてプロキシサーバー経由でルーティング
- **Headers** – ノード設定または`msg.headers`経由で追加
- **Output** – レスポンスを文字列、パース済みJSON、またはバイナリバッファとして指定
- **Catch Node** – 2xx以外のHTTPレスポンスを処理

**動的GETリクエストの例:**
```json
{
  "method": "GET",
  "url": "https://api.example.com/users/{{userId}}",
  "headers": {
    "Authorization": "Bearer {{token}}"
  }
}
```

**重要:** HTTPノード間でヘッダーの漏洩を避けるため、`msg.headers`を`{}`にリセットしてください。

### Node.js HTTPリクエスト

**ネイティブHTTP/HTTPSモジュール:**  
組み込みストリーミングサポートを備えた、リクエストの完全制御のための低レベルモジュール。

**Fetch API(Node.js 18+):**  
Node.js 18以降に組み込み、Promiseを返し、async/await構文をサポート。

```js
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```

**axios:**  
インターセプター、タイムアウト、自動JSON処理、リクエスト/レスポンス変換を備えたPromiseベースのHTTPクライアント。

```js
const axios = require('axios');
axios.post('https://api.example.com/resource', {
  name: 'John Doe',
  email: 'john@example.com'
}, {
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN'
  }
}).then(response => {
  console.log(response.data);
});
```

## ベストプラクティス

**セキュリティ:**

- 組み込みの認証情報マネージャーを使用し、シークレットをハードコードしない
- 常にSSL証明書検証付きのHTTPSを使用
- すべての動的入力(ヘッダー、パラメータ、ボディ)をサニタイズ
- トークンをローテーション、期限切れ、安全に保管

**エラー処理:**

- 常にHTTPステータスコードを確認し、処理
- ハングするリクエストを避けるため、適切なタイムアウトを設定
- 一時的な障害(ネットワーク、5xxエラー)に対してリトライを実装

**コンテンツタイプとエンコーディング:**

- Content-Typeヘッダーをボディ形式に一致させる
- 特殊文字のクエリパラメータをURLエンコード
- 必要な配列エンコーディングについてAPIドキュメントを確認

**ページネーション:**

- APIパターンを認識(page/limit、offset、次のURL)
- 可能な場合はプラットフォームのページネーション機能を使用

**ヘッダーとレスポンス処理:**

- Node-REDでは、HTTPノード間で`msg.headers`をリセット
- レート制限、認証チャレンジ、ページネーションのためにレスポンスヘッダーを確認

**デバッグ:**

- 組み込みテスト機能またはPostmanなどのツールで設定を検証
- トラブルシューティングのために完全なレスポンスをログ記録

## よくある落とし穴

- 不正なContent-TypeによるAPI拒否
- 特殊文字を含むエンコードされていないクエリパラメータ
- Node-REDでのヘッダー継承(ノード間でリセットが必要)
- 適切なエラー処理なしで2xx以外のレスポンスを無視
- 認証情報を必要とするAPIで認証が欠落

## ユースケース

**API統合:**  
REST APIからユーザー情報を取得。GETメソッドを設定し、URLを設定、Authorizationヘッダーを追加、レスポンスをマッピング。

**データ送信:**  
フォームを送信。POSTメソッド、Content-Type `application/x-www-form-urlencoded`、フィールドを入力。

**ファイルアップロード:**  
`multipart/form-data`を使用してファイルをアップロード。POST/PUT、ファイルを添付。

**Webhookトリガー:**  
イベント発生時に外部システムに通知。POSTメソッド、URLを設定、JSONボディを送信。

**AIエージェントとの自動化(n8n):**  
LLMワークフローでHTTP Request Nodeを使用。ノードを接続し、最適化されたレスポンス抽出を設定。

## プラットフォーム固有の注意事項

**n8n:**

- 事前定義されたOAuth2、APIキー、汎用認証オプション
- ドラッグ&ドロップUI、cURLインポート
- Body/Headers/Queryをフィールドまたは直接JSON入力として
- ページネーションはパラメータ増分と次のURLをサポート
- AIエージェント統合はLLM向けにレスポンスを最適化

**Node-RED:**

- `msg.method`、`msg.url`、`msg.headers`経由の動的設定
- 動的URL/ヘッダー用のMustache構文
- オブジェクトペイロードの自動Content-Type
- レスポンス処理:文字列、JSON、バイナリバッファ

**Node.js:**

- HTTP/HTTPS:低レベル、完全制御
- axios/node-fetch/Fetch API:高レベル、Promiseベース
- ネイティブストリーミングサポート
- 環境またはライブラリオプション経由のプロキシ

## 参考資料

- [n8n HTTP Request Node Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [Mastering the n8n HTTP Request Node](https://automategeniushub.com/mastering-the-n8n-http-request-node/)
- [Node-RED HTTP Request Node](https://flowfuse.com/node-red/core-nodes/http-request/)
- [Node-RED Securing Guide](https://nodered.org/docs/user-guide/runtime/securing-node-red)
- [Node-RED HTTPS Configuration](https://nodered.org/docs/user-guide/runtime/securing-node-red#enabling-https-access)
- [Node-RED Proxy Configuration](https://flowfuse.com/node-red/core-nodes/http-proxy/)
- [Node.js HTTP Module Documentation](https://nodejs.org/api/http.html)
- [W3Schools: Node.js HTTP Module](https://www.w3schools.com/nodejs/nodejs_http.asp)
- [Axios Documentation](https://axios-http.com/docs/intro)
- [Node.js Fetch API Guide](https://oxylabs.io/blog/nodejs-fetch-api)
- [Stack Overflow: HTTP POST in Node.js](https://stackoverflow.com/questions/6158933/how-is-an-http-post-request-made-in-node-js)
- [Postman](https://www.postman.com/)
