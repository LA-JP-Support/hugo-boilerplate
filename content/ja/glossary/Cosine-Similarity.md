---
title: コサイン類似度
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: cosine-similarity
description: コサイン類似度は、2つの非ゼロベクトル間の角度のコサインを測定する指標で、大きさではなく方向性に基づいてそれらの類似性を評価します。機械学習、自然言語処理、レコメンデーションシステムで広く使用されています。
keywords:
- コサイン類似度
- 機械学習
- 自然言語処理
- レコメンデーションシステム
- ベクトル類似度
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Cosine Similarity
term: こさいんるいじど
url: "/ja/glossary/cosine-similarity/"
aliases:
- "/ja/glossary/Cosine-Similarity/"
---
## コサイン類似度とは?
コサイン類似度は、内積空間における2つの非ゼロベクトル間の角度のコサインを計算する定量的指標です。この指標は、データマイニング、機械学習、人工知能において広く使用され、2つのベクトルがどれだけ類似しているかを、大きさではなく方向性のみに基づいて評価します。方向性に焦点を当てることが根本的な利点であり、文書埋め込みや特徴ベクトルなどの高次元表現に最適です。

**公式:**  
\[
\text{Cosine Similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \times \|\mathbf{B}\|}
\]

ここで:
- \(\mathbf{A} \cdot \mathbf{B}\): ベクトルAとBの内積
- \(\|\mathbf{A}\|\)、\(\|\mathbf{B}\|\): 各ベクトルのユークリッドノルム(大きさ)
- \(\theta\): ベクトル間の角度

**解釈:**
- スコア **1**: ベクトルが同じ方向を向いている(完全な類似性)
- スコア **0**: ベクトルが直交している(類似性なし)
- スコア **-1**: ベクトルが反対方向を向いている(最大の非類似性)

ほとんどの実用的なアプリケーション(テキストマイニング、埋め込み)では非負のベクトルを使用するため、コサイン類似度スコアは通常0から1の範囲になります。

## 数学的説明

### ステップバイステップの計算

2つの非ゼロベクトルが与えられた場合:
\[
\mathbf{A} = [a_1, a_2, \ldots, a_n]
\]
\[
\mathbf{B} = [b_1, b_2, \ldots, b_n]
\]

**1. 内積:**  
\[
\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i b_i
\]

**2. 大きさ(ユークリッドノルム):**  
\[
\|\mathbf{A}\| = \sqrt{\sum_{i=1}^{n} a_i^2}
\]
\[
\|\mathbf{B}\| = \sqrt{\sum_{i=1}^{n} b_i^2}
\]

**3. コサイン類似度:**  
\[
\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \times \|\mathbf{B}\|}
\]

### 計算例

\(\mathbf{A} = [3, 2, 0, 5]\)、\(\mathbf{B} = [1, 0, 0, 0]\)とします。

- 内積: \(3*1 + 2*0 + 0*0 + 5*0 = 3\)
- Aの大きさ: \(\sqrt{3^2 + 2^2 + 0^2 + 5^2} = \sqrt{38} \approx 6.16\)
- Bの大きさ: \(\sqrt{1^2 + 0^2 + 0^2 + 0^2} = 1\)
- コサイン類似度: \(3 / (6.16 * 1) \approx 0.49\)

**コサイン非類似度:**  
非類似度は\(1 - \text{Cosine Similarity}\)として計算されることが多いです。上記の例では、\(D_C(\mathbf{A}, \mathbf{B}) = 1 - 0.49 = 0.51\)となります。

## 視覚的直感

多次元空間で同じ原点から始まる2本の矢印を想像してください:

- **0°(コサイン = 1):** 矢印が重なり、同一方向を示す
- **90°(コサイン = 0):** 矢印が直角で、関連性がない
- **180°(コサイン = -1):** 矢印が反対方向で、完全な非類似性を示す

## 実装例

### 主要なライブラリ

**NumPy**  
ベクトル化演算に効率的です。

**scikit-learn**  
ペアワイズ類似度行列のための`sklearn.metrics.pairwise.cosine_similarity`。

**TensorFlow**  
組み込みのCosineSimilarity損失関数。

**PyTorch**  
`torch.nn.CosineSimilarity`。

**ベクトルデータベース**  
PostgreSQL用のpgvectorなどの拡張機能。

### Pythonの例(NumPy)

```python
import numpy as np

def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

A = [1, 2, 3]
B = [4, 5, 6]
similarity = cosine_similarity(A, B)
print("Cosine similarity:", similarity)  # Output: 0.9746318461970762
```

## 応用とユースケース

### 1. 文書類似度と検索エンジン
文書とクエリは、TF-IDFやニューラル埋め込みを使用して高次元ベクトルに変換されます。コサイン類似度は、ベクトルの方向を比較することでコンテンツの関連性を測定します。

### 2. 推薦システム
ユーザーとアイテムの嗜好がベクトルとしてエンコードされます。最も高いコサイン類似度を持つアイテムやユーザーを見つけることで推薦が行われます。

### 3. 自然言語処理(NLP)と埋め込み
コサイン類似度は、単語、文、または文書の埋め込みを比較する際に重要です。これにより意味的類似性が定量化され、セマンティック検索、言い換え検出、クラスタリングが可能になります。

### 4. コンピュータビジョンと姿勢推定
身体の姿勢や画像特徴を表すキーポイントベクトルは、コサイン類似度を使用して構成の類似性を評価するために比較されます。

### 5. 不正検出と異常検出
多次元のトランザクションベクトルを比較し、コサイン類似度を使用して異常なパターンをフラグ付けします。

## 利点と欠点

### 利点

**大きさに非感応**  
方向のみが重要です。異なる長さのベクトルでも高い類似性を持つことができます。

**高次元での堅牢性**  
スパースで高次元のデータセット(例:テキスト分析、埋め込み)でうまく機能します。

**計算効率**  
計算は簡単で、主要な機械学習ライブラリで最適化されています。

**正規化が組み込み**  
入力ベクトルを明示的に正規化する必要がありません。

### 制限事項

**大きさを無視**  
同じ方向を向いている小さなベクトルと大きなベクトルを区別できません。

**ゼロベクトルで未定義**  
いずれかのベクトルがゼロベクトルの場合、コサイン類似度は定義されません。

**対称性**  
\(\text{CosineSimilarity}(A, B) = \text{CosineSimilarity}(B, A)\)であり、比較の方向性を考慮しません。

**スパース性に敏感**  
非ゼロ要素の重なりが少ない極端にスパースなデータでは性能が低下する可能性があります。

## 他の類似度指標との比較

| 指標 | 焦点 | 大きさに敏感 | 最適な用途 |
|--------|-------|------------------------|----------|
| **コサイン類似度** | 方向 | いいえ | テキスト、埋め込み |
| **ユークリッド距離** | 位置 | はい | 数値、物理データ |
| **ジャッカード類似度** | 重複/集合 | いいえ | 集合、バイナリ属性 |

**ユークリッド距離:** 直線距離を測定し、方向と大きさの両方に影響されます。絶対的な差が重要な場合に有用です。

**ジャッカード類似度:** 集合間の重複を測定し、カテゴリカルまたはバイナリ特徴(例:共有タグ)に最適です。

**内積:** 大きさを含むため、スケールが異なる場合は誤解を招く可能性があります。

## ベストプラクティスと実用的なヒント

**1. データの正規化**  
ゼロベクトルを削除し、すべてのベクトルが非ゼロであることを確認して、未定義の結果を防ぎます。

**2. スパースデータの処理**  
高次元でスパースなデータを扱う場合は、スパース行列に最適化されたライブラリを使用します。

**3. 指標の組み合わせ**  
より豊かな類似性分析のために、コサイン類似度を他の指標とモデル特徴として組み合わせます。

**4. 一貫した前処理**  
すべてのベクトルが同じプロセス/モデルから生成され、同じ次元数を持つことを確認します。

**5. 慎重な解釈**  
高いコサイン類似度が常に意味的等価性を意味するわけではありません。文脈とドメイン知識が不可欠です。

**6. 堅牢なライブラリの活用**  
NumPy、scikit-learn、TensorFlow、またはpgvectorの組み込み関数を使用します。

## 参考文献

- [GeeksforGeeks: Cosine Similarity](https://www.geeksforgeeks.org/dbms/cosine-similarity/)
- [IBM: What is Cosine Similarity](https://www.ibm.com/think/topics/cosine-similarity)
- [IBM: Natural Language Processing](https://www.ibm.com/think/topics/natural-language-processing)
- [IBM: Recommendation Engines](https://www.ibm.com/think/topics/recommendation-engine)
- [IBM: Embedding Techniques](https://www.ibm.com/think/topics/embedding)
- [IBM: Image Recognition](https://www.ibm.com/think/topics/image-recognition)
- [IBM: Fraud Detection](https://www.ibm.com/think/topics/fraud-detection)
- [IBM: Bag of Words (TF-IDF)](https://www.ibm.com/think/topics/bag-of-words)
- [IBM: Principal Component Analysis](https://www.ibm.com/think/topics/principal-component-analysis)
- [Wikipedia: Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Wikipedia: Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)
- [Built In: Understanding Cosine Similarity](https://builtin.com/machine-learning/cosine-similarity)
- [Tiger Data: A Guide to Cosine Similarity](https://www.tigerdata.com/learn/understanding-cosine-similarity)
- [YouTube: Cosine Similarity, StatQuest](https://www.youtube.com/watch?v=e9U0QAFbfLI)
- [GeeksforGeeks: Python Measure Similarity Between Two Sentences](https://www.geeksforgeeks.org/machine-learning/python-measure-similarity-between-two-sentences-using-cosine-similarity/)
- [GeeksforGeeks: Euclidean Distance](https://www.geeksforgeeks.org/maths/euclidean-distance/)
- [scikit-learn: Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- [scikit-learn: Euclidean Distance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
- [scikit-learn: Sparse Matrices](https://scikit-learn.org/stable/modules/scipy_sparse.html)
- [NumPy: Linear Algebra (linalg)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [TensorFlow: CosineSimilarity Loss](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity)
- [PyTorch: CosineSimilarity](https://pytorch.org/docs/stable/generated/torch.nn.CosineSimilarity.html)
- [pgvector: PostgreSQL Vector Search](https://github.com/pgvector/pgvector)
