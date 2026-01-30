# SmartWeb Support Documentation Site

このディレクトリは、LotusDocs テーマを使用したサポートドキュメント専用サイトです。

## 📋 概要

- **目的**: サポートコンテンツを専用のドキュメントサイトとして提供
- **テーマ**: LotusDocs (https://github.com/colinwilson/lotusdocs)
- **URL**: https://support.smartweb.com (予定)
- **言語**: 日本語 (ja) / 英語 (en)

## 🏗️ ディレクトリ構造

```
support-docs/
├── content/
│   ├── ja/
│   │   └── docs/          # 日本語サポート記事
│   └── en/
│       └── docs/          # 英語サポート記事
├── themes/
│   └── lotusdocs/         # LotusDocs テーマ (git clone)
├── static/                # 静的ファイル (画像など)
├── hugo.toml              # Hugo設定ファイル
├── go.mod                 # Hugo Modules設定
└── README.md              # このファイル

## 🚀 ローカル開発

### サーバー起動

```bash
cd support-docs
hugo server --port 1314
```

アクセス: http://localhost:1314/

### ビルド

```bash
hugo --cleanDestinationDir
```

## 📝 コンテンツ管理

### 新規記事の作成

```bash
hugo new content/ja/docs/category/article-name.md
```

### フロントマター例

```yaml
---
title: "記事タイトル"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
description: "記事の説明"
keywords: ["キーワード1", "キーワード2"]
weight: 10
---
```

## 🔗 内部リンク

### サポート記事間のリンク (相対パス)

```markdown
[関連記事](/ja/docs/category/article-name/)
```

### メインサイトへのリンク (絶対URL)

```markdown
[用語集](https://smartweb.com/ja/glossary/machine-learning/)
[ブログ](https://smartweb.com/ja/blog/ai-introduction/)
```

## 🎨 LotusDocs 機能

- ✅ 左サイドバーナビゲーション
- ✅ 右サイドバー目次 (TOC)
- ✅ 検索機能
- ✅ ダークモード
- ✅ コードハイライト
- ✅ 多言語対応
- ✅ レスポンシブデザイン

## 📦 デプロイ

### GitHub Actions (予定)

`.github/workflows/deploy-support.yml` で自動デプロイ設定

### 手動デプロイ

```bash
hugo --cleanDestinationDir --minify
# public/ ディレクトリをサーバーにアップロード
```

## 🔧 設定

主要な設定は `hugo.toml` で管理:

- `baseURL`: サイトのベースURL
- `defaultContentLanguage`: デフォルト言語
- `params.docs`: LotusDocs固有の設定
- `languages`: 多言語設定

## 📊 統計

- **日本語記事**: 399ファイル
- **英語記事**: (移行予定)
- **カテゴリ**: 10+

## 🔄 メインサイトとの関係

### メインサイト (hugo-boilerplate/)
- ブログ
- 用語集
- サービス紹介
- 会社情報

### サポートサイト (support-docs/)
- サポート記事
- ヘルプドキュメント
- FAQ

## 📚 参考リンク

- [LotusDocs Documentation](https://lotusdocs.dev/docs/)
- [Hugo Documentation](https://gohugo.io/documentation/)
- [LotusDocs GitHub](https://github.com/colinwilson/lotusdocs)

## ⚠️ 注意事項

1. **Hugo Modules**: このサイトはHugo Modulesを使用しています
2. **Go必須**: `go` コマンドが必要です
3. **テーマ更新**: `hugo mod get -u` でテーマを更新
4. **コンテンツ同期**: メインサイトの `content/ja/support/` から移行済み

## 🛠️ トラブルシューティング

### モジュールエラー

```bash
hugo mod tidy
hugo mod get
```

### ビルドエラー

```bash
hugo --cleanDestinationDir --verbose
```

### キャッシュクリア

```bash
rm -rf resources/ public/
hugo --cleanDestinationDir
```
