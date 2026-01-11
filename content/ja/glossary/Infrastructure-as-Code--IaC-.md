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
url: "/ja/glossary/infrastructure-as-code--iac-/"
aliases:
- "/ja/glossary/Infrastructure-as-Code--IaC-/"
---
## Infrastructure as Code (IaC)とは?

Infrastructure as Code (IaC)は、インフラストラクチャ(ネットワーク、仮想マシン、ロードバランサー、接続トポロジーなど)を手動プロセスではなく、コードと自動化を使用してプロビジョニングおよび管理するIT実践です。IaCは、システムの望ましい状態を機械可読な設定ファイルで記述することで、ソフトウェアエンジニアリングの原則をインフラストラクチャ管理に適用します。これらのファイルは通常、バージョン管理システムに保存されます。

この自動化アプローチは、エラーが発生しやすい手動設定を、反復可能でテスト可能、かつ監査可能なコード駆動型のデプロイメントに置き換え、クラウドおよびオンプレミスリソースの迅速なスケーリングと管理を可能にします。IaCは、DevOps、クラウドネイティブ運用、および最新のソフトウェアデリバリーパイプラインの基盤となっています。

## 主要概念

**冪等性:**  
同じIaC設定を繰り返し適用しても、実行回数に関係なく同じシステム状態が生成されます。冪等性により、安全で予測可能な更新が保証されます。

**バージョン管理:**  
すべてのインフラストラクチャコードは、バージョン管理システム(Gitなど)で管理されます。これにより、コラボレーション、コードレビュー、トレーサビリティ、および以前の状態へのロールバックが可能になります。

**モジュール性と再利用性:**  
IaCは、インフラストラクチャ定義を再利用可能なモジュール、ロール、またはスタックに分割することを推奨します。モジュール性により、重複が削減され、保守性が向上します。

**自動化:**  
自動化はIaCの中核です。ツールが設定ファイルを読み取り、必要に応じてインフラストラクチャをプロビジョニング、更新、または削除し、手動介入を排除します。

**宣言型モデルと命令型モデル:**

- **宣言型** – 望ましい状態を指定し、ツールが必要な手順を判断する
- **命令型** – 必要なコマンドまたは手順の正確なシーケンスを指定する

**可変インフラストラクチャと不変インフラストラクチャ:**

- **可変** – リソースをその場で変更する
- **不変** – 変更のために新しいリソースを作成し、古いものを破棄することでドリフトを削減する

## メリット

**一貫性と再現性:**  
すべての環境を同一にプロビジョニングでき、「スノーフレーク」サーバーを排除します。

**エラーの削減:**  
自動化とコードレビューにより、手動エラーと設定ドリフトが削減されます。

**スピードと俊敏性:**  
環境全体を数分で作成、更新、または破棄できます。

**コスト最適化:**  
自動化により、労力とクラウドリソースの無駄が削減されます。

**監査可能性:**  
すべての変更がバージョン管理で追跡され、コンプライアンスをサポートします。

**災害復旧:**  
コードから環境を迅速に再構築できます。

**コラボレーション:**  
コードベースのインフラストラクチャにより、チームが協力し、変更をレビューし、複雑なシステムを大規模に管理できます。

## 方法論

| 特徴 | 宣言型 | 命令型 |
|---------|-------------|------------|
| 哲学 | 最終状態がどうあるべきかを指定 | ステップバイステップの指示を指定 |
| 実行 | ツールがアクションを判断 | ユーザーがプロセスを制御 |
| 例 | Terraform、CloudFormation、Kubernetes | Bashスクリプト、Ansible ad-hoc、Chef |

**例 — 宣言型(Terraform):**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-123"
  instance_type = "t2.micro"
}
```

**例 — 命令型(Bash):**
```bash
aws ec2 run-instances --image-id ami-123 --instance-type t2.micro
```

宣言型モデルは、そのシンプルさ、保守性、および設定ドリフトを防ぐ能力から、一般的に推奨されます。

## インフラストラクチャライフサイクル

**記述:**  
設定ファイル(YAML、JSON、HCLなど)でインフラストラクチャを定義します。

**バージョン管理:**  
コードをVCS(例:Git)に保存します。ブランチ、プルリクエスト、コミット履歴を使用します。

**計画/検証:**  
変更を適用する前にプレビューします(例:`terraform plan`)。自動テストで構文、セキュリティ、ポリシーコンプライアンスをチェックします。

**プロビジョニング:**  
自動化エンジン(Terraform、CloudFormationなど)が設定を読み取り、インフラストラクチャを作成または更新します。

**デプロイ:**  
CI/CDパイプラインがアプリケーションコードと共にインフラストラクチャデプロイメントをトリガーします。

**破棄:**  
不要になったインフラストラクチャを自動的に廃止します。

## 主要ツール

### インフラストラクチャプロビジョニングツール

- **Terraform** – クラウド非依存、HCLを使用、AWS、Azure、GCPなどをサポート
- **AWS CloudFormation** – AWSネイティブ、YAMLまたはJSONを使用
- **Azure Resource Manager (ARM) Templates** – Azure向け、JSONを使用
- **Google Cloud Deployment Manager** – GCP向け、YAML/Python/Jinja2を使用
- **Pulumi** – 汎用言語(Python、Go、TypeScriptなど)を使用

### 構成管理ツール

- **Ansible** – エージェントレス、YAMLプレイブック
- **Puppet** – 宣言型、エージェントベース
- **Chef** – Ruby DSL、エージェントベース
- **SaltStack/Salt** – イベント駆動型、スケーラブル

### コンテナオーケストレーションツール

- **Kubernetes** – コンテナワークロードの宣言的管理
- **Docker Compose** – YAMLベース、マルチコンテナアプリケーション向け

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

**クラウドプロビジョニング:**  
クラウド環境(AWS、Azure、GCP)のデプロイメントを自動化します。

**自動アプリケーションデプロイメント:**  
コードを介して完全なアプリケーションスタックをプロビジョニングします。

**CI/CD統合:**  
ソフトウェアデリバリー中にインフラストラクチャを自動的に作成、テスト、破棄します。

**災害復旧:**  
障害発生後、代替リージョンでコードから環境全体を再作成します。

**マルチクラウド&ハイブリッド管理:**  
複数のクラウドとオンプレミス環境にわたってリソースを管理します。

**セキュリティとコンプライアンス:**  
セキュリティとコンプライアンスポリシーをIaCテンプレートに直接組み込みます。

**ネットワーク自動化:**  
ネットワーク、サブネット、セキュリティグループの作成を自動化します。

**ビッグデータ&AIインフラストラクチャ:**  
Hadoop、Spark、またはAI/MLクラスターをオンデマンドでプロビジョニングします。

## ベストプラクティス

**コードをバージョン管理に保存:**  
コラボレーション、トレーサビリティ、ロールバックを可能にします。

**モジュール化された再利用可能なコードを使用:**  
保守性のために小さく構成可能なモジュールを作成します。

**テストを自動化:**  
自動化された構文、セキュリティ、コンプライアンスチェックを統合します。

**不変インフラストラクチャを優先:**  
ドリフトを回避するため、その場での変更ではなく置き換えを行います。

**ピアレビュー:**  
コードレビューと承認のワークフローを確立します。

**徹底的にドキュメント化:**  
可能な限りコードベースを自己文書化します。

**シークレットを安全に管理:**  
専用のシークレット管理システムを使用します。

**自動検証:**  
リンターと静的解析ツールを使用します。

**一貫した命名とタグ付け:**  
リソースに対して厳格な命名/タグ付け規則を適用します。

## 課題

**学習曲線:**  
チームは新しいツールとパラダイムを学ぶ必要があります。

**状態管理:**  
状態ファイル(例:Terraform)は保護およびバックアップする必要があります。

**設定ドリフト:**  
IaC外での手動変更は不整合を引き起こす可能性があります。

**ツールの複雑性:**  
複数のツールが必要になる場合があり、統合が複雑になる可能性があります。

**セキュリティリスク:**  
ハードコードされたシークレット、設定ミスは脆弱性につながる可能性があります。

**デバッグ:**  
自動化されたエラーは手動プロセスよりも直感的でない場合があります。

**組織的変化:**  
文化的抵抗が採用を遅らせる可能性があります。

**レガシー統合:**  
既存システムの移行は複雑になる可能性があります。

**緩和戦略:**

- IaCを段階的に採用する
- トレーニングとドキュメントを提供する
- テストと検証を自動化する
- 厳格な変更管理を実施する

## 参考文献

- [AWS: What is Infrastructure as Code?](https://aws.amazon.com/what-is/iac/)
- [Spacelift: Infrastructure as Code — Best Practices, Benefits & Examples](https://spacelift.io/blog/infrastructure-as-code)
- [Red Hat: What is Infrastructure as Code (IaC)?](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)
- [Microsoft Learn: What is infrastructure as code (IaC)?](https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code)
- [IBM: What Is Infrastructure as Code (IaC)?](https://www.ibm.com/think/topics/infrastructure-as-code)
- [IBM: GitOps](https://www.ibm.com/think/topics/gitops)
- [Red Hat: Policy as Code](https://www.redhat.com/en/technologies/management/ansible/automated-policy-as-code)
- [Red Hat: Configuration Management](https://www.redhat.com/en/topics/automation/what-is-configuration-management)
- [Red Hat: CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [Azure Resource Manager Templates Overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)
- [Google Cloud Deployment Manager Documentation](https://cloud.google.com/deployment-manager/docs)
- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [Ansible Documentation](https://docs.ansible.com/)
- [Puppet Documentation](https://puppet.com/docs/)
- [Chef Documentation](https://docs.chef.io/)
- [Salt Documentation](https://docs.saltproject.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
