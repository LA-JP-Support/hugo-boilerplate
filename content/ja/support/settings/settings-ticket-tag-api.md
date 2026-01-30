---
title: "スマートチケットの「タグ」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-ticket-tag-api"
description: "※LiveAgent version 4.0.30.6 以降に対応します。"
keywords: ["スマートチケット", "チケット", "API", "LiveAgent", "Agent"]
type: support
category: "settings"
e-title: "Ticket - Tag - Api"
---

### § 有効なすべてのタグのリストを呼び出す

※LiveAgent version 4.0.30.6 以降に対応します。

**
API 呼び出し例**

GET
  http://example.com/api/tags?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| apikey | text | API キー 

出力データの内容**

呼び出しフィールド

| フィールド名 | 形式 | 内容 
| tags | list | タグのリスト
 
| "tags" フィールドには 2 種類のカラムがあります  
| id | text | タグの識別子 
| name | text | タグの名称 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <tags>
  <tag>
   <id>sh3j</id>
   <name>VIP</name>
  </tag>
  <tag>
   <id>8sd5</id>
   <name>Support</name>
  </tag>
 </tags>
</response>
 
| 
JSON
 | {
  "response":{
    "tags":[
      {
        "id":"sh3j",
        "name":"VIP"
      },
      {
        "id":"8sd5",
        "name":"Support"
      }
    ]
  }
}