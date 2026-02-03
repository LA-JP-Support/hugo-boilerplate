---
title: "AIメール回答作成"
description: "AIメール回答作成（AI Answer Composer）は、顧客からのメールや問い合わせフォームを分析し、返信の下書きを自動生成する機能です。FlowHuntのナレッジベースに基づいた正確な回答を作成します。"
weight: 30
---

**AIメール回答作成（AI Answer Composer）**&#8203;は、顧客からのメールや問い合わせフォームを分析し、返信の下書きを自動生成する機能です。

## 主な特徴

| 特徴 | 説明 |
|------|------|
| **意図分析** | 顧客のメールから質問の意図を自動判別 |
| **RAG技術** | ナレッジベースから関連情報を検索して回答生成 |
| **複数質問対応** | 1通のメールに複数の質問がある場合も対応 |
| **AI回答アシスト連携** | 生成された下書きをそのままブラッシュアップ可能 |

## AIプロバイダー

AIメール回答作成は **FlowHunt のみ** に対応しています（OpenAIは非対応）。

FlowHuntのナレッジソース（Schedules、Q&A、Documents）を学習させることで、御社のFAQ・マニュアルに基づいた正確な返信下書きを生成します。

## ワークフロー

```
顧客からのメール受信
       ↓
AI Answer Composer（下書き自動生成）
       ↓
AI Answer Improver（文章ブラッシュアップ）
       ↓
オペレーターが確認・編集
       ↓
     送信
```

## このセクションの内容

- [AIメール回答作成について](/docs/email-composer/about-ai-answer-composer/)
- [設定方法](/docs/email-composer/setup/)
- [ナレッジベースの準備](/docs/email-composer/knowledge-base/)
- [利用可能なプラン](/docs/email-composer/available-plans/)

## 関連情報

- [AI機能の基礎知識](/docs/ai-fundamentals/) - 3つのAI機能の違いと使い分け
- [AIの学習方法](/docs/ai-fundamentals/ai-learning/) - ナレッジソースの設定
- [RAG技術について](/docs/ai-fundamentals/rag-technology/) - 高精度回答を実現する仕組み
- [AIプロバイダーの設定](/docs/ai-fundamentals/ai-provider-setup/) - FlowHuntの設定方法
- [AI回答アシスト](/docs/ai-answer-assist/) - 生成された下書きのブラッシュアップ
