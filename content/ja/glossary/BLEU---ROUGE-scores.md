---
title: BLEUスコア/ROUGEスコア
lastmod: '2025-12-19'
date: '2025-12-19'
translationKey: bleu-rouge-scores
description: BLEUスコアとROUGEスコアについて学びましょう。機械翻訳、要約、AIにおいて、機械生成テキストを人間の参照テキストと比較評価するための重要なNLP評価指標です。
keywords:
- BLEUスコア
- ROUGEスコア
- NLP評価
- 機械翻訳
- テキスト要約
category: AI Chatbot & Automation
type: glossary
draft: false
e-title: BLEU/ROUGE Scores
term: ブルースコア/ルージュスコア
url: "/ja/glossary/bleu---rouge-scores/"
aliases:
- "/ja/glossary/BLEU---ROUGE-scores/"
---
## BLEUスコアとROUGEスコアとは?
BLEUスコアとROUGEスコアは、自然言語処理(NLP)において、機械生成テキストと人間が作成した参照テキストとの類似性を評価するための確立された指標です。これらの指標は単語やフレーズレベルでの重複を定量化し、生成AIシステムの体系的な比較と品質追跡を可能にします。

**BLEU (Bilingual Evaluation Understudy)**
- 候補テキストと参照テキスト間のn-gram重複の精度を評価
- 元々は機械翻訳用に設計
- 言語生成、画像キャプション生成、技術文書作成の標準指標

**ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**
- 再現率に焦点を当てた指標群
- n-gram、単語シーケンス、単語ペアの重複を測定
- テキスト要約、パラフレーズ生成、質問応答において特に影響力が大きい

両者とも参照ベースの指標であり、比較のために1つ以上の正解テキストが必要です。

## 理論的基礎

**BLEU:精度重視**

計算式:
```
BLEU = BP × exp(Σ wₙ log pₙ)
```

ここで:
- BP = 簡潔性ペナルティ(短い出力を抑制)
- wₙ = n-gram精度の重み
- pₙ = サイズnのn-gramに対する修正精度

修正精度:
```
pₙ = (サイズnの一致n-gram数) / (候補内のサイズnの総n-gram数)
```

簡潔性ペナルティ:
```
BP = {1 if c > r; e^(1-r/c) if c ≤ r}
```
ここで c = 候補の長さ、r = 参照の長さ

**ROUGE:再現率重視**

**主要なバリエーション**
- **ROUGE-N**: N-gram重複(ROUGE-1はユニグラム、ROUGE-2はバイグラム)
- **ROUGE-L**: 最長共通部分列に基づく
- **ROUGE-W**: 重み付きLCS(長い一致に高スコア)
- **ROUGE-S**: スキップバイグラム(順序を保った単語ペア、間隔あり可)

ROUGE-N計算式:
```
ROUGE-N = (重複n-gram数) / (参照内の総n-gram数)
```

ROUGE-L計算式:
```
精度 = LCS(X,Y) / |Y|
再現率 = LCS(X,Y) / |X|
F1 = (1+β²)PR / (R + β²P)
```

## 使用方法

**BLEUワークフロー**
1. 候補テキストと参照テキストをトークン化
2. n-gramを抽出(通常4-gramまで)
3. 過剰カウントを避けるためクリッピングして一致n-gramをカウント
4. 各n-gram次数の修正精度を計算
5. 精度の幾何平均を計算
6. 簡潔性ペナルティを適用
7. 0から1の間のスコアを出力

**ROUGEワークフロー**
1. 両テキストをトークン化・正規化
2. 重複n-gramをカウントまたはLCSを検出
3. 再現率、精度、F1を計算
4. 複数の参照がある場合、最大値または平均値を取る
5. 0から1の間のスコアを出力

## 実践的な計算

**BLEU (Python、NLTK)**
```python
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

reference = [['the', 'cat', 'is', 'on', 'the', 'mat']]
candidate = ['the', 'cat', 'is', 'on', 'mat']

bleu_score = sentence_bleu(reference, candidate, 
                          smoothing_function=SmoothingFunction().method1)
```

**ROUGE (Python、rouge-score)**
```python
from rouge_score import rouge_scorer

reference = "the cat is on the mat"
candidate = "the cat is on mat"

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
scores = scorer.score(reference, candidate)
```

## ユースケース

**機械翻訳**
- BLEUは翻訳出力の比較における標準指標

**テキスト要約**
- ROUGEは要約のカバレッジ評価のデフォルト指標

**画像キャプション生成と対話**
- 応答が参照と一致すべき場合に両指標を適用

**質問応答**
- RAGやクローズドドメインQAにおける正解との重複をベンチマーク

**QAパイプラインの自動化**
- AI生成アノテーションのスコアを自動計算
- 受理/フラグ付けの閾値を設定

## 指標のバリエーション

**BLEUバリエーション**
- BLEU-1: ユニグラム精度のみ
- BLEU-2: バイグラムを追加
- BLEU-4: 4-gramまで(翻訳の標準)

**ROUGEバリエーション**
- ROUGE-1: ユニグラム重複
- ROUGE-2: バイグラム重複
- ROUGE-L: 最長共通部分列
- ROUGE-S: スキップバイグラム重複

## スコアの解釈

| 指標 | 範囲 | 良好なスコア | 解釈 |
|--------|-------|-----------|----------------|
| BLEU | 0–1 | >0.6 | 高い重複、流暢な出力 |
| ROUGE-1 | 0–1 | >0.5 | 主要コンテンツをカバー |
| ROUGE-L | 0–1 | >0.5 | 構造的類似性 |

**注意事項:**
- 複数の参照により信頼性が向上
- BLEUはより厳格で、創造的な出力では高スコアは稀
- ROUGEはパラフレーズに対してより寛容

## 強みと制限

| 側面 | BLEU | ROUGE |
|--------|------|-------|
| 方向性 | 精度 | 再現率 |
| 最適用途 | 翻訳、技術コンテンツ | 要約、抽出 |
| 強み | 高速、言語非依存 | カバレッジを捉える、パラフレーズに対応 |
| 制限 | 再現率を無視、同義語に非感応 | 冗長性を報酬する可能性 |

**よくある落とし穴**
- 両者とも同義語やパラフレーズを使用した出力を過小評価
- BLEUは短い出力にペナルティ
- 参照外の有効な回答に低スコア
- スコア解釈にはデータセットのコンテキストが必要

## 比較表

| 特徴 | BLEU | ROUGE |
|---------|------|-------|
| 正式名称 | Bilingual Evaluation Understudy | Recall-Oriented Understudy for Gisting |
| 焦点 | 精度(候補 → 参照) | 再現率(参照 → 候補) |
| 典型的用途 | 機械翻訳 | 要約、パラフレーズ |
| スコア計算 | n-gram精度の幾何平均 | 再現率、精度、F1 |
| バリエーション | BLEU-1からBLEU-4 | ROUGE-N、ROUGE-L、ROUGE-S |
| 強み | 流暢性、精度 | コンテンツカバレッジ、構造 |

## ベストプラクティス

- 翻訳と厳密なシーケンス忠実性にはBLEU-4を使用
- 要約にはROUGE-LとROUGE-1を使用
- 複数の参照により公平性が向上
- METEOR、BERTScore、人間評価と組み合わせる
- スケーラブルな評価のためCI/CDに統合

**実践的なヒント**
- テキストを正規化:小文字化、句読点除去
- BLEUの短い出力にはスムージングを使用
- タスクごとに経験的に「良好な」スコアを決定
- デフォルトでパラフレーズを使用—引用は稀な例外とすべき(15語以上)
- ソースごとに引用は最大1つ

## よくある質問

**BLEUとROUGEの違いは何ですか?**
BLEUは精度(候補のうち参照にある割合)を測定し、ROUGEは再現率(参照のうち候補にある割合)を測定します。

**BLEUとROUGEはいつ使い分けるべきですか?**
翻訳や精度重視のタスクにはBLEUを使用し、要約やカバレッジ重視のタスクにはROUGEを使用します。

**高スコアは常により良いですか?**
必ずしもそうではありません。スコアはタスク、データセット、ベースラインとの比較のコンテキストで解釈する必要があります。

**これらの指標は意味的類似性を評価できますか?**
いいえ。語彙的重複を測定するもので、意味的意味は測定しません。意味評価には埋め込みベースの指標と組み合わせてください。

## 参考文献

- [GeeksforGeeks: Understanding BLEU and ROUGE Score](https://www.geeksforgeeks.org/nlp/understanding-bleu-and-rouge-score-for-nlp-evaluation/)
- [SuperAnnotate: BLEU - ROUGE Guide](https://doc.superannotate.com/docs/guide-bleu-rouge)
- [Elastic: Evaluating RAG Metrics](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics)
- [BLEU Score - Wikipedia](https://en.wikipedia.org/wiki/BLEU)
- [NLTK BLEU Documentation](https://www.nltk.org/api/nltk.translate.html#nltk.translate.bleu_score.sentence_bleu)
- [rouge-score PyPI](https://pypi.org/project/rouge-score/)
