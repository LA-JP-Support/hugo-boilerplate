---
title: 環境変数(シークレット)
translationKey: environment-variables-secrets-the
description: アプリケーションの安全な設定のための環境変数(シークレット)について学びます。APIキーやパスワードなどの機密データをコードから分離し、セキュリティと柔軟性を確保します。
keywords:
- 環境変数
- シークレット管理
- APIキー
- アプリケーションセキュリティ
- 設定管理
category: General
type: glossary
date: 2025-12-03
draft: false
term: かんきょうへんすう(しーくれっと):しょうさいようごしゅう
reading: 環境変数(シークレット)
kana_head: その他
e-title: Environment Variables (Secrets)
---

# 環境変数(シークレット)とは何か?

環境変数は、外部で定義された名前付きのキー・バリューペアであり、アプリケーションに実行時の設定を提供します。シークレットとして利用される場合、APIキー、パスワード、接続文字列、トークンなどの機密データをコードベース、UI、ログの外部に保存します。この分離により、シークレットがソースコードにハードコーディングされたり、バージョン管理にチェックインされたりすることがなくなります。

- **例え:** 環境変数の値は、コード内のプレースホルダーとして機能します。例えば、`API_KEY = "secret123"`と記述する代わりに、`API_KEY`を参照し、その値は実行環境で実行時にのみ定義されます。
- **セキュリティコンテキスト:** シークレットを環境変数に保存することで、コードの漏洩、Gitリポジトリへのアクセス、ログを通じた偶発的な露出のリスクを最小限に抑えます。機密値は実行時に注入され、特に必要な場合を除き、ビジュアルインターフェースや設定ファイルには保存されません。
- **シークレットの種類:** データベースパスワード、APIトークン、OAuth認証情報、暗号化キー、機能フラグなど。

**参照:**  
- [OWASP Secrets Management Cheat Sheet—Intro and General Concepts](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#1-introduction)  
- [Kinsta: What Is an Environment Variable?](https://kinsta.com/blog/what-is-an-environment-variable/)

## なぜシークレットに環境変数を使用するのか?

**コードと設定の分離:**  
- 機密データをコードベースやバージョン管理から切り離します。  
- 同じコードベースを異なる環境(開発、ステージング、本番)で異なる認証情報を使用して実行できます。

**セキュリティ:**  
- シークレットをコードや公開リポジトリに埋め込まないことで、漏洩リスクを軽減します。
- シークレットがログ、エラーメッセージ、UIに露出するのを防ぎます。

**柔軟性と保守性:**  
- コード変更なしでシークレットを更新またはローテーションできます。
- インシデント(認証情報の漏洩など)への迅速な対応をサポートし、環境変数を変更してアプリケーションを再起動するだけで対処できます。

**スケーラビリティと一貫性:**  
- 環境固有の値(開発/ステージング/本番)を一元管理します。
- 設定更新のためのコード変更を必要としない一貫したデプロイメントパイプライン(CI/CD)をサポートします。

**プロセスの分離:**  
- 各プロセスは関連するシークレットのみにアクセスでき、偶発的な露出や権限昇格を軽減します。

**参考文献:**  
- [Microsoft Learn: Best practices for protecting secrets](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)  
- [OWASP: Centralize and Standardize Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#22-centralize-and-standardize)

## 環境変数の種類

### 1. システム環境変数
- OS レベルで設定されます。
- マシン上のすべてのプロセスとユーザーに影響します。
- 例: UnixやWindowsで`PATH`変数にディレクトリを追加する。

### 2. ユーザー環境変数
- 特定のユーザープロファイルにスコープされます。
- そのユーザーが起動したプロセスのみがこれらの変数にアクセスできます。
- 例: Windowsではコントロールパネルからユーザー環境変数を編集できます。

### 3. プロセス/実行時環境変数
- 特定のプロセスまたはセッションにスコープされます。
- セッションまたはプロセス起動時に一時的に設定されます。

### 4. ビルド時 vs. 実行時シークレット
- **ビルド時:** ビルド/コンパイルプロセス中に使用されます(例: 依存関係の取得)。
- **実行時:** アプリケーションの実行中に使用されます(例: ライブサービスへの接続)。

### 5. アプリケーション/プロジェクトレベル(.envファイル、シークレットマネージャー)
- `.env`ファイルはローカル開発用の環境変数を保存します。
- シークレットマネージャー(例: AWS Secrets Manager、Azure Key Vault、HashiCorp Vault)は、監査、アクセス制御、ローテーション機能を備えた暗号化ストレージを提供します。

### プラットフォームの違い
- **Windows:** コントロールパネル、CLI(`set`)、またはPowerShell(`$env:VAR_NAME`)で設定します。
- **Unix/Linux/macOS:** シェルで`export VAR=value`を使用するか、永続化のために`.bashrc`/`.zshrc`に追加します。

**参考文献:**  
- [DreamHost: Environment Variables Explained](https://www.dreamhost.com/blog/environment-variables/)  
- [Kinsta: Environment Variable Types](https://kinsta.com/blog/what-is-an-environment-variable/)

## 環境変数の使用方法

**ワークフロー:**
1. コードベースの外部でシークレットを定義します(OS、`.env`ファイル、シークレットマネージャー、デプロイメントダッシュボード)。
2. アプリケーションコードで環境変数APIを介してそれらを参照します。
3. アプリケーションをデプロイすると、シークレットが実行時に注入されます。

**例:**  
`API_KEY = "abc123"`とハードコーディングする代わりに、値を環境変数として設定し、アプリケーションが実行時に安全に読み取るようにします。

**自動シークレット注入:**  
- CI/CDでは、シークレットはビルド時またはデプロイ時に注入されることが多いです。
- シークレットマネージャーやデプロイメントダッシュボードは、シークレットの定義とローテーションのためのUI/APIを提供します。

**参考文献:**  
- [Render: Configure Environment Variables](https://render.com/docs/configure-environment-variables)  
- [OWASP: Automate Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#24-automate-secrets-management)

## 一般的なユースケースと例

- **APIキー:** 外部サービス(OpenAI、Google Cloud、Stripe)。
- **データベース認証情報:** DBユーザー名、パスワード、ホスト名を安全に渡します。
- **シークレットトークン:** JWT署名キー、OAuthクライアントシークレット、Webhookトークン。
- **機能フラグ:** 機能を動的に有効/無効にします。
- **環境タグ:** `development`、`staging`、または`production`を示します。

**.env の例:**
```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=postgres://user:pass@host:5432/db
MODE=production
```

**プラットフォームの例:**
- [Netlify Environment Variables](https://docs.netlify.com/configure-builds/environment-variables/)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## 環境変数の設定とアクセス

### OSレベルで

#### Unix/Linux/macOS

- 現在のセッションで設定:
  ```sh
  export API_KEY="abc123"
  ```
- 単一コマンドで設定:
  ```sh
  API_KEY="abc123" python app.py
  ```
- ユーザーに対して永続化:
  ```sh
  echo 'export API_KEY="abc123"' >> ~/.bashrc
  source ~/.bashrc
  ```

#### Windows

- 現在のセッションで設定(コマンドプロンプト):
  ```bat
  set API_KEY=abc123
  ```
- GUIで永続化:  
  コントロールパネル → システム → 詳細設定 → 環境変数
- PowerShell:
  ```powershell
  $env:API_KEY="abc123"
  ```

### アプリケーションコードで(.envファイル、シークレットマネージャー、プラットフォームダッシュボード)

#### .envファイル

- プロジェクトルートに`.env`ファイルを配置:
  ```
  API_KEY=abc123
  DB_PASS=supersecret
  ```
- **セキュリティ:** バージョン管理への偶発的なコミットを避けるため、常に`.env`を`.gitignore`に追加してください。

#### シークレットマネージャー

- **AWS Secrets Manager:** [公式ドキュメント](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- **Azure Key Vault:** [公式ドキュメント](https://learn.microsoft.com/en-us/azure/key-vault/)
- **HashiCorp Vault:** [公式ドキュメント](https://www.vaultproject.io/docs)
- シークレットは暗号化され、アクセス制御され、監査可能です。

#### プラットフォームダッシュボード

- **Render:** [Configure Environment Variables](https://render.com/docs/configure-environment-variables)
- **Netlify:** [Environment Variables](https://docs.netlify.com/configure-builds/environment-variables/)
- **Vercel:** [Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

### コード例: Node.js、Python、.NET

#### Node.js

- 環境変数へのアクセス:
  ```js
  // index.js
  console.log(process.env.API_KEY);
  ```
- dotenvを使用:
  ```js
  require('dotenv').config();
  const apiKey = process.env.API_KEY;
  ```

#### Python

- 環境変数へのアクセス:
  ```python
  import os
  api_key = os.environ.get('API_KEY')
  ```
- python-dotenvを使用:
  ```python
  from dotenv import load_dotenv
  load_dotenv()
  api_key = os.getenv('API_KEY')
  ```

#### .NET (C#)

- 環境変数へのアクセス:
  ```csharp
  var apiKey = Environment.GetEnvironmentVariable("API_KEY");
  ```
- ASP.NET Core User Secrets:
  1. シークレットの初期化:
     ```
     dotnet user-secrets init
     ```
  2. シークレットの設定:
     ```
     dotnet user-secrets set "Movies:ServiceApiKey" "12345"
     ```
  3. コードでのアクセス:
     ```csharp
     var builder = WebApplication.CreateBuilder(args);
     var movieApiKey = builder.Configuration["Movies:ServiceApiKey"];
     ```

**参考文献:**  
- [Microsoft Docs: Safe storage of app secrets in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [npm dotenv](https://www.npmjs.com/package/dotenv)

## シークレットの管理とローテーション

**シークレットのライフサイクル:**
- **複数のシークレットを設定:** `.env`ファイル、プラットフォームダッシュボード、またはシークレットマネージャーAPIを介してバッチ処理します。
- **シークレットのリスト表示:** CLIツール(例: `dotnet user-secrets list`)、ダッシュボード、API。
- **更新/ローテーション:** シークレットマネージャー、`.env`ファイル、またはダッシュボードで値を変更し、必要に応じてアプリを再デプロイ/再起動します。
- **削除/期限切れ:** 不要になったシークレットを削除または取り消します。期限切れのシークレットは削除する必要があります。

**自動ローテーション:**
- 可能な場合は、使用後またはセッション後に期限切れになる動的シークレット(例: Vault経由の一時的なDB認証情報)を使用します。
- シークレットマネージャー(例: AWS、Azure、HashiCorp Vault)でスケジュールされたローテーションを設定します。
- アプリケーションコードがシークレット変更時のホットリロードまたは優雅な再認証をサポートしていることを確認します。

**設定オブジェクトへのマッピング:**
- .NET: 構造化されたアクセスのためにシークレットをPOCOにマップします。
- Node.js/Python: 検証と集約のために設定ライブラリまたはカスタムラッパーを使用します。

**参考文献:**  
- [OWASP: Automated Secrets Rotation](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#24-automate-secrets-management)
- [Azure Key Vault: Secret Rotation](https://learn.microsoft.com/en-us/azure/key-vault/secrets/tutorial-rotation)

## セキュリティのベストプラクティス

- **シークレットをバージョン管理に保存しないでください。**
- **`.env`および類似のファイルを`.gitignore`に追加してください。**
- **本番環境ではプレーンテキストファイルではなくシークレットマネージャーを使用してください。**
- **最小権限の原則:** 必要な人だけにアクセスを制限します。
- **シークレットを定期的にローテーションおよび取り消します。**
- **すべてのシークレットアクセスを監査およびログ記録します。**
- **実行時シークレットをクライアント側コード(例: ブラウザJavaScript)に公開しないでください。**
- **CI/CDパイプラインでシークレットスキャンを自動化します:**
    - [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning)
    - [Azure DevOps Credential Scanner](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-secret-scanning)

- **保存時および転送中のシークレットを暗号化します。**
- **環境とサービスごとにシークレットを分離します。**
- **人間とシークレットの相互作用を最小限に抑え、自動化されたパイプラインを使用します。**

**参考文献:**  
- [OWASP: Access Control & Automation](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#23-access-control)
- [Microsoft Learn: Best practices for protecting secrets](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)

## 高度なシナリオ: 複数の環境、シークレットファイル、環境グループ

- **複数の環境:** `development`、`staging`、`production`用に個別の`.env`ファイルまたはシークレットセットを使用します。
- **シークレットファイル:** プラットフォームダッシュボード(例: Render、Vercel)を介してシークレットファイル(例: 秘密鍵)をアップロードします。
- **環境グループ:** マイクロサービスまたはマルチアプリデプロイメント用に変数をグループ化します。
- **一元化された設定:** 環境グループまたはシークレットマネージャーを使用して、チーム/サービス間でシークレットを共有します。

**アーキテクチャパターン:**
- **Kubernetes Sidecar:** サイドカーコンテナ(例: Vault Agent)を使用してシークレットを取得し、メインコンテナにマウントします([OWASP Example](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#example-1-kubernetes-with-a-sidecar-container))。
- **動的シークレット:** アプリケーションが起動時にシークレットを要求し、一時的で自動期限切れの認証情報を受け取ります。

## 制限事項と代替手段

**制限事項:**
- **プレーンテキストストレージ:** `.env`ファイルとOSレベルの変数はディスク上で暗号化されていません。
- **複雑な設定:** 環境変数でネストされた大規模な設定を構造化することは困難です。
- **手動同期:** 中央マネージャーなしでチーム/環境間でシークレットを配布することはエラーが発生しやすいです。

**代替手段:**
- **シークレットマネージャー:** AWS Secrets Manager、Azure Key Vault、HashiCorp Vault。
- **暗号化された設定ファイル:** 複雑な設定用(バージョン管理から除外する必要があります)。
- **プラットフォームツール:** デプロイメントダッシュボード(Render、Vercel、Netlify)を使用してシークレットを管理およびグループ化します。

**参考文献:**  
- [Azure Key Vault Overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
- [HashiCorp Vault Overview](https://www.vaultproject.io/docs)

## 重要なポイント

- 環境変数は、コードやUIに露出することなく、機密値をアプリに安全に注入します。
- 設定をコードから分離し、安全で柔軟なデプロイメントをサポートします。
- ローカル開発には`.env`ファイルを使用し(厳格な`.gitignore`で)、本番環境にはシークレットマネージャーまたはプラットフォームダッシュボードを使用します。
- シークレットをローテーションおよび監査し、クライアント側コードでログに記録したり公開したりしないでください。
- 分離のために環境とチームごとにシークレットを管理します。
- シークレットをソース管理にコミットせず、本番環境ではアクセス制御と暗号化を使用してください。

## 参考文献とさらなる読み物

- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Microsoft Learn: Best practices for protecting secrets](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)
- [Microsoft Docs: Safe storage of app secrets in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [Kinsta: What Is an Environment Variable?](https://kinsta.com/blog/what-is-an-environment-variable/)
- [DreamHost: Environment Variables Explained](https://www.dreamhost.com/blog/environment-variables/)
- [Render Docs: Environment Variables and Secrets](https://render.com/docs/configure-environment-variables)
- [Stack Overflow: How to store and access API keys and passwords with Gatsby?](https://stackoverflow.com/questions/62231572/how-to-store-and-access-api-keys-and-passwords-with-gatsby)
- [HashiCorp Vault Documentation](https://www.vaultproject.io/docs)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning)

## 例のシナリオ: 本番環境のAIチャットボット

外部LLM APIキーを必要とするAIチャットボットがあるとします。APIキーをコードベースに埋め込む代わりに、次のようにします:
1. プラットフォームの環境変数ダッシュボードまたはシークレットマネージャーにAPIキーを保存します。
2. アプリケーションは実行時に環境から`OPENAI_API_KEY`を読み取ります。
3. キーはユーザー、コード、ログに公開されることはありません。
4. ローテーションするには、ダッシュボード/シークレットマネージャーで更新し、再デプロイします—コード変更は不要です。

**Node.jsのサンプル:**
```js
require('dotenv').config();
const openai = require('openai');
openai.apiKey = process.env.OPENAI_API_KEY;
```
**Pythonのサンプル:**
```python
import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
```
**。NETのサンプル:**
```csharp
var builder = WebApplication.CreateBuilder(args);
var openAiApiKey = builder.Configuration["OPENAI_API_KEY"];
```

**参照:**  
- [Safe storage of app secrets in ASP.NET Core – Microsoft Docs](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [How to store and access API keys and passwords with Gatsby? – Stack Overflow](https://stackoverflow.com/questions/62231572/how-to-store-and-access-api-keys-and-passwords-with-gatsby)