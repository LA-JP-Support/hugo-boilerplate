---
title: "「カスタマーポータル（ナレッジベース/提案）」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-customer-portal-knowledge-base-suggestion"
description: "※ LiveAgent version 4.7.3.0 以降に対応します。"
keywords: ["カスタマーポータル", "ナレッジベース", "ナレッジ", "Suggestions", "LiveAgent"]
type: support
category: "settings"
e-title: "Customer Portal - Knowledge Base - Suggestion - Api"
---

## 【目次】

	- [ナレッジベースを検索する](#0)

	- [全ての「提案」カテゴリーを呼び出す](#1)

	- [「提案」を新規作成する](#2)

 

### § ナレッジベースを検索する

※ LiveAgent version 4.7.3.0 以降に対応します。

**

API 呼び出し例**

GET

  http://example.com/api/knowledgebase/search?query=[value]&apikey=[value]

 

呼び出し時の必須パラメータ

	
		
			| パラメータ名 
			| 形式 
			| 内容 
		

		
			| query 
			| text 
			| 検索クエリの文字列 
		

		
			| apikey 
			| text 
			| API キー 
		

	

 

オプションのパラメータ

	
		
			| パラメータ名 
			| 形式 
			| 内容 
		

		
			| top_article_id 
			| text 
			| Top article ID. Search will start from given ID. Leave empty if all articles should be searched. 
		

	

**

出力データの内容****
 
呼び出しフィールド

	
		
			| フィールド名 
			| 形式 
			| 内容 
		

		
			| articles 
			| list 
			| ナレッジベースの記事リスト 
		

		
			| "articles" フィールドには 12 種類のカラムがあります 
		

		
			| kb_entry_id 
			| text 
			| ナレッジベースの記事 ID 
		

		
			| urlcode 
			| text 
			| ナレッジベースの記事 URL ID 
		

		
			| title 
			| text 
			| 件名/タイトル 
		

		
			| content_text 
			| text 
			| 記事内容 
		

		
			| content_simple_html 
			| text 
			| Simple and short article HTML 
		

		
			| treepath 
			| text 
			| Tree path 
		

		
			| rtype 
			| text 
			| 形式 （有効値： A - 返答済み...etc） 
		

		
			| rstatus 
			| text 
			| ステータス (有効値：P - ...etc） 
		

		
			| votesCount 
			| text 
			| 「提案」の投票カウント数 
		

		
			| datechanged 
			| text 
			| 最終更新日時 
		

		
			| conversationid 
			| text 
			| 会話履歴（チケット） ID (関連づけられている場合のみ) 
		

		
			| url 
			| text 
			| ナレッジベース記事 URL 
		

	

 

	
		
			| データ出力例 
		

		
			| 
			
XML

			 
			| 
			
<?xml version="1.0" encoding="utf-8"?>
<response>
 <articles>
  <article>
   <kb_entry_id>4150</kb_entry_id>
   <urlcode>011157</urlcode>
   <title>LiveAgent integration</title>
   <content_text>Please note: this integration is available in PostAffiliatePro v.5.0.6.8</content_text>
   <content_simple_html>Please note: this integration is available in PostAffiliatePro v.5.0.6.8</content_simple_html>
   <treepath>0|449|541|4149</treepath>
   <rtype>A</rtype>
   <rstatus>P</rstatus>
   <votesCount>0</votesCount>
   <datechanged>2013-08-21 00:47:51</datechanged>
   <conversationid/>
   <url>\/\/support.qualityunit.com\/011157-LiveAgent-integration</url>
  </article>
 </articles>
</response>

			 
		

		
			| 
			
JSON

			 
			| 
			
{
  "response":{
    "articles":[
      {
        "kb_entry_id":"4150",
        "urlcode":"011157",
        "title":"LiveAgent integration",
        "content_text":"Please note: this integration is available in PostAffiliatePro v.5.0.6.8",
        "content_simple_html":"Please note: this integration is available in PostAffiliatePro v.5.0.6.8",
        "treepath":"0|449|541|4149",
        "rtype":"A",
        "rstatus":"P",
        "votesCount":"0",
        "datechanged":"2013-08-21 00:47:51",
        "conversationid":"",
        "url":"\\\/\\\/support.qualityunit.com\\\/011157-LiveAgent-integration"
      }
    ]
  }
}
			 
		

	

 

### § 全ての「提案」カテゴリーを呼び出す

※ LiveAgent version 2.8.2.1 以降に対応します。

API 呼び出し例**

GET

  http://example.com/api/suggestioncategories?apikey=[value]

 

呼び出し時の必須パラメータ

	
		
			| パラメータ名 
			| 形式 
			| 内容 
		

		
			| apikey 
			| text 
			| API キー 
		

	

**

出力データの内容****
 
呼び出しフィールド

	
		
			| フィールド名 
			| 形式 
			| 内容 
		

		
			| suggestioncategories 
			| list 
			| 提案カテゴリーのリスト 
		

		
			| "suggestioncategories" フィールドには 3 種類のカラムがあります 
		

		
			| id 
			| text 
			| カテゴリーの ID 
		

		
			| title 
			| text 
			| カテゴリーのタイトル 
		

		
			| path 
			| text 
			| カテゴリーの配置（パス） 
		

	

 

	
		
			| データ出力例 
		

		
			| 
			
XML

			 
			| 
			
<?xml version="1.0" encoding="utf-8"?>
<response>
 <suggestioncategories>
  <suggestioncategorie>
   <id>15</id>
   <title>Suggestions</title>
   <path>Product1 / Suggestion</path>
  </suggestioncategorie>
  <suggestioncategorie>
   <id>16</id>
   <title>Ideas</title>
   <path>Product2 / Ideas</path>
  </suggestioncategorie>
 </suggestioncategories>
</response>

			 
		

		
			| 
			
JSON

			 
			| 
			
{
  "response":{
    "suggestioncategories":[
      {
        "id":"15",
        "title":"Suggestions",
        "path":"Product1 \/ Suggestion"
      },
      {
        "id":"16",
        "title":"Ideas",
        "path":"Product2 \/ Ideas"
      }
    ]
  }
}
			 
		

	

 

### § 「提案」を新規作成する

※ LiveAgent version 3.0.18.2 以降に対応します。

API 呼び出し例**

POST

  http://example.com/api/suggestions

　注: この API コールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-の利用例-サンプルコード#post) の POST メソッドを利用します**
 
呼び出し時の必須パラメータ

	
		
			| パラメータ名 
			| 形式 
			| 内容 
		

		
			| useridentifier 
			| text 
			| ユーザーのメールアドレス 
		

		
			| category 
			| text 
			| 提案のカテゴリー (ID または URL コード) 
		

		
			| subject 
			| text 
			| 提案の件名 
		

		
			| message 
			| text 
			| 提案の内容 
		

		
			| apikey 
			| text 
			| API キー 
		

	

出力データの内容**

 
呼び出しフィールド

	
		
			| フィールド名 
			| 形式 
			| 内容 
		

		
			| status 
			| text 
			| OK 
		

		
			| statuscode 
			| int 
			| 実行されたリクエストのステータスコード 
		

		
			| id 
			| text 
			| 提案の ID 
		

		
			| url 
			| text 
			| 提案のページ URL 
		

	

 

	
		
			| データ出力例 
		

		
			| 
			
XML

			 
			| 
			
<?xml version="1.0" encoding="utf-8"?>
<response>
 <status>OK</status>
 <statuscode>0</statuscode>
 <id>s4ds456a</id>
 <url>http://www.yoursite.com/856325-New-Suggeston</url>
</response>

			 
		

		
			| 
			
JSON

			 
			| 
			
{
  "response":{
    "status":"OK",
    "statuscode":0,
    "id":"s4ds456a",
    "url":"http:\/\/www.yoursite.com\/856325-New-Suggeston"
  }
}