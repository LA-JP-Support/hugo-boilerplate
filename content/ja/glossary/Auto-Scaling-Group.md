---
title: オートスケーリンググループ
date: 2025-11-25
translationKey: auto-scaling-group
description: オートスケーリンググループ(ASG)は、需要に基づいてスケーリングを行うことで、EC2インスタンスなどのコンピューティングリソースを自動的に調整し、アプリケーションのパフォーマンスを維持しながらコストを最小化します。
keywords:
- オートスケーリンググループ
- AWS Auto Scaling
- EC2インスタンス
- クラウドインフラストラクチャ
- スケーリングポリシー
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Auto-Scaling Group
term: オートスケーリンググループ
reading: オートスケーリンググループ
kana_head: あ
---
## 導入 / 定義

**Auto-Scaling Group(ASG)**は、クラウド環境における計算リソース(通常は[Amazon EC2インスタンス](https://aws.amazon.com/ec2/))の論理的なグループです。ASGは、実行中のインスタンス数を自動的に調整することで、安定した予測可能なアプリケーションパフォーマンスを維持しながらコストを最小化します。この弾力性は、リアルタイムの需要、ヘルスステータス、または事前定義されたスケーリングポリシーに応じて、スケールアウト(インスタンスの追加)またはスケールイン(インスタンスの削除)によって実現されます。ASGは、手動介入なしに、起動、監視、終了を含むインスタンスの完全なライフサイクルを管理します。

Auto-Scaling Groupは、弾力的で回復力があり、コスト最適化されたクラウドアーキテクチャの基盤となります。変動するワークロードを持つアプリケーションに不可欠であり、組織が可用性とパフォーマンスを維持し、過剰プロビジョニングを回避し、容量管理を自動化することを可能にします。

**参考資料:**  
- [Amazon EC2 Auto Scaling: What is Amazon EC2 Auto Scaling? (Official AWS Documentation)](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)  
- [Spot.io: Understanding EC2 Auto Scaling Groups](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/)  
- [GeeksforGeeks: Create and Configure the Auto Scaling Group in EC2](https://www.geeksforgeeks.org/devops/create-and-configure-the-auto-scaling-group-in-ec2/)

## コアコンポーネント

Auto-Scaling Groupは、リソース管理の自動化と最適化を目的として設計された、複数の統合コンポーネントで構成されています。

### 1. **起動テンプレート / 起動設定**
- **定義:** ASGによって起動されるインスタンスの設定を指定します。AMI、インスタンスタイプ、ストレージ、ネットワーキング、セキュリティ設定、IAMロール、ブートストラップスクリプトなどが含まれます。
- **起動テンプレート**は推奨されるより柔軟なオプションで、バージョニング、混合インスタンスポリシー(つまり、1つのグループ内で複数のインスタンスタイプと購入オプションを組み合わせる)、および高度なネットワーキング機能をサポートします。
- **起動設定**は古く、柔軟性が低く、作成後に変更できません。

**参考資料:**  
- [AWS: Launch Templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)  
- [Spot.io: EC2 Auto Scaling Groups with Multiple Instance Types](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a3)

### 2. **スケーリングポリシー**
- **目的:** ASGが容量を変更するタイミングと方法を定義します。
- **タイプ:**
  - **ターゲット追跡ポリシー:** 特定のメトリック(例:平均CPU使用率)を目標値で自動的に維持します。
  - **ステップスケーリングポリシー:** メトリックがしきい値からどれだけ逸脱しているかに応じて、さまざまな量でインスタンス数を調整します。
  - **シンプルスケーリングポリシー:** メトリックがしきい値を超えたときに、固定数のインスタンスを増減します。
  - **スケジュールスケーリング:** 事前定義された時間(例:営業時間、週末)にスケールします。
- **メトリック:** 一般的にCPU、メモリ、ネットワークI/O、リクエスト数、またはカスタム[CloudWatch](https://aws.amazon.com/cloudwatch/)メトリックを使用します。

**参考資料:**  
- [AWS: Dynamic Scaling Policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html)  
- [Datadog: Auto-Scaling Policy Types](https://www.datadoghq.com/knowledge-center/auto-scaling/)

### 3. **ヘルスチェック**
- **機能:** Amazon EC2ステータスチェックを使用してインスタンスのヘルスを継続的に監視し、オプションでElastic Load Balancer(ELB)を介したアプリケーションレベルのヘルスチェックも実施します。
- **アクション:** 異常なインスタンスは自動的に終了され、希望する容量を維持するために置き換えられます。

**参考資料:**  
- [AWS: Health Checks for Auto Scaling Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks.html)  
- [Spot.io: Health Checks](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a1)

### 4. **希望容量、最小容量、最大容量**
- **希望容量:** ASGが維持しようとする目標インスタンス数。
- **最小容量:** グループが持つ最小インスタンス数。
- **最大容量:** インスタンス数の上限で、過剰プロビジョニングを防ぎます。

**参考資料:**  
- [AWS: Configure Auto Scaling Group Size](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html)

### 5. **インスタンスタイプと購入オプション**
- **複数のインスタンスタイプ:** ASGは、ワークロードのニーズに合わせて容量を調整するために、複数のインスタンスタイプ(例:コンピューティング最適化、メモリ最適化、GPU対応)の組み合わせを使用できます。
- **購入モデル:** 単一のASG内でオンデマンド、リザーブド、[スポットインスタンス](/en/glossary/spot-instances/)をサポートし、コストと可用性を最適化します。

**参考資料:**  
- [AWS: Mixed Instances Policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)  
- [Spot.io: Auto Scaling Groups and Spot Instances](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a6)

### 6. **アベイラビリティーゾーン(AZ)**
- **目的:** [高可用性](/en/glossary/high-availability--ha-/)と耐障害性のために、リージョン内の複数のAZにインスタンスを分散します。
- **動作:** ASGは各有効なAZ内のインスタンス数のバランスを取り、障害が発生したAZを正常なAZでインスタンスを起動することで置き換えます。

**参考資料:**  
- [AWS: Distributing Instances Across Availability Zones](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-distribution-balancing.html)  
- [Spot.io: Auto Scaling Groups and Availability Zones](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a2)

### 7. **Elastic Load Balancing(ELB)統合**
- **役割:** 正常なASGインスタンス間で受信トラフィックを分散します。
- **タイプ:** Application Load Balancer(ALB)、Network Load Balancer(NLB)、Classic Load Balancer(CLB)、Gateway Load Balancer(GWLB)。
- **動作:** 新しいインスタンスは自動的に登録され、終了されたインスタンスは登録解除されます。

**参考資料:**  
- [AWS: Attach a Load Balancer to Your Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html)  
- [Spot.io: Elastic Load Balancing and Auto Scaling Groups](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a5)

### 8. **ライフサイクルフック**
- **定義:** インスタンスライフサイクルの特定のポイント(例:初期化、終了)でカスタムスクリプトやロジックを実行し、設定、ドレイン、またはクリーンアップタスクを処理できるようにします。

**参考資料:**  
- [AWS: Lifecycle Hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)

### 9. **タグとメタデータ**
- **使用法:** 追跡、自動化、コスト配分、ガバナンスのために、ASGとインスタンスにキーと値のペアを割り当てます。

**参考資料:**  
- [AWS: Tagging Auto Scaling Groups and Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html)  
- [Spot.io: Tagging Auto Scaling Groups](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a4)

## Auto-Scaling Groupの動作原理

Auto-Scaling Groupは、リアルタイムの需要と定義されたポリシーに基づいて、正常な計算インスタンスの最適な数を動的に維持します。

### 1. **初期化**
- ASGは、起動テンプレート/設定に従ってインスタンスを起動し、希望容量に達するまで、指定されたアベイラビリティーゾーン全体にインスタンスを分散します。

### 2. **ヘルス監視と置き換え**
- 定期的なヘルスチェック(EC2および/またはELB)により異常なインスタンスが特定され、容量を維持するために終了され、置き換えられます。

### 3. **スケーリングアクション**
- **スケールアウト:** 監視されているメトリック(例:CPU > 70%)がしきい値を超えると、ASGは最大容量まで追加のインスタンスを起動します。
- **スケールイン:** メトリックが下限しきい値を下回るか、需要が減少すると、ASGはインスタンスを終了しますが、最小容量を下回ることはありません。
- **スケジュールスケーリング:** 定義されたスケジュールに基づいて容量を調整します。
- **予測スケーリング(高度):** 履歴パターンと機械学習を使用して需要を予測し、事前にスケールします。

**例:**  
大規模イベント(例:ライブストリーミング)中、ASGは負荷の急増を検出し、より多くのインスタンスを起動します。イベントが終了すると、コストを最適化するためにスケールインします。

### 4. **Elastic Load Balancing統合**
- ロードバランサーは、新しく起動された正常なインスタンスにトラフィックをルーティングし、削除されるインスタンスを登録解除して、中断のないサービスを保証します。

### 5. **混合インスタンスと購入戦略**
- コスト効率と可用性のためにオンデマンドと[スポットインスタンス](/ja/glossary/spot-instances/)を組み合わせ、スポットフリートの割り当て戦略(例:容量最適化、最低価格)を使用します。

### 6. **ライフサイクル管理**
- ライフサイクルフックは、インスタンスの起動または終了時に、設定、状態保存、またはクリーンアップのための自動化をトリガーします。

### 7. **クロスAZバランシング**
- ASGは、回復力のためにAZ全体にインスタンスを均等に分散します。AZに障害が発生した場合、正常なAZで置き換えインスタンスが起動されます。

**参考資料:**  
- [AWS: How Auto Scaling Works](https://docs.aws.amazon.com/autoscaling/ec2/userguide/how-asg-works.html)  
- [Spot.io: How Do Auto Scaling Groups Work?](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a1)

## メリットとユースケース

### 主なメリット

- **弾力性:** 変動するワークロード需要に容量を合わせます。
- **コスト効率:** 過剰プロビジョニングを削減し、特にスポットおよびリザーブドインスタンスを使用して支出を最適化します。
- **高可用性:** ヘルスチェックとクロスAZ分散により耐障害性を確保します。
- **運用効率:** 容量管理を自動化し、手動介入を削減します。
- **回復力:** インスタンスまたはAZ障害からの迅速な回復。

### 代表的なユースケース

- **Webアプリケーション:** 変動するトラフィックを持つEコマース、SaaS、ストリーミングプラットフォーム(例:[Netflix](https://about.netflix.com/)、[Amazon.com](https://www.amazon.com/))。
- **ビッグデータ処理:** 一時的な計算フリートを必要とするバッチジョブ(例:ETL、ログ分析)。
- **マイクロサービスとコンテナ:** マイクロサービスごとにASGを割り当てて独立したスケーリングを実現。
- **CI/CDパイプライン:** ビルド/テスト環境を動的にプロビジョニング。
- **APIバックエンド:** リクエスト量に基づいてAPIサーバーをスケール。
- **イベント駆動型ワークロード:** キャンペーン、製品発売、またはバイラルイベントのための迅速なスケーリング。

**業界の例:**  
- **Netflix:** グローバルマイクロサービスのスケーラビリティのためにASGを使用。  
- **Airbnb:** 数百万のユーザーのために、旅行のピークシーズン中にリソースをスケール。

**参考資料:**  
- [Spot.io: Real-World Auto Scaling Examples](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/)  
- [CloudZero: AWS Auto Scaling 101](https://www.cloudzero.com/blog/aws-auto-scaling/)

## 設定とベストプラクティス

### 基本的なセットアップ手順

1. **起動テンプレート/設定を定義:** AMI、インスタンスタイプ、セキュリティ、ネットワーキング、スクリプトを指定します。
2. **Auto-Scaling Groupを作成:** 希望容量、最小容量、最大容量を設定し、アベイラビリティーゾーンを選択します。
3. **ロードバランサーをアタッチ:** トラフィックとヘルス監視のためにELBを統合します。
4. **スケーリングポリシーを設定:** ターゲット追跡、ステップ、シンプル、またはスケジュールポリシーを実装します。
5. **ヘルスチェックを有効化:** EC2および/またはELBヘルスチェックを選択します。
6. **タグを適用:** コスト配分、自動化、ガバナンスのため。
7. **ライフサイクルフックを実装(オプション):** 起動と終了タスクを自動化します。
8. **スケーリングイベントをテスト:** 負荷をシミュレートし、スケーリングとヘルス置き換えを検証します。

### ベストプラクティス

- **起動テンプレートを使用**して柔軟性と高度な機能を活用。
- **複数のAZに分散**して回復力を確保。
- **混合インスタンスポリシーを活用**してコスト削減。
- **使用状況とSLAに基づいて現実的な容量制限を設定**。
- **ユーザーエクスペリエンスとワークロードに合った関連メトリックを選択**。
- **ステートレス設計:** セッション/状態を外部(S3、DynamoDB)に保存。
- **重要なワークロードのインスタンス保護を有効化**。
- **監視と調整:** [CloudWatch](https://aws.amazon.com/cloudwatch/)、Datadog、または同様のツールを使用。
- **ライフサイクルフックを実装**して自動化。
- **定期的にコストをレビュー:** [CloudZero](https://www.cloudzero.com/blog/aws-auto-scaling/)を使用。

**さらなる参考資料:**  
- [AWS: Create Your First Auto Scaling Group (Tutorial)](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-your-first-auto-scaling-group.html)  
- [Spot.io: EC2 Auto Scaling Best Practices](https://spot.io/resources/aws-autoscaling/scaling-ec2-ecs-rds-and-more/ec2-autoscaling-the-basics-and-4-best-practices/)

## 課題と考慮事項

### 1. **設定の複雑さ**
- テンプレート、ポリシー、ヘルスチェックの正確な設定が必要です。設定ミスは、リソースのスラッシング、コスト増加、またはパフォーマンス問題を引き起こす可能性があります。

### 2. **アプリケーション設計の制約**
- アプリケーションは水平スケーリングとステートレス動作をサポートする必要があります。ステートフル/モノリシック設計は、完全なメリットを得るためにリファクタリングが必要です。

### 3. **クロスリージョンの制限**
- ASGはリージョナルです。クロスリージョンの冗長性には、別々のASGが必要です。

### 4. **メトリック選択の課題**
- 不適切なメトリック選択は、非効率的なスケーリングにつながる可能性があります。継続的な監視と調整が必要です。

### 5. **スケーリングラグ**
- インスタンスの起動/ウォームアップは、急激な急増時のスケーリングを遅らせる可能性があります。

### 6. **スポットインスタンスの中断**
- スポットインスタンスは中断される可能性があります。容量リバランシングを使用し、優雅な中断のためにアーキテクチャを設計します([詳細はこちら](https://spot.io/blog/predictive-rebalancing/))。

### 7. **制限とクォータ**
- AWSはリージョン、グループ、アカウントごとにクォータを適用します。

### 8. **他のサービスとの統合**
- フルスタックの自動スケーリングには、コンピューティング、ロードバランシング、ストレージ、データベース全体での調整された設定が必要です。

**推奨事項:**  
スケーリングイベント、ログ、コストを定期的にレビューします。可観測性ツール(例:[Datadog](https://www.datadoghq.com/knowledge-center/auto-scaling/)、CloudWatch)を使用し、必要に応じてポリシーを改善します。

## さらなるリソース

- [Amazon EC2 Auto Scaling documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)
- [Spot.io: Understanding EC2 Auto Scaling Groups](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/)
- [IBM: What is auto scaling?](https://www.ibm.com/think/topics/autoscaling)
- [CloudZero: AWS Auto Scaling 101](https://www.cloudzero.com/blog/aws-auto-scaling/)
- [Datadog: What is Auto-scaling?](https://www.datadoghq.com/knowledge-center/auto-scaling/)
- [Graph AI: Auto Scaling Groups](https://www.graphapp.ai/engineering-glossary/cloud-computing/auto-scaling-groups)

## よくある質問(FAQ)

**Q: Auto-Scaling Groupは複数のリージョンで使用できますか?**  
A: いいえ、ASGはリージョンスコープです。クロスリージョンの[高可用性](/ja/glossary/high-availability--ha-/)のためには、各リージョンで独立してASGを作成および管理します。  
[Spot.io: Multi-AZ vs Multi-Region](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/#a2)

**Q: Elastic Load BalancingはASGとどのように連携しますか?**  
A: ELBは正常なASGインスタンス間でトラフィックを分散し、インスタンスが追加または削除されると自動的に登録/登録解除します。  
[AWS: ELB Integration with ASGs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html)

**Q: ASG内のスポットインスタンスが中断されるとどうなりますか?**  
A: ASGは容量を維持するために置き換えインスタンスの起動を試みます。容量リバランシングは、リスクのあるスポットインスタンスを事前に置き換えます。  
[Spot.io: Capacity Rebalancing](https://spot.io/blog/predictive-rebalancing/)

**Q: 同じASGで異なるインスタンスタイプを使用できますか?**  
A: はい、起動テンプレートと混合ポリシーを使用すると、ASGは複数のインスタンスタイプの組み合わせを起動できます。  
[AWS: Mixed Instances Policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)

**Q: ASGの設定における一般的な落とし穴は何ですか?**  
A: 問題には、不適切なメトリック選択、非現実的な容量制限、ステートレス設計の欠如、AZ全体への分散の失敗が含まれます。

## ビジュアルリファレンス

- [Official AWS architecture diagram](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)

## 用語集クロスリファレンス

- **Elastic Load Balancer(ELB):** 複数の計算ターゲット間で受信アプリケーション/ネットワークトラフィックを分散するサービス。
- **スポットインスタンス:** 中断の可能性がある、より低コストでAWSの余剰容量を使用するEC2コンピューティング。
- **起動テンプレート:** インスタンスを起動するための設定を含むリソース。
- **容量リバランシング:** スポットインスタンスがリスクにさらされているときに可用性を事前に維持します。
- **ライフサイクルフック:** ASG内の主要なライフサイクルイベントでトリガーされるカスタムアクション。

## 関連記事

- [AWS Auto Scaling 101: Tips For Success](https://www.cloudzero.com/blog/aws-auto-scaling/)
- [Understanding EC2 Auto Scaling Groups | Spot.io](https://spot.io/resources/aws-autoscaling/understanding-ec2-auto-scaling-groups/)
- [What is Auto-scaling? How it Works & Use Cases | Datadog](https://www.datadoghq.com/knowledge-center/auto-scaling/)
- [Auto Scaling Groups: Definition, Examples, and Applications | Graph AI](https://www.graphapp.ai/engineering-glossary/cloud-computing/auto-scaling-groups)
- [IBM: What is auto scaling?](https://www.ibm.com/think/topics/autoscaling)
- [Amazon EC2 Auto Scaling groups - AWS Documentation](https://docs.aws.amazon.com/[autoscaling](/en/glossary/autoscaling/)/ec2/user