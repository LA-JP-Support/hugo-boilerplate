# Hugo Glossary Creation & Translation Manual
## 英語グロッサリー作成→日本語翻訳 完全マニュアル

**作成日**: 2025-12-19  
**バージョン**: 2.0  
**重要**: 翻訳スクリプトは **e-title, term, url の3フィールドを自動追加します** ✅

---

## 📋 目次

1. [重要な変更点](#重要な変更点)
2. [プロジェクト概要](#プロジェクト概要)
3. [APIキー設定](#apiキー設定)
4. [フロントマター仕様](#フロントマター仕様)
5. [翻訳ワークフロー](#翻訳ワークフロー)
6. [実行例（5件テスト）](#実行例5件テスト)
7. [トラブルシューティング](#トラブルシューティング)
8. [クイックリファレンス](#クイックリファレンス)

---

## ⚡ 重要な変更点

### ✅ 翻訳スクリプトが自動処理するフィールド

翻訳スクリプト `scripts/translate_glossary_en_to_ja.py` は、日本語版に以下のフィールドを**自動的に追加**します：

| フィールド | 処理内容 | 例 |
|-----------|---------|-----|
| **e-title** | 英語titleをコピー | `"Active Learning"` |
| **term** | Claude APIがひらがな生成 | `"あくてぃぶらーにんぐ"` |
| **url** | ファイル名から生成 | `"/ja/glossary/Active-Learning/"` |

**手動追加は不要です！** 🎉

---

## 1. プロジェクト概要

### 1.1 目的
AI/自動化関連用語のSEO最適化されたバイリンガルグロッサリーを構築

### 1.2 品質目標

| 項目 | 英語版 | 日本語版 |
|------|--------|---------|
| 文字数 | 2,600-2,800語 | 制限なし（翻訳結果による） |
| コンテンツ比率 | 30%散文 / 70%構造化 | 同左 |
| フロントマター | 9フィールド | 12フィールド（+3自動追加） |
| References | 全外部リンク統合 | 英語版と同じURL |

### 1.3 ディレクトリ構造

```
hugo-boilerplate/
├── .env                              # APIキー（機密情報）
├── content/
│   ├── en/glossary/                  # 英語グロッサリー記事
│   │   ├── Active-Learning.md
│   │   ├── Code-Generation.md
│   │   └── ...
│   └── ja/glossary/                  # 日本語グロッサリー記事
│       ├── Active-Learning.md
│       ├── Code-Generation.md
│       └── ...
├── docs/
│   ├── prioritized_keywords.csv      # 用語マスターリスト ★
│   └── GLOSSARY_CREATION_TRANSLATION_MANUAL.md  # このファイル
├── scripts/
│   └── translate_glossary_en_to_ja.py  # 翻訳メインスクリプト（改良版）
└── GLOSSARY_OPTIMIZATION_GUIDE.md    # 品質基準ガイド
```

---

## 2. APIキー設定

### 2.1 .envファイルの場所と内容

**ファイルパス**: `/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/.env`

**内容**:
```bash
# Claude API Key (Anthropic) - 両方設定推奨
CLAUDE_API_KEY="your-api-key-here"
ANTHROPIC_API_KEY="your-api-key-here"
```

### 2.2 環境変数の設定方法

```bash
# 一時的設定（現在のセッションのみ）
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 確認
echo $ANTHROPIC_API_KEY
```

---

## 3. フロントマター仕様

### 3.1 英語版（9フィールド）

```yaml
---
title: "Active Learning"
date: 2025-12-19
translationKey: active-learning
description: "A machine learning process where the model explicitly asks a human to label data points it is uncertain about."
keywords:
- active learning
- machine learning
- data labeling
- human-in-the-loop
- model training
category: "AI Chatbot & Automation"
type: glossary
draft: false
---
```

### 3.2 日本語版（12フィールド）- **自動生成**

```yaml
---
title: "Active Learning（アクティブラーニング）"  # ✅ 自動翻訳
date: 2025-12-19                                    # コピー
translationKey: active-learning                     # コピー
description: "機械学習プロセス..."                   # ✅ 自動翻訳
keywords:                                            # ✅ 自動翻訳
- アクティブラーニング
- 機械学習
- データラベリング
- ヒューマンインザループ
- モデル訓練
category: "AI Chatbot & Automation"                 # コピー（英語のまま）
type: glossary                                       # コピー
draft: false                                         # コピー
e-title: "Active Learning"                          # ✅ 自動追加
term: "あくてぃぶらーにんぐ"                         # ✅ 自動追加（Claude API生成）
url: "/ja/glossary/Active-Learning/"                # ✅ 自動追加
---
```

### 3.3 自動追加フィールドの詳細

| フィールド | 生成方法 | 例 |
|-----------|---------|-----|
| **e-title** | 英語版のtitleをそのままコピー | `"Active Learning"` |
| **term** | Claude APIがTERM_JAとしてひらがな生成 | `"あくてぃぶらーにんぐ"` |
| **url** | ファイル名から生成: `/ja/glossary/{filename}/` | `"/ja/glossary/Active-Learning/"` |

### 3.4 titleの形式ルール

**日本語版title形式**: `"英語タイトル（カタカナ読み）"`

**例**:
| 英語タイトル | 日本語title |
|-------------|-------------|
| Active Learning | "Active Learning（アクティブラーニング）" |
| Code Generation | "Code Generation（コード生成）" |
| Machine Learning | "Machine Learning（機械学習）" |
| Deep Learning | "Deep Learning（ディープラーニング）" |

---

## 4. 翻訳ワークフロー

### 4.1 事前準備

```bash
# プロジェクトルートに移動
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

# APIキー設定
export ANTHROPIC_API_KEY="your-api-key-here"

# 確認
echo $ANTHROPIC_API_KEY
```

### 4.2 単一ファイル翻訳

```bash
python scripts/translate_glossary_en_to_ja.py --one-file Active-Learning.md
```

**実行結果の例**:
```
✓ Translated content/en/glossary/Active-Learning.md -> content/ja/glossary/Active-Learning.md
```

### 4.3 翻訳スクリプトが自動処理する内容

#### 処理される項目

1. **title**: `"Active Learning"` → `"Active Learning（アクティブラーニング）"` ✅
2. **description**: 英語 → 日本語訳 ✅
3. **keywords**: 英語配列 → 日本語配列 ✅
4. **e-title**: `"Active Learning"` を自動追加 ✅
5. **term**: Claude APIがひらがな生成 → `"あくてぃぶらーにんぐ"` ✅
6. **url**: `/ja/glossary/Active-Learning/` を自動生成 ✅
7. **内部リンク**: `/en/glossary/` → `/ja/glossary/` に自動書き換え ✅

#### 処理されない項目（そのままコピー）

- date
- translationKey
- category（英語のまま維持）
- type
- draft

### 4.4 確認方法

```bash
# 日本語版のフロントマター確認（先頭25行）
head -25 content/ja/glossary/Active-Learning.md

# 特定フィールドのみ確認
head -25 content/ja/glossary/Active-Learning.md | grep -E "(e-title|term|url):"
```

**期待される出力**:
```yaml
e-title: "Active Learning"
term: "あくてぃぶらーにんぐ"
url: "/ja/glossary/Active-Learning/"
```

---

## 5. 実行例（5件テスト）

### 5.1 CSVから未作成用語を選択

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

# 未作成ファイル確認
tail -n +2 docs/prioritized_keywords.csv | cut -d',' -f4 | \
while read f; do 
    [ ! -f "content/en/glossary/$f" ] && echo "$f"
done | head -5
```

**選択した5件（例）**:
1. Active-Learning.md
2. Aspect-Based-Sentiment-Analysis.md
3. Demand-Forecasting.md
4. Financial-Risk-Management.md
5. Fraud-Detection.md

### 5.2 英語版作成

（各用語について、Claudeに2,600-2,800語の記事作成を依頼）

### 5.3 日本語翻訳（バッチ処理）

```bash
# APIキー設定
export ANTHROPIC_API_KEY="your-api-key-here"

# ファイル配列定義
FILES=(
    "Active-Learning.md"
    "Aspect-Based-Sentiment-Analysis.md"
    "Demand-Forecasting.md"
    "Financial-Risk-Management.md"
    "Fraud-Detection.md"
)

# 順次翻訳
for file in "${FILES[@]}"; do
    echo "翻訳中: $file"
    python scripts/translate_glossary_en_to_ja.py --one-file "$file"
    
    if [ $? -eq 0 ]; then
        echo "✅ 完了: $file"
    else
        echo "❌ エラー: $file"
    fi
    
    sleep 3  # API制限対策
    echo ""
done
```

### 5.4 確認

```bash
echo "=== 翻訳結果確認 ==="
for file in "${FILES[@]}"; do
    echo ""
    echo "=== $file ==="
    head -25 "content/ja/glossary/$file" | grep -E "(title:|e-title:|term:|url:)"
done
```

**期待される出力**:
```
=== Active-Learning.md ===
title: "Active Learning（アクティブラーニング）"
e-title: "Active Learning"
term: "あくてぃぶらーにんぐ"
url: "/ja/glossary/Active-Learning/"

=== Aspect-Based-Sentiment-Analysis.md ===
title: "Aspect-Based Sentiment Analysis（アスペクトベース感情分析）"
e-title: "Aspect-Based Sentiment Analysis"
term: "あすぺくとべーすかんじょうぶんせき"
url: "/ja/glossary/Aspect-Based-Sentiment-Analysis/"
```

---

## 6. トラブルシューティング

### Q1: e-title, term, url が追加されない

**原因**: 古いバージョンのスクリプトを使用している

**解決策**:
```bash
# スクリプトにurl自動追加機能があるか確認
grep 'fm_ja\["url"\]' scripts/translate_glossary_en_to_ja.py

# 見つからない場合
# → scripts/translate_glossary_en_to_ja_IMPROVED.py を使用するか、
#    スクリプトを更新してください
```

### Q2: APIエラー "ANTHROPIC_API_KEY is not set"

**原因**: 環境変数が設定されていない

**解決策**:
```bash
# 確認
echo $ANTHROPIC_API_KEY

# 設定
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# .envファイル確認
cat .env | grep API_KEY
```

### Q3: termの読み仮名が正しくない

**原因**: Claude APIが生成するため、まれに不正確な場合がある

**解決策**: 手動で修正
```bash
# ファイルを開いて修正
vim content/ja/glossary/Active-Learning.md

# termフィールドを修正
term: "正しいひらがな"
```

### Q4: Rate limit exceeded

**原因**: APIリクエスト数制限

**解決策**: バッチ処理にsleep追加
```bash
for file in "${FILES[@]}"; do
    python scripts/translate_glossary_en_to_ja.py --one-file "$file"
    sleep 5  # 5秒待機
done
```

---

## 7. クイックリファレンス

### 7.1 基本コマンド

```bash
# プロジェクトルート移動
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

# APIキー設定
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 翻訳
python scripts/translate_glossary_en_to_ja.py --one-file Active-Learning.md

# 確認
head -25 content/ja/glossary/Active-Learning.md | grep -E "(e-title|term|url):"
```

### 7.2 重要パス

| 項目 | パス |
|------|------|
| プロジェクトルート | `/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate` |
| 英語グロッサリー | `content/en/glossary/` |
| 日本語グロッサリー | `content/ja/glossary/` |
| 翻訳スクリプト | `scripts/translate_glossary_en_to_ja.py` |
| 用語リストCSV | `docs/prioritized_keywords.csv` |
| APIキー | `.env` |
| このマニュアル | `docs/GLOSSARY_CREATION_TRANSLATION_MANUAL.md` |

### 7.3 フィールド早見表

#### 英語版（9フィールド）
```yaml
title: "Active Learning"
date: 2025-12-19
translationKey: active-learning
description: "A machine learning process..."
keywords: [5-8個、小文字、英語]
category: "AI Chatbot & Automation"
type: glossary
draft: false
```

#### 日本語版（12フィールド）
```yaml
title: "Active Learning（アクティブラーニング）"
date: 2025-12-19
translationKey: active-learning
description: "機械学習プロセス..."
keywords: [5-8個、日本語]
category: "AI Chatbot & Automation"  # 英語のまま
type: glossary
draft: false
e-title: "Active Learning"  # ✅ 自動追加
term: "あくてぃぶらーにんぐ"  # ✅ 自動追加
url: "/ja/glossary/Active-Learning/"  # ✅ 自動追加
```

---

## まとめ

### ✅ 翻訳スクリプトの自動処理

翻訳スクリプト `scripts/translate_glossary_en_to_ja.py` は以下を**自動的に処理**します：

1. **title**: 英語 → 日本語（英語+カタカナ形式）
2. **description**: 英語 → 日本語
3. **keywords**: 英語配列 → 日本語配列
4. **e-title**: 英語タイトルを自動追加
5. **term**: Claude APIがひらがな読みを自動生成
6. **url**: `/ja/glossary/{filename}/` を自動生成
7. **内部リンク**: `/en/glossary/` → `/ja/glossary/` に書き換え

### ❌ 手動作業は不要

以下のフィールドは**自動追加**されるため、手動で追加する必要はありません：
- e-title
- term
- url

### 🎉 翻訳後すぐに使用可能

翻訳完了後、日本語版ファイルはそのまま使用できます。追加の編集作業は不要です。

---

**作成者**: Takazumi  
**最終更新**: 2025-12-19  
**バージョン**: 2.0（自動追加版）  
**保存先**: `docs/GLOSSARY_CREATION_TRANSLATION_MANUAL.md`
