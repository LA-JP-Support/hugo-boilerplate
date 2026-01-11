# Changelog - Internal Linking System

## [2.1.3] - 2026-01-11

### 🐛 Fixed

- **hreflang の `href` に `%!s(<nil>)` が混入する問題を修正**
  - `layouts/partials/helpers/get-language-url.html`: `site.BaseURL` ベースで安全にURLを組み立てるように変更

### 🔄 Changed

- **glossary 配下リンクの小文字正規化を強化**
  - `scripts/linkbuilding.py`: 既存の `<a href>` について、`/glossary/` を含むURLは path を小文字に正規化
  - これにより、既存HTMLに残っていた mixed-case glossary URL も後処理で統一

- **用語集翻訳スクリプトの `url` を小文字生成に統一**
  - `scripts/translate_glossary_en_to_ja.py`: `url: "/ja/glossary/<slug>/"` を小文字で生成

### 📝 Documentation

- `docs/SCRIPTS_USAGE_GUIDE.md`: `translate_glossary_en_to_ja.py` の実際のCLI引数に合わせて更新（model / max-workers / batch-size / skip-existing / csv-path など）

## [2.1.2] - 2026-01-10

### 📝 Documentation

- **ローカルで内部リンク付きプレビュー手順を追加**
  - `docs/INTERNAL_LINKING_QUICK_START.md`: `hugo server` では内部リンクが付かない旨と、静的ビルド + HTML後処理 + 同一ポート配信の手順を追記
- **旧方式（Markdown直接編集）と現行方式（HTML後処理）の位置付けを明確化**
  - `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`: 旧スクリプト（CSV/Markdown編集）を「旧方式」として明示し、現行の `extract_automatic_links.py` + `linkbuilding_parallel.py` へ誘導
- **description最適化のskipped条件を明文化**
  - `docs/SCRIPTS_USAGE_GUIDE.md`: `description` 未設定/フロントマター不正の場合に `skipped` になる点と対処を追記
- **用語集ワークフローの注意点を追記**
  - `WORKFLOW.md`: `hugo server` 単体では内部リンクが付かない点を追記

## [2.1.1] - 2026-01-08

### 🐛 Fixed

- **日本語リンク精度の向上**
  - `Janome` による形態素解析を導入し、複合語の一部（例：「交通信号」内の「通信」）への誤った部分一致リンクを防止
- **太字レンダリング問題の修正**
  - Markdownの太字記法（`**`）が特定の記号（括弧、コロン等）と隣接した場合にレンダリングされない問題を修正
  - `scripts/fix_bold_syntax_to_html.py` を作成し、Markdown内の太字を `<strong>` タグに一括変換（コードブロック等は保護）
- **リンク先マッピングの修正**
  - 「通信」がDTMFページへ誤リンクされる問題を修正（Denylistへ正規化して追加）
  - 「検索拡張生成(RAG)」と「キャッシュ拡張生成(CAG)」のリンク先を適切な日本語ページ（用語集/ブログ）に修正
- **再現性テスト**
  - `linkbuilding-repro.md` を作成し、太字とリンクの競合ケースを網羅的にテスト・検証

### 🔧 Technical Details

- **依存関係**: 日本語処理用に `janome` ライブラリを追加（`linkbuilding.py` 内で条件付きインポート）
- **スクリプト更新**:
  - `linkbuilding.py`: 形態素境界チェックロジックを追加
  - `fix_bold_syntax_to_html.py`: 新規追加（Markdown修正用）

---

## [2.1.0] - 2026-01-08

### 🎯 Major Changes - CSV Database System

**Breaking Changes**: CSVデータベースシステムを導入しました。内部リンクシステムの構造と使用方法が変更されました。

### ✨ Added

- **CSV Database System Guide** (`docs/CSV_DATABASE_SYSTEM_GUIDE.md`)
  - 完全なCSVシステムの役割、構造、使用方法を文書化
  - Description最適化ワークフローを追加
  - CSV→JSON変換プロセスを明確化
- **Description最適化機能**
  - Claude Haiku 4.5を使用した自動最適化
  - 英語1,222件、日本語1,223件のdescription最適化完了
  - マウスオーバー表示用の簡潔な説明文に統一
- **最新CSV Database生成**
  - `databases/link_database_en.csv` (1,222エントリ)
  - `databases/link_database_ja.csv` (1,223エントリ)
  - 最適化されたdescriptionを含む

### 🔄 Changed

- **CSV生成方法の改善**
  - Pythonワンライナーで簡単に生成可能に
  - frontmatterライブラリを使用した安全なパース
  - YAMLエラーの検出と報告機能
- **内部リンクシステムの整理**
  - 日本語「自然言語処理」キーワードをdenylistに追加（404エラー対策）
  - 「AIシステム」のリンク先を正しい人工知能ページに修正
  - ja.yamlから279個のtitleを最適化（簡易的な「〜の用語集ページ」を削除）

### 🗄️ Fixed

- **404エラーの修正**
  - 存在しないページへのリンクを削除
  - 自然言語処理関連の3つの不正なエントリを削除
- **内部リンクの問題修正**
  - ブログ記事への内部リンク追加（18記事、267リンク）
  - 用語集ページへの内部リンク追加（1,244ページ、18,415リンク）

### 📝 Documentation

- **新規ドキュメント**
  - `docs/CSV_DATABASE_SYSTEM_GUIDE.md` - CSVシステム完全ガイド
- **運用ドキュメント追加**
  - `docs/00_START_HERE.md` - AI作業の入口（権威ファイル/ディレクトリ構造/作業別ナビ）
- **検証フローの廃止（アーカイブ化）**
  - `docs/HTML_LINKBUILDING_TEST_GUIDE.md` - `public-test/` を使う検証フローは廃止（履歴として残す）
- **更新予定**
  - `docs/INTERNAL_LINK_SYSTEM_GUIDE.md` - CSV統合情報を追加予定
  - `README.md` - CSVシステムへの参照を追加予定

### 🔧 Technical Details

**新しい推奨ワークフロー**:

```bash
# 1. クリーンなMarkdownからHugoビルド
hugo --contentDir content-clean --destination public --cleanDestinationDir

# 2. 自動キーワード辞書の更新（必要に応じて）
python3 scripts/extract_automatic_links.py --content-dir content-clean/en/ --output data/linkbuilding/en_automatic.json
python3 scripts/extract_automatic_links.py --content-dir content-clean/ja/ --output data/linkbuilding/ja_automatic.json

# 3. HTML後処理で内部リンク追加
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

**データフロー**:
1. `content-clean/` (Markdown) → Hugo → `public/` (HTML)
2. `data/linkbuilding/*.json` + `databases/danger_terms_*.csv` → `linkbuilding_parallel.py`
3. `public/` (HTML + 内部リンク)

---

## [2.0.0] - 2026-01-07

### 🎯 Major Changes - HTML後処理方式への統一

**Breaking Changes**: 内部リンクシステムを**HTML後処理方式**に完全統一しました。Markdownファイルを直接編集する旧方式は非推奨となり、アーカイブされました。

### ✨ Added

- **HTML後処理方式の確立**
  - `linkbuilding.py`: BeautifulSoupを使用した安全なHTML編集
  - `linkbuilding_parallel.py`: EN/JAの並列処理ラッパー
  - クリーンなMarkdownソース（`content-clean/`）の維持

- **重複除外機能**
  - `extract_automatic_links.py`: キーワード辞書生成時に自動的に重複を除外
  - 同一キーワードの最高優先度版のみを保持
  - EN: 3214個 → 1956個（重複除外）
  - JA: 2438個 → 1934個（重複除外）

- **Denylist統合**
  - `linkbuilding.py`: `--denylist` 引数で除外語CSVを指定可能
  - 言語コード（en/ja）を自動検出し、`databases/danger_terms_{lang}.csv` を自動読み込み
  - `linkbuilding_parallel.py`: `--denylist-dir` 引数で一括適用

- **太字処理改善**
  - `try_wrap_bold_tag()`: 太字タグ全体がキーワードにマッチする場合、タグ全体をリンクで囲む
  - 太字フォーマットの保持を改善

- **新規ユーティリティスクリプト**
  - `convert_link_database_csv_to_json.py`: CSV形式の辞書をJSON形式に変換
  - `analyze_keyword_sources.py`: EN/JAのキーワード統計を詳細分析

### 🔄 Changed

- **ワークフロー変更**
  - 旧: Markdown編集 → Hugoビルド
  - 新: Hugoビルド → HTML後処理

- **データ形式**
  - 主要形式: JSON/YAML（`data/linkbuilding/`）
  - CSV形式: 参考用・変換元として保持（`databases/`）

### 🗄️ Deprecated

以下のスクリプトは `scripts/archived_markdown_based/` に移動し、非推奨となりました：

- `add_internal_links.py` - Markdownファイルに直接リンクを挿入
- `add_links_from_database.py` - CSVデータベースからMarkdownにリンク追加
- `remove_internal_links.py` - Markdownからリンクを削除

**理由**:
- Markdownソースの可読性低下
- Git履歴の汚染
- リンク戦略変更の困難さ
- 保守性の問題

### 📊 Performance

- **処理速度**: EN/JA並列処理で約2.5分（合計2,503ファイル）
- **リンク数**: 
  - EN: 18,816リンク（1,263ファイル）
  - JA: 16,827リンク（1,240ファイル）
  - 合計: 35,643リンク

### 🐛 Fixed

- `linkbuilding.py`: `--dry-run` モードでファイルが書き込まれる問題を修正
- `extract_automatic_links.py`: 重複キーワードが生成される問題を修正
- `linkbuilding.py`: 太字タグ内でリンクを作成する際の `NoneType` エラーを修正
  - `linkbuilding.py`: 言語コードの正規化処理を改善
- **太字処理の修正 (v2.1.1)**
  - `try_wrap_bold_tag` を削除し、粒度の細かいリンク注入に変更
  - `**Keyword(KW)**` のような複合ケースや、入れ子リンクによる表示崩れを防止
  - Markdown内の不正な太字（スペース入り `** A **`）を自動修正するスクリプト適用

### 📝 Documentation

- `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`: v2.0.0対応に全面改訂
- `scripts/archived_markdown_based/README.md`: アーカイブ理由と代替方法を記載
- `CHANGELOG_INTERNAL_LINKING.md`: 本ファイルを新規作成

### 🔧 Technical Details

**新しい推奨ワークフロー**:

```bash
# 1. クリーンなMarkdownからHugoビルド
hugo --contentDir content-clean --destination public --cleanDestinationDir

# 2. 自動キーワード辞書の更新（必要に応じて）
python3 scripts/extract_automatic_links.py --content-dir content-clean/en/ --output data/linkbuilding/en_automatic.json
python3 scripts/extract_automatic_links.py --content-dir content-clean/ja/ --output data/linkbuilding/ja_automatic.json

# 3. HTML後処理で内部リンク追加
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

**データフロー**:
1. `content-clean/` (Markdown) → Hugo → `public/` (HTML)
2. `data/linkbuilding/*.json` + `databases/danger_terms_*.csv` → `linkbuilding_parallel.py`
3. `public/` (HTML + 内部リンク)

---

## [1.x.x] - 2025-01-06以前

### Legacy System (Markdown-based)

旧バージョンの履歴は `scripts/archived_markdown_based/` を参照してください。

主な特徴:
- Markdownファイルを直接編集
- CSV形式のデータベース使用
- 単一言語処理

---

## Migration Guide - v1.x → v2.0.0

### 移行手順

1. **Markdownソースのクリーンアップ**
   ```bash
   # 既存のMarkdownから内部リンクを削除（必要に応じて）
   # content/ → content-clean/ にコピー
   ```

2. **新しいワークフローの採用**
   ```bash
   # 上記「新しい推奨ワークフロー」を参照
   ```

3. **旧スクリプトの使用停止**
   - `add_internal_links.py` の使用を停止
   - `add_links_from_database.py` の使用を停止
   - `remove_internal_links.py` は不要（HTMLを再生成するだけ）

### 互換性

- **データ**: `databases/*.csv` は引き続き使用可能（denylistとして）
- **設定**: 新しいJSON/YAML形式への移行を推奨
- **出力**: HTML形式は変更なし（`data-lb="1"` マーカー付き）

---

## Version Numbering

- **Major (X.0.0)**: システムアーキテクチャの大幅変更
- **Minor (0.X.0)**: 新機能追加
- **Patch (0.0.X)**: バグ修正

---

**Maintained by**: Takazumi  
**Repository**: hugo-boilerplate  
**Last Updated**: 2026-01-07
