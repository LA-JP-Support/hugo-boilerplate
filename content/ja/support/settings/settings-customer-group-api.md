---
title: "顧客の「グループ」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-customer-group-api"
description: "※ LiveAgent version 4.0.19.1 以降に対応します。**"
keywords: ["グループ", "API", "顧客", "LiveAgent", "groups"]
type: support
category: "settings"
e-title: "Customer - Group - Api"
---

### § 顧客グループの全てを呼び出す

※ LiveAgent version 4.0.19.1 以降に対応します。**

API 呼び出し例**

GET
  http://example.com/api/customersgroups?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| apikey | text | API キー 

出力データの内容**

呼び出しフィールド

| フィールド名 | 形式 | 内容 
| groups | list | 顧客の全てのグループ 
| "groups" フィールドには 2 種類のカラムがあります:  
| groupid | text | グループ ID 
| groupname | text | グループの名称 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <groups>
  <group>
   <groupid>ag0h</groupid>
   <groupname>VIP</groupname>
  </group>
  <group>
   <groupid>2kt8</groupid>
   <groupname>Premium</groupname>
  </group>
 </groups>
</response>
 
| 
JSON
 | {
  "response":{
    "groups":[
      {
        "groupid":"ag0h",
        "groupname":"VIP"
      },
      {
        "groupid":"2kt8",
        "groupname":"Premium"
      }
    ]
  }
}