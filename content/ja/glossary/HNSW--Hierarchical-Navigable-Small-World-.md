---
title: HNSW(階層的ナビゲート可能スモールワールド)
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: hnsw-hierarchical-navigable-small-world
description: HNSW(Hierarchical Navigable Small World)は、ベクトルデータベースにおける高速かつ高精度な近似最近傍(ANN)検索のためのグラフベースアルゴリズムで、高次元データに最適です。
keywords:
- HNSW
- 近似最近傍探索
- ベクトル検索
- ベクトルデータベース
- グラフアルゴリズム
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: HNSW (Hierarchical Navigable Small World)
term: エイチエヌエスダブリュー(かいそうてきなびげーとかのうすもーるわーるど)
url: "/ja/glossary/HNSW--Hierarchical-Navigable-Small-World-/"
---
## HNSWとは?

HNSW(Hierarchical Navigable Small World)は、高次元ベクトル空間における高速、スケーラブル、かつ高精度な近似最近傍(ANN)検索のための近接グラフアルゴリズムです。ベクトルデータベースやAI駆動型アプリケーションで広く使用されており、HNSWは全数検索を行わずにクエリに最も近いアイテム(ベクトル)を見つけます。特に大規模なインメモリ環境において、速度と再現率の両面で多くの従来のANNアルゴリズムを凌駕しています。

**目的:** 大規模な高次元データセットにおける高再現率の効率的なANN検索。

**主要な革新:** スモールワールドグラフ(高速ナビゲーション)とスキップリスト的な階層構造(マルチスケール検索)を組み合わせています。

**応用分野:** セマンティック文書検索、画像/動画検索、レコメンデーションエンジン、LLMコンテキスト検索、異常検知。

## 中核概念

**ベクトル検索とANN:**  
ベクトル検索は、クエリに最も近い(最も類似した)ベクトルを探します。各データポイントは高次元ベクトル(768次元のBERTや1536次元のOpenAI埋め込み)として表現されます。総当たり検索はデータセットサイズに対して線形にスケール(O(N))し、大規模コレクションには実用的ではありません。

HNSWのような近似最近傍(ANN)アルゴリズムは、わずかな再現率の損失を許容することで検索時間を劇的に短縮し、数百万から数十億のベクトルに対するリアルタイムアプリケーションに不可欠な準線形時間複雑度を実現します。

**ナビゲート可能なスモールワールドグラフ:**  
スモールワールドグラフは、局所的リンクと長距離リンクにより、ほとんどのノードが少ないホップ数で他のノードに到達できるネットワークです。NSWグラフは貪欲ルーティングを可能にします:各ステップで、クエリに最も近い隣接ノードに移動します。NSWグラフは対数または準対数の検索複雑度を持ちます。

**階層構造(スキップリスト):**  
スキップリストは階層化された連結リストで、上位層がより長いジャンプを提供し、検索を高速化します。HNSWは同様の階層構造を導入し、各ベクトルは幾何分布に従ってランダムに層数が割り当てられます。上位層は疎(高速トラバーサル)、下位層は密(精密検索)です。この階層構造により、効率的な粗から密へのナビゲーションが可能になります。

## HNSWの動作原理

**グラフ構造:**  
HNSWは多層の有向近接グラフを作成します:

- **最上層** – 最も少ないノード数で長距離エッジを持つ
- **中間層** – 徐々に密になり、短距離接続を持つ
- **最下層(レイヤー0)** – すべてのベクトルが短距離の最近傍接続を持つ

各ノードは幾何分布(確率p、多くの場合1/ln(N))を使用して最高層が割り当てられ、層ごとのノード数が高さとともに指数関数的に減少することで、対数的な検索複雑度を実現します。

**検索プロセス:**

1. 最上層のエントリーノードから開始
2. 貪欲トラバーサル:クエリベクトルに最も近い隣接ノードに繰り返し移動
3. 局所最小値に到達したら、次の下位層に降下して繰り返す
4. 候補ノードの優先度キュー(efSearchパラメータでサイズ制御)を維持
5. 検索完了後、k個の最も近いベクトルを返す

このプロセスは、グローバルナビゲーションに長距離リンクを、局所的な絞り込みに短距離リンクを活用します。

**グラフ構築:**

1. 各新規ベクトルにランダムな層割り当て(幾何分布)
2. 各層で貪欲検索を実行するトップダウントラバーサル
3. 各層で新規ノードをM個の最近傍に接続
4. 割り当てられた層を降下し、各層で接続し、レイヤー0に到達するまで続ける

この増分的で確率的なプロセスにより、動的で効率的なインデックス構築が可能になります。

**主要パラメータ:**

- **M(最大隣接数)** – ノードごとの隣接数を制御。高いMは再現率とメモリを増加
- **efConstruction** – 構築時に考慮される候補数。高い値はより良い品質をもたらすが、構築時間が増加
- **efSearch** – 検索時に考慮される候補数。高い値は再現率を増加させるが、クエリレイテンシも増加

**トレードオフ:**  
Mまたはef*を増やすと再現率が向上しますが、メモリフットプリントやレイテンシが増加します。下げるとRAMが削減され、クエリが高速化されますが、再現率が低下する可能性があります。

**複雑度:**

- メモリ: N個のベクトルに対してO(M*N)エッジ
- インデックス構築時間: 高いefConstructionでO(N log N)
- 検索: 適切に調整されたグラフで期待O(log N)ホップ

## 他のANNアルゴリズムとの比較

| アルゴリズム | 構造 | 長所 | 短所 | 最適な使用例 |
|-----------|-----------|------|------|----------------|
| **HNSW** | グラフ + 階層 | 高再現率、動的、最先端 | 高メモリ、複雑性 | ほとんどのベクトルDB、AIワークロード |
| **KD-Tree** | ツリー | シンプル、低次元 | 高次元で劣化 | 小規模/低次元データセット |
| **IVF** | フラットクラスタ | ディスクスケーラブル、シンプル | 低再現率、静的インデックス | 数十億規模、低再現率 |
| **LSH** | ハッシュバケット | 高速、メモリ効率的 | 低再現率、ランダム | 高次元、ハッシングシナリオ |

**研究知見:**  
最近の研究では、グラフ内の「ハブ」(接続性の高いノード)がナビゲーション速度と再現率において、階層構造自体よりも重要な役割を果たすことが示されています。

## 実装

**Python + Faiss:**
```python
import faiss
import numpy as np

d = 128  # vector dimension
M = 32   # neighbors
index = faiss.IndexHNSWFlat(d, M)
index.hnsw.efConstruction = 200

index.add(xb)  # add vectors
index.hnsw.efSearch = 50
D, I = index.search(xq, k)  # search
```

**PostgreSQL + pgvector:**
```sql
CREATE INDEX document_embedding_idx 
ON document_embedding 
USING hnsw(embedding vector_cosine_ops);
```

**Redis:**
```bash
FT.CREATE docs_idx ON HASH PREFIX 1 docs: 
SCHEMA doc_embedding VECTOR HNSW 512 
TYPE FLOAT32 DISTANCE_METRIC COSINE M 16 EF_CONSTRUCTION 32
```

**パラメータチューニング:**  
デフォルトから開始: M=16–32、efConstruction=100–200、efSearch=40–100。

- 高再現率: efSearchやMを増やす
- 高速クエリ/低メモリ: MまたはefSearchを減らす
- 常に代表的なデータで再現率とレイテンシを測定

**エンジニアリングノート:**

- サポートされている場合は並列構築を使用
- 動的ワークロードで「孤島」を避けるために接続性を監視
- 頻繁な更新には増分挿入/削除を使用

## 応用例

**セマンティックテキスト検索:**  
ベクトル類似度による関連文書、FAQ、コードスニペットの検索を強化。顧客クエリ「パスワードをリセット」が埋め込まれ、数百万のサポート文書に対してミリ秒単位でマッチング。

**画像/動画検索:**  
大規模カタログから視覚的に類似したアセットを検索。写真が与えられると、1000万の製品から視覚的に類似した画像のトップを検索。

**製品レコメンデーション:**  
埋め込み類似度を使用して類似アイテム、記事、トラックを提案。

**異常検知:**  
クラスタ中心からの距離により、時系列、グラフ、ログの外れ値を検出。

**LLMコンテキスト検索:**  
チャットボットやアシスタント向けのRAG(Retrieval Augmented Generation)パイプラインを実現。

## 強みと課題

**強み:**

- ANNにおける最先端の再現率と速度
- 動的:完全な再構築なしで効率的な増分挿入/削除をサポート
- 柔軟性:M、efConstruction、efSearchによりアプリケーション固有のチューニングが可能
- 広範なサポート:Faiss、Milvus、Pinecone、Vespa、Redis、pgvector、Weaviate

**課題:**

- メモリ集約的:グラフ構造(O(M*N)エッジ)が大量のRAMを使用
- RAMを超えるスケーリング:インメモリインデックスのみ。RAMを超えるデータセットにはハイブリッドまたはディスクベースのインデックスが必要
- パラメータ感度:不適切な設定は再現率や速度を低下させる
- 複雑性:デバッグ、監視、分散シャーディングがツリーやハッシュベースの方法より困難

**緩和策:**

- 大規模問題には次元削減(PCA)または量子化を適用
- 大規模データセットにはハイブリッドHNSW+IVFまたはストリーミング/ディスクベースのアルゴリズムを使用
- 孤立ノードがないことを確認するために接続性と再現率を監視

## 高度なトピック

**フィルタリングとハイブリッド検索:**

- 事前フィルタリング:HNSW検索の前/中にメタデータやブール型フィルタを適用
- 事後フィルタリング:ANN後に検索結果をフィルタ。より高いefSearchが必要な場合あり
- ハイブリッドインデックス:HNSWをIVFまたはディスクベースの方法と組み合わせ

**次元削減:**  
PCA、UMAP、ランダム射影などの技術によりベクトルサイズを削減し、最小限の再現率損失でメモリと速度を改善。ベクトル量子化によりRAM使用量をさらに削減。

**分散環境:**  
HNSWはシャード可能。各シャードはデータパーティションとローカルHNSWインデックスを保持。分散HNSWはより複雑で、クエリのブロードキャストまたはグローバルインデックス経由のルーティングが必要。ベクトルDB(Milvus、Redis Cluster、Pinecone)はクラスタ管理と分散HNSWをネイティブにサポート。

## 参考文献

- [HNSW Original Paper (arXiv)](https://arxiv.org/abs/1603.09320)
- [Pinecone: Hierarchical Navigable Small Worlds (HNSW)](https://www.pinecone.io/learn/series/faiss/hnsw/)
- [Zilliz: HNSW Technical Deep Dive](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)
- [Redis: How HNSW Algorithms Can Improve Search](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/)
- [arXiv: Down with the Hierarchy - The 'H' in HNSW Stands for 'Hubs'](https://arxiv.org/html/2412.01940v1)
- [Zilliz: Vector Similarity Search](https://zilliz.com/learn/vector-similarity-search)
- [Pinecone: What is Similarity Search?](https://www.pinecone.io/learn/what-is-similarity-search/)
- [Wikipedia: Small-world Network](https://en.wikipedia.org/wiki/Small-world_network)
- [Wikipedia: Skip List](https://en.wikipedia.org/wiki/Skip_list)
- [Pinecone: Probability Skip List](https://www.pinecone.io/learn/series/faiss/hnsw/#Probability-Skip-List)
- [Pinecone: HNSW Structure Diagram](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fe63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png&w=3840&q=75)
- [Faiss HNSW Documentation](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes#hnsw)
- [pgvector HNSW Docs](https://github.com/pgvector/pgvector#hnsw)
- [Redis HNSW Documentation](https://redis.io/docs/latest/develop/interact/search-and-query/advanced-concepts/vectors/#hnsw-index)
- [Milvus HNSW Documentation](https://milvus.io/docs/hnsw.md#HNSW)
- [Zilliz: DiskANN and Vamana Algorithm](https://zilliz.com/learn/DiskANN-and-the-Vamana-Algorithm)
