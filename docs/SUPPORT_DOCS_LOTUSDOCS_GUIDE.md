# Support Docs (LotusDocs) 運用ガイド

## 概要

このドキュメントは、SmartWeb サポートドキュメントサイト（LotusDocs ベース）の運用・設定・デプロイに関するガイドです。

**サイトURL**: https://main.d2b65nc0n0a17p.amplifyapp.com/
**リポジトリパス**: `/support-docs/`
**テーマ**: LotusDocs (git submodule)

---

## URL構造とSEO設計

### 多言語URL構造

```
https://main.d2b65nc0n0a17p.amplifyapp.com/
├── index.html          ← 言語選択ページ（noindex）
├── /ja/
│   └── docs/           ← 日本語ドキュメント（インデックス対象）
├── /en/
│   └── docs/           ← 英語ドキュメント（インデックス対象）
└── sitemap.xml
```

### 重要な設定（hugo.toml）

```toml
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = true    # /ja/, /en/ サブディレクトリを使用
disableDefaultLanguageRedirect = true    # ルートの自動リダイレクトを無効化
```

**なぜこの設定が必要か:**
- `disableDefaultLanguageRedirect = true` により、ルート (`/`) に言語選択ページを表示
- Googleは自動リダイレクト（IP/ブラウザ言語ベース）を推奨しないため、明示的な言語選択を提供
- 各言語ページには hreflang タグで相互リンクを設定

### ルート言語選択ページ

**ファイル**: `static/index.html`

このファイルはビルド時に `public/index.html` にコピーされ、以下の役割を果たします：
- 言語選択ボタン（日本語/英語）を提供
- `noindex, follow` でSEO除外（インデックスされない）
- hreflang タグで各言語版へのリンクを明示
- `x-default` で言語に依存しないデフォルトページを指定

---

## hreflangタグ設定

### 実装場所

**ファイル**: `layouts/partials/head.html`

```html
<!-- Hreflang tags for multilingual SEO -->
{{ if .IsTranslated }}
  {{ range .Translations }}
  <link rel="alternate" hreflang="{{ .Lang }}" href="{{ .Permalink }}" />
  {{ end }}
  <link rel="alternate" hreflang="{{ .Lang }}" href="{{ .Permalink }}" />
{{ end }}
<link rel="alternate" hreflang="x-default" href="{{ .Site.BaseURL }}" />
```

### チェックポイント

- [ ] 各言語ページが相互にリンクしている（リターンリンク）
- [ ] `x-default` が設定されている
- [ ] canonical タグが正しく設定されている

---

## 内部リンク（用語集リンク）

### 仕組み

サポートドキュメント内のテキストから、メインサイト（smartweb.jp）の用語集へ自動的にリンクを作成します。

### 設定ファイル

| ファイル | 用途 |
|----------|------|
| `data/linkbuilding/ja.yaml` | 日本語キーワード定義 |
| `data/linkbuilding/en.yaml` | 英語キーワード定義 |
| `scripts/linkbuilding_support_docs.py` | リンク追加スクリプト |

### amplify.yml のビルドコマンド

```yaml
build:
  commands:
    - hugo --minify --cleanDestinationDir
    - cp static/index.html public/index.html
    - pip3 install beautifulsoup4 pyyaml --quiet
    - python3 scripts/linkbuilding_support_docs.py --linkbuilding-yaml data/linkbuilding/ja.yaml --public-dir public --language ja
    - python3 scripts/linkbuilding_support_docs.py --linkbuilding-yaml data/linkbuilding/en.yaml --public-dir public --language en
```

### 英語版キーワードの注意点

英語版の内部リンクを正しく機能させるため、以下の点に注意：

1. **キーワードのバリエーション**: 単数形/複数形、大文字/小文字のバリエーションを追加
2. **exact フラグ**: `exact: false` で柔軟なマッチングを許可
3. **priority**: 高頻度キーワードは優先度を高く設定（15程度）

**例:**
```yaml
- keyword: AI chatbots
  url: /en/glossary/ai-chatbot/
  exact: false
  priority: 15
  title: AI Chatbot - Intelligent conversational agents...
- keyword: chatbots
  url: /en/glossary/chatbot/
  exact: false
  priority: 14
  title: Chatbot - A software application...
```

---

## デプロイチェックリスト

### デプロイ前

- [ ] `hugo server` でローカル確認
- [ ] 言語選択ページ（`static/index.html`）の更新があれば反映
- [ ] `en.yaml` / `ja.yaml` のキーワード追加があれば確認

### デプロイ後

- [ ] ルートURL (`/`) で言語選択ページが表示されることを確認
- [ ] 各言語ページでhreflangタグが正しく出力されていることを確認
- [ ] 内部リンク（`data-lb="1"` 属性付き）が追加されていることを確認
- [ ] PageSpeed Insightsでモバイルテスト実行

### 確認コマンド（ブラウザコンソール）

```javascript
// 内部リンクの数を確認
document.querySelectorAll('a[data-lb="1"]').length

// hreflangタグを確認
document.querySelectorAll('link[hreflang]')
```

---

## ファイル構造

```
support-docs/
├── amplify.yml                     # AWS Amplifyビルド設定
├── hugo.toml                       # Hugo設定
├── content/
│   ├── ja/
│   │   ├── _index.md              # 日本語ルート（→/ja/docs/へリダイレクト）
│   │   └── docs/                   # 日本語ドキュメント
│   └── en/
│       ├── _index.md              # 英語ルート（→/en/docs/へリダイレクト）
│       └── docs/                   # 英語ドキュメント
├── data/
│   └── linkbuilding/
│       ├── ja.yaml                 # 日本語内部リンクキーワード
│       └── en.yaml                 # 英語内部リンクキーワード
├── layouts/
│   └── partials/
│       └── head.html              # カスタムhead（hreflang含む）
├── scripts/
│   └── linkbuilding_support_docs.py
├── static/
│   └── index.html                  # 言語選択ページ
└── themes/
    └── lotusdocs/                  # テーマ（git submodule）
```

---

## トラブルシューティング

### ルートで言語選択ページが表示されない

1. `hugo.toml` で `disableDefaultLanguageRedirect = true` が設定されているか確認
2. `amplify.yml` で `cp static/index.html public/index.html` が実行されているか確認
3. ブラウザキャッシュをクリア

### 英語版の内部リンクが作成されない

1. `en.yaml` にキーワードが定義されているか確認
2. キーワードが実際のコンテンツテキストと一致するか確認（大文字/小文字、単数/複数形）
3. `exact: false` で柔軟なマッチングを有効化
4. ビルドログでスクリプトのエラーを確認

### hreflangタグが出力されない

1. `layouts/partials/head.html` が存在し、hreflangコードが含まれているか確認
2. 対応する翻訳ページ（`translationKey` が一致）が存在するか確認

---

## 変更履歴

### 2026-02-04
- `disableDefaultLanguageRedirect = true` 追加（ルート言語選択ページ対応）
- `layouts/partials/head.html` 作成（hreflang + canonical + Critical CSS統合）
- `static/index.html` デザイン改善
- `en.yaml` に高頻度キーワードバリエーション追加
- 本ドキュメント作成
