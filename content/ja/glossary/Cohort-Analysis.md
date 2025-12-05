---
title: コホート分析
date: 2025-11-25
translationKey: cohort-analysis
description: コホート分析は、共通の特性に基づいてユーザーをグループに分類し、時間経過に伴う行動を追跡・比較する行動分析手法で、トレンドを明らかにします。
keywords:
- コホート分析
- リテンション
- チャーン
- 行動分析
- ユーザーエンゲージメント
category: Analytics & Content Effectiveness
type: glossary
draft: false
e-title: Cohort Analysis
term: コホートぶんせき
reading: コホート分析
kana_head: か
---
## コホート分析とは?

コホート分析は、定義された期間内で共通の特性や体験を持つユーザーをグループ(コホート)に分け、その行動を時系列で追跡・比較する行動分析手法です。すべてのユーザーを単一の未分化な集団として見るのではなく、コホート分析により特定のグループがどのように行動するかを把握でき、集計データでは隠れていたトレンドやパターンを明らかにできます。

**主要用語:**
- **コホート:** 共通の特性で定義されたユーザーグループ(例:登録日、初回購入、行動、人口統計)。
- **リテンション(継続率):** 一定期間後もアクティブなままのユーザーの割合。
- **チャーン(解約率):** 時間経過とともに製品の使用を停止したユーザーの割合。
- **獲得コホート:** 製品と最初に接触した時期でグループ化されたユーザー(例:登録月)。
- **行動コホート:** 実行したアクション(例:新機能の使用、オンボーディング完了)でグループ化されたユーザー。
- **タイムゼロ:** コホート行動を測定する開始点(例:登録日)。
- **コホート減少:** リテンションの裏側—コホートからユーザーが離脱する率。

**参考文献:**  
- [Mixpanel: Ultimate Guide to Cohort Analysis](https://mixpanel.com/blog/cohort-analysis/)
- [Corporate Finance Institute: Cohort Analysis](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/)
- [Appcues: Beginner's Guide to Cohort Analysis](https://www.appcues.com/blog/cohort-analysis)

## コホート分析はどのように使用されるか?

### ユーザーリテンションとチャーンの追跡

コホート分析は、リテンションの測定とチャーンパターンの特定に不可欠です。各コホートの何パーセントが1日目、7日目、30日目などの特定の間隔でアクティブなままかを追跡することで、ユーザーがいつ離脱するかを正確に特定し、その理由を仮説立てできます。

**例:**  
1月に1,000人のユーザーが登録し、30日後に400人がまだアクティブな場合、1月コホートの30日目リテンションは40%です。コホート分析ヒートマップは、離脱が最も深刻な箇所を視覚的に強調します。  
([Corporate Finance Institute](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/))

### 製品と機能のエンゲージメントの理解

オンボーディングを完了したユーザーなどの行動コホートを形成することで、特定のアクションが長期的なエンゲージメントにどのように影響するかを分析できます。例えば、新機能を採用したユーザーと採用しなかったユーザーのリテンション率を比較することで、どの機能が「粘着性」があり、リテンションを促進するかを明らかにできます。

**例:**  
最初の週に新機能を利用したユーザーの30日目リテンションが60%である一方、非採用者は30%のみの場合、この機能の重要性が浮き彫りになります。  
([Mixpanel Guide](https://mixpanel.com/blog/cohort-analysis/))

### 実験とキャンペーンの効果比較

マーケターやプロダクトマネージャーは、獲得チャネル、キャンペーン、機能ローンチ別にユーザー行動を比較するためにコホート分析を使用します。例えば、Facebook広告経由で獲得したユーザーとオーガニック検索からのユーザーを比較し、どのチャネルがより忠実なユーザーを生み出すかを判断できます。

### 情報に基づいた製品の反復改善

変更(新しいオンボーディングシーケンスなど)をローンチした後、コホートリテンションを追跡することで、更新の影響を検証し、データに基づいて反復改善できます。

### パーソナライゼーションとターゲットメッセージング

リスクのあるコホートや高価値コホートを特定することで、ライフサイクルの重要な瞬間にカスタマイズされた介入(メール、ナッジ、オファーなど)でユーザーをターゲットにできます。

## コホートのタイプ

### 1. 獲得コホート

**定義:** 製品と最初に接触した時期(例:登録の週または月)でユーザーをグループ化。

**使用例:**
- 登録期間別のリテンション測定
- マーケティングキャンペーンや製品ローンチの影響評価
- 季節的またはキャンペーンベースの違いの特定

**例表:獲得コホートリテンション**

| コホート(登録月) | ユーザー数 | 1日目リテンション | 7日目リテンション | 30日目リテンション |
|-----------------|----------|-----------------|-----------------|------------------|
| 1月             | 1,000    | 40%             | 25%             | 18%              |
| 2月             | 900      | 45%             | 28%             | 21%              |
| 3月             | 1,200    | 38%             | 22%             | 15%              |

特定のコホートでリテンションが急上昇または急降下した場合、その期間中の変更(例:オンボーディングフロー、キャンペーン、技術的問題)を調査する必要があることを示します。  
([Corporate Finance Institute Example](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/))

### 2. 行動コホート

**定義:** 製品内で実行した(または実行しなかった)アクションでユーザーをグループ化。

**使用例:**
- どの行動がエンゲージメントとリテンションを促進するかの特定
- 非アクティブに基づくリスクセグメントの検出
- ユーザージャーニーに関する仮説のテスト

**例表:行動コホート比較**

| コホート                | ユーザー数 | 30日目リテンション |
|------------------------|----------|-------------------|
| オンボーディング完了者  | 500      | 40%               |
| オンボーディングスキップ | 400      | 22%               |

オンボーディング完了者の高いリテンションは、オンボーディングが重要であることを示しており、その改善への投資が全体的なリテンションを促進できます。  
([Appcues Guide](https://www.appcues.com/blog/cohort-analysis))

### 3. その他のコホートタイプ

- **人口統計コホート:** 年齢、場所、デバイス
- **テクノグラフィックコホート:** アプリバージョン、ブラウザ、OS
- **プランベースコホート:** 無料vs有料、ティアレベル
- **規模ベースコホート:** 中小企業vs大企業顧客

これらの基準でセグメント化することで、行動の違いが明らかになり、特定のグループに合わせた戦略の調整に役立ちます。  
([Mixpanel Docs](https://docs.mixpanel.com/docs/users/cohorts))

## コホート分析を使用する理由

### 実行可能なインサイトの解放

- **ユーザーがいつ、なぜチャーンするかを特定:** 単一のチャーン率ではなく、離脱が正確にいつ発生するか(例:3日目、2週目)を確認。
- **粘着性のある機能を発見:** 長期的なリテンションと相関するアクションを特定。
- **オンボーディングの最適化:** 離脱ポイントを発見し、改善をテスト。
- **介入のパーソナライズ:** リスクのあるユーザーを正確なメッセージングでターゲット。

### 製品とビジネス成果の推進

- **チャーンの削減:** 大量離脱の前に痛点に積極的に対処。
- **リテンションとLTVの向上:** 顧客ライフタイムを延長する機能とアクションに焦点を当てる。
- **マーケティングROIの改善:** 高価値ユーザーをもたらすチャネルに投資。

### 製品変更の検証

- **A/Bテストの更新:** 新機能やフローがリテンションを改善するかを確認。
- **キャンペーン効果の測定:** どの獲得ソースが忠実なユーザーをもたらすかを追跡。

**参考文献:**  
- [Mixpanel: Ultimate Guide to Cohort Analysis](https://mixpanel.com/blog/cohort-analysis/)
- [Appcues: Cohort Analysis for Product Teams](https://www.appcues.com/blog/cohort-analysis)

## ステップバイステップ:コホート分析の実施方法

### 1. 目的の定義

明確なビジネス上の質問を確立:
- 早期チャーンを促進するものは何か?
- 新しいオンボーディングフローはリテンションを改善するか?
- どのチャネルが最も忠実なユーザーをもたらすか?

### 2. 追跡する指標の選択

主要指標には以下が含まれます:
- **リテンション率**(1日目、7日目、30日目など)
- **チャーン率**
- **アクティベーション率**(例:重要なアクションを完了)
- **コンバージョン率**(例:トライアルから有料へ)
- **コホート別LTV(ライフタイムバリュー)**

### 3. コホートの定義

以下のような基準を選択:
- **獲得日**(例:週次登録)
- **行動マイルストーン**(例:オンボーディング完了)
- **人口統計/プラン/機能使用**

コホートが以下であることを確認:
- **統計的に有意:** ノイズになるほど小さくない。
- **実行可能:** インサイトが希薄になるほど広くない。

### 4. コホートテーブルまたはチャートの構築

- **行:** コホート(例:登録週)
- **列:** 期間(例:1日目、7日目、30日目)
- **セル:** 保持されたユーザーの割合

**例表:**

| コホート(登録週) | ユーザー数 | 1日目 | 7日目 | 14日目 | 30日目 |
|-----------------|----------|-------|-------|--------|--------|
| 1月1-7日        | 200      | 45%   | 32%   | 25%    | 20%    |
| 1月8-14日       | 220      | 43%   | 31%   | 23%    | 18%    |

**視覚的ヒント:** ヒートマップを使用して高/低リテンションを強調。

### 5. 結果の分析とパターンの発見

以下を探す:
- 急激な離脱(例:3日目の大きなチャーン)
- 異常に高い/低いリテンションのコホート
- 製品変更やキャンペーンの影響

質問:
- 高リテンションコホートで何が異なっていたか?
- 機能ローンチはより良いリテンションと相関していたか?
- 行動やチャネルはより良い結果と関連しているか?

### 6. アクションを取り、反復する

- 仮説を形成(例:「オンボーディングを完了したユーザーはより長く保持される」)
- 変更をテスト(オンボーディングの改善、粘着性のある機能の促進)
- コホート分析を再実行して結果を測定
- サイクルを繰り返す;コホート分析は継続的なプロセス

**参考文献:**  
- [Mixpanel: How to Conduct Cohort Analysis](https://mixpanel.com/blog/cohort-analysis/)
- [Corporate Finance Institute: How To Conduct Cohort Analysis](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/)

## 使用例

### SaaSオンボーディング最適化

SaaS企業は、3日以内にオンボーディングを完了したユーザーが30日目に2倍のリテンション率を持つことをよく発見します。オンボーディングを改善し、新しいコホートのリテンションを追跡することで、変更が機能するかを検証します。

### Eコマースキャンペーン分析

Eコマース企業は、獲得チャネル別にコホートを比較します。メールキャンペーンコホートは、ディスプレイ広告コホートよりも高いリピート購入率を持つ可能性があり、予算配分の指針となります。

### 機能採用の影響

新しい「チェックリスト」機能を試したユーザーがライフタイムバリューが2倍の場合、チームはこの機能をより積極的に促進できます。

### チャーンリスク検出

7日間ログインしていないユーザーのコホートを特定することで、ターゲットを絞った再エンゲージメントが可能になり、その再アクティベーションをコホートとして追跡できます。

**参考文献:**  
- [Mixpanel: Cohort Analysis Examples](https://mixpanel.com/blog/cohort-analysis/)
- [Appcues: Cohort Analysis Use Cases](https://www.appcues.com/blog/cohort-analysis)

## 実践におけるコホート分析:視覚化

### コホートリテンションテーブル(視覚的説明)

- **行:** 週次登録コホート
- **列:** 登録からの日数(1日目、7日目、14日目、30日目)
- **セル値:** 各日にアクティブなコホートの%
- **色分け:** 高リテンションは緑、低リテンションは赤

### 行動コホート比較グラフ(視覚的説明)

- **X軸:** 登録からの日数
- **Y軸:** リテンション率(%)
- **線:** 「機能採用者」vs「非採用者」

これらの視覚化により、トレンドと外れ値を簡単に発見できます。

## ベストプラクティス、制限事項、よくある落とし穴

### ベストプラクティス

- **明確な目的から始める:** ビジネス上の質問を把握。
- **実行可能なコホートを選択:** 影響を与えられる特性や行動に焦点を当てる。
- **獲得コホートと行動コホートを組み合わせる:** いつ、なぜチャーンが発生するかの両方を確認。
- **データを視覚化:** テーブル、ヒートマップ、グラフを使用。
- **発見に基づいて行動:** 製品とマーケティングの改善を推進。

### よくある落とし穴

- **コホートが広すぎる/狭すぎる:** 広すぎる=無意味、狭すぎる=信頼性が低い。
- **相関と因果関係の混同:** 機能はリテンションと相関する可能性があるが、それを引き起こすとは限らない。
- **外部要因の無視:** 季節性、技術的問題、競争が結果に影響を与える可能性。
- **虚栄の指標:** リテンションとエンゲージメントは単純なログインよりも意味がある。

### 制限事項

- **データ量:** 小規模なユーザーベースは分析の信頼性を低下させる。
- **ツールの制約:** 一部のツール(例:Google Analytics)は基本的なコホート化のみを許可。
- **複雑さ:** 多次元コホート分析は解釈が難しい場合がある。

**参考文献:**  
- [Mixpanel: Cohort Analysis Limitations](https://mixpanel.com/blog/cohort-analysis/)
- [Appcues: Cohort Analysis Pitfalls](https://www.appcues.com/blog/cohort-analysis)

## コホート分析と類似概念の比較

| 概念              | 機能                                    | 主な違い                                    |
|------------------|----------------------------------------|-------------------------------------------|
| コホート分析      | ユーザーグループを時系列で追跡           | 時間ベースまたは行動変化に焦点              |
| セグメンテーション | 現在の特性や行動でグループ化             | 時点のスナップショット、縦断的ではない       |
| チャーン分析      | ユーザーが離脱する理由を調査             | コホート分析を手法として使用                |
| RFM分析          | 最新性、頻度、価値でセグメント化         | トランザクションベース、時間ベースの進化ではない |

**参考文献:**  
- [Mixpanel: Segmentation vs Cohort Analysis](https://mixpanel.com/blog/user-segmentation-guide-understanding-customers-2/)
- [Corporate Finance Institute: Cohort Analysis](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/)

## ツールとリソース

### コホート分析の主要ツール

- **Mixpanel:** 高度なコホート作成(獲得、行動、複数基準)、リテンション/頻度レポート、メッセージングツールとの統合。  
  [Mixpanel Cohort Analysis Guide](https://mixpanel.com/blog/cohort-analysis/)
- **Google Analytics:** 基本的なコホートレポート(獲得のみ)、柔軟性が限定的。
- **Userpilot:** コホート分析に加えて、アプリ内メッセージングとオンボーディングツール。  
  [Userpilot Cohort Analysis Guide](https://userpilot.com/blog/cohort-analysis/)
- **Amplitude、Indicative:** 高度な製品分析、柔軟なコホート化、視覚化。
- **スプレッドシート(Excel、Google Sheets):** プロトタイピングまたは小規模データセット用の手動コホートテーブル。
  [ProfitWell Cohort Analysis Template](https://docs.google.com/spreadsheets/d/1cHgCk1WeegbQ96yAmhLL1U3VWWkwQEwY50-UJLuM-sc/edit#gid=1491702461)

### チュートリアル

- [Mixpanel Cohort Analysis YouTube Tutorial](https://www.youtube.com/watch?v=kbjkUeu8v3M)
- [Mixpanel Cohort Templates Video](https://www.youtube.com/watch?v=hBZn3a8RSMw)
- [Corporate Finance Institute Cohort Analysis Guide](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/)
- [Appcues Beginner's Guide to Cohort Analysis](https://www.appcues.com/blog/cohort-analysis)

## 用語集:関連キーワードと概念

| 用語                        | 定義/文脈                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------|
| 獲得コホート分析            | 最初に登録または獲得された時期でユーザーをグループ化。                                                  |
| 行動コホート分析            | 共有されたアクションや行動(例:機能の使用、オンボーディング完了)でグループ化。                           |
| リテンション率              | 一定期間後もアクティブなコホートの割合。                                                               |
| チャーン率                  | 一定期間後に離脱したコホートの割合。                                                                   |
| 顧客ライフタイムバリュー(LTV) | 顧客が製品を使用する期間中にもたらす予測価値。                                                         |
| セグメンテーション          | スナップショット分析のためにユーザーをグループに分割—必ずしも時間ベースではない。                        |
| 共通特性                    | コホートを定義するために使用される特性(時間、アクション、場所、プランなど)。                            |
| 期間                        | コホート開始後の間隔(日、週、月)。                                                                     |
| コホート分析の実施/実行      | ビジネス上の質問に答えるためにコホートを定義、構築、分析するプロセス。                                  |
| リテンションの改善/チャーンの削減 | コホート分析がサポートする主なビジネス目標。                                                       |
| プロダクトチーム            | コホート分析の典型的なユーザー—プロダクトマネージャー、マーケター、分析専門家。                         |

## さらなる読書とリソース

- [Mixpanel Ultimate Guide to Cohort Analysis](https://mixpanel.com/blog/cohort-analysis/)
- [CleverTap Cohort Analysis Guide](https://clevertap.com/blog/cohort-analysis/)
- [Userpilot Cohort Analysis Guide](https://userpilot.com/blog/cohort-analysis/)
- [mParticle Cohort Analysis Article](https://www.mparticle.com/blog/what-is-cohort-analysis-a-guide-to-increasing-customer-retention/)
- [Optimizely Cohort Analysis Glossary](https://www.optimizely.com/optimization-glossary/cohort-analysis/)
- [Appcues Beginner's Guide to Cohort Analysis](https://www.appcues.com/blog/cohort-analysis)
- [Corporate Finance Institute Cohort Analysis](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/)
- [YouTube: Mixpanel Cohorts Tutorial](https://www.youtube.com/watch?v=kbjkUeu8v3M)
- [YouTube: Mixpanel Cohort Templates](https://www.youtube.com/watch?v=hBZn3a8RSMw)

## クイックチェックリスト:コホート分析の開始

- [ ] ビジネス上の質問または仮説を定義
- [ ] 適切な指標を選択(リテンション、チャーンなど)
- [ ] 意味のあるコホート基準を選択(獲得、行動など)
- [ ] コホートテーブルまたはチャートを構築(必要に応じてテンプレート/ツールから始める)
- [ ] パターンを分析(離脱、外れ値、トレンドを探す)
- [ ] 発見に基づいて仮説を開発しテスト
- [ ] 反復して繰り返す—コホート分析は継続的なプロセス

**さらなる研究と実装のための参考文献:**
- [Mixpanel: Ultimate Guide to Cohort Analysis](https://mixpanel.com/blog/cohort-analysis/)
- [Corporate Finance Institute: Cohort Analysis](https://corporatefinanceinstitute.com/resources/business-intelligence/cohort-analysis/)
- [Appcues: Cohort Analysis](https://www.appcues.com/blog/cohort-analysis)
- [Userpilot: Cohort Analysis](https://userpilot.com/blog/cohort-analysis/)
- [ProfitWell: Cohort Analysis Spreadsheet Template](https://docs.google.com/spreadsheets/d/1cHgCk1WeegbQ96yAmhLL1U3VWWkwQEwY50-UJLuM-sc/edit#gid=1491702461)
- [YouTube: Mixpanel Cohorts Tutorial](https://www.youtube.com/watch?v=kbjkUeu8v3M)