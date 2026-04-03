# Internal Linking Quick Start Guide

**バージョン**: v2.0.0  
**最終更新**: 2026-01-08

---

## ⚠️ 重要: HTML後処理方式への統一

v2.0.0より、内部リンクシステムは**HTML後処理方式**に統一されました。

**❌ 使用禁止**:
- `add_internal_links.py`
- `add_links_from_database.py`
- `remove_internal_links.py`

これらは `scripts/archived_markdown_based/` に移動されました。

**✅ 使用推奨**:
- `linkbuilding_parallel.py` (メインツール)
- `linkbuilding.py` (単一言語処理)

---

## 🚀 クイックスタート（5分で開始）

### 1. Hugoサイトをビルド

```bash
hugo --destination public --cleanDestinationDir
```

**ポイント**:
- `content/`: Markdownソース（リンクなし）
- `public/`: 生成されたHTML（リンク追加前）

### 2. 内部リンクを追加

```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

**処理内容**:
- EN/JAを並列処理
- 自動的にdenylist（除外語）を適用
- 約2-3分で完了

### 3. 結果確認

```bash
# リンク数を確認
grep -r 'data-lb="1"' public/en/ | wc -l
grep -r 'data-lb="1"' public/ja/ | wc -l
```

**期待される結果**:

サイト規模により増減しますが、EN/JAともに `data-lb="1"` が十分な件数になることを確認してください。

---

## 🧪 ローカルで「内部リンク付き」を確認する（同じポートで切り替え）

 `hugo server` は **HTML後処理（内部リンク付与）を自動実行しない**ため、ブラウザ上で内部リンクを確認したい場合は、内部リンク適用済みの静的HTMLを配信して確認します。

```bash
# 1) いったん hugo server を止める（同じポートを使う場合）

# 2) 静的ビルド（成果物: public/ は .gitignore 対象）
hugo --baseURL http://localhost:1313/ --destination public --cleanDestinationDir

# 3) HTML後処理で内部リンク追加（EN/JA両方）
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases

# 4) 静的サーバで配信（同じポート 1313）
python3 -m http.server 1313 --bind 127.0.0.1 --directory public

# 5) ブラウザで確認
# http://localhost:1313/ja/...
# http://localhost:1313/en/...
```

---

## 📁 ディレクトリ構造

```
smartweb/
├── content/                # Markdownソース
│   ├── en/
│   └── ja/
├── data/linkbuilding/      # リンク設定ファイル
│   ├── en_automatic.json   # EN自動キーワード（1956件）
│   ├── ja_automatic.json   # JA自動キーワード（1934件）
│   ├── en.yaml             # EN手動キーワード（334件）
│   └── ja.yaml             # JA手動キーワード（328件）
├── databases/              # Denylist（除外語）
│   ├── danger_terms_en.csv # EN除外語（9件）
│   └── danger_terms_ja.csv # JA除外語（10件）
└── public/                 # 生成されたHTML（リンク付き）
    ├── en/
    └── ja/
```

---

## 🔧 よくある操作

### キーワード辞書を更新

新しい記事を追加した後、キーワード辞書を更新します：

```bash
# EN
python3 scripts/extract_automatic_links.py \
  --content-dir content/en/ \
  --output data/linkbuilding/en_automatic.json

# JA
python3 scripts/extract_automatic_links.py \
  --content-dir content/ja/ \
  --output data/linkbuilding/ja_automatic.json
```

### 除外語（Denylist）を追加

誤ってリンクされる単語を除外します：

```bash
# databases/danger_terms_ja.csv に追加
echo "AI,ai" >> databases/danger_terms_ja.csv
```

### 単一言語のみ処理

ENのみ、またはJAのみを処理する場合：

```bash
# ENのみ
python3 scripts/linkbuilding.py \
  -k data/linkbuilding/en.yaml \
  -a data/linkbuilding/en_automatic.json \
  -d public/en \
  --language EN \
  --denylist databases/danger_terms_en.csv \
  --max-links 15 --max-keyword 1 --max-url 3

# JAのみ
python3 scripts/linkbuilding.py \
  -k data/linkbuilding/ja.yaml \
  -a data/linkbuilding/ja_automatic.json \
  -d public/ja \
  --language JA \
  --denylist databases/danger_terms_ja.csv \
  --max-links 15 --max-keyword 1 --max-url 3
```

### Dry-run（テスト実行）

実際にファイルを変更せずにテストします：

```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --dry-run
```

---

## 🎯 ベストプラクティス

### 1. Markdownはクリーンに保つ

**✅ 良い例** (`content/`):
```markdown
AIチャットボットは自然言語処理を使用します。
```

**❌ 悪い例** (旧方式):
```markdown
[AIチャットボット](/ja/glossary/chatbot/)は[自然言語処理](/ja/glossary/nlp/)を使用します。
```

### 2. 定期的にキーワード辞書を更新

新しい用語集記事を追加したら、`extract_automatic_links.py` を実行してキーワード辞書を更新します。

### 3. Denylistで誤リンクを防止

一般的な単語（例: "AI", "API"）が誤ってリンクされる場合は、denylistに追加します。

### 4. リンク数を制限

過剰なリンクはユーザー体験を損ないます。デフォルト設定を推奨：
- `--max-links 15`: 1ページあたり最大15リンク
- `--max-keyword 1`: 同じキーワードは1回のみ
- `--max-url 3`: 同じURLへは最大3回

### 5. glossary のURLは小文字に統一する

- `public/{en,ja}` のHTML後処理では、`/glossary/` 配下の `href` を小文字に正規化します（ケースセンシティブ環境での404対策）。
- `linkbuilding_parallel.py` は基本的に `public/en` と `public/ja` を処理対象とします。`public/files` などの別フォルダに置いたHTMLは対象外なので、必要なら別途 `scripts/linkbuilding.py -d <dir>` で処理してください。

---

## 🐛 トラブルシューティング

### リンクが追加されない

**原因**: キーワード辞書が古い、またはdenylistで除外されている

**解決策**:
```bash
# キーワード辞書を再生成
python3 scripts/extract_automatic_links.py --content-dir content/ja/ --output data/linkbuilding/ja_automatic.json

# 統計を確認
python3 scripts/analyze_keyword_sources.py
```

### リンクが重複している

**原因**: 同じHTMLファイルに対して複数回処理を実行した

**解決策**:
```bash
# HTMLを再生成
hugo --destination public --cleanDestinationDir

# 内部リンクを再追加
python3 scripts/linkbuilding_parallel.py --linkbuilding-dir data/linkbuilding --public-dir public --denylist-dir databases
```

### `extract_automatic_links.py` が失敗する（`What? faq already exists?`）

**原因**: TOMLフロントマターで FAQ を複数定義する際に、`[faq]` を繰り返している（TOMLのテーブル重複）

**解決策**:

- FAQが配列になるように `[[faq]]` を使用する

```toml
[[faq]]
question = "..."
answer = "..."

[[faq]]
question = "..."
answer = "..."
```

**探し方（例）**:

```bash
grep -R '^\[faq\]' content/en/blog
```

### ENだけリンクがほとんど増えない

**原因**: `linkbuilding_parallel.py` は「ENは `public/` 直下にある」前提で処理します。

このリポジトリのビルド結果では EN は `public/en/` 配下になるため、ENだけ別コマンドで `public/en` を対象に実行します。

**解決策（推奨）**:

```bash
# ENのみ（public/en を対象にする）
python3 scripts/linkbuilding.py \
  -k data/linkbuilding/en.yaml \
  -a data/linkbuilding/en_automatic.json \
  -d public/en \
  --language EN \
  --denylist databases/danger_terms_en.csv \
  --max-links 15 --max-keyword 1 --max-url 3
```

### 処理が遅い

**原因**: 並列処理のワーカー数が多すぎる、またはメモリ不足

**解決策**:
```bash
# ワーカー数を減らす
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --max-workers 2
```

---

## 📚 詳細ドキュメント

- **Start Here（入口）**: `docs/00_START_HERE.md`
- **システム全体**: `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`
- **運用（スクリプト）**: `docs/SCRIPTS_USAGE_GUIDE.md`
- **用語集最適化（検索/表記揺れ）**: `docs/GLOSSARY_OPTIMIZATION_GUIDE.md`
- **変更履歴**: `CHANGELOG_INTERNAL_LINKING.md`
- **アーカイブ**: `scripts/archived_markdown_based/README.md`

---

## ⚡ まとめ

### 標準ワークフロー

```bash
# 1. Hugoビルド
hugo --destination public --cleanDestinationDir

# 2. 内部リンク追加
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases

# 3. 確認
grep -r 'data-lb="1"' public/ | wc -l
```

### 重要なポイント

1. **Markdownはクリーン**に保つ（`content/`）
2. **HTML後処理**でリンクを追加（`linkbuilding_parallel.py`）
3. **Denylist**で誤リンクを防止（`databases/danger_terms_*.csv`）
4. **定期的に更新**（キーワード辞書の再生成）

---

**問題が発生した場合**: `docs/INTERNAL_LINK_SYSTEM_GUIDE.md` の「トラブルシューティング」セクションを参照してください。
