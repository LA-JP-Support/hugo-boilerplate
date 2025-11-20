# 🎬 YouTube動画埋め込み - 実装完了

## ✅ 完了した作業

「準備中」セクションにYouTube動画を埋め込みました。

### 動画情報
- **動画URL:** https://www.youtube.com/watch?v=frmB19r0k58
- **タイトル:** Welcome to Google Antigravity
- **ビデオID:** frmB19r0k58

---

## 📝 更新したファイル

### 日本語版
- ✅ `/content/ja/_index.md` - YouTube動画を追加（既に追加済み）

### 英語版
- ✅ `/content/en/_index.md` - YouTube動画を追加

---

## 🎯 実装内容

Hugoの標準YouTubeショートコードを使用：

```markdown
{{< youtube frmB19r0k58 >}}
```

このショートコードは自動的に以下を生成します：
- レスポンシブな16:9のアスペクト比
- iframeでの埋め込み
- モバイル・デスクトップ対応

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

「準備中 / Coming Soon」セクションにYouTube動画が表示されることを確認してください。

---

## 🎨 動画表示の調整（オプション）

### 動画のサイズを変更したい場合

カスタムショートコードを作成：

**`/layouts/shortcodes/youtube-custom.html`** を作成：

```html
{{ $id := .Get 0 }}
{{ $class := .Get "class" | default "" }}

<div class="video-container {{ $class }}">
  <iframe 
    src="https://www.youtube.com/embed/{{ $id }}" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
    allowfullscreen 
    title="YouTube video">
  </iframe>
</div>

<style>
.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
  max-width: 100%;
  margin: 2rem auto;
}

/* 動画の最大幅を制限したい場合 */
.video-container.narrow {
  max-width: 800px;
}
</style>
```

使用方法：
```markdown
{{< youtube-custom frmB19r0k58 >}}

<!-- または最大幅を制限 -->
{{< youtube-custom frmB19r0k58 class="narrow" >}}
```

### 背景を暗くしたい場合

home.htmlのコンテンツセクションのスタイルを調整：

```html
<!-- Content from Markdown -->
{{ if .Content }}
  <div class="py-16 bg-gray-900 dark:bg-black" style="position: relative; overflow: hidden;">
    <!-- ... -->
  </div>
{{ end }}
```

---

## 🔧 トラブルシューティング

### 動画が表示されない

1. **ショートコードの構文を確認:**
   ```markdown
   {{< youtube frmB19r0k58 >}}
   ```
   - スペースに注意
   - ビデオIDが正しいか確認

2. **Hugoサーバーを再起動:**
   ```bash
   hugo server --disableFastRender
   ```

3. **ブラウザのコンソールでエラーをチェック:**
   F12を押して「Console」タブを確認

### 動画の読み込みが遅い

YouTube動画はiframeで埋め込まれているため、初回読み込みに時間がかかることがあります。これは正常な動作です。

### プライバシー強化モードを使いたい場合

`/layouts/shortcodes/youtube.html` を作成：

```html
{{ $id := .Get 0 }}
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe 
    src="https://www.youtube-nocookie.com/embed/{{ $id }}" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
    allowfullscreen 
    title="YouTube video"
    loading="lazy">
  </iframe>
</div>
```

これにより：
- `youtube-nocookie.com` を使用（プライバシー保護）
- `loading="lazy"` で遅延読み込み

---

## 📱 レスポンシブ対応

Hugoの標準YouTubeショートコードは既にレスポンシブ対応しているため、以下のデバイスで正しく表示されます：

- ✅ デスクトップ
- ✅ タブレット
- ✅ スマートフォン

---

## 🌐 多言語対応

日本語版と英語版の両方に同じ動画を埋め込みました：

| 言語 | URL | ファイル |
|------|-----|---------|
| 日本語 | `/` | `/content/ja/_index.md` |
| 英語 | `/en/` | `/content/en/_index.md` |

---

## 🔄 Git操作

### コミット＆プッシュ

GitHub Desktopで：
1. Fetch origin
2. Pull origin
3. 変更を確認（en/_index.mdの1ファイル、ja/_index.mdは既に追加済み）
4. Commit（例：「Add YouTube video to Coming Soon section」）
5. Push origin

または、コマンドライン：
```bash
cd /Users/taka/Documents/GitHub/hugo-boilerplate
git add content/en/_index.md
git commit -m "Add YouTube video to Coming Soon section"
git push origin main
```

---

## 📊 表示例

### 日本語版
```
## 準備中

現在、新しいサービスの準備を進めています。近日公開予定ですので、お楽しみに！

[YouTube動画がここに表示]

最新の情報はブログでご確認いただけます。
```

### 英語版
```
## Coming Soon

We are currently preparing new services. Stay tuned!

[YouTube video displayed here]

Check our Blog for the latest information.
```

---

## 🎉 完了！

「準備中 / Coming Soon」セクションにYouTube動画が埋め込まれました。

次にやること：
1. ✅ `hugo server` で動作確認
2. ✅ ブラウザで日本語版・英語版を確認
3. ✅ モバイルでも確認（レスポンシブ対応）
4. ✅ Gitでコミット＆プッシュ

---

## 📞 補足

- YouTube動画のIDは常に11文字です
- 動画のプライバシー設定が「公開」または「限定公開」になっていることを確認してください
- 「非公開」動画は埋め込みできません

---

**実装完了！** 🎬
