---
name: translate
description: "英語→日本語翻訳のワークフロー。翻訳ルール（太字構文、ZWS、用語統一）の適用、翻訳スクリプトの実行、品質検証を含む。"
---

# 翻訳ワークフロー

英語コンテンツを日本語に翻訳する。スクリプトによるバッチ翻訳と、Claude自身による手動翻訳の両方に対応。
対象: $ARGUMENTS

## 翻訳5大ルール（必ず遵守）

1. **太字の助詞**: `**Anthropic**のClaude` (正) / `**Anthropicの**Claude` (誤)
   - 日本語助詞（の、は、が、を、に、へ、と、から、まで、より、で、や）は `**` の外
2. **太字 + 日本語句読点**: 閉じ `**` の後に `&#8203;`（ZWS）を追加
   - `**アジア（シンガポール）**&#8203;を推奨` (正)
3. **太字の閉じ忘れ禁止**: 開き `**` には必ず閉じ `**` をペアにする
4. **固有名詞・技術用語は英語保持**: ChatGPT, API, Claude, Hugo 等はそのまま
5. **文の区切りで改行**: 1-3文ごとに改行してMarkdownの可読性を保つ

## 翻訳フォーマットルール詳細

!`cat docs/TRANSLATION_GUIDELINES.md`

## 翻訳用語集（165+ 用語）

!`cat docs/TRANSLATION_GLOSSARY.md`

## 用語集タイトル翻訳判定（Decision Tree）

!`cat docs/GLOSSARY_TITLE_TRANSLATION_GUIDE.md`

## スクリプトによる翻訳

### Glossary翻訳（推奨）
```bash
# 単一ファイル
python scripts/translate_glossary_en_to_ja.py --one-file {filename}.md

# バッチ翻訳（未翻訳を自動検出）
python scripts/translate_glossary_en_to_ja.py \
  --skip-existing \
  --max-workers 5 \
  --model claude-sonnet-4-5-20250929 \
  --style-guide docs/TRANSLATION_GUIDELINES.md
```

### Blog翻訳
```bash
python scripts/translate_blog_with_flowhunt.py
```

## Claude自身が翻訳する場合の手順

1. 原文（EN）ファイルを読む
2. 上記5大ルール + 用語集を適用して翻訳
3. JA版フロントマターを適切に設定:
   - `translationKey`: EN版と同じ値
   - `url`: `/ja/{type}/{slug}/`
   - Glossary JA版では追加: `e-title`, `term`（ひらがな読み）
4. 翻訳結果をファイルに書き出す

## 日本語Glossary固有の後処理

```bash
# 用語読み修正
python scripts/fix_term_readings_ja.py --ja-dir content/ja/glossary

# かなインデックス追加
python scripts/add_kana_index.py --glossary-dir content/ja/glossary
```

## 品質チェック

- [ ] 太字構文が正しい（助詞が `**` の外）
- [ ] 太字 + 日本語句読点に `&#8203;` あり
- [ ] 全ての `**` がペアで閉じている
- [ ] 技術用語・ブランド名が英語のまま
- [ ] フロントマターのキーは英語のまま、値のみ翻訳
- [ ] URL・リンク構文は未翻訳
- [ ] コードブロック・インラインコード内は未翻訳
- [ ] 段落が適切に改行されている

### 自動検証
```bash
python scripts/validate_frontmatter.py --check-translations
python scripts/validate_translation.py databases/glossary-keywords-ja.csv content/ja/glossary
```
