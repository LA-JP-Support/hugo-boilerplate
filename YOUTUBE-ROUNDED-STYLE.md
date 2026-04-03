# 🎬 YouTube動画 角丸スタイル - 実装ガイド

## ✅ 現在の実装

**2025年1月更新**: Lite YouTube方式とともに角丸スタイルを実装。

### 適用されるスタイル

| プロパティ | 値 | 説明 |
|-----------|-----|------|
| border-radius | 18px | 角丸 |
| box-shadow | 0 25px 60px rgba(0,0,0,0.25) | 影 |
| max-width | 768px | 最大幅制限 |
| aspect-ratio | 16:9 | アスペクト比 |

---

## 📝 対象ファイル

### ショートコード
- `/layouts/shortcodes/youtube.html`

### パーシャル
- `/layouts/partials/sections/features/with_alternating_sections.html`

---

## 🎨 CSS詳細

### Lite YouTube用スタイル

```css
/* ラッパー */
.youtube-embed-wrapper {
  max-width: 768px !important;
  margin: 2rem auto 3rem !important;
}

/* Lite YouTubeコンテナ */
.lite-youtube {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* 16:9 */
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25);
  background: #000;
  cursor: pointer;
}

/* サムネイル画像 */
.lite-youtube-poster {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: filter 0.2s ease;
}

.lite-youtube:hover .lite-youtube-poster {
  filter: brightness(0.85);
}

/* プレイボタン */
.lite-youtube-playbtn {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 68px;
  height: 48px;
  background: transparent;
  border: none;
  cursor: pointer;
  z-index: 2;
  transition: transform 0.2s ease, filter 0.2s ease;
}

.lite-youtube:hover .lite-youtube-playbtn {
  transform: translate(-50%, -50%) scale(1.1);
  filter: brightness(1.1);
}

/* プレイボタン背景（赤） */
.lite-youtube-playbtn-bg {
  fill: #f00;
  fill-opacity: 0.9;
}

/* プレイボタンアイコン（白） */
.lite-youtube-playbtn-icon {
  fill: #fff;
}

/* iframe読み込み後 */
.lite-youtube.lite-youtube-activated {
  cursor: default;
}

.lite-youtube.lite-youtube-activated .lite-youtube-poster,
.lite-youtube.lite-youtube-activated .lite-youtube-playbtn {
  display: none;
}

.lite-youtube iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
```

---

## 🌙 ダークモード対応

```css
.dark .lite-youtube,
.dark .youtube-embed-container {
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5) !important;
}
```

---

## 📱 レスポンシブ対応

```css
@media (max-width: 768px) {
  .youtube-embed-wrapper {
    margin: 1.5rem auto 2rem !important;
    padding: 0 1rem !important;
  }
  
  .lite-youtube,
  .youtube-embed-container {
    border-radius: 12px !important;
  }
}
```

---

## 🎯 角丸のカスタマイズ

### より丸くしたい場合

```css
.lite-youtube {
  border-radius: 24px; /* デフォルト18pxより大きく */
}
```

### より控えめにしたい場合

```css
.lite-youtube {
  border-radius: 12px; /* デフォルト18pxより小さく */
}
```

### 角丸なし

```css
.lite-youtube {
  border-radius: 0;
}
```

---

## 🌟 影のカスタマイズ

### より濃い影

```css
.lite-youtube {
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.35);
}
```

### より薄い影

```css
.lite-youtube {
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}
```

### 影なし

```css
.lite-youtube {
  box-shadow: none;
}
```

---

## 📐 サイズのカスタマイズ

### 最大幅を変更

```css
.youtube-embed-wrapper {
  max-width: 640px; /* より小さく */
}
```

または

```css
.youtube-embed-wrapper {
  max-width: 100%; /* 画面幅いっぱい */
}
```

---

## 🎬 プレイボタンのカスタマイズ

### 色を変更

```css
.lite-youtube-playbtn-bg {
  fill: #4f46e5; /* 紫色に */
}
```

### サイズを変更

```css
.lite-youtube-playbtn {
  width: 80px;
  height: 56px;
}
```

---

## 📚 Tailwindクラス参照

もしTailwindクラスを直接使う場合:

| クラス | 値 |
|--------|-----|
| `rounded` | 4px |
| `rounded-lg` | 8px |
| `rounded-xl` | 12px |
| `rounded-2xl` | 16px |
| `rounded-3xl` | 24px |

---

## 🔄 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2025-01-23 | Lite YouTube方式対応のスタイル追加 |
| 2025-01-23 | プレイボタンスタイル追加 |
| (以前) | 初期実装 |

---

## 📚 関連ドキュメント

- [YOUTUBE-IMPLEMENTATION.md](./YOUTUBE-IMPLEMENTATION.md) - 実装詳細
- [smartweb-technical-documentation.md](./smartweb-technical-documentation.md) - 全体技術仕様

---

**スタイル実装完了！** 🎨
