---
title: 対話状態追跡
translationKey: dialogue-state-tracking
description: 対話状態追跡(DST)は、対話システムにおいてユーザーの目標、スロット値、会話履歴を推定し、一貫性のある適切なAI応答を可能にします。
keywords: ["対話状態追跡", "会話型AI", "チャットボット", "対話システム", "スロットフィリング"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: たいわじょうたいついせき
reading: 対話状態追跡
kana_head: その他
e-title: Dialogue State Tracking
---
## Dialogue State Tracking(対話状態追跡)とは?

Dialogue State Tracking(DST)は、タスク指向型の会話AI システムの基盤となる技術です。複数ターンにわたる会話を通じて重要な詳細情報を体系的に追跡し、以下の構造化された機械可読な表現を維持します:

- **ユーザーの目標と意図**
- **スロット値**(ユーザーが表現した特定の情報)
- **対話履歴とコンテキスト**

各ターンにおいて、DSTはユーザーの現在の目的とそれを達成するために必要なすべての関連パラメータを推定します。これにより、システムは次に何をすべきか、何を言うべきかについて情報に基づいた意思決定を行い、会話の一貫性と関連性を確保できます。

DSTは、ユーザー入力の解釈(自然言語理解技術を通じて)と[対話管理](/ja/glossary/dialogue-management/)(システム応答の意思決定)の間の仲介役として機能します。会話ループの重要な部分を形成します:ユーザーの発話が処理され、状態が推定され、システムが次のアクションを決定します。

**参考文献:**
- [Fiveable NLP Study Guide: Dialogue State Tracking and Management](https://fiveable.me/natural-language-processing/unit-10/dialogue-state-tracking-management/study-guide/INVJzuMxkLvmaoRV)
- [Stanford NLP: Chatbots & Dialogue Systems](https://web.stanford.edu/~jurafsky/slp3/old_dec21/24.pdf)
- [YouTube: What Are Common Dialogue State Tracking Approaches?](https://www.youtube.com/watch?v=5wlVFr90l1k)

## Dialogue State Trackingの用途

DSTは以下の目的で使用されます:

- **会話コンテキストの維持:** 以前のターンと解決済み情報の記憶を保持することで、継続性と一貫性を確保します。
- **対話ポリシーの誘導:** チャットボットやエージェントに適切な次のアクション(例:不足データの質問、詳細の確認、タスクの実行)を通知します。
- **曖昧さの解決:** 複数ターンにわたる照応(アナフォラ)を処理し、特にノイズや曖昧なコンテキストでユーザーのリクエストを明確化します。
- **応答のパーソナライズ:** ユーザーの好みや過去のインタラクションに基づいてシステムの動作を適応させ、コンテキストを考慮したユーザー向けの返答を可能にします。
- **複数ターンの推論を実現:** 予約やトラブルシューティングなどのタスクに不可欠な、複数の対話ターンにまたがる複雑なクエリと依存関係を追跡します。

**応用領域には以下が含まれます:**

- **バーチャルアシスタント:** 例:Alexa、Siri、Google Assistant
- **カスタマーサポートチャットボット:** 例:自動ヘルプデスク、ライブチャットサポート
- **自動予約システム:** 例:レストラン、ホテル、フライト、タクシー
- **会話型コマース:** カート、好みを追跡するショッピングアシスタント
- **ヘルスケアエージェント:** 複数ターンにわたる患者情報の収集、トリアージ
- **技術トラブルシューティング:** ステップバイステップのガイダンスとコンテキスト保持

**参考文献:**
- [Hybrid Dialogue State Tracking for Persian Chatbots - arXiv](https://arxiv.org/html/2510.01052v1)
- [IBM: Conversational AI Examples, Applications & Use Cases](https://www.ibm.com/think/topics/conversational-ai-use-cases)
- [Stanford NLP: Chatbots & Dialogue Systems](https://web.stanford.edu/~jurafsky/slp3/old_dec21/24.pdf)

## 主要な概念と用語

| 用語                        | 定義                                                                                         |
|-----------------------------|----------------------------------------------------------------------------------------------------|
| **スロット(Slot)**                    | 特定の情報を表す変数(例:「場所」、「時間」、「料理」)。    |
| **スロット値(Slot Value)**              | スロットに対するユーザー提供またはシステム推論された値(例:「場所」に対する「ニューヨーク」)。           |
| **スロット値ペア(Slot-Value Pair)**         | スロットとその現在の値のキー・バリューレコード(例:{"time": "7 PM"})。                       |
| **対話状態(Dialogue State)**          | 各ターンで追跡されるすべてのスロット値ペアとその他のコンテキスト情報の現在のセット。      |
| **信念状態(Belief State)**            | 可能な対話状態に対する確率分布;確率的DSTで使用される。                |
| **オントロジー(Ontology)**                | ドメインのすべての可能なスロットとその許可値を定義するスキーマ。                       |
| **情報可能スロット(Informable Slot)**         | ユーザーが制約として指定できるスロット(例:「area = north」)。                                |
| **要求可能スロット(Requestable Slot)**        | ユーザーが情報を要求できるスロット(例:「住所は何ですか?」)。                      |
| **ターン(Turn)**                    | ユーザーの発話とシステムの応答のペア。                                                  |
| **対話ポリシー(Dialogue Policy)**         | 現在の対話状態に基づいて次のシステムアクションを選択する意思決定ロジック。         |

**参考文献:**
- [Dialog State Tracking Challenge Series: A Review (Semantic Scholar)](https://pdfs.semanticscholar.org/4ba3/39bd571585fadb1fb1d14ef902b6784f574f.pdf)
- [arXiv: Scalable Multi-Domain Dialogue State Tracking](https://arxiv.org/pdf/1712.10224)
- [ACL Anthology: The Dialog State Tracking Challenge](https://aclanthology.org/W13-4065.pdf)

## Dialogue State Trackingのアプローチ

DSTは、ルールベースのパターンマッチングシステムから複雑なデータ駆動型アーキテクチャへと進化してきました。主なアプローチには以下が含まれます:

### ルールベースDST

- **仕組み:** 手作業で作成されたルールやパターンが、ユーザー入力に応じて対話状態を更新します。例えば、ユーザーが「イタリアン料理が欲しい」と言った場合、`cuisine = Italian`と設定します。
- **長所:** シンプル、解釈可能、データ不要。
- **短所:** 言語の多様性やスケールに対して堅牢でなく、未知のシナリオに脆弱で、集中的な手作業によるエンジニアリングが必要。
- **参考文献:**  
  - [MindMeld: Dialogue State Handlers](https://www.mindmeld.com/docs/quickstart/04_define_the_dialogue_handlers.html)

### 確率的DST

- **仕組み:** 可能な対話状態に対する確率分布(信念状態)を維持します。更新は、ベイジアンネットワーク、マルコフ決定過程(MDP)、部分観測マルコフ決定過程(POMDP)などの統計モデルを使用して実行されます。
- **長所:** 不確実性や入力エラー(例:音声認識から)に対して堅牢で、曖昧な言語を処理できます。
- **短所:** 計算集約的で、特徴量エンジニアリングが必要で、パラメータ推定のための十分なデータが必要。
- **参考文献:**  
  - [A hybrid approach to dialogue management based on probabilistic rules](http://home.nr.no/~plison/pdfs/cl/probrules-plison-csl2015.pdf)
  - [ScienceDirect: Hybrid Approach to Dialogue Management](https://www.sciencedirect.com/science/article/abs/pii/S0885230815000029)

### 機械学習/深層学習DST

- **仕組み:** 再帰型ニューラルネットワーク(RNN)、LSTM/GRU、Transformer(BERT、GPT)、条件付き確率場(CRF)などのモデルを使用して、会話データから直接対話状態を更新することを学習します。
- **長所:** 複雑な対話パターンを捉え、ドメイン間で汎化し、大規模アプリケーションをサポートします。
- **短所:** 大規模な注釈付きデータセットが必要で、ルールベースシステムよりも解釈性が低い。
- **技術例:**
    - 逐次対話モデリングのためのRNN/LSTM/GRU([MA-DST](https://ojs.aaai.org/index.php/AAAI/article/download/6322/6178))
    - 会話コンテキストをエンコードするためのTransformer(BERT/GPT)([Chain of Thought for DST](https://arxiv.org/html/2403.04656v1))
    - 関連する履歴に焦点を当てるアテンションメカニズム
    - 対話から直接スロット値を抽出するポインターネットワーク

- **参考文献:**  
  - [arXiv: Hybrid Dialog State Tracker](https://arxiv.org/pdf/1510.03710)
  - [AAAI: MA-DST](https://ojs.aaai.org/index.php/AAAI/article/download/6322/6178)

### ハイブリッド手法

- **仕組み:** ルールベースと機械学習アプローチを組み合わせます;ルールは頻繁/単純なケースを処理し、MLは稀/複雑なシナリオを処理します。
- **長所:** ルールの解釈可能性とMLの堅牢性を活用します。
- **短所:** 統合の複雑さ。
- **参考文献:**  
  - [Hybrid Dialogue State Tracking for Persian Chatbots - arXiv](https://arxiv.org/html/2510.01052v1)

## 対話状態の表現形式

DST状態は、システム要件に応じて複数の方法で表現できます:

### スロット値ペア

- **最も一般的な形式。**
- 各スロット(キー)が現在の値を保持します。例:
  ```json
  {
    "cuisine": "Italian",
    "location": "New York",
    "time": "7 PM"
  }
  ```
- 解釈が容易で、データベース/APIインターフェースに使用されます。

### 特徴ベクトル

- スロット値と対話特徴をエンコードする固定長の数値ベクトル。
- ML/DLモデル、特にニューラルネットとの統合に有用。

### グラフベース構造

- ノードはエンティティ、スロット、またはユーザー意図を表し、エッジは関係と依存関係を捉えます。
- 複雑なマルチドメイン会話の推論を容易にし、知識グラフとインターフェースできます。

**参考文献:**
- [Fiveable: Dialogue State Tracking and Representation](https://fiveable.me/natural-language-processing/unit-10/dialogue-state-tracking-management/study-guide/INVJzuMxkLvmaoRV)
- [Dialogue Agents 101 (arXiv)](https://arxiv.org/html/2307.07255v2)
- [Medium: Five Approaches To Managing Conversational Dialog](https://cobusgreyling.medium.com/five-approaches-to-managing-conversational-dialog-3f43d3255584)

## 対話状態更新メカニズム

対話状態の更新はDSTの中核機能です。メカニズムには以下が含まれます:

### ルールベース更新

- 事前定義されたルールが、パターンマッチング、正規表現、またはテンプレート手法を使用してユーザーの発話を状態変更にマッピングします。
- シンプルまたは明確に定義されたタスクに対して高速で信頼性があります。

### 確率的更新

- ベイズ推論が、入力ソース(例:音声認識エラー)からの不確実性を考慮して信念状態を更新します。
- 初期の音声対話システムで一般的で、ノイズに対して堅牢です。

### ニューラル/MLベース更新

- シーケンスモデル(RNN、Transformer)が対話履歴と現在の入力を処理して新しいスロット値を予測します。
- アテンションメカニズムが関連するコンテキストに焦点を当て、ジョイントモデリングがすべてのスロットを同時または個別に処理します。

### スロット充填

- 固有表現認識(NER)とシーケンスラベリング(例:CRFを使用)がユーザー入力からスロット値を抽出します。
- ジョイントモデルが各ターンですべての関連スロットを予測し、マルチドメインと動的シナリオをサポートします。

### Chain-of-Thought推論

- 複数の対話ターンにわたるステップバイステップの推論でスロット値を推論し、複雑なマルチターン対話をサポートします。
- 複雑なシナリオでDSTパフォーマンスを向上させることが実証されています。
- [Chain of Thought for DST - arXiv](https://arxiv.org/html/2403.04656v1)

**参考文献:**
- [Emergent Mind: User Goal State Tracking (UGST)](https://www.emergentmind.com/topics/user-goal-state-tracking-ugst)
- [Fiveable: Dialogue State Update Mechanisms](https://fiveable.me/natural-language-processing/unit-10/dialogue-state-tracking-management/study-guide/INVJzuMxkLvmaoRV)
- [YouTube: How Is Dialogue State Managed In Conversational AI?](https://www.youtube.com/watch?v=5UNuP-WyNYc)

## 評価、メトリクス、ベンチマーク

### 標準データセット

- **WOZ (Wizard of Oz):** レストラン予約における人間同士の対話([DSTC](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44018.pdf))
- **MultiWOZ:** 大規模、マルチドメイン、注釈付き対話データセット(10,000以上の対話)。
- **DSTC (Dialogue State Tracking Challenge):** DSTシステムのための一連のベンチマークタスクとデータセット。

### 一般的なメトリクス

| メトリクス                 | 説明                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------|
| **ジョイントゴール精度(Joint Goal Accuracy)**| すべてのスロットが正しく予測された対話ターンの割合(厳格な指標)。            |
| **スロット精度(Slot Accuracy)**      | 個々のスロット値予測の正確性。                                                    |
| **スロットF1スコア(Slot F1 Score)**      | スロット予測の適合率と再現率の調和平均;クラス不均衡を処理します。                  |
| **パープレキシティ(Perplexity)**         | 言語モデリングを評価し、モデルがコンテキスト内で次のトークンをどれだけ予測できるかを測定します。           |
| **人間評価(Human Evaluation)**   | システムパフォーマンスの主観的評価(一貫性、有用性、自然さ)。                   |

**参考文献:**
- [MultiWOZ Dataset](https://www.cambridge.org/engage/api-gateway/ai/assets/orp/resource/item/5c2b6e4e-0a5d-4b5b-8f1e-7a3d10e2b0d9/original/multiwoz-a-large-scale-multi-domain-wizard-of-oz-dataset-for-task-oriented-dialogue-modelling.pdf)
- [DSTC Challenges](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44018.pdf)
- [Fiveable: DST Evaluation and Metrics](https://fiveable.me/natural-language-processing/unit-10/dialogue-state-tracking-management/study-guide/INVJzuMxkLvmaoRV)

## 例とユースケース

### 例:レストラン予約の対話状態

**ターン1**
- *ユーザー:* 「イタリアンレストランを探しています。」
- **状態:**  
  ```json
  { "cuisine": "Italian" }
  ```

**ターン2**
- *ユーザー:* 「ニューヨークで。」
- **状態:**  
  ```json
  { "cuisine": "Italian", "location": "New York" }
  ```

**ターン3**
- *ユーザー:* 「午後7時で。」
- **状態:**  
  ```json
  { "cuisine": "Italian", "location": "New York", "time": "7 PM" }
  ```

**ターン4**
- *ユーザー:* 「時間を午後8時に変更してください。」
- **状態:**  
  ```json
  { "cuisine": "Italian", "location": "New York", "time": "8 PM" }
  ```

### 例:マルチドメイン対話

**ターン5の状態:**
```json
{
  "hotel-name": "York Hotel",
  "hotel-stars": "5",
  "taxi-destination": "York Hotel",
  "taxi-departure": "Cambridge Station"
}
```

**ユースケース:**
- 予約システム(フライト、ホテル、レストラン、タクシー)
- カスタマーサポート(問題追跡、ユーザー好みの保持)
- パーソナルアシスタント(リマインダー、セッション間のコンテキスト)
- ヘルスケア(マルチターンの症状収集)
- Eコマース(ショッピングカート、好み、注文詳細の管理)

**参考文献:**
- [Hybrid DST for Persian Chatbots (arXiv)](https://arxiv.org/html/2510.01052v1)
- [IBM: Conversational AI Use Cases](https://www.ibm.com/think/topics/conversational-ai-use-cases)

## 課題と最近の研究動向

### 主な課題

- **曖昧さと参照解決:** 曖昧なユーザー入力と照応(例:「そこを予約して」)の処理。
- **データ不足:** 高品質な対話データの収集と注釈付けの困難さ。
- **マルチドメインと長距離依存関係:** ドメイン間および多数のターンにわたるコンテキストの追跡。
- **語彙外スロット値:** 自由形式または以前に見たことのない値。
- **汎化:** 最小限の再トレーニングで新しいドメインやスロットスキーマに適応すること。

### 最近の動向

#### TransformerベースのDST

- Transformerモデル(BERT、GPT)が長距離会話コンテキストをエンコードし、転移学習をサポートします。
- [MA-DST (AAAI 2020)](https://ojs.aaai.org/index.php/AAAI/article/download/6322/6178)

#### アテンションとマルチアテンションメカニズム

- スロット推論のための対話の関連部分に焦点を当てます。
- クロスドメイン処理とスロット値解決を改善します。

#### Chain-of-Thought(CoT)推論

- 対話ターン全体にわたる複数ステップの推論を使用してスロット推論を改善します。
- [Chain of Thought for DST (arXiv)](https://arxiv.org/html/2403.04656v1)

#### ゼロショットとフューショット汎化

- 最小限のデータで新しいドメインへのDST適応のためのスキーマガイド型およびプロンプトベースのモデル。

#### データ拡張

- DST堅牢性を強化するための合成データ生成、言い換え、シミュレーション。

#### ジョイントモデリングとエンドツーエンドシステム

- スロット、意図、アクションの同時予測;エラー伝播を削減します。

**参考文献:**
- [DST Review (Google)](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44018.pdf)
- [MA-DST (AAAI 2020)](https://ojs.aaai.org/index.php/AAAI/article/download/6322/6178)
- [Chain of Thought for DST (arXiv)](https://arxiv.org/html/2403.04656v1)