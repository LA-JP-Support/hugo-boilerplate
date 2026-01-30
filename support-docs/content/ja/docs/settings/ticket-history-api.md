---
title: "「スマートチケット（会話履歴）」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "ticket-history-api"
description: "※LiveAgent version 2.8.2.1以降に対応しています"
keywords: ["スマートチケット", "チケット", "API", "LiveAgent", "WordPress"]
category: "settings"
---
## スマートチケット（会話履歴）API概要

### 目次
- [API呼び出しの基本](#api基本)
- [チケット管理の主要機能](#チケット管理)

## API基本情報

### APIバージョン
- 対応バージョン: LiveAgent version 2.8.2.1以降

### 認証
- API認証には、APIキーが必要

## チケット管理

### チケットの転送
#### 転送API仕様
- メソッド: PUT
- エンドポイント: `/api/conversations/[conversationid]/attendants`

#### 転送パラメータ
- 必須パラメータ:
  - `conversationid`: 会話履歴のID
  - `apikey`: LiveAgentのAPIキー

- オプションパラメータ:
  - `agentidentifier`: エージェント識別子
  - `useridentifier`: 転送先ユーザー
  - `department`: チームID
  - `note`: 転送理由

### チケットの削除
#### 削除API仕様
- メソッド: DELETE
- エンドポイント: `/api/conversations/[conversationid]`

#### 削除パラメータ
- 必須パラメータ:
  - `conversationid`: 会話履歴のID
  - `apikey`: LiveAgentのAPIキー

- オプションパラメータ:
  - `note`: 削除ノート
  - `useridentifier`: 削除ユーザー

### チケットの検索・参照
#### 検索API仕様
- メソッド: GET
- エンドポイント: `/api/conversations`

#### 検索パラメータ
- 必須パラメータ:
  - `apikey`: LiveAgentのAPIキー

- オプションパラメータ:
  - `owneridentifier`: 依頼者メールアドレス
  - `department`: チーム識別子
  - `status`: チケットステータス
  - `datefrom`: 開始日時
  - `dateto`: 終了日時

### その他のチケット操作
- チケットステータス変更
- タグの追加・削除
- 新規チケット作成
- メッセージ追加

## レスポンス
### 共通レスポンス形式
- `status`: 実行ステータス
- `statuscode`: ステータスコード

### レスポンス例
- XML形式
- JSON形式