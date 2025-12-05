---
title: レイテンシ
date: 2025-11-25
translationKey: latency
description: レイテンシとは、リクエストとシステムの応答との間の時間遅延のことで、AIインフラストラクチャ、Webアプリケーション、リアルタイムシステムにおいて重要な要素です。その種類、原因、削減戦略について解説します。
keywords:
- レイテンシ
- AIインフラストラクチャ
- ネットワークレイテンシ
- パフォーマンス最適化
- リアルタイムシステム
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Latency
term: れいてんし
---
## レイテンシとは何か?

レイテンシとは、プロセスの開始から完了までに発生する時間遅延のことです。ネットワークシステムやAIインフラストラクチャにおいては、データがある地点から別の地点へ移動するのにかかる時間を指し、最も一般的にはユーザーのアクションとシステムの応答との間の遅延として測定されます。通常、レイテンシはミリ秒(ms)で定量化され、ユーザーがWebアプリ、API、またはAI駆動型サービスとのやり取り中に感じる「ラグ」を表します。

**主要な定義:**  
> レイテンシとは、リクエストの開始(Webアプリのボタンをクリックするなど)からシステムまたはアプリケーションからの応答を受信するまでに発生する遅延を指します。

- **出典:** [Galileo AI: Understanding Latency in AI](https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works)
- **出典:** [AWS: What Is Latency?](https://aws.amazon.com/what-is/latency/)
- **出典:** [DriveNets: Latency in AI Networking](https://drivenets.com/blog/latency-in-ai-networking-inevitable-limitation-to-solvable-challenge/)

## デジタルシステムにおいてレイテンシが重要な理由

レイテンシは、ユーザーエクスペリエンス、アプリケーションパフォーマンス、デジタルインフラストラクチャの有効性に直接影響します。AIインフラストラクチャとデプロイメントにおいて、低レイテンシは以下の点で不可欠です:

- レスポンシブなWebおよびモバイルアプリケーション
- リアルタイム分析と意思決定
- AI駆動型検索と検索
- [クラウドコンピューティング](/en/glossary/cloud-computing/)とAPI統合
- 高頻度取引(HFT)と金融システム
- 遠隔医療、リモートモニタリング、医療アプリケーション
- オンラインゲームとインタラクティブメディア

**例:**
- 高頻度取引では、1ミリ秒の遅延が利益と損失の分かれ目になることがあります。  
  [参照: Investopedia on HFT Latency](https://www.investopedia.com/terms/h/high-frequency-trading.asp)
- AI駆動型チャットボットでは、高レイテンシが会話体験を低下させ、応答が遅く不自然に感じられます。
- 自動運転車では、わずかな遅延でも安全上のリスクをもたらす可能性があります([Galileo AI](https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works))。

## レイテンシの種類

デジタルシステムにおけるレイテンシは、いくつかの形態で現れます:

- **ネットワークレイテンシ:** データが送信者から受信者へネットワーク上を移動するのにかかる時間。物理的距離、伝送媒体、ネットワーク輻輳の影響を受けます。
- **検索レイテンシ:** クエリ後にシステム(例:AIモデル)がストレージまたはナレッジベースから関連データを取得するのにかかる時間。
- **ディスク/ストレージレイテンシ:** ストレージデバイスからのデータの読み書きにおける遅延。SSDはHDDよりも低レイテンシです。
- **オペレーショナル/コンピュートレイテンシ:** アプリケーションまたはサーバー処理によって導入される遅延。複雑なAIモデルや非効率的なアルゴリズムはコンピュートレイテンシを増加させます。

AIパイプラインでは、複数のレイテンシタイプが複合し、システム全体の応答性に影響を与えます。

- **出典:** [Galileo AI](https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works)
- **出典:** [DriveNets](https://drivenets.com/blog/latency-in-ai-networking-inevitable-limitation-to-solvable-challenge/)

## レイテンシはどのように使用または遭遇されるか?

レイテンシは、以下の設計、デプロイメント、運用における主要な懸念事項です:

- **AIモデル推論:** ユーザー入力から出力生成までの時間。
- **API統合:** 外部または内部サービス呼び出しにおける遅延。
- **データベース/検索検索:** 関連情報を取得する速度。
- **ネットワークアプリケーション:** 高速フィードバックを必要とするWeb、モバイル、IoTアプリ。

**例:**  
検索拡張生成(RAG)パイプラインでは、検索レイテンシがAIモデルの応答を通知するためにドキュメントや事実がどれだけ迅速に取得されるかを決定します。  
[参照: AI21 Labs on Retrieval Latency](https://www.ai21.com/glossary/foundational-llm/retrieval-latency/)

## 実用例とユースケース

### 1. ゲーミング
- **重要性:** マルチプレイヤーオンラインゲームは、リアルタイムインタラクションのために最小限のレイテンシを必要とします。
- **影響:** 高レイテンシはラグを引き起こし、ゲームプレイとユーザー満足度に深刻な影響を与えます。
  - [Fortinet: Gaming and Network Latency](https://www.fortinet.com/resources/cyberglossary/latency)

### 2. 金融と高頻度取引(HFT)
- **重要性:** 自動取引システムは、マイクロ秒が重要な注文を実行します。
- **影響:** わずかなレイテンシでも、重大な財務損失や機会損失につながる可能性があります。
  - [Investopedia: HFT](https://www.investopedia.com/terms/h/high-frequency-trading.asp)

### 3. クラウドベースのWebアプリケーション
- **重要性:** ユーザーは即座のロードとシームレスなインタラクションを期待します。
- **影響:** 遅いAPI応答やデータベースクエリはアプリケーションパフォーマンスを低下させます。
  - [MDN: Understanding Latency](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Understanding_latency)

### 4. 医療
- **重要性:** 遠隔医療、遠隔手術、臨床データ検索は、安全性と有効性のために低レイテンシを必要とします。
- **影響:** 高レイテンシは診断、モニタリング、またはリアルタイム介入を妨げる可能性があります。
  - [IBM: Latency in Healthcare](https://www.ibm.com/think/topics/latency)

### 5. AI/MLパイプライン
- **重要性:** リアルタイム推論とセマンティック検索は、高速データ検索に依存しています。
- **影響:** 高い検索レイテンシはモデルのスループットをボトルネックにし、ユーザーエクスペリエンスを低下させます。
  - [AI21: Retrieval Latency](https://www.ai21.com/glossary/foundational-llm/retrieval-latency/)

## レイテンシの主な原因と寄与要因

デジタルインフラストラクチャにおけるレイテンシには、いくつかの要因が寄与します:

- **物理的距離:** 距離が大きいほどレイテンシが増加します。[AWS: Latency](https://aws.amazon.com/what-is/latency/)
- **伝送媒体:** 光ファイバー < 銅線 < ワイヤレス < 衛星(レイテンシの順)。[Fortinet: Transmission Medium](https://www.fortinet.com/resources/cyberglossary/latency)
- **ネットワークホップ数:** 各ルーター、スイッチ、またはファイアウォールが処理時間を追加します。
- **ネットワーク輻輳:** 高トラフィック量が遅延を引き起こします。
- **サーバー/アプリケーションパフォーマンス:** 非効率的なサーバー処理がレイテンシを増加させます。
- **ストレージパフォーマンス:** HDDはSSDよりも高レイテンシです。[WEKA: Storage Latency](https://www.weka.io/blog/ai-ml/solving-latency-challenges-in-ai-data-centers/)
- **パケットサイズとデータ量:** より大きなパケットまたは量は遅延を増加させる可能性があります。
- **ルーティングとネットワークアーキテクチャ:** 非効率的なルーティングまたは不要なホップがレイテンシを追加します。
- **コードとアプリケーションロジック:** 非効率的なアルゴリズムまたは最適化されていないコードが遅延を導入する可能性があります。

### 要約表:一般的なレイテンシ寄与要因

| 要因                   | 説明                                            | レイテンシへの影響     |
|--------------------------|--------------------------------------------------------|----------------------|
| 伝送媒体      | 光ファイバー vs. 銅線 vs. ワイヤレス vs. 衛星            | 高                 |
| 物理的距離        | エンドポイント間の地理的分離              | 高                 |
| ネットワークホップ             | 中間デバイス(ルーター、スイッチ)の数     | 中程度から高     |
| ネットワーク輻輳       | 同じネットワーク上の競合トラフィック                  | 高                 |
| サーバー/アプリケーション遅延 | 処理速度と効率                        | 中程度から高     |
| ストレージデバイス           | SSD vs. HDD vs. クラウドストレージ                          | 中程度             |
| データパケットサイズ         | 転送される各データユニットの量とサイズ          | 中程度             |

- **出典:** [Galileo AI](https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works)、[WEKA](https://www.weka.io/blog/ai-ml/solving-latency-challenges-in-ai-data-centers/)

## レイテンシの測定方法

レイテンシは、標準化されたメトリクスを使用してミリ秒(ms)で測定されます:

### 1. Time to First Byte(TTFB)
- リクエストの開始から応答の最初のバイトを受信するまでの時間。
- サーバー処理とネットワーク遅延の両方を示します。
- [MDN: TTFB](https://developer.mozilla.org/en-US/docs/Glossary/Time_to_first_byte)

### 2. Round-Trip Time(RTT)
- データパケットがソースから宛先へ移動し、戻ってくるまでの時間。
- ネットワークレイテンシのコアメトリック;`ping`などのツールを使用して測定されます。

### 3. Pingコマンド
- 宛先にデータパケットを送信し、戻り時間を測定します。
- Pingが低い = レイテンシが低い、より応答性の高い接続。

### 4. アプリケーション固有のメトリクス
- 検索レイテンシ:クエリからデータ検索までの時間(AIおよび検索システムで重要)。
- ディスクレイテンシ:読み書きリクエストと完了の間の時間。

#### 例表:典型的なレイテンシ範囲

| テクノロジー/媒体      | 典型的なレイテンシ(ms) |
|------------------------|---------------------|
| 光ファイバーネットワーク    | 1–10                |
| 有線イーサネット(LAN)   | <1                  |
| 4G LTE                 | 20–50               |
| 5G                     | <10                 |
| 衛星インターネット     | 500+                |
| HDDストレージ            | 5–10                |
| SSDストレージ            | <1                  |

- **出典:** [AWS](https://aws.amazon.com/what-is/latency/)、[Galileo AI](https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works)

## レイテンシと関連概念

### 1. 帯域幅
- ネットワーク上で1秒あたりに送信される最大データ量。
- 比喩:帯域幅はパイプの幅;レイテンシは水が流れ始める速さ。
- 高帯域幅は低レイテンシを保証*しません*。
- [IBM: Bandwidth vs. Latency](https://www.ibm.com/think/topics/latency)

### 2. スループット
- 単位時間あたりに正常に転送された実際のデータ。
- スループットは帯域幅とレイテンシの両方に影響されます。
- [AWS: Throughput](https://aws.amazon.com/what-is/throughput/)

### 3. ジッター
- 時間経過に伴うレイテンシの変動。
- 高ジッターはVoIPやストリーミングなどのリアルタイムアプリを妨害します。

### 4. パケットロス
- 宛先に到達しないデータパケットの割合。
- パケットロスは実効レイテンシを増加させる可能性があります。

#### 比較表:レイテンシ vs. 帯域幅、スループット、ジッター、パケットロス

| 概念      | 測定対象                  | 単位         | 例/比喩                              |
|--------------|-----------------------------------|--------------|----------------------------------------------|
| レイテンシ      | 応答を受信するまでの遅延       | ms            | 蛇口をひねった後に水が流れるまでの時間 |
| 帯域幅    | 最大データ容量             | Mbps、Gbps    | パイプの直径                         |
| スループット   | 実際に配信されたデータ             | Mbps、Gbps    | 実際に1秒あたりに流れる水の量     |
| ジッター       | 遅延の変動                | ms            | 水圧の変動               |
| パケットロス  | 転送中に失われたデータ              | %             | パイプからの水漏れ                    |

- **出典:** [Fortinet: Latency Glossary](https://www.fortinet.com/resources/cyberglossary/latency)

## レイテンシを削減または管理する戦略

低レイテンシのための最適化には、アーキテクチャ、インフラストラクチャ、ソフトウェアの戦略が必要です:

### 1. コンテンツデリバリーネットワーク(CDN)
- ユーザーに近い場所にコンテンツをキャッシュし、データ配信の物理的距離を最小化します。
- [AWS CloudFront](https://aws.amazon.com/cloudfront/)

### 2. エッジコンピューティング
- 計算とデータストレージをエンドユーザーに近づけ、往復時間を削減します。
- [IBM Edge Computing](https://www.ibm.com/think/topics/edge-computing)

### 3. ネットワークインフラストラクチャのアップグレード
- ルーター、スイッチ、ケーブルをアップグレードします。
- 可能な場合は光ファイバーリンクに移行します。
- [WEKA: Data Center Upgrades](https://www.weka.io/blog/ai-ml/solving-latency-challenges-in-ai-data-centers/)

### 4. サーバーとアプリケーションの最適化
- サーバーコードをリファクタリングし、データベースクエリを最適化し、ブロッキング操作を最小化します。
- [MDN: Application Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)

### 5. サブネット化とネットワーク設計
- エンドポイントをグループ化してネットワークホップを最小化し、ルーティングパスを最適化します。

### 6. トラフィックシェーピングと優先順位付け
- アプリケーションの優先度に基づいて帯域幅を割り当てます(例:ファイルダウンロードよりもVoIP)。

### 7. キャッシング戦略
- 頻繁にアクセスされるデータを高速アクセスメモリに保存します。
- [AI21 RAGCache](https://www.ai21.com/glossary/retrieval-augmented-generation-rag/)

### 8. ネットワークホップと距離の削減
- ユーザーに近い場所にサーバーをホストして、中間デバイスを最小化します。

### 9. アプリケーションモニタリングと可観測性
- リアルタイムモニタリングツールを使用して、レイテンシのボトルネックを検出および解決します。
- [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)

### 10. AI検索のためのハイブリッド検索モデル
- ベクトル検索とキーワード検索を組み合わせて、AIアプリケーションにおける精度とレイテンシのバランスを取ります。

- **出典:** [Galileo AI](https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works)、[DriveNets](https://drivenets.com/blog/latency-in-ai-networking-inevitable-limitation-to-solvable-challenge/)

## 業界ソリューションとベストプラクティス

主要プロバイダーは、レイテンシ最適化のための専門的なソリューションを提供しています:

- [AWS Direct Connect](https://aws.amazon.com/directconnect/):AWSへの専用ネットワーク接続により、レイテンシと変動を削減します。
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/):低レイテンシコンテンツ配信のためのグローバルCDN。
- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/):最適なAWSエッジロケーションを通じてユーザートラフィックをルーティングします。
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/):人口密集地に近い場所にAWSサービスをデプロイします。
- [IBM Edge Computing](https://www.ibm.com/think/topics/edge-computing):レイテンシに敏感なワークロードのためにエッジにコンピュートリソースをデプロイします。
- [AI21 RAGCache](https://www.ai21.com/glossary/retrieval-augmented-generation-rag/):インテリジェントキャッシングを通じてAIパイプラインの検索レイテンシを削減します。

## よくある質問(FAQ)

**Q1:「良好な」レイテンシとは何ですか?**  
A:許容可能なレイテンシはユースケースによって異なります。インタラクティブアプリの場合、<100 msが一般的に良好です;高頻度取引やリアルタイムゲームの場合、<10 msが必要な場合があります。  
[出典: AWS](https://aws.amazon.com/what-is/latency/)

**Q2:高レイテンシと低レイテンシ、どちらが良いですか?**  
A:低レイテンシが常に望ましく、より高速で応答性の高いアプリケーションとより良いユーザーエクスペリエンスを可能にします。

**Q3:高帯域幅がレイテンシを改善しない理由は?**  
A:帯域幅は1秒あたりに移動するデータ量に関するものであり、単一トランザクションの速度ではありません。長いネットワークパスや輻輳は、高帯域幅でも高レイテンシを引き起こす可能性があります。

**Q4:Webアプリでレイテンシを削減するための簡単な方法は?**  
A:CDNを使用し、画像/スクリプトを最適化し、サードパーティAPIコールを最小化し、キャッシングを有効にし、ユーザーに近い場所にサーバーをデプロイします。

**Q5:検索レイテンシはAIシステムにどのように影響しますか?**  
A:高い検索レイテンシは推論とリアルタイム意思決定を遅くし、AI駆動型検索、推奨、チャットボットの有効性に直接影響します。  
[出典: AI21 Labs](https://www.ai21.com/glossary/foundational-llm/retrieval-latency/)

## さらなる読み物と権威あるリソース

- [AWS: What Is Latency?](https://aws.amazon.com/what-is/latency/)
- [IBM: What Is Latency?](https://www.ibm.com/think/topics/latency)
- [MDN: Understanding Latency](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Understanding_latency)
- [Fortinet: What Is Latency and How to Reduce It](https://www.fortinet.com/resources/cyberglossary/latency)
- [AI21: Retrieval Latency in AI](https://www.ai21.com/glossary/foundational-llm/retrieval-latency/)
- [WEKA: Solving Latency Challenges in AI Data Centers](https://www.weka.io/blog/ai-ml/solving-latency-challenges-in-ai-data-centers/)
- [DriveNets: Latency in AI Networking](https://drivenets.com/blog/latency-in-ai-networking-inevitable-limitation-to-solvable-challenge/)

## 要約表:主要なレイテンシ最適化戦略

| 戦略                     | 説明                                    | 最適な用途                                 |
|------------------------------|------------------------------------------------|-------------------------------------------|
| CDNとエッジコンピューティング         | コンテンツ/コンピュートをユーザーに近い場所に配布     | Webアプリ、ストリーミング、AI推論         |
| ネットワークインフラストラクチャのアップグレード| より高速なリンク、最新のハードウェアを使用           | 企業、データセンター                 |
| サーバー/アプリケーションの最適化| コードとクエリをリファクタリング                    | すべてのソフトウェア、特にAIパイプライン     |
| サブネット化とトラフィックシェーピング | トラフィックを効率的にグループ化および優先順位付け       | 大規模ネットワーク、クラウドデプロイメント         |
| キャッシング                      | 頻繁なデータをメモリに保存                  | AI検索、Webコンテンツ、分析         |
| モニタリングと可観測性   | 問題を事前に検出および解決            | 複雑で動的な環境             |

## 重要なポイント

- レイテンシは、リクエストの開始から応答の受信までの時間遅延です。
- AIインフラストラクチャ、リアルタイムアプリケーション、ユーザー向けデジタルシステムにおいて重要です。
- ネットワーク、ハードウェア、ソフトウェアなど、複数の要因が全体的なレイテンシに寄与します。
- レイテンシは帯域幅、スループット、ジッター、パケットロスとは異なります。
- レイテンシの削減には、アーキテクチャ、インフラストラクチャ、ソフトウェアの最適化が含まれます。
- 業界リーダーは、レイテンシを監視、削減、管理するためのツールとサービスを提供しています。

## 用語集参照

- **帯域幅:** 特定の時間におけるネットワークの最大データ転送容量。
- **スループット:** 単位時間あたりに転送される実際のデータ。
- **ジッター:** レイテンシの時間的変動。