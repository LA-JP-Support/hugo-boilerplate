---
title: スポットインスタンス
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: spot-instances
description: スポットインスタンスは、AWS、Azure、GCPが提供する割引価格のクラウドコンピューティングリソースで、バッチ処理、分析、機械学習トレーニングなどの耐障害性ワークロードに最適です。
keywords:
- スポットインスタンス
- クラウドコンピューティング
- AWS
- Azure
- GCP
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Spot Instances
term: すぽっといんすたんす
url: "/ja/glossary/Spot-Instances/"
---
## スポットインスタンスとは?

スポットインスタンスは、クラウドコンピューティングにおける購入モデルで、ユーザーは余剰キャパシティにアクセスし、オンデマンド価格と比較して最大90%の割引を受けることができます。主要なクラウドプロバイダーは、それぞれ異なる機能と価格メカニズムを持つスポットインスタンスプログラムを提供しています。

<strong>Amazon Web Services (AWS) スポットインスタンス:</strong>ユーザーは最大価格を指定し、市場価格がこの閾値を下回る場合にインスタンスを受け取ります。キャパシティが必要になった場合、または価格が最大入札額を超えた場合、2分前の通知でスポットインスタンスは回収されます。

<strong>Microsoft Azure スポット仮想マシン (VM):</strong>ユーザーは最大価格を設定し、市場価格がこの制限を超えるとVMは削除されます。Azureは30秒前の削除通知を提供します。

<strong>Google Cloud スポットVM:</strong>同様の割引を提供し、固定的かつ大幅な節約が可能です。価格は最大1ヶ月間安定しています。Googleは30秒前のプリエンプション通知を提供します。

スポットインスタンスは、柔軟で耐障害性のあるアプリケーションに最適です。プロバイダーは短時間の通知でこれらのインスタンスを回収できるため、中断への耐性が重要な要件となります。

## スポットインスタンスの仕組み

### 価格メカニズム

<strong>動的な需給主導型:</strong>各インスタンスタイプとリージョンのスポット価格は、リアルタイム入札ではなく、需給の長期的なトレンドに基づいて変動します。

<strong>最大価格:</strong>ユーザーは支払い意思のある最大価格を設定できます。現在のスポット価格がこれを下回る限り、インスタンスは実行されます。

<strong>リアルタイム入札なし(現代のモデル):</strong>初期のシステムではライブ入札が行われていましたが、現在ほとんどのプロバイダーは簡素化のために最大価格設定モデルを使用しています。

<strong>課金粒度:</strong>AWS、Azure、GCPは、1分間の最小値の後、秒単位で課金します。

<strong>例:</strong>AWSでは、`m5.large`オンデマンドインスタンスのコストは$0.096/時間ですが、スポット価格は$0.019/時間まで低くなる可能性があります(80%以上の節約)。

### 可用性と中断

<strong>キャパシティプール:</strong>各スポットインスタンスは、インスタンスタイプとアベイラビリティゾーンで定義されたプールから提供されます。

<strong>中断ポリシー:</strong>プロバイダーは、キャパシティが必要な場合、またはスポット価格が最大入札額を超えた場合、短時間の通知(AWSでは2分、AzureとGCPでは30秒)でインスタンスを終了または割り当て解除する場合があります。

<strong>中断通知:</strong>- AWS: 2分前の警告
- Azure: 30秒前の通知
- GCP: 30秒前の通知

<strong>リバランシング:</strong>AWSは「リバランス推奨」を提供し、スポットインスタンスが中断リスクが高まっていることを早期に警告します。

<strong>重要なポイント:</strong>アプリケーションは中断を処理できるように設計する必要があります。ステートレス性、チェックポイント、自動復旧が不可欠です。

## 比較:スポット vs オンデマンド vs リザーブド

| 機能 | スポットインスタンス | オンデマンドインスタンス | リザーブドインスタンス |
|---------|----------------|---------------------|-------------------|
| <strong>価格</strong>| 変動、最大90%割引 | 固定、最高価格 | 割引(最大72%)、固定 |
| <strong>可用性</strong>| 余剰キャパシティがある場合のみ | 常に利用可能 | 予約期間中は保証 |
| <strong>中断</strong>| 中断される可能性あり(2分または30秒前通知) | ユーザーが終了時期を決定 | 期間中は中断されない |
| <strong>コミットメント</strong>| コミットメントなし | コミットメントなし | 1年または3年必要 |
| <strong>ユースケース</strong>| 柔軟、耐障害性、非クリティカル | すべてのワークロード、特にクリティカル | 予測可能、定常状態 |
| <strong>SLA</strong>| SLAなし | 標準SLA | 標準SLA |
| <strong>課金</strong>| 秒単位(最初の1分後) | 秒単位 | 秒単位 |

## クラウドプロバイダー間の比較

| 機能 | AWSスポット | GCPスポットVM | Azureスポット VM |
|---------|----------|--------------|----------------|
| <strong>価格モデル</strong>| 変動、需給主導型 | 固定割引(最大91%オフ) | 変動、需給主導型 |
| <strong>使用時間制限</strong>| 固定制限なし | 最大24時間 | 固定制限なし |
| <strong>中断通知</strong>| 2分 | 30秒 | 30秒 |
| <strong>課金</strong>| 秒単位(1分後) | 秒単位 | 秒単位 |
| <strong>SLA</strong>| SLAなし | SLAなし | SLAなし |
| <strong>統合ツール</strong>| Spot Fleet、ASG、Kubernetes | MIG、GKE | VM Scale Sets、AKS |
| <strong>最適なユースケース</strong>| バッチ、CI/CD、ML、HPC、ステートレス | バッチ、分析、開発/テスト | バッチ、ステートレスアプリ、CI/CD |
| <strong>独自機能</strong>| スポットブロック(固定期間中断) | 継続使用割引 | 削除ポリシーのカスタマイズ |

## コアコンセプト

### スポットキャパシティプール

同じアベイラビリティゾーン内の同じインスタンスタイプの未使用仮想マシンのグループ。各プールは独立して動作し、キャパシティ/価格はプール間で異なる場合があります。

### スポットインスタンスリクエスト

ユーザーが開始するスポットインスタンスの割り当てリクエスト:
- <strong>ワンタイム:</strong>キャパシティが利用可能な場合に一度だけプロビジョニング
- <strong>永続的:</strong>中断された場合に自動的に再送信(最終的に完了する必要があるジョブに有用)

### リバランス推奨(AWS)

AWSは、スポットインスタンスが終了リスクが高まっている場合、標準の中断通知の前にリバランス推奨を発行し、ワークロードを事前に移行またはチェックポイントできるようにします。

## ユースケースと例

### 理想的なユースケース

<strong>バッチ処理:</strong>データ分析、ビデオトランスコーディング、レンダリング、ETLジョブ  
*例:* 研究者が気候データのモンテカルロシミュレーションを実行し、コンピューティングコストを80%以上節約。

<strong>ビッグデータ分析:</strong>Hadoop/Sparkクラスター、大規模なログ/データ分析  
*例:* メディア企業がAWS EMRでスポットインスタンスを使用して、毎晩ペタバイト規模のログを処理。

<strong>CI/CDパイプライン:</strong>短期間のビルドおよびテスト環境  
*例:* SaaSプロバイダーがJenkinsビルドエージェントとしてスポットインスタンスを使用し、コスト効率の高い並列CIを実現。

<strong>機械学習トレーニング:</strong>ディープラーニング、ハイパーパラメータチューニング、GPUでのチェックポイント付きトレーニング  
*例:* チームがスポットGPUインスタンスでニューラルネットワークをトレーニングし、中断復旧のための自動保存を使用。

<strong>コンテナとマイクロサービス:</strong>KubernetesまたはDocker Swarmによってオーケストレーションされるステートレスサービス

<strong>開発/テスト環境:</strong>中断が許容される非本番ワークロード

<strong>ハイパフォーマンスコンピューティング(HPC):</strong>ゲノムシーケンシング、金融モデリング、科学シミュレーション

### 非理想的なユースケース

<strong>ミッションクリティカルなアプリケーション:</strong>高可用性と最小限のダウンタイムが最優先される場合

<strong>耐性のないステートフルアプリ:</strong>状態をチェックポイントできない、または突然の終了から回復できないアプリ

## リスクと軽減戦略

### 主要なリスク

<strong>中断リスク:</strong>インスタンスは最短30秒前の通知で終了される可能性があります

<strong>キャパシティの変動性:</strong>スポットキャパシティは予測不可能に消失する可能性があります

<strong>価格変動:</strong>スポット価格は、特に人気のあるインスタンスタイプで急騰する可能性があります

<strong>SLAなし:</strong>プロバイダーは稼働時間や可用性を保証しません

### 軽減戦略

<strong>自動化:</strong>- オーケストレーションシステム(Kubernetes、AWS Auto Scaling)を使用して、中断されたワークロードを再スケジュールおよび置換
- 耐性のためにスポットをオンデマンドおよびリザーブドインスタンスと組み合わせる
- ライフサイクルとフォールバックを管理する自動化プラットフォームを採用

<strong>アプリケーション設計:</strong>- サービスをステートレスとして設計し、外部ストレージを活用
- 中断後にジョブを再開するためのチェックポイントを実装
- ノード障害に耐えるために疎結合を使用

<strong>プロアクティブな監視:</strong>- AWS Spot Instance Advisorなどのツールを使用して、リージョン/タイプ別の中断率を監視
- リバランス推奨に基づいて早期にワークロードを移行

<strong>多様化:</strong>- 「群れ」中断を避けるために、インスタンスタイプとリージョンの組み合わせを使用
- 突然の削除リスクを減らすために適切な最大入札額を設定

## ベストプラクティス

<strong>1. 非クリティカルなワークロードから開始</strong>クリティカルなワークロードを移行する前に、中断処理戦略を検証します。

<strong>2. 多様化</strong>信頼性を高めるために、複数のインスタンスタイプとアベイラビリティゾーンを使用します。

<strong>3. 自動化</strong>AWS Spot Fleet、Auto Scaling Groups、またはKubernetesオートスケーラーを採用します。

<strong>4. トレンドを監視</strong>AWS Spot Price HistoryとSpot Instance Advisorを使用します。

<strong>5. 最大価格を設定</strong>入札額をオンデマンド価格以下に制限します。

<strong>6. 中断を計画</strong>高速復旧とデータ損失ゼロのために設計します。

<strong>7. サードパーティツールを活用</strong>最適化と自動化のためにCast AIまたはCloudZeroを試します。

<strong>8. タグを使用</strong>チーム/プロジェクト別に使用状況と節約を追跡します。

<strong>9. 定期的にレビュー</strong>使用状況レポートに基づいて組み合わせと戦略を更新します。

## 課金と価格

<strong>スポット価格:</strong>プロバイダーが設定し、市場の需要と供給に応じて変動

<strong>課金粒度:</strong>最初の1分後、秒単位(AWS、Azure、GCP)

<strong>終了課金:</strong>一般的に、AWSが中断した場合、最後の部分時間は課金されません。ユーザーが終了した場合、使用した秒数分が課金されます。

<strong>節約の追跡:</strong>プロバイダーダッシュボード、AWS Spot Fleet節約レポート、またはサードパーティツールを使用

<strong>Savings Plansとの重複なし:</strong>スポット使用はAWS Savings Plansのコミットメントには貢献しません

## シナリオ例

<strong>シミュレーションを実行する研究チーム</strong>大学の研究グループは、気候モデリングのために数千のモンテカルロシミュレーションを実行する必要があります。Kubernetesによってオーケストレーションされたスポットインスタンスを使用することで、オンデマンド価格と比較してコンピューティングコストを85%削減しました。チェックポイントは中断前に永続ストレージに保存されるため、ジョブは損失なく再開されます。

## よくある質問

<strong>Q: 本番ワークロードにスポットインスタンスを使用できますか?</strong>A: はい、アプリケーションが中断に対して耐性がある場合は可能です。多くの組織は、クリティカルなワークロードのためにスポットをオンデマンドまたはリザーブドインスタンスと組み合わせています。

<strong>Q: スポットインスタンスでどれくらい節約できますか?</strong>A: 通常、リージョン、タイプ、需要に応じて、オンデマンドと比較して70〜90%節約できます。

<strong>Q: スポットインスタンスが中断されるとどうなりますか?</strong>A: 短い中断通知(AWSでは2分、Azure/GCPでは30秒)を受け取ります。その後、インスタンスは終了、停止、または休止状態になります。

<strong>Q: スポットインスタンスをリクエストするにはどうすればよいですか?</strong>A: クラウドプロバイダーのコンソール、CLI、またはAPIを使用します。必要に応じてインスタンスタイプ、最大価格、期間を指定します。

<strong>Q: スポットインスタンスはKubernetesで使用できますか?</strong>A: はい、Kubernetesなどのコンテナオーケストレーターは、スポットインスタンスが中断されたときにポッドを再スケジュールできます。

<strong>Q: スポットインスタンスにSLAはありますか?</strong>A: いいえ。プロバイダーはスポットインスタンスの稼働時間や可用性を保証しません。

## 参考文献


1. Amazon Web Services (AWS). (n.d.). AWS Spot Instances Documentation. AWS EC2 User Guide.
2. Amazon Web Services (AWS). (n.d.). AWS EC2 Spot Pricing. AWS Pricing.
3. Amazon Web Services (AWS). (n.d.). AWS Spot Interruptions. AWS EC2 User Guide.
4. Amazon Web Services (AWS). (n.d.). AWS Instance Rebalance Recommendations. AWS EC2 User Guide.
5. Amazon Web Services (AWS). (n.d.). AWS Spot Use Cases. AWS Website.
6. Amazon Web Services (AWS). (n.d.). AWS Spot HPC Use Case. AWS Website.
7. Amazon Web Services (AWS). (n.d.). AWS Billing & Purchasing Options. AWS EC2 User Guide.
8. Amazon Web Services (AWS). (n.d.). AWS Spot Price History. AWS EC2 User Guide.
9. Amazon Web Services (AWS). (n.d.). AWS Spot Instance Advisor. AWS Website.
10. Amazon Web Services (AWS). (n.d.). AWS EC2 Spot Fleet. AWS EC2 User Guide.
11. Amazon Web Services (AWS). (n.d.). AWS Spot Requests. AWS EC2 User Guide.
12. Amazon Web Services (AWS). (n.d.). AWS Spot Savings. AWS EC2 User Guide.
13. Amazon Web Services (AWS). (n.d.). AWS Billing for Interrupted Spot Instances. AWS EC2 User Guide.
14. Amazon Web Services (AWS). (n.d.). AWS Spot Best Practices. AWS Compute Blog.
15. Amazon Web Services (AWS). (n.d.). AWS Spot FAQ. AWS Website.
16. Google Cloud. (n.d.). Google Cloud Spot VMs. Google Cloud Documentation.
17. Google Cloud. (n.d.). Google Cloud Spot Preemption. Google Cloud Documentation.
18. Google Cloud. (n.d.). Google Cloud Pricing. Google Cloud Website.
19. Microsoft. (n.d.). Azure Spot Virtual Machines. Microsoft Learn.
20. Microsoft. (n.d.). Azure Spot Pricing. Azure Website.
21. Spot.io. (n.d.). Azure Spot VMs Guide. Spot.io Resources.
22. Spot.io. (n.d.). Spot vs On-Demand. Spot.io Resources.
23. Spot.io. (n.d.). Provider Comparison. Spot.io Resources.
24. Spot.io. (n.d.). Suitable Use Cases. Spot.io Resources.
25. Spot.io. (n.d.). Risks & Strategies. Spot.io Resources.
26. Spot.io. (n.d.). Ultimate Guide. Spot.io Resources.
27. Spot.io. (n.d.). Spot.io Eco. Spot.io Products.
28. CloudZero. (n.d.). Spot Instances Guide. CloudZero Blog.
29. Infracost. (n.d.). Spot Instances Glossary. Infracost Website.
30. Cast AI. (n.d.). Spot Guide. Cast AI Blog.
31. Milvus. (n.d.). AI Quick Reference: Spot Instances. Milvus AI Reference.
