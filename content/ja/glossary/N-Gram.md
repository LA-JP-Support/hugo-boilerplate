---
title: N-gram
translationKey: n-gram
description: N-gramとは、テキストや音声から抽出されるn個の連続したアイテム(単語、文字、記号)のシーケンスであり、自然言語処理における言語モデリングやテキスト分析の基礎となる手法です。
keywords:
- N-gram
- 自然言語処理
- 言語モデリング
- テキスト分析
- 音声認識
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: N-Gram
term: エヌグラム
url: "/ja/glossary/n-gram/"
aliases:
- "/ja/glossary/N-Gram/"
---
## N-Gramとは何か?

N-gramとは、テキストや音声のサンプルから抽出されたn個の連続したアイテムのシーケンスです。自然言語処理(NLP)において、N-gramは通常、単語、文字、または記号のシーケンスを指します。nの値が各チャンクの長さを決定します—n=1の場合はユニグラム(単一の単語)、n=2の場合はバイグラム(2単語のシーケンス)、n=3の場合はトライグラム(3単語のシーケンス)といった具合です。

N-gramモデルは計算言語学の基礎であり、言語の理解、生成、予測のための統計的フレームワークを提供します。スペルチェッカー、予測テキスト、機械翻訳、音声認識など、多くの古典的なNLPシステムのバックボーンとなっています。

N-gramに基づく言語モデルは、トークンのシーケンスに確率を割り当て、大規模コーパスにおけるアイテムの共起に関する統計情報を使用します。これにより、システムは次に来る可能性の高い単語を自動的に提案したり、エラーを修正したり、人間らしいテキストを生成したりできます。

## 歴史的背景

N-gramは言語学と情報理論の両方において豊かな歴史を持っています。数学的な形式化は、20世紀初頭にマルコフ連鎖に関する研究を行ったアンドレイ・マルコフまで遡ることができます。マルコフの洞察は、イベントの確率が全体の履歴ではなく、連鎖における前のイベントに依存する可能性があるというものでした(「マルコフ性」)。

1940年代と1950年代に、クロード・シャノンはマルコフモデルを英語テキストに適用し、言語のためのN-gramモデルの概念を導入しました。シャノンの実験は、統計モデルが驚くほど人間らしいテキストを生成できることを実証し、計算言語学の基礎を築きました。

1980年代と1990年代には、デジタルコーパスの台頭と計算能力の向上により、N-gramモデルは音声認識、光学文字認識(OCR)、初期の機械翻訳システムなどのタスクにおける標準的なアプローチとなりました。そのシンプルさ、解釈可能性、効果性により、多くのNLPパイプラインにおけるベースラインとなりました。

今日では、Transformersのような高度なニューラルアーキテクチャが多くのタスクでN-gramモデルを上回っていますが、N-gramは特徴量エンジニアリング、ベースライン比較、効率性と透明性が重要なアプリケーションにおいて依然として不可欠です。

## N-Gramの種類

### ユニグラム

**定義:** 単一のアイテム(通常は単語)のシーケンス。

**例:**
テキスト: "Natural language processing is fun."
ユニグラム: "Natural", "language", "processing", "is", "fun"

**ユースケース:** 基本的な単語頻度分析、テキスト分類、情報検索。

### バイグラム

**定義:** 2つの連続したアイテムのシーケンス。

**例:**
テキスト: "Natural language processing is fun."
バイグラム: "Natural language", "language processing", "processing is", "is fun"

**ユースケース:** フレーズ検出、感情分析("not good")、音声認識。

### トライグラム

**定義:** 3つの連続したアイテムのシーケンス。

**例:**
テキスト: "Natural language processing is fun."
トライグラム: "Natural language processing", "language processing is", "processing is fun"

**ユースケース:** より広いコンテキストの捕捉、オートコンプリート、スペル修正。

### 高次N-gram

**定義:** 4つ以上の連続したアイテムのシーケンス(4-gram、5-gram)。

**例:** "Natural language processing is fun."の場合
4-gram: "Natural language processing is", "language processing is fun"

**ユースケース:** ドメイン固有の言語モデリング、盗作検出。

**考慮事項:** nが増加すると、可能なN-gramの数が指数関数的に増加し、データのスパース性と計算オーバーヘッドが生じます。

## N-Gramモデルの仕組み

### 確率推定

N-gramモデルは、先行するn-1個のアイテムに基づいて単語またはトークンの確率を推定します。確率の連鎖律は、シーケンスの同時確率を条件付き確率の積として表現します。

この式は長いシーケンスに対して計算コストが高くなります。N-gramモデルはマルコフ仮定を行うことでこれを簡略化します。

### マルコフ仮定

マルコフ仮定は、単語の確率が先行する全体のコンテキストではなく、直前のn-1個の単語にのみ依存するという仮定です。これは実用的な計算にとって重要です。

バイグラム(n=2)の場合: P(wn | w1, w2, ..., wn-1) ≈ P(wn | wn-1)

トライグラム(n=3)の場合: P(wn | w1, ..., wn-1) ≈ P(wn | wn-2, wn-1)

この仮定により、パラメータの数が劇的に減少し、実世界のデータでの言語モデリングが実現可能になります。

### 最尤推定

最尤推定(MLE)は、観測データからN-gram確率を推定するために使用されます。N-gramモデルの一般的な式は次のとおりです:

P(wn | wn-N+1, ..., wn-1) = C(wn-N+1, ..., wn) / C(wn-N+1, ..., wn-1)

ここで:
- C(wn-N+1, ..., wn): コーパス内のN-gramの出現回数
- C(wn-N+1, ..., wn-1): (N-1)-gramプレフィックスの出現回数

バイグラムの場合: P(wn | wn-1) = C(wn-1, wn) / C(wn-1)

**計算例:**
コーパス:
- "I am Sam"
- "Sam I am"
- "I do not like green eggs and ham"

P(am | I)を計算するには:
- "I am"の出現回数: 2
- "I"の出現回数: 3
- P(am | I) = 2/3

### スムージング技術

**スムージングの必要性:** nが増加すると、多くの有効なN-gramが訓練データに現れない可能性があり、ゼロ確率推定が生じます。これをデータのスパース性と呼びます。スムージング技術は、未見のN-gramを考慮して確率推定を調整し、汎化性能を向上させます。

**ラプラス(加算)スムージング:** すべてのN-gramカウントに小さな定数(通常は1)を追加します:

P_Laplace(wn | wn-1) = (C(wn-1, wn) + 1) / (C(wn-1) + V)

ここでVは語彙サイズです。これにより、どのN-gramもゼロ確率を持たないことが保証されます。

**高度なスムージング:** Good-TuringやKneser-Neyスムージングは、コンテキストの分布に基づいて頻度を調整し、言語モデリングにおける最先端技術です。

### パープレキシティとエントロピー

**パープレキシティ**は、確率モデルがサンプルをどれだけうまく予測するかを測定します。パープレキシティが低いほど、言語モデルが優れていることを示します。

**エントロピー**は、テキストの予測不可能性を測定します。

## Python実装

### 基本的なN-gram抽出

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

出力:
```
Unigrams: [('Geeks',), ('for',), ('Geeks',), ('Community',)]
Bigrams: [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
Trigrams: [('Geeks', 'for', 'Geeks'), ('for', 'Geeks', 'Community')]
```

### ラプラススムージングの例

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

### NLTKの例

```python
import nltk
words = nltk.word_tokenize("I am going to the store")
bigrams = list(nltk.ngrams(words, 2))
trigrams = list(nltk.ngrams(words, 3))
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

## 特徴量エンジニアリング

### Bag-of-N-gramsモデル

Bag-of-N-gramsアプローチは、文書をスパースベクトルとして表現し、各次元が語彙からのN-gramに対応します。値は通常、文書内のN-gramの頻度です。

### スキップグラムとサブワードN-gram

**スキップグラム:** 非連続なN-gram(例:"I am Sam"における"I ... Sam")で、より長距離の依存関係を捕捉するのに有用です。

**サブワードN-gram:** 文字レベルまたは音節ベースのN-gramで、豊富な形態論を持つ言語やノイズの多いデータ(Twitter、OCR)を扱うために不可欠です。

### シーケンス表現

一部のモデルは、隠れマルコフモデル、RNN、Transformersなどのシーケンシャルモデルの入力として、シーケンス表現(N-gramの順序付きリスト)を使用します。

## アプリケーション

**言語モデリング:** 文中の次の単語を予測し、オートコンプリート、予測入力、チャットボットの応答を支援します。

**テキスト分類:** 文書を分類するための特徴抽出(トピック、感情)。"not good"のようなバイグラムは感情分類器を改善します。

**音声認識:** 単語シーケンスをモデル化して転写精度を向上させます。

**スペル修正:** 可能性の高い単語シーケンスに基づいて修正を提案します(例:"from"対"form")。

**機械翻訳:** 統計的翻訳システムは、N-gram確率を使用して目標言語の文を構築します。

**情報検索:** 検索エンジンは、文書のインデックス作成とランキングにN-gramを使用します。

**盗作検出:** 文書内の重複するシーケンスを検出します。

**予測入力/オートコンプリート:** ユーザーが入力する際に、頻繁なN-gramシーケンスを使用して次の単語を提案します。

## 高度なトピック

### データのスパース性と次元数

nの値が高くなると、可能なN-gramの数が指数関数的に増加します。例えば、10,000語の語彙では:
- 10,000個のユニグラム
- 100,000,000個のバイグラム
- 1,000,000,000,000個のトライグラム

これにより、データのスパース性(多くのN-gramがコーパスに現れない)と高次元性(ストレージと計算が困難になる)が生じます。

### バックオフと補間

**バックオフ:** 高次のN-gramが見つからない場合、低次のN-gramにバックオフします。

**補間:** 複数のN-gram次数からの確率を、その信頼性によって重み付けして組み合わせます。

## 制限事項

**固定コンテキスト:** n-1個の前の単語を超える依存関係を捕捉できません。

**データのスパース性:** 多くの有効なN-gramが訓練コーパスに現れない可能性があります。

**意味理解の欠如:** 単語を意味や同義語を理解せずに離散的なシンボルとして扱います。

**計算の複雑さ:** 高次のN-gramは、指数関数的に多くのストレージと計算を必要とします。

## 参考文献

- [Stanford Speech and Language Processing: N-gram Language Models (PDF)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [Wikipedia: N-gram](https://en.wikipedia.org/wiki/N-gram)
- [GeeksforGeeks: N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)
- [LinkedIn: Comprehensive Guide to Feature Engineering with N-Grams](https://www.linkedin.com/pulse/comprehensive-guide-feature-engineering-n-grams-david-adamson-mbcs)
- [GeeksforGeeks: Getting Started with Transformers](https://www.geeksforgeeks.org/machine-learning/getting-started-with-transformers/)
- [GeeksforGeeks: Hidden Markov Model in Machine Learning](https://www.geeksforgeeks.org/machine-learning/hidden-markov-model-in-machine-learning/)
- [GeeksforGeeks: Understanding RNN (Recurrent Neural Network)](https://www.geeksforgeeks.org/understanding-rnn-recurrent-neural-network/)
