# AWS Amplify モノレポ構成ガイド

## 概要

hugo-boilerplateリポジトリには2つのAmplifyアプリが含まれています：

| アプリ名               | ディレクトリ      | ドメイン                 | 用途                 |
|------------------------|-------------------|--------------------------|----------------------|
| smartweb               | `/` (ルート)      | `www.smartweb.jp`        | メインサイト         |
| smartweb-support-docs  | `/support-docs/`  | `support.smartweb.jp`    | サポートドキュメント |

## 設定ファイルの構成

```text
hugo-boilerplate/
├── amplify.yml                 ← モノレポ（smartweb / support-docs 両方）
└── support-docs/
    └── amplify.yml             ← 参照用（使っている場合はコンソール設定を優先確認）
```

### 重要：設定の管理方法

- **原則**: リポジトリの `/amplify.yml`（`applications` + `appRoot` のモノレポ構成）を権威として扱う
- **注意**: Amplifyコンソール側の Build spec / App root 設定が優先されるため、反映されない場合はコンソール設定を先に確認する

## Amplifyコンソールの設定

### smartweb（メインサイト）

- **App root**: `.` または空
- **ビルド設定**: `/amplify.yml` を使用

### smartweb-support-docs（サポートドキュメント）

- **App root**: `support-docs`
- **環境変数**: `AMPLIFY_MONOREPO_APP_ROOT` = `support-docs`
- **ビルド設定**: `/amplify.yml`（モノレポ設定）を参照

## 設定の優先順位

Amplifyは以下の順序で設定を探します：

1. **Amplifyコンソールの設定**（最優先）
2. **appRoot内のamplify.yml**
3. **ルートのamplify.yml**

⚠️ **重要**:

- コンソールに設定があると、リポジトリのamplify.ymlは無視されます
- コンソールのビルド設定は空にできません（エラーになる）
- 反映されない場合は、まずコンソールに残っている古いBuild specがないかを確認してください

## dev（ステージング）ブランチの運用

### 目的

- `dev` ブランチは **検索エンジンに載せない**（SEO事故防止）
- `dev` ブランチは **devのamplifyapp.comドメイン**を `baseURL` としてビルドし、production（www.smartweb.jp / support.smartweb.jp）への意図しないリダイレクトを避ける

### smartweb（メインサイト）の分岐（/amplify.yml）

`AWS_BRANCH` / `AWS_APP_ID` を使って、ビルド時に以下を切り替えます。

- `dev` のとき
  - `HUGO_ENV=staging`
  - `SITE_BASE_URL=https://dev.${AWS_APP_ID}.amplifyapp.com/`
  - `HUGO_SUPPORT_PORTAL_BASE_URL=https://dev.d2b65nc0n0a17p.amplifyapp.com/`
  - `public/robots.txt` を `Disallow: /` にする
- `main`（production）のとき
  - `HUGO_ENV=production`
  - `SITE_BASE_URL=https://www.smartweb.jp/`
  - `HUGO_SUPPORT_PORTAL_BASE_URL=https://support.smartweb.jp/`

### Hugoの getenv 制約（重要）

Amplify環境のHugoは、`getenv` の参照がセキュリティポリシーで制限されます。

- `^HUGO_` プレフィックスの環境変数は参照可能
- `HUGO_` 以外の環境変数は `access denied` でビルド失敗することがある

そのため、テンプレートから参照する変数は `HUGO_SUPPORT_PORTAL_BASE_URL` のように `HUGO_` プレフィックスを付けます。

参照箇所:

- `layouts/partials/header.html`
- `layouts/partials/footer.html`

### デプロイ後の検証（BasicAuth + curl）

AmplifyのBranch access control（BasicAuth）が有効な場合でも、ローカルの `.env` を使うと `curl` でHTMLを検証できます。

例（`.env` は Git 管理しない）:

```bash
AMPLIFY_DEV_USER=...
AMPLIFY_DEV_PASS=...

SMARTWEB_DEV_URL=https://dev.d35i77pd7clyhz.amplifyapp.com
SUPPORT_DOCS_DEV_URL=https://dev.d2b65nc0n0a17p.amplifyapp.com
```

smartweb（メインサイト）確認:

```bash
set -a; source .env; set +a

# noindex / canonical
curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SMARTWEB_DEV_URL/ja/" \
| grep -niE '<meta[^>]+name="robots"|noindex|rel="canonical"' | head -n 20

curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SMARTWEB_DEV_URL/en/" \
| grep -niE '<meta[^>]+name="robots"|noindex|rel="canonical"' | head -n 20

# production support ドメイン混入がないこと
curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SMARTWEB_DEV_URL/ja/" \
| grep -n 'support\.smartweb\.jp' | head -n 20

curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SMARTWEB_DEV_URL/en/" \
| grep -n 'support\.smartweb\.jp' | head -n 20

# dev support-docs を指していること
curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SMARTWEB_DEV_URL/ja/" \
| grep -n 'dev\.d2b65nc0n0a17p\.amplifyapp\.com' | head -n 20

curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SMARTWEB_DEV_URL/en/" \
| grep -n 'dev\.d2b65nc0n0a17p\.amplifyapp\.com' | head -n 20
```

support-docs（サポートドキュメント）確認:

```bash
set -a; source .env; set +a

curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SUPPORT_DOCS_DEV_URL/robots.txt" | cat
curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SUPPORT_DOCS_DEV_URL/ja/docs/" \
| grep -niE '<meta[^>]+name="robots"|noindex|rel="canonical"' | head -n 20
curl -sS -L -u "$AMPLIFY_DEV_USER:$AMPLIFY_DEV_PASS" "$SUPPORT_DOCS_DEV_URL/en/docs/" \
| grep -niE '<meta[^>]+name="robots"|noindex|rel="canonical"' | head -n 20
```

### ローカル確認（staging 相当で hugo server）

テンプレートの環境分岐（`hugo.IsProduction`）を本番と同条件にしないため、ローカルは `--environment staging` で起動します。

```bash
HUGO_SUPPORT_PORTAL_BASE_URL="https://dev.d2b65nc0n0a17p.amplifyapp.com/" \
hugo server --buildDrafts --buildFuture --disableFastRender \
  --environment staging --baseURL "http://localhost:1313/"
```

## ビルドコマンドの説明

### サポートドキュメント (Amplifyコンソールに設定)

Amplifyコンソール > App settings > Build settings に以下を設定：

```yaml
version: 1
applications:
  - appRoot: support-docs
    frontend:
      phases:
        preBuild:
          commands:
            - echo "Installing Go..."
            - wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
            - tar -xzf go1.21.5.linux-amd64.tar.gz
            - export PATH="$PWD/go/bin:$PATH"
            - export GOPATH="$PWD/go-workspace"
            - export GOCACHE="$PWD/go-cache"
            - mkdir -p "$GOPATH" "$GOCACHE"
            - go version
            - echo "Installing Hugo Extended..."
            - wget https://github.com/gohugoio/hugo/releases/download/v0.152.2/hugo_extended_0.152.2_Linux-64bit.tar.gz
            - tar -xzf hugo_extended_0.152.2_Linux-64bit.tar.gz
            - chmod +x hugo
            - export PATH="$PWD:$PATH"
            - hugo version
        build:
          commands:
            - echo "Building SmartWeb Support Documentation..."
            - export PATH="$PWD/go/bin:$PWD:$PATH"
            - export GOPATH="$PWD/go-workspace"
            - export GOCACHE="$PWD/go-cache"
            - hugo --minify --cleanDestinationDir
            - echo "Replacing root index.html with language selector..."
            - cp static/index.html public/index.html
            - echo "Adding glossary links..."
            - pip3 install beautifulsoup4 pyyaml --quiet
            - python3 scripts/linkbuilding_support_docs.py --linkbuilding-yaml data/linkbuilding/ja.yaml --public-dir public --language ja
            - python3 scripts/linkbuilding_support_docs.py --linkbuilding-yaml data/linkbuilding/en.yaml --public-dir public --language en
      artifacts:
        baseDirectory: public
        files:
          - "**/*"
      cache:
        paths:
          - resources/**/*
          - .hugo_cache/**/*
```

#### コマンドの意図

```yaml
build:
  commands:
    # Hugo ビルド
    - hugo --minify --cleanDestinationDir
    
    # 言語選択ページをルートにコピー
    - cp static/index.html public/index.html
    
    # 内部リンク処理（日本語・英語両方）
    - python3 scripts/linkbuilding_support_docs.py ... --language ja
    - python3 scripts/linkbuilding_support_docs.py ... --language en
```

## トラブルシューティング

### 設定変更が反映されない場合

1. **Amplifyコンソールの設定を確認**
   - App settings → Build settings
   - コンソールの設定が最優先される
   - コンソールの設定は空にできない（エラーになる）

2. **support-docsの設定を変更する場合**
   - Amplifyコンソールで直接編集する
   - 上記の完全なYAMLをコピー＆ペースト
   - Saveして再デプロイ

3. **再デプロイをトリガー**
   - 新しいコミットをpush、または
   - コンソールで「このバージョンを再デプロイ」

### ビルドログで確認すべきこと

正常なサポートドキュメントビルドでは、以下が表示される：

```text
Processing XXX HTML files in public/ja...
...
Processing XXX HTML files in public/en...
```

日本語版のみ表示される場合は、設定が古いままです。

## 関連ドキュメント

- [docs/00_START_HERE.md](docs/00_START_HERE.md) - プロジェクト概要
- [support-docs/docs/DEPLOYMENT_CHECKLIST.md](support-docs/docs/DEPLOYMENT_CHECKLIST.md) - デプロイチェックリスト
