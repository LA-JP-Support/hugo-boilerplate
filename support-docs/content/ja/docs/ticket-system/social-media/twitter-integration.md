---
title: "Twitter と連携してツイートを取り込むには"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "twitter-integration"
description: "LiveAgent の Twitter サポートチャネルは、特定の検索基準と一致するツイートをチケットへ変換して取り込むことができます。"
keywords: ["Twitter", "連携", "LiveAgent", "Agent", "アカウント"]
category: "ticket-system/social-media"
---
## Twitterチャネルでツイートをサポートチケットに取り込む方法

### Twitter連携の概要
LiveAgentのTwitterサポートチャネルは、特定の検索基準と一致するツイートをチケットへ変換して取り込むことができます。

### Twitter連携設定

![Twitter連携設定画面](/liveagent/scripts/file.php?view=Y&file=d4e94b4f72b1ac282b930c8bdc2ae98f)

### 検索クエリの追加と言語設定
新規クエリを追加すると、フィールドが追加されますので、そのフィールドに検索したいキーワードを入力します。また、日本語のツイートを検索する場合には、「言語」の項目で「Japanese」を選びます。

### Twitter検索APIについて
ツイート検索には Twitter の検索 API が利用可能です。詳しくは [Twitter 社公式ページ](https://dev.twitter.com/rest/public/search)をご覧ください （英語）

### 検索クエリの記入例と検索結果

| 検索ワード | 検索されるツイート |
|-----------|---------------------|
| twitter search | twitterと searchを含むツイートを検索。これが基本的な動作です |
| "happy hour" | happy hour と完全一致したツイートを検索 |
| love OR hate | love または hate （もしくは両方）を含むツイートを検索 |
| beer -root | root を除いた、beer を含むツイートを検索 |
| #haiku | ハッシュタグ #haiku を含むツイートを検索 |
| from:twitterapi | ユーザ @twitterapi から送信されたツイートを検索 |
| to:twitterapi | ユーザ @twitterapi 宛に送信されたツイートを検索 |
| @mashable | mashable のアカウントに関連したツイートを検索 |
| superhero since:2010-12-27 | superhero を含む、2010年12月27日（年-月-日）のツイートを検索 |
| ftw until:2010-12-27 | ftw を含む、2010年12月27日までのツイートを検索 |
| movie -scary | movie を含むが、scary を含まないツイートを検索 |
| flight :( | flight と記号 :( を含むツイートを検索（ " :) "　や" :( "は顔文字 ;p ） |
| hilarious filter:links | hilarious を含み、リンク URL があるツイートを検索 |
| news source:twitterfeed | news を含み、TwitterFeed を利用してツイートされたものを検索 |

### 注意事項
※これらの検索 API は Twitter 側で仕様変更されることがあります。