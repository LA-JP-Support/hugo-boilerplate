---
title: 精度と再現率
translationKey: precision-and-recall
description: 精度と再現率は、分類システムや情報検索システムを評価するための中核的な指標です。精度は正しい陽性予測を測定し、再現率はすべての実際の陽性を見つけ出します。
keywords:
- 精度
- 再現率
- 機械学習
- 分類指標
- 混同行列
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: せいどとさいげんりつ
reading: 精度と再現率
kana_head: その他
e-title: Precision and Recall
---

## カテゴリー:AIチャットボット&自動化

**定義:**  
適合率(Precision)と再現率(Recall)は、分類および情報検索システムのパフォーマンスを評価するために使用される中核的な指標です。適合率はモデルが正の予測を正しく識別する能力を定量化し、再現率は実際の正例をすべて見つける能力を測定します。両方の指標は、特にクラスが不均衡な場合や、特定のタイプのエラーが異なるコストを伴う場合に、モデルの強みと弱みを理解するために不可欠です。

## TL;DR(要約)

- **適合率(Precision):** 正と予測したもののうち、実際に正しかったものの割合。
- **再現率(Recall)(感度/真陽性率):** 実際の正例のうち、モデルが正しく識別したものの割合。
- これらの指標は、特に不均衡なデータセットや偽陽性と偽陰性のコストが異なる場合に、モデルを評価するために重要です。
- 適合率と再現率は通常トレードオフの関係にあります:一方を改善すると他方が低下する可能性があります。
- 偽陽性を最小化するには適合率を、偽陰性を最小化するには再現率を使用します。
- モデルのパフォーマンスをバランスよく把握するため、常に両方の指標(そして多くの場合F1スコア)を報告してください。

## 適合率と再現率とは?

適合率と再現率は、教師あり機械学習、特に分類および情報検索タスクにおいて最も広く使用される評価指標の2つです。  
- **適合率:** モデルが正と予測したすべてのインスタンスのうち、実際に正であった割合は?
- **再現率:** データセット内のすべての実際の正のインスタンスのうち、モデルが正しく識別したのは何個?

これらの重要性は以下の場合に増大します:
- データセットが不均衡である(一方のクラスが他方よりもはるかに稀である)。
- 偽陽性と偽陰性のコストが同じではない。

**権威ある参考資料:**  
- [Google ML Crash Course: Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)  
- [EvidentlyAI: Accuracy vs Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)  

## 混同行列:基礎

適合率と再現率は両方とも**混同行列(Confusion Matrix)**から導出されます。混同行列は分類アルゴリズムの結果を要約するものです。

|                       | **予測:正** | **予測:負** |
|-----------------------|-----------------------|-----------------------|
| **実際:正**   | 真陽性(TP)    | 偽陰性(FN)   |
| **実際:負**   | 偽陽性(FP)   | 真陰性(TN)    |

- **真陽性(TP):** モデルが正のインスタンスを正しく予測した。
- **偽陽性(FP):** モデルが誤って正と予測した(実際は負)。
- **真陰性(TN):** モデルが負のインスタンスを正しく予測した。
- **偽陰性(FN):** モデルが誤って負と予測した(実際は正)。

混同行列は、適合率、再現率、F1スコア、正確度、特異度など、ほぼすべての分類評価指標の出発点です。

**リソース:**  
- [EvidentlyAI: Confusion Matrix Explained](https://www.evidentlyai.com/classification-metrics/confusion-matrix)

## 適合率:定義、公式、直感的理解

### 定義

適合率は正の予測の正確性を測定します。*「モデルが正とラベル付けしたすべてのインスタンスのうち、実際に正だったのは何個?」*という問いに答えます。

### 公式

\[
\text{適合率} = \frac{\text{真陽性(TP)}}{\text{真陽性(TP)} + \text{偽陽性(FP)}}
\]

### 直感的理解

適合率は、モデルが偽陽性エラーをほとんど起こさない場合に高くなります。言い換えれば、「正」と予測したとき、通常は正しいということです。  
- **高い適合率:** 誤警報が少ない;正の予測のほとんどが真である。
- **低い適合率:** 誤警報が多い;正の予測がしばしば間違っている。

### 適合率が重要なのはいつ?

適合率は、偽陽性のコストが高い場合に特に重要です。  
**例:**
- **スパム検出:** 高い適合率により、正当なメールがスパムとしてマークされることがほとんどなくなります。([GeeksforGeeks: Precision and Recall](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/))
- **法的文書レビュー:** 関連性のない文書を関連性があると誤ってラベル付けすることはコストがかかります。

### 制限事項

- 適合率を過度に最適化すると、モデルが多くの真陽性を見逃す可能性があります(再現率の低下)。
- モデルが非常に確信がある場合にのみ「正」と予測すると、正の予測をほとんど行わなくなり、高い適合率だが低い再現率につながる可能性があります。

## 再現率:定義、公式、直感的理解

### 定義

再現率(感度または真陽性率とも呼ばれる)は、モデルがすべての実際の正のインスタンスを見つける能力を測定します。*「データ内のすべての真の正例のうち、モデルが捕捉したのは何個?」*という問いに答えます。

### 公式

\[
\text{再現率} = \frac{\text{真陽性(TP)}}{\text{真陽性(TP)} + \text{偽陰性(FN)}}
\]

### 直感的理解

再現率は、モデルが実際の正のケースをほとんど見逃さない場合に高くなります。  
- **高い再現率:** モデルがほとんどの正例を見つける(偽陰性が少ない)。
- **低い再現率:** モデルが多くの正例を見逃す(偽陰性が多い)。

### 再現率が重要なのはいつ?

再現率は、正のケースを見逃すことが高いコストを伴う場合に重要です。  
**例:**
- **医療診断:** 病気を見逃すこと(偽陰性)は致命的になる可能性があります。高い再現率により、ほとんどの病気の患者が発見されます。
- **不正検出:** 不正な取引を見逃すことはコストがかかります。

### 制限事項

- 再現率を過度に最適化すると、モデルが多くの偽陽性エラーを起こす可能性があります(適合率の低下)。
- モデルがほぼすべてを正とラベル付けすると、再現率は高くなりますが適合率は低下します。

## 適合率と再現率の計算:ステップバイステップの例

**ケーススタディ:** 不正なクレジットカード取引の検出。

- **データセット:** 1,000件の取引;50件が不正(正のクラス)、950件が正常。
- **モデルの予測:** 40件の取引を不正と予測。
    - 30件は実際に不正(**TP=30**)
    - 10件は不正ではない(**FP=10**)
- 50件の実際の不正のうち、20件はモデルに見逃される(**FN=20**)
- モデルは940件を正常と正しく識別(**TN=940**)

**混同行列:**

|                       | **予測:不正** | **予測:正常** |
|-----------------------|--------------------|------------------------|
| **実際:不正**      | 30 (TP)            | 20 (FN)                |
| **実際:正常**  | 10 (FP)            | 940 (TN)               |

**計算:**

- **適合率:**  
  \[
  \text{適合率} = \frac{TP}{TP + FP} = \frac{30}{30+10} = 0.75
  \]  
  *解釈:不正としてフラグが立てられた取引の75%が実際に不正でした。*

- **再現率:**  
  \[
  \text{再現率} = \frac{TP}{TP + FN} = \frac{30}{30+20} = 0.60
  \]  
  *解釈:モデルはすべての不正ケースの60%を識別しました。*

**視覚的参考資料:**  
- [GeeksforGeeks: Precision and Recall Example](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/)

## 適合率 vs. 再現率:トレードオフとユースケース

適合率と再現率は通常、互いにトレードオフの関係にあります:

| **指標**   | **最適化すべき場合**                 | **単独で最大化した場合のリスク**     | **アプリケーション例**          |
|--------------|-----------------------------------|---------------------------------|----------------------------------|
| 適合率    | 偽陽性がコストがかかる        | 真陽性を見逃す(低い再現率) | スパム検出、法的レビュー     |
| 再現率       | 偽陰性がコストがかかる/危険 | 多くの偽陽性(低い適合率) | 医療スクリーニング、不正検出 |

**適合率-再現率のトレードオフ:**  
- **高い適合率、低い再現率:** モデルはめったに正の予測を行わないが、それらはほとんど正しい。
- **高い再現率、低い適合率:** モデルはほとんどの正例を見つけるが、多くの負例を誤って正とラベル付けする。

**閾値依存性:**  
適合率と再現率のバランスは、モデルの決定閾値を使用して調整できます:  
- 閾値を下げると再現率が増加しますが適合率が低下します。
- 閾値を上げると適合率が増加しますが再現率が低下します。

**視覚化と曲線:**
- **適合率-再現率曲線:** さまざまな閾値での適合率と再現率をプロットします。([scikit-learn documentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html))
- **ROC曲線:** 真陽性率(再現率)と偽陽性率をプロットします。

## 適合率、再現率、または両方をいつ使用するか

- **適合率:** 偽陽性が高いコストを伴う場合に焦点を当てる(例:重要なメールをスパムとしてマークする)。
- **再現率:** 偽陰性が高いコストを伴う場合に焦点を当てる(例:がん診断を見逃す)。
- **両方:** ほとんどの実世界の問題では、偽陽性と偽陰性の両方に結果があるため、両方の指標のバランスを取る必要があります。

**リソース:**  
- [EvidentlyAI: When to Use Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)

## 関連指標:F1スコア、正確度、ROC-AUC、特異度

### F1スコア

F1スコアは適合率と再現率の調和平均です:

\[
\text{F1} = 2 \times \frac{\text{適合率} \times \text{再現率}}{\text{適合率} + \text{再現率}}
\]

- **使用する場合:** 適合率と再現率のバランスを取る単一の指標が必要な場合、特に不均衡なデータセットの場合。

### 正確度

\[
\text{正確度} = \frac{TP + TN}{TP + FP + TN + FN}
\]

- **制限事項:** クラスが不均衡な場合、誤解を招く可能性があります。  
  ([Google ML Crash Course: Accuracy vs Precision vs Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall))

### ROC-AUC(受信者操作特性曲線 - 曲線下面積)

- **ROC曲線:** 異なる閾値での真陽性率(再現率)と偽陽性率をプロットします。
- **AUC:** ROC曲線の下の面積;すべての閾値にわたってクラスを区別するモデルの能力を測定します。
- モデルを比較し、トレードオフを視覚化するのに役立ちます。  
  ([DeepAI: ROC Curve](https://deepai.org/machine-learning-glossary-and-terms/receiver-operating-characteristic-curve))

### 特異度

\[
\text{特異度} = \frac{TN}{TN + FP}
\]

- 正しく識別された実際の負例の割合を測定します。
- 医療診断で特に関連性があり、しばしば再現率(感度)と一緒に使用されます。

## よくある落とし穴と制限事項

- **クラス不均衡を無視する:** 高い正確度は稀なクラスでの低いパフォーマンスを隠す可能性があります;適合率と再現率はより多くの洞察を提供します。
- **1つの指標のみを報告する:** 重大な弱点を隠す可能性があります;常に適合率と再現率の両方を報告してください。
- **閾値感度:** 適合率と再現率の値は決定閾値に依存します;複数の閾値で評価するか、曲線を使用してください。
- **未定義(NaN)値:** 正の予測がない場合(TP + FP = 0)、適合率は未定義(NaN)です。  
  ([Google ML Crash Course: Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall))

## 適合率と再現率を使用するためのベストプラクティス

- 正確度だけでなく、両方の指標を評価して報告する。
- 混同行列を使用してモデルのエラーを理解する。
- 要約としてF1スコアを報告するが、常に適合率と再現率を含める。
- 適合率-再現率曲線とROC曲線でパフォーマンスを視覚化する。
- ビジネスまたは安全要件を満たすために決定閾値を調整する。
- アプリケーションにおけるエラーの実世界のコストに基づいて指標を選択する。
- 徹底的な評価のために、特異度、ROC-AUC、平均適合率などの追加指標で補完する。

**リソース:**  
- [EvidentlyAI: Classification Metrics Guide](https://www.evidentlyai.com/classification-metrics)

## 適合率と再現率のユースケース例

| **ドメイン**        | **ユースケース**           | **優先度** | **理由**                                         |
|-------------------|-----------------------|--------------|----------------------------------------------------|
| 医療診断 | 疾患スクリーニング     | 再現率       | 病気の患者を見逃すことは非常に重大な結果を招く     |
| スパム検出    | メールフィルタリング       | 適合率    | 本物のメールをスパムとしてマークすることは破壊的         |
| 不正検出   | 取引監視| 再現率       | 不正を見逃すことはコストがかかる                          |
| 検索エンジン    | 関連文書の検索 | 両方   | ユーザーはすべての関連性のある結果と少ない無関係な結果を望む |
| 画像認識 | 物体検出      | 両方(文脈依存) | 見逃しまたは余分な検出のコストに依存 |

## 要約表:適合率 vs. 再現率

| **側面**             | **適合率**                        | **再現率**                         |
|------------------------|--------------------------------------|------------------------------------|
| 定義             | TP / (TP + FP)                       | TP / (TP + FN)                     |
| 焦点                  | 正の予測の正確性  | 実際の正例のカバレッジ       |
| 高い値の意味       | 偽陽性が少ない                  | 偽陰性が少ない                |
| 使用する場合               | 偽陽性がコストがかかる           | 偽陰性がコストがかかる         |
| アプリケーション例    | スパムフィルター(正当なメールの損失を最小化) | 疾患スクリーニング(すべての病気のケースを見つける) |

## 参考文献とさらなる読み物

- [Google ML Crash Course: Accuracy, Precision, Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [EvidentlyAI: Accuracy vs Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)
- [GeeksforGeeks: Precision and Recall](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/)
- [DeepAI: Precision and Recall](https://deepai.org/machine-learning-glossary-and-terms/precision-and-recall)
- [BuiltIn: Precision and Recall](https://builtin.com/data-science/precision-and-recall)
- [Lyzr: Glossary - Precision and Recall](https://www.lyzr.ai/glossaries/precision-and-recall/)

## 用語集:主要用語

- **真陽性(TP):** 正しく予測された正のインスタンス。
- **偽陽性(FP):** 誤って予測された正のインスタンス。
- **偽陰性(FN):** モデルに見逃された実際の正例。
- **真陰性(TN):** 正しく予測された負のインスタンス。
- **混同行列:** TP、FP、TN、FNを要約する表。
- **閾値:** モデルが正と予測する値;これを調整すると適合率と再現率が変化します。
- **クラス不均衡:** 一方のクラスが他のクラスよりもはるかに頻繁に出現する場合。
- **F1スコア:** 適合率と再現率の調和平均。

## さらなる学習

- [EvidentlyAI: Confusion Matrix Explained](https://www.evidentlyai.com/classification-metrics/confusion-matrix)
- [DeepAI: ROC Curve and AUC](https://deepai.org/machine-learning-glossary-and-terms/receiver-operating-characteristic-curve)
- [BuiltIn: F1 Score and Advanced Metrics](https://builtin.com/data-science/f1-score)
- [scikit-learn: Precision-Recall Curves](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

## ビデオガイド

- [StatQuest: Precision and Recall, Clearly Explained (YouTube)](https://www.youtube.com/watch?v=0pP4EwWJgIU)
- [Corey Schafer: Precision and Recall Explained (YouTube)](https://www.youtube.com/watch?v=Kdsp6soqA7o)

**まとめ:**  
適合率と再現率は、分類モデルのパフォーマンスを評価するための基礎です—特に単純な正確度が実世界のコストやクラス不均衡を捉えられない場合に重要です。これらの指標を理解しバランスを取ること、F1スコアやROC-AUCなどの関連指標と合わせて、AIおよび自動化システムの堅牢で文脈を考慮した評価と展開を保証します。

**詳細、高度なチュートリアル、ライブ例については、これらの信頼できるリソースをご覧ください:**

- [Google ML Crash Course: Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
- [EvidentlyAI: Accuracy vs Precision vs Recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)
- [GeeksforGeeks: Precision and Recall](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/)
- [scikit-learn: Precision-Recall Curves](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)