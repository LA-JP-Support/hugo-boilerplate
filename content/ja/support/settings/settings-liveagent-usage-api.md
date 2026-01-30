---
title: "LiveAgent で利用できる API "
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-liveagent-usage-api"
description: "LiveAgent では、皆様の業務によりよく活用していただけるよう API をご用意しています。多くの開発者にご利用いただけるよう、各種 API のドキュメントおよびサンプルコードについて、少しずつですがご紹介していきたいと思います。"
keywords: ["LiveAgent", "Agent", "API", "ナレッジベース", "メールアドレス"]
type: support
category: "settings"
e-title: "Liveagent - Usage - Api"
---

LiveAgent では、皆様の業務によりよく活用していただけるよう API をご用意しています。多くの開発者にご利用いただけるよう、各種 API のドキュメントおよびサンプルコードについて、少しずつですがご紹介していきたいと思います。

![](/liveagent/scripts/file.php?view=Y&file=edd470b0f9e89336f5304e62a9388854)

## LiveAgent で利用可能な API

### 目次

	- 
	#### 【フォーマット】

	

		[データフィールドのフォーマット](#dataformats)

		- [出力データの形式](#returnmsgs)

		- [エラーメッセージの形式](#errormsgs)

	

	 

	
	- 
	#### 【API 利用サンプル】

	

		[REST API の利用例 （サンプルコード）](http://support.smartweb.jp/liveagent/359468-REST-API-%E3%81%AE%E5%88%A9%E7%94%A8%E4%BE%8B-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89)

	

	 

	
	- 
	#### 【REST API v.1】

	

		エージェント
		

			[エージェント情報と AUTH トークンの呼び出し](http://support.smartweb.jp/liveagent/813683-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API)

		

		
		- アプリケーション
		

			[アプリケーションのインストール日時と最新バージョンの参照](http://support.smartweb.jp/liveagent/799875-%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API-%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E7%89%88)

		

		
		- 会話（チケット）
		

			[他のチームやエージェントへ、会話履歴（チケット）を転送する](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#0)

			- [会話履歴（チケット）の削除](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#1)

			- [依頼者、チーム、件名からの、全ての会話履歴（チケット）の参照](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#2)

			- [会話履歴（チケット）の個別情報の参照](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#3)

			- [すべての会話履歴メッセージの呼び出し](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#4)

			- [会話履歴（チケット）に新しいメッセージを作成する](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#5)

			- [会話履歴（チケット）を新規作成する](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#6)

			- [会話履歴（チケット）のステータスを変更する](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#7)

			- [会話履歴（チケット）に付けられたタグを解除する](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#8)

			- [会話履歴（チケット）に割り当てられたタグのリストを参照する](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#9)

			- [会話履歴（チケット）にタグを割り当てる](http://support.smartweb.jp/liveagent/312524-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E4%BC%9A%E8%A9%B1%E5%B1%A5%E6%AD%B4%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#10)

		

		
		- 顧客情報（コンタクト）
		

			[全ての顧客名を呼び出す](http://support.smartweb.jp/liveagent/029428-%E3%82%B3%E3%83%B3%E3%82%BF%E3%82%AF%E3%83%88%E9%A1%A7%E5%AE%A2%E6%83%85%E5%A0%B1%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#0)

			- [顧客情報を呼び出す](http://support.smartweb.jp/liveagent/029428-%E3%82%B3%E3%83%B3%E3%82%BF%E3%82%AF%E3%83%88%E9%A1%A7%E5%AE%A2%E6%83%85%E5%A0%B1%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#1)

			- [グループから顧客を除外する](http://support.smartweb.jp/liveagent/029428-%E3%82%B3%E3%83%B3%E3%82%BF%E3%82%AF%E3%83%88%E9%A1%A7%E5%AE%A2%E6%83%85%E5%A0%B1%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#2)

			- [顧客のグループを呼び出す](http://support.smartweb.jp/liveagent/029428-%E3%82%B3%E3%83%B3%E3%82%BF%E3%82%AF%E3%83%88%E9%A1%A7%E5%AE%A2%E6%83%85%E5%A0%B1%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#4)

			- [顧客をグループに追加する](http://support.smartweb.jp/liveagent/029428-%E3%82%B3%E3%83%B3%E3%82%BF%E3%82%AF%E3%83%88%E9%A1%A7%E5%AE%A2%E6%83%85%E5%A0%B1%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#5)

			- [顧客を新規登録する](http://support.smartweb.jp/liveagent/029428-%E3%82%B3%E3%83%B3%E3%82%BF%E3%82%AF%E3%83%88%E9%A1%A7%E5%AE%A2%E6%83%85%E5%A0%B1%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#6)

		

		
		- 顧客グループ
		

			[顧客グループの全てを呼び出す](http://support.smartweb.jp/liveagent/726348-%E9%A1%A7%E5%AE%A2%E3%81%AE%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#0)

		

		
		- エージェントのチーム
		

			[チームに所属する全てのエージェントのステータスを呼び出す](http://support.smartweb.jp/liveagent/919756-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E3%83%81%E3%83%BC%E3%83%A0%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#0)

			- [チームのリストを呼び出す](http://support.smartweb.jp/liveagent/919756-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E3%83%81%E3%83%BC%E3%83%A0%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#1)

			- [チームの詳細情報を呼び出す](http://support.smartweb.jp/liveagent/919756-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E3%83%81%E3%83%BC%E3%83%A0%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#2)

		

		
		- ナレッジベース
		

			[ナレッジベースを検索する](http://support.smartweb.jp/liveagent/991497-%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%83%BC%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB%E3%83%8A%E3%83%AC%E3%83%83%E3%82%B8%E3%83%99%E3%83%BC%E3%82%B9%E6%8F%90%E6%A1%88%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#0)

			- [全ての「提案」カテゴリーを呼び出す](http://support.smartweb.jp/liveagent/991497-%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%83%BC%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB%E3%83%8A%E3%83%AC%E3%83%83%E3%82%B8%E3%83%99%E3%83%BC%E3%82%B9%E6%8F%90%E6%A1%88%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#1)

			- [「提案」を新規作成する](http://support.smartweb.jp/liveagent/991497-%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%83%BC%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB%E3%83%8A%E3%83%AC%E3%83%83%E3%82%B8%E3%83%99%E3%83%BC%E3%82%B9%E6%8F%90%E6%A1%88%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#2)

		

		
		- チケットのタグ
		

			[有効なすべてのタグのリストを呼び出す](http://support.smartweb.jp/liveagent/121835-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E3%81%AE%E3%82%BF%E3%82%B0%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B-API#0)

		

		
	

	

 

## データフィールドのフォーマット

	
		
			| 変数 
			| 内容 
		

		
			| datetime 
			| 日付の表示は、次の書式が適用されます: YYYY-MM-DD HH:MM:SS.**
			　注: 日付の表示はデフォルトで「太平洋標準時（UTC-8）」が適用されます 
		

		
			| text 
			| 任意の文字列または空欄 
		

		
			| constlist 
			| 有限集合の中のただ1つのインスタンスです。可用値は、特定フィールドの定義で指定されています。 
		

		
			| int 
			| 0以上の整数値 
		

		
			| list 
			| エンティティのリスト。すべてのエンティティは、その特定の列の定義を持っています。 
		

		
			| opdatetime 
			| 演算子の日付。このフィールドの書式は、以下のような演算子を用いない場合 'datetime' と共通となります。

			

			利用可能な演算子：
			

				- eq:** 等しい　例） 'eq:2009-11-12 05:02:01' または '2009-11-12 05:02:01'

				- **neq:** 等しくない　例） 'neq:2009-11-12 05:02:01'

				- **gt:** より大きい　例） 'gt:2009-11-12 05:02:01'

				- **lt:** より小さい　例） 'lt:2009-11-12 05:02:01'

				- **gte:** 以上である　例） 'gte:2009-11-12 05:02:01'

				- **lte:** 以下である　例） 'lte:2009-11-12 05:02:01'

				- **btw:** 中間である　例） 'btw:2009-11-12 05:02:01,2010-10-11 04:01:59'

				- **lk:** 含んでいる　例） 'lk:2009-11-12 05:02:01' これはワイルドカード "%" (すべての数値) または "?" (1桁の数値) を用いて 'lk:2009-01-%' or 'lk:2011-12-01 ??:59:59' と表記することも可能です。

			

			　注：演算子を用いない場合, 'eq' がデフォルトで適用されます。 
		

	

[目次へ戻る↑](#apiindex)

## 出力データの形式

LiveAgent API から出力されるデータは JSON 形式がデフォルトとなっています。XML 形式で出力する場合は、API の呼び出し URL の末尾に ".xml" を付け加えることで対応します。

例 1）　次の URL から呼び出す際は、JSON 形式のデータを出力します。

GET

  http://example.com/api/agents/john@agent.com

**
例 2）　上記 URL の末尾に .xml** を加えることで、XML 形式のデータ出力に対応します。

GET

  http://example.com/api/agents/john@agent.com.xml

**
注: お使いの PHP で [PHP YAML](http://www.php.net/manual/en/book.yaml.php) 拡張が有効な場合、URL の末尾に".yaml**" を加えることで YAML 形式の出力にも対応します。

[目次へ戻る↑](#apiindex)

## エラーメッセージの形式

	**400 - Bad request**
	
	アプリケーション内の API キーの問題による、API キーの認証エラー時に表示されます。

	
	**401 - Forbidden**
	
	誤った API キー利用による認証エラー時に表示されます。

	
	**404 - Not found**
	
	「入力したメールアドレスに該当するエージェントが見つからない」場合に表示されます。

	
	**500 - Common porcessing error**
	
	これは最も多いエラー形式です。「パラメータのメッセージが見つからない」場合や「会話の読み込みができない」場合に表示されます。

	
	**503 - Service Unavailable**
	
	プロセス要求（アップデートやインストールなど）に対しアプリケーションが無効である場合に表示されます。

	

 

	
		
			| Error response example 
		

		
			| 
			
XML

			 
			| 
			
<?xml version="1.0" encoding="utf-8"?>
<response>
 <status>ERROR</status>
 <statuscode>500</statuscode>
 <errormessage>Example error message</errormessage>
 <debugmessage>debug info</debugmessage>
</response>

			 
		

		
			| 
			
JSON

			 
			| 
			
{
  "response":{
    "status":"ERROR",
    "statuscode":500,
    "errormessage":"Example error message",
    "debugmessage":"debug info"
  }
}
			 
		

	

[目次へ戻る↑](#apiindex)

 

現在利用可能な API のリファレンスは[**こちら（英語ページ）**](https://support.ladesk.com/840770-Complete-API-reference)をご参照ください