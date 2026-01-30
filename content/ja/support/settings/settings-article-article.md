---
title: "Article article-181"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-article-article"
description: "LiveAgent では、Apache の \"mod_rewrite\" 利用なしでも API を利用することができます。その際、呼び出し URL の一部に変更が必要となります。以下に \"mod_rewrite\" を利用しないI URL 呼び出し　API 例をご紹介します。"
keywords: ["LiveAgent", "Agent", "ファイル", "URL", "API"]
type: support
category: "settings"
e-title: "Article article-181"
---

LiveAgent では、Apache の "mod_rewrite" 利用なしでも API を利用することができます。その際、呼び出し URL の一部に変更が必要となります。以下に "mod_rewrite" を利用しないI URL 呼び出し　API 例をご紹介します。

http://example.com/api/conversations/[conversationid]/messages?apikey=key123456

"mod_rewrite" 未利用時の表示イメージは次のようになります。:

URL_To_LiveAgent/api/index.php?handler=conversations/[conversationid]/messages&apikey=key123456

固有の API handler ファイルを呼び出す必要があります。

http://example.com/api/index.php

その後、ハンドラのストリングと API Key を付加します。:

handler=conversations/[conversationid]/messages?apikey=key123456

Another example:
- if you wanted to retrieve all the conversations of a department then you could do it this way:

URL_To_LiveAgent/api/index.php?handler=conversations&department=[departmentid]&apikey=key123456