---
title: ブループリントのインポート/エクスポート
translationKey: import-export-blueprint
description: ブループリントのインポート/エクスポートは、自動化/チャットボットのロジックをファイル(JSON/YAML)として保存し、プラットフォームや環境間での共有、バックアップ、移行、バージョン管理を可能にします。
keywords: ["自動化ブループリント", "チャットボットブループリント", "JSON", "YAML", "ワークフロー移行"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: ブループリントのインポート/エクスポート
reading: ブループリントのインポート/エクスポート
kana_head: は
---
## 定義

**インポート / エクスポート ブループリント**とは、自動化シナリオやチャットボットの全ロジック、設定、構造(すべての設定、モジュール、フロー、ロジックを含む)を標準化されたファイル—一般的にはJSON形式またはYAML形式—として保存するプロセスです。これにより、ユーザーはこれらのブループリントを異なるアカウント、環境、またはプラットフォーム間で共有、バックアップ、移行、または移動することができます。

- **共有:** 高度な自動化やチャットボットフローを他のユーザー、チーム、またはコミュニティに配布します。
- **バックアップ:** 重要な自動化のロジックと設定を安全に保存し、データ損失を防ぎます。
- **移行:** 自動化やチャットボットを環境間(開発、ステージング、本番など)またはアカウント間で移動します。
- **バージョン管理:** 自動化フローの変更を時系列で追跡し、必要に応じて以前のバージョンに戻します。
- **コラボレーション:** ブループリントを交換することで、プロセス設計、レビュー、デプロイメントを容易に協力して行います。

ブループリントのインポート/エクスポートは、コアロジック、設定、メタデータ(サポートされている場合)を保持し、互換性のある環境で最小限の手作業で復元します。

## 1. インポート / エクスポート ブループリントとは?

インポート / エクスポート ブループリントは、多くの自動化およびAIチャットボットプラットフォームのコア機能です。これにより、ユーザーはワークフロー、シナリオ、またはボットの全定義—すべての設定、モジュール、ロジックを含む—をブループリントファイルに保存できます。このファイルは通常JSONまたはYAML形式で、自動化ロジックのポータブルで構造化された表現です。

### 有用性

- **コラボレーション**: チームはブループリントを交換することで、自動化を協力して開発、レビュー、デプロイします。
- **バージョン管理**: ブループリントをソース管理システム(Gitなど)に保存し、変更を追跡します。
- **リスク軽減**: 定期的なブループリントエクスポートは、バックアップおよび災害復旧ポイントとして機能します。
- **移行**: 一貫した設定で環境間で自動化を移動します。

### 業界の例

- [Make.com: Export and Import Blueprints (YouTubeチュートリアル)](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- [Microsoft Azure: Import and Export Blueprints with PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- [Blueprint Help Center: Migrate - Import/Export (RPAプラットフォーム)](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)

## 2. インポート / エクスポート ブループリントの使用方法

### 2.1 ブループリントのエクスポート

ブループリントのエクスポートは、ワークフロー、ボット、または自動化の現在の状態をファイルとして保存します。方法には以下が含まれます:

- **ユーザーインターフェース(UI):** ほとんどのプラットフォームは「エクスポート」ボタンまたはメニュー項目を提供します。
- **コマンドラインインターフェース(CLI):** 上級ユーザーは、CLIツールまたはスクリプト(例:Azure上のPowerShell)を使用できます。

**ファイル形式:**

- **JSON:** 最も一般的で、読みやすく、広くサポートされています。
- **YAML:** 特に設定が多い環境で、その読みやすさから一部の環境で使用されます。

#### 例: Make.com

1. シナリオエディタを開きます。
2. ツールバーの三点リーダーをクリックします。
3. 「Export Blueprint」を選択して`.json`ファイルをダウンロードします。

#### 例: Azure Blueprints (PowerShell)

```powershell
$bpDefinition = Get-AzBlueprint -SubscriptionId '{subId}' -Name 'MyBlueprint' -Version '1.1'
Export-AzBlueprintWithArtifact -Blueprint $bpDefinition -OutputPath 'C:\Blueprints'
```

#### 例: RPAプラットフォーム (Blueprint、UiPath、Blue Prism、Automation Anywhere)

インスタンス管理者は、各プラットフォームのエクスポート設定を構成し、必要に応じてエクスポート機能を有効または無効にできます。具体的な手順については、[Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)を参照してください。

### 2.2 ブループリントのインポート

ブループリントのインポートは、ブループリントファイルをアップロードすることで、新しい環境またはアカウントでワークフロー、自動化、またはボットを再作成します。

- **UIベースのインポート:** ほとんどのプラットフォームは、JSON/YAMLファイルをアップロードするための「Import Blueprint」オプションを提供します。
- **CLIベースのインポート:** 上級ユーザーは、ファイルパスとターゲット環境を指定してCLIツールを使用できます。

#### 例: Make.com

1. シナリオエディタを開きます。
2. ツールバーの三点リーダーをクリックします。
3. 「Import Blueprint」を選択し、`.json`ファイルを選択して「Save」をクリックします。
4. プロンプトに従って統合または接続を更新します。

#### 例: Azure Blueprints (PowerShell)

```powershell
Import-AzBlueprintWithArtifact -Name 'MyBlueprint' -ManagementGroupId 'DevMG' -InputPath 'C:\Blueprints\MyBlueprint'
```

#### 例: RPAプラットフォーム

インスタンス管理パネルを通じて、プラットフォームごと(例:Automation Anywhere、Blue Prism、UiPath)にインポートオプションを有効または無効にします([詳細ガイド](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export))。

**インポート後のアクション:**

- 統合またはアカウント(例:API、SaaSコネクタ)を再接続します。
- 環境固有の変数、エンドポイント、または認証情報を更新します。

## 3. ブループリントファイルの構造と形式

### 3.1 一般的な構造

ブループリントファイルには以下が含まれます:

- **メタデータ:** 名前、説明、バージョン、作成者、作成日。
- **モジュール/ステップ:** アクションまたはノードのシーケンス(例:トリガー、条件、API呼び出し)。
- **変数/パラメータ:** 入力、出力、環境変数、マッピングされたフィールド。
- **接続:** 統合ポイント(APIキー、認証情報—通常はセキュリティ上の理由でエクスポートされません)。
- **アーティファクト:** Azure Blueprintsは、`artifacts`フォルダ内の追加アーティファクトファイルを参照する場合があります。

### 3.2 フォルダ/ファイル階層 (Azure Blueprintsの例)

```
MyBlueprint/
  blueprint.json           # メインブループリント定義
  artifacts/               # すべてのアーティファクトファイル用フォルダ
    artifact1.json
    artifact2.json
```
参照: [Azure公式ドキュメント: Import and Export Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)

### 3.3 形式要件

- **JSON/YAML構文:** 有効で整形式である必要があります。
- **命名規則:** メインファイルは通常`blueprint.json`という名前で、アーティファクトは`artifacts/`内にあります。
- **機密データ:** 認証情報はほとんど含まれません。インポート後に再接続します。

### 3.4 バージョン互換性

- エクスポートされたブループリントがプラットフォームバージョンと互換性があることを確認します。
- 一部のプラットフォームは後方互換性を許可しますが、非推奨の機能は動作しない場合があります。
- [Azure Blueprints非推奨](https://learn.microsoft.com/en-us/azure/governance/blueprints/deprecated)通知—Template SpecsおよびDeployment Stacksに移行してください。

## 4. ユースケースと例

### 4.1 自動化テンプレートの共有

チームは実証済みのフローを共有するためにブループリントをエクスポートし、オンボーディングを加速し、プロセスを標準化します。  
**例:** ソリューションアーキテクトが、他の部門がカスタマイズできるようにデータ処理ブループリントをエクスポートします。

### 4.2 環境間の移行

ブループリントをエクスポート/インポートすることで、開発からステージングまたは本番環境に自動化を移動します。  
**例:** 検証済みのチャットボットを開発環境からエクスポートし、信頼性の高いデプロイメントのために本番環境にインポートします。

### 4.3 ミッションクリティカルな自動化のバックアップ

定期的なブループリントエクスポートはバックアップとして機能し、問題が発生した場合に迅速な復元を可能にします。  
**例:** 大規模な更新の前に、管理者はブループリントをエクスポートして、必要に応じてロールバックできるようにします。

### 4.4 バージョン管理とCI/CD

ブループリントをコードとして扱うことで、バージョン管理、協力開発、コードレビュー、自動テスト、CI/CDパイプラインが可能になります。  
**例:** DevOpsチームはブループリントJSONファイルをGitに保存し、デプロイメント前にプルリクエストと自動テストを使用します。

### 4.5 ベンダーまたはプラットフォームの変更

ブループリントファイルは、ターゲットが形式をサポートしているか、インポートツールを提供している場合、プラットフォーム間の移行を容易にします。  
**例:** UiPathからボットをエクスポートし、組み込み設定を介してアップグレードされた環境にインポートします。

包括的な移行ガイドについては:  
[Switching Automation Platforms: Complete Data Export and Import Guide | Autonoly](https://www.autonoly.com/blog/68a2aa89d4fe118dae2a444b/switching-automation-platforms-complete-data-export-and-import-guide)

## 5. ブループリントの管理: ベストプラクティス

- **インポート前の検証:** JSON/YAMLリンターを使用してファイルが有効であることを確認します。
- **依存関係の確認:** 参照されるリソース、接続、またはアーティファクトがターゲット環境に存在することを確認します。
- **機密データ:** ブループリントファイルに認証情報やシークレットを保存しないでください。
- **バージョンの追跡:** メタデータとファイル名にバージョン情報を使用します。
- **バックアップの自動化:** 定期的なエクスポートをスケジュールします。
- **ソース管理の使用:** コラボレーションと監査可能性のために、ブループリントをGitまたは他のVCSに保存します。
- **最新の状態を維持:** インポート/エクスポート機能の更新、非推奨、変更についてプラットフォームドキュメントを確認します。

## 6. 一般的なエラーとトラブルシューティング

### 6.1 インポートの失敗

- **無効なファイル形式:** リンターを使用して構文を確認します。
- **依存関係の欠落:** すべてのモジュール/リソースが利用可能である必要があります。
- **バージョンの非互換性:** ファイルがプラットフォームバージョン要件と一致することを確認します。
- **ロックされたブループリント:** 一部のプラットフォームは、チェックアウトされたブループリントの上書きを防ぎます。
- **ブラウザサポート:** 一部のブラウザはインポート/エクスポート機能をサポートしていない場合があります。

**トラブルシューティング手順:**

1. ファイル構文を検証します。
2. 形式/バージョン要件についてドキュメントを確認します。
3. 参照されるすべてのリソースが存在することを確認します。
4. ロックされたまたはチェックアウトされたブループリントへのインポートを避けます。
5. 推奨されるブラウザまたはCLIツールを使用します。

### 6.2 インポート後の問題

- **切断された統合:** すべての外部アカウント/APIを再接続します。
- **環境固有の設定:** 必要に応じて変数と設定を更新します。
- **設計エラー:** プラットフォームによってフラグが立てられた欠落リソースまたはエラーに対処します。

## 7. インポート / エクスポート ブループリントをサポートするプラットフォーム

### 7.1 Make.com

- **形式:** JSON
- **インポート/エクスポート:** シナリオエディタツールバー経由
- **チュートリアル:** [YouTube: Export and Import Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- **コミュニティ:** [Make Community: Importing JSON Blueprint](https://community.make.com/t/importing-json-blueprint/88348)

### 7.2 Azure Blueprints

- **形式:** アーティファクトサブフォルダ付きJSON
- **インポート/エクスポート:** PowerShell (`Export-AzBlueprintWithArtifact`、`Import-AzBlueprintWithArtifact`)
- **ドキュメント:** [Import/Export Blueprints with PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- **非推奨:** [Template Specs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/template-specs)および[Deployment Stacks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks)に移行してください。

### 7.3 BMC Cloud Lifecycle Management

- **形式:** JSON
- **インポート/エクスポート:** Service Designerワークスペース
- **ドキュメント:** [Exporting or importing a blueprint](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)

### 7.4 RPAプラットフォーム

- **Blueprint、Automation Anywhere、Blue Prism、UiPath**
- **形式:** プラットフォーム固有(多くの場合JSONまたは独自形式)
- **インポート/エクスポート:** インスタンス管理者によって管理され、設定可能な設定があります([Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export))

## 8. 関連用語

| キーワード               | 説明                                  |
|-----------------------|--------------------------------------|
| Export blueprint      | ブループリントファイルを保存するプロセスまたはコマンド。 |
| Import blueprint      | ブループリントをプラットフォームにロードするプロセスまたはコマンド。 |
| Export import         | システム間でファイルを転送する一般的な用語。 |
| Exporting importing   | エクスポートとインポートの両方の操作を実行すること。 |
| Managing blueprint    | ブループリントファイルを処理するための実践とツール。 |
| JSON file             | ブループリント構造に使用されるJavaScript Object Notationファイル。 |
| YAML file             | ブループリントに時々使用されるYAML Ain't Markup Languageファイル。 |

## 9. さらなるリソースと次のステップ

- **公式ドキュメント:**
  - [Microsoft Learn: Import and export blueprints with PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
  - [Exporting or importing a blueprint – BMC Documentation](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)
  - [Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)
- **チュートリアルとビデオ:**
  - [Make.com YouTube: Export and Import Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
  - [Make Community: Importing JSON Blueprint](https://community.make.com/t/importing-json-blueprint/88348)
- **コミュニティとトレーニング:**
  - [Make Academy](https://academy.make.com)
  - [Make Help Centre](https://www.make.com/en/help)
  - [BMC Communities](https://community.bmc.com/)
- **ベストプラクティス:**
  - ブループリントファイルをソース管理(例:GitHub、GitLab)に保存します。
  - ブループリント管理をCI/CDパイプラインに統合します。
  - インポート/エクスポート機能の変更について、プラットフォームのリリースノートを定期的に確認します。

## 10. 要約表

| 側面                    | 詳細                                                                                 |
|------------------------|-------------------------------------------------------------------------------------|
| **目的**               | 自動化/チャットボットフローの共有、バックアップ、移行、またはバージョン管理                   |
| **ファイルタイプ**            | JSON(主要)、YAML(時々)                                                    |
| **エクスポート方法**         | UIアクションまたはCLIコマンド                                                               |
| **インポート方法**          | UIアクションまたはCLIコマンド                                                               |
| **一般的なユースケース**      | チーム共有、環境移行、バックアップ、バージョン管理、プラットフォーム移行       |
| **プラットフォーム例**     | Make.com、Azure Blueprints、BMC CLM、RPAツール                                         |
| **トラブルシューティング**       | ファイル形式、依存関係、プラットフォームバージョン互換性を確認                        |
| **ベストプラクティス**        | 検証、バックアップ、ソース管理の使用、インポート後の統合更新                |
| **さらなる読み物**       | 上記のドキュメントとコミュニティリンクを参照                                            |

## 11. よくある質問

**Q: あるプラットフォームで作成されたブループリントファイルを別のプラットフォームで使用できますか?**  
A: ほとんどのブループリントファイルはプラットフォーム固有です。一部のプラットフォームは変換ツールまたは互換性のある形式を提供する場合がありますが、システム間でインポートする前に必ずドキュメントを確認してください。

**Q: ブループリントをエクスポートすると、APIキーとパスワードが含まれますか?**  
A: いいえ。機密データは通常除外されます。インポート後に統合を再接続してください。

**Q: すでに存在するブループリントをインポートするとどうなりますか?**  
A: プラットフォームの動作は異なります—一部は新しいバージョンを作成し、他は上書きし、一部は手動マージが必要です。インポート警告とドキュメントを確認してください。

**Q: バックアップのためにブループリントエクスポートを自動化するにはどうすればよいですか?**  
A: CLIツールまたはAPIを使用してエクスポートをスクリプト化し、ファイルを安全に保存するか、バージョン管理に保存します。

## 12. 関連項目

- [Infrastructure as Code (IaC)](https://learn.microsoft.com/en-us/azure/governance/blueprints/concepts/lifecycle)
- [Source Control Fundamentals](https://docs.github.com/en/get-started/quickstart/hello-world)
- [CI/CD with Automation Platforms](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-cicd)

### 参考文献とチュートリアル

- [Make.com YouTube: Export and Import Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- [Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)
- [Switching Automation Platforms: Complete Data Export and Import Guide | Autonoly](https://www.autonoly.com/blog/68a2aa89d4fe118dae2a444b/switching-automation-platforms-complete-data-export-and-import-guide)
- [Azure Blueprints Documentation](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- [BMC Documentation: Exporting or importing a blueprint](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)

この用語集エントリは、インポート / エクスポート ブループリントの包括的で詳細な概要を、権威ある参考文献、ベストプラクティス、技術的なファイル構造、プラットフォーム固有の手順とともに提供します。さらなる学習については、上記にリンクされているドキュメントとコミュニティリソースを参照してください。