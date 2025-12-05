---
title: コサイン類似度
date: 2025-11-25
translationKey: cosine-similarity
description: コサイン類似度は、2つの非ゼロベクトル間の角度のコサインを測定する指標で、大きさではなく方向性に基づいてベクトルの類似性を評価します。機械学習、自然言語処理、レコメンデーションシステムで広く使用されています。
keywords: ["コサイン類似度", "機械学習", "自然言語処理", "レコメンデーションシステム", "ベクトル類似度"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Cosine Similarity
term: こさいんるいじど
reading: コサイン類似度
kana_head: か
---
## コサイン類似度とは?

コサイン類似度は、内積空間における2つの非ゼロベクトル間の角度のコサインを計算する定量的指標です。この指標は、データマイニング、機械学習、人工知能において広く使用されており、2つのベクトルがどれだけ類似しているかを、大きさではなく方向性のみに基づいて評価します。方向性に焦点を当てることが根本的な利点であり、文書埋め込みや特徴ベクトルなどの高次元表現に最適です([IBM: What is Cosine Similarity](https://www.ibm.com/think/topics/cosine-similarity)、[GeeksforGeeks: Cosine Similarity](https://www.geeksforgeeks.org/dbms/cosine-similarity/)を参照)。

**公式:**  
\[
\text{Cosine Similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \times \|\mathbf{B}\|}
\]
- \(\mathbf{A} \cdot \mathbf{B}\): ベクトルAとBの内積  
- \(\|\mathbf{A}\|\)、\(\|\mathbf{B}\|\): 各ベクトルのユークリッドノルム(大きさ)  
- \(\theta\): ベクトル間の角度

**解釈:**
- スコア **1**: ベクトルが同じ方向を向いている(完全な類似性)。
- スコア **0**: ベクトルが直交している(類似性なし)。
- スコア **-1**: ベクトルが反対方向を向いている(最大の非類似性)。

ほとんどの実用的なアプリケーション(テキストマイニング、埋め込み)では非負のベクトルを使用するため、コサイン類似度スコアは通常0から1の範囲になります。

## 数学的説明

**ステップバイステップの計算:**

2つの非ゼロベクトルが与えられた場合:
\[
\mathbf{A} = [a_1, a_2, \ldots, a_n]
\]
\[
\mathbf{B} = [b_1, b_2, \ldots, b_n]
\]

1. **内積:**  
   \[
   \mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i b_i
   \]

2. **大きさ(ユークリッドノルム):**  
   \[
   \|\mathbf{A}\| = \sqrt{\sum_{i=1}^{n} a_i^2}
   \]
   \[
   \|\mathbf{B}\| = \sqrt{\sum_{i=1}^{n} b_i^2}
   \]

3. **コサイン類似度:**  
   \[
   \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \times \|\mathbf{B}\|}
   \]

**計算例:**  
次のように設定します:  
\(\mathbf{A} = [3, 2, 0, 5]\)、  
\(\mathbf{B} = [1, 0, 0, 0]\)。

- 内積: \(3*1 + 2*0 + 0*0 + 5*0 = 3\)
- Aの大きさ: \(\sqrt{3^2 + 2^2 + 0^2 + 5^2} = \sqrt{9 + 4 + 0 + 25} = \sqrt{38} \approx 6.16\)
- Bの大きさ: \(\sqrt{1^2 + 0^2 + 0^2 + 0^2} = 1\)
- コサイン類似度: \(3 / (6.16 * 1) \approx 0.49\)

(参考: [GeeksforGeeks Example](https://www.geeksforgeeks.org/dbms/cosine-similarity/))

**コサイン非類似度:**  
多くの場合、非類似度は\(1 - \text{Cosine Similarity}\)として計算されます。上記の例では、\(D_C(\mathbf{A}, \mathbf{B}) = 1 - 0.49 = 0.51\)となります。

## 視覚的直感

多次元空間で同じ原点から始まる2つの矢印を想像してください:

- **0°(コサイン = 1):** 矢印が重なり、同一の方向を示します。
- **90°(コサイン = 0):** 矢印が直角で、関連性がないことを示します。
- **180°(コサイン = -1):** 矢印が反対方向で、完全な非類似性を示します。

視覚化については、[GeeksforGeeksの図](https://media.geeksforgeeks.org/wp-content/uploads/20200911171455/UntitledDiagram2.png)を参照してください。

**StatQuestビデオ解説:**  
[YouTube: Cosine Similarity, Clearly Explained!!! (StatQuest)](https://www.youtube.com/watch?v=e9U0QAFbfLI)

## 実装例

**主要なライブラリ:**
- **NumPy:** ベクトル化された演算に効率的([NumPy linalg documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html))
- **scikit-learn:** ペアワイズ類似度行列用の[`sklearn.metrics.pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)。
- **TensorFlow:** 組み込みの[CosineSimilarity loss](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity)
- **PyTorch:** [`torch.nn.CosineSimilarity`](https://pytorch.org/docs/stable/generated/torch.nn.CosineSimilarity.html)
- **ベクトルデータベース:** [pgvector for PostgreSQL](https://github.com/pgvector/pgvector)などの拡張機能

**Pythonの例(NumPy):**
```python
import numpy as np

def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

A = [1, 2, 3]
B = [4, 5, 6]
similarity = cosine_similarity(A, B)
print("Cosine similarity:", similarity)  # Output: 0.9746318461970762
```
詳細については、[GeeksforGeeks: Python Measure Similarity Between Two Sentences](https://www.geeksforgeeks.org/machine-learning/python-measure-similarity-between-two-sentences-using-cosine-similarity/)を参照してください。

## 応用とユースケース

**1. 文書類似度と検索エンジン**  
文書とクエリは、TF-IDFまたはニューラル埋め込みを使用して高次元ベクトルに変換されます。コサイン類似度は、ベクトルの方向を比較することでコンテンツの関連性を測定します。  
- [IBM: NLP and Cosine Similarity](https://www.ibm.com/think/topics/natural-language-processing)

**2. 推薦システム**  
ユーザーとアイテムの好みがベクトルとしてエンコードされます。最も高いコサイン類似度を持つアイテムまたはユーザーを見つけることで推薦が行われます。  
- [IBM: Recommendation Engines](https://www.ibm.com/think/topics/recommendation-engine#:~:text=A%20recommendation%20engine%2C%20also%20called,items%20based%20on%20those%20patterns.)

**3. 自然言語処理(NLP)と埋め込み**  
コサイン類似度は、単語、文、または文書の埋め込みを比較する際に重要です。これにより意味的類似性が定量化され、セマンティック検索、言い換え検出、クラスタリングが可能になります。  
- [IBM: Embedding Techniques](https://www.ibm.com/think/topics/embedding)

**4. コンピュータビジョンと姿勢推定**  
身体の姿勢や画像特徴を表すキーポイントベクトルは、コサイン類似度を使用して構成の類似性を評価するために比較されます。  
- [IBM: Image Recognition](https://www.ibm.com/think/topics/image-recognition#:~:text=Image%20recognition%20is%20an%20application,in%20digital%20images%20or%20video.)

**5. 不正検出と異常検出**  
多次元のトランザクションベクトルを比較し、コサイン類似度を使用して異常なパターンにフラグを立てます。  
- [IBM: Fraud Detection](https://www.ibm.com/think/topics/fraud-detection)

## 利点と欠点

**利点**
- **大きさに非感応:** 方向のみが重要であり、異なる長さのベクトルでも高い類似性を持つことができます([GeeksforGeeks](https://www.geeksforgeeks.org/dbms/cosine-similarity/))。
- **高次元での堅牢性:** 疎で高次元のデータセット(例:テキスト分析、埋め込み)でうまく機能します。
- **計算効率:** 計算が簡単で、主要な機械学習ライブラリで最適化されています。
- **正規化が組み込み:** 入力ベクトルを明示的に正規化する必要がありません。

**制限事項**
- **大きさを無視:** 同じ方向を向いている小さなベクトルと大きなベクトルを区別できません。
- **ゼロベクトルで未定義:** いずれかのベクトルがゼロベクトルの場合、コサイン類似度は定義されません。
- **対称性:** \(\text{CosineSimilarity}(A, B) = \text{CosineSimilarity}(B, A)\)であり、比較の方向性を考慮しません。
- **疎性に敏感:** 非ゼロ要素の重複が少ない極端に疎なデータでは性能が低下する可能性があります。

## 他の類似度指標との比較

| 指標               | 焦点       | 大きさへの感応性 | 最適な用途                   | 参考資料                                  |
|--------------------|-------------|-----------------------|----------------------------|---------------------------------------------|
| コサイン類似度  | 方向   | いいえ                    | テキスト、埋め込み           | [IBM](https://www.ibm.com/think/topics/cosine-similarity) |
| ユークリッド距離 | 位置    | はい                   | 数値、物理データ     | [GeeksforGeeks](https://www.geeksforgeeks.org/maths/euclidean-distance/) |
| Jaccard類似度 | 重複/集合 | いいえ                    | 集合、バイナリ属性    | [Wikipedia: Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index) |

- **ユークリッド距離:** 直線距離を測定し、方向と大きさの両方に影響されます。絶対的な差が重要な場合に有用です([scikit-learn Euclidean Distance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html))。
- **Jaccard類似度:** 集合間の重複を測定し、カテゴリカルまたはバイナリ特徴(例:共有タグ)に最適です。
- **内積:** 大きさを含むため、スケールが異なる場合は誤解を招く可能性があります。

## ベストプラクティスと実用的なヒント

1. **データの正規化:** ゼロベクトルを削除し、すべてのベクトルが非ゼロであることを確認して、未定義の結果を防ぎます。
2. **疎データの処理:** 高次元で疎なデータを扱う場合は、疎行列に最適化されたライブラリを使用します(例:[scikit-learn sparse matrices](https://scikit-learn.org/stable/modules/scipy_sparse.html))。
3. **指標の組み合わせ:** より豊かな類似性分析のために、コサイン類似度を他の指標とモデル特徴として組み合わせます。
4. **一貫した前処理:** すべてのベクトルが同じプロセス/モデルから生成され、同じ次元数を持つことを確認します。
5. **慎重な解釈:** 高いコサイン類似度が常に意味的等価性を意味するわけではありません。文脈とドメイン知識が不可欠です。
6. **堅牢なライブラリの活用:** [NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)、[scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)、[TensorFlow](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity)、または[pgvector](https://github.com/pgvector/pgvector)の組み込み関数を使用します。

## 参考資料

- [Cosine Similarity – GeeksforGeeks](https://www.geeksforgeeks.org/dbms/cosine-similarity/)
- [IBM: What is Cosine Similarity](https://www.ibm.com/think/topics/cosine-similarity)
- [Wikipedia: Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Built In: Understanding Cosine Similarity and Its Applications](https://builtin.com/machine-learning/cosine-similarity)
- [Tiger Data: A Guide to Cosine Similarity](https://www.tigerdata.com/learn/understanding-cosine-similarity)
- [YouTube: Cosine Similarity, StatQuest](https://www.youtube.com/watch?v=e9U0QAFbfLI)
- [scikit-learn: Cosine Similarity Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- [NumPy: Linear Algebra (linalg)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [TensorFlow: CosineSimilarity Loss](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity)
- [pgvector: PostgreSQL Vector Search Extension](https://github.com/pgvector/pgvector)

## 関連項目

- [ユークリッド距離](https://www.geeksforgeeks.org/maths/euclidean-distance/)
- [Jaccard類似度](https://en.wikipedia.org/wiki/Jaccard_index)
- [TF-IDFベクトル化](https://www.ibm.com/think/topics/bag-of-words)
- [単語埋め込み](https://www.ibm.com/think/topics/embedding)
- [主成分分析](https://www.ibm.com/think/topics/principal-component-analysis#:~:text=Principal%20component%20analysis%2C%20or%20PCA,of%20variables%2C%20called%20principal%20components.)

### 追加の技術的詳細、コードサンプル、数学的証明については、上記にリストされているリンク先のドキュメントと教育リソースをご覧ください。
- [scikit-learn: Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)