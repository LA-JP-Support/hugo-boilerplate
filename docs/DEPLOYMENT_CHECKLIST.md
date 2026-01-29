# デプロイチェックリスト

## 概要

本ドキュメントは、SmartWebサイトのデプロイ前後で実施すべきチェック項目を定義します。
パフォーマンス低下を防ぎ、継続的に高品質なサイトを維持するためのガイドラインです。

**重要:** パフォーマンスの問題は、デプロイ後に発覚することが多いため、**毎回のデプロイ後にPageSpeed Insightsで確認**することを必須としています。

---

## クイックチェック（毎回必須）

### デプロイ前

```bash
# 1. ローカルでビルドエラーがないことを確認
hugo --minify

# 2. ローカルサーバーで目視確認
hugo server
# → http://localhost:1313/ja/ と /en/ をブラウザで確認
```

### デプロイ後（必須）

| ステップ | アクション | 合格基準 |
|---------|----------|---------|
| 1 | Amplifyデプロイ完了を確認 | ステータスが「Deployed」 |
| 2 | 本番サイトをブラウザで目視確認 | 表示崩れなし |
| 3 | **PageSpeed Insights実行** | 下記の基準を満たす |

### PageSpeed基準値（モバイル）

| 指標 | 目標値 | 警告値 | 要対応 |
|------|-------|-------|-------|
| Performance | 75+ | 60-74 | <60 |
| FCP | <1.8s | 1.8-3.0s | >3.0s |
| LCP | <2.5s | 2.5-4.0s | >4.0s |
| TBT | <200ms | 200-600ms | >600ms |
| CLS | <0.1 | 0.1-0.25 | >0.25 |
| Speed Index | <3.4s | 3.4-5.8s | >5.8s |

---

## PageSpeed Insights実行手順

### 1. テストURL

```
https://pagespeed.web.dev/analysis?url=https://main.d1jtfhinlastnr.amplifyapp.com/ja/
```

または手動で:
1. https://pagespeed.web.dev/ にアクセス
2. `https://main.d1jtfhinlastnr.amplifyapp.com/ja/` を入力
3. 「分析」をクリック

### 2. 確認項目

#### モバイル（必須）
- [ ] パフォーマンススコア: 75以上
- [ ] CLS: 0.1以下
- [ ] TBT: 200ms以下
- [ ] LCP: 2.5秒以下

#### デスクトップ（推奨）
- [ ] パフォーマンススコア: 90以上

### 3. 問題発生時の対応

| 指標 | 問題の兆候 | 確認箇所 | 対処法 |
|------|----------|---------|-------|
| CLS高い | >0.1 | 「レイアウトシフトの原因」 | 画像にwidth/height追加、min-height指定 |
| TBT高い | >200ms | 「強制リフロー」「長いタスク」 | JS最適化、getBoundingClientRect削減 |
| LCP遅い | >2.5s | 「LCPの内訳」 | ヒーロー画像最適化、フォントpreload |
| FCP遅い | >1.8s | サーバー応答時間 | CDNキャッシュ、Critical CSS確認 |

---

## よくある問題と解決策

### 1. CLS（レイアウトシフト）が高い

**原因の特定:**
1. PageSpeed Insightsで「レイアウトシフトの原因」を展開
2. 最もスコアが高い要素を確認

**よくある原因と対処:**

| 原因 | 対処法 |
|------|-------|
| 画像サイズ未指定 | `width` `height`属性を追加 |
| フォント読み込み | `font-display: swap`を使用 |
| 動的コンテンツ | `min-height`または`aspect-ratio`を指定 |
| Critical CSSとmain.cssの競合 | Critical CSSを最小限に |

**画像サイズ指定の例:**
```html
<!-- 修正前 -->
<img src="/images/logo.webp" alt="Logo" class="h-16 w-auto">

<!-- 修正後 -->
<img src="/images/logo.webp" alt="Logo" class="h-16 w-auto" width="200" height="64">
```

### 2. TBT（Total Blocking Time）が高い

**原因の特定:**
1. 「強制リフロー」セクションを確認
2. DevToolsのPerformanceタブで長いタスクを特定

**よくある原因と対処:**

| 原因 | 対処法 |
|------|-------|
| getBoundingClientRect()の多用 | IntersectionObserverに置換 |
| 同期的DOM操作 | requestAnimationFrameでバッチ処理 |
| 大きなJSファイル | コード分割、遅延読み込み |

### 3. LCPが遅い

**原因の特定:**
1. 「LCPの内訳」でLCP要素を確認
2. 通常はヒーロー画像かh1テキスト

**対処法:**
- LCP画像には `loading="eager"` を使用（lazy loadingしない）
- ヒーロー画像はWebPで最適化
- フォントをpreload

---

## デプロイ前チェックリスト（詳細版）

### コード品質

- [ ] `hugo --minify` でエラーなし
- [ ] ローカルで日本語/英語両方のページを目視確認
- [ ] 新規追加した画像に `width` `height` 属性あり
- [ ] 新規追加したJSに `defer` または遅延読み込みあり

### パフォーマンス関連

- [ ] 大きな画像（100KB以上）はWebP変換済み
- [ ] YouTubeはLite YouTube方式を使用
- [ ] サードパーティスクリプトは遅延読み込み
- [ ] Critical CSSの変更がある場合、CLSへの影響を確認

### セキュリティ・SEO

- [ ] 外部リンクに `rel="noopener noreferrer"` あり
- [ ] 画像に適切な `alt` テキストあり
- [ ] メタデータ（title, description）が設定済み

---

## デプロイ後チェックリスト（詳細版）

### 即時確認（デプロイ後5分以内）

- [ ] Amplifyコンソールでデプロイ成功を確認
- [ ] 本番URL (https://main.d1jtfhinlastnr.amplifyapp.com/ja/) にアクセス
- [ ] 変更箇所が正しく反映されていることを確認
- [ ] コンソールエラーがないことを確認（DevTools → Console）

### パフォーマンス確認（デプロイ後10分以内）

- [ ] PageSpeed Insightsでモバイルテスト実行
- [ ] パフォーマンススコアが75以上
- [ ] CLSが0.1以下
- [ ] TBTが200ms以下
- [ ] 問題があれば「診断」セクションを確認

### 問題発生時

1. **軽微な問題（スコア60-74、CLS 0.1-0.25）**
   - 問題箇所を特定
   - 次回デプロイまでに修正

2. **重大な問題（スコア<60、CLS>0.25、TBT>600ms）**
   - 直前の変更をrevert検討
   - 原因を特定して即座に修正

---

## パフォーマンス履歴記録

デプロイごとにパフォーマンス指標を記録し、傾向を把握します。

| 日付 | デプロイ内容 | Performance | CLS | TBT | LCP | 備考 |
|------|------------|-------------|-----|-----|-----|------|
| 2026-01-29 | CTA語順修正 | 70 | 0.552 | 10ms | 3.5s | CLS要改善 |
| 2026-01-28 | JS最適化 | 65 | 0.01 | 830ms | 3.5s | TBT改善前 |

---

## 自動化（将来の検討事項）

### GitHub Actions（推奨）

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on:
  push:
    branches: [main]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Lighthouse
        uses: treosh/lighthouse-ci-action@v10
        with:
          urls: |
            https://main.d1jtfhinlastnr.amplifyapp.com/ja/
          budgetPath: ./lighthouse-budget.json
```

### 予算ファイル例

```json
// lighthouse-budget.json
[
  {
    "path": "/*",
    "resourceSizes": [
      { "resourceType": "script", "budget": 150 },
      { "resourceType": "stylesheet", "budget": 50 }
    ],
    "resourceCounts": [
      { "resourceType": "third-party", "budget": 5 }
    ]
  }
]
```

---

## 関連ドキュメント

- [PAGESPEED_OPTIMIZATION.md](./PAGESPEED_OPTIMIZATION.md) - 詳細な最適化手法
- [IMAGE_OPTIMIZATION.md](./IMAGE_OPTIMIZATION.md) - 画像最適化ガイド

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-01-29 | 初版作成 |
