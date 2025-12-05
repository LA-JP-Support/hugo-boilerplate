---
title: オートスケーリング
date: 2025-11-25
translationKey: autoscaling
description: オートスケーリングは、リアルタイムの需要に基づいてクラウドコンピューティングリソース(VM、コンテナ)を自動的に調整し、パフォーマンス、可用性、コスト効率を最適化します。
keywords: ["オートスケーリング", "クラウドコンピューティング", "リソース割り当て", "水平スケーリング", "垂直スケーリング"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Autoscaling
term: オートスケーリング
reading: オートスケーリング
kana_head: あ
---
## メタディスクリプション

クラウドコンピューティングにおけるオートスケーリングは、ワークロードの需要に合わせてリソースの数やサイズを自動的に調整します。オートスケーリングの仕組み、種類(水平、垂直)、メリット、課題、ユースケース、ベストプラクティス、そしてロードバランシングとの違いについて学びましょう。

## オートスケーリングの定義

**オートスケーリング**は、仮想マシン(VM)、コンテナ、サーバーレス関数、ストレージなどの計算リソースを、リアルタイムのワークロード需要とポリシー駆動型ルールに基づいて自動的に割り当てまたは解放する、クラウドコンピューティングの基盤となる機能です。オートスケーリングにより、アプリケーションは一貫した可用性とパフォーマンスを維持するために必要なリソースを確保しながら、過剰なプロビジョニングと低活用を削減することでコストを最小化します。

AWS、Azure、Google Cloud、IBM、Oracleなどのクラウドプロバイダーは、すべてオートスケーリングをコア機能として提供しており、コンピュート、メモリ、その他のサービスタイプに対する動的なリソース割り当てを可能にしています。

> 「オートスケーリングは、アプリケーションが一貫した可用性を維持し、パフォーマンス目標を達成するために必要なリソースを確保するとともに、クラウドリソースの効率的な使用を促進し、クラウドコストを最小化するために使用されます。」  
> [IBM: What is Auto Scaling?](https://www.ibm.com/think/topics/autoscaling)  
> [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)

## オートスケーリングの仕組み

オートスケーリングは、システムメトリクスを監視し、事前定義されたポリシーに従ってスケーリングアクションを実行するサービスまたはフレームワークによって実装されます。

### 主要コンポーネント

- **起動設定**: 新しいリソースのプロビジョニング方法を定義し、イメージ、インスタンスタイプ、初期化スクリプト、セキュリティ設定を指定します。
- **オートスケーリンググループ(ASG)**: 一緒に管理されるリソースの論理グループで、最小、最大、希望するリソース数を持ちます。
- **スケーリングポリシー**: メトリクスまたはスケジュールによってトリガーされる、リソースの追加または削除のタイミングと方法を制御するルール。
- **監視とメトリクス**: CPU、メモリ、ディスクI/O、ネットワークスループット、またはカスタムアプリケーションメトリクスなどのシステム指標の収集と分析。
- **ヘルスチェック**: リソースの健全性を確保するための自動チェックで、必要に応じて不健全なインスタンスを置き換えます。
- **ライフサイクルフック**: スケーリングイベントの前後に実行されるカスタムアクションまたはスクリプト。
- **クールダウン/安定化期間**: 急速で反復的なスケーリング(スラッシング)を防ぐための、スケーリングアクション後の遅延。

> [AWS Auto Scaling Overview](https://aws.amazon.com/autoscaling/)  
> [GeeksforGeeks: What is Auto Scaling?](https://www.geeksforgeeks.org/system-design/what-is-auto-scaling/)  
> [DigitalOcean: A Deep Dive into Cloud Auto Scaling Techniques](https://www.digitalocean.com/community/tutorials/auto-scaling-techniques-guide)

### オートスケーリングプロセスのステップバイステップ

1. **監視**: オートスケーリングサービスは、スケーリンググループ内のすべてのリソースからリアルタイムメトリクスを収集します。
2. **評価**: 現在のメトリクス値をスケーリングポリシーのしきい値と比較します。
3. **決定**: しきい値を超えた場合、システムはスケールアウト(リソースの追加)またはスケールイン(リソースの削除)を決定します。
4. **アクション**: スケーリングアクションが実行されます—インスタンスのプロビジョニングまたは終了、またはリソースのサイズ変更。
5. **ヘルスチェックとライフサイクルフック**: 新しいリソースが検証され、設定されます。
6. **クールダウン**: システムは、さらなるスケーリングアクションの前に安定化期間を待ちます。
7. **フィードバックループ**: ワークロードとメトリクスが進化するにつれて、プロセスが繰り返されます。

この自動化により、手動でのリソース調整が不要になり、運用オーバーヘッドが削減されます。  
> [Datadog: Auto-scaling Knowledge Center](https://www.datadoghq.com/knowledge-center/auto-scaling/)

## オートスケーリングの種類

オートスケーリングは、2つの主要なアプローチに分類できます:

### 水平スケーリング(スケールアウト/イン)

水平スケーリングは、ワークロードの変化に対応するために実行されているリソースインスタンスの数を調整します。

- **仕組み:** VM、コンテナ、またはサーバーインスタンスを追加または削除します。
- **例:** トラフィックの急増時に、ロードバランサーの背後にさらにWebサーバーが追加され、オフピーク時にはサーバーが削除されます。
- **利点:** ダウンタイムなし、ステートレスで分散されたワークロードに対して高いスケーラビリティ、耐障害性の向上。
- **最適な用途:** マイクロサービス、Webアプリケーション、API、[コンテナ化](/ja/glossary/containerization/)されたワークロード。

### 垂直スケーリング(スケールアップ/ダウン)

垂直スケーリングは、既存のインスタンスのリソース割り当てを変更します。

- **仕組み:** 実行中のVMまたはコンテナのCPU、RAM、またはストレージを増減します。
- **例:** VMを2 vCPU/8GB RAMから8 vCPU/32GB RAMにスケーリングします。
- **利点:** 簡単に分散できないモノリシックまたはステートフルなアプリケーションに有用。
- **制限事項:** ダウンタイムまたはリソース移行が必要な場合があり、物理ハードウェアの制約によって制限されます。
- **最適な用途:** レガシーアプリ、データベース、または分散用に設計されていないワークロード。

| 側面                  | 水平スケーリング                | 垂直スケーリング                    |
|-------------------------|-----------------------------------|-------------------------------------|
| 何が変わるか?           | インスタンスの数               | 単一インスタンスのサイズ/リソース |
| ダウンタイムが必要か?      | 通常なし                      | 場合によってはあり                      |
| スケーラビリティ             | 高い(理論的には無制限)    | ハードウェアによって制限                 |
| 最適な用途                | ステートレス、分散ワークロード  | ステートフル、モノリシックワークロード      |
| 例                 | Webサーバーの追加/削除       | VM CPU/RAMのアップグレード                |

> [Hydrolix: Autoscaling in Cloud Computing](https://hydrolix.io/glossary/autoscaling/)  
> [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)

## オートスケーリングポリシーと戦略

オートスケーリングポリシーは、スケーリングアクションがいつどのように発生するかを管理します。最も一般的な戦略には以下が含まれます:

- **しきい値ベース(リアクティブ)スケーリング**  
  監視されたメトリクスが定義されたしきい値を超えたときにスケーリングアクションをトリガーします(例:5分間CPU > 80%)。
- **ターゲット追跡スケーリング**  
  メトリクスのターゲット値を維持するためにリソースを継続的に調整します(例:平均CPU使用率を60%に保つ)。
- **予測的(プロアクティブ)スケーリング**  
  過去の使用パターンまたは機械学習を使用して需要を予測し、事前にスケーリングします。
- **スケジュールベースのスケーリング**  
  事前に決められた時刻または日付にリソースをスケーリングします(例:営業時間中にスケールアップ)。
- **手動スケーリング**  
  管理者が手動でリソースを調整します。通常はフォールバックとして使用されます。

> [Datadog: Auto-scaling Knowledge Center](https://www.datadoghq.com/knowledge-center/auto-scaling/)  
> [Hydrolix: Autoscaling in Cloud Computing](https://hydrolix.io/glossary/autoscaling/)

## オートスケーリングのメリット

オートスケーリングは、大きな運用上および財務上のメリットをもたらします:

- **パフォーマンスの最適化**: 需要の急増時にアプリケーションの速度と稼働時間を維持します。
- **コスト効率**: アイドル状態のリソースに対する支払いから組織を解放し、クラウドの無駄を削減します。
- **可用性と信頼性の向上**: 障害が発生したリソースを自動的に置き換え、サービスの継続性を維持します。
- **運用の俊敏性**: 手動介入なしに動的なワークロードの変化に対応します。
- **ユーザーエクスペリエンス**: 速度低下や停止を防ぎ、一貫したサービス品質を確保します。
- **エネルギー効率**: アイドル状態のリソースをデプロビジョニングすることで、不要な電力使用を最小化します。

> [IBM: What is Auto Scaling?](https://www.ibm.com/think/topics/autoscaling)  
> [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)

## 課題と考慮事項

利点にもかかわらず、オートスケーリングには一連の課題があります:

- **設定の複雑さ**: 効果的なポリシーとグループを設計するには専門知識が必要です。
- **反応の遅延**: 新しいリソースのプロビジョニングには数分かかる場合があり、突然の急増時にパフォーマンスの遅延が発生するリスクがあります。
- **メトリクスの選択**: 効果的でないメトリクスの選択(例:メモリがボトルネックの場合にCPUでスケーリング)は非効率を引き起こす可能性があります。
- **コストの予期しない増加**: 過度に積極的なスケーリングまたは設定ミスは、予期しない費用につながる可能性があります。
- **アプリケーション設計の制約**: オートスケーリングは、ステートレスで水平にスケーラブルなアーキテクチャに最も効果的です。
- **監視と可観測性**: 可視性が低いと、スケーリングの問題やアプリケーションの問題が見えにくくなる可能性があります。

> [Datadog: Auto-scaling Knowledge Center](https://www.datadoghq.com/knowledge-center/auto-scaling/)  
> [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)

## 実世界のユースケースと例

オートスケーリングは、業界やシナリオを超えて広く使用されています:

### Eコマースプラットフォーム
- **シナリオ:** ブラックフライデーのセールが予測不可能なトラフィックの急増を引き起こします。
- **ソリューション:** オートスケーリングが追加のアプリケーションサーバーとデータベースサーバーをプロビジョニングし、可用性と高速なチェックアウトを確保します。

### メディアストリーミングサービス
- **シナリオ:** バイラルイベントまたは主要なリリースが同時視聴者を増加させます。
- **ソリューション:** ストリーミングサーバーがリアルタイムでスケールアップし、スムーズな再生を維持します。

### SaaSスタートアップ
- **シナリオ:** バイラルマーケティングが突然のユーザー成長を促進します。
- **ソリューション:** バックエンドリソースがオートスケールし、過剰なプロビジョニングなしに急速な成長を可能にします。

### ビッグデータとAI/MLワークロード
- **シナリオ:** モデルトレーニングまたは分析ジョブが変動するコンピュートを必要とします。
- **ソリューション:** コンピュートクラスターが並列処理のためにスケールし、ジョブ完了後に削減されます。

### APIとマイクロサービス
- **シナリオ:** 異なるエンドポイントまたはサービスが可変のリクエストレートを経験します。
- **ソリューション:** 各サービスが独自の負荷に基づいて独立してオートスケールします。

> [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)  
> [DigitalOcean: A Deep Dive into Cloud Auto Scaling Techniques](https://www.digitalocean.com/community/tutorials/auto-scaling-techniques-guide)

## オートスケーリングのベストプラクティス

オートスケーリングの効果を最大化するために、以下のベストプラクティスに従ってください:

- **主要メトリクスの監視**: 堅牢なツール(例:AWS CloudWatch、Azure Monitor、Datadog)を使用して、CPU、メモリ、アプリケーションメトリクスを追跡します。
- **明確なポリシーの定義**: 保守的なスケーリングしきい値から始め、シミュレートされた負荷の下でテストします。
- **クールダウンの実装**: スケーリングスラッシュを避けるために安定化期間を設定します。
- **ステートレスサービスの設計**: リソースを簡単に追加または削除できるように、セッション状態を外部に保存します。
- **アベイラビリティゾーン全体への分散**: オートスケーリンググループを分散することで回復力を高めます。
- **定期的なレビュー**: スケーリングアクションを分析し、パターンが進化するにつれてポリシーを調整します。
- **クラウドクォータの理解**: プロバイダーの制限を把握し、積極的に増加を要求します。
- **戦略の組み合わせ**: 既知のパターンには予測的またはスケジュールベースのスケーリングを使用し、バックアップとしてリアクティブスケーリングを使用します。
- **アラートの設定**: 予期しないスケーリングイベントやコストの急増に対する通知を設定します。

> [Hydrolix: Autoscaling in Cloud Computing](https://hydrolix.io/glossary/autoscaling/)  
> [DigitalOcean: A Deep Dive into Cloud Auto Scaling Techniques](https://www.digitalocean.com/community/tutorials/auto-scaling-techniques-guide)

## オートスケーリング vs. ロードバランシング

オートスケーリングとロードバランシングはしばしば一緒に使用されますが、異なる目的を果たします。

| 側面           | **オートスケーリング**                            | **ロードバランシング**                      |
|------------------|--------------------------------------------|-----------------------------------------|
| 目的          | リソースの数またはサイズを調整        | 受信トラフィックを分散            |
| 機能    | インスタンスの追加/削除、リソースのスケーリング   | リクエストを健全なサーバーにルーティング      |
| トリガー     | リソースメトリクスまたはスケジュール              | 各受信リクエスト                   |
| 影響           | インフラストラクチャ容量を変更            | リソース使用率を最適化          |
| スコープ            | インフラストラクチャレベル                       | ネットワーク/アプリケーションレベル               |
| コスト管理  | スケーリングによって支出を直接制御         | 間接的、過負荷コストを防止    |
| 例          | CPU > 70%が10分間続いたときに5台のVMを追加      | HTTPリクエストを最も負荷の少ないVMにルーティング  |

オートスケーリングは弾力的な容量を提供し、ロードバランシングはトラフィックの効率的で信頼性の高い分散を確保します。  
> [Datadog: Auto-scaling Knowledge Center](https://www.datadoghq.com/knowledge-center/auto-scaling/)

## 主要クラウドプロバイダー別のオートスケーリング機能

| プロバイダー    | オートスケーリングサービス                   | 主要機能とユースケース                                               |
|-------------|------------------------------------------|-----------------------------------------------------------------------|
| **AWS**     | [EC2 Auto Scaling Groups](https://aws.amazon.com/ec2/autoscaling/)、[Application Auto Scaling](https://aws.amazon.com/autoscaling/) | EC2、ECS、DynamoDB、Auroraを管理、ターゲット/予測的/スケジュールベースのポリシーをサポート、ELBとCloudWatchと統合 |
| **Azure**   | [Virtual Machine Scale Sets](https://azure.microsoft.com/en-us/services/virtual-machine-scale-sets/)、[Azure Autoscale](https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-get-started) | VM、App Servicesをスケーリング、メトリクスベースおよびスケジュールベースのスケーリングをサポート、ハイブリッドクラウドサポート                       |
| **GCP**     | [Managed Instance Groups](https://cloud.google.com/compute/docs/instance-groups)、[GKE Cluster Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) | Compute Engine VMとKubernetesノード/ポッドをスケーリング、カスタムメトリクスとHTTP負荷スケーリングをサポート               |
| **IBM Cloud** | [VPC Auto Scaling](https://www.ibm.com/cloud/vpc)、[Kubernetes Autoscaler](https://www.ibm.com/cloud/kubernetes-service/autoscaling) | VMとKubernetesクラスターをサポート、IBM Cloud Load Balancerと統合                                   |
| **Oracle Cloud** | [Instance Pools & Autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm) | コンピュートプールをスケーリング、メトリクスベースおよびスケジュールベースのスケーリングをサポート、OCI Load Balancerと統合             |

> [Hydrolix: Autoscaling in Cloud Computing](https://hydrolix.io/glossary/autoscaling/)  
> [IBM: What is Auto Scaling?](https://www.ibm.com/think/topics/autoscaling)

## 関連概念

- **エラスティシティ**: 需要に応じたリソースの自動適応。
- **クラウドの無駄**: 活用されていないまたはアイドル状態のリソースでコストを増加させるもの、オートスケーリングはこれを削減するのに役立ちます。
- **Infrastructure as Code (IaC)**: 一貫性のためにオートスケーリンググループとポリシーをプログラム的に定義すること。
- **FinOps**: クラウドコスト最適化のための財務運用プラクティス、しばしばオートスケーリングを活用します。
- **マイクロサービス**: 水平オートスケーリングから最も恩恵を受ける分散アーキテクチャ。
- **Kubernetesオートスケーリング**: コンテナオーケストレーションプラットフォームは、ポッドレベルおよびノードレベルのオートスケーリングを提供します。

> [IBM: What is Auto Scaling?](https://www.ibm.com/think/topics/autoscaling)  
> [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)

## 参考資料

- [IBM: What is Auto Scaling?](https://www.ibm.com/think/topics/autoscaling)
- [AWS Auto Scaling Overview](https://aws.amazon.com/autoscaling/)
- [DigitalOcean: A Deep Dive into Cloud Auto Scaling Techniques](https://www.digitalocean.com/community/tutorials/auto-scaling-techniques-guide)
- [Datadog: Auto-scaling Knowledge Center](https://www.datadoghq.com/knowledge-center/auto-scaling/)
- [GeeksforGeeks: What is Auto Scaling?](https://www.geeksforgeeks.org/system-design/what-is-auto-scaling/)
- [Hydrolix: Autoscaling in Cloud Computing](https://hydrolix.io/glossary/autoscaling/)
- [Middleware: What is Autoscaling?](https://middleware.io/blog/what-is-autoscaling/)
- [Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)

> **重要な洞察**  
> オートスケーリングは、需要が変動する際にクラウド環境がリソースを動的に割り当てることを可能にし、パフォーマンスとコストの両方を最適化します。これは、AI、ビッグデータ、または顧客向けプラットフォームを展開する組織にとっての基盤です。

**より技術的な詳細や実装ガイドについては、[Zesty: Autoscaling Glossary](https://zesty.co/finops-glossary/autoscaling/)または## メタディスクリプションをご覧ください。**