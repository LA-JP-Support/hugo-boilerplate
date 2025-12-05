---
title: Webhook Fulfillment
date: 2025-11-25
translationKey: webhook-fulfillment
description: Webhook fulfillmentは、AIチャットボットや自動化ワークフローにおけるインテントに応答して実行されるバックエンドプロセスです。APIを介してデータを取得・操作し、動的でコンテキストに応じた応答を実現します。
keywords:
- webhook
- fulfillment
- AIチャットボット
- 自動化
- API
category: AI Chatbot & Automation
type: glossary
draft: false
e-title: Webhook Fulfillment
term: ウェブフック フルフィルメント
---

## はじめに

Webhook フルフィルメントは、AI チャットボット、自動化プラットフォーム、および最新の Web アプリケーションで使用される、リアルタイムでイベント駆動型のメカニズムです。ビジネスロジックをバックエンドサービスに委譲するために用いられます。ユーザーメッセージ、インテントマッチ、外部トリガーなどのイベントが発生すると、プラットフォームは指定されたエンドポイントに構造化された HTTP リクエスト(Webhook)を送信します。バックエンドはイベントを処理し、データベースへのクエリ、API の呼び出し、ビジネスワークフローの調整などを行い、動的なレスポンスを返します。このアーキテクチャにより、システムはポーリングや手動介入なしに、パーソナライズされた最新情報を提供し、複雑なワークフローを効率的に実行できます。

- [What Are Webhooks? A Comprehensive Guide for Developers](https://dev.to/robbiecahill/what-are-webhooks-a-comprehensive-guide-for-developers-4l72)
- [Dialogflow ES Fulfillment Webhook Guide](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook)

## 定義

### Webhook

Webhook とは、特定のイベントが発生したときに、ソースシステム(チャットボットや SaaS プラットフォームなど)から公開アクセス可能な URL に送信される自動化された HTTP リクエストです。クライアントが新しいデータをポーリングする従来の API とは異なり、Webhook は「プッシュ」モデルを使用し、イベントがトリガーされるとすぐにリアルタイムでデータを配信します。

> 例:Stripe で決済が完了すると、Stripe は決済詳細を含む HTTP POST リクエストを Webhook エンドポイントに送信します。

- [Red Hat: What is a webhook?](https://www.redhat.com/en/topics/automation/what-is-a-webhook)
- [GetStream: What is a webhook?](https://getstream.io/glossary/webhook/)

### Webhook フルフィルメント(AI チャットボット & 自動化における)

Webhook フルフィルメントは、チャットボットや自動化システムによって検出されたイベントまたはインテントに応答して実行されるバックエンドプロセスです。Webhook ハンドラーは通常、イベントを記述する JSON ペイロードを受信し、ビジネスロジック(API 呼び出し、計算、データベース検索など)を実行し、構造化されたレスポンスを返します。これにより、チャットボットや自動化ワークフローは、動的でコンテキストに応じた結果を提供できます。

> 例:ユーザーが銀行チャットボットに残高を尋ねると、チャットボットは Webhook フルフィルメントをトリガーし、銀行 API にクエリを実行して、チャットで残高を返します。

- [Dialogflow ES Fulfillment Webhook](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook)
- [Webhooks in Chatbot](https://www.chatbot.com/help/webhooks/what-are-webhooks/)

### ペイロード

ペイロードは、Webhook の HTTP リクエストまたはレスポンスボディに含まれるデータです。ペイロードは最も一般的に JSON 形式ですが、XML やフォームデータが使用されることもあります。ペイロードには、トリガーイベント、コンテキスト、ユーザー/セッション、および処理に必要な関連パラメータに関する構造化情報が含まれます。

> 例:
> ```json
> {
>   "event": "order.completed",
>   "data": {
>     "order_id": "12345",
>     "amount": 99.99
>   }
> }
> ```

### イベント駆動型アーキテクチャ

イベント駆動型アーキテクチャは、コンポーネントがスケジュールされたポーリングに依存するのではなく、変化(イベント)に対して通信し反応するシステム設計パターンです。Webhook は、イベント駆動型ワークフローを実装するための主要なメカニズムであり、分散システム全体で即座にプッシュベースの更新を提供します。

> 例:CRM システムは、新しいリードが作成されるとすぐに、Webhook を使用してマーケティングツールに自動的に同期します。

- [What is Event-driven Architecture? (Red Hat)](https://www.redhat.com/en/topics/integration/what-is-event-driven-architecture)

## Webhook vs. API/ポーリング

Webhook と API はどちらもシステム統合に使用されますが、データの転送方法とタイミングが根本的に異なります。

- **Webhook(プッシュ):** イベントが発生すると、データが自動的にエンドポイントに配信されます。
- **API ポーリング(プル):** システムが定期的にサーバーからデータをリクエストして更新を確認します。

ポーリングはリソース集約的で[レイテンシ](/en/glossary/latency/)が発生しますが、Webhook は最小限のオーバーヘッドで、ほぼ瞬時の効率的な通信を提供します。

### 比較表

| 機能              | Webhook(プッシュ)               | API ポーリング(プル)           |
|----------------------|------------------------------|------------------------------|
| データフロー            | サーバーからクライアント(イベントベース) | クライアントからサーバー(スケジュール)  |
| トリガーメカニズム    | イベント駆動型                 | クライアント主導             |
| レイテンシ              | ほぼリアルタイム               | 間隔依存           |
| 効率性           | 高(イベント時のみ)            | 低(頻繁/空のリクエスト)|
| スケーラビリティ          | ステートレス、簡単なエンドポイント    | レート制限が必要        |
| セットアップ                | エンドポイント URL を登録        | スケジュールされたポーリングを実装   |
| エラーハンドリング       | リトライ、ステータスコード        | クライアントが失敗を処理       |
| セキュリティ             | HMAC、[シークレット](/en/glossary/environment-variables--secrets-/)、mTLS、HTTPS   | API キー、OAuth、HTTPS        |
| ユースケース            | 通知、統合  | 一括クエリ、定期同期   |

- [Webhooks vs. APIs: A Clear Comparison](https://dev.to/robbiecahill/what-are-webhooks-a-comprehensive-guide-for-developers-4l72)

## Webhook フルフィルメントの仕組み

Webhook フルフィルメントは通常、次のステップに従います。

### ライフサイクルステップ

1. **イベントトリガー:**  
   イベントが発生します(例:インテントマッチ、ユーザーアクション、データ更新)。

2. **Webhook リクエスト:**  
   ソースシステムは、登録された Webhook エンドポイントに HTTPS POST リクエストを送信します。ペイロードには、イベントの詳細と関連するコンテキストが含まれます。

3. **ペイロード処理:**  
   Webhook ハンドラーは真正性を検証し、ペイロードを解析し、ビジネスロジック(API 呼び出し、DB クエリ、計算)を実行します。

4. **レスポンス生成:**  
   Webhook ハンドラーは、フルフィルメント結果を含む HTTP レスポンス(通常は JSON)を返します。

5. **確認と承認:**  
   ソースシステムは、成功を確認するために 2xx HTTP ステータスコードを期待します。受信されない場合、ポリシーに従って配信を再試行します。

6. **リトライとエラーハンドリング:**  
   ハンドラーが失敗または利用できない場合、ソースは指数バックオフまたは固定回数の試行で再試行します。

**ビジュアルフロー:**
```
[ユーザーアクション/インテント]
      |
      v
[チャットボット/自動化プラットフォーム]
      |
      v    (HTTP POST)
[Webhook フルフィルメントエンドポイント]
      |
      v
[外部 API/データベース]
      |
      v
[プラットフォームへのレスポンス]
      |
      v
[ユーザーが動的レスポンスを受信]
```

### ペイロード例

**Webhook リクエスト(JSON 例):**
```json
{
  "event": "intent_matched",
  "intent": "GetAccountBalance",
  "session": {
    "id": "abc123",
    "parameters": { "user_id": "456" }
  },
  "timestamp": "2025-06-24T12:34:56Z"
}
```

**Dialogflow リクエスト例:**  
[Dialogflow WebhookRequest リファレンス](https://cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#webhookrequest)を参照
```json
{
  "responseId": "response-id",
  "session": "projects/project-id/agent/sessions/session-id",
  "queryResult": {
    "queryText": "End-user expression",
    "parameters": {
      "param-name": "param-value"
    }
  }
}
```

**Webhook レスポンス(JSON 例):**
```json
{
  "fulfillmentText": "Your current account balance is $1,250.",
  "parameters": { "balance": 1250 }
}
```

## 技術的詳細

### プロトコルとペイロード形式

- **プロトコル:** セキュリティのため HTTPS が必須です。
- **HTTP メソッド:** POST が標準(柔軟なシナリオでは GET/PATCH/PUT も可能)。
- **ペイロード:** JSON が標準形式です。レガシーシステムでは XML や URL エンコードされたフォームが使用されることもあります。
- **ヘッダー:**  
  - `Content-Type: application/json`  
  - `Authorization: Bearer <token>` または認証用のカスタムヘッダー  
  - HMAC 検証用の署名ヘッダー

- [Dialogflow Webhook Requirements](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook)

### 認証とセキュリティ

不正アクセスや偽装リクエストを防ぐため、Webhook エンドポイントのセキュリティ確保は不可欠です。

- **HTTPS 必須:** 転送中のデータは常に暗号化する必要があります。  
  [Why HTTPS? (Google Support)](https://support.google.com/domains/answer/7630973)

- **認証メカニズム:**
    - **認証ヘッダー:** `Authorization` ヘッダー内の静的または動的トークン。
    - **Basic 認証:** ユーザー名/パスワード、base64 エンコード。
    - **OAuth:** 管理された API 用の OAuth2 Bearer トークン。
    - **サービス ID トークン:** クラウドシステム用(例:Google Cloud)。
    - **相互 TLS(mTLS):** 両側が SSL 証明書を提示。
    - **HMAC 署名:** 共有シークレットがペイロードに署名し、ハンドラーが検証。
- **検証:** 受信リクエストのデジタル署名またはトークンを常に検証します。
- **IP 許可リスト:** 使用されることもありますが、動的なクラウド IP のため信頼性が低い場合があります。

- [Webhook Security Guide (Hookdeck)](https://hookdeck.com/webhooks/guides/complete-guide-to-webhook-security)
- [Dialogflow Authentication Options](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook#authentication)

### タイムアウト、リトライ、冪等性

- **タイムアウト:**  
  ハンドラーは迅速に応答する必要があります(多くの場合 1〜10 秒以内)。長時間実行される作業はオフロードする必要があります。
- **リトライ:**  
  プロデューサーは、指数バックオフで失敗した配信を最大試行回数まで再試行します。
- **冪等性:**  
  ハンドラーは冪等である必要があります。同じイベントを複数回処理しても、意図しない影響が発生しないようにします。一意のイベント ID を使用して重複を検出し、スキップします。

- [Implementing a Webhook: Step-by-Step Guide](https://racklify.com/encyclopedia/implementing-a-webhook-a-step-by-step-beginner-guide/)

### 非同期 vs. 同期処理

- **同期:**  
  ハンドラーは即座に処理して結果を返します(例:決済確認)。
- **非同期:**  
  ハンドラーは受信を迅速に承認し、バックグラウンドで作業を実行します。Webhook タイムアウトウィンドウよりも長くかかるタスクに便利です。

## 実装と設定

### セットアップ手順

1. **イベントトリガーの定義:**  
   Webhook 呼び出しをトリガーするイベント(インテントマッチ、ページ遷移)を特定します。

2. **Webhook ハンドラーの開発:**  
   HTTPS リクエストを受信して処理するバックエンドサービス(Node.js、Python、Java など)を実装します。署名/トークンを検証することを確認します。

3. **ハンドラーのデプロイ:**  
   公開アクセス可能なエンドポイントでホストします。サーバーレス(AWS Lambda、Google Cloud Functions)または従来のサーバーを使用します。常に HTTPS 経由で提供します。

4. **Webhook の登録:**  
   チャットボット/自動化プラットフォームで、Webhook URL、HTTP メソッド、認証、必要なパラメータを設定します。

5. **ペイロード/レスポンスマッピングの設定:**  
   送信および期待するパラメータを指定します。

6. **統合のテスト:**  
   ngrok や Tunnelmole などのツールを使用して、テスト用にローカルサーバーを公開します。

- [Implementing a Webhook: Step-by-Step Guide (Racklify)](https://racklify.com/encyclopedia/implementing-a-webhook-a-step-by-step-beginner-guide/)
- [Testing Webhooks Locally with ngrok](https://ngrok.com/)

### 設定パラメータ

| パラメータ         | 説明                                   |
|-------------------|-----------------------------------------------|
| Webhook URL       | リクエストを受信するエンドポイント                  |
| HTTP メソッド       | POST(標準)、サポートされている場合は他のメソッド          |
| リクエストボディ      | JSON 構造、イベント/セッションパラメータを含む |
| 認証    | トークン、OAuth、mTLS など                      |
| タイムアウト           | レスポンスの最大待機時間(例:5 秒)       |
| レスポンスマッピング  | レスポンスフィールドをセッションパラメータにマッピング    |
| 環境       | テスト/本番環境の設定を分離              |
| カスタムヘッダー    | 認証/セキュリティ用の追加 HTTP ヘッダー          |

### サンプルコードスニペット

**Express(Node.js)例:**
```js
const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhook', (req, res) => {
  const { event, session } = req.body;
  // 例:外部 API からユーザーデータを取得
  fetchUserBalance(session.parameters.user_id)
    .then(balance => {
      res.json({
        fulfillmentText: `Your current balance is $${balance}.`,
        parameters: { balance }
      });
    })
    .catch(() => {
      res.status(500).json({ fulfillmentText: 'Unable to fetch balance.' });
    });
});

function fetchUserBalance(userId) {
  // API 呼び出しをシミュレート
  return Promise.resolve(1250);
}

app.listen(3000, () => console.log('Webhook listening on port 3000'));
```

**署名検証(疑似コード):**
```python
import hmac
import hashlib

def verify_signature(secret, payload, signature):
    computed = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)
```

**パラメータ付き柔軟な Webhook URL:**
```
https://api.example.com/webhook?user_id=$session.params.user_id
```

- [Dialogflow Webhook Code Samples](https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook#example)

## 実用的なユースケース

Webhook フルフィルメントは、多数の自動化シナリオを可能にします。

- **AI チャットボット:**
    - ユーザープロファイル/アカウントデータをリアルタイムで取得。
    - ユーザー入力を検証(例:プロモーションコード)。
    - コンテキストに応じたパーソナライズされたレスポンスを提供。
    - ユーザーステータスによって会話をルーティング(例:VIP ルーティング)。
- **決済 & E コマース:**
    - 注文が作成、支払い、または出荷されたときにシステムに通知。
    - 在庫を更新またはフルフィルメントプロセスをトリガー。
- **CRM & マーケティング:**
    - 連絡先/リードデータをサードパーティツールと即座に同期。
    - ユーザーアクションに基づいてマーケティングキャンペーンをトリガー。
- **IT & DevOps 自動化:**
    - コードマージ時にインフラストラクチャの変更を開始。
    - CI/CD、監視、またはインシデント管理ワークフローを統合。
- **ワークフローオーケストレーション:**
    - ダウンストリームシステムをトリガーして、複数ステップのプロセスをチェーン。
    - 新しいデータが到着したときにデータパイプラインまたは分析プロセスを開始。

- [Dialogflow Fulfillment Use Cases](https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook)
- [Webhooks in ChatBot](https://www.chatbot.com/help/webhooks/what-are-webhooks/)

## ベストプラクティス

**セキュリティ:**
- 傍受を防ぐため、常に HTTPS を使用します。
- リクエスト署名または認証トークンを検証します。
- 認証なしでエンドポイントを公開しないでください。

**信頼性:**
- 送信側と受信側の両方でリトライロジックを実装します。
- イベント ID を追跡して冪等性を確保します。
- 遅いタスクにはキュー/バックグラウンドワーカーを使用します。

**パフォーマンス:**
- Webhook に迅速に応答し、重い作業を延期します。
- エンドポイントの健全性を監視し、すべてのリクエスト/失敗をログに記録します。

**スケーラビリティ:**
- 高負荷にはロードバランサー/分散インフラストラクチャを使用します。
- 処理前に受信イベントをデータベースまたはキューに永続化します。

**保守性:**
- Webhook エンドポイントのドキュメントを最新の状態に保ちます。
- テスト環境と本番環境を分離します。
- 下位互換性のためにペイロードをバージョン管理します。

- [Webhook Security Guide (Hookdeck)](https://hookdeck.com/webhooks/guides/complete-guide-to-webhook-security)
- [Implementing a Webhook: Step-by-Step Guide (Racklify)](https://racklify.com/encyclopedia/implementing-a-webhook-a-step-by-step-beginner-guide/)

## よくある質問

**Webhook と API は同じですか?**  
いいえ。Webhook はサーバー主導の HTTP リクエスト(イベント駆動型)であり、API はクライアント主導(リクエスト/レスポンス)です。Webhook は変更を通知し、API はデータのクエリまたは更新を可能にします。

**Webhook エンドポイントがダウンしている場合はどうなりますか?**  
ソースシステムは、リトライポリシーに従って配信を再試行します。リトライ制限を超えて利用できない場合、イベントが失われる可能性があります。

**Webhook ペイロードはカスタマイズできますか?**  
多くのプラットフォームは、柔軟なペイロードとパラメータマッピングをサポートしています。

**ローカルで Webhook フルフィルメントをテストするにはどうすればよいですか?**  
[ngrok](https://ngrok.com/) や [Tunnelmole](https://tunnelmole.com/) などのトンネリングツールを使用して、ローカルサーバーを公開します。

**重複処理を回避するにはどうすればよいですか?**  
一意のイベント ID を追跡し、冪等性のために繰り返されるイベントを無視します。

**どのペイロード形式がサポートされていますか?**  
JSON が標準です。XML またはフォームエンコードされたデータが使用されることもあります。

**Webhook エンドポイントをセキュリティで保護するにはどうすればよいですか?**  
HTTPS を使用し、HMAC 署名またはトークンを検証し、可能であれば IP を制限します。

## 参考文献 & 参考資料

- [Google Dialogflow ES Webhooks Documentation](https://docs.cloud.google.com/dialogflow/es