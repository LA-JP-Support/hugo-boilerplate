---
title: HNSW(階層的ナビゲート可能スモールワールド)
date: 2025-11-25
translationKey: hnsw-hierarchical-navigable-small-world
description: HNSW(Hierarchical Navigable Small World)は、ベクトルデータベースにおける高速かつ高精度な近似最近傍(ANN)検索のためのグラフベースアルゴリズムで、高次元データに最適です。
keywords: ["HNSW", "近似最近傍探索", "ベクトル検索", "ベクトルデータベース", "グラフアルゴリズム"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: HNSW (Hierarchical Navigable Small World)
term: エイチエヌエスダブリュー(かいそうてきなびげーとかのうすもーるわーるど)
reading: HNSW(階層的ナビゲート可能スモールワールド)
kana_head: その他
---
## HNSWとは?

HNSW(Hierarchical Navigable Small World、階層的ナビゲート可能スモールワールド)は、高次元ベクトル空間における高速で拡張性が高く正確な*近似最近傍(ANN)検索*のための近接グラフアルゴリズムです。ベクトルデータベースやAI駆動型アプリケーションにおいて、全数検索を行わずにクエリに最も近いアイテム(ベクトル)を見つけるために広く使用されています。HNSWは、特に大規模なインメモリ環境において、速度と再現率の両面で多くの従来のANNアルゴリズムを凌駕しています。

- **目的:** 大規模かつ高次元データセットにおける高再現率の効率的なANN検索。
- **主要な革新:** スモールワールドグラフ(高速ナビゲーション用)とスキップリスト様の階層構造(マルチスケール検索用)の長所を組み合わせています。
- **典型的な応用:** セマンティック文書検索、画像/動画検索、レコメンデーションエンジン、LLMコンテキスト検索、異常検知。
## コアコンセプト

### ベクトル検索とANN

*ベクトル検索*は、クエリに最も近い(最も類似した)ベクトルを探索します。各データポイントは高次元ベクトル(768次元のBERTや1536次元のOpenAI埋め込みなど)として表現されます。ブルートフォース検索はデータセットサイズに対して線形にスケールする(O(N))ため、大規模コレクションでは実用的ではありません。

HNSWのような**近似最近傍(ANN)アルゴリズム**は、わずかな再現率(精度)の損失を許容することで検索時間を劇的に短縮し、準線形時間計算量を実現します。これは、数百万から数十億のベクトルに対するリアルタイムアプリケーションにとって重要です。
### ナビゲート可能スモールワールドグラフ(NSW)

*スモールワールドグラフ*は、局所的リンクと長距離リンクの両方により、ほとんどのノードが少数のホップで他のすべてのノードから到達可能なネットワークです。NSWグラフでは、各ノードは最近傍ノードに接続し、一部は遠方のノードにも接続することで、貪欲ルーティングを可能にします:各ステップで、クエリに最も近い隣接ノードに移動します。

- NSWグラフは対数または多重対数の検索複雑度を持ちます[Zilliz](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)。
- *貪欲検索*プロセスは、クエリへの最短利用可能パスをたどります。
### スキップリストと階層構造

*スキップリスト*は階層化された連結リストで、上位層がより長いジャンプを提供し、検索を高速化します([Skip List, Wikipedia](https://en.wikipedia.org/wiki/Skip_list)参照)。HNSWは同様の階層構造を導入しています:

- 各ベクトルは、幾何分布に従って出現する層数がランダムに割り当てられます。
- 上位層は疎で高速な横断を提供し、下位層は密で精密な検索を保証します。

この階層構造により、効率的な粗から細へのナビゲーションが可能になります。
## HNSWの動作原理

### グラフ層と構造

HNSWは多層の有向近接グラフを作成します:

- **最上層:** 最も少数のノードを含み、各ノードは長距離エッジを持ちます。
- **中間層:** 徐々に密になり、より短距離の接続を持ちます。
- **最下層(レイヤー0):** すべてのベクトルを含み、短距離(最近傍)接続を持ちます。

各ノードは幾何分布(確率p、多くの場合1/ln(N))を使用して最高層が割り当てられ、層ごとのノード数が高さとともに指数関数的に減少することを保証します([arXiv](https://arxiv.org/abs/1603.09320))。この構造により、実際には対数的な検索複雑度が実現されます。

**可視化:**  
- [Pinecone HNSW Structure Diagram](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fe63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png&w=3840&q=75)

### 検索プロセス

1. **最上層から開始:** 指定されたエントリーノードから。
2. **貪欲横断:** 各レベルで、クエリベクトルに最も近い隣接ノードに繰り返し移動します。
3. **局所最小値:** どの隣接ノードもより近くない場合、次の下位層に降下して繰り返します。
4. **候補リスト:** 最下層で、候補ノードの優先度キュー(サイズは`efSearch`パラメータで制御)を維持します。
5. **結果:** 検索完了後、k個の最近傍ベクトルを返します。

このプロセスは、グローバルナビゲーションには長距離リンクを、局所的な絞り込みには短距離リンクを活用することで、高速で正確な検索を保証します。
### グラフ構築(挿入)

1. **ランダム層割り当て:** 各新規ベクトルは、幾何分布を使用してランダムに最高層を取得します。
2. **トップダウン横断:** 最上層から開始し、各層で貪欲検索を実行して最も近いエントリーポイントを見つけます。
3. **接続:** 各層で、新しいノードをM個の最近傍ノードに接続します(Mは調整可能なパラメータ)。
4. **繰り返し:** 割り当てられた層を降下し、各層で接続を行い、レイヤー0に到達するまで続けます。

**重要な洞察:** この増分的で確率的なプロセスにより、動的で効率的なインデックス構築が可能になります。
### 主要パラメータとトレードオフ

- **M(最大隣接数):** ノードあたりの隣接数を制御します。Mが高いほど再現率とメモリ使用量が増加します。
- **efConstruction:** 構築中に考慮される候補数。値が高いほどインデックス品質が向上しますが、構築時間が増加します。
- **efSearch:** 検索中に考慮される候補数。値が高いほど再現率が向上しますが、クエリレイテンシが増加します。

**トレードオフ:**
- Mまたはef*を増やすと再現率が向上しますが、メモリフットプリントやレイテンシが増加します。
- これらを下げるとRAMが削減され、クエリが高速化されますが、再現率が低下する可能性があります。

**数学的複雑度:**
- **メモリ:** Nベクトルに対してO(M*N)エッジ。
- **インデックス構築時間:** 高いefConstructionでO(N log N)。
- **検索:** 適切に調整されたグラフでO(log N)の期待ホップ数。
## 他のANNアルゴリズムとの比較

| アルゴリズム        | 構造      | 長所                  | 短所                        | 最適な使用ケース                |
|------------------|---------------|-----------------------|-----------------------------|-------------------------------|
| **HNSW**         | グラフ + 階層 | 高再現率、動的、最先端 | 高メモリ、複雑性     | ほとんどのベクトルDB、AIワークロード |
| **KD-Tree**      | ツリー          | シンプル、低次元        | 高次元で劣化        | 小規模/低次元データセット        |
| **IVF**          | フラットクラスタ | ディスクスケーラブル、シンプル  | 低再現率、静的インデックス  | 数十億規模、低再現率  |
| **LSH**          | ハッシュバケット  | 高速、メモリ効率的 | 低再現率、ランダム        | 高次元、ハッシングシナリオ   |

**ベンチマークと研究:**  
- [arXiv: "Down with the Hierarchy: The 'H' in HNSW Stands for 'Hubs'" (2024)](https://arxiv.org/html/2412.01940v1): 階層構造の実際の影響を研究し、グラフ内の「ハブ」(接続性の高いノード)がナビゲーション速度と再現率において、階層構造自体よりも重要な役割を果たす場合があることを発見しています。
- [Redis: HNSW vs. IVF/LSH](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/): HNSWがインメモリデータベースのデフォルトとして選ばれることが多い理由を説明し、IVFとLSHはディスク制約またはストリーミングシナリオに適していることを示しています。

## 実装と使用方法

### 人気ライブラリでのHNSW使用

#### Python + Faiss

```python
import faiss
import numpy as np

d = 128        # ベクトル次元
M = 32         # 隣接数
ef_construction = 200
ef_search = 50

index = faiss.IndexHNSWFlat(d, M)
index.hnsw.efConstruction = ef_construction

# ベクトルを追加
index.add(xb)  # xb = 形状(num_vectors, d)のnp.ndarray

# 検索
index.hnsw.efSearch = ef_search
D, I = index.search(xq, k)  # xq = クエリベクトル、k = 上位k個
```
- [Faiss HNSW documentation](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes#hnsw)

#### PostgreSQL + pgvector

```sql
CREATE INDEX document_embedding_idx ON document_embedding USING hnsw(embedding vector_cosine_ops);
```
- [pgvector HNSW docs](https://github.com/pgvector/pgvector#hnsw)

#### Redis

```bash
FT.CREATE docs_idx ON HASH PREFIX 1 docs: SCHEMA doc_embedding VECTOR HNSW 512 TYPE FLOAT32 DISTANCE_METRIC COSINE M 16 EF_CONSTRUCTION 32
```
- [Redis HNSW documentation](https://redis.io/docs/latest/develop/interact/search-and-query/advanced-concepts/vectors/#hnsw-index)

#### Milvus

- [Milvus HNSW documentation](https://milvus.io/docs/hnsw.md#HNSW)
- [Zilliz HNSW guide](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)

### パラメータチューニング: 実践的ガイダンス

デフォルト値から開始: M=16–32、efConstruction=100–200、efSearch=40–100。

- より高い再現率のため: efSearchやMを増やします。
- より高速なクエリ/低メモリのため: MまたはefSearchを減らします。
- 最終決定前に、代表的なデータで常に再現率とレイテンシを測定してください。

**エンジニアリングノート:**
- サポートされている場合は並列構築を使用します(例: Faiss、Redis)。
- 動的ワークロードの場合、「孤島」を避けるために定期的に接続性を監視します。
- 頻繁な更新の場合は、増分挿入/削除を使用します。
## アプリケーションと使用ケース

- **セマンティックテキスト検索:** ベクトル類似度(埋め込み検索)による関連文書、FAQ、コードスニペットの検索を強化。
- **画像/動画検索:** 大規模カタログから視覚的に類似したアセットを検索。
- **製品またはコンテンツレコメンデーション:** 埋め込み類似度を使用して類似アイテム、記事、トラックを提案。
- **異常検知:** 距離をクラスタ中心からの距離により、時系列、グラフ、ログ内の外れ値を検出。
- **LLMコンテキスト検索:** チャットボットやアシスタント向けのRAG(Retrieval Augmented Generation)パイプラインを実現。

**例(セマンティック検索):**  
顧客クエリ「パスワードをリセット」が埋め込まれ、HNSWを使用して数百万のサポート文書に対してミリ秒単位でマッチングされます。

**例(画像検索):**  
写真が与えられた場合、1000万製品のデータセットから視覚的に類似した上位画像を検索します。
## 強みと課題

### 強み

- **高性能:** ANNにおける最先端の再現率と速度。
- **動的:** 完全な再構築なしで効率的な増分挿入/削除をサポート。
- **柔軟性:** M、efConstruction、efSearchにより、アプリケーション固有のチューニングが可能。
- **広範なサポート:** Faiss、[Milvus](/ja/glossary/milvus/)、Pinecone、Vespa、Redis、pgvector、[Weaviate](/ja/glossary/weaviate/)に統合。

### 課題

- **メモリ集約的:** グラフ構造(O(M*N)エッジ)は、特に大きなMまたは高カーディナリティで大量のRAMを使用する可能性があります。
- **RAMを超えるスケーリング:** インメモリインデックスのみ。RAMを超えるデータセットの場合、ハイブリッド(ディスク+RAM)またはディスクベースのインデックス(DiskANN、Vamanaなど)が必要です([Zilliz: DiskANN](https://zilliz.com/learn/DiskANN-and-the-Vamana-Algorithm))。
- **パラメータ感度:** 不適切な設定は再現率や速度を低下させる可能性があり、慎重なチューニングが必要です。
- **複雑性:** デバッグ、監視、分散シャーディングは、ツリーベースやハッシュベースの方法よりも困難な場合があります。

**緩和戦略:**
- 大規模で高次元の問題には、次元削減(例: PCA)または量子化を適用します。
- 大規模データセットの場合、ハイブリッドHNSW+IVFまたはストリーミング/ディスクベースのアルゴリズムを使用します。
- 孤立ノードがないことを確認するために、接続性と再現率を監視します。
## 高度なトピック

### フィルタリングとハイブリッド検索

- **事前フィルタリング:** HNSW検索の前または最中にメタデータまたはブール値フィルタを適用。
- **事後フィルタリング:** ANN後に検索結果をフィルタリング。補償のためにより高いefSearchが必要になる場合があります。
- **ハイブリッドインデックス:** RAM制限またはストリーミング使用ケースのために、HNSWをIVFまたはディスクベースの方法と組み合わせます。

### 次元削減

- PCA、UMAP、ランダム投影などの技術により、ベクトルサイズを削減し、最小限の再現率損失でメモリと速度を改善できます。
- ベクトル量子化により、超大規模展開でRAM使用量をさらに削減できます。

### 分散/シャード環境

- HNSWはシャード可能です。各シャードはデータのパーティションとローカルHNSWインデックスを保持します。
- 分散HNSWはより複雑で、シャード間検索にはクエリのブロードキャストまたはグローバルインデックス経由のルーティングが必要です。
- 一部のベクトルDB([Milvus](/ja/glossary/milvus/)、Redis Cluster、Pinecone)は、クラスタ管理と分散HNSWをネイティブにサポートしています。
- [Redis: HNSW Sharding](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/)
## 参考資料

- [HNSW original paper (arXiv)](https://arxiv.org/abs/1603.09320)
- [Pinecone: Hierarchical Navigable Small Worlds (HNSW)](https://www.pinecone.io/learn/series/faiss/hnsw/)
- [Zilliz: HNSW Technical Deep Dive](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)
- [Redis: How HNSW Algorithms Can Improve Search](https://redis.io/blog/how-hnsw-algorithms-can-improve-search/)