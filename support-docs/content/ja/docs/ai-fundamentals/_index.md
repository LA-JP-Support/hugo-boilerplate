---
title: "AI機能の基礎知識"
date: 2026-02-03
lastmod: 2026-02-03
draft: false
translationKey: "ai-fundamentals"
description: "SmartWebのAI機能（AIチャットボット、AI回答アシスト、AIメール回答作成）に共通する基礎知識、学習方法、セキュリティについて解説します。"
keywords: ["AI", "FlowHunt", "LiveAgent", "RAG", "学習", "セキュリティ", "基礎知識"]
weight: 15
---

SmartWebは、AIプラットフォーム「**FlowHunt**」とチケットシステム「**LiveAgent**」を完全統合したAIカスタマーサポートサービスです。このセクションでは、すべてのAI機能に共通する基礎知識を解説します。

## SmartWebの3つのAI機能

| 機能 | 対象 | 目的 | AIプロバイダー |
|------|------|------|----------------|
| **AIチャットボット** | 顧客 | 24時間自動応答 | FlowHunt |
| **AIメール回答作成** | オペレーター | 返信下書きの自動生成 | FlowHunt のみ |
| **AI回答アシスト** | オペレーター | 文章の改善・調整 | FlowHunt または OpenAI |

## このセクションの内容

### AI機能の概要
- [SmartWebのAI機能とは](/ja/support/ai-fundamentals/ai-features-overview/) - 3つのAI機能の違いと使い分け

### 基盤技術
- [FlowHuntとは](/ja/support/ai-fundamentals/flowhunt-about/) - ノーコードAIプラットフォームの解説
- [AIプロバイダーの設定](/ja/support/ai-fundamentals/ai-provider-setup/) - FlowHuntとOpenAIの違い・設定方法
- [RAG技術について](/ja/support/ai-fundamentals/rag-technology/) - 高精度回答を実現する技術

### ナレッジと学習
- [AIの学習方法](/ja/support/ai-fundamentals/ai-learning/) - ナレッジソース、コンテンツ形式、設定ガイド

### セキュリティ
- [セキュリティとデータ保護](/ja/support/ai-fundamentals/ai-security-data/) - データ保護、GDPR対応

## ナレッジベースの共有

AIチャットボットとAIメール回答作成は**同じナレッジベースを共有**&#8203;しています。

```
┌─────────────────────────────────────────┐
│         FlowHunt ナレッジソース           │
│  ┌─────────┬─────────┬─────────┐        │
│  │Schedules│  Q&A   │Documents│        │
│  │(Webクロ │(質問と │(ファイル│        │
│  │ール)    │回答)   │アップ   │        │
│  │         │        │ロード)  │        │
│  └────┬────┴────┬───┴────┬────┘        │
│       │         │        │             │
│       └─────────┼────────┘             │
│                 ▼                       │
│         RAG（検索拡張生成）              │
└─────────────────┬───────────────────────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│AIチャット│ │AIメール  │ │AI回答    │
│ボット   │ │回答作成  │ │アシスト  │
│         │ │(Composer)│ │(Improver)│
└─────────┘ └──────────┘ └──────────┘
     ▼            ▼            ▼
   顧客      オペレーター   オペレーター
  (自動)     (確認後送信)  (確認後送信)
```

**メリット**:
- 一度の整備で複数チャネルに対応
- 回答の一貫性を確保
- メンテナンスの効率化
