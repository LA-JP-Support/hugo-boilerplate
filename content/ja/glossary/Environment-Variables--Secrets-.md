---
title: 環境変数(シークレット):詳細ガイド
translationKey: environment-variables-secrets
description: アプリケーションの安全な設定のための環境変数(シークレット)について学びます。APIキーやパスワードなどの機密データをコードから分離し、セキュリティと柔軟性を確保します。
keywords:
- 環境変数
- シークレット管理
- APIキー
- アプリケーションセキュリティ
- 設定管理
category: General
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: 'Environment Variables (Secrets): The Deep'
term: かんきょうへんすう(しーくれっと):しょうさいがいど
url: "/ja/glossary/Environment-Variables--Secrets-/"
---
## 環境変数(シークレット)とは何か?
環境変数は、外部で定義された名前付きキー・バリューペアで、アプリケーションに実行時設定を提供します。シークレットとして使用される場合、機密データ(APIキー、パスワード、データベース認証情報、トークン)をソースコードの外部に保存し、コードリポジトリやログを通じた偶発的な露出を防ぎます。この分離により、シークレットがバージョン管理、UI表示、またはアプリケーションログに明示的に必要とされない限り表示されないことが保証されます。

環境変数の値は、コード内のプレースホルダーとして機能します。`API_KEY = "secret123"`と記述する代わりに、`API_KEY`を参照します。これは実行環境において実行時にのみ存在します。このアプローチにより、コードコミット、リポジトリアクセス、またはログファイルを通じた認証情報漏洩のリスクが最小化されます。機密値は実行時に注入され、特別に設定されない限り視覚的インターフェースから隔離されたままです。

一般的なシークレットタイプには、データベースパスワード、APIトークン、OAuth認証情報、暗号化キー、機能フラグ、環境固有の設定値が含まれます。ウェブ、モバイル、クラウド、IoTなど、すべてのプラットフォームにわたる最新のアプリケーションは、開発、ステージング、本番環境全体で柔軟なデプロイメントを可能にしながらセキュリティを維持するために環境変数に依存しています。

## なぜシークレットに環境変数を使用するのか?

**コードと設定の分離**機密データをコードベースとバージョン管理から切り離すことで、同じコードが異なる環境で異なる認証情報を使用して実行できるようになります。開発、ステージング、本番環境はそれぞれ、コード変更なしに適切なシークレットを使用します。**セキュリティの強化**コードに埋め込まれたシークレットは、リポジトリアクセス、コード共有、または偶発的なコミットを通じて常に露出リスクに直面します。環境変数は、シークレットをコードベースの外部に保持することで、この攻撃ベクトルを排除します。エラーメッセージ、スタックトレース、デバッグ出力での露出を防ぎます。**運用の柔軟性**コードに触れることなくシークレットを更新またはローテーションできます。環境変数を変更してアプリケーションを再起動するだけで、新しい認証情報を実装できます。この俊敏性は、認証情報が漏洩した場合やローテーションが必要な場合の迅速なインシデント対応をサポートします。**デプロイメントの一貫性**CI/CDパイプラインは、デプロイメント中に自動的にシークレットを注入し、環境全体で一貫したプロセスを維持します。チームは手動の認証情報管理を回避し、人的エラーを削減します。**プロセスレベルの分離**各アプリケーションプロセスは関連するシークレットのみにアクセスし、1つのプロセスが侵害された場合の影響範囲を縮小します。きめ細かいアクセス制御により、権限昇格を防ぎます。

## 環境変数の種類

**システムレベル変数**オペレーティングシステムレベルで設定され、すべてのプロセスとユーザーに影響します。例として、Unixシステムの`PATH`ディレクトリやWindowsの環境設定があります。**ユーザースコープ変数**特定のユーザープロファイルに限定されます。そのユーザーによって起動されたプロセスのみがこれらの変数にアクセスでき、ユーザーレベルの分離を提供します。**プロセススコープ変数**個々のプロセスまたはセッションに対してのみ存在します。より広範なシステムに影響を与えることなく、特定のプロセスを起動する際に一時的に設定されます。**ビルド時とランタイムのシークレット**ビルド時シークレットは、コンパイルと依存関係の取得をサポートします。ランタイムシークレットは、実行中のアプリケーションが本番サービスやデータベースに接続できるようにします。**アプリケーションレベルの管理**`.env`ファイルは、ローカル開発用の変数を保存します。シークレットマネージャー(AWS Secrets Manager、Azure Key Vault、HashiCorp Vault)は、本番環境向けに監査証跡、アクセス制御、自動ローテーション機能を備えた暗号化ストレージを提供します。

## 一般的な使用例

**API統合**外部サービス(OpenAI、Google Cloud、Stripe、決済処理業者)は、ハードコードではなく環境変数を介して渡されるAPIキーを必要とします。**データベース接続**ユーザー名、パスワード、ホスト名を含む接続文字列は、安全かつ環境固有のままです。**認証トークン**JWT署名キー、OAuthクライアントシークレット、Webhook検証トークンは、ソースコードの外部で保護されます。**機能管理**機能フラグは、コードデプロイメントなしに環境全体で機能を制御します。**環境識別**`development`、`staging`、`production`などのタグが、アプリケーションの動作を適切に導きます。

## 実装アプローチ

### .envファイルを使用したローカル開発

プロジェクトルートに`.env`ファイルを作成します:

```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=postgres://user:pass@host:5432/db
MODE=production
```

**重要:**バージョン管理へのコミットを防ぐため、必ず`.env`を`.gitignore`に追加してください。

### Node.js実装

```javascript
require('dotenv').config();
const apiKey = process.env.API_KEY;
const dbUrl = process.env.DATABASE_URL;
```

### Python実装

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
db_url = os.getenv('DATABASE_URL')
```

### .NET実装

```csharp
var builder = WebApplication.CreateBuilder(args);
var apiKey = builder.Configuration["API_KEY"];

// ローカル開発用のUser Secretsを使用
// dotnet user-secrets init
// dotnet user-secrets set "Movies:ServiceApiKey" "12345"
var movieKey = builder.Configuration["Movies:ServiceApiKey"];
```

### オペレーティングシステムの設定

**Unix/Linux/macOS**```bash
# 現在のセッション
export API_KEY="abc123"

# 単一コマンド
API_KEY="abc123" python app.py

# 永続的(~/.bashrcまたは~/.zshrcに追加)
echo 'export API_KEY="abc123"' >> ~/.bashrc
source ~/.bashrc
```**Windows**```bat
# コマンドプロンプト
set API_KEY=abc123

# PowerShell
$env:API_KEY="abc123"

# 永続的: コントロールパネル → システム → 詳細設定 → 環境変数
```

## シークレット管理のベストプラクティス

**バージョン管理にシークレットを保存しない**Gitリポジトリは完全な履歴を保持します。コミットされたシークレットは、削除後もアクセス可能なままです。`.gitignore`を厳格に使用してください。**本番環境のシークレットマネージャー**AWS Secrets Manager、Azure Key Vault、HashiCorp Vaultは、本番環境に不可欠な暗号化、アクセスログ、自動ローテーション、コンプライアンス機能を提供します。**最小権限アクセス**シークレットへのアクセスを必要最小限の人員とシステムに制限します。ロールベースのアクセス制御を実装します。**定期的なローテーション**スケジュールまたはインシデント後にシークレットをローテーションします。シークレットマネージャーの機能や自動的に期限切れになる動的シークレットを使用して、可能な限り自動化します。**包括的な監査ログ**セキュリティ監視とコンプライアンス要件のために、すべてのシークレットアクセスを追跡します。**クライアント側の分離**ランタイムシークレット(データベースパスワード、APIキー)をブラウザJavaScriptに公開しないでください。外部サービスアクセスにはバックエンドプロキシを使用します。**自動セキュリティスキャン**CI/CDパイプラインにシークレットスキャンを実装し、偶発的なコミットがリポジトリに到達する前に検出します。**暗号化要件**ストレージシステムでの保存時およびネットワーク上での転送時にシークレットを暗号化します。**環境のセグメンテーション**開発、ステージング、本番環境用に個別のシークレットセットを維持し、環境間の汚染を防ぎます。

## 高度なパターン

**複数環境の管理**各環境に対して個別の`.env`ファイル(`.env.development`、`.env.production`)またはシークレットマネージャーの名前空間を使用します。**シークレットファイルの処理**プラットフォームダッシュボード(Render、Vercel、Netlify)は、秘密鍵や証明書などのシークレットファイル全体のアップロードをサポートしています。**マイクロサービスのシークレット共有**環境グループまたはシークレットマネージャーにより、セキュリティ境界を維持しながら、関連サービス間で設定を共有できます。**Kubernetesサイドカーパターン**Vault Agentをサイドカーコンテナとしてデプロイし、実行時にアプリケーションコンテナにシークレットを取得して注入します。**動的シークレット**アプリケーションはシークレットマネージャーから一時的な認証情報を要求し、時間制限付き露出によってセキュリティを強化する自動期限切れアクセストークンを受け取ります。

## セキュリティ上の考慮事項

**平文の制限**ローカルの`.env`ファイルとOSレベルの変数は、データを暗号化せずに保存します。開発には許容されますが、本番環境には不十分です。**設定の複雑さ**環境変数は、ネストされた階層的な設定に苦労します。複雑な構造には、暗号化された設定ファイルを検討してください。**配布の課題**チーム全体での手動のシークレット配布は、エラーとセキュリティギャップを引き起こします。集中型シークレットマネージャーがこの問題を解決します。**代替ソリューション**構造を必要とする複雑な設定には、プラットフォーム固有のシークレット管理ツールと組み合わせて、暗号化された設定ファイル(バージョン管理から除外)を使用します。

## 本番環境アーキテクチャの例

外部LLM APIアクセスを必要とするAIチャットボットを考えてみましょう:

1. シークレットマネージャーまたはプラットフォームダッシュボードにAPIキーを保存
2. アプリケーションは起動時に環境から`OPENAI_API_KEY`を読み取る
3. キーはコード、ログ、ユーザーインターフェースに表示されない
4. ローテーションには、シークレットマネージャーの値を更新して再デプロイするだけで済む
5. 開発、ステージング、本番環境で異なるキーを使用
6. 監査証跡がすべてのAPIキーアクセスを追跡

**Node.js:**```javascript
require('dotenv').config();
const { OpenAI } = require('openai');
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});
```**Python:**```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
```**C#:**```csharp
var builder = WebApplication.CreateBuilder(args);
var apiKey = builder.Configuration["OPENAI_API_KEY"];
```

## 重要なポイント

環境変数は、コードに機密データを埋め込むことなく、アプリケーションへの安全で柔軟なシークレット注入を提供します。設定を実装から分離し、環境固有の認証情報を使用して環境全体で同一のコードベースを可能にします。ローカル開発では、厳格な`.gitignore`保護を伴う`.env`ファイルを使用します。本番環境のデプロイメントでは、暗号化、アクセス制御、監査ログ、自動ローテーションを提供するシークレットマネージャーまたはプラットフォームダッシュボードを活用します。定期的なシークレットローテーション、包括的なログ、クライアント側の分離により、セキュリティ態勢を維持します。適切な実装により、迅速なデプロイメントとインシデント対応を可能にしながら、認証情報の漏洩を防ぎます。

## 参考文献


1. OWASP. (n.d.). Secrets Management Cheat Sheet. OWASP Cheat Sheets Series.

2. Microsoft. (n.d.). Best Practices for Protecting Secrets. Microsoft Learn.

3. Microsoft. (n.d.). Safe Storage of App Secrets in ASP.NET Core. Microsoft Docs.

4. Kinsta. (n.d.). What Is an Environment Variable?. Kinsta Blog.

5. DreamHost. (n.d.). Environment Variables Explained. DreamHost Blog.

6. Render. (n.d.). Environment Variables and Secrets. Render Documentation.

7. Netlify. (n.d.). Environment Variables. Netlify Documentation.

8. Vercel. (n.d.). Environment Variables. Vercel Documentation.

9. AWS. (n.d.). Secrets Manager Documentation. AWS Documentation.

10. Microsoft. (n.d.). Azure Key Vault Documentation. Microsoft Learn.

11. HashiCorp. (n.d.). Vault Documentation. HashiCorp Vault Documentation.

12. GitHub. (n.d.). Secret Scanning. GitHub Documentation.

13. Microsoft. (n.d.). Azure DevOps Credential Scanner. Microsoft Learn.

14. Stack Overflow. (n.d.). Storing API Keys with Gatsby. Stack Overflow.
