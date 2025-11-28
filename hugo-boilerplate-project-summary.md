# Hugo-Boilerplateプロジェクト総合ドキュメント

## 🌟 プロジェクトサマリー

### プロジェクト概要
**Hugo-Boilerplate**は、SmartWeb/Interwork Corporation向けに開発された高性能な静的サイトジェネレーターテンプレートです。Hugo、Tailwind CSS、多言語対応、SEO最適化、自動ビルドシステムを統合した完全なWebサイトソリューションを提供します。

---

## 📊 主要コンポーネント一覧

### 1. フロントエンド技術スタック

| コンポーネント | バージョン | 用途 |
|------------|---------|------|
| Hugo | v0.80+ | 静的サイトジェネレーター |
| Tailwind CSS | 3.4+ | ユーティリティファーストCSS |
| PostCSS | 8.4+ | CSS処理パイプライン |
| Gulp | 5.0+ | タスクランナー |
| ESBuild | 0.25+ | JavaScript バンドラー |
| Inter Font | Variable | Webフォント |

### 2. ビルドツール設定

```javascript
// gulpfile.js 主要タスク
exports.css = buildCSS;      // CSS ビルド
exports.js = buildJS;        // JS ビルド
exports.build = build;       // 本番ビルド
exports.dev = dev;          // 開発サーバー
exports.watch = watch;      // ファイル監視
```

### 3. スクリプト一覧

| スクリプト名 | 言語 | 主要機能 |
|-----------|------|---------|
| build_content.sh | Bash | マスタービルドスクリプト |
| convert_tooltip_syntax.py | Python | ツールチップ構文変換 |
| linkbuilding.py | Python | 自動内部リンク生成 |
| translate_with_flowhunt.py | Python | 自動多言語翻訳 |
| generate_related_content.py | Python | 関連記事生成 |
| precompute_linkbuilding.py | Python | リンク最適化 |
| validate_tables.py | Python | Markdownテーブル検証 |
| preprocess-images.sh | Bash | 画像最適化 |

---

## 🚀 クイックスタートガイド

### 1. 環境セットアップ

```bash
# リポジトリクローン
git clone https://github.com/LA-JP-Support/hugo-boilerplate.git
cd hugo-boilerplate

# 依存関係インストール
npm install
pip3 install -r scripts/requirements.txt

# Hugo確認
hugo version
```

### 2. 開発サーバー起動

```bash
# Gulp開発サーバー（CSS/JS自動ビルド付き）
npm run dev

# または個別実行
gulp css    # CSS ビルド
gulp js     # JS ビルド
hugo server # Hugo サーバー
```

### 3. 本番ビルド

```bash
# フルビルドプロセス
./scripts/build_content.sh

# Hugo本番ビルド
hugo --minify
```

---

## 🏗️ プロジェクト構成詳細

### ディレクトリ構造

```
hugo-boilerplate/
├── 📁 assets/              # ソースファイル
│   ├── css/               # CSS ソース
│   │   ├── main.css      # メインエントリー
│   │   ├── tooltip.css   # ツールチップ
│   │   └── variables.css # CSS変数
│   └── js/               # JavaScript ソース
│       ├── main.js       # メインエントリー
│       ├── tooltip.js    # ツールチップ機能
│       └── lazy-loading.js # 遅延読み込み
│
├── 📁 content/            # コンテンツファイル
│   ├── ja/               # 日本語コンテンツ
│   │   ├── _index.md    # ホームページ
│   │   ├── blog/        # ブログ記事
│   │   └── privacy-policy.md
│   └── en/              # 英語コンテンツ
│       └── (同構造)
│
├── 📁 layouts/           # Hugoテンプレート
│   ├── _default/        # デフォルトレイアウト
│   ├── partials/        # 部分テンプレート
│   └── shortcodes/      # ショートコード
│       └── tooltip.html # ツールチップ
│
├── 📁 scripts/          # ビルドスクリプト
│   ├── build_content.sh
│   └── *.py            # Python スクリプト群
│
├── 📁 static/           # 静的ファイル
│   ├── css/            # ビルド済みCSS
│   ├── js/             # ビルド済みJS
│   └── images/         # 画像ファイル
│
├── 📄 hugo.toml        # Hugo設定
├── 📄 gulpfile.js      # Gulpタスク
├── 📄 package.json     # NPM設定
└── 📄 tailwind.config.js # Tailwind設定
```

---

## 🔧 主要機能詳細

### 1. ツールチップシステム

**実装方法:**
```markdown
# Markdownでの使用
{{< tooltip text="説明文" >}}用語{{< /tooltip >}}
```

**特徴:**
- Tailwind CSSベースのスタイリング
- デスクトップ：ホバー表示
- モバイル：タップ表示
- キーボード操作対応
- ARIA属性による アクセシビリティ

### 2. 多言語対応

**対応言語:** 日本語、英語（拡張可能）

**設定例 (hugo.toml):**
```toml
[languages.ja]
  languageName = "日本語"
  contentDir = "content/ja"
  weight = 1

[languages.en]
  languageName = "English"
  contentDir = "content/en"
  weight = 2
```

### 3. リンクビルディングシステム

**設定項目:**
- 最大リンク数/ページ: 50
- 最大リンク数/段落: 3
- キーワードごとの最大置換: 2
- 既存リンクスキップ: 有効

**処理フロー:**
1. キーワード定義（YAML/JSON）
2. HTMLコンテンツ解析
3. 自動リンク挿入
4. 密度制御
5. レポート生成

### 4. 画像最適化

**処理内容:**
- WebP自動変換
- レスポンシブサイズ生成（320w, 640w, 1024w, 1920w）
- 遅延読み込み実装
- 圧縮率: 85%

### 5. SEO最適化機能

**実装済み機能:**
- メタタグ自動生成
- Open Graph対応
- Twitter Card対応
- 構造化データ（Schema.org）
- XMLサイトマップ
- hreflangタグ（多言語）
- robots.txt

---

## 📈 パフォーマンス指標

### Core Web Vitals目標

| 指標 | 目標値 | 説明 |
|-----|-------|-----|
| LCP | < 2.5秒 | Largest Contentful Paint |
| FID | < 100ms | First Input Delay |
| CLS | < 0.1 | Cumulative Layout Shift |
| TTFB | < 600ms | Time to First Byte |

### 最適化技術

- **CSS最小化**: cssnano使用
- **JS最小化**: ESBuild使用
- **画像最適化**: WebP変換、遅延読み込み
- **キャッシュ戦略**: 長期キャッシュ設定
- **CDN活用**: CloudFront/Amplify

---

## 🚀 デプロイメント

### AWS Amplify設定

**amplify.yml例:**
```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm install
    build:
      commands:
        - npm run build
        - ./scripts/build_content.sh
        - hugo --minify
  artifacts:
    baseDirectory: public
    files:
      - '**/*'
```

**環境変数:**
```bash
HUGO_VERSION=0.120.0
NODE_VERSION=18
FLOWHUNT_API_KEY=<your-key>
```

---

## 🛠️ 開発ワークフロー

### 1. 新規記事作成

```bash
# 新規記事作成
hugo new ja/blog/new-article.md
hugo new en/blog/new-article.md

# フロントマター設定
---
title: "記事タイトル"
date: 2025-11-22
translationKey: "new-article"
description: "記事の説明"
keywords: ["キーワード1", "キーワード2"]
---
```

### 2. ツールチップ変換

```bash
# 既存コンテンツの一括変換
python scripts/convert_tooltip_syntax.py --dir content/ja/blog/
```

### 3. ビルド＆デプロイ

```bash
# ローカルテスト
npm run dev

# 本番ビルド
./scripts/build_content.sh
hugo --minify

# Gitプッシュ（Amplify自動デプロイ）
git add .
git commit -m "Update content"
git push origin main
```

---

## 📊 スクリプト実行統計

### build_content.sh 実行時間目安

| ステップ | 処理時間 | 備考 |
|---------|---------|------|
| sync_translations | ~5秒 | 翻訳キー同期 |
| build_hugo | ~30秒 | サイトビルド |
| translate | ~2分 | API呼び出し |
| generate_linkbuilding | ~1分 | キーワード生成 |
| apply_linkbuilding | ~2分 | リンク適用 |
| preprocess_images | ~3分 | 画像最適化 |
| **合計** | **~10分** | フルビルド |

---

## 🐛 トラブルシューティング

### よくある問題と解決方法

#### 1. ビルドエラー
```bash
# キャッシュクリア
rm -rf public/ resources/ static/css/* static/js/*
npm run build
```

#### 2. 翻訳エラー
```bash
# API キー確認
echo $FLOWHUNT_API_KEY

# .env ファイル作成
echo "FLOWHUNT_API_KEY=your-key" > scripts/.env
```

#### 3. リンクビルディングエラー
```bash
# Python環境再構築
rm -rf scripts/.venv
python3 -m venv scripts/.venv
source scripts/.venv/bin/activate
pip install -r scripts/requirements.txt
```

#### 4. 画像処理エラー
```bash
# ImageMagick確認
convert -version

# WebP ツール確認
cwebp -version
```

---

## 📚 ドキュメント一覧

| ドキュメント | 説明 |
|------------|------|
| README.md | プロジェクト概要 |
| SCRIPTS_README.md | スクリプト仕様 |
| hugo-boilerplate-technical-documentation.md | 技術仕様書 |
| hugo-boilerplate-scripts-documentation.md | スクリプト詳細 |
| PROJECT-COMPLETION.md | ツールチップシステム完成報告 |

---

## 🔄 更新・メンテナンス

### 定期メンテナンス項目

- [ ] 依存パッケージ更新（月次）
- [ ] セキュリティパッチ適用（随時）
- [ ] パフォーマンス測定（四半期）
- [ ] バックアップ確認（週次）
- [ ] ログファイル確認（日次）

### アップデート手順

```bash
# NPM パッケージ更新
npm update
npm audit fix

# Python パッケージ更新
pip install --upgrade -r scripts/requirements.txt

# Hugo 更新
brew upgrade hugo  # macOS
```

---

## 📞 サポート情報

### 開発チーム
- **組織**: SmartWeb/Interwork Corporation
- **リポジトリ**: https://github.com/LA-JP-Support/hugo-boilerplate
- **公開URL**: https://main.d1jtfhinlastnr.amplifyapp.com/

### 技術スタック バージョン要件
- Hugo: 0.80+
- Node.js: 14+
- Python: 3.6+
- Git: 2.0+

### ライセンス
GPL v2 or later

---

**最終更新日**: 2025年11月22日
