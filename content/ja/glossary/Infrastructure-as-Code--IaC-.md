---
title: Infrastructure as Code (IaC)
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: infrastructure-as-code-iac
description: Infrastructure as Code(IaC)は、ネットワーク、仮想マシン、ロードバランサーなどのITインフラストラクチャをコードと自動化を使用して定義・管理する手法です。そのメリット、ツール、ベストプラクティスについて解説します。
keywords:
- Infrastructure as Code
- IaC
- DevOps
- 自動化
- クラウドインフラストラクチャ
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Infrastructure as Code (IaC)
term: インフラストラクチャー アズ コード(アイエーシー)
url: "/ja/glossary/Infrastructure-as-Code--IaC-/"
---
## Infrastructure as Code (IaC)とは?

Infrastructure as Code (IaC)は、インフラストラクチャ(ネットワーク、仮想マシン、ロードバランサー、接続トポロジーなど)を手動プロセスではなく、コードと自動化を使用してプロビジョニングおよび管理するIT実践です。IaCは、システムの望ましい状態を機械可読な設定ファイルで記述することで、ソフトウェアエンジニアリングの原則をインフラストラクチャ管理に適用します。これらのファイルは通常、バージョン管理システムに保存されます。

この自動化アプローチは、エラーが発生しやすい手動設定を、反復可能でテスト可能、かつ監査可能なコード駆動型のデプロイメントに置き換え、クラウドおよびオンプレミスリソースの迅速なスケーリングと管理を可能にします。IaCは、DevOps、クラウドネイティブ運用、および最新のソフトウェアデリバリーパイプラインの基盤となっています。

## 主要概念

<strong>冪等性:</strong>同じIaC設定を繰り返し適用しても、実行回数に関係なく同じシステム状態が生成されます。冪等性により、安全で予測可能な更新が保証されます。

<strong>バージョン管理:</strong>すべてのインフラストラクチャコードは、バージョン管理システム(Gitなど)で管理されます。これにより、コラボレーション、コードレビュー、トレーサビリティ、および以前の状態へのロールバックが可能になります。

<strong>モジュール性と再利用性:</strong>IaCは、インフラストラクチャ定義を再利用可能なモジュール、ロール、またはスタックに分割することを推奨します。モジュール性により、重複が削減され、保守性が向上します。

<strong>自動化:</strong>自動化はIaCの中核です。ツールが設定ファイルを読み取り、必要に応じてインフラストラクチャをプロビジョニング、更新、または削除し、手動介入を排除します。

<strong>宣言型モデルと命令型モデル:</strong>- <strong>宣言型</strong>– 望ましい状態を指定し、ツールが必要な手順を判断する
- <strong>命令型</strong>– 必要なコマンドまたは手順の正確なシーケンスを指定する

<strong>可変インフラストラクチャと不変インフラストラクチャ:</strong>- <strong>可変</strong>– リソースをその場で変更する
- <strong>不変</strong>– 変更のために新しいリソースを作成し、古いものを破棄することでドリフトを削減する

## メリット

<strong>一貫性と再現性:</strong>すべての環境を同一にプロビジョニングでき、「スノーフレーク」サーバーを排除します。

<strong>エラーの削減:</strong>自動化とコードレビューにより、手動エラーと設定ドリフトが削減されます。

<strong>スピードと俊敏性:</strong>環境全体を数分で作成、更新、または破棄できます。

<strong>コスト最適化:</strong>自動化により、労力とクラウドリソースの無駄が削減されます。

<strong>監査可能性:</strong>すべての変更がバージョン管理で追跡され、コンプライアンスをサポートします。

<strong>災害復旧:</strong>コードから環境を迅速に再構築できます。

<strong>コラボレーション:</strong>コードベースのインフラストラクチャにより、チームが協力し、変更をレビューし、複雑なシステムを大規模に管理できます。

## 方法論

| 特徴 | 宣言型 | 命令型 |
|---------|-------------|------------|
| 哲学 | 最終状態がどうあるべきかを指定 | ステップバイステップの指示を指定 |
| 実行 | ツールがアクションを判断 | ユーザーがプロセスを制御 |
| 例 | Terraform、CloudFormation、Kubernetes | Bashスクリプト、Ansible ad-hoc、Chef |

<strong>例 — 宣言型(Terraform):</strong>```hcl
resource "aws_instance" "web" {
  ami           = "ami-123"
  instance_type = "t2.micro"
}
```

**例 — 命令型(Bash):**```bash
aws ec2 run-instances --image-id ami-123 --instance-type t2.micro
```

宣言型モデルは、そのシンプルさ、保守性、および設定ドリフトを防ぐ能力から、一般的に推奨されます。

## インフラストラクチャライフサイクル

<strong>記述:</strong>設定ファイル(YAML、JSON、HCLなど)でインフラストラクチャを定義します。

<strong>バージョン管理:</strong>コードをVCS(例:Git)に保存します。ブランチ、プルリクエスト、コミット履歴を使用します。

<strong>計画/検証:</strong>変更を適用する前にプレビューします(例:`terraform plan`)。自動テストで構文、セキュリティ、ポリシーコンプライアンスをチェックします。

<strong>プロビジョニング:</strong>自動化エンジン(Terraform、CloudFormationなど)が設定を読み取り、インフラストラクチャを作成または更新します。

<strong>デプロイ:</strong>CI/CDパイプラインがアプリケーションコードと共にインフラストラクチャデプロイメントをトリガーします。

<strong>破棄:</strong>不要になったインフラストラクチャを自動的に廃止します。

## 主要ツール

### インフラストラクチャプロビジョニングツール

- <strong>Terraform</strong>– クラウド非依存、HCLを使用、AWS、Azure、GCPなどをサポート
- <strong>AWS CloudFormation</strong>– AWSネイティブ、YAMLまたはJSONを使用
- <strong>Azure Resource Manager (ARM) Templates</strong>– Azure向け、JSONを使用
- <strong>Google Cloud Deployment Manager</strong>– GCP向け、YAML/Python/Jinja2を使用
- <strong>Pulumi</strong>– 汎用言語(Python、Go、TypeScriptなど)を使用

### 構成管理ツール

- <strong>Ansible</strong>– エージェントレス、YAMLプレイブック
- <strong>Puppet</strong>– 宣言型、エージェントベース
- <strong>Chef</strong>– Ruby DSL、エージェントベース
- <strong>SaltStack/Salt</strong>– イベント駆動型、スケーラブル

### コンテナオーケストレーションツール

- <strong>Kubernetes</strong>– コンテナワークロードの宣言的管理
- <strong>Docker Compose</strong>– YAMLベース、マルチコンテナアプリケーション向け

### ツール比較

| ツール | カテゴリ | モデル | プラットフォームサポート | 言語 |
|------|----------|-------|-----------------|----------|
| Terraform | プロビジョニング | 宣言型 | マルチクラウド/オンプレミス | HCL |
| CloudFormation | プロビジョニング | 宣言型 | AWS | YAML/JSON |
| Ansible | 構成管理 | ハイブリッド | マルチクラウド/オンプレミス | YAML |
| Puppet | 構成管理 | 宣言型 | マルチクラウド/オンプレミス | Puppet DSL |
| Chef | 構成管理 | 命令型 | マルチクラウド/オンプレミス | Ruby DSL |
| Kubernetes | オーケストレーション | 宣言型 | マルチクラウド/オンプレミス | YAML |

## ユースケース

<strong>クラウドプロビジョニング:</strong>クラウド環境(AWS、Azure、GCP)のデプロイメントを自動化します。

<strong>自動アプリケーションデプロイメント:</strong>コードを介して完全なアプリケーションスタックをプロビジョニングします。

<strong>CI/CD統合:</strong>ソフトウェアデリバリー中にインフラストラクチャを自動的に作成、テスト、破棄します。

<strong>災害復旧:</strong>障害発生後、代替リージョンでコードから環境全体を再作成します。

<strong>マルチクラウド&ハイブリッド管理:</strong>複数のクラウドとオンプレミス環境にわたってリソースを管理します。

<strong>セキュリティとコンプライアンス:</strong>セキュリティとコンプライアンスポリシーをIaCテンプレートに直接組み込みます。

<strong>ネットワーク自動化:</strong>ネットワーク、サブネット、セキュリティグループの作成を自動化します。

<strong>ビッグデータ&AIインフラストラクチャ:</strong>Hadoop、Spark、またはAI/MLクラスターをオンデマンドでプロビジョニングします。

## ベストプラクティス

<strong>コードをバージョン管理に保存:</strong>コラボレーション、トレーサビリティ、ロールバックを可能にします。

<strong>モジュール化された再利用可能なコードを使用:</strong>保守性のために小さく構成可能なモジュールを作成します。

<strong>テストを自動化:</strong>自動化された構文、セキュリティ、コンプライアンスチェックを統合します。

<strong>不変インフラストラクチャを優先:</strong>ドリフトを回避するため、その場での変更ではなく置き換えを行います。

<strong>ピアレビュー:</strong>コードレビューと承認のワークフローを確立します。

<strong>徹底的にドキュメント化:</strong>可能な限りコードベースを自己文書化します。

<strong>シークレットを安全に管理:</strong>専用のシークレット管理システムを使用します。

<strong>自動検証:</strong>リンターと静的解析ツールを使用します。

<strong>一貫した命名とタグ付け:</strong>リソースに対して厳格な命名/タグ付け規則を適用します。

## 課題

<strong>学習曲線:</strong>チームは新しいツールとパラダイムを学ぶ必要があります。

<strong>状態管理:</strong>状態ファイル(例:Terraform)は保護およびバックアップする必要があります。

<strong>設定ドリフト:</strong>IaC外での手動変更は不整合を引き起こす可能性があります。

<strong>ツールの複雑性:</strong>複数のツールが必要になる場合があり、統合が複雑になる可能性があります。

<strong>セキュリティリスク:</strong>ハードコードされたシークレット、設定ミスは脆弱性につながる可能性があります。

<strong>デバッグ:</strong>自動化されたエラーは手動プロセスよりも直感的でない場合があります。

<strong>組織的変化:</strong>文化的抵抗が採用を遅らせる可能性があります。

<strong>レガシー統合:</strong>既存システムの移行は複雑になる可能性があります。

<strong>緩和戦略:</strong>- IaCを段階的に採用する
- トレーニングとドキュメントを提供する
- テストと検証を自動化する
- 厳格な変更管理を実施する

## 参考文献


1. AWS. (n.d.). What is Infrastructure as Code?. AWS Documentation. URL: https://aws.amazon.com/what-is/iac/

2. Spacelift. (n.d.). Infrastructure as Code — Best Practices, Benefits & Examples. Spacelift Blog. URL: https://spacelift.io/blog/infrastructure-as-code

3. Red Hat. (n.d.). What is Infrastructure as Code (IaC)?. Red Hat Topics. URL: https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac

4. Microsoft. (n.d.). What is infrastructure as code (IaC)?. Microsoft Learn. URL: https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code

5. IBM. (n.d.). What Is Infrastructure as Code (IaC)?. IBM Think Topics. URL: https://www.ibm.com/think/topics/infrastructure-as-code

6. IBM. (n.d.). GitOps. IBM Think Topics. URL: https://www.ibm.com/think/topics/gitops

7. Red Hat. (n.d.). Policy as Code. Red Hat Technologies. URL: https://www.redhat.com/en/technologies/management/ansible/automated-policy-as-code

8. Red Hat. (n.d.). Configuration Management. Red Hat Topics. URL: https://www.redhat.com/en/topics/automation/what-is-configuration-management

9. Red Hat. (n.d.). CI/CD. Red Hat Topics. URL: https://www.redhat.com/en/topics/devops/what-is-ci-cd

10. Terraform. Documentation. URL: https://www.terraform.io/docs/

11. AWS CloudFormation. User Guide. URL: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html

12. Azure Resource Manager. Templates Overview. URL: https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview

13. Google Cloud Deployment Manager. Documentation. URL: https://cloud.google.com/deployment-manager/docs

14. Pulumi. Documentation. URL: https://www.pulumi.com/docs/

15. Ansible. Documentation. URL: https://docs.ansible.com/

16. Puppet. Documentation. URL: https://puppet.com/docs/

17. Chef. Documentation. URL: https://docs.chef.io/

18. Salt. Documentation. URL: https://docs.saltproject.io/

19. Kubernetes. Documentation. URL: https://kubernetes.io/docs/home/

20. Docker Compose. Documentation. URL: https://docs.docker.com/compose/
