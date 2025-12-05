---
title: 固有表現抽出（NER）
translationKey: named-entity-recognition-ner
description: 固有表現抽出（NER）は、テキスト内の実世界のエンティティ（人物、組織、場所など）を識別し分類することで、生データを構造化された情報に変換します。
keywords: ["固有表現抽出", "NER", "自然言語処理", "NLP", "エンティティ抽出"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: こゆうひょうげんちゅうしゅつ（エヌイーアール）
reading: 固有表現抽出（NER）
kana_head: その他
e-title: Named Entity Recognition (NER)
---
## Named Entity Recognition (NER)とは?

[Named Entity Recognition (NER)](https://en.wikipedia.org/wiki/Named-entity_recognition)は、[自然言語処理(NLP)](https://www.ibm.com/think/topics/natural-language-processing)における中核的なタスクであり、非構造化テキスト内の実世界のエンティティを自動的に識別し分類することに焦点を当てています。エンティティには、人名、組織名、場所、日付、数量、金額などが含まれます。NERは、関連する部分文字列(エンティティメンション)を特定し、事前定義されたカテゴリに割り当てることで、生のテキストを構造化された機械可読データに変換します。

実用的には、NERモデルはテキストデータを処理して重要な情報を抽出・注釈付けし、検索、質問応答、コンテンツ推薦、文書自動化などの下流アプリケーションを可能にします。

**例:**  
*"Apple is looking at buying U.K. startup for $1 billion."*  
NER出力:  
- "Apple" → 組織(ORG)
- "U.K." → 地政学的エンティティ(GPE)
- "$1 billion" → 金額(MONEY)

視覚的な例と詳細な説明については、[EncordのNERガイド](https://encord.com/blog/named-entity-recognition/)をご覧ください。

## NERが重要な理由

ほとんどのデジタルコンテンツは非構造化されています—メール、記事、顧客チャット、ソーシャルメディア投稿、医療記録、法的文書など。NERは機械がこのデータから事実的な意味を抽出することを可能にし、幅広いアプリケーションをサポートします:

- **検索:** 固有表現をインデックス化することで結果の関連性を向上
- **推薦:** 認識された人物、場所、製品に基づいてコンテンツを提案
- **自動化:** 請求書、契約書、フォームから構造化データを抽出
- **コンプライアンス:** 個人識別情報(PII)を識別し編集
- **知識グラフ:** 分析とAIのために情報を構造化

**曖昧性処理の例:**  
NERモデルは文脈を分析して曖昧な名前を解決します:
- *"Lincoln"*は「エイブラハム・リンカーン」(人物)、「リンカーン・モーター・カンパニー」(組織)、または「リンカーン、ネブラスカ」(場所)を指す可能性があります。

追加のユースケースについては、[AltexSoft NER概要](https://www.altexsoft.com/blog/named-entity-recognition/)をご覧ください。

## 主要な概念と用語

### 固有表現(NE)
固有名詞または固定参照によって示される、一意の実世界のオブジェクト。  
**例:** 「ミシェル・オバマ」(人物)、「ロンドン」(場所)、「Google」(組織)、「$500」(金額)。

### エンティティタイプ/ラベル/タグ
エンティティスパンに割り当てられるカテゴリ。PER(人物)、ORG(組織)、LOC(場所)、DATE、MONEYなど。

### エンティティ境界検出
テキスト内のエンティティメンションの開始位置と終了位置を検出するプロセス。複数語の名前や複雑なエンティティにとって重要。
- 例: 「The George Washington University Hospital」を単一のエンティティとして正しく抽出。

### タグ付けスキーム
NERモデルはエンティティ境界をマークするためにタグ付けスキームを使用することが多い:
- **BIO**(Begin、Inside、Outside): B-ORG、I-ORG、O
- **IOBES**(Inside、Outside、Begin、End、Single): B-ORG、I-ORG、E-ORG、S-ORG、O

**タグ付けの例と視覚化:**  
[Encord: NERタグ付けスキーム](https://encord.com/blog/named-entity-recognition/)

### 品詞(POS)タグ付け
単語に文法的役割(名詞、動詞、形容詞など)を割り当て、NERモデルの特徴量としてよく使用される。

### チャンキング
単語を意味のある単位(例:名詞句)にグループ化し、エンティティ境界の識別を容易にする。

### 単語埋め込み
単語を密なベクトル表現に変換(Word2Vec、GloVe、またはBERTのような文脈モデルを使用)し、機械学習のための意味的・構文的関係を捉える。

### ガゼッティア(辞書)
ルールベースまたはハイブリッドNERアプローチに使用される既知のエンティティ名の辞書。

### コーパス
NERシステムの訓練と評価に使用される、大規模な注釈付きテキストコレクション。

## NERの仕組み:詳細なワークフロー

NERプロセスは複数の連続した段階で構成されます:

### 1. テキスト入力と前処理
- **トークン化:** 生テキストを単語、句読点、記号(トークン)に分割
- **文分割:** 文の境界を識別
- **正規化:** 小文字化、ステミング、レンマ化により単語形式を削減

### 2. 特徴抽出
NERモデルはエンティティ境界と分類を通知するために特徴を抽出:
- **形態論的:** 単語の形状、接頭辞、接尾辞、大文字化
- **構文的:** POSタグ、句構造
- **意味的:** 文脈的意味、近隣語
- **外部:** ガゼッティアマッチ、正規表現パターン

### 3. エンティティ境界検出
文脈的・構文的手がかりを使用して、エンティティを表す可能性のある候補スパンを特定。

### 4. エンティティ分類
検出された各候補に最も可能性の高いラベル(例:人物、場所、組織)を割り当て。手作りルール、統計モデル、またはディープラーニングを使用。

### 5. 後処理
- **重複/入れ子エンティティ:** エンティティが重複または入れ子になっている場合を解決(例:「University of California, Berkeley」)
- **曖昧性解消:** 文脈を活用して多義的な名前を明確化
- **一貫性の強制:** 文書内および文書間で一貫したラベル付けを保証

### 6. 出力生成
構造化された結果を返す。通常は注釈付きテキスト、JSON、またはXML形式。

**サンプルJSON:**  
```json
[
  { "text": "Steve Jobs", "type": "PERSON", "startOffset": 0, "endOffset": 10 },
  { "text": "Apple", "type": "ORG", "startOffset": 22, "endOffset": 27 }
]
```

**参考資料:**  
- [Encord NERガイド](https://encord.com/blog/named-entity-recognition/)
- [IBM: Named Entity Recognitionとは?](https://www.ibm.com/think/topics/named-entity-recognition)

## NERにおけるラベルタイプとタグ付けスキーム

### 一般的なエンティティラベル

| ラベル       | 説明                                              | 例                              |
|--------------|--------------------------------------------------|--------------------------------|
| PER          | 人物(個人、架空のキャラクター)                      | 「マリー・キュリー」、「シャーロック・ホームズ」 |
| ORG          | 組織(企業、機関、グループ)                         | 「Google」、「国際連合」         |
| LOC          | 場所(山、川、都市など)                             | 「エベレスト山」、「ナイル川」    |
| GPE          | 地政学的エンティティ(国、都市、州)                  | 「東京」、「アメリカ合衆国」      |
| DATE         | 暦日または期間                                     | 「2022年1月1日」、「19世紀」     |
| TIME         | 特定の時刻または期間                               | 「午後5時」、「2時間」           |
| MONEY        | 金額                                              | 「$100」、「€5000万」           |
| PERCENT      | パーセンテージ                                     | 「50%」、「半分」               |
| FAC          | 施設(建物、空港、高速道路)                         | 「JFK空港」、「ゴールデンゲートブリッジ」 |
| PRODUCT      | 製品、車両、ソフトウェア                           | 「iPhone」、「ボーイング747」    |
| EVENT        | 固有のイベント(戦争、スポーツ、災害)                | 「オリンピック」、「ハリケーン・カトリーナ」|
| WORK_OF_ART  | 書籍、映画、絵画                                   | 「モナリザ」、「スター・ウォーズ」 |
| LANGUAGE     | 言語                                              | 「英語」、「北京語」             |
| LAW          | 法的文書、条約                                     | 「ヴェルサイユ条約」             |
| NORP         | 国籍、宗教、政治グループ                           | 「アメリカ人」、「民主党員」      |

**視覚化と詳細:**  
[Encord: NERラベル表](https://encord.com/blog/named-entity-recognition/)

### タグ付けスキーム

- **BIO(Begin、Inside、Outside):**
  - B-ORG: 組織の開始
  - I-ORG: 組織の内部
  - O: エンティティの外部

- **IOBES/IOB2:**  
  より細かい境界制御のためにE(End)とS(Single)でBIOを拡張。

- **入れ子/重複タグ付け:**  
  一部の高度なNERシステムは入れ子エンティティ認識をサポート。生物医学や法律テキストで重要。

**視覚化と例:**  
[Encord: タグ付けスキーム](https://encord.com/blog/named-entity-recognition/)

## 手法とアプローチ

### 1. ルールベース(パターンベース/辞書ベース)
- 辞書(ガゼッティア)、正規表現、言語ルールを使用
- 高速で解釈可能だが脆弱—新しいエンティティやドメインには手動更新が必要
- 固定形式(電話番号、日付、既知のPII)に効果的
- **参考:** [Wikipedia: Named-entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)

### 2. 従来の機械学習
- 設計された特徴量(単語形状、POS、文脈)を使用して注釈付きデータセットから学習
- 人気のアルゴリズム: 条件付き確率場(CRF)、隠れマルコフモデル(HMM)、サポートベクターマシン(SVM)、決定木
- 未知の例に汎化できるがラベル付きデータと特徴量エンジニアリングが必要
- **参考資料:** [Stanford NLP CRFClassifier](https://nlp.stanford.edu/software/CRF-NER.html)

### 3. ディープラーニングアプローチ

#### a. リカレントニューラルネットワーク(RNN、LSTM)
- 系列依存性を学習。トランスフォーマー以前に人気
- 双方向LSTMは左右両方の文脈を捉える

#### b. トランスフォーマーベースモデル(BERT、RoBERTa、GPTなど)
- 自己注意機構を使用して文脈内の複雑な依存関係をモデル化
- 大規模コーパスで事前学習され、ラベル付きNERデータで微調整
- 曖昧性、文脈、長距離依存性、サブワード単位、入れ子エンティティを処理
- **BERTによるNER:**  
  - 文脈認識、双方向、転移学習をサポート
  - 複数語エンティティのIOBタグ付けをサポート
  - 標準ベンチマークで以前のモデルを上回る性能
  - [BERTでNERを行う方法: Machine Learning Mastery](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)
  - [NERの最近の進歩: arXivサーベイ](https://arxiv.org/html/2401.10825v3)
- **コード例:**  
  ```python
  from transformers import pipeline
  ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")
  text = "Apple CEO Tim Cook announced new iPhone models in California yesterday."
  entities = ner_pipeline(text)
  for entity in entities:
      print(entity)
  ```

#### c. 大規模言語モデル(LLM)
- GPT-4、PaLM、Claudeなどの汎用LLMは、ゼロショットまたは少数ショットプロンプティングでNERを実行可能
- ラベル付きデータが少なくて済むが、細かい制御やドメイン特異性に欠ける可能性

#### d. ドメイン適応と転移学習
- カスタムコーパス(例:医療、法律)で事前学習モデルを微調整し、ドメイン固有のNERを実現

#### e. 強化学習とグラフベースNER
- 強化学習はNERパイプラインを最適化可能
- グラフベースアプローチはエンティティ間の関係をモデル化し精度を向上
- [最近の進歩: arXiv NERサーベイ](https://arxiv.org/html/2401.10825v3)

## NERにおける課題

NERは以下の理由によりNLPにおいて困難な問題です:

- **曖昧性と多義性:** 単語は複数のエンティティタイプを持つ可能性(「Amazon」:企業または川)
- **境界検出:** 複数語および入れ子のエンティティ名(「Martin Luther King Jr.」、「University of California, Berkeley」)
- **ドメイン適応:** 専門分野(生物医学、法律)における新規または稀なエンティティ
- **進化する言語:** 新しい用語、ブランド、スラング、頭字語
- **多言語NER:** コードスイッチング、異なる文字体系、言語固有のエンティティタイプの処理
- **ラベル付きデータの不足:** 大規模コーパスの注釈付けは高コストで時間がかかる
- **入れ子/重複エンティティ:** エンティティ内のエンティティ(特に生物医学や法律テキスト)
- **ノイズと非形式性:** ソーシャルメディア、OCR、音声書き起こしはエラーと非形式的言語を導入

**課題の詳細:**  
[Encord: NERにおける課題](https://encord.com/blog/named-entity-recognition/)  
[arXiv: NERの最近の進歩](https://arxiv.org/html/2401.10825v3)

## NERのユースケースとアプリケーション

### 1. 検索と情報検索
NERは記事やコンテンツにタグを付け、「Apple」(企業 vs. 果物)などのエンティティを区別することで検索の関連性を向上。

### 2. 推薦エンジン
ストリーミングサービスは抽出されたエンティティ(俳優、ジャンル)に基づいてコンテンツを推薦。

### 3. 文書自動化とRPA
請求書、契約書、フォームから名前、日付、金額を抽出し自動処理。

### 4. 知識グラフ構築
非構造化文書からエンティティと関係の構造化グラフを作成し、分析とAIを強化。

### 5. コンプライアンスとプライバシー
GDPR、HIPAAなどの規制コンプライアンスのため、機密文書内のPIIを識別し編集。

  **編集例:**  
  「Steve Jobs founded Apple in Cupertino.」  
  → 「[PERSON]が[LOCATION]で[ORG]を設立。」

### 6. 感情分析の強化
特定のエンティティに感情を関連付け(例:ホテルレビューで「朝食ビュッフェ」は否定的、「部屋」は肯定的)。

### 7. カスタマーサポート自動化
製品名、コース名、苦情の主題を抽出してチケットをルーティング。

### 8. ドメイン固有NER
生物医学(遺伝子、タンパク質、疾患)、法律(判例、法令)、金融(ティッカー、金融商品)など。

**ケーススタディと例:**  
- [AltexSoft NERアプリケーション](https://www.altexsoft.com/blog/named-entity-recognition/)
- [GeeksforGeeks: NERアプリケーション](https://www.geeksforgeeks.org/nlp/named-entity-recognition/)

## 実践的実装:spaCyを使用したステップバイステップの例

### ステップ1: 必要なライブラリのインストール
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### ステップ2: spaCyモデルの読み込み
```python
import spacy
nlp = spacy.load("en_core_web_sm")
```

### ステップ3: テキストの処理とエンティティの抽出
```python
content = "Steve Jobs and Steve Wozniak founded Apple on April 1, 1976 in Cupertino, California."
doc = nlp(content)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

**サンプル出力:**
```
Steve Jobs 0 10 PERSON
Steve Wozniak 15 29 PERSON
Apple 39 44 ORG
April 1, 1976 48 61 DATE
Cupertino 65 74 GPE
California 76 86 GPE
```

### ステップ4: エンティティの視覚化
```python
from spacy import displacy
displacy.render(doc, style="ent")
```
![spaCyによるNER視覚化](https://www.altexsoft.com/static/blog-post/2024/3/afb1c9bf-f08e-4ad7-a4ec-ad9745dda06d.jpg)

### ステップ5: エンティティを構造化データに変換
```python
import pandas as pd
entities = [(ent.text, ent.label_) for ent in doc.ents]
df = pd.DataFrame(entities, columns=['Entity', 'Type'])
print(df)
```

**結果:**

| Entity           | Type   |
|------------------|--------|
| Steve Jobs       | PERSON |
| Steve Wozniak    | PERSON |
| Apple            | ORG    |
| April 1, 1976    | DATE   |
| Cupertino        | GPE    |
| California       | GPE    |

**チュートリアルとコードサンプル:**  
- [spaCy固有表現ドキュメント](https://spacy.io/usage/linguistic-features#named-entities)
- [MachineLearningMastery: BERTでNERを行う方法](https://machinelearningmastery.com/how-to-do-named-entity-recognition-ner-with-a-bert-model/)

## 主要なNERツール、ライブラリ、API

| ツール/ライブラリ                | ハイライト/最適用途                                              | 言語           | 参考資料 |
|------------------------------- |---------------------------------------------------------------------|----------------|-----------|
| [spaCy](https://spacy.io/)     | 高速、本番環境対応、カスタマイズ可能、事前学習モデル                 | Python         | [spaCyドキュメント](https://spacy.io/usage/linguistic-features#named-entities) |
| [NLTK](https://www.nltk.org/)  | 教育用、基本的なNER、言語分析                                       | Python         | [NLTKドキュメント](https://www.nltk.org/) |
| [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) | 学術的ゴールドスタンダード、ルール用RegexNER、多言語サポート | Java、Python   | [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) |
| [Tonic Textual](https://www.tonic.ai/products/textual) | エンタープライズNER、編集、合成、カスタムモデル                    | API、Python SDK| [Tonic Textual](https://www.tonic.ai/products/textual) |
| [DeepPavlov](https://deeppavlov.ai/) | ディープラーニング、事前学習モデル、ドメイン適応                    | Python         | [DeepPavlov](https://deeppavlov.ai/) |
| [Google Cloud NLP](https://cloud.google.com/natural-language)