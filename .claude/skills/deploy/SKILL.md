---
name: deploy
description: "デプロイチェックリスト。ビルド確認、dev/mainブランチ切り替え、noindex検証、PageSpeed Insights基準値チェックを含む。"
---

# デプロイチェックリスト

SmartWebサイトのデプロイ前後チェック。AWS Amplifyによるdev/main分岐運用。

## 現在のGit状態

!`git status`
!`git branch -a`

## クイックリファレンス

### デプロイ前（必須）
```bash
# 1. フロントマター検証
python scripts/validate_frontmatter.py --all --errors-only

# 2. 翻訳キー整合性
python scripts/validate_frontmatter.py --check-translations

# 3. 画像参照の存在チェック
grep -rn 'image:.*"/images/' content/ | while read line; do
  file=$(echo "$line" | cut -d: -f1)
  img=$(echo "$line" | grep -o '"/images/[^"]*"' | tr -d '"')
  if [ -n "$img" ] && [ ! -f "static$img" ]; then
    echo "MISSING: $file → static$img"
  fi
done

# 4. ビルドエラーなし確認
hugo --minify

# 5. ローカル目視確認
hugo server
# → /ja/ と /en/ を確認
```

### dev ブランチ確認（noindex 必須）
- `robots.txt` が `Disallow: /`
- `<meta name="robots" content="noindex, nofollow">`
- canonical が dev ドメインを指している
- supportリンクが dev support-docs を指している

### デプロイ後（必須）
1. Amplifyデプロイ成功を確認
2. 本番サイトを目視確認
3. **PageSpeed Insights 実行**

### PageSpeed 基準値（モバイル）

| 指標 | 目標 | 警告 | 要対応 |
|------|------|------|--------|
| Performance | 75+ | 60-74 | <60 |
| CLS | <0.1 | 0.1-0.25 | >0.25 |
| TBT | <200ms | 200-600ms | >600ms |
| LCP | <2.5s | 2.5-4.0s | >4.0s |
| FCP | <1.8s | 1.8-3.0s | >3.0s |

### PageSpeed テストURL
```
https://pagespeed.web.dev/analysis?url=https://main.d1jtfhinlastnr.amplifyapp.com/ja/
```

## デプロイフロー

```bash
# 1. コンテンツ品質チェック（コミット前に実行）
python scripts/validate_frontmatter.py --all --errors-only
python scripts/validate_frontmatter.py --check-translations
grep -rn 'image:.*"/images/' content/ | while read line; do
  file=$(echo "$line" | cut -d: -f1)
  img=$(echo "$line" | grep -o '"/images/[^"]*"' | tr -d '"')
  if [ -n "$img" ] && [ ! -f "static$img" ]; then
    echo "MISSING: $file → static$img"
  fi
done

# 2. ローカルビルド確認
hugo --minify

# 3. ローカルサーバーで目視確認
hugo server

# 4. dev ブランチにpush（ステージング）
git checkout dev
git merge feature-branch
git push

# 5. Amplify dev デプロイ確認
# → noindex, robots.txt, canonical を検証

# 6. main ブランチにpush（本番）
git checkout main
git merge dev
git push

# 7. PageSpeed Insights 確認（デプロイ後10分以内）
```

## 問題発生時の対応

| 指標 | 確認箇所 | 対処 |
|------|---------|------|
| CLS高い | 画像width/height | `width`/`height`追加、`min-height`指定 |
| TBT高い | JS最適化 | IntersectionObserver置換、requestAnimationFrame |
| LCP遅い | ヒーロー画像 | WebP最適化、`loading="eager"` |

## デプロイチェックリスト全文

!`cat docs/DEPLOYMENT_CHECKLIST.md`

## パフォーマンス最適化の詳細（問題がある場合）

!`cat docs/PAGESPEED_OPTIMIZATION.md`

## 画像最適化が必要な場合

!`cat docs/IMAGE_OPTIMIZATION.md`
