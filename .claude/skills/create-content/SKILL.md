---
name: create-content
description: "Blog、Glossary、YouTube動画紹介、Support、Serviceの各コンテンツタイプの新規記事作成。フロントマター設定、ファイル配置、画像設定を含む。"
---

# コンテンツ作成ワークフロー

新しいコンテンツを作成する際の統合ガイド。$ARGUMENTS からコンテンツタイプを判定して手順を実行する。

## 前提確認

作成前に必ず:
1. `git status` で作業ツリーがクリーンか確認
2. 必要なら `git commit` でバックアップ

## コンテンツタイプ判定

ユーザーの依頼から以下のいずれかを判定:
- **Blog（通常）**: ブログ記事。`content/{lang}/blog/` に配置
- **Blog（YouTube）**: YouTube動画紹介。`layout: single-youtube` を使用
- **Glossary（単体）**: 用語集記事1つ。バッチ作成は glossary-pipeline Skill を使用
- **Service**: サービスページ。`content/{lang}/services/` に配置
- **Support**: ヘルプ記事。`content/{lang}/support/{category}/` に配置

## 各タイプの詳細フロントマターと手順

!`cat docs/CONTENT_CREATION_WORKFLOWS.md`

## 現在のarchetypeテンプレート

### Blog archetype
!`cat archetypes/blog.md`

### Glossary archetype
!`cat archetypes/glossary.md`

## 作成手順（共通フロー）

### 1. ファイル作成
```bash
# Hugoのarcetypeを使用
hugo new content/{lang}/{type}/{slug}.md
```

### 2. フロントマター設定
- コンテンツタイプごとの必須フィールドを全て設定
- `translationKey` はEN/JAで必ず一致させる
- `date` は実際の作成日
- `description` は簡潔に（冗長な "Comprehensive guide to..." は禁止）

### 3. 画像配置（必要な場合）
- `static/images/{type}/` に配置
- `width`/`height` 属性を必ず指定

### 4. 対訳ファイル作成
- EN/JA 両方のファイルを作成
- `translationKey` で紐付け

### 5. ローカル確認
```bash
hugo server -D
# http://localhost:1313/{lang}/{type}/{slug}/
```

## YouTube記事の追加ルール

!`cat docs/youtube-article-workflow.md`

## 品質チェック（作成後）

- [ ] 必須フロントマターが全て設定済み
- [ ] `translationKey` がEN/JAで一致
- [ ] `description` が簡潔（160文字以内推奨）
- [ ] 画像に `width`/`height` 属性あり
- [ ] 参考資料の見出し: EN `## References` / JA `## 参考資料`
- [ ] Markdownに内部リンクを直接挿入していない
- [ ] `hugo server -D` でエラーなし

## フロントマター検証
```bash
python scripts/validate_frontmatter.py {作成したファイルパス}
```
