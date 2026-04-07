# smartweb

SmartWeb製品サイト + サポートドキュメント（日英2言語展開）。

## 技術スタック

Hugo + Boilerplate theme + Gulp + Tailwind CSS

## ビルド & デプロイ

```bash
hugo --gc --minify
```

デプロイ: `git push origin main`（AWS Amplifyで自動ビルド）。開発はdevブランチ。

## ローカル開発

```bash
hugo server -D   # Hugo dev server (port 1313)
```

## セキュリティ注意事項

- CTA/Mautic設定は hugo.toml の `[params]` セクションで管理
- 2アプリ構成（www + support）: Amplifyで別々にビルド

## 依存関係

- media-dashboardのCTA APIに依存
- デプロイ順序: media-dashboard → **smartweb**（並列可） → intwk-website → mautic-ai-email

## スキル

smartweb固有スキル（glossary-pipeline, translate, validate等）は `.claude/skills/` を参照。

## エコシステムルール

エコシステム横断に影響する変更は `../interwork-ops/changelog.md` に追記:
```
- [smartweb] 変更内容の1行要約
```

UI作業時は `DESIGN.md` を参照。色・フォント・スペーシングの判断はDESIGN.mdに従うこと。絵文字は原則禁止。

すべての応答は日本語で行うこと
