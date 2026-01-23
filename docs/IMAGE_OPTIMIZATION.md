# 画像最適化ガイド

## 概要

このプロジェクトでは、画像の自動最適化システムを使用してWebパフォーマンスを向上させています。画像をアップロードすると、自動的に以下の最適化が適用されます：

- **WebP形式への変換**：対応ブラウザ向けに軽量なWebP形式を生成
- **レスポンシブ画像**：複数サイズ（300px、1024px、元サイズ）を生成
- **遅延読み込み**：スクロールに応じて画像を読み込み
- **自動最適化**：元の画像より大きくなる場合は元の画像を使用

## 画像アップロード時の自動最適化

### 1. 画像を追加する

画像を `static/images/` ディレクトリに配置します：

```bash
# 例：pillarsディレクトリに画像を追加
cp my-new-feature.jpg static/images/pillars/
```

### 2. 画像最適化スクリプトを実行

```bash
# プロジェクトルートから実行
bash scripts/preprocess-images.sh
```

または、ビルドスクリプトの一部として実行：

```bash
# 画像最適化のみ実行
bash scripts/build_content.sh --step preprocess_images
```

### 3. 最適化された画像を確認

最適化された画像は `static/images/processed/` ディレクトリに生成されます：

```text
static/images/processed/pillars/
├── my-new-feature.jpg          # 最適化された元サイズ
├── my-new-feature.webp         # WebP形式（元サイズ）
├── my-new-feature-300.jpg      # 300px幅
├── my-new-feature-300.webp     # 300px幅（WebP）
├── my-new-feature-1024.jpg     # 1024px幅（必要な場合）
└── my-new-feature-1024.webp    # 1024px幅（WebP、必要な場合）
```

### 4. 変更をコミット＆プッシュ

```bash
# 最適化された画像をステージング
git add static/images/processed/

# コミット
git commit -m "Add optimized images for new feature"

# プッシュ（Amplifyで自動デプロイ）
git push
```

## コードでの使用方法

### 最適化された画像を使用する

テンプレートやパーシャルで `lazyimg_internal.html` を使用します：

```html
{{ partial "components/media/lazyimg_internal.html" (dict
  "src" "/images/pillars/my-new-feature.jpg"
  "alt" "新機能の説明"
  "maxWidth" 800
  "class" ""
) }}
```

### パラメータ

- `src`: 元の画像パス（`/images/` から始まる）
- `alt`: 代替テキスト（アクセシビリティ）
- `maxWidth`: 最大幅（ピクセル）
  - タブサムネイル: `300`
  - コンテンツ画像: `800`
  - フルサイズ: `1024` または省略
- `class`: 追加のCSSクラス（オプション）
- `noLazy`: `true` に設定すると遅延読み込みを無効化（ファーストビュー画像用）

## 自動化のヒント

### Git Hooksで自動化（オプション）

画像追加時に自動的に最適化するには、`.git/hooks/pre-commit` を作成：

```bash
#!/bin/bash
# 画像が変更された場合のみ実行
if git diff --cached --name-only | grep -q "^static/images/.*\.\(jpg\|jpeg\|png\|webp\)$"; then
    echo "画像が変更されました。最適化を実行中..."
    bash scripts/preprocess-images.sh
    git add static/images/processed/
fi
```

実行権限を付与：

```bash
chmod +x .git/hooks/pre-commit
```

### VSCode タスクで自動化

`.vscode/tasks.json` に追加：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Optimize Images",
      "type": "shell",
      "command": "bash scripts/preprocess-images.sh",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": false
      }
    }
  ]
}
```

## トラブルシューティング

### 画像が最適化されない

1. **ImageMagickがインストールされているか確認**：

   ```bash
   magick --version
   ```

2. **WebP変換ツールがインストールされているか確認**：

   ```bash
   cwebp -version
   ```

3. **スクリプトに実行権限があるか確認**：

   ```bash
   chmod +x scripts/preprocess-images.sh
   ```

### 最適化された画像が表示されない

1. **ファイルパスが正しいか確認**：
   - 元の画像: `static/images/pillars/image.jpg`
   - 最適化後: `static/images/processed/pillars/image.jpg`

2. **Hugoビルドをクリーン**：

   ```bash
   hugo --cleanDestinationDir
   ```

3. **ブラウザキャッシュをクリア**

## デプロイ環境

### Amplify

現在の設定では、最適化された画像は**ローカルで生成してコミット**する必要があります。

`amplify.yml` にはビルド時の画像最適化は含まれていません（ビルド時間短縮のため）。

### 今後の改善案

ビルド時に自動最適化を行う場合は、`amplify.yml` の `preBuild` に追加：

```yaml
preBuild:
  commands:
    - apt-get update && apt-get install -y imagemagick webp
    - bash scripts/preprocess-images.sh
```

**注意**: ビルド時間が大幅に増加します。

## 参考

- スクリプト: `scripts/preprocess-images.sh`
- パーシャル: `layouts/partials/components/media/lazyimg_internal.html`
- 使用例: `layouts/partials/sections/features/pillars_tabs.html`
