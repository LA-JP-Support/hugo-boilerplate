---
title: "AIプロバイダーの設定（FlowHunt / OpenAI）"
date: 2026-02-03
lastmod: 2026-02-03
draft: false
translationKey: "ai-provider-setup"
description: "SmartWebのAI機能で使用するAIプロバイダー（FlowHunt・OpenAI）の違いと設定方法を解説します。AI Answer ComposerはFlowHuntのみ、AI Answer ImproverはFlowHuntまたはOpenAIに対応しています。"
keywords: ["FlowHunt", "OpenAI", "AIプロバイダー", "設定", "API", "LiveAgent"]
category: "ai-fundamentals"
---

SmartWebのAI機能は、**FlowHunt**&#8203;または**OpenAI**&#8203;をAIプロバイダーとして使用できます。ただし、機能によって対応するプロバイダーが異なります。

## AIプロバイダー対応表

| 機能 | FlowHunt | OpenAI | 備考 |
|------|:--------:|:------:|------|
| **AIチャットボット** | ✓ | - | FlowHuntのみ |
| **AIメール回答作成**（AI Answer Composer） | ✓ | - | FlowHuntのみ |
| **AI回答アシスト**（AI Answer Improver） | ✓ | ✓ | 両方対応 |

## FlowHunt vs OpenAI の違い

### FlowHunt

| 項目 | 内容 |
|------|------|
| **開発元** | Quality Unit社（LiveAgent開発元と同一） |
| **ナレッジベース** | 統合済み（RAG対応） |
| **データセキュリティ** | 同社製品間連携で外部流出リスクなし |
| **対応機能** | 全AI機能（チャットボット、Composer、Improver） |
| **料金** | SmartWebプランに含まれる |

### OpenAI

| 項目 | 内容 |
|------|------|
| **開発元** | OpenAI社 |
| **ナレッジベース** | 未統合（入力テキストのみ処理） |
| **データセキュリティ** | OpenAI社のポリシーに準拠 |
| **対応機能** | AI回答アシスト（Improver）のみ |
| **料金** | OpenAI社との直接契約（API利用料別途） |

## 推奨プロバイダー

### FlowHuntを推奨する理由

1. **データセキュリティ**: LiveAgentと同一開発元のため、データが外部に流出するリスクがありません
2. **ナレッジベース統合**: RAG技術により、御社のFAQ・マニュアルに基づいた正確な回答が可能
3. **シームレスな連携**: AI Answer ComposerとAI Answer Improverの連携がスムーズ
4. **コスト効率**: SmartWebプランに含まれるため、追加のAPI契約が不要

### OpenAIを選択する場合

- AI回答アシスト（Improver）のみを使用する場合
- 既にOpenAI APIを他システムで利用している場合
- 特定のOpenAIモデル（GPT-4など）を指定したい場合

## FlowHuntの設定手順

### 1. FlowHuntでフローを作成

1. FlowHuntにログイン
2. 「新規フロー作成」をクリック
3. テンプレート「**LiveAgent AI Answer Assistant (Composer & Improver)**」を選択
4. フロー名を設定して保存

### 2. ナレッジソースを追加

フローにナレッジソースを接続します：

| ナレッジソース | 用途 |
|---------------|------|
| **Schedules** | WebサイトのURLを定期クロール |
| **Q&A** | よくある質問と回答を手動登録 |
| **Documents** | PDF、Word、Excelなどをアップロード |

### 3. LiveAgentにAPIキーを登録

1. FlowHuntで「API Keys」からAPIキーを取得
2. LiveAgent管理画面 → 「設定」→「AI」
3. 「FlowHunt API Key」にキーを入力
4. 使用するフローを選択

### 4. 動作確認

- チケット画面でAI Answer Composerのアイコンが表示されることを確認
- テスト返信を作成し、AI Answer Improverが動作することを確認

## OpenAIの設定手順

### 1. OpenAI APIキーを取得

1. [OpenAI Platform](https://platform.openai.com/) にログイン
2. 「API Keys」から新しいキーを作成
3. キーを安全な場所に保存

### 2. LiveAgentにAPIキーを登録

1. LiveAgent管理画面 → 「設定」→「AI」
2. 「OpenAI API Key」にキーを入力
3. 使用するモデルを選択（GPT-4、GPT-3.5-turboなど）

### 3. 利用上の注意

- OpenAI連携では**AI回答アシスト（Improver）のみ**&#8203;が利用可能です
- AIチャットボット、AIメール回答作成（Composer）はOpenAIでは動作しません
- API利用料はOpenAI社から直接請求されます

## 両方を併用する場合

FlowHuntとOpenAIを同時に設定することも可能です：

```
AIチャットボット ──────────→ FlowHunt
AIメール回答作成（Composer）→ FlowHunt
AI回答アシスト（Improver）──→ FlowHunt または OpenAI（選択可）
```

AI回答アシストでは、使用時にどちらのプロバイダーを使用するか選択できます。

## トラブルシューティング

### FlowHuntが動作しない場合

- APIキーが正しく入力されているか確認
- フローが「公開」状態になっているか確認
- ナレッジソースが正しく接続されているか確認

### OpenAIが動作しない場合

- APIキーが有効か確認（OpenAI Dashboardで確認）
- 利用上限（Rate Limit）に達していないか確認
- 請求情報が正しく設定されているか確認

## 関連情報

- [FlowHuntとは](/ja/support/ai-fundamentals/flowhunt-about/) - FlowHuntの概要
- [AIの学習方法](/ja/support/ai-fundamentals/ai-learning/) - ナレッジソースの設定
- [セキュリティとデータ保護](/ja/support/ai-fundamentals/ai-security-data/) - データ保護ポリシー
