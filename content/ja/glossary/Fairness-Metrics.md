---
title: 公平性メトリクス
date: 2025-11-25
translationKey: fairness-metrics
description: 公平性メトリクスは、AI/MLシステムにおけるバイアスを定量化、評価、監視するために使用される数学的・統計的ツールであり、グループ間での公平な扱いを確保します。
keywords:
- 公平性メトリクス
- AIバイアス
- アルゴリズムバイアス
- 責任あるAI
- 機械学習の公平性
category: AI Ethics & Safety Mechanisms
type: glossary
draft: false
e-title: Fairness Metrics
term: こうへいせいめとりくす
reading: 公平性メトリクス
kana_head: その他
---
## **公平性メトリクスとは?**

公平性メトリクスは、人工知能(AI)および機械学習(ML)システムにおけるバイアスを定量化、評価、監視するために設計された数学的・統計的ツールです。これらのメトリクスは、AIモデルが個人やグループを公平に扱っているか、または人種、性別、年齢、社会経済的地位などの機微な属性に基づいて不当に不利益を与えているかを評価する構造化された方法を提供します。

公平性メトリクスは、責任あるAI開発の中核をなすものです。これにより、組織はアルゴリズムバイアスを特定、測定、軽減することができます。これは、信頼できるAIの構築、規制への準拠の確保、社会的受容の促進にとって重要です。

- **参考:** [Shelf.io: Fairness Metrics in AI](https://shelf.io/blog/fairness-metrics-in-ai/)  
- **参考:** [Google ML Fairness Guide](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias)

## **公平性メトリクスが使用される理由**

AIモデルは、採用、医療、法執行、金融、教育における意思決定にますます影響を与えています。セーフガードがなければ、これらのモデルは以下のような問題を引き起こす可能性があります:

- 訓練データに存在する既存のバイアスを永続化または増幅する
- 特定の個人やグループに不当な不利益を与える(例:マイノリティに対する融資承認率の低下)
- 評判、倫理、法的リスクを生み出す

**公平性メトリクスは以下の目的で使用されます:**

- 人口統計グループ間の異なる結果を定量化し監視する
- モデル開発およびデプロイメント中にアルゴリズムバイアスを特定し対処する
- データの調整、アルゴリズムの改良、決定閾値の修正などの是正措置を導く
- ステークホルダー、規制当局、一般市民に対して[透明性](/en/glossary/transparency/)と説明責任を示す
- 以下を含む規制への準拠を確保する:
  - [EU AI法](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)
  - [公正信用報告法](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)
  - [平等信用機会法](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/equal-credit-opportunity-act/)
  - [アルゴリズム説明責任法(米国)](https://www.congress.gov/bill/117th-congress/house-bill/6580/text)
  - [GDPR](https://gdpr.eu/)

## **公平性メトリクスは実際にどのように使用されるか?**

**公平性メトリクスを使用するワークフロー:**

1. **データ収集と準備**
   - 人口統計および機微な属性データ(例:性別、人種、年齢)を収集する
   - すべての関連グループに対して代表的なデータを確保する
   - 参考: [AI Bias and Data Collection](https://shelf.io/blog/ai-bias/)

2. **モデルの訓練と評価**
   - ラベル付きデータセットでモデルを訓練する
   - 公平性メトリクスを使用してグループ間でモデル出力を評価する
   - 参考: [Google ML Crash Course - Fairness](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias)

3. **バイアス評価**
   - 1つ以上の公平性メトリクスを適用して結果の格差を測定する
   - 特定のサブグループを分析し、不公平が発生している箇所を特定する

4. **軽減と反復**
   - 公平性メトリクスからの実用的な洞察を使用して、データ、アルゴリズム、または閾値を修正する
   - 許容可能な公平性レベルが達成されるまで再評価と反復を行う
   - 参考: [AIF360 Bias Mitigation Algorithms](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.algorithms.html)

5. **監視と報告**
   - デプロイメント後も公平性メトリクスを継続的に監視する
   - 監査とコンプライアンスのために調査結果と軽減努力を文書化する
   - 参考: [Model Cards for Model Reporting](https://modelcards.withgoogle.com/about)

**モデルライフサイクルとの統合:**

- **前処理:** 訓練前にデータのバイアスに対処する(例:再重み付け、データ拡張)
- **処理中:** モデル訓練中に公平性制約または正則化を適用する
- **後処理:** より公平な結果のために訓練後にモデル予測または閾値を調整する

## **公平性メトリクスの主要なタイプ**

### **1. デモグラフィックパリティ(統計的パリティ/グループ公平性)**

- **定義:** 異なる人口統計グループの個人が肯定的な結果(例:採用通知、融資承認)を受け取る確率が同じであることを保証します。
- **数式:**  
  P(Outcome = 1 | Group A) = P(Outcome = 1 | Group B)
- **使用例:**
  - 採用アルゴリズム:男性と女性の選考率が等しいことを保証する
  - 融資承認:民族間で承認率が等しい
- **制限事項:**
  - グループの資格の違いを考慮しない
  - 厳格な実施は「逆差別」や効用の低下につながる可能性がある
- **参考:** [Fairness Metrics in AI—Your Step-by-Step Guide](https://shelf.io/blog/fairness-metrics-in-ai/#toc-header-3)

### **2. 機会均等**

- **定義:** 異なるグループの適格な個人が肯定的な結果を受け取る確率が同じであることを保証します。
- **数式:**  
  P(Outcome = 1 | Qualified = 1, Group A) = P(Outcome = 1 | Qualified = 1, Group B)
- **使用例:**
  - 大学入学:すべての背景を持つ同等の資格を持つ学生が等しい入学率を持つ
  - 社内昇進:同等の資格を持つ従業員が等しい昇進機会を持つ
- **制限事項:**
  - 「資格」の正確で偏りのない測定に依存する
- **参考:** [Google ML Fairness Guide](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias)

### **3. 均等化オッズ(オッズの平等)**

- **定義:** 真陽性率と[偽陽性](/en/glossary/false-positive/)率がグループ間で等しいことを保証します。
- **数式:**  
  - TPR: P(Outcome = 1 | Actual = 1, Group A) = P(Outcome = 1 | Actual = 1, Group B)
  - FPR: P(Outcome = 1 | Actual = 0, Group A) = P(Outcome = 1 | Actual = 0, Group B)
- **使用例:**
  - 刑事司法リスク評価:すべての人種で正しい予測率と誤った予測率が等しい
  - 医療診断:性別間で診断エラー率が等しい
- **制限事項:**
  - 達成が困難;他のメトリクスやモデル精度と矛盾する可能性がある
- **参考:** [Shelf.io Fairness Metrics](https://shelf.io/blog/fairness-metrics-in-ai/#toc-header-3)

### **4. 予測パリティ(予測平等/予測値パリティ)**

- **定義:** 精度(陽性予測値)がグループ間で等しいことを保証します。
- **数式:**  
  P(Actual = 1 | Outcome = 1, Group A) = P(Actual = 1 | Outcome = 1, Group B)
- **使用例:**
  - 融資デフォルト予測:承認された申請者が返済する可能性が人口統計間で等しい
  - 医療治療推奨:すべての患者グループで治療成功を予測する精度が等しい
- **制限事項:**
  - 機会均等または均等化オッズと矛盾する可能性がある
- **参考:** [AIF360 Documentation](https://aif360.res.ibm.com/)

### **5. 処遇平等**

- **定義:** 偽陽性と偽陰性の比率がグループ間で等しいことを保証します。
- **数式:**  
  P(Outcome = 1 | Actual = 0, Group A) / P(Outcome = 0 | Actual = 1, Group A) =  
  P(Outcome = 1 | Actual = 0, Group B) / P(Outcome = 0 | Actual = 1, Group B)
- **使用例:**
  - 予測的警察活動:誤逮捕と見逃された犯罪率のバランスを取る
  - 不正検出:顧客セグメント間で誤警報と見逃された不正を均等化する
- **制限事項:**
  - 解釈と実装が複雑
- **参考:** [Shelf.io Fairness Metrics](https://shelf.io/blog/fairness-metrics-in-ai/#toc-header-3)

### **6. 個人公平性**

- **定義:** 類似した個人はAIシステムから類似した結果を受け取るべきです。
- **測定:** タスク固有の類似性メトリクスと、類似した入力ケースに対するモデルの一貫性の分析が必要です。
- **使用例:**
  - 融資承認:類似した財務プロファイルを持つ個人が類似した決定を受ける
  - 医療トリアージ:比較可能な患者が一貫した推奨を受ける
- **制限事項:**
  - 「類似性」の定義は主観的でコンテキスト依存
- **参考:** [AIF360 Documentation](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.html)

### **7. 反事実的公平性**

- **定義:** 機微な属性(例:人種、性別)が変更されても、他のすべてが一定に保たれている場合、モデルの予測は同じままであることを保証します。
- **測定:** 実際の入力と反事実的(変更された)入力の予測結果を比較します。
- **使用例:**
  - 融資申請:申請者の性別が異なっていても他のすべてが同じであれば、決定は変わるか?
  - 求人選考:保護された属性によって決定が影響を受けないことを保証する
- **制限事項:**
  - 因果モデリングと反事実的データ生成が必要
- **参考:** [Forbes: AI & Fairness Metrics](https://councils.forbes.com/blog/ai-and-fairness-metrics)

## **実世界の例と使用例**

### **採用アルゴリズム**
- **問題:** 履歴書スクリーニングツールが特定の性別または民族の候補者を優遇する
- **適用されるメトリクス:** デモグラフィックパリティ、機会均等
- **軽減策:** 訓練データの調整、公平性制約の適用、選考率の監視
- **参考:** [Google ML Fairness Use Case](https://developers.google.com/machine-learning/crash-course/fairness/video-lecture)

### **顔認識システム**
- **問題:** 代表性の低いグループ(例:有色人種)に対するエラー率が高い
- **適用されるメトリクス:** 均等化オッズ
- **軽減策:** 訓練データの多様化、モデルの再訓練、パフォーマンス格差の監査
- **参考:** [NIST Face Recognition Vendor Test](https://www.nist.gov/programs-projects/face-recognition-vendor-test-frvt)

### **融資承認**
- **問題:** 歴史的バイアスによるマイノリティ申請者の承認率の低下
- **適用されるメトリクス:** 予測パリティ、反事実的公平性
- **軽減策:** デバイアスの適用、閾値の調整、規制準拠の確保
- **参考:** [AIF360 Case Studies](https://aif360.res.ibm.com/)

### **医療診断**
- **問題:** 特定の人口統計グループに対する診断ツールの精度が低い
- **適用されるメトリクス:** 均等化オッズ、処遇平等
- **軽減策:** 訓練データの拡張、公平性メトリクスの監視、ドメイン専門家の関与
- **参考:** [Google AI Blog: Fairness in Healthcare](https://ai.googleblog.com/2019/10/ensuring-fairness-in-medical-ai.html)

## **オープンソースの公平性メトリクスライブラリとツール**

- **[Fairlearn](https://fairlearn.org/):** モデルの公平性を評価し改善するためのPythonライブラリ。メトリクス、軽減アルゴリズム、可視化機能を備えています。
- **[AIF360 (AI Fairness 360)](https://aif360.res.ibm.com/):** 幅広い公平性メトリクスと[バイアス軽減](/en/glossary/bias-mitigation/)技術を備えたIBMツールキット。
- **[Fairness Indicators](https://www.tensorflow.org/tfx/guide/fairness_indicators):** 特にTensorFlowモデル向けの公平性メトリクスを評価し可視化するためのGoogleのツール。
- **[FairComp](https://www.faircomp.io/):** 公平性介入を比較し、異なるメトリクスをベンチマークするためのライブラリ。
- **[FairML](https://github.com/adebayoj/fairml):** モデルの公平性を監査し、バイアスの原因を特定するためのツール。
- **[Aequitas](https://github.com/dssg/aequitas):** 人口統計グループに対するモデルの影響を分析するための監査ツール。
- **[Themis](https://github.com/LASER-UMASS/Themis) & [Themis-ML](https://github.com/cosmicBboy/themis-ml):** 個人公平性に焦点を当てたライブラリ。

## **公平性メトリクスを使用するためのベストプラクティス**

1. **複数のメトリクスを使用する:**  
   公平性の全体像を把握するために複数のメトリクスを組み合わせます。
   - 参考: [Shelf.io Best Practices](https://shelf.io/blog/fairness-metrics-in-ai/#toc-header-5)

2. **コンテキストを考慮する:**  
   実世界への影響に合わせてメトリクスの選択と解釈を調整します。

3. **ステークホルダーを関与させる:**  
   影響を受けるグループ、ドメイン専門家、意思決定者を巻き込みます。

4. **定期的な監査:**  
   デプロイメント後も公平性メトリクスを継続的に監視します。

5. **文書化と報告:**  
   公平性分析、決定、是正措置を記録することで透明性を維持します。

6. **公平性と精度のバランス:**  
   公平性の向上は精度を低下させる可能性があります;多目的最適化を使用し、情報に基づいたトレードオフを行います。

## **よくある落とし穴とその回避方法**

- **単一のメトリクスに依存する:**  
  1つのメトリクスだけでは全体像を提供することはほとんどありません。
- **社会的コンテキストを無視する:**  
  関連する社会的・倫理的枠組みの中でメトリクスを解釈します。
- **静的な評価:**  
  データ、モデル、人口が変化するにつれて定期的に再評価します。
- **相関と因果関係を混同する:**  
  格差は、モデルのバイアスだけでなく、現実世界の不平等を反映している可能性があります。
- **透明性を軽視する:**  
  文書化の失敗は、コンプライアンスの問題と信頼の喪失につながる可能性があります。

## **コンプライアンス、規制、業界標準**

**法的・規制的枠組み:**

- **[EU AI法](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence):** 透明性、説明責任、公平性の要件を設定;リスク評価と文書化を義務付けます。
- **[公正信用報告法(FCRA)](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act):** 信用データの使用を規制し、自動化された信用決定における差別を禁止します。
- **[平等信用機会法(ECOA)](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/equal-credit-opportunity-act/):** 融資決定における差別を禁止します。
- **[GDPR](https://gdpr.eu/):** EU内の自動化された決定に対する透明性と「説明を受ける権利」を義務付けます。
- **[アルゴリズム説明責任法(米国)](https://www.congress.gov/bill/117th-congress/house-bill/6580/text):** (提案中)アルゴリズムバイアス評価と報告を要求します。

**業界ガイドライン:**

- **倫理委員会と責任あるAI委員会:** 公平性とバイアスに関する組織的監督。
- **文書化標準:** モデルカードとデータシートは公平性チェックとリスクを記録します。
  - 参考: [Model Cards](https://modelcards.withgoogle.com/about)
  - 参考: [Datasheets for Datasets](https://arxiv.org/abs/1803.09010)

## **用語集:主要用語**

- **バイアス(AI):** 偏ったデータ、欠陥のあるアルゴリズム、または歪んだ訓練によって引き起こされるAI出力の体系的なエラー。
- **機微な属性:** 意思決定に使用された場合に差別につながる可能性のある人口統計的特徴(人種、性別、年齢)。
- **異なる影響:** 機微な属性が明示的に使用されていなくても、モデル予測が保護されたグループに不均衡に害を与えること。
- **透明性:** AI決定とプロセスが理解、監査、説明できる程度。
- **説明責任:** AIシステムの結果、特に公平性に関して正当化し、責任を負う義務。

## **さらなる読み物とリソース**

- [Shelf.io: Fairness Metrics in AI](https://shelf.io/blog/fairness-metrics-in-ai/)
- [Forbes: AI & Fairness Metrics](https://councils.forbes.com/blog/ai-and-fairness-metrics)
- [Google ML Fairness Guide](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias)
- [AI Evaluation Metrics – Bias & Fairness](https://www.francescatabor.com/articles/2025/7/10/ai-evaluation-metrics-bias-amp-fairness)
- [Fairlearn documentation](https://fairlearn.org/)
- [AIF360 documentation](https://aif360.res.ibm.com/)
- [EU AI Act summary](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)

**動画:**
- [YouTube: ML Fairness (Google Crash Course)](https://www.youtube.com/watch?v=59bMh59JQDo)
- [YouTube: Responsible AI—Fairness and Bias](https://www.youtube.com/watch?v=F03lK5q6ohM)

## **要約表:一般的な公平性メトリクス**

| メトリクス                | 測定内容                                           | 数式(簡略化)                                      | 使用例                        |
|-----------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------|
| デモグラフィックパリティ    | グループ間で肯定的な率が等しい                        | P(Y=1|A=a) = P(Y=1|A=b)                                   | 採用、融資承認                   |
| 機会均等     | 適格な個人に対するTPRが等しい                       | P(Y=1|Y*=1, A=a) = P(Y=1|Y*=1, A=b)                       | 大学入学                   |
| 均等化オッズ        | グループ間でTPRとFPRが等しい                           | TPR_a = TPR_b; FPR_a = FPR_b                              | 刑事司法、医療診断  |
| 予測パリティ     | グループ間で精度(PPV)が等しい                       | P(Y*=1|Y=1, A=a) = P(Y*=1|Y=1, A=b)                       | 融資デフォルト予測                 |
| 処遇平等    | グループ間でFP/FN比が等しい                           | FP/FN ratio_a = FP/FN ratio_b                             | 予測的警察活動、不正検出    |
| 個人公平性   | 類似した個人が類似した結果を得る                  | Distance(Y(x), Y(x')) ≈ Distance(x, x')                   | 融資承認、医療トリアージ    |