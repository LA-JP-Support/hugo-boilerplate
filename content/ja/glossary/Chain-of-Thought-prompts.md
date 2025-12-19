---
title: Chain-of-Thought プロンプト
lastmod: '2025-12-19'
date: 2025-12-19
translationKey: chain-of-thought-prompts
description: Chain-of-Thought(CoT)プロンプトについて学びます。これは、AIモデルが複雑なタスクに対して段階的な中間論理を明示的に表現するよう導くことで、AI推論を強化するプロンプトエンジニアリング技術です。
keywords:
- Chain of Thought (CoT)
- プロンプトエンジニアリング
- 大規模言語モデル (LLM)
- 推論ステップ
- AIシステム
category: AI Chatbot & Automation
type: glossary
draft: false
e-title: Chain-of-Thought Prompts
term: チェーン・オブ・ソート・プロンプト
url: "/ja/glossary/Chain-of-Thought-prompts/"
---
## 概要:Chain-of-Thoughtプロンプトとは何か?

Chain-of-Thought(CoT)プロンプトは、AIモデルから直接的な回答だけでなく、中間的な推論ステップを引き出すように設計されています。このアプローチは人間が問題を解決する方法を模倣し、数学的問題解決、記号的推論、多段階の意思決定などの複雑な推論タスクにモデルが取り組めるようにします。Wei et al.(2022)による基礎研究は、CotプロンプティングがLLMに創発的な推論能力を示させることを実証しました。特に段階的論理の例示が提供された場合に効果的です([Wei et al., 2022, arXiv](https://arxiv.org/abs/2201.11903))。

Cotプロンプティングはモダンなプロンプトエンジニアリングの中核技術となり、特に論理的で多段階の推論を必要とするタスクにおいて、AIモデルの精度と透明性の両方を向上させています([Prompt Engineering Guide: CoT](https://www.promptingguide.ai/techniques/cot); [IBM Think Blog](https://www.ibm.com/think/topics/chain-of-thoughts))。

## Chain-of-Thoughtプロンプティングの仕組み

### 基本原理

標準的なプロンプトは通常、モデルに直接的な回答を求めます。Chain-of-Thoughtプロンプトは、モデルに「作業過程を示す」よう指示し、問題を論理的なステップに分解します。これは以下の方法で実現されます:

- モデルに段階的に推論するよう明示的に指示する
- 中間的な推論を示すサンプルQ&Aペアを含める
- 「段階的に考えましょう」などの手がかりを使用して詳細な推論を促す([Prompt Engineering Guide: CoT](https://www.promptingguide.ai/techniques/cot))

#### 例:標準プロンプト vs. Chain-of-Thoughtプロンプト

| プロンプトタイプ | プロンプト例 | モデルの応答 |
|-----------------|-------------|-------------|
| 標準 | Q: 23 × 7は何ですか? | A: 161 |
| Chain-of-Thought | Q: 23 × 7は何ですか?段階的に考えましょう。 | A: 23 × 7 = (20 × 7) + (3 × 7) = 140 + 21 = 161。答えは161です。 |

**重要なポイント:**  
Cotプロンプトはモデルに中間ステップを明示させることで、複雑なタスクの精度と解釈可能性を向上させます。

## Chain-of-Thoughtプロンプティングが重要な理由

### 推論能力の強化

- **パフォーマンスの向上:** Cotプロンプティングにより、LLMは算術、常識、記号的推論、意思決定など、多段階の論理を必要とする問題に取り組めるようになります([Wei et al., 2022](https://arxiv.org/abs/2201.11903))。
- **人間らしい推論:** クエリを論理的なステップに分解することで、CotはAI出力を人間の問題解決アプローチに整合させます。
- **透明性とデバッグ:** 中間ステップにより、モデルの論理を観察、理解、デバッグすることが容易になります([PromptHub: CoT Guide](https://www.prompthub.us/blog/chain-of-thought-prompting-guide))。

### 典型的なユースケース

- 数学的問題解決
- コードのデバッグと説明
- 法律および財務分析
- 医療診断
- チュータリングと段階的な説明
- 複雑な意思決定支援システム

## ステップバイステップ:Chain-of-Thoughtプロンプトの構築

### 1. タスクの特定

数学の文章題や論理的推論など、段階的な推論から恩恵を受ける問題を選択します。

### 2. プロンプティング手法の選択

**a. Zero-shot Cotプロンプティング:**  
プロンプトに明示的な指示を追加します(例:「段階的に考えましょう」)。  
[Zero-shot Cotの詳細](https://www.promptingguide.ai/techniques/cot#zero-shot-cot-prompting)

**b. Few-shot Cotプロンプティング:**  
新しい質問の前に、段階的な推論を示すいくつかの例を含めます。

**c. Self-Consistency CoT:**  
複数の推論パスを生成し、最も一貫性のある回答を選択します—[Self-Consistency Prompting](https://learnprompting.org/docs/intermediate/self_consistency)、[Prompt Engineering Guide: Consistency](https://www.promptingguide.ai/techniques/consistency)を参照。

### 3. 例示の作成(Few-shotの場合)

望ましい推論スタイルを示すQ&Aペアを提供します:

```plaintext
Q: 林には15本の木があります。植樹後、21本の木があります。何本植えられましたか?
A: 最初に15本の木があります。植樹後、21本になりました。したがって、21 - 15 = 6。答えは6です。
```

### 4. 対象の質問を追加

例示と同じスタイルで新しい問題を提示します。

### 5. (オプション)CoT誘導フレーズの追加

Zero-shot Cotの場合、以下のようなフレーズを追加します:

- 「段階的に考えましょう。」
- 「答えを出す前に推論プロセスを説明してください。」
- 「これを段階的に解いてください。」

## Chain-of-Thoughtプロンプティング:詳細な例

### 例1:算術の文章題

**プロンプト(Few-shot CoT):**
```plaintext
Q: 林には15本の木があります。植樹後、21本の木があります。何本植えられましたか?
A: 最初に15本の木があります。植樹後、21本になりました。したがって、21 - 15 = 6。答えは6です。

Q: 駐車場に3台の車があり、さらに2台の車が到着した場合、駐車場には何台の車がありますか?
A: 最初に3台の車があります。2台の車が到着します。3 + 2 = 5。答えは5です。

Q: Leahは32個のチョコレートを持っていて、妹は42個持っていました。35個食べた場合、合計で何個残っていますか?
A:
```
**期待されるモデル出力:**
```plaintext
最初に、Leahは32個のチョコレートを持っていました。妹は42個持っていました。合計は32 + 42 = 74です。35個食べた後、74 - 35 = 39。答えは39です。
```

### 例2:常識推論におけるZero-shot CoT

**プロンプト:**
```plaintext
Johnは本をバックパックに入れて、車に置いていきました。本はどこにありますか?
段階的に考えましょう。
```
**期待されるモデル出力:**
```plaintext
まず、Johnは本をバックパックに入れました。次に、バックパックを車に置いていきました。したがって、本は車の中にあります。
```

さらなる例は[Prompt Engineering Guide: CoT](https://www.promptingguide.ai/techniques/cot)および[PromptHub: CoT Guide](https://www.prompthub.us/blog/chain-of-thought-prompting-guide)を参照してください。

## バリエーションと関連技術

Chain-of-Thoughtプロンプティングは複数のバリエーションを生み出しており、それぞれに特定の強みとユースケースがあります:

| バリエーション | 説明 | ユースケース | 強み | トレードオフ |
|---------------|------|-------------|------|-------------|
| **Zero-shot CoT** | 例なしで推論の手がかり(「段階的に考えましょう」)を追加 | 一般的な推論 | シンプル、低オーバーヘッド | 複雑なタスクでは精度が低い |
| **Few-shot CoT** | 質問の前に推論ステップを含む例示プロンプトを提供 | 数学、論理、複雑なタスク | 高精度 | 高品質な例示が必要 |
| **Self-Consistency CoT** | 複数の推論パスを生成し、最も一貫性のある回答を選択 | 高リスク、重要なタスク | 信頼性の向上 | 計算コストが高い |
| **Auto-CoT** | クラスタリング/サンプル選択を通じてFew-shot Cotの推論例示を自動生成 | 大規模で多様なタスク | 手動作業の削減 | 外部ツールが必要な場合がある |
| **Tree-of-Thought(ToT)** | ツリー構造で複数の推論パスを探索し、代替案を評価 | 計画、決定木 | 分岐、バックトラッキングに対応 | 高い計算/リソース使用 |
| **Multimodal CoT** | 複数のデータタイプ(テキスト、画像など)にわたる推論を統合 | ビジョン-言語タスク | より豊かなクロスモーダル推論 | モデル/プロンプトの複雑性 |

- ToTの詳細については、[Prompt Engineering Guide: ToT](https://www.promptingguide.ai/techniques/tot)、[Zero to Mastery: ToT](https://zerotomastery.io/blog/tree-of-thought-prompting/)、[LearnPrompting: ToT](https://learnprompting.org/docs/advanced/decomposition/tree_of_thoughts)を参照してください。
- Auto-CoTについては、[PromptHub: CoT Guide](https://www.prompthub.us/blog/chain-of-thought-prompting-guide)を参照してください。

## Self-Consistencyプロンプティング

Self-consistencyはCotの拡張版です。単一の推論チェーンに依存する代わりに、モデルは同じプロンプトに対して複数の推論パスを生成し、多数決で回答を選択します([Prompt Engineering Guide: Consistency](https://www.promptingguide.ai/techniques/consistency); [LearnPrompting: Self-Consistency](https://learnprompting.org/docs/intermediate/self_consistency))。このアプローチは、特に算術、常識、記号的推論タスクにおいて信頼性と精度を向上させます。例えば、モデルが段階的推論を使用してメールを複数回分類するよう求められた場合、最も頻繁に出現する回答が最終的な分類として選択されます。

## Tree-of-Thoughtプロンプティング

Tree-of-Thought(ToT)プロンプティングは、モデルがツリー状の構造で複数の推論パスを探索・評価できるようにすることでCotを一般化し、人間の問題解決戦略を模倣します([Prompt Engineering Guide: ToT](https://www.promptingguide.ai/techniques/tot); [LearnPrompting: ToT](https://learnprompting.org/docs/advanced/decomposition/tree_of_thoughts))。モデルは各ステップで複数の部分的解決策を提案し、それらを評価し、どの分岐を拡張またはバックトラックするかを選択します。これは最良優先探索アルゴリズムに似ています。

**応用例:**

- 数学パズル(例:24ゲーム)
- 創作活動(複数の物語パスの計画)
- ビジネスロジックと計画における複雑な決定木

**利点:**  
代替案の探索を可能にし、解決策の堅牢性を高め、バックトラッキングを可能にします—ただし、より高い計算コストがかかります。

## 実世界での応用とユースケース

- **数学と記号的推論:**  
  詳細な段階的計算による方程式の解法、算術の文章題、論理パズル([Wei et al., 2022](https://arxiv.org/abs/2201.11903))。
- **プログラミングとデバッグ:**  
  段階的なコード説明、バグの追跡、根拠の生成。
- **医療診断:**  
  症状と検査結果の順次分析。
- **法律とコンプライアンス分析:**  
  事実から結論への推論を概説することによる判例法や規制の解釈。
- **財務分析:**  
  財務履歴を分解することによる信用スコアリングとリスク評価。
- **教育/チュータリング:**  
  学生向けのガイド付き説明と問題解決。
- **複雑な意思決定:**  
  ロボティクス、戦略計画、ゲームにおける多段階サポート。

## Chain-of-Thoughtプロンプティングの利点

- **精度の向上:**  
  複雑なタスクを論理的なステップに分解することで、正しい回答の可能性が高まります([Prompt Engineering Guide: CoT](https://www.promptingguide.ai/techniques/cot))。
- **透明性:**  
  中間ステップによりモデル出力が解釈可能になります。
- **デバッグ可能性:**  
  段階的な応答により、モデルがどこで誤る可能性があるかが明らかになります。
- **汎用性:**  
  数学、言語、コード、論理など、幅広い分野に適用可能です。
- **ファインチューニング不要:**  
  モデルの再トレーニングではなく、プロンプト設計を通じて実装されます。

## 制限と課題

- **計算コストの増加:**  
  多段階の出力はより多くのトークンと計算を消費します([LearnPrompting: Self-Consistency](https://learnprompting.org/docs/intermediate/self_consistency))。
- **品質への依存:**  
  効果は適切に作成されたプロンプトと例示に依存します。
- **ハルシネーションのリスク:**  
  モデルはもっともらしいが不正確な推論チェーンを生成する可能性があります。
- **応答時間の延長:**  
  段階的な出力により遅延が増加します。
- **スタイルへの過適合:**  
  例示の過度な使用は汎化を低下させる可能性があります。
- **主観的な評価:**  
  「推論」の改善の評価は定性的になる可能性があります。

## 比較表:Cotバリエーションとその特性

| 手法 | プロンプト構造 | 精度 | セットアップの複雑さ | ユースケース | 制限 |
|------|---------------|------|---------------------|-------------|------|
| 標準プロンプティング | 直接Q → A | 低〜中程度 | 最小限 | シンプルなQ&A | 多段階タスクでは不十分 |
| Zero-shot CoT | Q + 「考えましょう…」 | 中程度 | 低 | 迅速なプロトタイピング、一般的 | 複雑なタスクでは効果が低い |
| Few-shot CoT | 例 + Q | 高 | 中程度 | 数学、論理、推論 | 関連する例示が必要 |
| Self-Consistency CoT | 複数のCoT出力 | 非常に高い | 高 | 重要/高リスクタスク | 高コスト(計算) |
| Auto-CoT | 自動化された例示 | 高 | 中〜高 | 大規模で多様なデータセット | セットアップ時間、追加ツール |
| ToT | ツリー構造のステップ | 最高 | 非常に高い | 決定木、計画 | 高コスト、複雑 |

## 実装のヒント

- 複雑な推論には、多様で適切に選択された例示を使用したFew-shot Cotを使用します。
- 迅速な展開には、推論誘導フレーズを使用したZero-shot Cotを使用します。
- 高信頼性アプリケーションには、Self-consistencyとCotを組み合わせます。
- 回答だけでなく、推論ステップの妥当性と忠実性を検証します。
- 分岐/創造的なタスクには、Tree-of-Thoughtプロンプティングを試してください([LearnPrompting: ToT](https://learnprompting.org/docs/advanced/decomposition/tree_of_thoughts))。

## よく使用されるChain-of-Thoughtキーワード

- Chain of Thought(CoT)
- 中間推論ステップ
- 複雑な推論タスク
- Few-shotプロンプティング
- Zero-shot CoT
- 論理的ステップ
- 記号的推論
- 推論パス
- 段階的思考
- 意思決定
- 推論チェーン
- Tree-of-Thought(ToT)
- Auto-CoT
- Self-consistency
- エージェンティックAI

## まとめ表:重要なポイント

| 側面 | 説明 |
|------|------|
| **定義** | AIに推論を論理的で中間的なステップに分解させるプロンプティング |
| **目的** | 複雑な推論タスクにおける精度と解釈可能性の向上 |
| **バリエーション** | Zero-shot、Few-shot、Self-consistency、Auto-CoT、Tree-of-Thought |
| **主な利点** | 精度の向上、透明性、デバッグ可能性、汎用性 |
| **制限** | 計算コスト、高品質なプロンプトの必要性、ハルシネーションのリスク |
| **最適なユースケース** | 数学、コード、論理、法律、医療、教育、意思決定タスク |
| **実装** | 段階的な指示または例示を追加し、タスクの複雑さに応じてバリエーションを選択 |

## 参考文献

1. Wei, J., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903), [PDF](https://arxiv.org/pdf/2201.11903)
2. Kojima, T., et al. (2022). "Large Language Models are Zero-Shot Reasoners." [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)
3. IBM Research. "[What is chain of thought (CoT) prompting?](https://www.ibm.com/think/topics/chain-of-thoughts)"
4. [Prompt Engineering Guide: Chain-of-Thought Prompting](https://www.promptingguide.ai/techniques/cot)
5. [Prompt Engineering Guide: Self-Consistency](https://www.promptingguide.ai/techniques/consistency)
6. [Prompt Engineering Guide: Tree of Thoughts](https://www.promptingguide.ai/techniques/tot)
7. [PromptHub: Chain of Thought Prompting Guide](https://www.prompthub.us/blog/chain-of-thought-prompting-guide)
8. [LearnPrompting: Self-Consistency](https://learnprompting.org/docs/intermediate/self_consistency)
9. [LearnPrompting: Tree of Thoughts](https://learnprompting.org/docs/advanced/decomposition/tree_of_thoughts)
10. [Zero to Mastery: Tree-of-Thought Prompting](https://zerotomastery.io/blog/tree-of-thought-prompting/)

**注記:**  
この用語集エントリは、実世界のAIシステムでChain-of-Thoughtプロンプティング技術を設計、評価、または実装するAI、自動化の専門家、プロンプトエンジニア、上級実務者向けの技術リファレンスです。

**さらなる探求と最新の例については、以下をご覧ください:**  
- [arXiv: Chain-of-Thought Prompting Elicits Reasoning in LLMs (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)  
- [Prompt Engineering Guide: CoT](https://www.promptingguide.ai/techniques/cot)  
- [LearnPrompting: Self-Consistency](https://learnprompting.org/docs/intermediate/self_consistency)  
- [PromptHub: Chain of Thought Prompting Guide](https://www.prompthub.us/blog/chain-of-thought-prompting-guide)  
- [Prompt Engineering Guide: Tree of Thoughts](https://www.promptingguide.ai/techniques/tot)
