# 🎬 YouTube動画 角丸スタイル - 実装完了

## ✅ 完了した作業

1. ✅ 「準備中」セクションの文章を削除
2. ✅ YouTube動画を角丸スタイル（Googleスタイル）に変更
3. ✅ カスタムYouTubeショートコードを作成

---

## 📝 更新したファイル

### 新規作成
- ✅ `/layouts/shortcodes/youtube.html` - 角丸スタイル対応のカスタムショートコード

### 更新
- ✅ `/content/ja/_index.md` - 文章を削除、動画のみに
- ✅ `/content/en/_index.md` - 文章を削除、動画のみに

---

## 🎨 実装内容

### カスタムYouTubeショートコード

**場所:** `/layouts/shortcodes/youtube.html`

**特徴:**
- ✅ **角丸デザイン** - `border-radius: 1.5rem` (24px)
- ✅ **影付き** - Googleスタイルの洗練された影
- ✅ **レスポンシブ** - 16:9のアスペクト比を維持
- ✅ **ダークモード対応** - 影の濃さを自動調整
- ✅ **遅延読み込み** - `loading="lazy"` で最適化

### スタイル詳細

```css
.youtube-video-container {
  border-radius: 1.5rem;           /* 角丸 24px */
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 
              0 10px 10px -5px rgba(0, 0, 0, 0.04);
  margin: 2rem auto;               /* 上下の余白 */
}
```

---

## 🚀 確認手順

### 1. Hugoサーバーを起動

```bash
cd /Users/taka/Documents/GitHub/hugo-boilerplate
hugo server
```

### 2. ブラウザで確認

- **日本語:** http://localhost:1313/
- **英語:** http://localhost:1313/en/

### 3. 確認ポイント

- ✅ 動画の四隅が角丸になっている
- ✅ 動画に影が付いている
- ✅ 余計な文章が表示されていない
- ✅ モバイルでも正しく表示される

---

## 🎨 角丸のサイズを調整

### より丸くしたい場合

**`/layouts/shortcodes/youtube.html`** を編集：

```css
border-radius: 2rem;  /* 32px - より丸く */
```

### より四角くしたい場合

```css
border-radius: 1rem;  /* 16px - 控えめに */
```

### 完全に四角にしたい場合

```css
border-radius: 0;  /* 角丸なし */
```

---

## 🌟 影のカスタマイズ

### より濃い影

```css
box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
```

### より薄い影

```css
box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 
            0 4px 6px -2px rgba(0, 0, 0, 0.05);
```

### 影なし

```css
box-shadow: none;
```

---

## 📐 動画のサイズを調整

### 最大幅を制限したい場合

**`/layouts/shortcodes/youtube.html`** のCSSに追加：

```css
.youtube-video-container {
  max-width: 800px;  /* 最大幅を800pxに */
  margin: 2rem auto; /* 中央配置 */
}
```

### さらに大きく表示したい場合

```css
.youtube-video-container {
  max-width: 100%;  /* 画面幅いっぱい */
}
```

---

## 🔄 元の標準スタイルに戻したい場合

**`/layouts/shortcodes/youtube.html`** を削除するだけです：

```bash
rm /Users/taka/Documents/GitHub/hugo-boilerplate/layouts/shortcodes/youtube.html
```

Hugoは自動的に標準のYouTubeショートコードを使用します。

---

## 📱 レスポンシブ対応

カスタムショートコードは完全にレスポンシブです：

- ✅ **デスクトップ** - 大きく美しく表示
- ✅ **タブレット** - 画面幅に自動調整
- ✅ **スマートフォン** - 縦向き・横向き対応

---

## 🌙 ダークモード

影の濃さが自動的に調整されます：

```css
/* ライトモード */
box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

/* ダークモード */
.dark .youtube-video-container {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
}
```

---

## 🔧 トラブルシューティング

### 角丸が表示されない

1. **ブラウザのキャッシュをクリア:**
   - Chrome: `Ctrl+Shift+R` (Windows) / `Cmd+Shift+R` (Mac)
   - Firefox: `Ctrl+F5` (Windows) / `Cmd+Shift+R` (Mac)

2. **Hugoサーバーを再起動:**
   ```bash
   hugo server --disableFastRender
   ```

3. **ブラウザの開発者ツールで確認:**
   - F12を押す
   - 動画要素を右クリック → 検証
   - `border-radius` が適用されているか確認

### 動画が表示されない

ショートコードの構文を確認：
```markdown
{{< youtube frmB19r0k58 >}}
```
- スペースに注意
- `<` と `>` の向きに注意
- ビデオIDが正しいか確認

---

## 🎯 表示例

### 変更前
```
## 準備中

現在、新しいサービスの準備を進めています。近日公開予定ですので、お楽しみに！

[YouTube動画 - 角丸なし]

最新の情報はブログでご確認いただけます。
```

### 変更後
```
[YouTube動画 - 角丸あり、影付き]
```

---

## 🔄 Git操作

### コミット＆プッシュ

GitHub Desktopで：
1. Fetch origin
2. Pull origin
3. 変更を確認（3つのファイル）
   - `layouts/shortcodes/youtube.html` (新規)
   - `content/ja/_index.md` (更新)
   - `content/en/_index.md` (更新)
4. Commit（例：「Add rounded YouTube video, remove text」）
5. Push origin

または、コマンドライン：
```bash
cd /Users/taka/Documents/GitHub/hugo-boilerplate
git add layouts/shortcodes/youtube.html
git add content/ja/_index.md content/en/_index.md
git commit -m "Add rounded YouTube video style, remove Coming Soon text"
git push origin main
```

---

## 📚 参考情報

### Tailwindの角丸クラス（参考）

もしTailwindを使う場合：
- `rounded` - 4px
- `rounded-lg` - 8px
- `rounded-xl` - 12px
- `rounded-2xl` - 16px
- `rounded-3xl` - 24px (今回使用)

### CSSの影（box-shadow）構文

```css
box-shadow: [横の位置] [縦の位置] [ぼかし] [広がり] [色];
```

例：
```css
box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
/*          ↑  ↑   ↑    ↑    ↑
            横  縦  ぼかし 広がり 色（透明度0.1） */
```

---

## 🎉 完了！

YouTube動画が以下の仕様で表示されるようになりました：

- ✅ 余計な文章なし（動画のみ）
- ✅ 角丸デザイン（24px）
- ✅ 洗練された影付き
- ✅ Googleスタイルの美しい見た目
- ✅ レスポンシブ対応
- ✅ ダークモード対応

---

次にやること：
1. ✅ `hugo server` で確認
2. ✅ ブラウザで角丸を確認
3. ✅ モバイルでも確認
4. ✅ Gitでコミット＆プッシュ

---

**実装完了！** 🎬✨
