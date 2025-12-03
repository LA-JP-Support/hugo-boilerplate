---
title: N-gram
translationKey: n-gram
description: N-gramとは、テキストや音声から抽出されるn個の連続したアイテム(単語、文字、記号)のシーケンスであり、自然言語処理における言語モデリングやテキスト分析の基礎となる手法です。
keywords: ["N-gram", "自然言語処理", "言語モデリング", "テキスト分析", "音声認識"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: エヌグラム
reading: N-gram
kana_head: その他
---
## 定義と概要

**N-gram**とは、テキストや音声のサンプルから抽出された*n*個の連続したアイテムの系列です。[自然言語処理(NLP)](https://en.wikipedia.org/wiki/Natural_language_processing)の文脈では、N-gramは通常、単語、文字、または記号の系列を指します。*n*の値によって各チャンクの長さが決まります:

- *n=1*の場合、モデルは**ユニグラム**(単一の単語またはトークン)を使用します。
- *n=2*の場合、**バイグラム**(2単語の系列)を使用します。
- *n=3*の場合、**トリグラム**(3単語の系列)を使用します。
- より広いコンテキストが必要な場合には、高次のN-gram(*n > 3*)も使用されます。

N-gramモデルは計算言語学の基礎であり、言語の理解、生成、予測のための統計的フレームワークを提供します。スペルチェッカー、予測テキスト、機械翻訳、音声認識など、多くの古典的なNLPシステムのバックボーンとなっています。

N-gramに基づく言語モデルは、大規模コーパスにおけるアイテムの共起に関する統計情報を使用して、トークン系列に確率を割り当てます。これにより、システムは次の単語を自動的に提案したり、エラーを修正したり、人間らしいテキストを生成したりできます。

*出典: [Stanford Speech and Language Processing, N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

## 歴史的背景と発展

N-gramは言語学と情報理論の両方において豊かな歴史を持っています。N-gramの数学的形式化は、20世紀初頭に**マルコフ連鎖**に関する研究を行ったアンドレイ・マルコフに遡ることができます。マルコフの洞察は、イベントの確率が全体の履歴ではなく、連鎖における前のイベントに依存する可能性があるというものでした(「マルコフ性」)。

1940年代から1950年代にかけて、クロード・シャノンはマルコフモデルを英語テキストに適用し、言語のためのN-gramモデルの概念を導入しました。シャノンの実験は、統計モデルが驚くほど人間らしいテキストを生成できることを実証し、計算言語学の基礎を築きました。

1980年代から1990年代にかけて、デジタルコーパスの台頭と計算能力の向上により、N-gramモデルは音声認識、光学文字認識(OCR)、初期の機械翻訳システムなどのタスクにおける標準的なアプローチとなりました。そのシンプルさ、解釈可能性、有効性により、多くのNLPパイプラインにおけるベースラインとなりました。

今日では、[Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/)のような高度なニューラルアーキテクチャが多くのタスクでN-gramモデルを上回っていますが、N-gramは特徴量エンジニアリング、ベースライン比較、効率性と透明性が重要なアプリケーションにおいて依然として不可欠です。

*参考文献: [Wikipedia: N-gram](https://en.wikipedia.org/wiki/N-gram)*

## N-gramの種類

### ユニグラム

- **定義:** 単一のアイテム(通常は単語)の系列。
- **例:**  
  テキスト: "Natural language processing is fun."  
  ユニグラム: "Natural", "language", "processing", "is", "fun"
- **使用例:** 基本的な単語頻度分析、テキスト分類、情報検索。

### バイグラム

- **定義:** 連続する2つのアイテムの系列。
- **例:**  
  テキスト: "Natural language processing is fun."  
  バイグラム: "Natural language", "language processing", "processing is", "is fun"
- **使用例:** フレーズ検出、感情分析("not good")、音声認識。

### トリグラム

- **定義:** 連続する3つのアイテムの系列。
- **例:**  
  テキスト: "Natural language processing is fun."  
  トリグラム: "Natural language processing", "language processing is", "processing is fun"
- **使用例:** より広いコンテキストの捕捉、オートコンプリート、スペル修正。

### 高次N-gram

- **定義:** 4つ以上の連続するアイテムの系列(例: 4-gram、5-gram)。
- **例:** "Natural language processing is fun."の場合  
  4-gram: "Natural language processing is", "language processing is fun"
- **使用例:** ドメイン固有の言語モデリング、盗作検出。
- **考慮事項:** *n*が増加すると、可能なN-gramの数が指数関数的に増加し、データのスパース性と計算オーバーヘッドが生じます。

*出典: [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*

## N-gramモデルの仕組み

### 確率推定

N-gramモデルは、先行する*n-1*個のアイテムに基づいて単語またはトークンの確率を推定します。**確率の連鎖律**は、系列の同時確率を条件付き確率の積として表現します:

\[
P(w_1, w_2, \ldots, w_n) = P(w_1) \cdot P(w_2|w_1) \cdot P(w_3|w_1, w_2) \cdots P(w_n|w_1, \ldots, w_{n-1})
\]

この式は長い系列に対して計算コストが高くなります。N-gramモデルは**マルコフ仮定**によってこれを簡略化します。

### マルコフ仮定

**マルコフ仮定**は、単語の確率が先行する全体のコンテキストではなく、直前の*n-1*個の単語にのみ依存すると仮定します。これは実用的な計算において極めて重要です。

バイグラム(*n=2*)の場合:
\[
P(w_n | w_1, w_2, ..., w_{n-1}) \approx P(w_n | w_{n-1})
\]

トリグラム(*n=3*)の場合:
\[
P(w_n | w_1, ..., w_{n-1}) \approx P(w_n | w_{n-2}, w_{n-1})
\]

この仮定により、パラメータ数が劇的に削減され、実世界のデータに対する言語モデリングが実現可能になります。

*出典: [Stanford Speech and Language Processing, N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### 最尤推定(MLE)

MLEは観測データからN-gram確率を推定するために使用されます。N-gramモデルの一般的な式は次のとおりです:

\[
P(w_n | w_{n-N+1}, ..., w_{n-1}) = \frac{C(w_{n-N+1}, ..., w_n)}{C(w_{n-N+1}, ..., w_{n-1})}
\]

ここで:
- \(C(w_{n-N+1}, ..., w_n)\): コーパス内のN-gramの出現回数。
- \(C(w_{n-N+1}, ..., w_{n-1})\): (N-1)-gram接頭辞の出現回数。

バイグラムの場合、これは次のようになります:
\[
P(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n)}{C(w_{n-1})}
\]

**計算例:**  
次のコーパスが与えられた場合:
- "I am Sam"
- "Sam I am"
- "I do not like green eggs and ham"

\(P(am | I)\)を計算するには:
- "I am"の出現回数: 2
- "I"の出現回数: 3
- \(P(am | I) = 2/3\)

*完全な計算と数学的導出については、[Stanford Speech and Language Processing, Chapter 3](https://web.stanford.edu/~jurafsky/slp3/3.pdf)を参照してください。*

### 平滑化技術

#### 平滑化の必要性

*n*が増加すると、多くの有効なN-gramが訓練データに現れない可能性があり、確率推定がゼロになります。これを**データのスパース性**と呼びます。平滑化技術は、未見のN-gramを考慮して確率推定を調整し、汎化性能を向上させます。

#### ラプラス(加算)平滑化

ラプラス平滑化は、すべてのN-gram出現回数に小さな定数(通常は1)を加えます:

\[
P_{Laplace}(w_n | w_{n-1}) = \frac{C(w_{n-1}, w_n) + 1}{C(w_{n-1}) + V}
\]

ここで:
- \(V\)は語彙サイズ。

これにより、N-gramの確率がゼロにならないことが保証されます。

#### 高度な平滑化: Good-Turing、Kneser-Ney

- **Good-Turing平滑化:** 1回、2回などの出現回数を持つN-gramの数に基づいてN-gram頻度を調整します。
- **Kneser-Ney平滑化:** 言語モデリングにおける最先端技術で、N-gramが出現する頻度とコンテキストの分布の両方を考慮します。

*詳細な説明: [Stanford PDF, Section 3.4](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### パープレキシティとエントロピー

- **パープレキシティ**は、確率モデルがサンプルをどれだけうまく予測するかの尺度です。パープレキシティが低いほど、言語モデルが優れていることを示します。
  \[
  Perplexity(P) = 2^{H(P)}
  \]
  ここで\(H(P)\)は確率分布のエントロピーです。
- **エントロピー**はテキストの予測不可能性を測定します。

*詳細: [Stanford PDF, Section 3.5](https://web.stanford.edu/~jurafsky/slp3/3.pdf)*

### Python実装例

#### 基本的なN-gram抽出

```python
def generate_ngrams(text, n):
    tokens = text.split()
    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    return ngrams

text = "Geeks for Geeks Community"

unigrams = generate_ngrams(text, 1)
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)

print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

#### 出力
```
Unigrams: [('Geeks',), ('for',), ('Geeks',), ('Community',)]
Bigrams: [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
Trigrams: [('Geeks', 'for', 'Geeks'), ('for', 'Geeks', 'Community')]
```

#### ラプラス平滑化の例

```python
from collections import Counter

def laplace_smoothing(ngrams, vocab_size):
    ngram_counts = Counter(ngrams)
    smoothed_ngrams = {ngram: (count + 1) / (len(ngrams) + vocab_size)
                       for ngram, count in ngram_counts.items()}
    return smoothed_ngrams

ngrams = [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
vocab_size = 5

smoothed_ngrams = laplace_smoothing(ngrams, vocab_size)
print("Smoothed N-grams:", smoothed_ngrams)
```

**出力:**
```
Smoothed N-grams: {('Geeks', 'for'): 0.25, ('for', 'Geeks'): 0.25, ('Geeks', 'Community'): 0.25}
```

#### NLTKの例

```python
import nltk
words = nltk.word_tokenize("I am going to the store")
bigrams = list(nltk.ngrams(words, 2))
trigrams = list(nltk.ngrams(words, 3))
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

## N-gramを用いた特徴量エンジニアリング

N-gram特徴量は、機械学習モデルのためのNLPにおいて広く使用されています。古典的なテキスト分類器、情報検索などのバックボーンとして機能します。

### Bag-of-N-gramsモデル

**Bag-of-N-grams**アプローチは、文書をスパースベクトルとして表現し、各次元は語彙からのN-gramに対応します。値は通常、文書内のN-gramの頻度です。

#### 例: PythonとSciPy

```python
import scipy.sparse as sp
import numpy as np

def extract_ngrams(text, n):
    ngrams_list = []
    for i in range(len(text) - n + 1):
        ngrams_list.append(tuple(text[i:i + n]))
    return ngrams_list

def build_bag_of_ngrams(text, n, vocabulary):
    ngrams_list = extract_ngrams(text, n)
    ngrams_index = {ngram: i for i, ngram in enumerate(vocabulary)}
    col = [ngrams_index[ngram] for ngram in ngrams_list if ngram in ngrams_index]
    data = [1] * len(col)
    row = [0] * len(col)
    vector = sp.csr_matrix((data, (row, col)), shape=(1, len(vocabulary)))
    return vector
```

### Skip-gramとサブワードN-gram

- **Skip-gram:** 非連続なN-gram(例: "I am Sam"における"I ... Sam")で、より長距離の依存関係を捕捉するのに有用です。
- **サブワードN-gram:** 文字レベルまたは音節ベースのN-gramで、形態が豊富な言語やノイズの多いデータ(例: Twitter、OCR)を扱うために不可欠です。

### 系列表現

Bag-of-N-gramsの代わりに、一部のモデルは[隠れマルコフモデル](https://www.geeksforgeeks.org/machine-learning/hidden-markov-model-in-machine-learning/)、[RNN](https://www.geeksforgeeks.org/understanding-rnn-recurrent-neural-network/)、または[Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/)などの系列モデルの入力として、系列表現(N-gramの順序付きリスト)を使用します。

*出典: [A Comprehensive Guide To Feature Engineering with N-Grams For NLP](https://www.linkedin.com/pulse/comprehensive-guide-feature-engineering-n-grams-david-adamson-mbcs)*

## N-gramの応用

N-gramは、多数のNLPおよびAI自動化タスクにおいて基礎となっています:

- **言語モデリング:** 文中の次の単語を予測し、オートコンプリート、予測入力、チャットボットの応答を支援します。
- **テキスト分類:** 文書の分類(トピック、感情)のための特徴抽出。"not good"のようなバイグラムは感情分類器を改善します。
- **音声認識:** 単語系列をモデル化して転写精度を向上させます。
- **スペル修正:** 可能性の高い単語系列に基づいて修正を提案します(例: "from"対"form")。
- **機械翻訳:** 統計的翻訳システムは、N-gram確率を使用して目標言語の文を構築します。
- **情報検索:** 検索エンジンは、文書のインデックス作成とランキングにN-gramを使用します。
- **盗作検出:** 文書内の重複する系列を検出します。
- **予測入力/オートコンプリート:** ユーザーが入力する際に、頻出するN-gram系列を使用して次の単語を提案します。

**具体例:**
- 感情分析では、"very good"や"poor quality"などのバイグラムは、ポジティブまたはネガティブな感情を強く示します。
- Google検索の提案は、頻出するトリグラムの分析によって支えられています:"how to"と入力すると、N-gram頻度に基づいて"how to cook"、"how to code"が表示されます。

*出典: [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*

## 高度なトピック

### データのスパース性と次元性

*n*の値が高くなると、可能なN-gramの数が指数関数的に増加します。例えば、10,000語の語彙では:

- 10,000個のユニグラム
- 100,000,000個のバイグラム
- 1,000,000,000,000個のトリグラム

これにより以下が生じます:
- **データのスパース性:** 多くのN-gramがコーパスに出現しません。
- **高次元性:** ストレージと計算が困難になります。

### N-gramバックオフと補間

**バックオフ:** 高次のN-gramが