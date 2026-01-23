# Hugo-Boilerplateプロジェクト 技術仕様書

## 📋 目次

1. [プロジェクト概要](#1-プロジェクト概要)
2. [プロジェクト構造](#2-プロジェクト構造)
3. [ビルドシステム](#3-ビルドシステム)
4. [スクリプト詳細](#4-スクリプト詳細)
5. [フロントエンド実装](#5-フロントエンド実装)
6. [コンテンツ管理](#6-コンテンツ管理)
7. [ツールチップシステム](#7-ツールチップシステム)
8. [多言語対応](#8-多言語対応)
9. [SEO最適化](#9-seo最適化)
10. [デプロイメント](#10-デプロイメント)

---

## 1. プロジェクト概要

### プロジェクト基本情報
- **プロジェクト名**: Hugo-Boilerplate Site (SmartWeb/Interwork Corporation)
- **フレームワーク**: Hugo Static Site Generator
- **ホスティング**: AWS Amplify
- **リポジトリ**: LA-JP-Support/hugo-boilerplate (GitHub)
- **開発環境**: macOS (複数Mac環境対応)
- **バージョン管理**: Git/GitHub Desktop

### 主要技術スタック
- **静的サイトジェネレーター**: Hugo v0.80+
- **CSSフレームワーク**: Tailwind CSS 3.4+
- **ビルドツール**: Gulp 5.0 + ESBuild
- **スクリプト言語**: Python 3.6+ / Bash
- **パッケージマネージャー**: npm

---

## 2. プロジェクト構造

```
hugo-boilerplate/
├── archetypes/          # コンテンツテンプレート
├── assets/              # 未処理のアセット（CSS/JS）
│   ├── css/
│   │   ├── main.css    # メインCSSエントリー
│   │   ├── tooltip.css # ツールチップスタイル
│   │   └── ...
│   └── js/
│       ├── main.js     # メインJSエントリー
│       ├── tooltip.js  # ツールチップ機能
│       └── ...
├── content/            # マークダウンコンテンツ
│   ├── ja/            # 日本語コンテンツ
│   └── en/            # 英語コンテンツ
├── data/              # データファイル
├── i18n/              # 翻訳ファイル
├── layouts/           # Hugoテンプレート
│   ├── _default/
│   ├── partials/
│   └── shortcodes/    # カスタムショートコード
├── scripts/           # ビルド・処理スクリプト
│   ├── build_content.sh
│   ├── convert_tooltip_syntax.py
│   ├── linkbuilding.py
│   └── ...
├── static/            # 静的ファイル
├── themes/            # テーマファイル
├── gulpfile.js        # Gulpタスク定義
├── hugo.toml         # Hugo設定
├── package.json      # Node依存関係
├── postcss.config.js # PostCSS設定
└── tailwind.config.js # Tailwind設定
```

---

## 3. ビルドシステム

### 3.1 Gulpタスク (gulpfile.js)

**主要タスク:**

```javascript
// CSSビルド
function buildCSS() {
  return gulp.src('assets/css/main.css')
    .pipe(postcss([
      postcssImport,    // @import解決
      tailwindcss,      // Tailwind処理
      autoprefixer,     // ベンダープレフィックス
      cssnano()         // 圧縮
    ]))
    .pipe(gulp.dest('static/css'));
}

// JavaScriptビルド
function buildJS() {
  return esbuild.build({
    entryPoints: ['assets/js/main.js'],
    bundle: true,      // バンドル化
    minify: true,      // 圧縮
    format: 'iife',    // 即時実行関数
    outdir: 'static/js'
  });
}

// 開発サーバー
function startHugoServer() {
  const hugo = spawn('hugo', [
    'server', 
    '--buildDrafts', 
    '--buildFuture', 
    '--disableFastRender'
  ]);
}
```

**使用コマンド:**

```bash
npm run dev     # 開発サーバー起動
npm run build   # 本番ビルド
npm run watch   # ファイル監視
```

### 3.2 PostCSS設定 (postcss.config.js)

```javascript
module.exports = {
  plugins: {
    'postcss-import': {},
    tailwindcss: {},
    autoprefixer: {},
    cssnano: process.env.NODE_ENV === 'production' ? {} : false
  }
}
```

### 3.3 Tailwind設定 (tailwind.config.js)

**主要設定:**

```javascript
module.exports = {
  darkMode: 'class',
  content: [
    './layouts/**/*.html',
    '../../layouts/**/*.html',
    '../**/layouts/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      colors: {
        primary: {
          // カスタムカラーパレット
          50: 'rgb(var(--color-primary-50) / <alpha-value>)',
          // ... 100-950
        },
        'button-primary': {
          DEFAULT: 'rgb(var(--color-button-primary) / <alpha-value>)',
          hover: 'rgb(var(--color-button-primary-hover) / <alpha-value>)',
          // ...
        }
      }
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
```

---

## 4. スクリプト詳細

### 4.1 ビルドコンテンツスクリプト (build_content.sh)

**主要機能:**
1. Python仮想環境の作成・管理
2. 翻訳同期
3. Hugo静的サイトビルド
4. 画像最適化
5. リンクビルディング
6. 関連コンテンツ生成

**実行ステップ:**

```bash
# 全ステップ実行
./scripts/build_content.sh

# 特定ステップのみ
./scripts/build_content.sh --step translate
./scripts/build_content.sh --step generate_related_content

# 複数ステップ
./scripts/build_content.sh --steps sync_translations,build_hugo
```

**利用可能なステップ:**
- `sync_translations` - 翻訳キー同期
- `build_hugo` - Hugoサイトビルド
- `offload_images` - 画像オフロード
- `find_duplicate_images` - 重複画像検出
- `translate` - FlowHunt API翻訳
- `sync_content_attributes` - コンテンツ属性同期
- `sync_translation_urls` - 翻訳URL同期
- `generate_amplify_redirects` - Amplifyリダイレクト生成
- `generate_linkbuilding_keywords` - リンクビルディングキーワード生成
- `generate_related_content` - 関連コンテンツ生成
- `extract_automatic_links` - 自動リンク抽出
- `precompute_linkbuilding` - リンクビルディング最適化
- `apply_linkbuilding` - リンクビルディング適用
- `preprocess_images` - 画像前処理

### 4.2 ツールチップ構文変換 (convert_tooltip_syntax.py)

**変換パターン:**

```markdown
# 変換前
**人工知能**（説明：コンピュータが人間のように考えたり判断したりする技術）

# 変換後
{{< tooltip text="コンピュータが人間のように考えたり判断したりする技術" >}}人工知能{{< /tooltip >}}
```

**主要機能:**
- 正規表現によるパターンマッチング
- バックアップ自動作成
- ディレクトリ一括処理
- エスケープ処理（`"` → `&quot;`）

**使用方法:**

```bash
# 単一ファイル変換
python convert_tooltip_syntax.py --input file.md

# ディレクトリ一括変換
python convert_tooltip_syntax.py --dir content/ja/blog/

# バックアップなし
python convert_tooltip_syntax.py --dir content/ja/blog/ --no-backup
```

### 4.3 リンクビルディング (linkbuilding.py / linkbuilding_parallel.py)

**主要機能:**
- キーワードベースの自動内部リンク生成
- 並列処理による高速化
- カスタマイズ可能な設定
- リンク密度制御

**設定項目 (LinkConfig):**

```python
@dataclass
class LinkConfig:
    max_replacements_per_keyword: int = 2
    max_replacements_per_url: int = 2
    max_replacements_per_keyword_url: int = 1
    max_links_on_page: int = 50
    max_replacements_per_page: int = 30
    max_replacements_per_paragraph: int = 3
    min_chars_between_links: int = 1
    min_paragraph_length: int = 30
    max_paragraph_density: int = 30
    skip_existing_links: bool = True
    preserve_case: bool = True
    add_title_attribute: bool = True
```

**並列処理実装:**

```python
# linkbuilding_parallel.py
max_workers = 8  # 並列ワーカー数
with ProcessPoolExecutor(max_workers=max_workers) as executor:
    futures = []
    for lang_code in languages:
        future = executor.submit(process_language, lang_code, args)
        futures.append(future)
```

---

## 5. フロントエンド実装

### 5.1 CSS構造

**main.css:**

```css
/* インポート順序が重要 */
@import "./variables.css";      /* CSS変数定義 */
@import "./fonts.css";          /* フォント定義 */
@import "./typewriter.css";     /* タイプライター効果 */
@import "./lazy-images.css";    /* 遅延読み込み画像 */
@import "./lazy-videos.css";    /* 遅延読み込み動画 */
@import "./tooltip.css";        /* ツールチップ */

/* Tailwindレイヤー */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* カスタムコンポーネント */
@layer components {
  .wrapper {
    @apply max-w-7xl mx-auto px-4 sm:px-6 lg:px-8;
  }
  .wrapper-narrow {
    @apply max-w-4xl mx-auto px-4 sm:px-6 lg:px-8;
  }
}
```

### 5.2 JavaScript構造

**main.js (エントリーポイント):**

```javascript
// モジュールインポート
import './lazy-loading.js';        // 遅延読み込み
import './lazy-videos.js';         // 動画遅延読み込み
import './banner-dismiss.js';      // バナー閉じる機能
import './cookie-consent.js';      // Cookie同意
import './copyToClipboard.js';     // クリップボードコピー
import './typewriter.js';          // タイプライター効果
import './tooltip.js';             // ツールチップ
import './dynamic-font-sizing.js'; // 動的フォントサイズ
```

### 5.3 レスポンシブデザイン

**ブレークポイント (Tailwind標準):**
- `sm`: 640px以上
- `md`: 768px以上
- `lg`: 1024px以上
- `xl`: 1280px以上
- `2xl`: 1536px以上

---

## 6. コンテンツ管理

### 6.1 コンテンツ構造

```
content/
├── ja/                    # 日本語コンテンツ
│   ├── _index.md         # トップページ
│   ├── blog/             # ブログ記事
│   │   └── article.md
│   └── privacy-policy.md
└── en/                    # 英語コンテンツ
    ├── _index.md
    ├── blog/
    └── privacy-policy.md
```

### 6.2 フロントマター

```yaml
---
title: "記事タイトル"
date: 2025-11-19
draft: false
translationKey: "article-key"  # 言語間リンク用
description: "記事の説明"
keywords: ["キーワード1", "キーワード2"]
image: "/images/blog/image.jpg"
tags: ["タグ1", "タグ2"]
categories: ["カテゴリー"]
---
```

---

## 7. ツールチップシステム

### 7.1 実装詳細

**ショートコード (tooltip.html):**

```html
{{- $text := .Get "text" -}}
{{- $content := .Inner -}}
<span class="tooltip-wrapper group relative inline-block" 
      role="tooltip" 
      aria-expanded="false"
      data-tooltip-text="{{ $text }}">
  <span class="tooltip-term">{{ $content | markdownify }}</span>
  <span class="tooltip">{{ $text | markdownify }}</span>
</span>
```

**JavaScript実装 (tooltip.js):**

```javascript
const TooltipSystem = {
    settings: {
        touchDevice: false,
        initialized: false,
        mobileBreakpoint: 768,
        activeTooltip: null,
        breakpoint: window.matchMedia('(max-width: 768px)')
    },
    
    init: function() {
        this.detectTouchDevice();
        this.setup();
        this.bindEvents();
    },
    
    detectTouchDevice: function() {
        this.settings.touchDevice = (
            'ontouchstart' in window ||
            navigator.maxTouchPoints > 0
        );
    },
    
    bindEvents: function() {
        if (!this.settings.touchDevice) {
            this.bindDesktopEvents();  // ホバーイベント
        } else {
            this.bindMobileEvents();   // タッチイベント
        }
        this.bindKeyboardEvents();     // キーボード操作
    }
};
```

**CSS実装 (tooltip.css):**

```css
/* デスクトップ: Tailwind group-hoverで制御 */
.tooltip-wrapper .tooltip {
  @apply invisible opacity-0 absolute bottom-full left-1/2 
         transform -translate-x-1/2 -translate-y-2
         transition-all duration-200;
}

.tooltip-wrapper:hover .tooltip,
.group:hover .tooltip {
  @apply visible opacity-100;
}

/* モバイル: JavaScript制御 */
@media (max-width: 768px) {
  .tooltip-wrapper.active .tooltip {
    @apply visible opacity-100 fixed top-1/2 left-1/2 
           transform -translate-x-1/2 -translate-y-1/2 z-[9999];
  }
}
```

---

## 8. 多言語対応

### 8.1 Hugo設定 (hugo.toml)

```toml
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = true

[languages]
  [languages.ja]
    languageName = "日本語"
    title = "SmartWeb"
    weight = 1
    contentDir = "content/ja"
    [languages.ja.params]
      bcp47Lang = "ja"
      description = "次世代のWeb体験をあなたに"
  
  [languages.en]
    languageName = "English"
    title = "SmartWeb"
    weight = 2
    contentDir = "content/en"
    [languages.en.params]
      bcp47Lang = "en"
      description = "Next-generation web experience"
```

### 8.2 翻訳ファイル構造

```
i18n/
├── ja.yaml
└── en.yaml
```

**ja.yaml例:**

```yaml
read_more:
  other: "続きを読む"
  
posted_on:
  other: "投稿日"
  
by_author:
  other: "著者"
```

### 8.3 言語切り替え実装

```html
<!-- layouts/partials/language-switcher.html -->
{{ range $.Site.Home.AllTranslations }}
  <a href="{{ .Permalink }}" 
     class="language-link {{ if eq .Language $.Language }}active{{ end }}">
    {{ .Language.LanguageName }}
  </a>
{{ end }}
```

---

## 9. SEO最適化

### 9.1 メタタグ生成

```html
<!-- layouts/partials/head.html -->
<meta name="description" content="{{ .Description | default .Site.Params.description }}">
<meta name="keywords" content="{{ delimit .Keywords ", " }}">

<!-- Open Graph -->
<meta property="og:title" content="{{ .Title }}">
<meta property="og:description" content="{{ .Description }}">
<meta property="og:image" content="{{ .Params.image | absURL }}">
<meta property="og:url" content="{{ .Permalink }}">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ .Title }}">
<meta name="twitter:description" content="{{ .Description }}">
<meta name="twitter:image" content="{{ .Params.image | absURL }}">

<!-- hreflangタグ -->
{{ range .AllTranslations }}
  <link rel="alternate" hreflang="{{ .Lang }}" href="{{ .Permalink }}">
{{ end }}
```

### 9.2 サイトマップ生成

```xml
<!-- layouts/index.sitemap.xml -->
{{ printf "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>" | safeHTML }}
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  {{ range .Data.Pages }}
    <url>
      <loc>{{ .Permalink }}</loc>
      <lastmod>{{ safeHTML .Lastmod.Format "2006-01-02T15:04:05-07:00" }}</lastmod>
      {{ with .Sitemap.ChangeFreq }}<changefreq>{{ . }}</changefreq>{{ end }}
      {{ if ge .Sitemap.Priority 0.0 }}<priority>{{ .Sitemap.Priority }}</priority>{{ end }}
      {{ range .AllTranslations }}
        <xhtml:link rel="alternate" hreflang="{{ .Language.Lang }}" href="{{ .Permalink }}"/>
      {{ end }}
    </url>
  {{ end }}
</urlset>
```

### 9.3 構造化データ

```html
<!-- layouts/partials/schema.html -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{ .Title }}",
  "image": "{{ .Params.image | absURL }}",
  "datePublished": "{{ .PublishDate.Format "2006-01-02" }}",
  "dateModified": "{{ .Lastmod.Format "2006-01-02" }}",
  "author": {
    "@type": "Person",
    "name": "{{ .Params.author | default .Site.Params.author }}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{{ .Site.Title }}",
    "logo": {
      "@type": "ImageObject",
      "url": "{{ "/images/logo.png" | absURL }}"
    }
  },
  "description": "{{ .Description }}"
}
</script>
```

---

## 10. デプロイメント

### 10.1 AWS Amplify設定

**amplify.yml:**

```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm install
        - pip3 install -r scripts/requirements.txt
    build:
      commands:
        - npm run build
        - ./scripts/build_content.sh
        - hugo --minify
  artifacts:
    baseDirectory: public
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
      - scripts/.venv/**/*
```

### 10.2 環境変数

```bash
# AWS Amplify環境変数
HUGO_VERSION=0.120.0
NODE_VERSION=18
FLOWHUNT_API_KEY=your-api-key
```

### 10.3 リダイレクト設定

```json
[
  {
    "source": "/ja",
    "target": "/",
    "status": "301",
    "condition": null
  },
  {
    "source": "/<*>",
    "target": "/index.html",
    "status": "404-200",
    "condition": null
  }
]
```

---

## 付録A: トラブルシューティング

### よくある問題と解決方法

**1. ビルドエラー**
```bash
# キャッシュクリア
rm -rf public/ resources/
npm run build
hugo --cleanDestinationDir
```

**2. 言語切り替えが機能しない**
- `translationKey`が全言語ファイルで一致しているか確認
- ファイル名が同一か確認（`-en`サフィックスを避ける）

**3. ツールチップが表示されない**
```bash
# CSSとJSの再ビルド
gulp css
gulp js
```

**4. リンクビルディングエラー**
```bash
# 仮想環境の再構築
rm -rf scripts/.venv
./scripts/build_content.sh
```

---

## 付録B: パフォーマンス最適化

### 1. 画像最適化

- WebP形式への自動変換
- レスポンシブ画像の生成
- 遅延読み込みの実装

### 2. CSS/JS最小化

- PostCSS cssnanoによるCSS圧縮
- ESBuildによるJavaScript圧縮
- 未使用CSSの削除（PurgeCSS）

### 3. キャッシュ戦略

- 静的アセットの長期キャッシュ
- HTMLの短期キャッシュ
- CDN活用（CloudFront）

### 4. Core Web Vitals最適化

- LCP（Largest Contentful Paint）: < 2.5秒
- FID（First Input Delay）: < 100ms
- CLS（Cumulative Layout Shift）: < 0.1

### 5. Google Fonts最適化（2025-01更新）

**問題**: Google Fontsがレンダリングをブロック（-620ms影響）

**解決策**: media="print" onload方式で非同期読み込み

```html
<!-- layouts/partials/head.html -->
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?...">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?..." 
      media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?..."></noscript>
```

### 6. YouTube埋め込み最適化（2025-01更新）

**問題**: YouTube iframeが777 KiBのJavaScriptを読み込み、TBT +490ms

**解決策**: Lite YouTube方式（クリック時にのみiframe読み込み）

**変更ファイル**:
- `/layouts/shortcodes/youtube.html` - Lite YouTube対応
- `/layouts/partials/sections/features/with_alternating_sections.html`
- `/static/js/app.js` - 初期化スクリプト

**使用方法**:
```markdown
{{</* youtube videoID="frmB19r0k58" */>}}  <!-- Lite YouTube -->
{{</* youtube videoID="frmB19r0k58" autoload=true */>}}  <!-- 従来方式 -->
```

**注意**: 再生回数は正常にカウントされます

### 7. クリティカルCSS（2025-01更新）

**問題**: CSSがレンダリングをブロック

**解決策**: フォントフォールバックと初期レイアウトCSSをインライン化

```html
<!-- layouts/partials/head.html -->
<style>
@font-face {
  font-family: 'Inter';
  font-display: swap;
  src: url('/fonts/inter/Inter-VariableFont_opsz,wght.woff2') format('woff2');
}
.font-sans { font-family: Inter, 'Noto Sans JP', system-ui, sans-serif; }
.font-serif, .font-mincho { font-family: 'Noto Serif JP', Georgia, serif; }
</style>
```

### 8. PageSpeed最適化結果サマリー

| 指標 | 改善前 | 改善後 | 効果 |
|------|--------|--------|------|
| パフォーマンススコア | 53 | 75-85 | +20-30pt |
| LCP | 3.3s | ~1.5s | -55% |
| TBT | 490ms | ~50ms | -90% |
| FCP | 1.6s | ~1.0s | -38% |

**詳細**: [PAGESPEED-OPTIMIZATION.md](./PAGESPEED-OPTIMIZATION.md)

---

## 更新履歴

- **2025-01-23**: PageSpeed最適化（Google Fonts非同期化、Lite YouTube、クリティカルCSS）
- **2025-11-22**: 初版作成
- **2025-11-20**: ツールチップシステム統合
- **2025-11-19**: 多言語対応強化

---

## 連絡先

- **開発チーム**: SmartWeb/Interwork Corporation
- **リポジトリ**: https://github.com/LA-JP-Support/hugo-boilerplate
- **公開サイト**: https://main.d1jtfhinlastnr.amplifyapp.com/
