---
title: 固有表現認識（NER）
translationKey: named-entity-recognition-ner
description: 固有表現認識（NER）は、テキスト内の実世界のエンティティ（人物、組織、場所など）を識別し分類することで、生データを構造化された情報に変換します。
keywords:
- 固有表現認識
- NER
- 自然言語処理
- NLP
- エンティティ抽出
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: Named Entity Recognition (NER)
term: こゆうひょうげんにんしき（エヌイーアール）
url: "/ja/glossary/Named-Entity-Recognition--NER-/"
---
## 固有表現認識(NER)とは?

固有表現認識(NER)は、自然言語処理(NLP)における中核的なタスクであり、非構造化テキスト内の実世界のエンティティを自動的に識別し分類することに焦点を当てています。エンティティには、人名、組織名、場所、日付、数量、金額などが含まれます。NERは、関連する部分文字列(エンティティメンション)を特定し、事前定義されたカテゴリに割り当てることで、生のテキストを構造化された機械可読データに変換します。

実用的には、NERモデルはテキストデータを処理して重要な情報を抽出・注釈付けし、検索、質問応答、コンテンツ推薦、文書自動化などの下流アプリケーションを可能にします。

**例:**
「Appleは10億ドルでイギリスのスタートアップの買収を検討している。」

NER出力:
- "Apple" → 組織(ORG)
- "U.K." → 地政学的エンティティ(GPE)
- "$1 billion" → 金額(MONEY)

## NERが重要な理由

デジタルコンテンツの大半は非構造化データです—メール、記事、顧客チャット、ソーシャルメディア投稿、医療記録、法的文書など。NERは機械がこのデータから事実的な意味を抽出することを可能にし、幅広いアプリケーションをサポートします:

**検索:** 固有表現をインデックス化することで結果の関連性を向上させます。

**推薦:** 認識された人物、場所、製品に基づいてコンテンツを提案します。

**自動化:** 請求書、契約書、フォームから構造化データを抽出します。

**コンプライアンス:** 個人識別情報(PII)を識別し編集します。

**ナレッジグラフ:** 分析とAIのために情報を構造化します。

**曖昧性処理の例:**
NERモデルは文脈を分析して曖昧な名前を解決します:
- 「Lincoln」は「Abraham Lincoln」(人物)、「Lincoln Motor Company」(組織)、または「Lincoln, Nebraska」(場所)を指す可能性があります。

## 主要概念

### 固有表現(NE)

固有名詞または固定参照によって示される、一意の実世界のオブジェクト。

**例:** 「Michelle Obama」(人物)、「London」(場所)、「Google」(組織)、「$500」(金額)。

### エンティティタイプ / ラベル / タグ

エンティティスパンに割り当てられるカテゴリ。PER(人物)、ORG(組織)、LOC(場所)、DATE、MONEYなど。

### エンティティ境界検出

テキスト内のエンティティメンションの開始位置と終了位置を検出するプロセス。複数語の名前や複雑なエンティティにとって重要です。

**例:** 「The George Washington University Hospital」を単一のエンティティとして正しく抽出する。

### タグ付けスキーム

NERモデルはエンティティ境界をマークするためにタグ付けスキームを使用することがよくあります:

**BIO(Begin、Inside、Outside):** B-ORG、I-ORG、O

**IOBES(Inside、Outside、Begin、End、Single):** B-ORG、I-ORG、E-ORG、S-ORG、O

## NERの仕組み

### ワークフロー

**テキスト入力と前処理:** トークン化、文分割、正規化。

**特徴抽出:** 形態素、構文、意味、外部特徴を抽出。

**エンティティ境界検出:** エンティティを表す可能性のある候補スパンを特定。

**エンティティ分類:** ルール、統計モデル、またはディープラーニングを使用して、検出された各候補に最も確率の高いラベルを割り当てる。

**後処理:** 重複/入れ子のエンティティを解決し、曖昧性を解消し、一貫性を強制。

**出力生成:** 注釈付きテキスト、JSON、またはXMLとして構造化結果を返す。

## エンティティタイプ

| ラベル | 説明 | 例 |
|-------|------|-----|
| **PER** | 人物 | "Marie Curie"、"Sherlock Holmes" |
| **ORG** | 組織 | "Google"、"United Nations" |
| **LOC** | 場所 | "Mount Everest"、"Nile River" |
| **GPE** | 地政学的エンティティ | "Tokyo"、"United States" |
| **DATE** | 暦日または期間 | "January 1, 2022"、"19th century" |
| **TIME** | 特定の時刻または期間 | "5 PM"、"two hours" |
| **MONEY** | 金額 | "$100"、"€50 million" |
| **PERCENT** | パーセンテージ | "50%"、"half" |
| **FAC** | 施設 | "JFK Airport"、"Golden Gate Bridge" |
| **PRODUCT** | 製品、車両、ソフトウェア | "iPhone"、"Boeing 747" |
| **EVENT** | 名前付きイベント | "Olympics"、"Hurricane Katrina" |
| **WORK_OF_ART** | 書籍、映画、絵画 | "Mona Lisa"、"Star Wars" |
| **LANGUAGE** | 言語 | "English"、"Mandarin" |
| **LAW** | 法的文書、条約 | "Treaty of Versailles" |
| **NORP** | 国籍、宗教、政治団体 | "American"、"Democrat" |

## 手法とアプローチ

### ルールベース(パターンベース)

辞書(地名辞典)、正規表現、言語ルールを使用。

**長所:** 高速で解釈可能。

**短所:** 脆弱—新しいエンティティやドメインに対して手動更新が必要。

**使用例:** 固定フォーマット(電話番号、日付、既知のPII)。

### 従来の機械学習

エンジニアリングされた特徴(単語形状、品詞、文脈)を使用して注釈付きデータセットから学習。

**人気のアルゴリズム:** 条件付き確率場(CRF)、隠れマルコフモデル(HMM)、サポートベクターマシン(SVM)、決定木。

**長所:** 未知の例に汎化可能。

**短所:** ラベル付きデータと特徴エンジニアリングが必要。

### ディープラーニングアプローチ

**再帰型ニューラルネットワーク(RNN、LSTM):** 逐次的依存関係を学習。双方向LSTMは両方向から文脈を捉える。

**Transformerベースモデル(BERT、RoBERTa、GPT):**
- 自己注意機構を使用して文脈内の複雑な依存関係をモデル化
- 大規模コーパスで事前学習され、ラベル付きNERデータでファインチューニング
- 曖昧性、文脈、長距離依存関係、サブワード単位、入れ子エンティティを処理
- 標準ベンチマークで以前のモデルを上回る性能

**大規模言語モデル(LLM):** GPT-4のような汎用LLMは、ゼロショットまたは少数ショットプロンプティングによってNERを実行可能。

**ドメイン適応と転移学習:** カスタムコーパスで事前学習モデルをファインチューニングすることで、ドメイン固有のNERを実現。

## Python実装例

### spaCyの使用

```python
import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "Steve Jobs and Steve Wozniak founded Apple on April 1, 1976 in Cupertino, California."
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

**出力:**
```
Steve Jobs 0 10 PERSON
Steve Wozniak 15 29 PERSON
Apple 39 44 ORG
April 1, 1976 48 61 DATE
Cupertino 65 74 GPE
California 76 86 GPE
```

### Transformers(BERT)の使用

```python
from transformers import pipeline

ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")
text = "Apple CEO Tim Cook announced new iPhone models in California yesterday."
entities = ner_pipeline(text)

for entity in entities:
    print(entity)
```

## 課題

**曖昧性と多義性:** 単語は複数のエンティティタイプを持つ可能性(「Amazon」:会社または川)。

**境界検出:** 複数語および入れ子のエンティティ名(「Martin Luther King Jr.」、「University of California, Berkeley」)。

**ドメイン適応:** 専門ドメイン(生物医学、法律)における新規または稀なエンティティ。

**進化する言語:** 新しい用語、ブランド、スラング、略語。

**多言語NER:** コードスイッチング、異なる文字体系、言語固有のエンティティタイプの処理。

**ラベル付きデータの不足:** 大規模コーパスの注釈付けは高コストで時間がかかる。

**入れ子/重複エンティティ:** エンティティ内のエンティティ(特に生物医学または法律テキスト)。

**ノイズと非形式性:** ソーシャルメディア、OCR、音声書き起こしはエラーや非形式的言語を導入。

## 応用例

### 検索と情報検索

NERは記事やコンテンツにタグを付け、「Apple」(会社 vs. 果物)のようなエンティティを区別することで検索関連性を向上させます。

### 推薦エンジン

ストリーミングサービスは抽出されたエンティティ(俳優、ジャンル)に基づいてコンテンツを推薦します。

### 文書自動化とRPA

請求書、契約書、フォームから名前、日付、金額を抽出して自動処理を実現します。

### ナレッジグラフ構築

非構造化文書からエンティティと関係の構造化グラフを作成し、分析とAIを強化します。

### コンプライアンスとプライバシー

GDPR、HIPAAなどの規制コンプライアンスのために、機密文書内のPIIを識別し編集します。

**編集例:**
「Steve JobsはCupertinoでAppleを設立した。」
→ 「[PERSON]は[LOCATION]で[ORG]を設立した。」

### 感情分析の強化

特定のエンティティに感情を関連付けます(例:ホテルレビューで「朝食ビュッフェ」は否定的、「部屋」は肯定的)。

### カスタマーサポート自動化

製品名、コース名、苦情の主題を抽出してチケットをルーティングします。

### ドメイン固有NER

生物医学(遺伝子、タンパク質、疾患)、法律(判例、法令)、金融(ティッカー、金融商品)。

## 主要なツールとライブラリ

| ツール/ライブラリ | ハイライト | 言語 |
|--------------|-----------|------|
| **spaCy** | 高速、本番環境対応、カスタマイズ可能、事前学習モデル | Python |
| **NLTK** | 教育的、基本的NER、言語分析 | Python |
| **Stanford CoreNLP** | 学術的ゴールドスタンダード、RegexNER、多言語サポート | Java、Python |
| **Tonic Textual** | エンタープライズNER、編集、合成、カスタムモデル | API、Python SDK |
| **DeepPavlov** | ディープラーニング、事前学習モデル、ドメイン適応 | Python |
| **Google Cloud NLP** | マネージドサービス、エンティティ分析、感情分析 | API |
| **AWS Comprehend** | エンティティ抽出、感情、キーフレーズ検出 | API |
| **Hugging Face Transformers** | BERTベースNER、豊富なモデルライブラリ | Python |

## 参考文献

- [Wikipedia: Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)
- [IBM: What is Named Entity Recognition?](https://www.ibm.com/think/topics/named-entity-recognition)
- [Encord: Named Entity Recognition Guide](https://encord.com/blog/named-entity-recognition/)
- [AltexSoft: Named Entity Recognition Overview](https://www.altexsoft.com/blog/named-entity-recognition/)
- [GeeksforGeeks: Named Entity Recognition](https://www.geeksforgeeks.org/nlp/named-entity-recognition/)
- [Stanford NLP: CRFClassifier](https://nlp.stanford.edu/software/CRF-NER.html)
- [Machine Learning Mastery: How to Do NER with BERT](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)
- [arXiv: Recent Advances in NER](https://arxiv.org/html/2401.10825v3)
- [spaCy: Named Entities Documentation](https://spacy.io/usage/linguistic-features#named-entities)
- [Hugging Face: NER Models](https://huggingface.co/models?pipeline_tag=token-classification)
