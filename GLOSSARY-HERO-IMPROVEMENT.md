# 用語集ヒーローセクション デザイン改善

## 🎯 改善のコンセプト

### Before（旧デザイン）
- 色を使いすぎている（青色のバッジ、タグ）
- 余白が不十分
- 階層が曖昧
- カジュアルすぎる印象

### After（新デザイン）
- **モノクローム基調**：グレースケール中心
- **タイポグラフィ重視**：フォントサイズと余白で階層を表現
- **シンプル＆洗練**：細いライン、広い余白
- **プロフェッショナル**：ミニマルで高級感のあるデザイン

---

## 📊 主な変更点

### 1. ヘッダー全体
```html
<!-- 余白を大きく -->
<header class="py-12 sm:py-16 border-b border-gray-200">
  <!-- 最大幅を4xlに制限（より読みやすく） -->
  <div class="mx-auto max-w-4xl">
```

**変更内容：**
- 上下の余白を広く（py-8 → py-12）
- 下部に細いボーダーを追加
- 最大幅を5xl → 4xlに変更（より集中しやすい）

---

### 2. パンくずリスト
```html
<ol class="flex items-center space-x-2 text-gray-400">
  <!-- 薄いグレーでシンプルに -->
</ol>
```

**変更内容：**
- 色を薄く（text-gray-500 → text-gray-400）
- ホームアイコンのサイズを小さく（h-5 → h-4）
- 区切り文字を薄く（text-gray-300）

---

### 3. カテゴリーバッジ

#### Before（青い背景）
```html
<span class="bg-indigo-100 px-3 py-1 text-indigo-600">
```

#### After（ボーダーのみ）
```html
<span class="text-xs uppercase tracking-wider text-gray-500 border-b border-gray-300 pb-1">
```

**変更内容：**
- 背景色を削除
- 下部にボーダーを追加
- 小文字 → 大文字（uppercase）
- 文字間隔を広く（tracking-wider）
- アイコンのサイズを小さく（h-4 → h-3.5）

---

### 4. タイトル

#### Before
```html
<h1 class="text-3xl sm:text-4xl md:text-5xl">
```

#### After
```html
<h1 class="text-4xl sm:text-5xl md:text-6xl mb-6">
```

**変更内容：**
- フォントサイズを大きく（3xl → 4xl）
- 下部の余白を追加（mb-6）
- より大胆なタイポグラフィ

---

### 5. 説明文

#### Before
```html
<p class="text-lg sm:text-xl text-gray-600">
```

#### After
```html
<p class="text-xl sm:text-2xl leading-relaxed text-gray-600 font-light max-w-3xl">
```

**変更内容：**
- フォントサイズを大きく（lg → xl）
- 行間を広く（leading-relaxed）
- フォントウェイトを軽く（font-light）
- 最大幅を制限（max-w-3xl）

---

### 6. 区切り線（新規追加）

```html
<div class="my-8 border-t border-gray-200"></div>
```

**追加理由：**
- 説明文とメタ情報を明確に分離
- 視覚的な階層を強化

---

### 7. キーワードタグ

#### Before（グレー背景）
```html
<span class="bg-gray-100 px-2.5 py-1 text-gray-700">
```

#### After（ボーダーのみ）
```html
<span class="bg-transparent border border-gray-200 px-2.5 py-1 text-gray-600 hover:border-gray-400">
```

**変更内容：**
- 背景色を削除（bg-transparent）
- ボーダーを追加
- ホバーエフェクトを追加
- 角を丸く（rounded）

---

### 8. 更新日

#### Before
```html
<div class="mt-4 text-sm text-gray-500">
```

#### After
```html
<div class="text-sm text-gray-500 flex items-center">
  <svg class="mr-1.5 h-4 w-4">
    <!-- 時計アイコン -->
  </svg>
  <!-- 日付 -->
</div>
```

**変更内容：**
- アイコンを追加
- flexboxで配置
- キーワードと同じ行に配置（sm:flex-row）

---

### 9. レイアウト調整

#### メタ情報セクション
```html
<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
  <!-- キーワード -->
  <!-- 更新日 -->
</div>
```

**変更内容：**
- flexboxで左右に配置（モバイルは縦、デスクトップは横）
- 間隔を統一（gap-4）

---

## 🎨 カラーパレット

### Before（カラフル）
- カテゴリーバッジ: `bg-indigo-100` `text-indigo-600`
- タグ: `bg-gray-100` `text-gray-700`
- リンク: `text-indigo-600`

### After（モノクローム）
- カテゴリーバッジ: `text-gray-500` `border-gray-300`
- タグ: `text-gray-600` `border-gray-200`
- リンク: `text-gray-900` `underline`

---

## 📐 余白の最適化

| 要素 | Before | After |
|------|--------|-------|
| ヘッダー上下 | py-8 (2rem) | py-12 (3rem) |
| タイトル下 | mt-4 (1rem) | mb-6 (1.5rem) |
| 説明文下 | mt-4 (1rem) | — |
| 区切り線 | — | my-8 (2rem) |
| タグ上 | mt-4 (1rem) | — |
| 更新日上 | mt-4 (1rem) | — |

---

## 🔤 タイポグラフィ

### フォントサイズ階層

| 要素 | Before | After |
|------|--------|-------|
| タイトル（デスクトップ） | text-5xl (48px) | text-6xl (60px) |
| 説明文（デスクトップ） | text-xl (20px) | text-2xl (24px) |
| カテゴリー | text-sm (14px) | text-xs (12px) |
| タグ | text-xs (12px) | text-xs (12px) |

### フォントウェイト

| 要素 | Before | After |
|------|--------|-------|
| タイトル | font-bold (700) | font-bold (700) |
| 説明文 | — | font-light (300) |
| カテゴリー | font-medium (500) | font-medium (500) |

---

## 🚀 確認方法

### 1. サーバーを起動

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
hugo server -D
```

### 2. ブラウザで確認

```
http://localhost:1313/en/glossary/botpress/
```

### 3. 確認ポイント

- ✅ タイトルが大きく、目を引く
- ✅ 余白が広く、読みやすい
- ✅ カテゴリーバッジがシンプル
- ✅ タグがミニマル（ボーダーのみ）
- ✅ 全体的にモノクロームでプロフェッショナル
- ✅ 区切り線で階層が明確
- ✅ レスポンシブ対応

---

## 🔄 元に戻す方法

もし元のデザインに戻したい場合：

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/layouts/glossary
mv single.html single-improved.html
mv single-original-backup.html single.html
```

または Filesystem APIで：

1. `single.html` を削除
2. `single-original-backup.html` を `single.html` にリネーム

---

## 💡 さらなるカスタマイズ

### カテゴリーバッジをアイコンのみにする

```html
<span class="inline-flex items-center text-gray-400">
  <svg class="h-4 w-4">
    <!-- アイコンのみ -->
  </svg>
</span>
```

### タグを完全に削除

```html
{{ if false }}
  <!-- キーワードタグを非表示 -->
{{ end }}
```

### タイトルをさらに大きく

```html
<h1 class="text-5xl sm:text-6xl md:text-7xl">
```

---

## 📚 参考デザイン

この改善は以下のデザイン原則に基づいています：

1. **Medium.com**：シンプルなタイポグラフィ中心
2. **Apple.com**：広い余白、細いライン
3. **Stripe.com**：モノクローム基調
4. **Linear.app**：ミニマルで洗練されたデザイン

---

## 🎉 完了！

用語集のヒーローセクションが、シンプルで洗練されたデザインになりました。

**作成日:** 2025-12-02  
**ファイル:** `/layouts/glossary/single.html`  
**バックアップ:** `/layouts/glossary/single-original-backup.html`
