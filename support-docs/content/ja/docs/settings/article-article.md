---
title: "Article article-181"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "article-article"
description: "LiveAgent では、Apache の \"mod_rewrite\" 利用なしでも API を利用することができます。その際、呼び出し URL の一部に変更が必要となります。以下に \"mod_rewrite\" を利用しないI URL 呼び出し　API 例をご紹介します。"
keywords: ["LiveAgent", "Agent", "ファイル", "URL", "API"]
category: "settings"
---
## mod_rewrite なしでの LiveAgent API 呼び出し

LiveAgent の API 呼び出しは、Apache の mod_rewrite 機能を使用しない場合でも柔軟に対応できます。このアプローチは、特定のサーバー環境や制限がある場合に有効な代替手段となります。

### API URL 呼び出しの基本形式

LiveAgent API は、異なるサーバー環境でも一貫した方法で呼び出すことができます。mod_rewrite を使用しない場合、URL 形式を若干調整する必要があります。

#### 標準的な API URL 例

一般的な API URL は、リソースとパラメータを明確に指定します：
```
http://example.com/api/conversations/[conversationid]/messages?apikey=key123456
```

#### mod_rewrite 未使用時の URL 形式

mod_rewrite を利用しない場合、API 呼び出しは以下のように変更されます：
```
URL_To_LiveAgent/api/index.php?handler=conversations/[conversationid]/messages&apikey=key123456
```

### API 呼び出しの詳細手順

LiveAgent API を効果的に利用するためには、正確な手順に従うことが重要です。

#### ステップ1: メインAPIエンドポイントの指定

専用の API ハンドラファイルを呼び出します：
```
http://example.com/api/index.php
```

#### ステップ2: ハンドラとAPIキーの追加

具体的な機能とセキュリティのために、ハンドラと API キーを追加します：
```
handler=conversations/[conversationid]/messages?apikey=key123456
```

### 追加の API 呼び出し例

LiveAgent の API は多様な機能を提供しています。

#### 部門会話の取得

特定の部門のすべての会話を取得する例：
```
URL_To_LiveAgent/api/index.php?handler=conversations&department=[departmentid]&apikey=key123456
```

この API アプローチにより、以下のメリットがあります：
- サーバー環境への柔軟な対応
- 明確な API 呼び出し方法
- セキュアな認証方式
- 多様な機能へのアクセス