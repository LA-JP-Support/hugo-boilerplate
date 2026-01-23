# 🚀 PageSpeed Insights パフォーマンス最適化

## 📊 最適化結果サマリー

**実施日**: 2025年1月23日  
**対象ページ**: https://main.d1jtfhinlastnr.amplifyapp.com/ja/

### スコア改善（第1回最適化後）

| カテゴリ | 改善前 | デスクトップ | モバイル |
|---------|--------|-------------|---------|
| パフォーマンス | 53 | **86** ✅ | 58 |
| ユーザー補助 | 97 | 97 | 97 |
| おすすめの方法 | 73 | **96** ✅ | 96 |
| SEO | 100 | 100 | 100 |

---

## 📱 モバイル向け追加最適化（第2回）

### モバイル分析結果

| 指標 | 値 | 状態 |
|------|-----|------|
| FCP | 7.2秒 | 🔴 要改善 |
| LCP | 9.9秒 | 🔴 要改善 |
| TBT | 0ミリ秒 | 🟢 良好 |
| CLS | 0.005 | 🟢 良好 |

### 主要なボトルネック

| 問題 | 影響 | 原因 |
|------|------|------|
| **LCPの遅延** | 3,140ms | font-mincho (Noto Serif JP) の読み込み待ち |
| **FCP遅延** | 470ms | CSS読み込み (main.css) がレンダリングブロック |
| **未使用CSS** | 141 KiB | Google Fonts 118.5 KiB + main.css 22.7 KiB |

### 実施した改善

#### 1. 日本語フォントフォールバック最適化

**問題**: LCP要素（h1.font-mincho）がNoto Serif JPの読み込みを待機

**解決策**: システムフォントを含む日本語フォールバックチェーン

```css
/* Before */
.font-mincho { font-family: 'Noto Serif JP', Georgia, serif; }

/* After - iOS/macOS/Windows対応 */
.font-mincho { 
  font-family: 'Noto Serif JP', 'Hiragino Mincho ProN', 'Yu Mincho', 'MS PMincho', Georgia, serif; 
}
```

**効果**: フォント読み込み前でもシステム明朝で即座に表示

#### 2. CSS非同期読み込み

**問題**: main.cssがレンダリングをブロック（470ms）

**解決策**: media="print" onload方式 + クリティカルCSSインライン化

```html
<!-- Preload + Async -->
<link rel="preload" href="/css/main.css" as="style">
<link rel="stylesheet" href="/css/main.css" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="/css/main.css"></noscript>
```

**効果**: レンダリングブロック解消

#### 3. クリティカルCSSの拡張

**問題**: CSS非同期化によるFOUC（スタイルなし表示）の可能性

**解決策**: ヘッダー・ヒーロー・基本ユーティリティをインライン化

```css
/* Header */
header { position: sticky; top: 0; z-index: 50; background-color: #fff; }

/* Hero */
.antigravity-hero { background-color: #0f172a; }
.hero-content h1, .hero-slide h1 { color: #fff; }

/* Tailwind critical utilities */
.relative { position: relative; }
.flex { display: flex; }
.hidden { display: none; }
/* ... */
```

**効果**: FOUC防止、即座にスタイル適用

#### 4. LCP要素のプリロード

**問題**: Noto Serif JPの読み込みが遅い

**解決策**: ヒーローテキストに使用する文字のみをプリロード

```html
<link rel="preload" as="style" 
  href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500;700&display=swap&text=問い合わせ対応を、AIでスマートに。">
```

**効果**: LCPに必要な最小限のフォントを優先読み込み

---

## ✅ 実施した最適化（第1回）

### 1. Google Fontsの非同期読み込み

**問題**: Google Fontsがレンダリングをブロック（-620ms）

**解決策**: media="print" onload方式で非同期化

**効果**: LCP -620ms

### 2. YouTube埋め込みのLite YouTube化

**問題**: YouTube iframeが777 KiBのJavaScriptを読み込み

**解決策**: サムネイル+クリック読み込み方式

**効果**: TBT -440ms、初期JS -777 KiB

**注意**: 再生回数は正常にカウントされます

### 3. クリティカルCSSのインライン化

**問題**: CSSがレンダリングをブロック

**解決策**: フォントフォールバックとレイアウトCSSをインライン化

**効果**: FCP -250ms、FOIT防止

---

## 📁 変更ファイル一覧

| ファイル | 変更内容 |
|----------|---------|
| `layouts/partials/head.html` | Google Fonts非同期化、CSS非同期化、クリティカルCSS拡張 |
| `layouts/shortcodes/youtube.html` | Lite YouTube方式に変更 |
| `layouts/partials/sections/features/with_alternating_sections.html` | YouTube iframe → Lite YouTube |
| `static/js/app.js` | Lite YouTube初期化JS追加 |

---

## 🔜 今後の最適化候補

### 高優先度（モバイル向け）

| 項目 | 効果 | 実装難易度 |
|------|------|-----------|
| Noto Serif JPのセルフホスティング | LCP大幅改善 | 中 |
| PurgeCSSで未使用CSS削除 | -141 KiB | 中 |
| 画像の遅延読み込み強化 | FCP改善 | 低 |

### 中優先度

| 項目 | 効果 | 実装難易度 |
|------|------|-----------|
| GTMの遅延読み込み | -55 KiB | 低 |
| 画像リサイズ | -54 KiB | 低 |
| キャッシュポリシー改善 | -34 KiB | 低 |

---

## 🧪 確認手順

### 1. ローカルでビルド

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
hugo --minify
```

### 2. ローカルサーバーで確認

```bash
hugo server
```

ブラウザで http://localhost:1313/ja/ を開き：
- ヒーローテキストが即座に表示されるか確認（FOIT/FOUCなし）
- YouTube動画がサムネイル表示されているか確認
- クリックで動画が再生されるか確認

### 3. デプロイ

```bash
git add .
git commit -m "perf: モバイル向けPageSpeed最適化 - CSS非同期化、フォントフォールバック強化"
git push origin main
```

### 4. PageSpeed Insightsで再テスト

https://pagespeed.web.dev/ でデプロイ後のURLをテスト

---

## 📚 関連ドキュメント

- [YOUTUBE-IMPLEMENTATION.md](./YOUTUBE-IMPLEMENTATION.md) - YouTube実装詳細
- [YOUTUBE-ROUNDED-STYLE.md](./YOUTUBE-ROUNDED-STYLE.md) - YouTubeスタイリング
- [hugo-boilerplate-technical-documentation.md](./hugo-boilerplate-technical-documentation.md) - 全体技術仕様

---

## 📝 参考リンク

- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Google Fonts最適化](https://web.dev/optimize-webfont-loading/)
- [Core Web Vitals](https://web.dev/vitals/)
- [クリティカルCSS](https://web.dev/extract-critical-css/)

---

## 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2025-01-23 | 第2回最適化: モバイル向けCSS非同期化、フォントフォールバック強化 |
| 2025-01-23 | 第1回最適化: Google Fonts非同期化、Lite YouTube、クリティカルCSS |

---

**最適化完了！** 🚀
