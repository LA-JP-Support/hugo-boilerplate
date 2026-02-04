# AWS Amplify モノレポ構成ガイド

## 概要

hugo-boilerplateリポジトリには2つのAmplifyアプリが含まれています：

| アプリ名 | ディレクトリ | ドメイン | 用途 |
|----------|-------------|----------|------|
| smartweb | `/` (ルート) | www.smartweb.jp | メインサイト |
| smartweb-support-docs | `/support-docs/` | support.smartweb.jp | サポートドキュメント |

## 設定ファイルの構成

```
hugo-boilerplate/
├── amplify.yml                 ← メインサイト専用
└── support-docs/
    └── amplify.yml             ← 参照用（実際はコンソールで管理）
```

### 重要：設定の管理方法

- **メインサイト**: `/amplify.yml` を使用
- **サポートドキュメント**: **Amplifyコンソールで管理**（コンソールの設定は空にできないため）

## Amplifyコンソールの設定

### smartweb（メインサイト）

- **App root**: `.` または空
- **ビルド設定**: `/amplify.yml` を使用

### smartweb-support-docs（サポートドキュメント）

- **App root**: `support-docs`
- **環境変数**: `AMPLIFY_MONOREPO_APP_ROOT` = `support-docs`
- **ビルド設定**: **Amplifyコンソールで直接設定**（必須）

## 設定の優先順位

Amplifyは以下の順序で設定を探します：

1. **Amplifyコンソールの設定**（最優先）
2. **appRoot内のamplify.yml**
3. **ルートのamplify.yml**

⚠️ **重要**: 
- コンソールに設定があると、リポジトリのamplify.ymlは無視されます
- コンソールのビルド設定は空にできません（エラーになる）
- support-docsは**Amplifyコンソールで設定を管理**してください

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

#### ビルドコマンドの説明

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
```
Processing XXX HTML files in public/ja...
...
Processing XXX HTML files in public/en...
```

日本語版のみ表示される場合は、設定が古いままです。

## 関連ドキュメント

- [docs/00_START_HERE.md](docs/00_START_HERE.md) - プロジェクト概要
- [support-docs/docs/DEPLOYMENT_CHECKLIST.md](support-docs/docs/DEPLOYMENT_CHECKLIST.md) - デプロイチェックリスト
