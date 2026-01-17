# Internal Linking Adoption Guide（他プロジェクト導入ガイド）

このドキュメントは、このリポジトリで運用している **HTML後処理方式** の内部リンク機能（Hugoビルド後の `public/` HTMLへリンクを付与）を、**別プロジェクトへ移植/導入**するための手順をまとめたものです。

- 標準フロー（本リポジトリ）
  - `content-clean/` (Markdown) → Hugo → `public/` (HTML)
  - `scripts/linkbuilding_parallel.py` / `scripts/linkbuilding.py` で `public/` を後処理して内部リンク付与
- 重要な原則
  - Markdown（`content/` や `content-clean/`）に内部リンクを直接挿入しない
  - `public/` は成果物（Artifact）として都度生成し、Git管理しない

---

## 1. 何をコピーすれば動くか（最小セット）

導入先プロジェクトに以下をコピーすれば、HTML後処理での内部リンク付与が動作します。

### 必須（HTML後処理の本体）

- `scripts/linkbuilding.py`
- `scripts/linkbuilding_parallel.py`

### 必須（リンク辞書）

- `data/linkbuilding/`
  - `en_automatic.json` / `ja_automatic.json`（自動辞書）
  - `en.yaml` / `ja.yaml`（手動辞書）
  - `*_synonyms.yaml`（任意、同義語辞書）

### 推奨（誤リンク防止）

- `databases/`
  - `danger_terms_en.csv` / `danger_terms_ja.csv`（Denylist）

### 任意（自動辞書を導入先で生成したい場合）

- `scripts/extract_automatic_links.py`

---

## 2. 依存関係（Python）

導入先で最低限必要なPythonパッケージは次の通りです。

### linkbuilding 実行に必要

- `beautifulsoup4`
- `lxml`
- `pyyaml`

### 日本語の精度改善（推奨）

- `janome`
  - 未インストールでも動作しますが、日本語の複合語・部分一致の誤リンク回避が弱くなります。

### 自動辞書生成（extract_automatic_links）に必要（任意）

- `python-frontmatter`

参考: 本リポジトリでは `scripts/requirements.txt` に各種依存がまとまっています。

```bash
# 依存関係をインストールする
pip install -r scripts/requirements.txt
```

---

## 3. ディレクトリ構成（推奨）

導入先プロジェクトの推奨構成です（Hugo以外の静的サイトでも考え方は同じです）。

```markdown
<your-project>/
├── scripts/
│   ├── linkbuilding.py
│   ├── linkbuilding_parallel.py
│   └── extract_automatic_links.py        # 任意
├── data/
│   └── linkbuilding/
│       ├── en.yaml
│       ├── en_automatic.json
│       ├── ja.yaml
│       ├── ja_automatic.json
│       └── *_synonyms.yaml               # 任意
├── databases/
│   ├── danger_terms_en.csv               # 推奨
│   └── danger_terms_ja.csv               # 推奨
└── public/                               # 静的サイト生成物（例: Hugo出力）
```

---

## 4. ワークフロー（導入先での実行手順）

### 4.1 Hugoの場合（推奨フロー）

1. クリーンなMarkdownからビルド

```bash
hugo --contentDir content-clean --destination public --cleanDestinationDir
```

1. HTML後処理で内部リンク付与

```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

### 4.2 Hugo以外の静的サイトの場合

- 静的サイトジェネレータの出力先ディレクトリ（例: `dist/` / `build/`）を `--public-dir` の代わりに与えるだけです。

```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir dist \
  --denylist-dir databases
```

---

## 5. linkbuilding の設定（リンク数制御）

基本はCLI引数で上書きします（CIでの再現性が高いです）。

- `--max-links`
- `--max-keyword`
- `--max-url`

例（控えめ）:

```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --max-links 15 --max-keyword 1 --max-url 3
```

例（Amplify等のビルドで最大限付与したい場合）:

```bash
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases \
  --max-links 9999 --max-keyword 1 --max-url 1
```

---

## 6. リンク辞書（data/linkbuilding）の作り方

### 6.1 手動辞書（YAML）

- 手動で追加・調整したいキーワードは `data/linkbuilding/{lang}.yaml` に入れます。
- 同義語を分離したい場合は `data/linkbuilding/{lang}_synonyms.yaml` を追加できます（`linkbuilding_parallel.py` が自動検出）。

### 6.2 自動辞書（JSON）

- 本リポジトリでは `scripts/extract_automatic_links.py` が **Markdownのフロントマター** から自動抽出して `*_automatic.json` を生成します。

例:

```bash
python3 scripts/extract_automatic_links.py \
  --content-dir content-clean/en/ \
  --output data/linkbuilding/en_automatic.json

python3 scripts/extract_automatic_links.py \
  --content-dir content-clean/ja/ \
  --output data/linkbuilding/ja_automatic.json
```

---

## 7. Denylist（誤リンク防止）

- `databases/danger_terms_{lang}.csv` に含まれる `keyword` / `normalized` はリンク対象から除外されます。
- まずは運用しながら「リンクされすぎる一般語」を追加していくのが現実的です。

---

## 8. 動作確認（導入直後のチェック）

### 8.1 リンク付与の確認

- `data-lb="1"` は linkbuilding が追加したリンクに付与されるマーカーです。

例:

```bash
grep -r 'data-lb="1"' public/en/ | wc -l
grep -r 'data-lb="1"' public/ja/ | wc -l
```

### 8.2 ローカルで内部リンク付きHTMLを確認

`hugo server` は HTML後処理を自動実行しないため、内部リンクをブラウザで見たい場合は「静的ビルド + 後処理 + 静的配信」で確認します。

```bash
hugo --baseURL http://localhost:1313/ --destination public --cleanDestinationDir
python3 scripts/linkbuilding_parallel.py --linkbuilding-dir data/linkbuilding --public-dir public --denylist-dir databases
python3 -m http.server 1313 --bind 127.0.0.1 --directory public
```

---

## 9. CI/CD 組み込み例

### 9.1 AWS Amplify

本リポジトリの `amplify.yml` は以下の順で実行しています。

- Hugoビルド
- `python3 scripts/linkbuilding_parallel.py ...`

導入先でも同様に、**ビルド後に後処理**を挟んでください。

### 9.2 GitHub Actions（例）

概念例:

- `hugo --minify` などで `public/` を作る
- `python3 scripts/linkbuilding_parallel.py ...` で内部リンク付与
- `public/` をデプロイ

---

## 10. よくある落とし穴

- `hugo server` だけ見て「リンクが付かない」と誤解する
- `public/` をGit管理してしまい差分が膨らむ
- glossary URL の大小文字が混在し、ケースセンシティブ環境で 404 になる
  - `linkbuilding.py` は `/glossary/` 配下の `href` を小文字正規化する処理を含みます
- 日本語で誤リンクが増える
  - `janome` を入れていない可能性があります

---

## 関連ドキュメント（本リポジトリ）

- `docs/INTERNAL_LINKING_QUICK_START.md`
- `docs/INTERNAL_LINK_SYSTEM_GUIDE.md`
- `CHANGELOG_INTERNAL_LINKING.md`
