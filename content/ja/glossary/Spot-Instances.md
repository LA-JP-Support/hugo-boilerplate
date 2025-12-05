---
title: スポットインスタンス
date: 2025-11-25
translationKey: spot-instances
description: スポットインスタンスは、AWS、Azure、GCPが提供する割引価格のクラウドコンピューティングリソースで、バッチ処理、分析、機械学習トレーニングなどの耐障害性ワークロードに最適です。
keywords: ["スポットインスタンス", "クラウドコンピューティング", "AWS", "Azure", "GCP"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Spot Instances
term: すぽっといんすたんす
reading: スポットインスタンス
kana_head: か
---
## スポットインスタンスとは?

スポットインスタンスは、ユーザーが余剰リソースに**最大90%割引**でアクセスできるクラウドコンピューティングの購入モデルです。主要プロバイダーには以下が含まれます:

- **Amazon Web Services (AWS) スポットインスタンス:** ユーザーが最大価格を指定し、市場価格がこの閾値を下回る場合にインスタンスを受け取ります。[AWS スポットインスタンスドキュメント](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- **Microsoft Azure スポット仮想マシン (VM):** ユーザーが最大価格を設定し、市場価格がこれを超えるとVMが削除されます。[Azure スポットVMガイド](https://spot.io/resources/azure-pricing/the-complete-guide/what-are-azure-spot-virtual-machines/)
- **Google Cloud スポットVM:** 同様の割引を提供し、固定的かつ大幅な節約が可能で、価格は最大1ヶ月間安定しています。[Google Cloud スポットVM](https://cloud.google.com/compute/docs/instances/spot)

スポットインスタンスは**柔軟で障害耐性のあるアプリケーション**に最適です。プロバイダーは短時間の通知でこれらのインスタンスを回収できるため、中断への耐性が重要な要件となります。  

## スポットインスタンスの仕組み

### 価格メカニズム

- **動的な需給駆動型:** 各インスタンスタイプとリージョンのスポット価格は、リアルタイム入札ではなく、需給の長期的なトレンドに基づいて変動します。[AWS 価格設定](https://aws.amazon.com/ec2/spot/pricing/)
- **最大価格:** ユーザーは支払い意思のある最大価格を設定できます。現在のスポット価格がこれを下回る限り、インスタンスは実行されます。
- **リアルタイム入札なし(現代モデル):** 初期のシステムではライブ入札が行われていましたが、現在ほとんどのプロバイダーは簡素化のため最大価格設定モデルを使用しています。ユーザーはもはやリアルタイムオークションで競争しません。[Spot.io: スポット vs オンデマンド](https://spot.io/resources/spot-instances/spot-instances-vs-on-demand-instances-pros-and-cons/)
- **課金粒度:** AWS、Azure、GCPは1分間の最小値の後、秒単位で課金します。[Google Cloud 価格設定](https://cloud.google.com/compute/pricing)

> **例:** AWSでは、`m5.large` オンデマンドインスタンスのコストは$0.096/時間ですが、スポット価格は$0.019/時間まで低下する可能性があります(80%以上の節約)。  
> [AWS スポット価格設定](https://aws.amazon.com/ec2/spot/pricing/)を参照

### 可用性と中断

- **キャパシティプール:** 各スポットインスタンスは、インスタンスタイプとアベイラビリティゾーンで定義されたプールから提供されます。
- **中断ポリシー:** プロバイダーは、容量が必要な場合やスポット価格が最大入札額を超えた場合、短時間の通知(AWSでは2分、AzureとGCPでは30秒)でインスタンスを終了または割り当て解除することがあります。
- **中断通知:** AWSは2分間の警告を送信し、AzureとGCPは30秒の通知を提供します。
  - [AWS スポット中断](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
  - [Azure スポットVM](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
  - [GCP スポットVM](https://cloud.google.com/compute/docs/instances/spot#preemption)
- **リバランシング:** AWSは「リバランス推奨」を提供し、スポットインスタンスが中断リスクの高い状態にあることを早期に警告します。
  - [AWS リバランス推奨](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)
  
> **重要ポイント:** アプリケーションは中断を処理できるように設計**する必要があります**—ステートレス性、チェックポイント、自動復旧が不可欠です。

## スポットインスタンス vs オンデマンド vs リザーブドインスタンス

| 機能                    | **スポットインスタンス**                                             | **オンデマンドインスタンス**                           | **リザーブドインスタンス**                       |
|----------------------------|---------------------------------------------------------------|---------------------------------------------------|----------------------------------------------|
| **価格設定**                | 変動、オンデマンドより最大90%安い                      | 固定、最高価格                              | 割引(最大72%)、固定                |
| **可用性**           | 余剰容量がある場合のみ                                 | 常に利用可能(容量がある場合)             | 予約期間中は保証          |
| **中断**          | いつでも中断される可能性(2分または30秒の通知)       | ユーザーが終了を決定                     | 期間中は中断されない                   |
| **コミットメント**             | コミットメントなし                                                 | コミットメントなし                                     | 1年または3年(コミットメント必須)            |
| **ユースケース**              | 柔軟、障害耐性、非クリティカル                        | すべてのワークロード、特にクリティカル                 | 予測可能、定常状態のワークロード           |
| **SLA**                    | SLAなし                                                        | 標準SLA                                      | 標準SLA                                 |
| **課金粒度**    | 秒単位(最初の1分後)                                 | 秒単位                                        | 秒単位                                   |

- **参考資料:** [AWS 課金と購入オプション](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

## クラウドプロバイダー間の比較

| 機能                 | **AWS スポットインスタンス**                  | **GCP スポットVM**                     | **Azure スポットVM**                 |
|-------------------------|-----------------------------------------|--------------------------------------|------------------------------------|
| **価格モデル**       | 変動、需給駆動型          | 固定割引(最大91%オフ)       | 変動、需給駆動型     |
| **使用時間制限**    | 固定制限なし                          | 最大24時間                         | 固定制限なし                     |
| **中断通知** | 2分                               | 30秒                           | 30秒                         |
| **課金**             | 秒単位(1分後)                | 秒単位                           | 秒単位                         |
| **SLA**                 | SLAなし                                  | SLAなし                               | SLAなし                             |
| **統合ツール**   | Spot Fleet、ASG、Kubernetes             | MIG、GKE                             | VM Scale Sets、AKS                 |
| **最適なユースケース**      | バッチ、CI/CD、ML、HPC、ステートレスアプリ   | バッチ、分析、開発/テスト           | バッチ、ステートレスアプリ、CI/CD       |
| **独自機能**     | スポットブロック(固定期間中断)    | 継続使用割引              | 削除ポリシーのカスタマイズ      |

- [Spot.io プロバイダー比較](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)

## 主要概念

### スポットキャパシティプール

同じアベイラビリティゾーン内の同じインスタンスタイプの未使用仮想マシンのグループ。各プールは独立して動作し、容量/価格はプール間で異なる場合があります。[AWS スポットプール](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

### スポットインスタンスリクエスト

スポットインスタンスを割り当てるためのユーザー開始リクエスト。リクエストは以下のいずれかです:
- **ワンタイム:** 容量がある場合に一度だけプロビジョニング。
- **永続的:** 中断された場合に自動的に再送信(最終的に完了する必要があるジョブに有用)。

### リバランス推奨(AWS)

AWSは、スポットインスタンスが終了リスクの高い状態にある場合、標準の中断通知の前にリバランス推奨を発行し、ワークロードが事前に移行またはチェックポイントできるようにします。[AWS インスタンスリバランス推奨](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)

## ユースケースと実用例

スポットインスタンスは、**中断が管理可能**でコストを最小化する必要があるシナリオで優れています。主なユースケースには以下が含まれます:

### 理想的なユースケース

- **バッチ処理:** データ分析、動画トランスコーディング、レンダリング、ETLジョブ。
  - *例:* 気候データのモンテカルロシミュレーションを実行する研究者が、コンピューティングコストを80%以上節約。
- **ビッグデータ分析:** Hadoop/Sparkクラスター、大規模なログ/データ分析。
  - *例:* メディア企業がAWS EMRでスポットインスタンスを使用して、毎晩ペタバイト規模のログを処理。
- **CI/CDパイプライン:** 短命なビルドおよびテスト環境。
  - *例:* SaaSプロバイダーがスポットインスタンスをJenkinsビルドエージェントとして使用し、コスト効率の高い並列CIを実現。
- **機械学習トレーニング:** ディープラーニング、ハイパーパラメータチューニング、GPUでのチェックポイント付きトレーニング。
  - *例:* スポットGPUインスタンスでニューラルネットワークをトレーニングし、中断復旧のために自動保存を使用するチーム。
- **コンテナとマイクロサービス:** KubernetesまたはDocker Swarmによってオーケストレーションされるステートレスサービス。
- **開発/テスト環境:** 中断が許容される非本番ワークロード。
- **ハイパフォーマンスコンピューティング(HPC):** ゲノム配列決定、金融モデリング、科学シミュレーション。

- [AWS スポットユースケース](https://aws.amazon.com/ec2/spot/use-cases/)

### 非理想的なユースケース

- **ミッションクリティカルなアプリケーション:** 高可用性と最小限のダウンタイムが最優先される場合。
- **耐性のないステートフルアプリ:** 状態をチェックポイントできない、または突然の終了から復旧できないアプリ。

- [Spot.io: 適切なユースケース](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Suitable-Use-Cases-for-Spot-Instances)

## リスク、課題、および緩和戦略

### 主要なリスク

- **中断リスク:** インスタンスは最短30秒の通知で終了または割り当て解除される可能性があります。
- **容量の変動性:** スポット容量は、リージョン、タイプ、市場需要に応じて予測不可能に消失する可能性があります。
- **価格変動:** スポット価格は、特に混雑時の人気インスタンスタイプで急騰する可能性があります。
- **SLAなし:** プロバイダーはスポットインスタンスの稼働時間や可用性を保証しません。

- [AWS スポット中断](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [Spot.io: リスクと戦略](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/#Strategies-to-Optimize-the-Use-of-Spot-Instances)

### 緩和戦略

- **自動化:**
  - オーケストレーションシステム(例: Kubernetes、AWS Auto Scaling)を使用して、中断されたワークロードを再スケジュールおよび置換。
  - 耐性のためにスポットをオンデマンドおよびリザーブドインスタンスと組み合わせる。
  - ライフサイクルとフォールバックを管理する自動化プラットフォーム(例: [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)、[Spot.io](https://spot.io/products/eco/))を採用。
- **アプリケーション設計:**
  - サービスをステートレスとして設計し、外部ストレージを活用。
  - 中断後にジョブを再開するためのチェックポイントを実装。
  - ノード障害に耐えるための疎結合を使用。
- **プロアクティブな監視:**
  - [AWS スポットインスタンスアドバイザー](https://aws.amazon.com/ec2/spot/instance-advisor/)などのツールを使用して、リージョン/タイプ別の中断率を監視。
  - [リバランス推奨](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#instance-rebalance-recommendations)に基づいてワークロードを早期に移行。
- **多様化:**
  - 「群れ」中断を避けるために、インスタンスタイプとリージョンの組み合わせを使用。
  - 突然の削除リスクを減らすために、適切な最大入札額を設定。

- [Cast AI スポットガイド](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

## スポットインスタンス使用のベストプラクティス

1. **非クリティカルなワークロードから開始:** 中断処理戦略を検証。
2. **多様化:** より高い信頼性のために、複数のインスタンスタイプとアベイラビリティゾーンを使用。
3. **自動化:** [AWS Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)、Auto Scaling Groups、またはKubernetesオートスケーラーを採用。
4. **トレンドを監視:** [AWS スポット価格履歴](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html)と[スポットインスタンスアドバイザー](https://aws.amazon.com/ec2/spot/instance-advisor/)を使用。
5. **最大価格を設定:** オンデマンド価格以下で入札額を上限設定。
6. **中断に備える:** 高速復旧とデータ損失ゼロのために設計。
7. **サードパーティツールを活用:** 最適化と自動化のために[Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)または[CloudZero](https://www.cloudzero.com/blog/spot-instances/)を試す。
8. **タグを使用:** チーム/プロジェクト別に使用状況と節約を追跡。
9. **定期的にレビュー:** 使用状況レポートに基づいて組み合わせと戦略を更新。

- [AWS スポットベストプラクティス](https://aws.amazon.com/blogs/compute/best-practices-to-optimize-your-amazon-ec2-spot-instances-usage/)
- [CloudZero スポットガイド](https://www.cloudzero.com/blog/spot-instances/)

## 課金と価格設定の詳細

- **スポット価格:** プロバイダーによって設定され、市場の需給で変動。
- **課金粒度:** 最初の1分後に秒単位(AWS、Azure、GCP)。
- **終了課金:** 一般的に、AWSが中断した場合、最後の部分時間は課金されません。ユーザーが終了した場合、使用秒数分を支払います。[AWS 課金詳細](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html)
- **節約追跡:** プロバイダーダッシュボード、[AWS Spot Fleet節約レポート](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)、またはサードパーティツール(例: [Cast AI](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)、[Infracost](https://www.infracost.io/glossary/spot-instances/))を使用。
- **Savings Plansとの重複なし:** スポット使用はAWS Savings Plansのコミットメントには貢献しません。

- [AWS EC2 スポット価格設定](https://aws.amazon.com/ec2/spot/pricing/)
- [GCP スポット価格設定](https://cloud.google.com/compute/pricing)
- [Azure スポット価格設定](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/spot/)

## シナリオ例

**シミュレーションを実行する研究チーム**

ある大学の研究グループは、気候モデリングのために数千のモンテカルロシミュレーションを実行する必要があります。Kubernetesによってオーケストレーションされたスポットインスタンスを使用することで、オンデマンド価格と比較してコンピューティングコストを85%削減しました。チェックポイントは中断前に永続ストレージに保存されるため、ジョブは損失なく再開されます。

- [AWS スポットHPCユースケース](https://aws.amazon.com/ec2/spot/use-cases/hpc/)
- [Milvus AI クイックリファレンス: スポットインスタンス](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)

## よくある質問(FAQ)

**Q: 本番ワークロードにスポットインスタンスを使用できますか?**  
A: はい、アプリケーションが中断に耐性がある場合。多くの組織は、クリティカルなワークロードのためにスポットをオンデマンドまたはリザーブドインスタンスと組み合わせています。  
- [AWS スポットFAQ](https://aws.amazon.com/ec2/spot/faqs/)

**Q: スポットインスタンスでどれくらい節約できますか?**  
A: 通常、リージョン、タイプ、需要に応じて、オンデマンドと比較して70〜90%。  
- [AWS スポット節約](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)

**Q: スポットインスタンスが中断されるとどうなりますか?**  
A: 短い中断通知(AWSでは2分、Azure/GCPでは30秒)を受け取ります。その後、プロバイダーポリシーに従ってインスタンスが終了、停止、または休止されます。  
- [AWS スポット中断](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)

**Q: スポットインスタンスをリクエストするにはどうすればよいですか?**  
A: クラウドプロバイダーのコンソール、CLI、またはAPIを使用します。必要に応じてインスタンスタイプ、最大価格、期間を指定します。  
- [AWS スポットリクエスト](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)

**Q: スポットインスタンスはKubernetesで使用できますか?**  
A: はい、Kubernetesなどのコンテナオーケストレーターは、スポットインスタンスが中断されたときにポッドを再スケジュールできます。  
- [Kubernetesとスポットインスタンス](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)

**Q: スポットインスタンスにSLAはありますか?**  
A: いいえ。プロバイダーはスポットインスタンスの稼働時間や可用性を保証しません。

## 参考資料

- [AWS スポットインスタンスドキュメント](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [AWS EC2 スポット価格設定](https://aws.amazon.com/ec2/spot/pricing/)
- [CloudZero スポットインスタンスガイド](https://www.cloudzero.com/blog/spot-instances/)
- [Infracost スポットインスタンス用語集](https://www.infracost.io/glossary/spot-instances/)
- [Cast AI スポットインスタンスガイド](https://cast.ai/blog/reduce-cloud-costs-with-spot-instances/)
- [Milvus AI クイックリファレンス: スポットインスタンス](https://milvus.io/ai-quick-reference/what-are-spot-instances-in-cloud-computing)
- [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)
- [AWS スポットインスタンスアドバイザー](https://aws.amazon.com/ec2/spot/instance-advisor/)
- [Spot.io 究極ガイド](https://spot.io/resources/spot-instances/spot-instances-aws-azure-google-cloud/)
- [AWS スポットFAQ](https://aws.amazon.com/ec2/spot/faqs/)

## 関連用語

- [オンデマンドインスタンス](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html)
- [リザーブドインスタンス](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)