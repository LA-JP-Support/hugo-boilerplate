---
title: Weaviate
date: 2025-11-25
translationKey: weaviate
description: Weaviateは、オブジェクトと高次元埋め込みを保存するオープンソースのクラウドネイティブなベクトルデータベースです。セマンティック検索、ハイブリッド検索、大規模なAI/MLアプリケーションを可能にします。
keywords: ["Weaviate", "ベクトルデータベース", "セマンティック検索", "ベクトル埋め込み", "ハイブリッド検索"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Weaviate
term: ウィービエイト
reading: Weaviate
kana_head: その他
---
## Weaviateとは?

**Weaviate**は、構造化データオブジェクトと高次元ベクトル埋め込みの両方を保存するために特別に設計された、オープンソースのクラウドネイティブなベクトルデータベースです。そのアーキテクチャは、高度なセマンティック検索、ハイブリッド検索、大規模なAI/MLアプリケーションを可能にします。

- **オープンソース**: BSD-3-Clauseライセンスの下で提供され、Weaviateは強力な開発者コミュニティと透明性の高いコードベースを特徴としています([Weaviate GitHub](https://github.com/weaviate/weaviate))。
- **クラウドネイティブ**: Kubernetes、パブリッククラウド、またはオンプレミスインフラストラクチャ全体で、分散型で回復力があり、スケーラブルなデプロイメント向けに設計されています([Weaviate Deployment Docs](https://docs.weaviate.io/deploy))。
- **オブジェクトとベクトルの統合**: Weaviateは、従来のオブジェクトプロパティとそれに対応するベクトル表現の両方を保存するという独自の特徴を持ち、類似性検索やセマンティック検索に最適です([Weaviate Docs](https://docs.weaviate.io/weaviate))。
## コアコンセプト

### ベクトルとベクトル埋め込み

- **ベクトル埋め込み**: ベクトル埋め込みは、テキスト、画像、音声などのデータからセマンティックな意味を捉えるために機械学習モデルによって生成される数値配列(多くの場合、数百から数千の浮動小数点数)です([DataCamp: Vector Embeddings](https://www.datacamp.com/blog/vector-embedding))。例えば、*「AIデータベース」*というフレーズは`[0.12, -0.98, 1.54, ...]`のようになる可能性があります。
- **オブジェクト**: Weaviateでは、オブジェクトはベクトル埋め込みと共に保存されるデータエントリ(ドキュメント、画像、製品など)です。このペアリングにより、データベース内で直接強力なセマンティック検索と類似性検索が可能になります。

> **詳細:**  
> [Vector Embeddings Explained](https://weaviate.io/blog/vector-embeddings-explained)  
> [Embeddings and Vector Databases (Medium)](https://medium.com/@vladris/embeddings-and-vector-databases-732f9927b377)

### ベクトルインデックス

数十億のベクトルを効率的に検索するために、Weaviateは専用のインデックス構造を使用します([Vector Indexing Docs](https://docs.weaviate.io/weaviate/concepts/vector-index)):

- **フラットインデックス**: 小規模なデータセットやマルチテナントケースに最適な、シンプルで軽量な構造です。ベクトルを順番に保存し、検索は正確ですが線形時間です。
- **HNSWインデックス(Hierarchical Navigable Small World)**: グラフベースのインデックスで、対数的な検索複雑度を持ち、大規模な近似最近傍(ANN)クエリに最適化されています。[HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/)は本番環境でのデフォルトです([HNSW explained](https://docs.weaviate.io/weaviate/concepts/vector-index#hierarchical-navigable-small-world-hnsw-index))。
- **ダイナミックインデックス**: フラットインデックスとして開始し、設定されたしきい値を超えると自動的に[HNSW](/ja/glossary/hnsw--hierarchical-navigable-small-world-/)に変換され、取り込み速度とクエリパフォーマンスのバランスを取ります。

> **技術詳細:**  
> [Vector Index Configuration](https://docs.weaviate.io/weaviate/config-refs/indexing/vector-index)  
> [Choosing an Index Type](https://docs.weaviate.io/weaviate/concepts/vector-index#which-vector-index-is-right-for-me)

### シャーディングとクラスタリング

**シャーディング**は、コレクションを複数のシャードに分割し、それぞれが独自のベクトルインデックスとオブジェクトストアを持ち、ノード間に分散されて水平スケールと回復力を実現します。シャードにより、単一の論理データベースを複数のサーバーにまたがらせ、ストレージと計算能力を倍増させることができます([Cluster Concepts](https://docs.weaviate.io/weaviate/concepts/cluster))。

**レプリケーション**は、シャードの冗長コピーを作成し、[高可用性](/ja/glossary/high-availability--ha-/)とフォールトトレランスを確保します。Weaviateは、データにはリーダーレスで最終的に一貫性のあるレプリケーションモデルを使用し、メタデータにはRaftコンセンサスを使用して、堅牢な分散デプロイメントを可能にします([Cluster Architecture](https://docs.weaviate.io/weaviate/concepts/replication-architecture/cluster-architecture))。

![Weaviate Sharding](https://docs.weaviate.io/assets/images/shards_explained-9a5f2cea95faf0d860cbd63ec77f73cb.png)
## Weaviateの主要機能

- **セマンティック検索**: クエリは、キーワードだけでなく意味によってデータを取得し、学習されたベクトル埋め込みを使用します([Weaviate Search Basics](https://docs.weaviate.io/weaviate/search/basics))。
- **ハイブリッド検索**: ベクトル類似性と従来のキーワード検索(BM25、ブール論理)を組み合わせて、比類のない関連性を実現します([Hybrid Search Docs](https://docs.weaviate.io/weaviate/search/hybrid))。
- **検索拡張生成(RAG)サポート**: LLMに事実に基づいた最新の知識を提供するベクトルストアバックエンドとして機能します([Weaviate RAG](https://weaviate.io/rag)、[LangChain Integration](https://weaviate.io/blog/enterprise-workflow-langchain-weaviate))。
- **マルチテナンシー**: 単一のクラスター内でテナント(顧客、チームなど)間でデータと計算を分離します([Multi-Tenancy Docs](https://docs.weaviate.io/weaviate/concepts/data#multi-tenancy))。
- **スケーラビリティとクラスタリング**: データをシャーディングおよびレプリケートして、線形スケールと[高可用性](/ja/glossary/high-availability--ha-/)を実現します([Clustering Docs](https://docs.weaviate.io/weaviate/concepts/cluster))。
- **モデル統合**: OpenAI、Cohere、HuggingFace、Google、AWS、NVIDIAなど、15以上のMLプロバイダーをすぐに使用できます([Model Provider List](https://docs.weaviate.io/weaviate/model-providers))。
- **エージェントAI**: 自律的な推論とワークフロー実行を必要とするエージェント駆動型アプリケーションの基盤([Agent Framework](https://docs.weaviate.io/agents))。
- **エンタープライズ対応**: RBAC、暗号化、監査ログ、SOC 2、HIPAAなどへの準拠を含む機能。
- **柔軟なデプロイメント**: Weaviateをセルフホスト、マネージドサービス(Weaviate Cloud)、Kubernetes、またはPython/JS/TSアプリに組み込んで実行できます([Deployment Guide](https://docs.weaviate.io/deploy))。

> **包括的な機能リスト:**  
> [Weaviate Platform Features](https://weaviate.io/platform#open-source-vector-database-features)

## 技術詳細

### ベクトル埋め込み

Weaviateのベクトル埋め込みは、機械学習モデルによって生成され、オブジェクトのセマンティック特性をエンコードします。統合されたモデルプロバイダーを使用してネイティブに作成するか、外部パイプラインからインポートできます([Model Providers](https://docs.weaviate.io/weaviate/model-providers))。

- 埋め込みは、類似したオブジェクトをベクトル空間内で近くに配置し、セマンティック検索とクラスタリングを可能にします。

### ベクトルインデックスと近似最近傍(ANN)検索

- **HNSW**: HNSWインデックスは、高速でスケーラブルなANN検索のために多層グラフを構築します。数百万または数十億のベクトルを持つデータセットに効率的です([HNSW in Weaviate](https://docs.weaviate.io/weaviate/concepts/vector-index#hierarchical-navigable-small-world-hnsw-index))。
- **フラット**: 直接的な線形スキャン—小規模なデータセットやマルチテナントシナリオに適しています。
- **ダイナミック**: データが増加するにつれて、フラットからHNSWに自動的に移行します。
- **圧縮**: PQ、SQ、BQ圧縮オプションにより、メモリ使用量と検索速度をさらに最適化します([Compression Docs](https://docs.weaviate.io/weaviate/configuration/compression))。

### ハイブリッド検索

- BM25キーワード検索とベクトル類似性を統合し、単一のクエリで語彙的およびセマンティック的な関連性を組み合わせます([Hybrid Search Docs](https://docs.weaviate.io/weaviate/search/hybrid))。
- ハイブリッドクエリは、最適な結果を得るためにブレンド比率を調整できます。

### マルチテナンシー

- 各テナントは、データと計算が厳密に分離された独立したシャード(またはシャードのセット)を取得します([Multi-Tenancy Docs](https://docs.weaviate.io/weaviate/concepts/data#multi-tenancy))。

### クラスタリング、シャーディング、レプリケーション

- クラスターは、ノード間でシャードを分散することでスケールアウトします([Cluster Docs](https://docs.weaviate.io/weaviate/concepts/cluster))。
- レプリケーションは、データにリーダーレスモデルを使用し、メタデータにRaftを使用して、[高可用性](/ja/glossary/high-availability--ha-/)と回復力をサポートします([Replication Architecture](https://docs.weaviate.io/weaviate/concepts/replication-architecture/cluster-architecture))。

### モデルと言語の統合

- 主要なプロバイダー(OpenAI、Anthropic、AWS、Cohere、HuggingFace、Google、NVIDIAなど)に接続します([Full Model Provider List](https://docs.weaviate.io/weaviate/model-providers))。
- APIベースとセルフホスト推論の両方をサポートします。

### APIとSDK

- **GraphQL API**: すべての操作に対応する柔軟で強力なクエリ機能。
- **REST API**: CRUDと検索のための従来のHTTPエンドポイント。
- **SDK**: Python、Go、JavaScript、TypeScript、Java用の公式ライブラリ([SDK Reference](https://docs.weaviate.io/weaviate/client-libraries))。
- [Weaviate Recipes](https://github.com/weaviate/recipes): すべてのSDKとユースケースのための実用的なコードサンプル。

## クエリ例

#### 1. 純粋なベクトル検索
```python
response = collection.query.near_vector(
    near_vector=[0.1, 0.1, 0.1],
    limit=5
)
```

#### 2. セマンティック検索
```python
response = collection.query.near_text(
    query="login issues after OS upgrade",
    limit=5
)
```

#### 3. ハイブリッド検索
```python
response = collection.query.hybrid(
    query="login issues after OS upgrade",
    alpha=0.75,
    limit=5
)
```

> **クイックスタート:** [15〜30分でWeaviateを試す](https://docs.weaviate.io/weaviate/quickstart)

## ユースケースと業界アプリケーション

| ユースケース                       | 説明                                                                                 | 例                                                   |
|---------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **セマンティック検索**             | キーワードだけでなく、意味で検索します。                                                         | 「アカウントロックアウト」に関連するサポートチケットを検索       |
| **検索拡張生成(RAG)** | プライベートデータでLLM出力を強化します。                                      | 企業のナレッジベースに基づいたチャットボット                |
| **レコメンデーションシステム**      | 類似またはパーソナライズされたアイテムを提案します。                                                      | eコマースでの製品レコメンデーション                     |
| **チャットボットと仮想エージェント**   | コンテキストを認識したAI会話を可能にします。                                                      | 意図理解を備えたカスタマーサービスボット           |
| **コンテンツ分類**      | 非構造化データにタグ付けして整理します。                                                        | トピックの類似性によってニュースを自動ラベル付け                       |
| **画像とマルチメディア検索**   | ファイル名だけでなく、コンテンツ/画像の類似性で検索します。                                     | サンプルに視覚的に類似した画像を検索                   |
| **不正検出**             | 複雑なデータ内の異常なトランザクションパターンを発見します。                                       | 既知のケースとのセマンティック類似性による不正検出     |

> **その他の例:** [Weaviate Use Cases](https://weaviate.io/solutions)

**業界例**: eコマース(セマンティック検索、レコメンデーション)、メディア(コンテンツ発見)、ヘルスケア(臨床文書検索)、金融(不正検出)、エンタープライズAI検索([Industry Solutions](https://weaviate.io/solutions))。

## デプロイメントオプション

- **セルフホスト**: Docker、ベアメタル、またはVM上で実行([Local Install](https://docs.weaviate.io/weaviate/quickstart/local))。
- **マネージドクラウド**: 高度なセキュリティとエンタープライズ機能を備えたWeaviateによる完全管理([Weaviate Cloud](https://weaviate.io/cloud))。
- **Kubernetes**: 公式Helmチャートを使用してスケーラブルなマイクロサービスとして実行([K8s Deployment Guide](https://docs.weaviate.io/deploy/installation-guides/k8s-installation))。
- **組み込み**: 迅速なプロトタイピングのためにPythonまたはJS/TSから直接起動([Embedded deployment](https://docs.weaviate.io/deploy/embedded))。

## 統合とエコシステム

- **モデルプロバイダー**: Anthropic、AWS、Cohere、Google、Hugging Face、NVIDIA、OpenAI、Mistral、Voyage AI、Databricks、JinaAIなどと統合([Full List](https://docs.weaviate.io/weaviate/model-providers))。
- **プラグインとフレームワーク**: Haystack、LangChain、LlamaIndex、CrewAI、Semantic Kernelなどとのネイティブ統合([Integrations](https://docs.weaviate.io/integrations/llm-agent-frameworks/langchain))。
- **データプラットフォーム**: Airbyte、Box、Databricks、IBM、Unstructuredなど([Data Platform Integrations](https://docs.weaviate.io/integrations/data-platforms/airbyte))。
- **モニタリングと運用**: Arize、Comet、Cleanlab、Weights & Biases、Langtraceなど([Ops Integrations](https://docs.weaviate.io/integrations/operations/arize))。
- **コミュニティ**: 15,000以上のGitHubスター、50,000以上の開発者、活発な[Slackチャンネル](https://weaviate.io/slack)。

## 他のベクトルデータベースとの比較

| 機能                           | **Weaviate**                | Pinecone | [Milvus](/ja/glossary/milvus/) | [Chroma](/ja/glossary/chroma/) | Qdrant |
|------------------------------------|-----------------------------|----------|--------|--------|--------|
| **オープンソース**                   | はい(BSD-3-Clause)          | いいえ       | はい    | はい    | はい    |
| **組み込みモデル統合**    | はい(15以上のプロバイダー)         | 限定的  | 限定的| いいえ     | 限定的|
| **ハイブリッド検索**                 | はい(ネイティブ)                | 部分的  | 部分的| いいえ     | はい    |
| **マルチテナンシー**                 | はい                         | はい      | はい    | いいえ     | はい    |
| **RAGとエージェントサポート**         | はい                         | はい      | はい    | はい    | はい    |
| **デプロイメントの柔軟性**        | ローカル、クラウド、K8s、組み込み | クラウド    | ローカル  | ローカル  | ローカル  |
| **エンタープライズ機能**           | RBAC、暗号化、監査     | はい      | はい    | いいえ     | はい    |

> **参考資料:**  
> [What is a Vector Database?](https://weaviate.io/blog/what-is-a-vector-database)

## Weaviateを始める

### クイックスタート手順

1. **インスタンスを起動:**  
   - [Weaviate Cloud Quickstart](https://docs.weaviate.io/weaviate/quickstart)
   - [Local Docker Quickstart](https://docs.weaviate.io/weaviate/quickstart/local)
2. **データを接続:** SDKを使用してオブジェクトとベクトルをインポートします。
3. **ベクトル化:** 組み込みモデル統合を使用するか、事前計算されたベクトルをインポートします。
4. **クエリ:** APIまたはSDKを介してセマンティック、ハイブリッド、フィルタリングされた検索を実行します。
5. **スケール:** ノードを追加し、[マルチテナンシー](/ja/glossary/multi-tenancy/)を有効にし、バックアップを設定します。

> **完全なセットアップガイド:** [Weaviate Quickstart](https://docs.weaviate.io/weaviate/quickstart)

## 例: Python SDKを使用したセマンティック検索

```python
import weaviate

client = weaviate.Client("https://my-weaviate-instance")
collection = client.collections.get("SupportTickets")

# 「ログインの問題」に関するチケットのセマンティック検索
response = collection.query.near_text(
    query="login issues after OS upgrade",
    limit=5
)

for ticket in response.objects:
    print(ticket["title"], ticket["description"])
```

**その他のコードサンプル:**  
- [Weaviate Recipes GitHub](https://github.com/weaviate/recipes)

## コミュニティとサポート

- **オープンソース:**  
  - [Weaviate GitHub](https://github.com/weaviate/weaviate)
  - 機能リクエスト、貢献、コード閲覧。
- **ドキュメントとチュートリアル:**  
  - [Weaviate Docs](https://docs.weaviate.io/weaviate)
  - [Weaviate Academy](https://academy.weaviate.io/)
- **コミュニティ:**  
  - [Slack](https://weaviate.io/slack): Q&A、イベント、ディスカッション。
  - [Blog](https://weaviate.io/blog): 技術記事、アップデート、ケーススタディ。
- **サポート:**  
  - フォーラムとSlackを通じたコミュニティサポート。
  - エンタープライズ: Weaviate Cloudによる専用サポート。

> **お客様の声:**  
> 「Weaviateのバッテリー内蔵アプローチは、[モデルサービング](/ja/glossary/model-serving/)とマルチテナンシーの両方を組み込んでおり、ベクトル検索を迅速にプロトタイプ化して構築するのに役立ちました。」— Stack Overflowチーム

## FAQ

**Q: Weaviateはオープンソースですか?**  
A: はい、BSD-3-Clauseライセンスです([GitHub](https://github.com/weaviate/weaviate))。

**Q: 検索拡張生成(RAG)にWeaviateを使用できますか?**  
A: はい、WeaviateはRAGバックエンドとして広く使用されています([RAG Docs](https://weaviate.io/rag))。

**Q: Weaviateはハイブリッド検索をサポートしていますか?**  
A: はい、セマンティック(ベクトル)検索とキーワード(BM25)検索をネイティブに組み合わせます([Hybrid Search](https://docs.weaviate.io/weaviate/search/hybrid))。

**Q: どの言語とSDKが利用可能ですか?**  
A: Python、Go、JavaScript、TypeScript、Java、REST、GraphQL([SDK Reference](https://docs.weaviate.io/weaviate/client-libraries))。

**Q: Weaviateはスケーリングと高可用性をどのように処理しますか?**  
A: 水平シャーディング、クラスタリング、レプリケーション([Scaling Guide](https://docs.weaviate.io/weaviate/concepts/cluster))。

**Q: Weaviateはエンタープライズ用途に適していますか?**  
A: はい。RBAC、暗号化、監査ログを提供しています。