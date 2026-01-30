---
title: "「スマートチケット（会話履歴）」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-ticket-history-api"
description: "※LiveAgent version 2.8.2.1以降に対応しています"
keywords: ["スマートチケット", "チケット", "API", "LiveAgent", "WordPress"]
type: support
category: "settings"
e-title: "Ticket - History - Api"
---

## 【目次】

- [他のチームやエージェントへ、会話履歴（チケット）を転送する](#0)

- [会話履歴（チケット）の削除](#1)

- [依頼者、チーム、件名からの、全ての会話履歴（チケット）の参照](#2)

- [会話履歴（チケット）の個別情報の参照](#3)

- [すべての会話履歴メッセージの呼び出し](#4)

- [会話履歴（チケット）に新しいメッセージを作成する](#5)

- [会話履歴（チケット）を新規作成する](#6)

- [会話履歴（チケット）のステータスを変更する](#7)

- [会話履歴（チケット）に付けられたタグを解除する](#8)

- [会話履歴（チケット）に割り当てられたタグのリストを参照する](#9)

- [会話履歴（チケット）にタグを割り当てる](#10)

**

### § 他のチームやエージェントへ、会話履歴（チケット）を転送する

※LiveAgent version 2.8.2.1以降に対応しています

API の呼び出し例**

PUT
  http://example.com/api/conversations/[conversationid]/attendants**
注：この API コールには [PUT メソッド](http://support.smartweb.jp/liveagent/359468-REST-API-%E3%81%AE%E5%88%A9%E7%94%A8%E4%BE%8B-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89#put)を使用する必要があります

呼び出し時の必須パラメータ

| パラメータ | 形式 | 内容 

| [conversationid] | text | 会話履歴の ID、コード、または公開 URL コードが入ります。 

| apikey | text | LiveAgent の API キー 

パラメータのオプション

| パラメータ | 形式 | 内容 

| agentidentifier | text | エージェント識別子で、メールアドレスかユーザー ID が入ります。 

| useridentifier | text | 会話履歴を転送するユーザーの識別子（メールアドレスまたはユーザー ID）です。不明の場合は "System" が自動挿入されます。 

| department | text | チーム ID （※「チーム名」ではありません） 

| note | text | 転送の理由 

出力データの内容**
**

戻り値のフィールド

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
    "statuscode":"0",
  }
} 

### § 会話履歴（チケット）の削除

※LiveAgent version 2.8.2.1以降に対応しています[](http://support.qualityunit.com/060256-Single-sign-on-example-for-WordPress)

API の呼び出し例**

DELETE
  http://example.com/api/conversations/[conversationid]?apikey=[value]

**
呼び出し時の必須パラメータ

| パラメータ 
| 形式 
| 内容 

| [conversationid] 
| text 
| 会話履歴の ID、コード、または公開 URL コードが入ります。 

| apikey 
| text 
| LiveAgent の API キー 

パラメータのオプション

| パラメータ 
| 形式 
| 内容 

| note 
| text 
| 削除のノート 

| useridentifier 
| text 
| 会話履歴を転送するユーザーの識別子（メールアドレスまたはユーザー ID）です。不明の場合は "System" が自動挿入されます。 

出力データの内容**
**

戻り値のフィールド

| フィールド名 
| 形式 
| 内容 

| status 
| text 
| OK 

| statuscode 
| int 
| 実行されたリクエストのステータスコード 

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
    "statuscode":"0",
  }
} 

### § 依頼者、チーム、件名からの、全ての会話履歴（チケット）の参照

※LiveAgent version 2.8.2.1以降に対応しています

API の呼び出し例**

GET
  http://example.com/api/conversations?apikey=[value]

**
呼び出し時の必須パラメータ

| パラメータ 
| 形式 
| 内容 

| apikey 
| text 
| LiveAgent の API キー 

パラメータのオプション

| パラメータ 
| 形式 
| 内容 

| owneridentifier 
| text 
| 会話履歴の依頼者（オーナー）の識別子で、メールアドレスが入ります 

| department 
| text 
| エージェントの「チーム」の識別子 

| status 
| text 
| 指定されたステータスの会話履歴のみ呼び出します。ステータスの指定は1つ以上から可能で、複数指定する場合はカンマで区切ります。例： status=R,T,C
注：このパラメータは version 2.8.12.1 以降が対象です 

| datefrom 
| datetime 
| 指定日時より新しい会話履歴を呼び出します 

| dateto 
| datetime 
| 指定日時より古い会話履歴を呼び出します 

| datechanged 
| opdatetime 
| 会話履歴を変更した最終日時 

| subject 
| text 
| 指定した件名の会話履歴を呼び出します
注：version 3.0.1.2 以降が対象です 

注："department" と "owneridentifier" のどちらか、または両方を入力する必要があります。少なくとも一項目の入力を怠った場合、コールは除外されます。

出力データの内容**
**

出力フィールド

| フィールド名 
| 形式 
| 内容 

| conversations 
| list | 会話履歴のリスト 

| "conversation" フィールドには 12種類のカラムがあります： 

| conversationid | text | 会話履歴の ID 

| code | text | 会話履歴のコード 

| datecreated 
| datetime 
| データの作成日時 

| datechanged | datetime | データの最終更新日時 

| departmemtname | text | チーム名 

| departmentid | text | チーム ID 

| status 
| constlist | 会話履歴のステータス（有効値：A - 返信済み、P - 呼び出し、T - チャット、X - 削除された、B - スパム、I - 内部、C - オープン、R - 完了、N - 新規、W - 延期された） 

| ownername | text | 会話履歴の所有者（依頼者）の氏名 

| owneremail 
| text 
| 会話履歴の所有者のメールアドレス 

| subject | text | 会話履歴の件名 

| preview | text | 会話履歴のプレビュー 

| publicurlcode 
| text 
| 会話履歴の公開 URL コード 

| データ出力例 

| 

XML
 
| 

<?xml version="1.0" encoding="utf-8"?>
<response>
 <conversations>
  <conversation>  
   <conversationid>s4y7t5s7</conversationid>
   <code>AX4-B4T-FD8</code>
   <datecreated>2012-03-02 11:21:04</datecreated>
   <datechanged>2012-03-02 11:21:05</datechanged>
   <department>Department 1</department>
   <departmeintid>a5j9t4d8</departmentid>
   <status>A</status>
   <ownername>John Owner</ownername>
   <ownermail>john@owner.com</ownermail>
   <subject>Test ticket</subject>
   <preview>this is test ticket</preview>
   <publicurlcode>bI5fR3oN40708G65</publicurlcode>
  </conversation>
  <conversation>
   <conversationid>5h7t58d9</conversationid>
   <code>D5S-55S-A9A</code>
   <datecreated>2012-03-02 12:21:04</datecreated>
   <datechanged>2012-03-02 12:21:05</datechanged>
   <department>Department 1</department>
   <departmeintid>a5j9t4d8</departmentid>
   <status>A</status>
   <ownername>John Sliver</ownername>
   <ownermail>john@Silver.com</ownermail>
   <subject>My ticket</subject>
   <preview>this is my ticket</preview>
   <publicurlcode>xU6fR3zN40708G65</publicurlcode>
  </conversation>
 </conversations>
</response>
 

| 
JSON
 
| {
  "response":{
    "conversations":[
      {
        "conversationid":"s4y7t5s7",
        "code":"AX4-B4T-FD8",
        "datecreated":"2012-03-02 11:21:04",
        "datechanged":"2012-03-02 11:21:05",
        "departmentname":"Department 1",
        "departmentid":"a5j9t4d8",
        "status":"A",
        "ownername":"John Owner",
        "owneremail":"john@owner.com",
        "subject":"Test ticket",
        "preview":"this is test ticket",
        "publicurlcode":"bI5fR3oN40708G65"
      },
      {
        "conversationid":"5h7t58d9",
        "code":"D5S-55S-A9A",
        "datecreated":"2012-03-02 12:21:04",
        "datechanged":"2012-03-02 12:21:05",
        "departmentname":"Department 1",
        "departmentid":"a5j9t4d8",
        "status":"A",
        "ownername":"John Silver",
        "owneremail":"john@silver.com",
        "subject":"My ticet",
        "preview":"this my ticket",
        "publicurlcode":"xU6fR3zN40708G65"
      }
    ]
  }
} 

### § 会話履歴（チケット）の個別情報の参照

※ LiveAgent version 2.8.2.1 以降に対応しています。

API の呼び出し例**

GET
  http://example.com/api/conversations/[conversationid]?apikey=[value]

**
呼び出し時の必須パラメータ

| パラメータ名 
| 形式 
| 内容 

| [conversationid] 
| text 
| 会話履歴  ID、コード、または公開 URL コード 

| apikey 
| text 
| LiveAgent の API キー 

出力データの内容**
**

出力フィールド

| フィールド名 
| 形式 
| 内容 

| conversationid 
| text 
| 会話履歴（チケット） ID 

| code 
| text 
| 会話履歴コード 

| datecreated 
| datetime 
| 会話履歴の作成日時 

| datechanged 
| datetime 
| 会話履歴の最終更新日時 

| departmentname 
| text 
| 割り当てられたチーム名 

| departmentid 
| text 
| 割り当てられたチームの ID 

| status 
| constlist 
| 会話履歴のステータス (有効値： A - 返信済み、P - 呼び出し、T - チャット、X - 削除された、B - スパム、I - 内部、 C - オープン、R - 完了、N - 新規、W - 延期された) 

| ownername 
| text 
| 会話履歴の所有者（依頼者）名 

| owneremail 
| text 
| 会話履歴の所有者（依頼者）のメールアドレス 

| subject 
| text 
| 会話の件名 

| ownernote 
| text 
| 会話履歴の所有者のノート - 
　注：version 2.8.12.X+以降で有効 

| preview 
| text 
| 会話履歴のプレビュー 

| publicurlcode 
| text 
| 公開 URL コード 

| assignedto 
| text 
| 会話履歴を割り当てられたエージェントの識別子 

| データ出力例 

| 
XML
 | <?xml version="1.0" encoding=<font color="#FF00FF">"utf-8"?>
<response>
 <conversationid>cid00001</conversationid>
 <code>C01-D54-E45</code>
 <datecreated>2012-04-01 00:15:11</datecreated>
 <datechanged>2012-04-01 00:15:21</datechanged>
 <departmentname>Department 1</departmentname>
 <departmentid>dep1s5a4</departmentid>
 <status>R</status>
 <ownername>John Doe</ownername>
 <owneremail>owner@example.com</owneremail>
 <subject>My first ticket</subject>
 <ownernote/>
 <preview>Hello, this is my first ticket...</preview>
 <publicurlcode>bI5fR3oN40708G65</publicurlcode>
 <assignedto/>
</response> 

| 
JSON
 
| {
  "response":{
    "conversationid":"cid00001",
    "code":"C01-D54-E45",
    "datecreated":"2012-04-01 00:15:11",
    "datechanged":"2012-04-01 00:15:21",
    "departmentname":"Department 1",
    "departmentid":"dep1s5a4",
    "status":"R",
    "ownername":"John Doe",
    "owneremail":"owner@example.com",
    "subject":"My first ticket",
    "ownernote":null,
    "preview":"Hello, this is my first ticket...",
    "publicurlcode":"bI5fR3oN40708G65",
    "assignedto":null
  }
} 

### § すべての会話履歴メッセージの呼び出し

※ LiveAgent version: 2.8.2.1 以降に対応しています

API 呼び出し例**

GET
  http://example.com/api/conversations/[conversationid]/messages?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [conversationid] | text | 会話履歴 ID、コード、または公開 URL コード 
| apikey | text | LiveAgent の API キー 

パラメータのオプション

| パラメータ名 | 形式 | 内容 
| datefrom | datetime | 指定日時より新しい会話履歴を呼び出します. 
| dateto | datetime | 指定日時より古い会話履歴を呼び出します. 

出力データの内容****
出力フィールド

| フィールド名 | 形式 | 内容 
| groups | list | メッセージのグループ （メッセージを束ねたチケットを指します） 
| groups フィールドには 7 種類のカラムがあります：  
| messagegroupid | text | メッセージグループの ID 
| userid | text | グループに関連付けられたユーザーの ID 
| rtype | constlist | グループの形式 (有効値： P - 呼び出し, C - チャット, X - 消去された, F - Facebook, I - 内部, Z - 内部 (collapsed by default), K - ナレッジベース, A - Type knowledgebase start, M - オフライン, R - 解決された, Y - リツイート, S - Type startinfo, G - タグ, T - 転送, W - Twitter) 
| rstatus | constlist | グループのステータス (有効値： D - 消去された, P - Status promoted, V - 閲覧可, S - 分割された) 
| datecreated | datetime | 作成日時 
| datefinished | datetime | 最終メッセージの日時 
| messages | list | メッセージ　（チケットに紐付いたメール等の単体を指します） 
| messages フィールドには 5 つのカラムがあります：  
| messageid | text | メッセージの ID 
| userid | text | メッセージユーザーの ID 
| rtype | constlist | メッセージの形式 (有効値： D - 呼び出し, E - 終了, F - ファイル, Z - Type フォームフィールド, H - ヘッダー, I - 内部, M - メッセージ, B - 分割された, X - Type mixed message, N - ノート, L - ノートファイル, Q - 引用テキスト, C - Type ranking comment, P - Type ranking punishment, W - Type ranking reward, J - Type statis, S - システム, G - タグ, O - フッター, A - ヘッダー, T - 件名, R - 転送, U - ユーザーエージェント, V - 音声) 
| datecreated | datetime | メッセージの作成日時 
| message | text | メッセージ本文 

| Example responses 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <groups>
  <group>
   <userid>uid12345</userid>
   <rtype>M</rtype>
   <rstatus>V</rstatus>
   <datecreated>2012-04-03 12:21:21</datecreated>
   <datefinished>2012-04-03 12:31:21</datefinished>
   <messages>
    <message>
     <messageid>mid00003</messageid>
     <userid>uid00001</userid>
     <rtype>M</rtype>
     <datecreated>2012-04-03 12:25:21</datecreated>
     <message>hello, this is example message</message>
    </message>
   </messages>
  </group>
  <group>
   <userid>uid12346</userid>
   <rtype>M</rtype>
   <rstatus>V</rstatus>
   <datecreated>2012-04-03 12:41:21</datecreated>
   <datefinished>2012-04-03 13:21:21</datefinished>
   <messages>
    <message>
     <messageid>mid00004</messageid>
     <userid>uid00001</userid>
     <rtype>M</rtype>
     <datecreated>2012-04-03 18:21:21</datecreated>
     <message>hello, this is example message</message>
    </message>
    <message>
     <messageid>mid00005</messageid>
     <userid>uid00001</userid>
     <rtype>M</rtype>
     <datecreated>2012-04-03 19:21:21</datecreated>
     <message>hello, this is example message</message>
    </message>
   </messages>
  </group>
 </groups>
</response>
 
| 
JSON
 | {
  "response":{
    "groups":[
      {
        "userid":"uid12345",
        "rtype":"M",
        "rstatus":"V",
        "datecreated":"2012-04-03 12:21:21",
        "datefinished":"2012-04-03 12:31:21",
        "messages":[
          {
            "messageid":"mid00003",
            "userid":"uid00001",
            "rtype":"M",
            "datecreated":"2012-04-03 12:25:21",
            "message":"hello, this is example message"
          }
        ]
      },
      {
        "userid":"uid12346",
        "rtype":"M",
        "rstatus":"V",
        "datecreated":"2012-04-03 12:41:21",
        "datefinished":"2012-04-03 13:21:21",
        "messages":[
          {
            "messageid":"mid00004",
            "userid":"uid00001",
            "rtype":"M",
            "datecreated":"2012-04-03 18:21:21",
            "message":"hello, this is example message"
          },
          {
            "messageid":"mid00005",
            "userid":"uid00001",
            "rtype":"M",
            "datecreated":"2012-04-03 19:21:21",
            "message":"hello, this is example message"
          }
        ]
      }
    ]
  }
} 

### §　会話履歴に新しいメッセージを作成する

※ LiveAgent version: 2.8.2.1 以降に対応しています

API の呼び出し例**

POST
  http://example.com/api/conversations/[conversationid]/messages**注: このコールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-%E3%81%AE%E5%88%A9%E7%94%A8%E4%BE%8B-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89#post) の POST メソッドを利用します。

呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [conversationid] | text | 会話履歴 ID、コード、または公開 URL コード 
| message | text | メッセージ本文 (UTF-8 エンコードである必要があります) 
| apikey | text | LiveAgent の API キー 

パラメータのオプション

| パラメータ名 | 形式 | 内容 
| useridentifier | text | エージェントの識別子で、メールアドレスまたはユーザー ID が入ります。空欄の場合 "System" が代わりに入ります。 
| type | constlist | メッセージの形式 (有効値： M - メッセージ, N - ノート) 
| mail_messsage_id | text | メールメッセージの ID。返信時のヘッダにこの ID が含まれている返信メールはすべて、この ID の会話履歴に関連付けられます。 
| do_not_send_mail | constlist | メッセージ作成時に顧客へ送信されるメールを配信無効にします。外部のメール配信システムを利用時に使います。 (有効値： Y - 送信しない, N - 送信する) 
| is_html_message | constlist | メッセージテキストを HTML 形式に変換します。 (有効値： Y - 有効, N - 無効) 

注: "useridentifier" が空欄の場合、メッセージ形式が "M" であってもノートしか作成されません。

出力データの内容****
出力フィールド

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

### § 会話履歴（チケット）を新規作成する

※ LiveAgent version 2.8.2.1 以降に対応しています

API 呼び出し例**

POST
  http://example.com/api/conversations**注: このコールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-%E3%81%AE%E5%88%A9%E7%94%A8%E4%BE%8B-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89#post) の POST メソッドを利用します。

呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| message | text | メッセージ本文 
| useridentifier | text | チケット作成者の識別子。ユーザー ID、または、エージェントまたはコンタクトへ登録済みの顧客のメールアドレスが入ります。 
| department | text | チームの識別子。チーム ID が入ります。(チーム名ではありません)。 
| subject | text | メッセージの件名 
| recipient | text | メッセージの宛先 
| apikey | text | LiveAgent の API キー 

パラメータのオプション

| パラメータ名 | 形式 | 内容 
| recipient_name | text | メッセージ受信者（宛先）の氏名。フォーマットは "名 姓" となります 
| cc | text | その他のメッセージの宛先。カンマで区切って入力します。 
| status | constlist | 作成する会話履歴（チケット）のステータス。未設定の場合 "N- 新規" となります。 (有効値： A - 返信済み, P - 呼び出し, T - チャット, X - 削除された, B - スパム, I - 内部チケット, C - オープン, R - 完了, N - 新規, W - 延期された) 
| mail_messsage_id | text | メールメッセージの ID。返信時のヘッダにこの ID が含まれている返信メールはすべて、この ID の会話履歴に関連付けられます。 
| do_not_send_mail | constlist | メッセージ作成時に顧客へ送信されるメールを配信無効にします。外部のメール配信システムを利用時に使います。 (有効値： Y - 送信しない, N - 送信する) 
| is_html_message | constlist | メッセージテキストを HTML 形式に変換します。 (有効値： Y - 有効, N - 無効) 

出力データの内容****
出力フィールド

| フィールド名 | 形式 | 内容 
| status | text | OK 
| statuscode | int | 実行されたリクエストのステータスコード 
| conversationid | text | 会話履歴（チケット）の ID 
| code | text | 会話履歴のコード 
| publicurlcode | text | 会話の公開 URL コード 

| データ出力例 
| 
XML
 | <?xml version="1.0" encoding="utf-8"?>
<response>
 <status>OK</status>
 <statuscode>0</statuscode>
 <conversationid>cid00001</conversationid>
 <code/>
 <publicurlcode/>
</response>
 
| 
JSON
 | {
  "response":{
    "status":"OK",
    "statuscode":"0",
    "conversationid":"cid00001",
    "code":null,
    "publicurlcode":null
  }
} 

### § 会話履歴（チケット）のステータス変更

LiveAgent version 2.8.2.1 以降に対応しています

API 呼び出し例**

PUT
  http://example.com/api/conversations/[conversationid]/status**注: このコールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-%E3%81%AE%E5%88%A9%E7%94%A8%E4%BE%8B-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89#put) の PUT メソッドを利用します。

呼び出し時に必須のパラメータ

| パラメータ名 | 形式 | 内容 
| [conversationid] | text | 会話履歴（チケット）ID、コード、または公開 URL コード 
| status | constlist | 会話履歴（チケット）のステータス (有効値： A - 返信済み, R - 完了, C - オープン) 
| apikey | text | LiveAgent の API キー 

パラメータのオプション

| パラメータ名 | 形式 | 内容 
| useridentifier | text | エージェント識別子で、メールアドレスまたはユーザー ID が入ります。空欄の場合は "System" が入ります。 
| note | text | ノート 

出力データの内容****
出力フィールド

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

### § 会話履歴（チケット）に付けられたタグを解除する

LiveAgent version 4.0.36.0 以降に対応しています

API 呼び出し例**

DELETE
  http://example.com/api/conversations/[conversationid]/tags?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [conversationid] | text | 会話履歴（チケット）ID、コード、または公開 URL コード 
| apikey | text | LiveAgent の API キー 

出力データの内容****
出力フィールド

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

### § 会話履歴（チケット）に割り当てられたタグのリストを参照する

※LiveAgent version 4.0.30.6 以降に対応します

API 呼び出し例**

GET
  http://example.com/api/conversations/[conversationid]/tags?apikey=[value]
**呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [conversationid] | text | 会話履歴（チケット）ID、コード、または公開 URL コード 
| apikey | text | LiveAgent の API キー 

出力データの内容****
出力フィールド

| フィールド名 | 形式 | 内容 
| tags | list | 割り当てられたタグのリスト 
| "tags" のフィールドには 2種類のカラムがあります 
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

### § 会話履歴（チケット）にタグを割り当てる

※ LiveAgent version 4.0.30.6 以降に対応します

API 呼び出し例**

POST
  http://example.com/api/conversations/[conversationid]/tags**注: このコールでは、[send parameters](http://support.smartweb.jp/liveagent/359468-REST-API-%E3%81%AE%E5%88%A9%E7%94%A8%E4%BE%8B-%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89#post) の POST メソッドを利用します。

呼び出し時の必須パラメータ

| パラメータ名 | 形式 | 内容 
| [conversationid] | text | 会話履歴（チケット）ID、コード、または公開 URL コード 
| apikey | text | LiveAgent の API キー 

パラメータのオプション

| パラメータ名 | 形式 | 内容 
| id | text | タグの識別子 
| name | text | タグの名称 

出力データの内容**

出力フィールド

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