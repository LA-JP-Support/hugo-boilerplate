# Scripts フォルダ 仕様書

このドキュメントは、`scripts/`フォルダ内の各スクリプトの機能と使用方法を説明します。

## 📋 目次

- [表バリデーション](#表バリデーション)
- [ツールチップ変換](#ツールチップ変換)
- [翻訳](#翻訳)
- [リンクビルディング](#リンクビルディング)
- [コンテンツ生成](#コンテンツ生成)
- [その他のユーティリティ](#その他のユーティリティ)
- [トラブルシューティング](#トラブルシューティング)

---

## 表バリデーション

### validate_tables.py

**目的**: Markdownファイル内の表の構文エラーを検出・修正

**検出する問題**:
1. ヘッダー行の後に区切り線(`|---|---|`)がない
2. セル内に改行がある（`<br>`タグに変換が必要）

**使用方法**:
```bash
# 問題を検出のみ（修正しない）
python validate_tables.py --path ../content/ja

# 問題を自動修正
python validate_tables.py --fix --path ../content/ja

# 全言語をチェック
python validate_tables.py --fix --path ../content
```

**出力例**:
```
🔍 表の検証を開始: /path/to/content/ja
🔧 修正モード: 有効

📄 blog/example.md
  ⚠️  行 113: 表のヘッダー行の後に区切り線がありません
  ✓ 区切り線を追加: 2列 (行 113)
  ✅ 修正完了

============================================================
📊 結果: 1/10 ファイルに問題が見つかりました
```

**技術詳細**:
- 正規表現を使用して表のヘッダー行を検出
- 列数を自動カウントして適切な区切り線を生成
- セル内改行を`<br>`タグに自動変換
- UTF-8エンコーディングで安全に処理

---

## ツールチップ変換

### convert_tooltip_syntax.py

**目的**: 旧形式のツールチップ構文を新しいHugoショートコード形式に変換

**変換パターン**:
```markdown
# 変換前
用語（説明：詳細な説明文）
**用語**（説明：詳細な説明文）

# 変換後
{{< tooltip text="詳細な説明文" >}}用語{{< /tooltip >}}
```

**使用方法**:
```bash
# 単一ファイルを変換
python convert_tooltip_syntax.py --input file.md

# ディレクトリ内の全ファイルを変換
python convert_tooltip_syntax.py --dir content/ja/blog/

# バックアップなしで変換
python convert_tooltip_syntax.py --dir content/ja/blog/ --no-backup
```

**機能**:
- 自動バックアップ作成（`.bak`ファイル）
- 複数ファイルの一括処理
- 変換前後のプレビュー表示
- エラーハンドリング

---

## 翻訳

### translate_with_flowhunt.py

**目的**: FlowHunt APIを使用して英語コンテンツを多言語に自動翻訳

**サポート言語**: 
日本語、中国語、韓国語、スペイン語、フランス語、ドイツ語など20+言語

**使用方法**:
```bash
# 基本使用
python translate_with_flowhunt.py

# カスタムパス指定
python translate_with_flowhunt.py --path /path/to/content

# カスタムフローID指定
python translate_with_flowhunt.py --flow-id "custom-flow-id"

# 最大バッチサイズ指定
python translate_with_flowhunt.py --max-scheduled-tasks 100
```

**前提条件**:
- FlowHunt APIキー（`.env`ファイルまたは環境変数`FLOWHUNT_API_KEY`）
- Python 3.6以上
- 必要パッケージ: `flowhunt`, `tqdm`, `python-dotenv`

**処理フロー**:
1. `/content/en/`から英語ファイルを読み込み
2. 各ターゲット言語ディレクトリをチェック
3. 存在しないファイルのみ翻訳
4. FlowHunt APIで翻訳実行
5. 結果を対応する言語ディレクトリに保存

---

## リンクビルディング

### linkbuilding.py / linkbuilding_parallel.py

**目的**: コンテンツ内に自動的に内部リンクを挿入

**機能**:
- キーワードベースの自動リンク生成
- 並列処理による高速化（`linkbuilding_parallel.py`）
- カスタマイズ可能なキーワード設定
- HTML出力の自動更新

**使用方法**:
```bash
# 基本使用
./linkbuilding.sh

# 並列処理版
python linkbuilding_parallel.py \
  --linkbuilding-dir ../data/linkbuilding \
  --public-dir ../public \
  --max-workers 4
```

**設定ファイル**: `linkbuilding_config.json`

---

## コンテンツ生成

### generate_content.py

**目的**: テンプレートからコンテンツを自動生成

**使用方法**:
```bash
python generate_content.py --template blog --output ../content/ja/blog/
```

### generate_related_content.py

**目的**: 関連記事の自動リンク生成

**機能**:
- コンテンツの類似度分析
- 自動的に関連記事を提案
- フロントマターへの自動追加

---

## その他のユーティリティ

### find_duplicate_images.py
重複画像を検出して削除

### sync_translations.py
翻訳ファイルの同期を管理

### generate_amplify_redirects_file.py
AWS Amplifyのリダイレクトファイルを生成

---

## トラブルシューティング

### 一般的な問題

**問題**: `ModuleNotFoundError`
**解決**: 
```bash
pip install -r requirements.txt
```

**問題**: 権限エラー
**解決**:
```bash
chmod +x script_name.py
```

**問題**: パスが見つからない
**解決**: スクリプトは`scripts/`ディレクトリから実行してください

---

## 📝 開発ガイドライン

新しいスクリプトを追加する場合:

1. **ドキュメント**: スクリプトの先頭にdocstringを追加
2. **引数**: `argparse`を使用してコマンドライン引数を定義
3. **エラーハンドリング**: 適切な例外処理を実装
4. **ロギング**: 進捗状況を明確に表示
5. **テスト**: 実行前に小規模データでテスト

---

## 📞 サポート

問題が発生した場合:
1. このREADMEを確認
2. スクリプトの`--help`オプションを実行
3. エラーメッセージを確認
4. 開発チームに連絡

---

最終更新: 2025-11-20