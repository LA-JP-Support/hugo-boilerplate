---
title: Fact-Score (FActScore)
lastmod: '2025-12-19'
date: '2025-12-19'
translationKey: fact-score
description: FActScoreは、AI生成テキストにおける事実の正確性を定量化する自動評価指標です。出力を原子的事実に分解し、信頼できる外部知識ソースからの裏付けを検証します。
keywords:
- FActScore
- 事実精度
- AI生成テキスト
- 原子的事実
- LLM評価
category: AI Chatbot & Automation
type: glossary
draft: false
e-title: Fact-Score (FActScore)
term: ファクトスコア
url: "/ja/glossary/Fact-Score/"
---
## FActScoreとは何か?
FActScore(Fine-grained Atomic Evaluation of Factual Precision、細粒度原子的事実精度評価)は、AIが生成した長文テキストにおける事実精度を定量化するために設計された自動評価指標です。文書全体や文単位で評価する粗粒度の指標とは異なり、FActScoreは生成されたコンテンツを原子的事実(atomic facts)—最小限の、文脈に依存しない事実的記述—に分解し、それぞれをWikipediaなどの権威ある外部知識ソースと照合して検証します。

この指標は、サポートされた原子的事実の総原子的事実に対する比率を計算します:

**FActScore = (サポートされた事実の数 / 総原子的事実数) × 100%**

ここで、サポートされた事実とは信頼できる参照資料に対して検証されたもので、総原子的事実は生成されたテキストから抽出されたすべての事実的主張を表します。

FActScoreは、大規模言語モデル(LLM)評価における重要な限界に対処します。従来の指標は微妙な事実誤りを見逃すことが多く、幻覚(ハルシネーション)を検出できずに通過させたり、特定の不正確さを識別するための十分な粒度を提供しなかったりします。原子的事実レベルで動作することで、FActScoreはサポートされていない主張を正確に識別でき、伝記生成、医療情報、財務報告、科学コミュニケーションなど、高い事実精度を必要とするアプリケーションにとって非常に価値があります。

## コア手法:分解-検証パイプライン

FActScoreは、モジュール式の4段階パイプラインを採用しています:

**ステージ1:原子的事実生成**  
生成されたテキストを文に分割し、さらにLLMベースのプロンプトまたはルールベースの解析を使用して原子的事実に分解します。各原子的事実は、独立して検証可能な独立した最小限の事実的記述を表します。

**ステージ2:証拠検索**  
各原子的事実について、密検索器(GTRベースのシステムなど)が外部知識ソース(通常は英語版Wikipedia)から関連する証拠パッセージを抽出します。検索はエンティティ中心で、検証情報を含む可能性が最も高いパッセージをターゲットにします。

**ステージ3:原子的事実検証**  
各原子的事実を検索された証拠と照合してサポートを判定します。検証方法には以下が含まれます:

- **人間の専門家による注釈** – 専門のファクトチェッカーが各原子的事実を「サポートされている」「サポートされていない」「無関係」とラベル付け
- **自動化モデル** – LLMまたはマスク言語モデルがサポート尤度を計算し、信頼度閾値を使用して事実を分類

**ステージ4:スコア計算**  
最終的なFActScoreは、すべての抽出された原子的事実の中でサポートされた事実の割合として計算されます。

このパイプラインはオープンソースのPythonパッケージとして利用可能で、人間参加型と完全自動化の両方のデプロイメントをサポートしています。

## 評価プロトコルと精度

**人間による注釈のゴールドスタンダード**  
専門の注釈者が検索された証拠をレビューし、原子的事実にラベルを付けます。高い注釈者間一致率が信頼性を示しています:伝記生成タスクにおいて、InstructGPTで96%、ChatGPTで90%、PerplexityAIで88%です。

**自動化推定**  
自動化パイプラインは、分解と検証の両方に検索拡張LLMを使用します。人間の注釈と比較して2%未満の誤差率で、数千の出力にスケーラブルです。

**パフォーマンス指標:**

- サポートされていない事実検出のためのマイクロレベルF1、精度、再現率
- 精度 = |予測されたサポートなし ∩ ゴールドサポートなし| / |予測されたサポートなし|
- 再現率 = |予測されたサポートなし ∩ ゴールドサポートなし| / |ゴールドサポートなし|

**実装間の一貫性**  
オープンソースとプロプライエタリ実装間の強いピアソン相関(r > 0.99)により、再現可能なクロスベンチマーク比較が可能です。

## 多言語拡張と知識の限界

**多言語評価**  
標準のFActScoreパイプラインは英語中心です。非英語の出力の場合:

- テキストを英語に翻訳して原子的事実抽出と検証を実行
- 言語間でのWikipediaカバレッジの不一致を制御
- 多言語LLMベンチマーキングに使用され、多言語幻覚ギャップを特定

**知識ソースの制約**  
FActScoreの精度は、参照コーパスの品質とカバレッジに依存します:

- 低リソース言語やニッチなドメインでのWikipediaコンテンツの制限がスコアにバイアスをかける可能性
- 緩和戦略には、主張ごとにより多くのパッセージを検索すること、インターネット全体のソースで拡張すること、LLM生成の明確化を使用することが含まれます
- 事実性は、選択された参照コーパスのカバレッジと信頼性によって制限されます

## モデルパフォーマンスとアプリケーション

**ベンチマーク結果:**

- 商用モデル:GPT-4とChatGPTは公開LLMを上回る(ChatGPT ≈58% vs. 人間執筆 ≈88%)
- モデルスケーリング:大規模モデルほど高いFActScoreを達成(Alpaca 65B > 13B > 7B)
- 公開モデル:Alpaca/Vicuna(≈40%)はMPTChat(30%)とStableLM(17%)を上回る

**トレーニングとアライメントの影響:**

- モジュール式幻覚検出/編集によりFActScoreが最大16.2ポイント向上
- ファインチューニングフレームワークにより事実性が49.19%から77.53%に向上
- 批評ベースの評価によりベースラインより14-16%改善

**実用的なユースケース:**

- **モデルベンチマーキング** – 伝記や要約タスクにおける事実品質によるLLMのランキング
- **事実アライメント** – 要約や推論集約的な出力におけるサポートされていない主張の特定
- **幻覚検出** – 多言語またはドメイン固有のデプロイメントにおけるサポートされていないコンテンツの監視
- **自動ファクトチェック** – 科学コミュニケーション、気候報道、敵対的ナラティブ検出

## 堅牢性と既知の限界

**分解品質への感度**  
FActScoreの信頼性は原子的事実分解方法に依存します。代替戦略(意味解析、プロンプトエンジニアリング、異なる言語フレームワーク)は可変的な事実セットを生成します。DecompScoreは分解の原子性とカバレッジを測定します。

**敵対的脆弱性:**

- 繰り返しや些細な事実が、真の事実性を改善することなくスコアを人為的に膨らませる可能性
- MontageLieベンチマークは、真の記述を誤解を招くナラティブに並べ替えることで原子的事実評価器を欺くことを示す(AUC-ROC < 65%)
- すべての記述が個別には真実でも、選択的な順序付けにより集合的に誤解を招く可能性

**緩和戦略:**

- プラグアンドプレイモジュールがサブクレーム選択と情報性重み付けを適用
- 繰り返しを抑制しながら、ユニークで情報性の高い事実を報酬
- 事実サポートとイベント順序の一貫性の両方に対処する共同指標(DOVESCORE)

**根本的な限界:**

- 並べ替えや選択的省略を含む構成的操作を検出できない
- 外部知識ソースの広さと深さによって制限される
- 事実抽出品質はドメインと言語によって異なる
- 英語版Wikipediaとテキストのみのドメインを超えた拡張は検索の課題を導入

## 実装とアクセス

**利用可能性:**

- オープンソースPythonパッケージ:`pip install factscore`
- GitHubやOpenFActScoreを含む研究リポジトリ
- Hugging Face互換モデルをサポート

**統合オプション:**

- ゴールドスタンダード較正のための人間参加型注釈
- 大規模評価のための完全自動化評価
- 多様なモデル評価のためのサードパーティLLM互換性

**カスタマイズ:**

- Wikipediaを超える代替知識ソースへの拡張可能
- 翻訳パイプラインを通じた追加言語への適応可能
- カスタム参照コーパスを通じたドメイン固有のファクトチェック

## 技術的アプリケーション

**モデル開発:**  
AI研究所は、開発中のLLMバリアント間の事実精度を比較するためにFActScoreを使用します。結果はトレーニングデータのキュレーション、ファインチューニング戦略、モデル選択を導きます。

**品質保証:**  
コンテンツモデレーションチームは、ユーザー生成AIコンテンツにおける幻覚情報を検出しフィルタリングするためにFActScoreを適用し、プラットフォームの品質基準を維持します。

**研究評価:**  
学術研究者は、標準化された事実性指標としてFActScoreを使用して、新しいアーキテクチャ、トレーニング方法、またはプロンプトエンジニアリング技術をベンチマークします。

**本番監視:**  
顧客向けアプリケーションにLLMを展開する組織は、FActScoreを監視して事実性のドリフトを検出し、スコアが低下したときに再トレーニングまたは介入をトリガーします。

## 最近の進歩

**強化された堅牢性:**

- コアタイプモジュールは、些細な繰り返しを抑制しながらユニークで情報性の高い主張を報酬
- 事実性とイベント順序の共同指標が構成的限界に対処
- RLベースのオンラインアライメントが報酬信号に事実検証を組み込む

**拡大されたアクセシビリティ:**

- OpenFActScoreがあらゆるHugging Faceモデルに対する高忠実度評価を民主化
- 類似のBERTScore-F1と誤差率で元のベンチマークと一致
- 研究者と実務者のための事実性評価の障壁を削減

**今後の方向性:**

- 低リソース言語とマルチモーダルコンテンツへの拡張
- クロスドメイン評価(医療、法律、科学)
- 本番システムにおけるリアルタイム事実性監視
- 敵対的攻撃とナラティブ操作に対する強化された堅牢性

## 関連指標との比較

| 側面 | FActScore | 従来の指標 |
|--------|-----------|-------------------|
| 粒度 | 原子的事実レベル | 文または文書レベル |
| 参照 | 外部知識(Wikipedia) | 多くの場合なしまたは内部 |
| 評価者 | 人間または自動化 | 通常は自動化のみ |
| 幻覚検出 | 高精度 | しばしば見逃される |
| スケーラビリティ | 自動化により優れている | 様々 |
| 構成的認識 | 限定的 | 同様に限定的 |

## 主要用語

- **原子的事実(Atomic Fact)** – 生成されたテキストからの最小限の、文脈に依存しない事実的記述
- **検索器モデル(Retriever Model)** – 検証のために知識ソースから関連パッセージを取得するシステム
- **マスク言語モデリング(Masked Language Modeling、MLM)** – 検証のためにトークンをマスクして予測するアプローチ
- **幻覚(Hallucination)** – AIモデルによって生成されたサポートされていないまたは捏造されたコンテンツ
- **分解(Decomposition)** – 粒度の細かい評価のためにテキストを原子的事実に分割するプロセス
- **DecompScore** – 分解品質と原子性を評価する指標

## 参考文献

- [Min et al., 2023: FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP)](https://arxiv.org/abs/2305.14251)
- [Emergent Mind: FActScore Topic Overview](https://www.emergentmind.com/topics/factscore)
- [OpenFActScore: Open-Source Atomic Evaluation of Factuality in Text Generation](https://www.emergentmind.com/papers/2507.05965)
- [Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore](https://www.emergentmind.com/papers/2402.18045)
- [Multilingual Hallucination Gaps in Large Language Models](https://www.emergentmind.com/papers/2410.18270)
- [An Analysis of Multilingual FActScore](https://www.emergentmind.com/papers/2406.19415)
- [A Closer Look at Claim Decomposition](https://arxiv.org/html/2403.11903v1)
- [Core: Robust Factual Precision with Informative Sub-Claim Identification](https://www.emergentmind.com/papers/2407.03572)
- [PFME: A Modular Approach for Fine-grained Hallucination Detection and Editing](https://www.emergentmind.com/papers/2407.00488)
- [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://www.emergentmind.com/papers/2503.02846)
- [Improving Model Factuality with Fine-grained Critique-based Evaluator](https://www.emergentmind.com/papers/2410.18359)
- [Learning to Reason for Factuality](https://www.emergentmind.com/papers/2508.05618)
- [CLAImate: AI-Enabled Climate Change Communication](https://www.emergentmind.com/papers/2507.11677)
- [Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://arxiv.org/html/2505.15792v1)
- [TruthTorchLM: A Comprehensive Library for Predicting Truthfulness in LLM Outputs](https://www.emergentmind.com/papers/2507.08203)
- [GitHub: FActScore Repository](https://github.com/shmsw25/FActScore)
- [PyPI: FActScore Package](https://pypi.org/project/factscore/)
