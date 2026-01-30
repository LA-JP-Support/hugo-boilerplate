---
title: "エージェントの「チーム」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "agent-team-api"
description: "※ LiveAgent version 2.8.2.1 以降に対応します。Avaliable examples: Wordpress widget example -->"
keywords: ["エージェント", "API", "チーム", "LiveAgent", "WordPress"]
category: "settings"
---
## エージェントのチーム API リファレンス

### 目次
- [チームに所属するエージェントのステータス取得](#チームに所属するエージェントのステータス取得)
- [チームリストの取得](#チームリストの取得)

### チームに所属するエージェントのステータス取得

※ LiveAgent version 2.8.2.1 以降に対応します。Avaliable examples: [Wordpress widget example](http://support.qualityunit.com/876517-Online-agents-widget-for-WordPress)

#### API呼び出し

GET
  http://example.com/api/departments/[departmentid]/agents?apikey=[value]

#### 必須パラメータ

| パラメータ名 | 形式 | 内容 |
| --- | --- | --- |
| [departmentid] | text | エージェントのチーム ID |
| apikey | text | API キー |

#### 出力データ詳細

##### エージェント情報フィールド

| フィールド名 | 形式 | 内容 |
| --- | --- | --- |
| agents | list | チームに所属する全てのエージェントのリスト |
| userid | text | エージェントのユーザー ID |
| firstname | text | エージェントの名 |
| lastname | text | エージェントの姓 |
| email | text | エージェントのメールアドレス |
| onlinestatus | text | チームにおけるエージェントのオンラインステータス |
| presetstatus | text | チームにおけるエージェントの現在のステータス |

#### データ出力例

XML
```xml
<?xml version="1.0" encoding="utf-8"?>
<response>
 <agents>
  <agent>
   <userid>ag0h45s</userid>
   <firstname>John</firstname>
   <lastname>Doe</lastname>
   <email>john@agent.com</email>
   <onlinestatus>M</onlinestatus>
   <presetstatus>M</presetstatus>
  </agent>
 </agents>
</response>
```

JSON
```json
{
  "response":{
    "agents":[
      {
        "userid":"ag0h45s",
        "firstname":"John",
        "lastname":"Doe",
        "email":"john@agent.com",
        "onlinestatus":"M",
        "presetstatus":"M"
      }
    ]
  }
}
```

### チームリストの取得

※ LiveAgent version 2.8.2.1 以降に対応します。

#### API呼び出し

GET
  http://example.com/api/departments?apikey=[value]

#### 必須パラメータ

| パラメータ名 | 形式 | 内容 |
| --- | --- | --- |
| apikey | text | API キー |

#### 出力データ詳細

##### チーム情報フィールド

| フィールド名 | 形式 | 内容 |
| --- | --- | --- |
| departments | list | エージェントのチームのリスト |
| departmentid | text | チーム ID |
| name | text | チームの名称 |
| description | text | チームの概要 |
| onlinestatus | text | チームのオンラインステータス |
| presetstatus | text | チームの現在のステータス |
| deleted | constlist | チームが削除されたかどうか |

#### データ出力例

XML
```xml
<?xml version="1.0" encoding="utf-8"?>
<response>
 <departments>
  <department>
   <departmentid>d1s58gs4</departmentid>
   <name>Department 1</name>
   <description>This is first department</description>
   <onlinestatus>M</onlinestatus>
   <presetstatus>M</presetstatus>
   <deleted>N</deleted>
  </department>
 </departments>
</response>
```