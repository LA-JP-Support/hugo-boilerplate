---
title: "レポートの項目（情報種別）について"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "items-info-type"
description: "レポートで抽出できる項目（情報種別）は以下のように定義しています。（2017/12/26更新）"
keywords: ["レポート", "について", "項目", "カスタマーポータル", "LiveAgent"]
category: "ticket-system/reports"
---
## レポートの項目（情報種別）について

このドキュメントは、レポートで抽出できる各種情報の詳細を説明します。（2017/12/26更新）

### 回答 <Answers>

- メール、フォーラムなどから作成されたチケットへの返信数（チャット対応は含まない）
- チャットで作成されたチケットからメール回答した場合はカウント

### 回答時間関連

#### 新規回答の平均時間 <New answer avg time(hours)>

- 「新規」チケットの回答に要した平均時間
- チケット作成から「回答」ステータスへの切り替え時間を測定

#### 未解決の平均時間 <Open answer avg time(hours)>

- 「オープン」チケットの回答に要した平均時間
- チケット受信から「回答」ステータスへの切り替え時間を測定

### チャット関連 <Chats>

#### チャット総数 <chats>

- ユーザがチャットボタンをクリックして開始したチャット
- 招待チャット、オンライン訪問者画面からの手動開始チャットを含む

#### チャットメッセージ <Chat messages>

- エージェントが送信したメッセージ数
- ウェルカムメッセージも「1」としてカウント

#### チャットの種類と状態

- 逃したチャット <Missed chats>
- チャットピックアップ <Chat pickup>
- チャット着信 <Incoming chats>
- 完了したチャット <Finished chats>
- 未返答のチャット <Unanswered chats>

#### チャット時間関連

- チャットピックアップ平均時間 <Chat pickup avg time(minutes)>
- チャット平均時間 <Chat avg time(minutes)>

### 通話関連 <Calls>

#### 通話総数と種類

- 通話 <Calls>
- 発信通話 <Outgoing calls>
- 不在着信 <Missed calls>
- 着信 <Incoming calls>
- 完了した通話 <Finished calls>

#### 通話時間関連

- 通話時間 <Call minutes>
- 発信通話時間 <Outgoing call minutes>
- 通話応答の平均時間 <Call pick up avg time>
- 通話の平均時間 <Call average time>
- 発信通話の平均時間 <Outgoing call average time>

### 評価関連

- 未評価 <Not ranked>
- 未評価（％）
- 良い評価 <Rewards>
- 良い評価（％）