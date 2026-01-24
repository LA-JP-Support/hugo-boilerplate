# PageSpeed最適化ガイド

## 概要

このドキュメントでは、SmartWebサイトのPageSpeed Insightsスコアを最適化するための手法と実装について説明します。

**目標スコア:**
- デスクトップ: 90+
- モバイル: 80+

---

## Core Web Vitals

### 1. LCP（Largest Contentful Paint）

**目標値:** 2.5秒以下

**最適化施策:**

#### フォント読み込みの最適化
```html
<!-- layouts/partials/head.html -->
<style>
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url('/fonts/inter/Inter-VariableFont_opsz,wght.woff2') format('woff2');
}
</style>
```

#### クリティカルCSSのインライン化
```html
<!-- layouts/partials/head.html -->
<style>
/* Critical CSS - above the fold */
html { scroll-behavior: smooth; }
body { margin: 0; -webkit-font-smoothing: antialiased; }
header.bg-white { position: sticky !important; top: 0; z-index: 50; }
/* Hero section styles */
.hero-gradient-support { background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); }
</style>
```

#### 画像の遅延読み込み
```html
{{ partial "components/media/lazyimg.html" (dict 
  "src" $imageUrl
  "alt" $imageAlt
  "class" "aspect-3/2 w-full rounded-lg object-cover"
) }}
```

---

### 2. CLS（Cumulative Layout Shift）

**目標値:** 0.1以下

**最適化施策:**

#### 画像にwidth/heightを明示的に指定

**問題:** 画像サイズが指定されていないと、読み込み時にレイアウトがシフトする

**解決策:**
```html
<!-- 修正前 -->
<img src="/images/logo.png" alt="Logo" class="h-full w-auto">

<!-- 修正後 -->
<img src="/images/logo.png" alt="Logo" class="h-full w-auto" width="150" height="40">
```

**実装例（Partner Logo）:**
```html
<!-- layouts/partials/sections/features/with_alternating_sections.html -->
<div class="h-8 md:h-10 w-auto" style="min-width: 120px;">
  <img src="{{ . }}" alt="Partner Logo" 
       class="h-full w-auto object-contain" 
       loading="lazy" 
       width="150" 
       height="40">
</div>
```

**YouTubeサムネイル:**
```html
<img src="https://i.ytimg.com/vi/{{ $videoId }}/maxresdefault.jpg" 
     alt="{{ $title }}"
     loading="lazy"
     width="1280"
     height="720"
     class="absolute inset-0 w-full h-full object-cover">
```

#### ヘッダーのposition指定

**問題:** ヘッダーの`position`がCSS読み込み後に変わるとシフトが発生

**解決策:**
```css
/* layouts/partials/head.html - Critical CSS内 */
header.bg-white { 
  position: sticky !important; 
  top: 0; 
  z-index: 50; 
  background-color: #fff; 
}
```

#### コンテナの最小高さ指定

**問題:** 動的コンテンツの高さが確定するまでシフトが発生

**解決策:**
```html
<!-- アスペクト比を維持 -->
<div style="padding-top: 56.25%;"> <!-- 16:9 -->
  <img class="absolute inset-0 w-full h-full object-cover">
</div>

<!-- 最小高さを指定 -->
<div class="min-h-[200px]">
  <!-- 動的コンテンツ -->
</div>
```

---

### 3. FID/INP（First Input Delay / Interaction to Next Paint）

**目標値:** FID 100ms以下 / INP 200ms以下

**最適化施策:**

#### JavaScriptの遅延読み込み
```html
<script src="/js/app.js" defer></script>
```

#### Lite YouTube方式
```html
<!-- クリック時のみiframeを読み込み -->
<div class="lite-youtube" data-videoid="{{ $videoId }}">
  <img src="https://i.ytimg.com/vi/{{ $videoId }}/maxresdefault.jpg">
  <button aria-label="Play video">▶</button>
</div>

<script>
document.querySelectorAll('.lite-youtube').forEach(el => {
  el.addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube.com/embed/${el.dataset.videoid}?autoplay=1`;
    el.replaceWith(iframe);
  });
});
</script>
```

---

## モバイル固有の最適化

### ヘッダーの条件付きsticky

モバイルでは画面が狭いため、stickyヘッダーがコンテンツを圧迫する。
特定のページ（blog、glossary）ではモバイル時のみヘッダーを非固定にする。

**実装:**
```html
<!-- layouts/blog/single.html, layouts/glossary/single.html -->
<style>
@media (max-width: 1023px) {
  header.bg-white { position: relative !important; }
}
</style>
```

| 画面サイズ | ヘッダー動作 |
|-----------|-------------|
| PC (1024px以上) | sticky - 固定表示 |
| モバイル (1023px以下) | relative - スクロールで消える |

---

## チェックリスト

### デプロイ前確認

- [ ] 画像に`width`と`height`属性が指定されている
- [ ] YouTubeはLite YouTube方式を使用している
- [ ] クリティカルCSSがインライン化されている
- [ ] フォントは`font-display: swap`を使用している
- [ ] JavaScriptは`defer`属性付きで読み込んでいる

### PageSpeed Insightsテスト

1. ローカルでビルド: `hugo --minify`
2. GitHubにプッシュ
3. Amplifyでデプロイ完了を確認
4. [PageSpeed Insights](https://pagespeed.web.dev/)でテスト
5. 問題があれば「診断」セクションを確認

---

## 関連ファイル

### クリティカルCSS
- `layouts/partials/head.html` - インラインCSS定義

### 画像最適化
- `layouts/partials/components/media/lazyimg.html` - 遅延読み込み画像
- `layouts/partials/components/media/lazyimg_internal.html` - 内部画像用
- `scripts/preprocess-images.sh` - 画像最適化スクリプト

### YouTube
- `layouts/shortcodes/youtube.html` - YouTubeショートコード
- `layouts/partials/sections/features/with_alternating_sections.html` - Lite YouTube実装
- `static/js/app.js` - YouTube読み込みスクリプト

### ヘッダー
- `layouts/partials/header.html` - ヘッダーテンプレート
- `layouts/blog/single.html` - ブログ記事（モバイル対応）
- `layouts/glossary/single.html` - 用語集（モバイル対応）

---

## トラブルシューティング

### CLSが高い（0.1以上）

1. PageSpeed Insightsの「レイアウト シフトの原因」セクションを確認
2. 指摘された要素に`width`/`height`を追加
3. 動的コンテンツには`min-height`または`aspect-ratio`を指定

### LCPが遅い（2.5秒以上）

1. LCP要素を特定（通常はヒーロー画像またはh1）
2. LCP画像には`loading="eager"`を使用（遅延読み込みしない）
3. フォントのpreloadを検討
4. クリティカルCSSが正しくインライン化されているか確認

### TBTが高い（200ms以上）

1. サードパーティスクリプトを確認
2. 不要なJavaScriptを削除または遅延読み込み
3. 重いDOM操作を最適化

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-01-24 | CLS改善（Partner Logo、YouTubeサムネイルにwidth/height追加） |
| 2026-01-24 | モバイル用ヘッダー条件付きsticky実装 |
| 2026-01-24 | 初版作成 |
