---
title: JSON Path
translationKey: json-path
description: JSON Pathは、簡潔なパス式を使用して複雑なJSONデータ構造から特定の値を抽出、検索、操作するためのクエリ構文です。
keywords: ["JSON Path", "JSONデータ", "クエリ構文", "データ抽出", "APIテスト"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: ジェイソン パス
reading: JSON Path
kana_head: その他
e-title: JSON Path
---
## JSON Pathとは?

JSON Pathは、JSON(JavaScript Object Notation)ドキュメント内の要素をナビゲート、抽出、評価するために設計されたクエリ言語です。XMLにおけるXPathに相当し、標準化された読みやすい構文を使用してJSON構造の任意の深さから対象データを取得できます。JSON Pathは、プログラミング、自動化、APIテスト、データエンジニアリング、構成管理で広く使用されており、JSONデータを効率的に扱う必要があるすべての人にとって不可欠なツールです。

- **標準化:** JSON PathはIETFの[RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535)で標準化され、JSONPathクエリ式の統一された構文とセマンティクスを提供しています。
- **クロスランゲージサポート:** JSON Pathは多数のプログラミング言語(JavaScript、Python、Java、PHP、SQLデータベースなど)で実装されています。
- **ユースケース:** APIテスト、検証、データ抽出、ETL(抽出、変換、ロード)プロセス、構成管理、チャットボット自動化。

**JSONの例:**
```json
{
  "user": {
    "id": 123,
    "profile": {
      "name": "Alice",
      "roles": ["admin", "editor"]
    }
  }
}
```
**ユーザーIDを抽出:**
```jsonpath
$.user.id
// 出力: 123
```

**参考資料:**  
- [RFC 9535: JSONPath標準](https://datatracker.ietf.org/doc/html/rfc9535)  
- [SmartBear JSONPath構文ドキュメント](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html)  
- [JSONPathオンライン評価ツール](https://jsonpath.com/)

## なぜJSON Pathを使用するのか?

JSON Pathは、深くネストされたJSONドキュメント内のデータの抽出や検証を劇的に簡素化します。以下のことが可能になります:

- ネストの任意の深さでデータを取得する簡潔なクエリを記述できます。
- プロパティ値に基づいて配列やオブジェクトをフィルタリングできます。
- APIレスポンス、構成ファイル、ログ、データベース内のデータを選択、変換、検証できます。
- プログラミング、テスト、分析における反復的なデータ抽出タスクを自動化できます。

**一般的なユースケース:**

- **APIテストと自動化:** REST APIレスポンスの特定フィールドをアサートおよび検証(Postman、Rest-Assuredなど)。
- **データ処理パイプライン:** 分析やETLのためにJSONログやデータレイクから対象データを抽出。
- **データベース統合:** データベース(SQL Server、PostgreSQL、MongoDB)のJSON列をクエリ。
- **構成管理:** JSON構成ファイルの設定を取得または更新。
- **AIチャットボット:** JSON形式の会話でユーザー属性、インテント、メッセージ履歴を解析。

**参考資料:**  
- [ToolsQA: JSONPathとJSONPathを使用したJSONのクエリ](https://toolsqa.com/rest-assured/jsonpath-and-query-json-using-jsonpath/)  
- [Curiosity Software: JSONPathドキュメント](https://knowledge.curiositysoftware.ie/docs/jsonpath-extracting-values-from-json)

## JSON Path構文と演算子

### コア構文要素

JSON Path式は、JSONデータをトラバースおよびフィルタリングするためのセレクタと演算子で構成されます。[SmartBear JSONPath構文ドキュメント](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html)と[RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535)が包括的なリファレンスを提供しています。

#### 1. **ルートオブジェクト(`$`)**
- JSONドキュメントのルートを示します。
- 例: `$.store`はルートの`store`オブジェクトを選択します。

#### 2. **子演算子(`.`と`[]`)**
- ドット記法(`.`): 子プロパティにアクセス(例: `$.user.name`)。
- ブラケット記法(`['property']`): スペース、特殊文字、予約語を含むプロパティ名を処理(例: `$['user']['profile']`)。ブラケットは常にシングルクォートを使用します。

#### 3. **配列アクセス**
- インデックス(`[n]`): n番目(0ベース)の要素を選択(`$.store.book[0]`)。
- 複数インデックス(`[n,m]`): 複数の要素を選択(`$.store.book[0,2]`)。

#### 4. **配列スライス演算子(`[start:end:step]`)**
- 配列要素の範囲を選択(Pythonスタイル)。
- 例: `$.store.book[0:2]`は最初の2冊の本を選択、`$.store.book[::2]`は1つおきの本を選択。

#### 5. **ワイルドカード(`*`)**
- 現在のレベルのすべての要素を選択します。
- 例: `$.store.book[*].author`は本の配列内のすべての著者を取得します。

#### 6. **再帰的降下(`..`)**
- 現在のノード下の任意の深さにあるすべての一致要素を選択します。
- 例: `$..price`はドキュメント内のどこにでもあるすべての`price`フィールドを検索します。

#### 7. **フィルタ式(`[?(...)]`)**
- 条件に基づいて配列要素をフィルタリングします。
- 例: `$.store.book[?(@.price < 10)]`は価格が10未満の本を選択します。
- `@`は現在の要素を参照し、`$`はドキュメントルートを参照します。

#### 8. **スクリプト式**
- 一部の実装では`length`、`max`、`min`などの関数をサポート(RFC標準の一部ではありません)。
- 例: `$.store.book[?(@.author =~ /Evelyn.*/)]`は「Evelyn」で始まる著者を選択します。

#### 9. **ユニオン演算子(`[,]`)**
- 複数のプロパティまたは配列インデックスのユニオンを選択します。
- 例: `$.store.book[0,1]`は最初と2番目の本を選択します。

#### 10. **現在のオブジェクト(`@`)**
- フィルタ内で現在のアイテムを参照するために使用されます。
- 例: `$.store.book[?(@.category == 'fiction')]`

#### 11. **大文字小文字の区別**
- JSON Pathはプロパティ名と値で大文字小文字を区別します。

**参考資料:** [RFC 9535構文と例](https://datatracker.ietf.org/doc/html/rfc9535#section-2)

## JSON Path構文チートシート

| 演算子             | 説明                                          | 例                                     |
|--------------------|----------------------------------------------|----------------------------------------|
| `$`                | ルートオブジェクト                            | `$.store`                              |
| `.` / `['name']`   | 子/プロパティアクセス                         | `$.user.name`, `$['user']['profile']`  |
| `[*]`              | ワイルドカード(すべての要素)                  | `$.company.employees[*].name`          |
| `..`               | 再帰的降下(すべての子孫)                      | `$..price`                             |
| `[n]`              | 配列インデックスアクセス                      | `$.books[0]`                           |
| `[n,m]`            | 複数インデックス(ユニオン)                    | `$.books[0,2]`                         |
| `[start:end:step]` | 配列スライス演算子                            | `$.books[1:3]`                         |
| `[?()]`            | フィルタ式                                    | `$.books[?(@.price < 10)]`             |
| `@`                | フィルタ内の現在のオブジェクト                | `@.price > 20`                         |
| `*`                | ワイルドカード(このレベルのすべてのキーまたは値) | `$.store.*`                            |

**参考資料:**  
- [JSONPath構文 | SmartBear](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html#jsonpath-notation)

## 実用例

**サンプルJSON:**
```json
{
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      {
        "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      {
        "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  },
  "expensive": 10
}
```

### クエリ例

1. **すべての本のタイトルを取得**
   ```jsonpath
   $.store.book[*].title
   // 出力: ["Sayings of the Century", "Sword of Honour", "Moby Dick", "The Lord of the Rings"]
   ```

2. **フィクション本のすべての著者を取得**
   ```jsonpath
   $.store.book[?(@.category == 'fiction')].author
   // 出力: ["Evelyn Waugh", "Herman Melville", "J. R. R. Tolkien"]
   ```

3. **価格が10未満のすべての本を検索**
   ```jsonpath
   $.store.book[?(@.price < 10)]
   // 出力: [ ... 2つの本オブジェクト ... ]
   ```

4. **店舗内のすべての価格を取得(本と自転車)**
   ```jsonpath
   $.store..price
   // 出力: [8.95, 12.99, 8.99, 22.99, 19.95]
   ```

5. **配列の最後の本を選択**
   ```jsonpath
   $.store.book[-1]
   // 出力: { ... トールキンの本 ... }
   ```

6. **最初の2冊の本のタイトルを取得**
   ```jsonpath
   $.store.book[0:2].title
   // 出力: ["Sayings of the Century", "Sword of Honour"]
   ```

7. **店舗内のすべてのISBN番号を取得**
   ```jsonpath
   $.store.book[*].isbn
   // 出力: ["0-553-21311-3", "0-395-19395-8"]
   ```

8. **ワイルドカードを使用して店舗内のすべてのアイテムを取得(本と自転車)**
   ```jsonpath
   $.store.*
   // 出力: [本の配列, 自転車オブジェクト]
   ```

9. **再帰的降下でどこにでもあるすべての価格を取得**
   ```jsonpath
   $..price
   // 出力: [8.95, 12.99, 8.99, 22.99, 19.95, 10]
   ```

**参考資料:**  
- [SmartBear JSONPath構文: 例](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html#examples)

## JSON Path演算子とフィルタ(上級)

### サポートされている演算子([SmartBearドキュメント](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html#filters))

| 演算子 | 説明                                 | 例                                              |
|----------|-------------------------------------|------------------------------------------------------|
| `==`     | 等しい                               | `[?(@.color=='red')]`                                |
| `!=`     | 等しくない                           | `[?(@.color!='red')]`                                |
| `>`      | より大きい                           | `[?(@.price>10)]`                                    |
| `>=`     | 以上                                 | `[?(@.price>=10)]`                                   |
| `<`      | より小さい                           | `[?(@.price<10)]`                                    |
| `<=`     | 以下                                 | `[?(@.price<=10)]`                                   |
| `=~`     | 正規表現マッチ(実装依存)             | `[?(@.author =~ /Evelyn.*/)]`                        |
| `&&`     | 論理AND                              | `[?(@.category=='fiction' && @.price < 10)]`         |
| `||`     | 論理OR                               | `[?(@.category=='fiction' || @.price < 10)]`         |
| `in`     | 値が配列内にある                     | `[?(@.size in ['M','L'])]` (SmartBear TestEngine)    |
| `nin`    | 値が配列内にない                     | `[?(@.size nin ['M','L'])]` (SmartBear TestEngine)   |
| `subsetof` | 配列が別の配列のサブセット         | `[?(@.sizes subsetof ['M','L'])]` (TestEngineのみ)  |
| `contains` | 文字列または配列が値を含む         | `[?(@.name contains 'Alex')]` (TestEngineのみ)      |
| `size`   | 配列または文字列が特定の長さを持つ   | `[?(@.name size 4)]` (TestEngineのみ)               |
| `empty true/false` | 空/非空である            | `[?(@.name empty true)]` (TestEngineのみ)           |

**注意:** 演算子のサポートはライブラリによって異なる場合があります。標準化については[RFC 9535セクション2.3.5](https://datatracker.ietf.org/doc/html/rfc9535#section-2.3.5)を参照してください。

## JSON Pathの実践的な使用方法

### 1. API自動化とテスト

- [Postman](https://learning.postman.com/docs/writing-scripts/script-references/variables-list/)、[Rest-Assured](https://toolsqa.com/rest-assured/jsonpath-and-query-json-using-jsonpath/)、[SoapUI](https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html)などのツールでJSONPathを使用して**APIレスポンスを検証**。
- **例:** 返されたユーザーのメールが期待値と一致することをアサート:
  ```javascript
  // Postman
  pm.expect(pm.response.json().user.email).to.eql("test@example.com");
  // JSONPathを使用
  const email = jsonpath.query(response, '$.user.email')[0];
  ```

### 2. データ変換とETL

- [jsonpath-ng](https://github.com/h2non/jsonpath-ng)(Python)などのライブラリを使用して、分析用にJSONログやファイルからネストされた属性を抽出。
  ```python
  from jsonpath_ng import parse
  errors = [match.value for match in parse('$..errors[*].message').find(log_data)]
  ```

### 3. データベースクエリ

- JSONPathを使用してSQL ServerまたはPostgreSQLのJSON列をクエリ。
  - **SQL Server:** [SQL ServerのJSON Path式](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-path-expressions-sql-server?view=sql-server-ver17)
  - **例:**
    ```sql
    SELECT *
    FROM OPENJSON(@json, '$.store.book[?(@.price < 10)]')
    ```

### 4. AIチャットボットと自動化

- JSON形式のチャットログでユーザー属性、インテント、会話履歴を解析。
  ```jsonpath
  $.conversation[*].user_message
  ```

### 5. 構成管理

- JSONPath更新メソッドを使用してJSONファイルの構成値を動的に更新または読み取り。
  ```javascript
  jsonpath.value(config, '$.env.mode', 'production');
  ```

**参考資料:**  
- [JavaScriptのJSONPath: dchester/jsonpath](https://github.com/dchester/jsonpath)  
- [Python: h2non/jsonpath-ng](https://github.com/h2non/jsonpath-ng)  
- [Java: json-path/JsonPath](https://github.com/json-path/JsonPath)  
- [PHP: Flow-Communications/JSONPath](https://github.com/Flow-Communications/JSONPath)

## XPathとの比較

| 機能         | JSON Path           | XPath         |
|-----------------|--------------------|--------------|
| データ形式     | JSON               | XML          |
| 構文          | パスライク、`$..`   | パスライク、`//`、`/` |
| フィルタ         | `[?(条件)]`   | `[条件]`|
| 再帰       | `..`               | `//`         |
| 標準化?   | はい(RFC 9535)     | はい          |
| 親/兄弟  | サポートされていない      | サポートされている    |

- JSON PathはJSON用、XPathはXML用です。
- JSON PathにはXPathにある親/兄弟ナビゲーションがありません。

**参考資料:**  
- [RFC 9535 - JSONPath標準](https://datatracker.ietf.org/doc/html/rfc9535)

## コード内のJSON Path: 多言語例

### JavaScript (Node.js)
- [jsonpath](https://github.com/dchester/jsonpath)
```javascript
const jsonpath = require('jsonpath');
const data = require('./data.json');

// すべての本のタイトルを取得
const titles = jsonpath.query(data, '$.store.book[*].title');
console.log(titles);

// 10未満の本をフィルタ
const cheapBooks = jsonpath.query(data, '$.store.book[?(@.price < 10)]');
console.log(cheapBooks);
```

### Python
- [jsonpath-ng](https://github.com/h2non/jsonpath-ng)
```python
import json
from jsonpath_ng import parse

with open('data.json') as file:
    data = json.load(file)

titles = [match.value for match in parse('$.store.book[*].title').find(data)]
print(titles)
```

### Java
- [JsonPath](https://github.com/json-path/JsonPath)
```java
import com.jayway.jsonpath.JsonPath;

String json = new String(Files.readAllBytes(Paths.get("data.json")));
DocumentContext ctx = JsonPath.parse(json);

List<String> titles = ctx.read("$.store.book[*].title");
```

### PHP
- [Flow\JSONPath](https://github.com/Flow-Communications/JSONPath)
```php
use Flow\JSONPath\JSONPath;

$data = json_decode(file_get_contents('data.json'), true);

$titles = (new JSONPath($data))->find('$.store.book[*].title');
print_r($titles->data());
```

## ベストプラクティスとヒント

- **厳密モードと緩和モード:** 一部の実装(SQL Serverなど)は、欠落パスのエラー処理のために厳密/緩和モードを提供します。
- **ブラケット記法:** スペースや特殊文字を含むプロパティ名には常にブラケット記法を使用してください。