---
title: Qdrant
date: 2025-11-25
translationKey: qdrant
description: Qdrantは、高次元ベクトルデータ向けのオープンソースベクトル類似性検索エンジン兼ベクトルデータベースで、セマンティック検索、RAG、レコメンデーションを実現します。
keywords: ["Qdrant", "ベクトルデータベース", "ベクトル検索", "埋め込み", "RAG"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Qdrant
term: キュードラント
reading: Qdrant
kana_head: その他
---
## 概要

Qdrantは、機械学習およびディープラーニングモデルが生成する埋め込み(エンベディング)である高次元ベクトルデータの保存、インデックス作成、検索に特化して設計された、オープンソースのベクトル類似性検索エンジン兼ベクトルデータベースです。高速でスケーラブルなセマンティック検索、レコメンデーションシステム、検索拡張生成(RAG)、異常検知、その他のAI/MLユースケースを実現することで、Qdrantは膨大な非構造化データセットを扱う現代のデータ駆動型アプリケーションの独自のニーズに対応します。QdrantはRustで実装されており、堅牢なパフォーマンスとメモリ安全性を保証し、オープンソースとしても、フルマネージド[クラウドサービス](https://qdrant.tech/cloud/)としても利用可能です。

> **「Qdrantは、当社の要求の厳しいレコメンデーションおよびRAGアプリケーションを支えています。デプロイの容易さと大規模環境での高いパフォーマンスを理由に選択しましたが、その結果には一貫して感銘を受けています。」**  
> —Srubin Sethu Madhavan氏、HubSpot テクニカルリードII

## Qdrantとは?

Qdrant(「クアドラント」と発音)は以下を実現するよう設計されています:

- **保存** テキスト、画像、音声、動画、その他のデータタイプのセマンティクスを表す埋め込み(ベクトル)を保存。
- **インデックス作成** 数十億の高次元ベクトルを低レイテンシで検索できるようインデックス化。
- **検索** 設定可能な距離メトリクスを使用して、クエリベクトルに最も類似したベクトルを検索。
- **サポート** ハイブリッド検索(セマンティック+キーワード)、マルチモーダルデータ(ポイントごとに複数のベクトル)、ペイロードベースのフィルタリングをサポート。

QdrantのRust基盤は、高い並行性と効率的なメモリ使用を提供します。バッチ操作、フィルタリング、ハイブリッドクエリ、高度なインデックス機能をサポートする最新のAPIを提供しています。マネージドデプロイメントについては、[Qdrant Cloud](https://qdrant.tech/cloud/)をご覧ください。

詳細な実践的入門については、[A Developer's Friendly Guide to Qdrant Vector Database (Cohorte)](https://www.cohorte.co/blog/a-developers-friendly-guide-to-qdrant-vector-database)および[公式チュートリアル](https://qdrant.tech/documentation/database-tutorials/)をご参照ください。

## なぜQdrantのようなベクトルデータベースが必要なのか?

従来のデータベース(リレーショナルまたはNoSQL)は構造化データの保存に優れていますが、以下には対応していません:

- **高次元埋め込み**(ニューラルモデルから生成される数百から数千の次元)。
- **類似性検索**(「Xに最も類似しているものは何か?」)を数学的なベクトル距離を使用して実行。
- **非構造化およびマルチモーダルデータ**(テキスト、画像、音声など)。

Qdrantのようなベクトルデータベースは類似性によるクエリに最適化されており、これは現代のAI/MLワークロード(セマンティック検索、レコメンデーション、RAGなど)に不可欠です。

詳細な説明については、[What is a Vector Database? (Qdrant)](https://qdrant.tech/articles/what-is-a-vector-database/)をご覧ください。

## 主要な概念と用語

### 1. **ベクトル(埋め込み)**

- **定義:**  
  ベクトルは、埋め込みモデル(OpenAI、HuggingFace、CLIPなど)によって生成される、オブジェクト(テキスト、画像など)のセマンティック特徴を表す数値(通常は浮動小数点数)の順序付きリストです。各数値は高次元空間における座標です。ベクトルは意味やコンテキストを「エンコード」し、数学的な比較を可能にします。

- **例:**  
  - 文に対する768次元ベクトル。
  - 製品説明に対する1536次元ベクトル。

- **タイプ:**  
  - **密ベクトル:** ほとんどの要素がゼロ以外; 通常はトランスフォーマーモデルから生成。
  - **疎ベクトル:** ほとんどの要素がゼロ; キーワードベース(BM25)検索で一般的。

- **ユースケース:**  
  アイテムをベクトルとして表現することで、距離メトリクスを介して「類似した」アイテムを見つけることができ、セマンティック検索やレコメンデーションを実現します。

> **参考資料:**  

### 2. **ポイント**

- **定義:**  
  Qdrantにおけるデータの原子単位。各ポイントは以下で構成されます:
  - **ID:** 一意のキー(整数またはUUID)。
  - **ベクトル:** 高次元埋め込み。
  - **ペイロード:** オプションのスキーマレスJSONメタデータ。

- **類推:**  
  SQLの「行」に似ていますが、主要データは列ではなくベクトルです。

- **例:**
  ```json
  {
    "id": 123,
    "vector": [0.1, -0.2, 0.7, ...],
    "payload": {
      "category": "news",
      "author": "Alice",
      "timestamp": "2024-06-01"
    }
  }
  ```

- **使用法:**  
  ポイントはペイロードを介したフィルタリングとファセット検索をサポートします。

### 3. **コレクション**

- **定義:**  
  同じ次元数と距離メトリクスを共有するポイント(ベクトル+ペイロード)の名前付きセット。SQLのテーブルに類似。

- **使用法:**  
  - `products_collection`にアイテムベクトルを保存。
  - `customers_collection`に顧客埋め込みを保存。

- **設定:**
  - ベクトルサイズ(例: 768)。
  - 距離メトリクス(下記参照)。
  - ストレージタイプ(RAM、memmap/オンディスク; [リソース最適化](https://qdrant.tech/articles/vector-search-resource-optimization/)参照)。
  - 量子化設定。

> [Qdrant Collections Documentation](https://qdrant.tech/documentation/concepts/collections/)

### 4. **距離メトリクス**

- **定義:**  
  2つのベクトル間の「類似性」を測定する関数。

- **Qdrantでサポート:**
  - **コサイン類似度:** ベクトル間の角度を測定; テキスト埋め込みで一般的。
  - **ドット積:** 方向と大きさの両方に敏感; レコメンデーションで使用。
  - **ユークリッド距離:** 直線距離; 画像やセンサー埋め込みに有用。
  - **マンハッタン距離:** 絶対差の合計; 疎データで時々使用。

- **例:**  
  文書検索では、[コサイン類似度](/ja/glossary/cosine-similarity/)が類似した意味を持つテキストを見つけます。

> [Distance Metrics Reference](https://qdrant.tech/documentation/concepts/collections/#distance-metrics)

### 5. **ペイロード**

- **定義:**  
  各ポイントに添付される柔軟なJSONオブジェクトで、構造化メタデータ(タグ、カテゴリ、タイムスタンプ、生テキストなど)を保存します。

- **目的:**  
  高度なフィルタリングとファセット検索を可能にします。例えば、カテゴリや価格で検索結果をフィルタリング。

- **例:**
  ```json
  "payload": {
    "category": "electronics",
    "brand": "Acme",
    "price": 199.99,
    "release_date": "2024-01-15"
  }
  ```

- **インデックス作成:**  
  フィールドは高速検索とフィルタリングのためにインデックス化できます([Indexing](https://qdrant.tech/documentation/concepts/indexing/)参照)。

> [Payloads in Qdrant](https://qdrant.tech/documentation/concepts/payload/)

### 6. **ストレージオプション: RAM、Memmap(オンディスク)、量子化**

- **RAMストレージ:**  
  ベクトルはメモリに保存; 利用可能なRAMに収まるデータセットに最速。

- **Memmap(オンディスク)ストレージ:**  
  ベクトルはディスクに保存され、効率的なアクセスのためにメモリマップされます。RAMを超える大規模データセットに不可欠。

- **量子化ストレージ:**  
  ベクトルは圧縮され、より少ないビット(例: 8ビット、2ビット)を使用し、精度とのトレードオフで大幅に大きなデータセットを可能にします。[Quantization Guide](https://qdrant.tech/documentation/guides/quantization/)参照。

> [Resource Optimization Strategies](https://qdrant.tech/articles/vector-search-resource-optimization/#storage-disk-vs-ram)
> [Storage Options in Qdrant](https://qdrant.tech/documentation/concepts/storage/)

### 7. **インデックス作成(HNSW、ペイロードインデックス)**

- **目的:**  
  数十億のベクトルに対する類似性検索を高速化し、高速なメタデータフィルタリングを可能にします。

- **ベクトルインデックス(HNSW):**
  - **階層的ナビゲート可能スモールワールド(HNSW):**  
    近似最近傍(ANN)検索のためのグラフベースのインデックス。対数スケーリングを提供し、速度と再現率のバランスを取ります。パラメータ`m`、`ef`、`ef_construct`で設定可能。  
    技術的背景については: [HNSW Paper](https://arxiv.org/abs/1603.09320)、[HNSW Indexing Fundamentals](https://qdrant.tech/course/essentials/day-2/what-is-hnsw/)。
  - **設定例:**  
    検索精度/速度のトレードオフのために`hnsw_ef`を調整。

- **ペイロードインデックス:**
  - 特定のフィールド(例: 文字列、数値、キーワード)をインデックス化して高速フィルタリング。  
    例:  
    ```python
    client.create_payload_index(
        collection_name="products",
        field_name="category",
        field_schema="keyword"
    )
    ```
  - [Indexing Documentation](https://qdrant.tech/documentation/concepts/indexing/)参照。

- **ハイブリッドインデックス:**  
  単一のクエリでベクトル検索、疎/キーワード検索、ペイロードフィルタリングを組み合わせます。

> [Indexing in Qdrant](https://qdrant.tech/documentation/concepts/indexing/)

### 8. **量子化**

- **定義:**  
  値あたりのビット数を減らしてベクトルを表現することでベクトルを圧縮し、RAMまたはディスクにより多くのベクトルを保存できるようにします。

- **技術:**  
  - スカラー量子化(例: 8ビット)。
  - 極端な圧縮のためのバイナリ/非対称量子化。
  - Qdrantは複数の量子化戦略をサポート; [Quantization Guide](https://qdrant.tech/documentation/guides/quantization/)参照。

- **利点:**  
  適切に調整すれば、精度の損失を最小限に抑えながら、同じスペースに最大32倍のベクトルを保存できます。

- **設定:**  
  コレクション作成時に`quantization_config`を設定。

### 9. **マルチテナンシー**

- **定義:**  
  単一のQdrantインスタンス内で複数のユーザーまたはプロジェクトのデータを論理的に分離。

- **ベストプラクティス:**  
  ペイロードに`tenant`フィールドを持つ単一のコレクションを使用。すべての読み取り/書き込みをテナントIDでフィルタリング。高度なケースについては、[Multiple Partitions Guide](https://qdrant.tech/documentation/guides/multiple-partitions/)参照。

### 10. **ハイブリッド、密、疎検索**

- **密検索:**  
  密埋め込みを使用したセマンティック類似性(Qdrantのデフォルト)。

- **疎検索:**  
  疎ベクトル表現(例: BM25)を使用したキーワードベース検索。

- **ハイブリッド検索:**  
  相互ランク融合(RRF)やDBSFなどのスコア融合技術を使用して、密と疎の結果を組み合わせます。マルチステージおよびマルチモーダルクエリをサポート; [Hybrid Search Revamped](https://qdrant.tech/articles/hybrid-search/)および[Hybrid Queries Documentation](https://qdrant.tech/documentation/concepts/hybrid-queries/)参照。

- **ハイブリッドクエリの例:**  
  密検索とキーワード検索の結果を組み合わせて、関連性と再現率の両方を最大化。

### 11. **クライアントとSDK**

- **サポート言語:**  
  - [Python](https://github.com/qdrant/qdrant-client)
  - [Go](https://github.com/qdrant/go-client)
  - [Rust](https://github.com/qdrant/rust-client)
  - [JavaScript/TypeScript](https://github.com/qdrant/qdrant-js)
  - [Java](https://github.com/qdrant/java-client)
  - [C#](https://github.com/qdrant/qdrant-dotnet)

- **例:**
  ```python
  from qdrant_client import QdrantClient
  client = QdrantClient(url="http://localhost:6333")
  ```

- **APIリファレンスとチュートリアル:**  
  [Qdrant API Documentation](https://qdrant.tech/documentation/api/)参照。

### 12. **Qdrant Cloud**

- **定義:**  
  フルマネージド、エンタープライズグレードのQdrantホスティング。スケーリング、ゼロダウンタイムアップグレード、モニタリング、永久無料ティアを提供。

- **利点:**  
  サーバー管理不要。シングルテナントおよびマルチテナントデプロイメントをサポートし、高度なセキュリティとコンプライアンス機能を備えています。

> [Qdrant Cloud Overview](https://qdrant.tech/cloud/)

## Qdrantの使用方法

Qdrantは、AI、検索、分析アプリケーションの幅広い分野で展開されています。柔軟なAPIと高速なベクトル検索により、人気のフレームワークやクラウドインフラストラクチャとの統合が可能です。

### **1. セマンティック検索**

**目標:**  
キーワードの一致だけでなく、類似した意味を持つドキュメント、製品、メディアを返す。

**Qdrantの役割:**  
- すべてのアイテムのベクトル埋め込みを保存。
- ユーザークエリを埋め込み、高い類似性を持つベクトルを検索(例: コサイン)。
- バッチ検索、フィルタリング、ハイブリッド(セマンティック+キーワード)クエリをサポート。

**例:**  
「このサポートチケットにセマンティック的に類似したFAQを見つける。」

**コード:**
```python
results = client.search(
    collection_name="faq_collection",
    query_vector=query_embedding,
    limit=5
)
```

> [LangChain Integration for RAG and Semantic Search](https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant)

### **2. レコメンデーションシステム**

**目標:**  
学習された類似性に基づいて関連アイテム(製品、コンテンツ、ユーザー)を提案。

**Qdrantの役割:**  
- ユーザーとアイテムの両方の埋め込みを保存。
- ドット積または[コサイン類似度](/ja/glossary/cosine-similarity/)を使用して最適なマッチを見つける。

**例:**  
「このユーザーが視聴したものに類似した映画を推薦する。」

> [Vector Search Resource Optimization Guide](https://qdrant.tech/articles/vector-search-resource-optimization/)

### **3. 検索拡張生成(RAG)**

**目標:**  
サポートドキュメントを動的に検索することで、LLMに関連コンテキストを提供。

**Qdrantの役割:**  
- すべてのドキュメントの埋め込みを保存。
- ユーザークエリを埋め込み、LLMコンテキストとしてトップk件の結果を検索。
- フィルタリング、[バッチ処理](/ja/glossary/batch-processing/)、ハイブリッド検索をサポート。

> [RAG Example: Qdrant, Cohere, Airbyte, AWS](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/)

### **4. 異常検知**

**目標:**  
高次元データにおける外れ値や異常なパターンを検出(例: 不正検知)。

**Qdrantの役割:**  
- 履歴イベント埋め込みを保存。
- 新しいイベントを埋め込み、最近傍を見つける。
- 近傍からの大きな距離は異常を示します。

### **5. マルチモーダル検索とクラスタリング**

**目標:**  
テキスト、画像、構造化データを一緒に扱う。分類や分析のためにアイテムをクラスタリング。

**Qdrantの役割:**  
- ポイントごとに複数の名前付きベクトルを保存(例: 画像とテキスト)。
- ベクトル類似性とメタデータフィルタリングを使用してクラスタリング。

### **6. AIエージェントオーケストレーション**

**目標:**  
分散AIエージェントがメモリを共有し、アクションを調整できるようにする。

**Qdrantの役割:**  
- コンテキストメモリをベクトルとして保存/検索。
- ステートフルなAIエージェントシステムのための高速でフィルタリングされた検索。

## 例: 実践的統合

**Pythonの例:**
```python
from qdrant_client import QdrantClient, models

# Qdrantに接続
client = QdrantClient("http://localhost:6333")

# 1. コレクションを作成
client.create_collection(
    collection_name="products",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)

# 2. ポイント(ベクトル+ペイロード)を挿入
client.upsert(
    collection_name="products",
    points=[
        models.PointStruct(
            id=1,
            vector=[0.1, 0.2, 0.3, ...],
            payload={"category": "books", "author": "Alice"}
        ),
        # さらにポイント...
    ]
)

# 3. 類似ベクトルを検索
query_vector = [0.15, 0.18, 0.28, ...]
results = client.search(
    collection_name="products",
    query_vector=query_vector,
    limit=3
)

for hit in results:
    print(hit.id, hit.payload)
```
> 高度な使用法(ハイブリッド検索、フィルタリング、バッチ操作)については、[Qdrant Python Client Docs](https://qdrant.tech/documentation/quick-start/)をご覧ください。

## 機能比較表

| 機能                     | Qdrant                 | 従来のDB(SQL/NoSQL) |
|-----------------------------|------------------------|----------------------------|
| データモデル                  | ベクトル(埋め込み)   | 行/列またはドキュメント  |
| クエリタイプ                  | 類似性検索      | 完全一致、範囲、結合  |
| フィルタリング                   | ペイロード(メタデータ)     | 列、フィールド            |
| インデックス作成                    | [HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/)、ハイブリッド           | Bツリー、ハッシュ、テキストインデックス  |
| ストレージモード               | RAM、Memmap、量子化 | RAM、ディスク                  |
| ユースケース                   | セマンティック、RAG、RecSys、異常検知 | OLTP、OLAP、CRUD      |
| マルチモーダルデータ             | はい                    | 限定的                    |
| クラウドネイティブスケーラビリティ    | はい(Qdrant Cloud)     | 様々                     |

> [What is a Vector Database? (Qdrant)](https://qdrant.tech/articles/what-is-a-vector-database/)

## 実世界のユースケース

- **エンタープライズRAG:**  
  ナレッジベースの回答を関連ドキュメントとともに取得するチャットボットやデジタルアシスタント。

- **Eコマースレコメンデーション:**  
  パーソナライズされた製品提案、「類似アイテム」カルーセル。

- **不正検知:**  
  トランザクション埋め込みを比較することによるリアルタイム異常検知。

- **ヘルスケア:**  
  診断と治療推奨のための患者類似性検索。

- **産業IoT:**  
  センサーデータ分析と予知保全。

- **コンテンツモデレーション:**  
  重複およびポリシー違反チェックのための類似画像、テキスト、音声の検出。

> [顧客事例の詳細と
