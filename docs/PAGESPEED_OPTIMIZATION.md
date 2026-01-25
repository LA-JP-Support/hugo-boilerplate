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

## Critical CSSとCLSの関係（重要）

### なぜCritical CSS変更でCLSが発生するのか

Critical CSSを変更すると、しばしばCLSが悪化します。これは以下のメカニズムによります：

```
[ブラウザの処理順序]
1. HTMLをパース開始
2. Critical CSS（head.html内のインライン）を適用 → 初期レイアウト確定
3. main.cssを非同期でダウンロード
4. main.css適用 → スタイルが異なるとレイアウト再計算 → CLS発生
```

### Critical CSS変更時の注意点

| やってはいけないこと | 理由 |
|---------------------|------|
| main.cssと異なる値を指定 | 読み込み後にレイアウトが変わる |
| font-size/line-heightを指定 | Tailwindクラスと競合する |
| position/display を変更 | 要素の配置が変わる |
| margin/padding を追加 | スペーシングが変わる |

### 安全なCritical CSS項目

```css
/* ✅ 安全：背景色・基本的なフォント指定 */
body { background-color: #fff; color: #1f2937; }
.bg-white { background-color: #fff; }

/* ✅ 安全：フォントファミリーのみ（サイズは指定しない） */
.hero-content h1 { 
  font-family: 'Hiragino Mincho ProN', serif !important;
  font-weight: 700;
  color: #fff;
}

/* ❌ 危険：サイズやレイアウトを指定 */
.hero-slide h1 { 
  font-size: 3rem;      /* main.cssと競合 */
  line-height: 1.1;     /* main.cssと競合 */
}
.hero-slide { 
  position: absolute;   /* JSで変更される可能性 */
  opacity: 0;           /* アニメーションと競合 */
}
```

### LCP vs CLS のトレードオフ

| 最適化手法 | LCPへの効果 | CLSリスク |
|-----------|------------|----------|
| CSS非同期読み込み | ✅ 改善 | ⚠️ 高い |
| Critical CSS追加 | ✅ 改善 | ⚠️ 中〜高 |
| フォントpreload | ✅ 改善 | ⚠️ 低い |
| 画像にwidth/height | ー | ✅ 改善 |

### 推奨アプローチ

1. **Critical CSSは最小限に保つ**
   - フォントファミリー、背景色、基本的なdisplay/positionのみ
   - サイズ指定（font-size, width, height, margin, padding）は避ける

2. **変更前後で必ずCLSを測定**
   - PageSpeed Insightsのモバイルテストを実行
   - CLS 0.1以下を維持

3. **問題発生時は変更を戻す**
   - LCP改善よりCLS維持を優先（ユーザー体験への影響が大きい）

---

## Google Analytics遅延読み込み

### 実装（2026-01-25）

Google Analyticsをページ読み込み後に遅延ロードし、初期レンダリングをブロックしないようにする。

**ファイル:** `layouts/partials/utils/analytics/google-analytics-consent.html`

```javascript
// 3秒後、またはユーザー操作時にGAを読み込み
const loadGA = () => {
  if (window.gaLoaded) return;
  window.gaLoaded = true;
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=GA_ID';
  script.async = true;
  document.head.appendChild(script);
};

// 3秒後に自動読み込み
setTimeout(loadGA, 3000);

// ユーザー操作時に即時読み込み
['scroll', 'click', 'touchstart', 'mousemove', 'keydown'].forEach(event => {
  window.addEventListener(event, loadGA, { once: true, passive: true });
});
```

**効果:**
- 未使用JavaScriptの削減: 約55 KiB
- TBT改善

---

## 画像最適化（WebP変換）

### ロゴ画像のWebP変換（2026-01-25）

| ファイル | 元サイズ | 最適化後 | 削減率 |
|---------|---------|---------|-------|
| flowhunt-logo.png | 42.8KB (2112x452) | 6.2KB (523x112 WebP) | 85% |
| liveagent-logo.png | 13.8KB (941x218) | 10.5KB (524x121 WebP) | 24% |

**変換コマンド:**
```bash
# ImageMagickを使用
convert input.png -resize 524x -quality 85 output.webp
```

**注意:** コンテンツファイル（_index.md）内の画像パスも更新が必要
```yaml
logos:
  - "/images/liveagent-logo.webp"  # .png → .webp
  - "/images/flowhunt-logo.webp"
```

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-01-25 | Critical CSSとCLSの関係について追記 |
| 2026-01-25 | GA遅延読み込み実装、ロゴWebP変換 |
| 2026-01-24 | CLS改善（Partner Logo、YouTubeサムネイルにwidth/height追加） |
| 2026-01-24 | モバイル用ヘッダー条件付きsticky実装 |
| 2026-01-24 | 初版作成 |
