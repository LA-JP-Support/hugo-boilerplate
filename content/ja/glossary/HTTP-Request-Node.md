---
title: HTTPリクエストノード用語集
translationKey: http-request-node-glossary
description: HTTPリクエストノードについて学びましょう。n8nやNode-REDなどの自動化プラットフォームにおいて、外部APIへのHTTPリクエスト送信やシステム統合を行うための重要なコンポーネントです。
keywords:
- HTTPリクエストノード
- API統合
- 自動化プラットフォーム
- n8n
- Node-RED
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: エイチティーティーピーリクエストノードようごしゅう
reading: HTTPリクエストノード用語集
kana_head: その他
e-title: HTTP Request Node Glossary
---

## はじめに

**HTTPリクエストノード**は、[n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)、[Node-RED](https://flowfuse.com/node-red/core-nodes/http-request/)、Node.jsを含む自動化および統合プラットフォームにおける中核的なコンポーネントです。外部サーバーやAPIに対してHTTPリクエスト(GET、POST、PUT、PATCH、DELETEなど)を送信し、自動化ワークフロー内でそのレスポンスを処理することができます。このノードは、異なるシステムの統合、サードパーティサービスの利用、Webhookのトリガー、アプリケーション間のデータ交換において不可欠です。

## ノードの機能

### サポートされるHTTPメソッド

HTTPリクエストノードは、それぞれ特定のRESTful操作に対応する以下のメソッドをサポートしています:

- **GET**: 指定されたリソースからデータを取得します。
- **POST**: リソースを作成または更新するためにデータを送信します。
- **PUT**: リソースを置換または更新します。
- **PATCH**: リソースを部分的に更新します。
- **DELETE**: リソースを削除します。
- **HEAD**: レスポンスボディなしでヘッダーを取得します。
- **OPTIONS**: サポートされている通信オプションを照会します。

参考資料:
- [n8n HTTPメソッド](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#method)
- [Node-RED HTTPメソッド](https://flowfuse.com/node-red/core-nodes/http-request/#configuring-http-request-node)

### 認証オプション

HTTPリクエストノードは、幅広い認証標準に対応しています:

- **認証なし**: オープンなエンドポイント向け。
- **Basic認証**: ヘッダー内のユーザー名とパスワード、通常はBase64エンコード。
- **Digest認証**: Basicよりも安全で、ハッシュ化された認証情報を使用。
- **Bearerトークン**: Authorizationヘッダー内のトークンベース(例:JWT)。
- **OAuth1 & OAuth2**: 委譲されたトークンベースのアクセス用。
- **ヘッダー認証**: APIキーやその他のトークン用のカスタムヘッダー。
- **カスタム認証**: ユーザー定義の認証ロジック。
- **クエリ認証**: クエリパラメータ経由で送信される認証情報。

参考資料:
- [n8n 認証](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#authentication)
- [Node-RED 認証](https://flowfuse.com/node-red/core-nodes/http-request/#configuring-http-request-node)

### サポートされるデータ形式

HTTPリクエストノードは、リクエストとレスポンスの両方で様々なデータ形式を処理します:

- **application/json**: JSONペイロード。
- **application/x-www-form-urlencoded**: ボディ内にエンコードされたキー/値ペア。
- **multipart/form-data**: ファイルアップロードや複雑なデータ用。
- **Raw**: 指定されたコンテンツタイプを持つ任意のコンテンツ。
- **プレーンテキスト**: 構造化されていないテキストペイロード。
- **バイナリ**: ファイルおよびバイナリデータ転送用。

参考資料:
- [n8n Send Body](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#send-body)
- [Axios リクエストボディ形式](https://axios-http.com/docs/req_config)
- [Node.js Fetch API](https://oxylabs.io/blog/nodejs-fetch-api)

### 追加機能

- **カスタムヘッダー**: 任意のHTTPヘッダー(例:Content-Type、Authorization)を設定。
- **クエリパラメータ**: リクエストを動的にフィルタリングまたは変更。
- **プロキシサポート**: HTTPプロキシ経由でリクエストをルーティング。
- **タイムアウト**: リクエストおよび接続のタイムアウトを制御。
- **SSL検証制御**: オプションでSSL証明書エラーを無視。
- **自動および手動ページネーション**: 複数ページのAPI結果を取得。
- **リダイレクト処理**: リダイレクトの追跡方法を設定。
- **レスポンス処理**: JSON、テキスト、バイナリ、またはファイルとして出力。
- **バッチ処理**: 並列または順次送信されるリクエストの数とタイミングを制御。
- **AIエージェント向け最適化**: (n8n) AIツールの利用に最適化されたレスポンス。

参考資料:
- [n8n ページネーション](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/#pagination)
- [Node-RED 出力オプション](https://flowfuse.com/node-red/core-nodes/http-request/#output)

## 設定手順

設定プロセスと利用可能なパラメータはプラットフォーム固有です。以下のセクションでは、n8n、Node-RED、Node.jsの典型的な設定ワークフローを説明します。

### n8n HTTPリクエストノード

**公式ドキュメント:**  
[n8n HTTPリクエストノード ドキュメント](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)  
[n8n HTTPリクエストノードをマスターする (AutomateGeniusHub)](https://automategeniushub.com/mastering-the-n8n-http-request-node/)

#### 1. ノードパラメータ

- **メソッド:** HTTPメソッドを選択(DELETE、GET、HEAD、OPTIONS、PATCH、POST、PUT)。
- **URL:** APIエンドポイントを入力。静的または[式](https://docs.n8n.io/code-expressions/)を使用して動的に構築可能。
- **認証:** 事前定義された認証情報から選択、または手動で設定(Basic、Digest、Bearer、OAuthなど)。
- **クエリパラメータの送信:** リクエストをフィルタリングまたは変更。キー/値ペアまたはJSONとして定義。
- **ヘッダーの送信:** カスタムヘッダーをキー/値ペアまたはJSONとして指定。
- **ボディの送信:** POST、PUT、PATCHリクエストで有効化。ボディのコンテンツタイプを選択(form URL-encoded、form-data、JSON、raw、binary)。
- **出力変数:** 出力(ステータスコード、ボディ、ヘッダー)をワークフロー変数にマッピング。

#### 2. 詳細オプション

- **クエリパラメータの配列形式:** 配列エンコーディングを制御(括弧なし、括弧あり、インデックス付き括弧)。
- **バッチ処理:** バッチあたりのアイテム数とバッチ間の遅延。
- **SSL問題を無視:** 信頼できるエンドポイントのみ。
- **ヘッダーを小文字化:** ヘッダー名の大文字小文字を切り替え。
- **リダイレクト:** 有効/無効、最大リダイレクト数を設定。
- **レスポンス処理:** ヘッダー/ステータスを含める、エラーを発生させない、形式を指定(自動、ファイル、JSON、テキスト)。
- **ページネーション:** オフ、パラメータ更新、レスポンス内の次のURL。
- **プロキシ:** HTTPプロキシを指定。
- **タイムアウト:** リクエストタイムアウトをミリ秒で設定。

#### 3. 例: JSONボディを使用したPOSTリクエストの送信

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

### Node-RED HTTPリクエストノード

**公式ドキュメント:**  
[Node-RED HTTPリクエストノード](https://flowfuse.com/node-red/core-nodes/http-request/)  
[Node-RED セキュリティベストプラクティス](https://nodered.org/docs/user-guide/runtime/securing-node-red)

#### ノード設定

- **メソッド:** GET、POST、PUT、DELETE、PATCHなど。
- **URL:** Mustache構文(`{{variable}}`または`{{{variable}}}`)を使用した静的または動的URL。
- **ペイロード:** 無視、クエリ文字列に追加、またはリクエストボディとして送信。
- **認証:** なし、Basic、Digest、Bearerトークン。
- **プロキシ:** 必要に応じてプロキシサーバー経由でリクエストをルーティング。
- **ヘッダー:** ノード設定または`msg.headers`経由でカスタムヘッダーを追加。ノード間でヘッダーの継承を避けるためにリセット。
- **出力:** レスポンスを文字列、パース済みJSON、またはバイナリバッファとして指定。
- **Catchノード:** 2xx以外のHTTPレスポンスを処理。

#### 例: ヘッダー付き動的GETリクエスト

```json
{
  "method": "GET",
  "url": "https://api.example.com/users/{{userId}}",
  "headers": {
    "Authorization": "Bearer {{token}}"
  }
}
```
**ヒント:** HTTPノード間でヘッダーの漏洩を避けるため、`msg.headers`を`{}`にリセットしてください。

### Node.js HTTPリクエスト

#### ネイティブHTTP/HTTPSモジュール

- **http / https**: リクエスト(メソッド、ヘッダー、ボディ、認証)を完全に制御できる低レベルモジュール。
- **ストリーミング:** 大きなペイロードに対する組み込みサポート。
- **プロキシサポート:** 環境変数またはカスタムコード経由。

**ドキュメント:**  
[Node.js HTTPモジュール](https://nodejs.org/api/http.html)  
[W3Schools Node.js HTTPモジュール](https://www.w3schools.com/nodejs/nodejs_http.asp)

#### Fetch API (Node.js 18+)

- **Fetch API**はNode.js 18以降で組み込み。Promiseを返し、async/await構文をサポート。
- **node-fetch**: 以前のNode.jsバージョン用、またはFetchスタイルの構文が必要な場合。

**例: Fetch APIを使用したGETリクエスト**
```js
const response = await fetch('https://api.example.com/data');
const data = await response.json();
console.log(data);
```
[Node.js Fetch APIガイド](https://oxylabs.io/blog/nodejs-fetch-api)

#### axios

- **axios**: Node.jsとブラウザ向けのPromiseベースのHTTPクライアント。
- **機能:** インターセプター、タイムアウト、自動JSON ボディ/レスポンス処理、リクエスト/レスポンス変換、進捗追跡。

**例: axiosを使用したPOSTリクエスト**
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
[Axios ドキュメント](https://axios-http.com/docs/intro)

## ベストプラクティスとヒント

### セキュリティ

- **認証情報の保存:** 組み込みの認証情報マネージャーを使用。シークレットをハードコードしない。
- **HTTPS:** 常にSSL証明書を検証。信頼できる内部エンドポイントのみSSLを無視([Node-RED HTTPS設定](https://nodered.org/docs/user-guide/runtime/securing-node-red#enabling-https-access))。
- **入力のサニタイズ:** すべての動的入力(ヘッダー、パラメータ、ボディ)を検証。
- **トークン管理:** トークンをローテーション、期限切れ、安全に保存。

### エラー処理

- **ステータスコード:** 常にHTTPステータスコードを確認して処理。
- **タイムアウト:** リクエストのハングを避けるため適切なタイムアウトを設定。
- **リトライ:** 一時的な障害(ネットワーク、5xxエラー)に対してリトライを実装。

### コンテンツタイプとエンコーディング

- **Content-Typeヘッダー:** 常にボディ形式と一致させる(`application/json`、`application/x-www-form-urlencoded`)。
- **URLエンコーディング:** 特殊文字を処理するためクエリパラメータをエンコード。
- **配列形式:** クエリパラメータで必要な配列エンコーディングについてAPIドキュメントを確認。

### ページネーション

- **パターン認識:** APIはpage/limit、offset、または次のURLパターンを使用。
- **自動化:** 可能な場合はプラットフォームのページネーション機能を使用。

### ヘッダーとレスポンス処理

- **ヘッダーのリセット:** Node-REDでは、HTTPノード間で`msg.headers`をリセット。
- **ヘッダーの検査:** レート制限、認証チャレンジ、レスポンスヘッダー内のページネーション手がかりを確認。

### プロキシ

- **プロキシ設定:** ネットワークまたはプロバイダーで必要な場合に設定([Node-RED プロキシ設定](https://flowfuse.com/node-red/core-nodes/http-proxy/))。

### デバッグとテスト

- **テストツールの使用:** 組み込みのテスト機能や[Postman](https://www.postman.com/)などのツールで設定を検証。
- **レスポンスのログ:** トラブルシューティングのため完全なレスポンスをキャプチャ。

## よくある落とし穴

- **誤ったContent-Type:** コンテンツタイプの不一致によりAPIが拒否。
- **エンコードされていないクエリパラメータ:** 特殊文字はエンコードが必要。
- **ヘッダーの継承:** Node-REDユーザーは漏洩を避けるためノード間でヘッダーをリセットする必要あり。
- **2xx以外のレスポンスの無視:** 常にステータスコードを確認してエラーを処理。
- **認証の欠落:** ほとんどのAPIは有効な認証情報またはトークンが必要。

## ユースケースと例

### 1. API統合

- **シナリオ:** REST APIからユーザー情報を取得。
- **手順:** GETメソッドを設定、URLを設定、Authorizationヘッダーを追加、レスポンスをマッピング。

### 2. Webサービスへのデータ送信

- **シナリオ:** フォームを送信。
- **手順:** POSTメソッド、Content-Type `application/x-www-form-urlencoded`、フィールドを入力。

### 3. ファイルアップロード

- **シナリオ:** `multipart/form-data`を使用してファイルをアップロード。
- **手順:** POST/PUT、Content-Type `multipart/form-data`、ファイルを添付。

### 4. Webhookトリガー

- **シナリオ:** イベント発生時に外部システムに通知。
- **手順:** POSTメソッド、URLを設定、JSONボディを送信。

### 5. AIエージェントとの自動化 (n8n)

- **シナリオ:** LLMワークフローでHTTPリクエストノードを使用。
- **手順:** ノードを接続、最適化されたレスポンス抽出を設定、フィールドを選択。

### 実例: 天気API用Node-RED HTTPリクエストノード

1. HTTPリクエストノードを挿入。
2. メソッド: GET
3. URL: `https://api.openweathermap.org/data/2.5/weather?q={{city}}&appid={{apiKey}}`
4. 出力: パース済みJSON。
5. 出力をファンクションノードに接続して処理。

### 実例: ページネーション付きn8n HTTPリクエストノード

- `/users`へのGETを設定。
- ページネーションを有効化: リクエストごとにpage/offsetパラメータを更新。
- 結果を集約。

### 実例: Form URLencodedボディを使用したNode.js HTTPS POST

```js
const querystring = require('querystring');
const https = require('https');

const postData = querystring.stringify({
  'username': 'demo',
  'password': 'secret'
});

const options = {
  hostname: 'api.example.com',
  path: '/login',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': Buffer.byteLength(postData)
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    console.log('Status:', res.statusCode);
    console.log('Body:', data);
  });
});

req.on('error', (e) => {
  console.error('Error:', e);
});

req.write(postData);
req.end();
```

## プラットフォーム固有の注意事項

### n8n

- **認証情報:** 事前定義されたOAuth2、APIキー、汎用認証オプション。
- **UI:** ドラッグ&ドロップ、cURLインポート。
- **ボディ/ヘッダー/クエリ:** フィールドまたは直接JSON入力。
- **ページネーション:** パラメータ増分と次のURLをサポート。
- **AIエージェント統合:** LLM向けにレスポンスを最適化。
- **ドキュメント:** [n8n HTTPリクエストノード](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)

### Node-RED

- **動的設定:** `msg.method`、`msg.url`、`msg.headers`を使用。
- **Mustache構文:** 動的URL/ヘッダー用。
- **ペイロード処理:** オブジェクトペイロードの自動Content-Type。
- **レスポンス処理:** 文字列、JSON、バイナリバッファ。
- **セキュリティ:** [Node-REDのセキュリティ保護](https://nodered.org/docs/user-guide/runtime/securing-node-red)
- **ドキュメント:** [Node-RED HTTPリクエストノード](https://flowfuse.com/node-red/core-nodes/http-request/)

### Node.js

- **HTTP/HTTPS:** 低レベル、完全制御。
- **axios/node-fetch/Fetch API:** 高レベル、Promiseベース、簡単なJSONサポート。
- **ストリーミング:** ネイティブサポート。
- **プロキシ:** 環境またはライブラリオプション。
- **ドキュメント:** [Node.js HTTPモジュール](https://nodejs.org/api/http.html)、[Axios ドキュメント](https://axios-http.com/docs/intro)、[Node.js Fetch API](https://oxylabs.io/blog/nodejs-fetch-api)

## 参考資料

- [n8n HTTPリクエストノード ドキュメント](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [n8n HTTPリクエストノードをマスターする](https://automategeniushub.com/mastering-the-n8n-http-request-node/)
- [Node-RED HTTPリクエストノード](https://flowfuse.com/node-red/core-nodes/http-request/)
- [Node-RED セキュリティ保護ガイド](https://nodered.org/docs/user-guide/runtime/securing-node-red)
- [Node.js HTTPモジュール ドキュメント](https://nodejs.org/api/http.html)
- [Axios ドキュメント](https://axios-http.com/docs/intro)
- [Node.js Fetch APIガイド](https://oxylabs.io/blog/nodejs-fetch-api)
- [W3Schools Node.js HTTPモジュール](https://www.w3schools.com/nodejs/nodejs_http.asp)
- [Stack Overflow: Node.jsでのHTTP POST](https://stackoverflow.com/questions/6158933/how-is-an-http-post-request-made-in-node-js)

この用語集は、HTTPリクエストノードに関する包括的で詳細なリファレンスを提供し、設定、認証、サポートされる形式、ベストプラクティス、落とし穴、n8n、Node-RED、Node.jsのプラットフォーム固有のガイダンスを含んでいます。具体的なコード例、トラブルシューティング、高度な統合については、リンクされたドキュメントとリソースを参照してください。