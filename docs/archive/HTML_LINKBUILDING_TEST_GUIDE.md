# HTML内部リンク検証ガイド

このドキュメントでは、MDファイルをクリーンな状態に保ちながら、HTMLビルド時に内部リンクを追加するアプローチの検証手順を説明します。

---

## ⚠️ 廃止（アーカイブ）

この検証フロー（`public-test/` を使う運用）は廃止しました。

今後は以下の標準フローに統一します。

- **Start Here（入口）**: `docs/00_START_HERE.md`
- **内部リンク Quick Start**: `docs/INTERNAL_LINKING_QUICK_START.md`
- **内部リンク System Guide**: `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`

以降の内容は、過去の検証経緯として残しています（再実施は推奨しません）。

## 検証の目的

| 比較項目 | MD編集方式 | HTML編集方式 |
|---------|-----------|-------------|
| ソース管理 | リンクがMDに残る | MDはクリーン |
| 用語集更新時 | 全MD再処理が必要 | 次回ビルドで自動適用 |
| デバッグ | 簡単 | やや複雑 |
| 日本語太字 | 問題あり | 自然に解決 |

---

## ディレクトリ構成

```
hugo-boilerplate/
├── content/                    # 本番コンテンツ（リンク付き）
│   ├── ja/blog/
│   └── en/blog/
│
├── content-clean/              # クリーンコンテンツ（リンク無し）
│   ├── ja/blog/                # ← 検証用
│   └── en/blog/
│
├── public/                     # 本番HTMLビルド出力
│
├── public-test/                # テスト用HTMLビルド出力
│   ├── ja/
│   └── en/
│
└── data/linkbuilding/          # リンクビルディング設定
    ├── ja_automatic.json
    └── en_automatic.json
```

---

## 検証手順

### Step 1: クリーンなMDを作成

現在の内部リンク付きMDから、リンクを除去したクリーン版を作成します。

```bash
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

# 日本語ブログをクリーン化
python3 scripts/create_clean_content.py \
    content/ja/blog \
    content-clean/ja/blog \
    --force

# 英語ブログをクリーン化
python3 scripts/create_clean_content.py \
    content/en/blog \
    content-clean/en/blog \
    --force

# 用語集もクリーン化（必要に応じて）
python3 scripts/create_clean_content.py \
    content/ja/glossary \
    content-clean/ja/glossary \
    --force

python3 scripts/create_clean_content.py \
    content/en/glossary \
    content-clean/en/glossary \
    --force
```

**プレビュー（dry-run）で確認：**
```bash
python3 scripts/create_clean_content.py \
    content/ja/blog \
    content-clean/ja/blog \
    --dry-run
```

---

### Step 2: テスト用Hugoビルド

クリーンなコンテンツからHTMLをビルドします。

```bash
# content-clean を使ってビルド（テスト用ディレクトリに出力）
hugo --contentDir content-clean --destination public-test

# または、hugoの設定を一時的に変更してビルド
# config.toml / hugo.toml を編集せずにコマンドラインで指定
```

**注意**: テスト用なので本番の `public/` ディレクトリは変更しません。

---

### Step 3: リンクビルディング用JSONを生成

CSVデータベースからJSON形式に変換します（linkbuilding.py用）。

```bash
# 日本語用JSON生成
python3 scripts/build_link_database.py \
    --glossary-dir content/ja/glossary \
    --output data/linkbuilding/ja_automatic.json \
    --lang ja \
    --format json

# 英語用JSON生成
python3 scripts/build_link_database.py \
    --glossary-dir content/en/glossary \
    --output data/linkbuilding/en_automatic.json \
    --lang en \
    --format json
```

**注意**: `build_link_database.py` がJSON出力に対応していない場合は、以下の変換スクリプトを使用：

```bash
# CSVからJSONへの変換（必要な場合）
python3 -c "
import csv
import json
from pathlib import Path

def csv_to_json(csv_path, json_path):
    keywords = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            keywords.append({
                'Keyword': row.get('keyword', ''),
                'URL': row.get('url', ''),
                'Title': row.get('title', ''),
                'Priority': int(row.get('priority', 0)),
                'Exact': row.get('exact_match', '').lower() in ('true', '1', 'yes')
            })
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({'keywords': keywords}, f, ensure_ascii=False, indent=2)
    
    print(f'Converted {len(keywords)} keywords: {csv_path} -> {json_path}')

csv_to_json('databases/link_database_ja.csv', 'data/linkbuilding/ja_automatic.json')
csv_to_json('databases/link_database_en.csv', 'data/linkbuilding/en_automatic.json')
"
```

---

### Step 4: HTML内部リンクを追加

テスト用HTMLディレクトリに対してリンクビルディングを実行します。

```bash
# 日本語HTMLにリンク追加
python3 scripts/linkbuilding.py \
    -a data/linkbuilding/ja_automatic.json \
    -d public-test/ja \
    --language ja

# 英語HTMLにリンク追加
python3 scripts/linkbuilding.py \
    -a data/linkbuilding/en_automatic.json \
    -d public-test/en \
    --language en
```

**dry-runで確認：**
```bash
python3 scripts/linkbuilding.py \
    -a data/linkbuilding/ja_automatic.json \
    -d public-test/ja \
    --language ja \
    --dry-run
```

---

### Step 5: 検証と比較

#### 5.1 リンク数の確認

```bash
# 追加されたリンク数を確認
grep -r 'data-lb="1"' public-test/ja/blog/ | wc -l
grep -r 'data-lb="1"' public-test/en/blog/ | wc -l
```

#### 5.2 日本語太字問題の確認

```bash
# 太字内のリンクを確認（HTMLでは自然に処理される）
grep -r '<strong>.*<a.*</a>.*</strong>' public-test/ja/blog/ | head -5
grep -r '<a.*<strong>.*</strong>.*</a>' public-test/ja/blog/ | head -5
```

#### 5.3 ローカルサーバーで確認

```bash
# テスト用HTMLをローカルサーバーで確認
cd public-test
python3 -m http.server 8080

# ブラウザで確認
open http://localhost:8080/ja/blog/
```

#### 5.4 MD編集方式との比較

```bash
# 本番（MD編集済み）のリンク数
grep -r '\[.*\](/ja/glossary/' content/ja/blog/ | wc -l

# テスト（HTML編集）のリンク数
grep -r 'data-lb="1"' public-test/ja/blog/ | wc -l
```

---

## 検証チェックリスト

| チェック項目 | 確認方法 | 期待結果 |
|-------------|---------|---------|
| 日本語キーワードがマッチする | `grep -r 'チャットボット' public-test/ja/` | リンク化されている |
| 英語キーワードがマッチする | `grep -r 'chatbot' public-test/en/` | リンク化されている |
| コードブロック内はスキップ | `<pre>` `<code>` 内を確認 | リンク化されていない |
| 見出し内はスキップ | `<h1>`〜`<h6>` 内を確認 | リンク化されていない |
| 既存リンク内はスキップ | `<a>` 内を確認 | 二重リンクになっていない |
| 太字が正しくレンダリング | ブラウザで確認 | 崩れていない |
| 同一キーワードの制限 | 1ページ内のリンク数を確認 | 2-3回まで |

---

## 問題が発生した場合

### 日本語キーワードがマッチしない

`linkbuilding.py` の `_create_pattern` メソッドを確認：

```python
def _has_cjk(self) -> bool:
    # CJK文字の判定ロジック
    ...

def _create_pattern(self) -> re.Pattern:
    if self._has_cjk():
        # 日本語: 直接マッチング
        pattern = f'({escaped})'
    else:
        # 英語: ワードバウンダリー使用
        pattern = r'(?<![A-Za-z0-9_])' + escaped + r'(?![A-Za-z0-9_])'
```

### リンクが多すぎる/少なすぎる

`LinkConfig` の設定を調整：

```python
max_replacements_per_keyword: int = 2    # キーワードごとの最大リンク数
max_replacements_per_page: int = 30      # ページごとの最大リンク数
max_paragraph_density: int = 30          # 段落内のリンク密度
```

---

## 次のステップ

検証が成功したら、以下を検討：

1. **CI/CDへの統合**: `amplify.yml` または GitHub Actions にリンクビルディングを追加
2. **本番MDのクリーン化**: 既存のリンク付きMDを段階的にクリーン版に置き換え
3. **ドキュメント更新**: `INTERNAL_LINK_SYSTEM_GUIDE.md` をHTML編集方式に更新

---

## 関連ファイル

- `scripts/create_clean_content.py` - クリーンMD作成
- `scripts/linkbuilding.py` - HTML編集（日本語対応済み）
- `scripts/linkbuilding_parallel.py` - 並列HTML編集
- `databases/link_database_*.csv` - キーワードデータベース
- `docs/INTERNAL_LINK_SYSTEM_GUIDE.md` - 内部リンクシステムガイド

---

**作成日**: 2025-01-06
