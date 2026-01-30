# LiveAgent マルチウィジェット ガイド

このドキュメントは、SmartWebサイトに実装されているLiveAgentマルチウィジェット（お問い合わせ・チャットボタン）の設定と管理方法を説明します。

---

## 概要

LiveAgentマルチウィジェットは、サイト右下に表示されるフローティングボタンで、訪問者が簡単にお問い合わせフォームやAIチャットボットにアクセスできるようにするものです。

### 機能

| ボタン | 日本語 | 英語 | 動作 |
|-------|--------|------|------|
| お問い合わせ | お問い合わせ | Contact | LiveAgentお問い合わせフォームを開く |
| チャット | チャット | Chat | AIチャットボット（FlowHunt連携）を開く |

---

## ファイル構成

```
layouts/
└── partials/
    └── components/
        ├── liveagent-multiwidget.html      # 日本語版
        └── liveagent-multiwidget.en.html   # 英語版

layouts/
└── _default/
    └── baseof.html                          # パーシャル呼び出し元
```

---

## 設定

### 有効/無効の切り替え

`hugo.toml` で設定します：

```toml
[params.liveagent.multiwidget]
  enable = true   # true: 表示 / false: 非表示
```

### 言語切り替え

`baseof.html` で言語に応じて自動的に切り替わります：

```go
{{ if eq .Lang "en" }}
  {{ partial "components/liveagent-multiwidget.en.html" . }}
{{ else }}
  {{ partial "components/liveagent-multiwidget.html" . }}
{{ end }}
```

---

## レスポンシブ対応

### PC（769px以上）

- メインボタン: テキスト + アイコン表示
- 位置: `bottom: 100px`（ページトップボタンとの重複を避けるため）
- パネル: 自動幅（コンテンツに応じて調整）

### タブレット（768px以下）

- メインボタン: アイコンのみ（52px 丸ボタン）
- パネル: min-width 160px

### スマホ（480px以下）

- メインボタン: アイコンのみ（48px 丸ボタン）
- 位置: `bottom: 80px`（ページトップボタンとの重複を避けるため）
- パネル: min-width 150px

---

## LiveAgent連携設定

### ボタンID

各ボタンはLiveAgentで設定したボタンIDと連携しています：

| 機能 | ボタンID | 変数名 |
|------|----------|--------|
| お問い合わせフォーム | `s141buj5` | `contactForm` |
| AIチャットボット | `tasrn8qe` | `botButton` |

### LiveAgent管理画面での設定

1. LiveAgent管理画面 → 設定 → チャット → チャットボタン
2. 「Own HTML button」タイプで作成
3. 生成されたボタンIDをパーシャルファイルに設定

---

## アイコン

アイコンはSmartWebのファイルサーバーでホストしています：

| アイコン | URL |
|---------|-----|
| お問い合わせ（青） | `https://files.intwk.co.jp/SmartWeb/form.svg` |
| チャット（オレンジ） | `https://files.intwk.co.jp/SmartWeb/chat.svg` |

### メインボタンアイコン

メインボタンのアイコンは外部画像を使用：
```
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkFnGM_CtOsOzloGOge47HQ7-U4gnyhrryn2iA7dmf0A&s
```

**注意**: このアイコンを自社サーバーでホストすることを推奨します。

---

## カスタマイズ

### 色の変更

CSSの以下の部分を変更：

```css
/* メインボタンのグラデーション */
.la-main-button {
  background: linear-gradient(90deg, #ffbd39 0%, #fa9531 100%);
}

/* ホバー時の色 */
.la-multiwidget-item.form:hover {
  background-color: #e8f4fd;  /* お問い合わせ: 青系 */
}

.la-multiwidget-item.chat:hover {
  background-color: #fef3e8;  /* チャット: オレンジ系 */
}
```

### ボタンの追加

新しいボタンを追加する場合：

1. HTMLに `<li>` 要素を追加
2. LiveAgentスクリプトを追加
3. CSSのホバー色を追加

例（ライブチャットを追加する場合）：

```html
<li id="laElementLive" class="la-multiwidget-item live" onclick="chatButton.onClick(); toggleLaMultiwidget();">
  <span class="la-multiwidget-item-text">ライブチャット</span>
  <img class="la-multiwidget-item-icon" src="アイコンURL" alt="Live" />
</li>
```

```javascript
var chatButton;
(function(d, src, c) { ... })(document,
'https://support.intwk.co.jp/scripts/track.js',
function(e){
  chatButton = LiveAgent.createButton('ボタンID', e);
});
```

---

## トラブルシューティング

### ボタンが表示されない

1. `hugo.toml` で `enable = true` になっているか確認
2. ブラウザのコンソールでJavaScriptエラーがないか確認
3. LiveAgentスクリプトが正しく読み込まれているか確認

### ボタンをクリックしても何も起きない

1. LiveAgentの管理画面でボタンが有効になっているか確認
2. ボタンIDが正しいか確認
3. ブラウザのコンソールで `contactForm` や `botButton` が定義されているか確認

### 位置がずれる

1. 他のCSSとの競合がないか確認
2. `z-index` の値を調整
3. `box-sizing` が正しく設定されているか確認

### モバイルでタップしにくい

1. ボタンサイズが最低44px以上あるか確認
2. パネルとメインボタンの間隔が適切か確認

---

## 関連ドキュメント

- [LiveAgent公式ドキュメント](https://support.liveagent.com/)
- [FlowHunt連携ガイド](https://www.flowhunt.io/docs)

---

## 変更履歴

| 日付 | 変更内容 |
|------|----------|
| 2026-01-30 | 初版作成。2ボタン構成（お問い合わせ、チャット）|
| 2026-01-30 | スマートフォン（480px以下）でページトップボタンとの重複を避けるため、LiveAgentボタンの位置を`bottom: 12px`から`bottom: 80px`に変更 |
| 2026-01-30 | PC（769px以上）でもページトップボタンとの重複を避けるため、LiveAgentボタンの位置を`bottom: 20px`から`bottom: 100px`に変更（80px経由で最終調整） |
