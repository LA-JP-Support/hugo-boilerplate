---
title: "「エージェント」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-agent-api"
description: "※LiveAgent version 2.8.2.1以降に対応しています"
keywords: ["エージェント", "API", "LiveAgent", "メールアドレス", "Agent"]
type: support
category: "settings"
e-title: "Agent - Api"
---

### § エージェント情報と AUTH トークンの呼び出し

※LiveAgent version 2.8.2.1以降に対応しています

API の呼び出し例**

GET
  http://example.com/api/agents/[agentidentifier]?apikey=[value]

**
呼び出し時の必須パラメータ

| パラメータ | 形式 | 内容 

| [agentidentifier] | text | エージェントの識別子で、メールアドレスまたはユーザ ID が該当します。 

| apikey | text | LiveAgent の API キー 

出力データの内容**

出力フィールド

| フィールド名 | 形式 | 内容 

| contactid | text | エージェントのコンタクト ID 

| userid | text | エージェントのユーザー ID 

| email | text | エージェントのメールアドレス
 

| firstname | text | エージェントの名
 

| lastname | text | エージェントの姓 

| systemname | text | システム上のエージェント名
 

| authtoken | text | エージェントの AUTH トークン 

| browsercookiename | text | エージェントのブラウザのクッキー名
 

| gender | constlist | エージェントの性別 (有効値： M - 男性、F - 女性) 

| role | constlist | エージェントの権限種別 (有効値： D - 管理者、A - エージェント、O - 所有者) 

| データ出力例 

| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <contactid>d44t87a5</contactid>
 <userid>uid1234</userid>
 <email>example@agent.com</email>
 <firstname>John</firstname>
 <lastname>Williams</lastname>
 <systemname>system001</systemname>
 <authtoken>5ceef21647f1db39a18cafc0bc2de015</authtoken>
 <browsercookiename>A_auth</browsercookiename>
 <gender>F</gender>
 <role>D</role>
</response>
 

| 
JSON
 | {
  "response":{
    "contactid":"d44t87a5",
    "userid":"uid1234",
    "email":"example@agent.com",
    "firstname":"John",
    "lastname":"Williams",
    "systemname":"system001",
    "authtoken":"5ceef21647f1db39a18cafc0bc2de015",
    "browsercookiename":"A_auth",
    "gender":"F",
    "role":"D"
  }
}