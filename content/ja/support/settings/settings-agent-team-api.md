---
title: "エージェントの「チーム」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-agent-team-api"
description: "※ LiveAgent version 2.8.2.1 以降に対応します。Avaliable examples: Wordpress widget example -->"
keywords: ["エージェント", "API", "チーム", "LiveAgent", "WordPress"]
type: support
category: "settings"
e-title: "Agent - Team - Api"
---

## 【目次】

- [チームに所属する全てのエージェントのステータスを呼び出す](#0)

- [チームのリストを呼び出す](#1)

- [チームの詳細情報を呼び出す](#2)

**

### § チームに所属する全てのエージェントのステータスを呼び出す

※ LiveAgent version 2.8.2.1 以降に対応します。Avaliable examples: [Wordpress widget example](http://support.qualityunit.com/876517-Online-agents-widget-for-WordPress) -->

API 呼び出し例**

GET
  http://example.com/api/departments/[departmentid]/agents?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [departmentid] | text | エージェントのチーム ID 
| apikey | text | API キー 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| agents | list | チームに所属する全てのエージェントのリスト 
| "agents" フィールドには 6 種類のカラムがあります 
| userid | text | エージェントのユーザー ID
 
| firstname | text | エージェントの名 
| lastname | text | エージェントの姓
 
| email | text | エージェントのメールアドレス 
| onlinestatus | text | チームにおけるエージェントのオンラインステータス。次の値を組み合わせます T, P, M (T - チャット, P - 電話, M - 自動チケット解決) 
| presetstatus | text | チームにおけるエージェントの現在のステータス。 エージェントの有効ステータスが次の値を組み合わせて示されます。 T, P, M (T - チャット, P - 電話, M - 自動チケット解決) 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
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
  <agent>
   <userid>bc0s45s</userid>
   <firstname>Any</firstname>
   <lastname>Johnason</lastname>
   <email>any@agent.com</email>
   <onlinestatus>M</onlinestatus>
   <presetstatus>M</presetstatus>
  </agent>
 </agents>
</response>
 
| 
JSON
 | {
  "response":{
    "agents":[
      {
        "userid":"ag0h45s",
        "firstname":"John",
        "lastname":"Doe",
        "email":"john@agent.com",
        "onlinestatus":"M",
        "presetstatus":"M"
      },
      {
        "userid":"bc0s45s",
        "firstname":"Any",
        "lastname":"Johnason",
        "email":"any@agent.com",
        "onlinestatus":"M",
        "presetstatus":"M"
      }
    ]
  }
} 

### § チームのリストを呼び出す

※ LiveAgent version 2.8.2.1 以降に対応します。

API 呼び出し例**

GET
  http://example.com/api/departments?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| apikey | text | API キー 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| departments | list | エージェントのチームのリスト
 
| "departments" フィールドには 6 種類のカラムがあります 
| departmentid | text | チーム ID 
| name | text | チームの名称 
| description | text | チームの概要 
| onlinestatus | text | チームのオンラインステータス - チームレベルでのオンラインステータスを次の値を組み合わせて出力します。 T, P, M (T - チャット, P - 電話, M - 自動チケット解決) 
| presetstatus | text | チームの現在のステータス - チームがサービス提供可能かのステータスを、次の値を組み合わせて出力します。 T, P, M (T - チャット, P - 電話, M - 自動チケット解決) 
| deleted | constlist | If チームが削除されたかどうか (有効値： Y - 削除済, N - 未削除) 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <departments>
  <department>
   <departmentid>d1s58gs4</departmentid>
   <name>Department 1</name>
   <description>This is first deaprtment</description>
   <onlinestatus>M</onlinestatus>
   <presetstatus>M</presetstatus>
   <deleted>N</deleted>
  </department>
  <department>
   <departmentid>d2s58gs4</departmentid>
   <name>Department 2</name>
   <description>This is second deaprtment</description>
   <onlinestatus>R</onlinestatus>
   <presetstatus>MRT</presetstatus>
   <deleted>N</deleted>
  </department>
 </departments>
</response>
 
| 
JSON
 | {
  "response":{
    "departments":[
      {
        "departmentid":"d1s58gs4",
        "name":"Department 1",
        "description":"This is first deaprtment",
        "onlinestatus":"M",
        "presetstatus":"M",
        "deleted":"N"
      },
      {
        "departmentid":"d2s58gs4",
        "name":"Department 2",
        "description":"This is second deaprtment",
        "onlinestatus":"R",
        "presetstatus":"MRT",
        "deleted":"N"
      }
    ]
  }
} 

### § チームの詳細情報を呼び出す

※ LiveAgent version 2.8.2.1 以降に対応します。

API 呼び出し例**

GET
  http://example.com/api/departments/[departmentid]?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [departmentid] | text | エージェントのチーム ID 
| apikey | text | API キー 

出力データの内容**

呼び出しフィールド

| フィールド名 | 形式 | 内容 
| departmentid | text | エージェントのチーム ID 
| name | text | チームの名称 
| description | text | チームの概要
 
| onlinestatus | text | チームのオンラインステータス- チームレベルでのオンラインステータスを、次の値を組み合わせて出力します。 T,
 P, M (T - チャット, P - 電話, M - 自動チケット解決) 
| presetstatus | text | チームの現在のステータス - チームレベルでのサービス稼働状況を、次の値を組み合わせて出力します。
 T, P, M (T - チャット, P - 電話, M - 自動チケット解決) 
| deleted | constlist | チームが削除されたかどうか (有効値： Y - 削除済, N - 未削除) 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <departmentid>e4y7g8s8</departmentid>
 <name>Support</name>
 <description>General support department</description>
 <onlinestatus>M</onlinestatus>
 <presetstatus>M</presetstatus>
 <deleted>N</deleted>
</response>
 
| 
JSON
 | {
  "response":{
    "departmentid":"e4y7g8s8",
    "name":"Support",
    "description":"General support department",
    "onlinestatus":"M",
    "presetstatus":"M",
    "deleted":"N"
  }
}