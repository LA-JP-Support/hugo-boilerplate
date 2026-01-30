---
title: "「コンタクト（顧客情報）」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-customer-info-api"
description: "※ LiveAgent version 2.8.2.1 以降に対応します。"
keywords: ["API", "顧客", "情報", "LiveAgent", "メールアドレス"]
type: support
category: "settings"
e-title: "Customer - Info - Api"
---

## 【目次】

- [全ての顧客名を呼び出す](#0)

- [顧客情報を呼び出す](#1)

- [グループから顧客を除外する](#2)

- [顧客のグループを呼び出す](#4)

- [顧客をグループに追加する](#5)

- [顧客を新規登録する](#6)

**

### § 全ての顧客名を呼び出す

※ LiveAgent version 2.8.2.1 以降に対応します。

API 呼び出し例**

GET
  http://example.com/api/customers?apikey=[value]
**呼び出し時に必須のパラメータ

| パラメータ名 | 形式 | 内容 
| apikey | text | API キー 

オプションのパラメータ

| パラメータ名 | 形式 | 内容 
| email | text | 指定の文字列を含むメールアドレスを有する顧客情報を呼び出します 
| firstname | text | 指定の文字列を含む名を有する顧客情報を呼び出します 
| lastname | text | 指定の文字列を含む姓を有する顧客情報を呼び出します 
| datecreatedfrom | datetime | 作成日がこの日時より新しい顧客情報を呼び出します 
| datecreatedto | datetime | 作成日がこの日時より古い顧客情報を呼び出します 
| limitcount | text | 指定値を呼び出し件数の最大値とします (デフォルトでは 100、最大 1,000まで値を指定できます) 
| limitfrom | text | Start from specified row number 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| customers | list | 顧客のリスト 
| Field customers has 8 columns:  
| contactid | text | 顧客のコンタクト ID 
| email | text | 顧客のメールアドレスl 
| firstname | text | 顧客の名 
| lastname | text | 顧客の姓 
| systemname | text | 顧客のシステム名 
| userid | text | 顧客のユーザー ID 
| role | constlist | 顧客の属性 (有効値： V - Visitor, R - Registered visitor) 
| gender | constlist | 顧客の性別 (有効値： M - 男性, F - 女性) 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <customers>
  <customer>
   <contactid>cid00001</contactid>
   <email>john@example.com</email>
   <firstname>John</firstname>
   <lastname>Doe</lastname>
   <systemname>system001</systemname>
   <userid>uid00001</userid>
   <gender>M</gender>
  </customer>
  <customer>
   <contactid>cid00002</contactid>
   <email>Janet@example.com</email>
   <firstname>Janet</firstname>
   <lastname>Doe</lastname>
   <systemname>system002</systemname>
   <userid>uid00002</userid>
   <gender>M</gender>
  </customer>
 </customers>
</response>
 
| 
JSON
 | {
  "response":{
    "customers":[
      {
        "contactid":"cid00001",
        "email":"john@example.com",
        "firstname":"John",
        "lastname":"Doe",
        "systemname":"system001",
        "userid":"uid00001",
        "gender":"M"
      },
      {
        "contactid":"cid00002",
        "email":"Janet@example.com",
        "firstname":"Janet",
        "lastname":"Doe",
        "systemname":"system002",
        "userid":"uid00002",
        "gender":"M"
      }
    ]
  }
} 

### § 顧客情報を呼び出す

※ LiveAgent version 2.9.5.0 以降に対応しています。

API 呼び出し例**

GET
  http://example.com/api/customers/[customeridentifier]?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [customeridentifier] | text | 顧客の識別子 (メールアドレスまたはコンタクト ID) 
| apikey | text | API キー 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| contactid | text | 顧客のコンタクト ID 
| email | text | 顧客のメールアドレス 
| firstname | text | 顧客の名 
| lastname | text | 顧客の姓 
| systemname | text | 顧客のシステム名 
| authtoken | text | 顧客のブラウザクッキーの識別子 
| browsercookiename | constlist | 顧客のブラウザクッキーの名称 (有効値： V_auth - Registerd visitor cookie name, LaVisitorId - Not yet registered visitor cookie name) 
| role | constlist | 顧客の属性 (有効値： V - Visitor, R - Registered visitor) 
| gender | constlist | 顧客の性別 (Possible values: M - Male, F - Female) 
| userid | text | 顧客のユーザー ID 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <contactid>cid00001</contactid>
 <email>john@example.com</email>
 <firstname>John</firstname>
 <lastname>Doe</lastname>
 <systemname>system001</systemname>
 <authtoken>4fsd5f4s6f4s56f4s56f4s56f4sd56</authtoken>
 <browsercookiename>V_auth</browsercookiename>
 <role>V</role>
 <gender>M</gender>
 <userid>uid00001</userid>
</response>
 
| 
JSON
 | {
  "response":{
    "contactid":"cid00001",
    "email":"john@example.com",
    "firstname":"John",
    "lastname":"Doe",
    "systemname":"system001",
    "authtoken":"4fsd5f4s6f4s56f4s56f4s56f4sd56",
    "browsercookiename":"V_auth",
    "role":"V",
    "gender":"M",
    "userid":"uid00001"
  }
} 

### § グループから顧客を除外する

※ LiveAgent version 2.9.5.0 以降に対応します。

API 呼び出し例**

DELETE
  http://example.com/api/customers/[customeridentifier]/groups?name=[value]&apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [customeridentifier] | text | 顧客の識別子 (メールアドレスまたはコンタクト ID) 
| name | text | 顧客のグループ名 
| apikey | text | API キー 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| status | text | OK 
| statuscode | int | 実行されたリクエストのステータスコード 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <status>OK</status>
 <statuscode>0</statuscode>
</response>
 
| 
JSON
 | {
  "response":{
    "status":"OK",
    "statuscode":0
  }
} 

### § 顧客のグループを呼び出す

※ LiveAgent version 2.9.5.0 以降に対応します。

API 呼び出し例**

GET
  http://example.com/api/customers/[customeridentifier]/groups?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [customeridentifier] | text | 顧客の識別子 (メールアドレスまたはコンタクト ID) 
| apikey | text | API キー 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| groups | list | 顧客の含まれるすべてのグループのリスト 
| "groups" フィールドには 2 種類のカラムがあります  
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

### § 顧客をグループに追加する

※ LiveAgent version 2.9.5.0 以降に対応します。

API 呼び出し例**

POST
  http://example.com/api/customers/[customeridentifier]/groups
　注： このコールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-の利用例-サンプルコード#post) の POST メソッドを利用します。**
呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [customeridentifier] | text | 顧客の識別子 (メールアドレスまたはコンタクト ID) 
| name | text | 顧客を追加したいグループの名称 
| apikey | text | API キー 

出力データの内容****
呼び出しフィールド

| フィールド名 | 形式 | 内容 
| status | text | OK 
| statuscode | int | 実行されたリクエストのステータスコード 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <status>OK</status>
 <statuscode>0</statuscode>
</response>
 
| 
JSON
 | {
  "response":{
    "status":"OK",
    "statuscode":0
  }
} 

### § 顧客を新規登録する

※ LiveAgent version 2.9.5.0 以降に対応します。

API 呼び出し例**

POST
  http://example.com/api/customers
　注： このコールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-の利用例-サンプルコード#post) の POST メソッドを利用します。**
呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| apikey | text | API キー 

オプションのパラメータ

| パラメータ名　　
 | 形式 | 内容 
| email | text | 顧客のメールアドレス 
| name | text | 顧客の氏名。"名 姓"の順で入力します。 
| gender | constlist | 性別 (有効値： M - 男性, F - 女性) 
| role | constlist | 属性 (Possible values: V - Visitor, R - Registered visitor) 
| password | text | Registerred visitor のみパスワードを設定できます。空欄の場合、パスワード設定リクエストの通知メールをこの visitor へ送信します。 

出力データの内容**

呼び出しフィールド

| フィールド名 | 形式 | 内容 
| contactid | text | 顧客のコンタクト ID 
| email | text | 顧客のメールアドレス 
| firstname | text | 顧客の名 
| lastname | text | 顧客の姓 
| systemname | text | 顧客のシステム名 
| authtoken | text | 顧客のブラウザクッキーの識別子 
| browsercookiename | constlist | 顧客のブラウザクッキーの名称 (有効値： V_auth - Registerd visitor cookie name, LaVisitorId - Not yet registered visitor cookie name) 
| role | constlist | 顧客の属性 (有効値： V - Visitor, R - Registered visitor) 
| gender | constlist | 顧客の性別 (有効値： M - 男性, F - 女性) 
| userid | text | 顧客のユーザー ID 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <contactid>cid00001</contactid>
 <email>john@example.com</email>
 <firstname>John</firstname>
 <lastname>Doe</lastname>
 <systemname>system001</systemname>
 <authtoken>4fsd5f4s6f4s56f4s56f4s56f4sd56</authtoken>
 <browsercookiename>V_auth</browsercookiename>
 <role>V</role>
 <gender>M</gender>
 <userid>uid00001</userid>
</response>
 
| 
JSON
 | {
  "response":{
    "contactid":"cid00001",
    "email":"john@example.com",
    "firstname":"John",
    "lastname":"Doe",
    "systemname":"system001",
    "authtoken":"4fsd5f4s6f4s56f4s56f4s56f4sd56",
    "browsercookiename":"V_auth",
    "role":"V",
    "gender":"M",
    "userid":"uid00001"
  }
}