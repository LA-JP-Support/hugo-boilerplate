# FlowHunt Translation Pipeline

統合翻訳パイプラインの使い方ガイド

## 概要

`pipeline_translate.py` は、FlowHunt生成記事を英語から日本語に翻訳する全工程を自動化します。

## ワークフロー

```
content-drafts/en/*.md (FlowHunt生成)
    ↓
1. cleanup_flowhunt_output.py → クリーンアップ
    ↓
2. enrich_glossary.py → キーワード・リンク追加（EN）
    ↓
3. → content/en/glossary/ にコピー
    ↓
4. translate_glossary_en_to_ja.py → Claude翻訳
    ↓
5. enrich_glossary.py → キーワード・リンク追加（JA）
    ↓
6. add_kana_index.py → 読み仮名追加
    ↓
7. fix_term_readings_ja.py → term修正
    ↓
8. compare_outline.py → 見出し差分チェック
    ↓
9. publish_drafts.py → draft: false（オプション）
```

## 使い方

### 前提条件

```bash
# .env に Claude API キーを設定
echo 'CLAUDE_API_KEY="sk-ant-..."' >> .env

# 依存パッケージをインストール
pip install python-dotenv anthropic pyyaml
```

### 新規記事を自動検出して処理

```bash
# content-drafts/en/ に新規記事を配置後
python scripts/pipeline_translate.py --auto
```

### 特定ファイルのみ処理

```bash
python scripts/pipeline_translate.py --file Copilot.md
```

### ドライラン（変更なし）

```bash
python scripts/pipeline_translate.py --auto --dry-run
```

### 特定ステップから開始

```bash
# 翻訳ステップから開始（cleanup, enrich_en, copy_to_content をスキップ）
python scripts/pipeline_translate.py --file Copilot.md --from-step translate
```

### 公開まで一括処理

```bash
python scripts/pipeline_translate.py --auto --publish
```

## ステップ一覧

| ステップ | 説明 |
|----------|------|
| `cleanup` | FlowHunt出力のクリーンアップ |
| `enrich_en` | 英語キーワード・リンク追加 |
| `copy_to_content` | content/en/glossary/ へコピー |
| `translate` | Claude APIで日本語翻訳 |
| `enrich_ja` | 日本語キーワード・リンク追加 |
| `add_kana` | 読み仮名メタデータ追加 |
| `fix_term` | term読みの修正（漢字→かな） |
| `compare` | EN/JA見出し差分チェック |
| `refresh_links` | **全記事**の内部リンクを更新（存在するページのみ） |
| `publish` | draft: false に設定 |

### refresh_links ステップについて

新しい記事を追加すると、既存の記事からその新しい記事へのリンクが可能になります。
`refresh_links` ステップは、全ての記事を再スキャンし、存在するページへのリンクのみを挿入します。

**重要**: 辞書に登録されていても、対応するページが存在しない場合はリンクされません。

## 設定ファイル

### config/keyword_dictionary.json (EN)

英語記事用のキーワード・リンク辞書

### config/keyword_dictionary_ja.json (JA)

日本語記事用のキーワード・リンク辞書。日本語独自の用語を追加可能。

```json
{
  "AIコパイロット": {
    "keywords": ["AIコパイロット", "コパイロット"],
    "link": "/ja/glossary/copilot/",
    "aliases": ["AIコパイロット", "コパイロット", "AI Copilot"]
  }
}
```

## ログ

処理ログは `logs/pipeline_YYYYMMDD_HHMMSS.log` に保存されます。

## トラブルシューティング

### API キーエラー

```
CLAUDE_API_KEY not set. Add to .env or export.
```

→ `.env` ファイルに `CLAUDE_API_KEY` を設定してください。

### 翻訳が途中で切れる

→ `translate_glossary_en_to_ja.py` の `max_tokens` を増やしてください（現在16000）。

### 見出し差分が検出される

→ 翻訳時にセクションが欠落している可能性があります。手動で確認してください。

## 関連スクリプト

- `cleanup_flowhunt_output.py` - FlowHunt出力クリーンアップ
- `enrich_glossary.py` - キーワード・リンク追加
- `translate_glossary_en_to_ja.py` - Claude翻訳
- `add_kana_index.py` - 読み仮名追加
- `fix_term_readings_ja.py` - term読み修正
- `compare_outline.py` - 見出し比較
- `publish_drafts.py` - 一括公開
