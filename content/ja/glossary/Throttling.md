---
title: スロットリング（APIスロットリング）
date: 2025-11-25
translationKey: throttling-api-throttling
description: スロットリング（APIスロットリングとも呼ばれる）は、特定の期間内にAPIやサービスへのリクエストを意図的に制限することです。過負荷を防ぎ、公平なアクセスを保証し、悪用を抑制し、パフォーマンスを維持します。
keywords:
- APIスロットリング
- レート制限
- トークンバケット
- APIゲートウェイ
- システム保護
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Throttling (API Throttling)
term: すろっとりんぐ（えーぴーあいすろっとりんぐ）
reading: スロットリング（APIスロットリング）
kana_head: か
---
## 簡潔な要約 / 定義

**Throttling**(スロットリング)は、*APIスロットリング*とも呼ばれ、特定の期間内にユーザー、クライアント、またはアプリケーションがAPIやサービスに対して行えるリクエスト数を意図的に制限することです。スロットリングは、バックエンドの過負荷を防ぎ、公平なアクセスを保証し、悪用を抑制し、受信トラフィックのフローを管理・平準化することで一貫したサービスパフォーマンスを維持するために不可欠です。

- [AWS API Gateway Throttling Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [Gravitee: API Throttling Best Practices](https://www.gravitee.io/blog/api-throttling-best-practices)
- [Knit.dev: 10 Best Practices for API Rate Limiting and Throttling](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

## スロットリングの重要性 / ユースケース

**スロットリングは以下の重要な目的を果たします:**

- **システム保護:** トラフィックの急増、偶発的な誤用、または意図的な攻撃からバックエンドサービスを保護し、パフォーマンス低下や障害を防ぎます。例えば、AWSはインフラストラクチャの過負荷を防ぐため、複数のシステムレベルでハードおよびソフトスロットリングを適用しています([出典](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html))。
- **公平な利用:** 単一のユーザーやクライアントがAPIリソースを独占できないようにし、すべての利用者に公平なアクセスを保証します([Gravitee](https://www.gravitee.io/blog/api-throttling-best-practices))。
- **セキュリティ:** リクエストの受け入れレートに上限を設けることで、悪意のある攻撃者がサービス拒否(DoS/DDoS)攻撃を仕掛ける能力を制限します([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling))。
- **パフォーマンスの安定性:** 変動の大きい負荷やバースト的な負荷の下でも、予測可能で安定したAPIレスポンスタイムを維持します。
- **収益化と計測:** 無料プランと有料プランの利用クォータを設定し、差別化された価格設定とサービス階層を可能にします。
- **リソース管理:** 需要を平準化し、同時ワークロードを制限することで、バックエンドリソース(データベース、キャッシュ、GPUなど)の枯渇を防ぎます。

**実際の例:**

- **ソーシャルAPI:** Twitterは、スパムを抑制しプラットフォームの安定性を保護するため、ユーザーごとに15分間のウィンドウでAPI使用を制限しています([Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api/rate-limits))。
- **予約エンジン:** オンライン旅行代理店は、上流のサービス中断を避けるため、航空会社の予約システム(Sabre、Amadeusなど)への呼び出しをスロットリングします。
- **クラウドストレージ:** AWS S3は、すべてのテナントに一貫したパフォーマンスを提供するため、リクエストクォータを適用しています([AWS S3 Limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html))。
- **AI API:** 画像認識や大規模言語モデルのAPIは、GPUコストを管理し[推論レイテンシ](/en/glossary/inference-latency/)を維持するため、ユーザーごとまたはアプリごとのスロットリングを適用します([Gravitee](https://www.gravitee.io/blog/api-throttling-best-practices))。

## スロットリングの仕組み

**スロットリングメカニズムには以下が含まれます:**

1. **レート制限:** 定義された時間内にユーザー、クライアント、またはAPIキーごとに許可される最大リクエスト数を設定します(例:1,000リクエスト/時間)。
2. **バースト制限:** 持続レートを超える短期的なスパイクを閾値まで許可します(例:1秒間に100リクエスト、平均は10/秒に制限)。
3. **エラーコード:** 制限を超えると、HTTPステータスコード`429 Too Many Requests`エラーレスポンスが返されます([RFC 6585](https://datatracker.ietf.org/doc/html/rfc6585#section-4))。
4. **リトライガイダンス:** APIは`Retry-After`ヘッダーを返し、クライアントにいつリトライすべきかを指示します。
5. **適用レベル:** スロットリングは、ユーザーごと、APIキーごと、アプリごと、リージョンごと、またはグローバルに適用でき、多くの場合APIゲートウェイまたはバックエンドで実施されます。

**スロットリングフロー:**

1. クライアントがAPIにリクエストを送信します。
2. システムは、設定された閾値(トークンバケット、カウンター、またはキューを使用)に対してリクエスト数とタイミングをチェックします。
3. 制限内の場合:リクエストが処理されます。制限を超えている場合:`429`エラーが返され、`Retry-After`、`X-RateLimit-Remaining`などのヘッダーが含まれます。
4. クライアントは、バックオフ戦略(リクエストの遅延、リトライ、または[バッチ処理](/ja/glossary/batch-processing/))を実装できます。

**レスポンス例:**

```http
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1712345678
Retry-After: 60
Content-Type: application/json

{
  "error": "Rate limit exceeded. Please wait 60 seconds before retrying."
}
```

- [AWS: How Throttling Works](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

## タイプとアルゴリズム

### 1. トークンバケットアルゴリズム

**メカニズム:**  
バケットが固定レートでトークンを蓄積します。各リクエストはトークンを消費します。トークンが利用可能な場合のみリクエストが処理され、短期的なバーストを許可しながら、時間経過に伴う持続的な平均レートを適用します。

- **長所:** バーストを許可、柔軟な調整、実装が簡単。
- **短所:** 設定ミスによりスパイクが発生する可能性。
- **類推:** 水滴(トークン)で満たされる水バケット。リクエストが水滴をすくい出す。空の場合は補充を待つ必要がある。

- [AWS Token Bucket Explanation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

**疑似コード:**
```python
def allow_request():
    now = current_time()
    bucket.tokens += (now - bucket.last_check) * bucket.refill_rate
    bucket.tokens = min(bucket.tokens, bucket.capacity)
    bucket.last_check = now
    if bucket.tokens >= 1:
        bucket.tokens -= 1
        return True
    else:
        return False
```

**例:** 株式市場API:100リクエストのバースト、10/秒で補充。

### 2. リーキーバケットアルゴリズム

**メカニズム:**  
リクエストは固定サイズのキュー(「バケット」)に入ります。リクエストは一定のレートで処理されます。バケットが満杯の場合、新しいリクエストは破棄または遅延されます。

- **長所:** バーストを平準化、安定した流出を保証。
- **短所:** [レイテンシ](/en/glossary/latency/)を導入したり、バースト的なトラフィックを破棄する可能性。
- **類推:** 穴の開いたバケット—任意のレートで水が入り、一定のレートで漏れ出る。

**例:** メールAPIは1分間に最大100通のメールをキューに入れ、一定のレートで送信。

### 3. 固定ウィンドウアルゴリズム

**メカニズム:**  
固定された間隔(例:分/時間)内のリクエストをカウントします。カウンターはウィンドウの境界でリセットされます。

- **長所:** 実装が簡単。
- **短所:** ウィンドウの境界でスパイクが発生しやすい。

**例:** Twitterは、ユーザーごとに15分間のウィンドウで300リクエストを許可。

### 4. スライディングウィンドウアルゴリズム

**メカニズム:**  
ローリングウィンドウ(例:過去60秒)内のリクエストを追跡し、より細かい制御を行い、バーストを平準化します。

- **長所:** ウィンドウの端でのバースト性を防ぐ。
- **短所:** タイムスタンプの追跡が必要で、より複雑。

**例:** SaaS APIは、ローリング60秒あたり100リクエストを許可。

### 5. 同時リクエスト制限

**メカニズム:**  
クライアントごとの同時(実行中)リクエスト数を制限します。

- **長所:** 並列ワークロードによるリソース枯渇を防ぐ。
- **短所:** 時間経過に伴う総リクエスト数は制限しない。

**例:** 画像処理APIは、クライアントごとに最大5つの同時リクエストを許可。

### 6. ハードスロットリング vs. ソフトスロットリング

- **ハードスロットリング:** 厳格な適用。超過リクエストは拒否(例:無料APIティア、重要なインフラストラクチャ)。
- **ソフトスロットリング:** 一時的な超過を許可、またはバックエンド容量に基づいてキュー/超過リクエストを処理。

### 7. ユーザーレベル vs. システムレベルスロットリング

- **ユーザーレベル:** 公平性のため、ユーザー/クライアント/APIキーごとに制限。
- **システムレベル:** インフラストラクチャ全体の健全性を確保するためのグローバル制限。

- [Gravitee: API Throttling Techniques](https://www.gravitee.io/blog/api-throttling-best-practices)

## 実装のベストプラクティス

**堅牢なスロットリングのための実践的なガイドライン:**

1. **きめ細かい制限:**  
   - 複数のレベル(ユーザー、APIキー、エンドポイント、リージョン)で設定。
   - 複数の時間ウィンドウ(秒/分/時間/日ごと)を使用。
   - [AWS: Per-client, per-method, per-stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html#apigateway-method-level-throttling-in-usage-plan)。

2. **分散カウンター:**  
   - 分散システムでは、Redisなどの集中ストアをカウンターに使用([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling))。

3. **明確なエラーメッセージ:**  
   - 常にHTTP `429`を返し、制限、残りクォータ、リセット時間(`Retry-After`)のヘッダーを含める。
   - ヘッダー例:`X-RateLimit-Limit`、`X-RateLimit-Remaining`、`X-RateLimit-Reset`、`Retry-After`。

4. **リトライ戦略:**  
   - サンダリングハード問題を避けるため、ジッターを伴う指数バックオフの使用をクライアントに推奨。

5. **APIゲートウェイ統合:**  
   - AWS API Gateway、Kong、Graviteeなどのプラットフォームを使用して、集中ポリシー管理と分析を実現([Gravitee](https://www.gravitee.io/platform/api-gateway))。

6. **監視と調整:**  
   - 使用状況、エラー率、システムの健全性を継続的に監視し、必要に応じて閾値を調整([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling))。

7. **透明性:**  
   - スロットリングポリシーを明確に文書化し、更新を伝達。可能であれば使用状況ダッシュボードを提供。

**トークンバケットの例(Python):**
```python
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_checked = time.time()
    
    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_checked
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_checked = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False
```
- [Knit.dev: Best Practices](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

## よくある落とし穴とミス

**頻繁に発生するエラー:**

- **不適切な制限設定:**  
  - 低すぎる:正当なユーザーをブロックし、エクスペリエンスを損なう。
  - 高すぎる:バックエンドを保護できず、障害のリスクがある([AWS Guidance](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html))。

- **不十分な監視:**  
  - リアルタイム分析がないと、悪用やパフォーマンス低下が見過ごされる可能性。

- **不明確なエラー処理:**  
  - 曖昧または欠落した`429`レスポンスは、API利用者を混乱させる。

- **ドキュメントの欠如:**  
  - スロットリングポリシーを伝えないと、開発者の不満や予測不可能な障害につながる。

- **リトライガイダンスの欠如:**  
  - `Retry-After`が欠落していると、不要なトラフィックと不適切なクライアント動作につながる。

- **分散システムの無視:**  
  - マルチノード環境でのローカルカウンターは、不正確な適用につながる([Knit.dev](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling))。

**対策:**

- 負荷テストを実施して閾値を調整。
- 集中化されたアトミックカウンターを使用。
- レスポンスに常にレート制限情報を含める。
- 制限とエラー処理を文書化して伝達。
- 実際の使用状況に基づいて定期的にレビューと調整を実施。

## FAQとさらなる参考資料

**よくある質問:**

**Q1:** スロットリング制限を超えるとどうなりますか?  
**A:** APIはHTTP `429 Too Many Requests`エラーを返し、多くの場合クールダウン期間を示すヘッダーが含まれます。クライアントは、クールダウンを待つか、リトライする前に`Retry-After`値を使用する必要があります。  
- [RFC 6585, Section 4](https://datatracker.ietf.org/doc/html/rfc6585#section-4)

**Q2:** クライアントはスロットリング制限に達するのをどのように回避できますか?  
**A:** リクエストパターンを最適化([バッチ処理](/ja/glossary/batch-processing/)、キャッシング)し、レート制限ヘッダーに従い、指数バックオフとジッターを伴うリトライロジックを実装します。  
- [Knit.dev: Retry Strategies](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

**Q3:** スロットリングとレート制限の違いは何ですか?  
**A:** レート制限はリクエスト上限を定義するポリシーです。スロットリングは、健全性を維持するためにリクエストを拒否または遅延させる適用です。

**Q4:** スロットリングは動的にできますか?  
**A:** はい、動的スロットリングは、リアルタイムのサーバー負荷や時間帯に基づいて制限を調整しますが、実装はより複雑です。

**Q5:** エラーレスポンスはどのように構造化すべきですか?  
**A:** HTTP `429`を返し、関連するヘッダー(`X-RateLimit-Limit`、`X-RateLimit-Remaining`、`X-RateLimit-Reset`、`Retry-After`)と明確なボディメッセージを含めます。

**さらなる参考資料:**

- [Throttle requests to your REST APIs for better throughput in API Gateway – AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [API Throttling Best Practices & Techniques – Gravitee Blog](https://www.gravitee.io/blog/api-throttling-best-practices)
- [What is Rate Limiting / API Throttling? – YouTube Explainer](https://www.youtube.com/watch?v=9CIjoWPwAhU)
- [What is API Throttling? – TIBCO Glossary](https://www.tibco.com/glossary/what-is-api-throttling)
- [API Throttling – GetStream Glossary](https://getstream.io/glossary/api-throttling/)
- [Knit.dev: 10 Best Practices for API Rate Limiting and Throttling](https://www.getknit.dev/blog/10-best-practices-for-api-rate-limiting-and-throttling)

## 要約表:スロットリングアルゴリズム

| アルゴリズム           | バースト許可 | 厳格な制限 | 複雑さ | ユースケース例                |
|---------------------|:-------------:|:------------:|:----------:|---------------------------------|
| トークンバケット        | はい           | いいえ           | 中程度     | トレーディングAPI、クラウドサービス    |
| リーキーバケット        | いいえ            | はい          | 中程度     | メール送信者、Webクローラー     |
| 固定ウィンドウ        | はい(端で) | はい          | 低     | Twitter API、天気API       |
| スライディングウィンドウ      | やや      | はい          | 高       | SaaS API、マイクロサービス        |
| 同時制限 | N/A           | はい          | 低        | DB接続、GPUワークロード   |

## シナリオ例:AIインフラストラクチャにおけるスロットリング

ある企業が公開AI画像認識APIを運用しています:

- **トークンバケット**: バーストで50リクエストを許可、5リクエスト/秒で補充。
- **同時制限**: GPU過負荷を防ぐため、クライアントごとに実行中のリクエストは10個まで。
- **システムレベルスロットリング**: GPUクラスター全体を保護するためのグローバル上限。
- **エラー処理**: 制限を超えると`429`レスポンスと`Retry-After`ヘッダーが返される。すべての使用状況は分析のために追跡される。

## 重要なポイント

- **スロットリング**は、APIを保護し、公平性を確保し、AIやその他のサービスの信頼性を維持します。
- 堅牢なエラー処理、透明なコミュニケーション、継続的な監視を実装します。
- ユースケースに応じて適切なアルゴリズムと制限を選択。APIゲートウェイは、適用の集中化とスケーリングに役立ちます。

**より詳細なガイダンスとコードサンプルについては、[AWS API Gateway Throttling Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)および[GraviteeのAPI Throttling Best Practices](https://www.gravitee.io/blog/api-throttling-best-practices)を参照してください。**

この用語集は、AWS、Gravitee、Knit.devなどの権威ある業界ドキュメントとベストプラクティスガイドに基づいています。詳細なビデオ紹介については、以下を参照してください:[What is Rate Limiting / API Throttling? (YouTube)](https://www.youtube.com/watch?v=9CIjoWPwAhU)