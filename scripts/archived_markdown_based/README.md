# Archived: Markdown-Based Internal Linking Scripts

**⚠️ これらのスクリプトは非推奨です（Deprecated）**

このディレクトリには、Markdownファイルを直接編集する旧方式の内部リンクスクリプトが保管されています。

## アーカイブ理由

2026年1月7日、内部リンクシステムを**HTML後処理方式**に統一しました。

### 旧方式の問題点

1. **Markdownソースの汚染**: `content/`のMarkdownファイルに直接リンクを埋め込むため、ソースが読みにくくなる
2. **保守性の低下**: リンクを変更する際、Markdownファイルを再編集する必要がある
3. **バージョン管理の複雑化**: Git履歴がリンク変更で汚れる
4. **柔軟性の欠如**: リンク戦略の変更が困難

### 新方式の利点

**HTML後処理方式**では：
- ✅ Markdownソースは`content-clean/`でクリーンに保持
- ✅ Hugoビルド後の`public/`HTMLに対してリンクを追加
- ✅ リンク戦略の変更が容易（HTMLを再生成するだけ）
- ✅ Git履歴がクリーン

## アーカイブされたスクリプト

| スクリプト | 説明 | 代替方法 |
|-----------|------|---------|
| `add_internal_links.py` | Markdownに内部リンクを追加 | `linkbuilding.py` + `linkbuilding_parallel.py` |
| `add_links_from_database.py` | CSVデータベースからMarkdownにリンク追加 | `linkbuilding.py` (JSON/YAML使用) |
| `remove_internal_links.py` | Markdownから内部リンクを削除 | 不要（HTMLを再生成するだけ） |

## 新しいワークフロー

```bash
# 1. クリーンなMarkdownからHugoビルド
hugo --contentDir content-clean --destination public --cleanDestinationDir

# 2. HTML後処理で内部リンク追加
python3 scripts/linkbuilding_parallel.py \
  --linkbuilding-dir data/linkbuilding \
  --public-dir public \
  --denylist-dir databases
```

詳細は `docs/INTERNAL_LINK_SYSTEM_GUIDE.md` を参照してください。

## 重要な注意事項

**⚠️ これらのスクリプトは使用しないでください**

- 新規プロジェクトでは使用禁止
- 既存のMarkdownファイルへの適用禁止
- 参考用としてのみ保管

もし誤ってこれらのスクリプトを使用した場合は、`content-clean/`から再度クリーンなMarkdownをコピーしてください。

---

**アーカイブ日**: 2026年1月7日  
**理由**: HTML後処理方式への統一  
**バージョン**: v2.0.0
