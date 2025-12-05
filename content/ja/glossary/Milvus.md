---
title: Milvus
date: 2025-11-25
translationKey: milvus-a
description: Milvusは、非構造化データに対するスケーラブルな類似性検索を実現する、オープンソースのクラウドネイティブなベクトルデータベースです。そのアーキテクチャ、機能、ユースケース、および他のベクトルデータベースとの比較について解説します。
keywords:
- Milvus
- ベクトルデータベース
- 類似性検索
- ベクトル埋め込み
- 非構造化データ
category: Vector Database
type: glossary
draft: false
e-title: Milvus
term: ミルバス
reading: Milvus
kana_head: その他
---
## Milvusとは？

Milvusは、大規模な非構造化データセットに対するスケーラブルで高性能な類似性検索を目的として構築された、オープンソースのクラウドネイティブなベクトルデータベースです。[Zilliz](https://zilliz.com/)によって開発され、[Apache 2.0ライセンス](https://github.com/milvus-io/milvus/blob/master/LICENSE)の下で管理されているMilvusは、AIや機械学習モデルによって生成されたデータの数値表現である高次元ベクトル埋め込みを効率的に保存、インデックス化、クエリします。ラップトップでのプロトタイピングから、分散アーキテクチャ全体で数百億のベクトルを管理するエンタープライズ本番環境まで、弾力的なスケーリングを実現するように設計されています。Milvusは、セマンティック検索、レコメンデーション、検索拡張生成(RAG)、コンピュータビジョン、異常検知などのアプリケーションを支えています。

**主な特徴:**
- Apache 2.0ライセンスのオープンソース
- クラウドネイティブなマイクロサービスベースのアーキテクチャ
- エンタープライズスケールでの高スループット、低レイテンシの類似性検索を実現
- 最新のAI/MLツールチェーンおよびフレームワークとの統合

**参考資料:**  
- [Milvus公式ドキュメント](https://milvus.io/docs/overview.md)  
- [Sealos: What is Milvus?](https://sealos.io/blog/what-is-milvus)  
- [IBM: What is Milvus?](https://www.ibm.com/think/topics/milvus)

## コアコンセプト

### ベクトル埋め込み

ベクトル埋め込みは、テキスト、画像、音声などの非構造化データのセマンティックまたは構造的情報をエンコードする高次元配列(例:128、768、4096次元)です。[OpenAI](https://platform.openai.com/docs/guides/embeddings)、[Hugging Face transformers](https://huggingface.co/)、その他のニューラルネットワークなどの埋め込みモデルによって生成され、複雑なデータを効率的な数学的比較に適した形式に変換します。

**例:** 「cat」という単語は、768次元空間において`[0.18, -0.46, 0.72, ...]`のように表現されます。意味的に類似した2つのテキストや画像は、この空間内で互いに近い位置に埋め込まれます。

**参考資料:**  
- [What Exactly is a Vector Database](https://milvus.io/blog/what-is-a-vector-database.md)  
- [OpenAI: Embeddings](https://platform.openai.com/docs/guides/embeddings)

### 非構造化データ

非構造化データとは、事前定義されたスキーマや構造に従わないデータ、例えば自由形式のテキスト、画像、音声、動画などを指します。リレーショナルデータとは異なり、非構造化データは従来のデータベースでは処理や分析が困難です。ベクトル埋め込みは、このデータを固定長のベクトルとして表現することで、効率的なインデックス化、検索、取得を可能にします。

**Milvusとの関連性:** Milvusは非構造化データの埋め込みを保存し、従来のシステムでは実現できない高速かつ正確な検索と分析を可能にします。

### 類似性検索とANN

- **類似性検索:** ベクトル距離メトリック(例:ユークリッド距離、[コサイン類似度](/en/glossary/cosine-similarity/)、内積)に基づいて、クエリアイテムに最も類似したデータセット内のアイテムを見つけます。
- **近似最近傍探索(ANN):** クエリベクトルに最も近いベクトルを持つアイテムを高速に取得するアルゴリズム群で、わずかな精度を犠牲にして大幅な速度向上を実現します。数十億規模のデータセットには不可欠です。

**参考資料:**  
- [Milvus Blog: What is a Vector Database](https://milvus.io/blog/what-is-a-vector-database.md)

## Milvusのアーキテクチャとデプロイメントモデル

### システム概要

Milvusは、ストレージとコンピュートを分離した**多層マイクロサービスベースのアーキテクチャ**を実装しています。その設計はデータプレーンとコントロールプレーンの分離に従い、独立したスケーラビリティと運用の柔軟性を促進します。

**主要なアーキテクチャコンポーネント** ([Milvus Architecture Overview](https://milvus.io/docs/architecture_overview.md)):
- **アクセス層:** クライアントリクエストとAPI(RESTful、SDK)を処理するステートレスプロキシで、リクエストの検証と結果の集約を行います。
- **コーディネーターサービス:** 論理的な「頭脳」として、負荷分散、メタデータ管理、システム状態、DDL/DCL操作、タスクスケジューリングを調整します。
- **ワーカーノード:** 検索、データ挿入、インデックス化のためのステートレスエグゼキューター。  
    - *ストリーミングノード*: リアルタイムデータ取り込みとストリーミング整合性を処理。  
    - *クエリノード*: 履歴(シール済み)データをロードしてクエリ。  
    - *データノード*: コンパクションやインデックス構築などのバックグラウンドタスクを処理。
- **オブジェクトストレージ層:** ベクトルデータ、インデックス、ログを永続化。MinIO、AWS S3、Azure Blobなどをサポート。
- **メタストレージ:** メタデータとクラスタ状態にetcdを使用。
- **WALストレージ:** データの耐久性と復旧のための先行書き込みログ(例:Woodpecker、Kafka、Pulsar)。

**データフロー例:**  
- 検索リクエストは、クライアント → アクセスプロキシ → ストリーミング/クエリノード → 結果集約と返却の順に処理されます。
- 挿入はストリーミングノードを経由し、WALに書き込まれ、シール済みセグメントに変換され、インデックス化されて保存されます。

**詳細:**  
- [Milvus Architecture Documentation](https://milvus.io/docs/architecture_overview.md)

### デプロイメントモード

Milvusは複数のデプロイメントモデルをサポートしています([Install Overview](https://milvus.io/docs/install-overview.md)):
| デプロイメントモード | 説明                                                                                                 | ユースケース              |
|---------------------|-----------------------------------------------------------------------------------------------------|---------------------------|
| Milvus Lite         | `pip`でインストール可能なPythonライブラリ。ノートブックやエッジデバイスに組み込んで実行。              | プロトタイピング、ローカル開発 |
| Standalone          | すべてのサービスをバンドルしたDockerベースのシングルノードデプロイメント。                              | テスト、小規模本番環境    |
| Distributed         | Kubernetesベースのクラウドネイティブデプロイメントで、水平スケーリングと[高可用性](/en/glossary/high-availability--ha-/)を実現。 | エンタープライズ、大規模環境 |
| Zilliz Cloud        | フルマネージドMilvus(SaaSおよびBYOCオプション)、サーバーレスまたは専用クラスタ、10倍のパフォーマンス向上。| 手間なし、本番環境        |

**参考資料:**  
- [Milvus Deployment Models](https://milvus.io/docs/install-overview.md)

### スケーラビリティとパフォーマンス

- **水平スケーリング:** コンピュート(例:クエリノード)とストレージは独立してスケール。ステートレスマイクロサービスにより、Kubernetesなどのプラットフォームで調整される弾力的な復旧とスケーリングが可能。
- **ハードウェア最適化:** AVX512、SIMD、[GPUアクセラレーション](/en/glossary/gpu-acceleration/)(NVIDIA CUDA、Cagra)、NVMe SSDサポート。
- **数十億規模のサポート:** 数百億のベクトルを持つデータセットに対する実証済みの安定性とパフォーマンスで、大手企業の本番環境で使用されています。

**参考資料:**  
- [Sealos: Milvus and Scalability](https://sealos.io/blog/what-is-milvus#scalability-and-performance)

## 主要機能と能力

### サポートされるデータタイプ

Milvusは、柔軟なモデリングのために豊富なデータタイプをサポートしています([Index Explained](https://milvus.io/docs/index-explained.md)):
- **密ベクトル:** `float32`、`float16`、`int8`配列(例:BERT、CLIP、ResNetから)。
- **疎ベクトル:** 多くのゼロを含む高次元データに効率的(テキスト検索、レコメンデーション)。
- **バイナリベクトル:** ハッシングやビジョンタスク用のコンパクトなビットパック表現。
- **プリミティブ型:** 整数、浮動小数点、文字列、ブール値など。
- **JSON/配列/セット:** 半構造化メタデータとマルチモーダルモデリング用。

### インデックスアルゴリズム

Milvusは、さまざまなシナリオに最適化された高度なベクトルインデックスオプションを提供しています([Index Explained](https://milvus.io/docs/index-explained.md)):

| アルゴリズム      | 説明                                                                      | ユースケース/利点          |
|-------------------|---------------------------------------------------------------------------|----------------------------|
| [HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/)              | [階層的ナビゲート可能スモールワールド](/en/glossary/hnsw--hierarchical-navigable-small-world-/)。高再現率/高速検索のためのグラフベースインデックス | 汎用性、高次元              |
| IVF               | 転置ファイルシステム。効率的な検索のためにベクトル空間を分割                | 速度/コストのバランス      |
| DiskANN           | RAMに収まらない大規模データセット用のディスク上インデックス                  | 数十億のベクトル、SSD      |
| Flat(総当たり)    | 最高精度のための線形スキャン                                                | 小規模データセット、評価    |
| SCANN、Annoy      | 特殊なニーズのための外部ライブラリとの統合                                  | カスタム、研究              |
| Cagra(GPU)        | NVIDIA GPU用に最適化されたグラフベースインデックス                          | 高スループット、GPUインフラ |

**主要概念:**
- *データ構造:* IVF(クラスタリング/バケット化)、[HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/)(グラフベース)、Flat(総当たり)。
- *量子化:* SQ8(スカラー量子化)やPQ(積量子化)などの技術により、メモリ効率のためにベクトルを圧縮。
- *リファイナー:* トップ候補の距離を高精度で再計算し、速度と精度のバランスを取ります。

**パフォーマンストレードオフ:**
- グラフベースインデックス([HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/))は、低k、高再現率クエリでIVFを上回ります。
- IVFバリアントは、大きなtop-kクエリに最適です。
- DiskANNは、SSDバックの数十億規模データセットに理想的です。
- フィルタ比率が極端に高い場合や小規模データセットには総当たり検索を使用します。

**参考資料:**  
- [Index Explained](https://milvus.io/docs/index-explained.md)

### 検索タイプ

Milvusは多様な検索パターンをサポートしています:
- **ANN検索:** クエリに最も類似したトップKベクトルを検索。
- **フィルタリング検索:** ベクトル検索とメタデータフィルタリング(タグ、範囲)を組み合わせ。
- **範囲検索:** 距離閾値内のベクトルを取得。
- **ハイブリッド検索:** クエリで複数のベクトルフィールド/モダリティを使用。
- **全文検索:** テキストフィールドのBM25ベース検索。
- **リランキング:** セカンダリアルゴリズムで初期結果を洗練。
- **IDによるフェッチ/クエリ:** プライマリキーまたは複雑な式でアイテムを取得。

### データモデリングと操作

- **コレクションとパーティション:** 効率的なアクセスのためにデータを階層的に整理。
- **スキーマ進化:** ダウンタイムなしでコレクションスキーマを更新。
- **CRUD操作:** ベクトルとメタデータの挿入、更新、削除、アップサート。
- **バッチ処理:** 一括インポート/エクスポートツール。
- **マルチテナンシー:** データベース、コレクション、またはパーティションキーによる分離。

### 整合性とセキュリティ

- **設定可能な整合性:** 強整合性、有界陳腐化、セッション、結果整合性モデル。
- **認証とRBAC:** ユーザー認証、ロールベースアクセス制御、きめ細かい権限。
- **TLS暗号化:** 転送中のデータを保護。
- **ホット/コールドストレージ:** コスト効率の高いパフォーマンスのための階層型ストレージ。

## 統合とエコシステム

Milvusは、最新のAI/MLスタックとのシームレスな統合を実現するように設計されています:

- **SDK:** [Python(PyMilvus)](https://milvus.io/api-reference/pymilvus/v2.3.x/)、Java、Go、Node.js、C#(Microsoft貢献)、RESTful API。
- **AIフレームワーク統合:** [LangChain](https://python.langchain.com/docs/integrations/vectorstores/milvus)、[LlamaIndex](https://gpt-index.readthedocs.io/en/latest/how_to/vector_stores/milvus.html)、[OpenAI](https://milvus.io/docs/integrate_with_openai.md)、[Hugging Face](https://huggingface.co/)、[DSPy](https://github.com/stanfordnlp/dspy)、[Haystack](https://haystack.deepset.ai/)、[Ragas](https://github.com/explodinggradients/ragas)、[MemGPT](https://github.com/cpacker/MemGPT)。
- **データ処理:** MLパイプライン用の[Apache Sparkコネクタ](https://github.com/milvus-io/spark-connector)。
- **可観測性:** 監視とアラート用の[Prometheus](https://prometheus.io/)と[Grafana](https://grafana.com/)。
- **管理ツール:** [Attu(GUI)](https://attu.zilliz.com/)、Birdwatcher(システムデバッグ)、Milvus Backup & CDC(災害復旧とバックアップ)、Vector Transmission Services(VTS、データ移行用)。

**例:OpenAIとの統合**  
MilvusはOpenAIモデルによって生成された埋め込みのベクトルストアとして機能し、セマンティック検索とRAGを促進します。  
[Semantic Search with Milvus and OpenAI(公式ガイド)](https://milvus.io/docs/integrate_with_openai.md)

**参考資料:**  
- [Milvus Integrations](https://milvus.io/docs/integrate_with_openai.md)  
- [SDK Documentation](https://milvus.io/api-reference/overview.md)  
- [GitHub: Milvus Project](https://github.com/milvus-io/milvus)

## 一般的なユースケース

Milvusは、さまざまなAIおよびデータ集約型アプリケーションを支えています:

### 検索拡張生成(RAG)

ベクトル検索を介してLLMと生成AIモデルを外部知識ベースに接続します。取得されたドキュメントや事実に基づいて、正確で最新の、文脈的に関連性の高いAI応答を可能にします。
- **参考資料:** [Build RAG with Milvus](https://milvus.io/docs/build-rag-with-milvus.md)

### レコメンデーションシステム

ユーザー嗜好埋め込みとアイテム特徴に基づいて、コンテンツ、製品、広告を表示します。eコマース、ストリーミング、ニュースフィード、広告ターゲティングで使用されます。

### コンピュータビジョン

視覚埋め込みを使用した画像類似性検索、物体検出、分類をサポート。逆画像検索、医療画像検索、小売ビジュアル検索を可能にします。

### 自然言語処理

テキスト埋め込みを使用したセマンティック検索、ドキュメントクラスタリング、チャットボット検索を促進。法的文書検索、文脈対応チャットボット、FAQシステムで使用されます。

### 不正検知と異常検知

リアルタイム異常検知のためにトランザクションパターンやネットワークイベントをベクトル化。金融不正検知とサイバーセキュリティで使用されます。

### 科学研究と創薬

分子類似性検索、ゲノム解析、材料科学アプリケーションを可能にします。

## 業界での採用と事例

Milvusは、さまざまな業界や組織で展開されています([Milvus Users](https://milvus.io/docs/overview.md#What-Makes-Milvus-so-Scalable)):

| 企業/組織            | ユースケース                      |
|----------------------|----------------------------------|
| NVIDIA               | AIインフラストラクチャ、GPUアクセラレーション |
| Salesforce           | 大規模文書・画像検索              |
| eBay                 | 画像類似性とレコメンデーション    |
| Walmart              | 小売AIアプリケーション            |
| IBM                  | NLPとメディア検索                 |
| Shopee、Tokopedia    | eコマースレコメンデーション、ビジュアル検索 |
| AT&T、PayPal         | 不正検知、通信分析                |
| ZipRecruiter         | 求人マッチングのセマンティック検索 |
| SmartNews、LINE      | コンテンツレコメンデーションと検索 |
| Bosch、Intuit、Roblox、Compass、OMERS、New Relic、Trend、MOJ、Inflection | 多様なAIおよび分析ワークロード |

## 比較:Milvusと他のベクトルデータベース

| 機能/側面           | Milvus       | [Pinecone](/en/glossary/pinecone/)        | [Weaviate](/en/glossary/weaviate/)         | [Qdrant](/en/glossary/qdrant/)         | [Chroma](/en/glossary/chroma/)        |
|---------------------|--------------|-----------------|------------------|----------------|---------------|
| オープンソース      | はい(Apache) | いいえ(SaaSのみ) | はい(OSS/商用)   | はい(OSS/商用) | はい          |
| デプロイメント      | セルフ、クラウド、K8s | SaaS    | セルフ、クラウド | セルフ、クラウド | セルフ、クラウド |
| スケーラビリティ    | 優秀         | マネージド      | 良好             | 良好           | 限定的        |
| インデックスタイプ  | [HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/)、IVF、DiskANN、Annoy、Cagra | プロプライエタリ | HNSW        | HNSW、IVF     | HNSW、Annoy   |
| ベクトルタイプ      | 密、疎、バイナリ | 密          | 密               | 密             | 密            |
| メタデータフィルタリング | 高度     | 基本            | GraphQL          | 高度           | 基本          |
| ハードウェアアクセラレーション | はい(GPU、SIMD、AVX) | 一部 | いいえ       | いいえ         | いいえ        |

**Milvusの際立った利点:**
- 豊富なインデックスの多様性(HNSW、IVF、DiskANN、Annoy、Cagra)
- クラウドネイティブマイクロサービスによる実証済みの数十億規模のパフォーマンス
- オープンで活発なコミュニティと幅広いSDK/言語サポート
- ハイブリッドおよびマルチモーダル検索(密、疎、バイナリベクトル+メタデータ)
- エンタープライズグレードのセキュリティ(TLS、RBAC、[マルチテナンシー](/en/glossary/multi-tenancy/))

**参考資料:**  
- [Oracle: Milvus Overview](https://www.oracle.com/database/vector-database/milvus/)  
- [IBM: What is Milvus?](https://www.ibm.com/think/topics/milvus)  
- [Sealos: What is Milvus?](https://sealos.io/blog/what-is-milvus)

## クイックスタート例

**PyMilvusを使用したPythonの例:**

```python
from pymilvus import MilvusClient

# Milvusに接続
client = MilvusClient("milvus_demo.db")

# 5次元ベクトルで新しいコレクションを作成
client.create_collection(
    collection_name="demo_collection",
    dimension=5
)

# ベクトルデータを挿入
vectors = [
    [0.1, 0.2, 0.3, 0.4, 0.5],
    [0.2, 0.1, 0.4, 0.3, 0.6]
]
client.insert(collection_name="demo_collection", data=vectors)

# 類似性検索を実行
query_vector = [0.1, 0.2, 0.3, 0.4, 0.5]
results = client.search(
    collection_name="demo_collection",
    data=[query_vector],
    top_k=1
)
print(results)
```