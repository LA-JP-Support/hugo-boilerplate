---
title: Chroma
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: chroma
description: AI ネイティブアプリケーション向けのオープンソースベクトルデータベース、Chroma について解説します。コアコンセプト、アーキテクチャ、RAG
  やセマンティック検索などのユースケース、そして代替ソリューションとの比較について学びましょう。
keywords:
- Chroma
- ベクトルデータベース
- エンベディング
- AI ネイティブアプリケーション
- セマンティック検索
category: General
type: glossary
draft: false
e-title: Chroma
term: クロマ
url: "/ja/glossary/Chroma/"
---
## Chromaとは?
Chromaは、AI-native アプリケーション、特に大規模言語モデル(LLM)やマルチモーダルAIを使用するアプリケーション向けに設計されたオープンソースのベクトル(埋め込み)データベースです。従来のデータベースとは異なり、Chromaは高次元ベクトル埋め込み(テキスト、画像、その他の非構造化データの数値表現)の保存、インデックス化、検索に特化しています。

Chromaの中核的な使命は、開発者や組織が最小限のセットアップと最大限の柔軟性で、セマンティック検索、レコメンデーション、RAG、AI-nativeの機能をアプリケーションに追加できるようにすることです。

**主な特徴:**
- ドキュメントとメタデータと共に埋め込みを保存・検索するネイティブサポート
- HNSWインデックスによる高速な近似最近傍(ANN)検索
- マルチモーダルサポート(テキスト、画像など)
- ハイブリッドクエリ:セマンティック検索+キーワード検索、メタデータフィルタリング
- 開発者フレンドリーなAPI(Python、JS)、LangChainやLlamaIndexなどのフレームワークとのネイティブ統合
- オープンソースApache 2.0ライセンス
- セルフホスト型とマネージドクラウドの両方のオプション

## コアコンセプト

### 埋め込み
埋め込みは、データのセマンティックな意味をエンコードする密なベクトルです。例えば、文章、画像、音声クリップは、数百または数千の数値のベクトルに変換できます。意味が類似したデータポイントは、元のデータが大きく異なっていても、類似した埋め込み(つまり、ベクトル空間で「近い」)を持ちます。

Chromaは、以下を含む人気のあるモデルで生成された埋め込みをサポートしています:
- OpenAIのtext-embeddingモデル(例:`text-embedding-3-small`)
- HuggingFaceモデル(例:`all-MiniLM-L6-v2`)
- Cohere、OpenCLIP、カスタム埋め込み

これは、セマンティック検索、レコメンデーション、検索拡張生成の基礎となります。

### コレクション
Chromaのコレクションは、ドキュメント、埋め込み、および関連するメタデータの論理的なグループです。各コレクションには、埋め込み関数/モデル、保存場所(インメモリまたは永続)、パフォーマンスやフィルタリングのためのオプションのカスタム設定を含む独自の構成があります。

これにより、別々のAIアプリケーションやプロジェクトを並行して実行でき、それぞれが特定のニーズに合わせて調整されます。

### メタデータとハイブリッド検索
Chromaでは、各ドキュメントまたはベクトルに任意のキー・バリューのメタデータを関連付けることができます。これにより、ハイブリッド検索が可能になります:メタデータ(例:著者、日付、タグ)で結果をフィルタリングし、ベクトル類似度でランク付けします。

サポートされる演算子には、等価・不等価、範囲クエリ(`$gt`、`$lt`)、集合メンバーシップ(`$in`)、論理結合(`$and`、`$or`)が含まれます。

## Chromaの仕組み

### ベクトルインデックスと類似度検索
Chromaは、高速な近似最近傍(ANN)検索のために階層的ナビゲート可能スモールワールド(HNSW)グラフを使用します。HNSWは、高次元ベクトル類似度検索のための最先端のアルゴリズムで、再現率(精度)と速度のバランスを取り、数百万のベクトルにスケールします。

**主な特性:**
- 大規模データセットに対する準線形検索時間
- 高い再現率/精度(設定可能)
- 動的な挿入と効率的な削除をサポート

### ドキュメントとメタデータの保存
Chromaの各エントリには、生のドキュメント/コンテンツ(テキスト、画像URI等)、ベクトル埋め込み、および関連するメタデータ(任意のキー・バリューJSON)が含まれます。これにより、ハイブリッドクエリと完全なセマンティック検索が可能になります。

Chromaはデータを以下の方法で保存できます:
- インメモリ(最速、非永続)
- ディスク上(メタデータ用SQLite、ベクトル用バイナリファイル)
- Chroma Cloud(完全マネージド)

### APIとクライアントライブラリ
Chromaは、4つの主要な操作を持つ最小限で直感的なAPIを提供します:
- **Add:** ドキュメントを挿入(オプションで埋め込みとメタデータ付き)
- **Update:** 保存されたエントリを変更
- **Delete:** エントリを削除
- **Query:** ベクトル検索で類似ドキュメントを取得、オプションのメタデータフィルタ付き

Python(`chromadb`)とJavaScript/TypeScript用のクライアントライブラリが存在します。ChromaはLangChainやLlamaIndexなどのフレームワークとネイティブに統合されます。

## アーキテクチャとデプロイメント

### オープンソース(セルフホスト)
Chromaは、ローカルまたは独自のインフラストラクチャで3つのモードで実行できます:

**インメモリ:** 高速、一時的、プロトタイピングやテストに最適  
**永続:** ディスクにデータを保存(SQLite + バイナリベクトルファイル)、ローカル/小規模本番環境に適している  
**クライアント-サーバー:** スタンドアロンサーバーとして実行、HTTP API経由で接続(マルチユーザー、マルチプロセスをサポート)

**サーバー起動例:**
```shell
chroma run --path ./db --port 8000
```

**Pythonクライアント:**
```python
import chromadb
client = chromadb.HttpClient(host="localhost", port=8000)
```

### Chroma Cloud(サーバーレス)
Chroma Cloudは完全マネージドのサーバーレスデプロイメントです。弾力的なスケーリング、自動バックアップと高可用性、メンテナンスとモニタリングを処理します。

**接続例:**
```python
import chromadb
client = chromadb.HttpClient(
    host="api.trychroma.com",
    headers={"Authorization": f"Bearer {CHROMA_API_KEY}"}
)
```

## セットアップと統合

### インストール

**Python:**
```bash
pip install chromadb
```

LangChain統合の場合:
```bash
pip install langchain-chroma
```

### 基本的な使用例

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("documents")

collection.add(
    documents=[
        "Artificial intelligence is transforming healthcare diagnostics",
        "Machine learning models predict patient outcomes with increasing accuracy",
        "Neural networks analyze medical imaging faster than radiologists"
    ],
    ids=["doc1", "doc2", "doc3"]
)

results = collection.query(
    query_texts=["AI applications in medicine"],
    n_results=2
)

print(results)
```

このコードは、コレクションを作成し、ドキュメントを挿入し、セマンティック検索クエリを実行します。

### 埋め込み関数の設定
Chromaコレクションは異なる埋め込みモデルを使用できます。OpenAI埋め込みを使用するには:

```python
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

openai_ef = OpenAIEmbeddingFunction(
    api_key="your-api-key",
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="openai_embeddings",
    embedding_function=openai_ef
)
```

### LangChain統合
LangChainは、RAG、チャットボット、メモリなどの高度なワークフローをサポートする、Chroma用のネイティブラッパーを提供します。

**例:**
```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)
```

## コア機能

**オープンソースApache 2.0** - ロックインなし、拡張可能、コミュニティ駆動(GitHub Stars 24k+)  
**高速ANN検索** - 準線形検索時間のためのHNSWグラフインデックス  
**ドキュメントとメタデータの保存** - 各埋め込みはドキュメントとユーザー定義のメタデータに関連  
**ハイブリッド検索** - セマンティック(ベクトル)検索とキーワード検索を組み合わせ  
**マルチモーダルサポート** - テキスト、画像などを保存/検索  
**バッチ操作** - 効率のための一括挿入とクエリ  
**シンプルなAPI** - 追加、更新、削除、検索  
**統合** - LangChain、LlamaIndex、OpenAI、HuggingFace、Cohere、OpenCLIPとネイティブ統合  
**柔軟なデプロイメント** - インメモリ、永続、クライアント-サーバー、マネージドクラウド  
**活発なコミュニティ** - Discord、GitHub、ドキュメント

## 主なユースケース

### セマンティック検索
Chromaは、キーワードだけでなく埋め込みを比較することでセマンティック検索を実現します。アプリケーションには、eコマース(「快適な夏の靴」を検索すると、異なる表現でも関連する結果を返す)、ナレッジマネジメント(社内wiki、サポートチケット、コードベース全体を検索)、ヘルスケア(類似のケース、研究、診断画像を検索)が含まれます。

### レコメンデーションシステム
埋め込みの類似性により類似したアイテム/ユーザーを見つけます。パーソナライズされた製品/ニュース/記事のレコメンデーション、アイテム間またはユーザー間のマッチングを可能にします。

### 検索拡張生成(RAG)
RAGにより、LLMはリアルタイムで外部ナレッジベースにアクセスでき、精度が向上し、ハルシネーションが減少します。チャットボットは特定のドキュメントを引用し、アシスタントは最新の企業知識で回答します。

### 画像、音声、マルチモーダル検索
画像、テキストなどを共有ベクトル空間に埋め込みます。ビジュアル検索(類似画像を検索)、クロスモーダル(テキストで画像を検索、逆も可)、マルチメディアデータセットの整理を可能にします。

### チャットボットとAIアプリケーション
ChromaはLLMとチャットボットのための永続的なセマンティックメモリとして機能します。会話履歴や関連する知識スニペットを取得し、コンテキストを考慮した応答を実現します。

### データサイエンスと分析
高次元データの探索的データ分析、金融/セキュリティログの異常検知、ナレッジグラフやセマンティックマップの構築をサポートします。

## パフォーマンス最適化

Chromaは開発者の速度と効率のために設計されていますが、最適化のヒントには以下が含まれます:

**バッチ操作** - オーバーヘッドを減らすために一括で挿入/クエリ  
**埋め込み次元数** - 低次元ベクトルはメモリ使用量が少なく、検索が高速(精度の犠牲を伴う可能性あり)  
**インデックス圧縮** - 頻繁な削除/更新後にHNSWインデックスを圧縮  
**メタデータ事前フィルタリング** - 類似度計算前にメタデータでフィルタリングして計算量を削減

**例:**
```python
collection.add(
    documents=large_document_list,
    ids=id_list,
    metadatas=metadata_list
)
```

## 比較と代替

### Chroma vs. Pinecone、Faiss、Weaviate、Qdrant、Milvus

| 機能 | Chroma | Pinecone | Faiss | Weaviate | Qdrant | Milvus |
|---------|--------|----------|-------|----------|--------|--------|
| **オープンソース** | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **セットアップの容易さ** | 非常にシンプル | マネージド、簡単 | 複雑 | 中程度 | 中程度 | 中程度 |
| **言語サポート** | Python、JS | Python、JS、Go | Python、C++ | Python、JS、Go | Python、REST | Python、REST |
| **ベクトルインデックス** | HNSW | 複数 | 複数 | HNSW、その他 | HNSW | IVF、HNSW |
| **ドキュメント保存** | 組み込み | なし | なし | 組み込み | 組み込み | 組み込み |
| **メタデータフィルタリング** | あり | あり | 制限あり | あり | あり | あり |
| **ハイブリッド検索** | あり | なし | なし | あり | なし | なし |
| **クラウド/サーバーレス** | Chroma Cloud | あり | なし | あり | あり | あり |
| **RBAC/マルチテナンシー** | なし | あり | なし | あり | あり | あり |
| **スケール** | シングルノード | 分散 | ローカル、分散 | 分散 | 分散 | 分散 |
| **最適用途** | 開発速度、プロトタイピング | 大規模 | 研究、カスタムML | エンタープライズ検索 | 高パフォーマンス | 超大規模 |

**エコシステムスナップショット:**
- **Chroma:** OSS、簡単なセットアップ、ハイブリッド検索、プロトタイピング/開発速度に最適
- **Pinecone:** マネージド、分散、エンタープライズグレード、マルチインデックスサポート、高スケール
- **Faiss:** OSS、研究/ML重視、C++/Python、データベースではない(ドキュメント/メタデータ保存なし)
- **Weaviate:** OSS、分散、ハイブリッド検索、スキーマ、マルチテナント
- **Qdrant:** OSS、分散、フィルタリング、REST/gRPC、高パフォーマンス
- **Milvus:** OSS、クラウドネイティブ、GPUサポート、超高スケール

## 参考文献


1. Chroma. GitHub Repository. URL: https://github.com/chroma-core/chroma
2. Chroma. Documentation. URL: https://docs.trychroma.com/
3. LangChain. Chroma Integration Documentation. URL: https://docs.langchain.com/oss/python/integrations/providers/chroma
4. Netflix. Chaos Monkey. URL: https://netflix.github.io/chaosmonkey/
5. Pinecone. Documentation. URL: https://www.pinecone.io/
6. Facebook Research. Faiss GitHub Repository. URL: https://github.com/facebookresearch/faiss
7. Weaviate. Documentation. URL: https://weaviate.io/
8. Qdrant. Documentation. URL: https://qdrant.tech/
9. Milvus. Documentation. URL: https://milvus.io/
