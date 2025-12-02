# コードブロック 文字色カスタマイズガイド

## 📍 ファイルの場所

```
/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/static/css/custom-code-blockquote.css
```

---

## 🎨 文字色の変更方法

### 1. インラインコード（`code`）

**現在の設定：**
```css
code {
    color: #d73a49 !important;  /* 濃い赤 */
    font-weight: 600 !important;
}
```

**変更例：**
```css
/* 青色に変更 */
code {
    color: #0366d6 !important;
}

/* 紫色に変更 */
code {
    color: #6f42c1 !important;
}

/* 濃いグレー */
code {
    color: #24292e !important;
}
```

---

### 2. コードブロック全体のテキスト（`pre code`）

**現在の設定：**
```css
pre code {
    color: #24292e !important;  /* 濃い黒 */
    font-weight: 500 !important;
}
```

**変更例：**
```css
/* より濃い黒 */
pre code {
    color: #000000 !important;
}

/* 濃いグレー */
pre code {
    color: #333333 !important;
}
```

---

### 3. シンタックスハイライトの色

#### キーワード（POST, GET, import など）

**現在の設定：**
```css
.highlight .kd,
.highlight .kn,
.highlight .kp,
.highlight .kr,
.highlight .kt {
    color: #d73a49 !important;  /* 濃い赤 */
    font-weight: 600 !important;
}
```

**変更例：**
```css
/* 青色に変更 */
.highlight .kd { color: #0366d6 !important; }

/* 紫色に変更 */
.highlight .kd { color: #6f42c1 !important; }
```

#### 文字列（"...", '...'）

**現在の設定：**
```css
.highlight .s,
.highlight .s1,
.highlight .s2 {
    color: #d73a49 !important;  /* 濃い赤 */
    font-weight: 500 !important;
}
```

**変更例：**
```css
/* 緑色に変更 */
.highlight .s { color: #22863a !important; }

/* オレンジ色に変更 */
.highlight .s { color: #e36209 !important; }
```

#### 数値（123, 456）

**現在の設定：**
```css
.highlight .m,
.highlight .mi,
.highlight .mf {
    color: #005cc5 !important;  /* 青 */
    font-weight: 500 !important;
}
```

#### 関数名・変数名

**現在の設定：**
```css
.highlight .n,
.highlight .nx,
.highlight .nf {
    color: #24292e !important;  /* 濃い黒 */
    font-weight: 500 !important;
}
```

**変更例：**
```css
/* 紫色に変更 */
.highlight .nf { color: #6f42c1 !important; }
```

---

## 🎯 おすすめカラーパレット

### GitHub風（現在の設定）

```css
code {
    color: #d73a49;  /* 赤 */
}

pre code {
    color: #24292e;  /* 濃い黒 */
}

.highlight .kd { color: #d73a49; }  /* キーワード: 赤 */
.highlight .s { color: #d73a49; }   /* 文字列: 赤 */
.highlight .m { color: #005cc5; }   /* 数値: 青 */
.highlight .c { color: #6a737d; }   /* コメント: グレー */
```

### VS Code風

```css
code {
    color: #c586c0;  /* 紫 */
}

pre code {
    color: #d4d4d4;  /* 明るいグレー */
}

.highlight .kd { color: #569cd6; }  /* キーワード: 青 */
.highlight .s { color: #ce9178; }   /* 文字列: オレンジ */
.highlight .m { color: #b5cea8; }   /* 数値: 緑 */
.highlight .c { color: #6a9955; }   /* コメント: 緑 */
```

### Monokai風

```css
code {
    color: #f92672;  /* マゼンタ */
}

pre code {
    color: #f8f8f2;  /* 明るい白 */
}

.highlight .kd { color: #f92672; }  /* キーワード: マゼンタ */
.highlight .s { color: #e6db74; }   /* 文字列: 黄色 */
.highlight .m { color: #ae81ff; }   /* 数値: 紫 */
.highlight .c { color: #75715e; }   /* コメント: グレー */
```

---

## 🔧 フォントウェイト（太さ）の変更

### より太く

```css
code {
    font-weight: 700 !important;  /* 太字 */
}

pre code {
    font-weight: 600 !important;
}
```

### より細く

```css
code {
    font-weight: 500 !important;  /* 中太 */
}

pre code {
    font-weight: 400 !important;  /* 標準 */
}
```

---

## 📊 背景色と文字色のコントラスト

### 高コントラスト（推奨）

```css
/* 背景: 明るい */
pre {
    background-color: #f6f8fa !important;
}

/* 文字: 濃い */
pre code {
    color: #000000 !important;
}
```

### 中コントラスト（現在）

```css
/* 背景: 明るいグレー */
pre {
    background-color: #f6f8fa !important;
}

/* 文字: 濃いグレー */
pre code {
    color: #24292e !important;
}
```

---

## ✅ 確認方法

### 1. CSSファイルを編集

```bash
nano /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/static/css/custom-code-blockquote.css
```

### 2. サーバーを再起動

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate
hugo server -D
```

### 3. ブラウザでキャッシュクリア

```
Ctrl+Shift+R (Windows/Linux)
Cmd+Shift+R (Mac)
```

### 4. 確認

```
http://localhost:1313/en/glossary/
```

---

## 🎨 カラーコード一覧

| 色 | カラーコード | 用途 |
|----|-------------|------|
| 濃い赤 | `#d73a49` | キーワード、文字列（現在） |
| 青 | `#0366d6` | リンク、数値 |
| 緑 | `#22863a` | 成功、文字列 |
| オレンジ | `#e36209` | 警告、数値 |
| 紫 | `#6f42c1` | 関数名、変数 |
| 濃い黒 | `#24292e` | 基本テキスト（現在） |
| グレー | `#6a737d` | コメント |
| 明るいグレー | `#d1d5da` | 境界線 |

---

## 💡 読みやすさのポイント

1. **コントラスト比**: 最低 4.5:1 以上を推奨
2. **フォントウェイト**: 500-600 が読みやすい
3. **背景色**: 明るすぎず暗すぎない
4. **文字色**: 濃いめの色を使用
5. **境界線**: 背景との区別を明確に

---

## 🚀 クイックコピペ

### より濃い色（最も読みやすい）

```css
/* これをCSSファイルに追加 */
code {
    color: #c7254e !important;
    font-weight: 700 !important;
}

pre code {
    color: #000000 !important;
    font-weight: 600 !important;
}

.highlight .s { color: #c7254e !important; }
.highlight .kd { color: #c7254e !important; }
```

---

**作成日:** 2025-12-02  
**最終更新:** 2025-12-02
