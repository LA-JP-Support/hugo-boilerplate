---
title: ブループリントのインポート/エクスポート
url: "/ja/glossary/Import---Export-Blueprint/"
translationKey: import-export-blueprint
description: ブループリントのインポート/エクスポートは、自動化やチャットボットのロジックをファイル(JSONまたはYAML)として保存し、プラットフォームや環境を超えた共有、バックアップ、移行、バージョン管理を可能にします。
keywords:
- 自動化ブループリント
- チャットボットブループリント
- JSON
- YAML
- ワークフロー移行
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: Import / Export Blueprint
term: ブループリントのインポート/エクスポート
---
## Import / Export Blueprintとは?
Import / Export Blueprintとは、自動化シナリオやチャットボットの全体的なロジック、設定、構造(すべての設定、モジュール、フロー、ロジックを含む)を標準化されたファイル—一般的にはJSON形式またはYAML形式—として保存するプロセスです。これにより、ユーザーはこれらのブループリントを異なるアカウント、環境、またはプラットフォーム間で共有、バックアップ、移行、または移動することができます。

**主な用途:**

- **共有** – 高度な自動化やチャットボットフローを他のユーザー、チーム、またはコミュニティに配布
- **バックアップ** – 重要な自動化のロジックと設定を安全に保存し、データ損失を防止
- **移行** – 自動化やチャットボットを環境間(開発、ステージング、本番)またはアカウント間で移動
- **バージョン管理** – 自動化フローの変更を時系列で追跡し、以前のバージョンに戻すことが可能
- **コラボレーション** – ブループリントを交換することで、プロセス設計、レビュー、デプロイメントを容易に協力

ブループリントのインポート/エクスポートは、コアロジック、設定、メタデータを保持し、互換性のある環境で最小限の手動作業で復元します。

## 仕組み

### ブループリントのエクスポート

エクスポートは、ワークフロー、ボット、または自動化の現在の状態をファイルとして保存します。方法には以下が含まれます:

**ユーザーインターフェース(UI):**  
ほとんどのプラットフォームは「エクスポート」ボタンまたはメニュー項目を提供しています。

**コマンドラインインターフェース(CLI):**  
上級ユーザーはCLIツールまたはスクリプトを使用できます。

**ファイル形式:**

- **JSON** – 最も一般的で、可読性が高く、広くサポートされている
- **YAML** – 一部の環境で可読性のために使用される

### ブループリントのインポート

インポートは、ブループリントファイルをアップロードすることで、新しい環境またはアカウントでワークフロー、自動化、またはボットを再作成します。

**UIベースのインポート:**  
ほとんどのプラットフォームは、JSON/YAMLファイルをアップロードするための「ブループリントをインポート」オプションを提供しています。

**CLIベースのインポート:**  
上級ユーザーは、ファイルパスとターゲット環境を指定してCLIツールを使用できます。

**インポート後のアクション:**

- 統合またはアカウント(API、SaaSコネクタ)を再接続
- 環境固有の変数、エンドポイント、または認証情報を更新

## プラットフォームの例

### Make.com

**エクスポート:**

1. シナリオエディタを開く
2. ツールバーの三点リーダーをクリック
3. 「ブループリントをエクスポート」を選択して`.json`ファイルをダウンロード

**インポート:**

1. シナリオエディタを開く
2. ツールバーの三点リーダーをクリック
3. 「ブループリントをインポート」を選択し、`.json`ファイルを選択して「保存」をクリック
4. プロンプトに従って統合または接続を更新

### Azure Blueprints

**エクスポート(PowerShell):**
```powershell
$bpDefinition = Get-AzBlueprint -SubscriptionId '{subId}' -Name 'MyBlueprint' -Version '1.1'
Export-AzBlueprintWithArtifact -Blueprint $bpDefinition -OutputPath 'C:\Blueprints'
```

**インポート(PowerShell):**
```powershell
Import-AzBlueprintWithArtifact -Name 'MyBlueprint' -ManagementGroupId 'DevMG' -InputPath 'C:\Blueprints\MyBlueprint'
```

**注意:** Azure Blueprintsは非推奨です。Template SpecsおよびDeployment Stacksへの移行が推奨されます。

### RPAプラットフォーム

**Blueprint、Automation Anywhere、Blue Prism、UiPath:**  
インスタンス管理パネルを通じて、プラットフォームごとにインポート/エクスポートオプションを有効化または無効化します。

## ブループリントファイルの構造

### 一般的な構造

ブループリントファイルには以下が含まれます:

- **メタデータ** – 名前、説明、バージョン、作成者、作成日
- **モジュール/ステップ** – アクションまたはノードのシーケンス
- **変数/パラメータ** – 入力、出力、環境変数、マッピングされたフィールド
- **接続** – 統合ポイント(APIキー、認証情報—通常はセキュリティ上の理由でエクスポートされない)
- **アーティファクト** – 追加のアーティファクトファイル(Azure Blueprints)

### フォルダ階層(Azureの例)

```
MyBlueprint/
  blueprint.json           # メインのブループリント定義
  artifacts/               # すべてのアーティファクトファイル用のフォルダ
    artifact1.json
    artifact2.json
```

### 形式要件

- **JSON/YAML構文** – 有効で整形式である必要がある
- **命名規則** – メインファイルは通常`blueprint.json`という名前で、アーティファクトは`artifacts/`内に配置
- **機密データ** – 認証情報はほとんど含まれない。インポート後に再接続が必要
- **バージョン互換性** – エクスポートされたブループリントがプラットフォームバージョンと互換性があることを確認

## ユースケース

**自動化テンプレートの共有:**  
チームはブループリントをエクスポートして実証済みのフローを共有し、オンボーディングを加速し、プロセスを標準化します。

**環境間の移行:**  
ブループリントをエクスポート/インポートすることで、開発からステージングまたは本番環境へ自動化を移動します。

**ミッションクリティカルな自動化のバックアップ:**  
定期的なブループリントエクスポートはバックアップとして機能し、問題発生時の迅速な復元を可能にします。

**バージョン管理とCI/CD:**  
ブループリントをコードとして扱うことで、バージョン管理、共同開発、コードレビュー、自動テスト、CI/CDパイプラインが可能になります。

**ベンダーまたはプラットフォームの変更:**  
ブループリントファイルは、ターゲットが形式をサポートしているか、インポートツールを提供している場合、プラットフォーム間の移行を容易にします。

## ベストプラクティス

**インポート前の検証:**  
JSON/YAMLリンターを使用してファイルが有効であることを確認します。

**依存関係の確認:**  
参照されるリソース、接続、またはアーティファクトがターゲット環境に存在することを確認します。

**機密データ:**  
ブループリントファイルに認証情報やシークレットを保存しないでください。

**バージョンの追跡:**  
メタデータとファイル名にバージョン情報を使用します。

**バックアップの自動化:**  
定期的なエクスポートをスケジュールします。

**ソース管理の使用:**  
コラボレーションと監査可能性のために、ブループリントをGitまたは他のVCSに保存します。

**最新状態の維持:**  
更新、非推奨、変更についてプラットフォームのドキュメントを確認します。

## 一般的なエラーとトラブルシューティング

**インポートの失敗:**

- **無効なファイル形式** – リンターを使用して構文を確認
- **依存関係の欠落** – すべてのモジュール/リソースが利用可能である必要がある
- **バージョンの非互換性** – ファイルがプラットフォームのバージョン要件と一致することを確認
- **ロックされたブループリント** – 一部のプラットフォームはチェックアウトされたブループリントの上書きを防止
- **ブラウザサポート** – 一部のブラウザはインポート/エクスポート機能をサポートしていない場合がある

**インポート後の問題:**

- **切断された統合** – すべての外部アカウント/APIを再接続
- **環境固有の設定** – 必要に応じて変数と設定を更新
- **設計エラー** – プラットフォームによってフラグが立てられた欠落リソースまたはエラーに対処

## Import / Exportをサポートするプラットフォーム

**Make.com:**

- 形式: JSON
- インポート/エクスポート: シナリオエディタのツールバー経由

**Azure Blueprints:**

- 形式: アーティファクトサブフォルダ付きJSON
- インポート/エクスポート: PowerShell
- 非推奨: Template SpecsおよびDeployment Stacksへの移行

**BMC Cloud Lifecycle Management:**

- 形式: JSON
- インポート/エクスポート: Service Designerワークスペース

**RPAプラットフォーム:**

- Blueprint、Automation Anywhere、Blue Prism、UiPath
- 形式: プラットフォーム固有(多くの場合JSONまたは独自形式)
- インポート/エクスポート: インスタンス管理者によって管理

## 関連用語

| キーワード | 説明 |
|---------|-------------|
| Export blueprint | ブループリントファイルを保存するプロセスまたはコマンド |
| Import blueprint | ブループリントをプラットフォームにロードするプロセスまたはコマンド |
| Export import | システム間でファイルを転送する一般的な用語 |
| Managing blueprint | ブループリントファイルを処理するための実践とツール |
| JSON file | JavaScript Object Notationファイル、ブループリント構造に使用 |
| YAML file | YAML Ain't Markup Languageファイル、ブループリントに使用されることがある |

## よくある質問

**Q: あるプラットフォームで作成したブループリントファイルを別のプラットフォームで使用できますか?**  
A: ほとんどのブループリントファイルはプラットフォーム固有です。一部のプラットフォームは変換ツールまたは互換性のある形式を提供する場合がありますが、常にドキュメントを確認してください。

**Q: ブループリントをエクスポートすると、APIキーやパスワードも含まれますか?**  
A: いいえ。機密データは通常除外されます。インポート後に統合を再接続してください。

**Q: 既に存在するブループリントをインポートするとどうなりますか?**  
A: プラットフォームの動作は異なります—新しいバージョンを作成するもの、上書きするもの、手動マージが必要なものがあります。インポート警告とドキュメントを確認してください。

**Q: バックアップのためにブループリントエクスポートを自動化するにはどうすればよいですか?**  
A: CLIツールまたはAPIを使用してエクスポートをスクリプト化し、ファイルを安全に保存するか、バージョン管理に保存します。

## 参考資料


1. Make.com. (n.d.). Export and Import Blueprints. YouTube.

2. Make Community. (n.d.). Importing JSON Blueprint. Make Community Forum.

3. Make Academy. Online Learning Platform. URL: https://academy.make.com

4. Make Help Centre. Support Resource. URL: https://www.make.com/en/help

5. Microsoft. (n.d.). Import and Export Blueprints with PowerShell. Microsoft Learn.

6. Microsoft. (n.d.). Azure Blueprints Deprecated. Microsoft Learn.

7. Microsoft. (n.d.). Template Specs. Microsoft Learn.

8. Microsoft. (n.d.). Deployment Stacks. Microsoft Learn.

9. Microsoft. (n.d.). Azure Blueprints Lifecycle. Microsoft Learn.

10. BMC. (n.d.). Exporting or Importing a Blueprint. BMC Documentation.

11. Blueprint Help Center. (n.d.). Migrate - Import/Export. Blueprint Help Docs.

12. Autonoly. (n.d.). Switching Automation Platforms Guide. Autonoly Blog.

13. BMC Communities. Online Community Platform. URL: https://community.bmc.com/

14. GitHub. (n.d.). Source Control Fundamentals. GitHub Docs.

15. Microsoft. (n.d.). CI/CD with Azure DevOps. Microsoft Learn.
