---
title: JSON Path
translationKey: json-path
description: JSON Pathは、簡潔なパス式を使用して複雑なJSONデータ構造から特定の値を抽出、検索、操作するためのクエリ構文です。
keywords:
- JSON Path
- JSONデータ
- クエリ構文
- データ抽出
- APIテスト
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: JSON Path
term: ジェイソン パス
url: "/ja/glossary/JSON-Path/"
---
## JSON Pathとは?

JSON Pathは、JSONドキュメント内の要素をナビゲート、抽出、評価するために設計されたクエリ言語です。XMLにおけるXPathに類似しており、JSON Pathは標準化された読みやすい構文を使用して、JSON構造の任意の深さから対象データを取得することを可能にします。この言語は、プログラミング、自動化、APIテスト、データエンジニアリング、構成管理において広く使用されています。

JSON PathはIETFによってRFC 9535で標準化され、クエリ式の統一された構文とセマンティクスを提供しています。この言語は、JavaScript、Python、Java、PHP、SQLデータベースなど、多数のプログラミング環境で実装されています。一般的な用途には、APIテストと検証、ETLプロセス、データベースのJSON列クエリ、構成管理、チャットボットのデータ解析などがあります。

<strong>クエリの例:</strong>```json
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

ユーザーIDを抽出:
```jsonpath
$.user.id
// 出力: 123
```

JSON Pathは、深くネストされたドキュメント内のデータの抽出や検証を劇的に簡素化します。任意のネスト深度での簡潔なクエリを可能にし、プロパティ値に基づいて配列やオブジェクトをフィルタリングし、APIレスポンスや構成ファイル内のデータを選択・変換し、プログラミングやテストにおける反復的な抽出タスクを自動化します。

## コア構文要素

### ルートとパス演算子

**ルートオブジェクト (`$`)**JSONドキュメントのルートを示します。すべてのパスは`$`で始まります。

**子要素へのアクセス**- ドット記法: `$.user.name` (単純なプロパティ)
- ブラケット記法: `$['user']['profile']` (特殊文字、スペース、予約語)
- ブラケットは常にシングルクォートを使用

**配列へのアクセス**- インデックス: `$.store.book[0]` (0ベースのインデックス)
- 複数のインデックス: `$.store.book[0,2]` (要素の結合)
- 負のインデックス: `$.store.book[-1]` (最後の要素)

**配列のスライス**Pythonスタイルのスライス: `[start:end:step]`
- `$.store.book[0:2]` (最初の2冊)
- `$.store.book[::2]` (1つおきの本)
- `$.store.book[1:]` (最初以外のすべて)

**ワイルドカードと再帰**- `*`: 現在のレベルのすべての要素 (`$.store.book[*].author`)
- `..`: 再帰的降下、任意の深さですべての一致を検索 (`$..price`)

### フィルタ式

**基本フィルタ**構文: `[?(condition)]` ここで`@`は現在の要素を参照

```jsonpath
$.store.book[?(@.price < 10)]        // 10ドル未満の本
$.store.book[?(@.category == 'fiction')]  // フィクションの本
```

**比較演算子**- `==`, `!=`: 等価比較
- `>`, `>=`, `<`, `<=`: 数値比較
- `=~`: 正規表現マッチ (実装依存)

**論理演算子**- `&&`: 論理AND
- `||`: 論理OR

```jsonpath
$.store.book[?(@.category=='fiction' && @.price < 10)]
```

**高度な演算子 (実装固有)**- `in`, `nin`: 配列メンバーシップ
- `subsetof`: 配列サブセットチェック
- `contains`: 文字列/配列の包含
- `size`: 長さチェック
- `empty`: 空/非空のテスト

### 結合と参照

**結合演算子**複数のプロパティやインデックスを選択: `[,]`

```jsonpath
$.store.book[0,1]  // 最初の2冊
$['name','age']    // 複数のプロパティ
```

**現在のオブジェクト**フィルタ内では、`@`はテスト中の現在のアイテムを参照します。

## 構文クイックリファレンス

| 演算子 | 説明 | 例 |
|----------|-------------|---------|
| `$` | ルートオブジェクト | `$.store` |
| `.property` | 子要素アクセス | `$.user.name` |
| `['property']` | ブラケットアクセス | `$['user']['profile']` |
| `[n]` | 配列インデックス | `$.books[0]` |
| `[n,m]` | 複数のインデックス | `$.books[0,2]` |
| `[start:end:step]` | 配列スライス | `$.books[1:3]` |
| `[*]` | すべての要素 | `$.store.book[*].title` |
| `..` | 再帰的降下 | `$..price` |
| `[?()]` | フィルタ式 | `$.books[?(@.price < 10)]` |
| `@` | 現在のオブジェクト | `@.price > 20` |

## 実用例

デモンストレーション用のサンプルJSON:

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
  }
}
```

### 一般的なクエリパターン

**すべての本のタイトル:**```jsonpath
$.store.book[*].title
// ["Sayings of the Century", "Sword of Honour", "Moby Dick", "The Lord of the Rings"]
```

<strong>フィクションの著者:</strong>```jsonpath
$.store.book[?(@.category == 'fiction')].author
// ["Evelyn Waugh", "Herman Melville", "J. R. R. Tolkien"]
```

**10ドル未満の本:**```jsonpath
$.store.book[?(@.price < 10)]
// 2つの本オブジェクトを返す
```

<strong>すべての価格 (再帰的):</strong>```jsonpath
$..price
// [8.95, 12.99, 8.99, 22.99, 19.95]
```

**最初の2冊の本のタイトル:**```jsonpath
$.store.book[0:2].title
// ["Sayings of the Century", "Sword of Honour"]
```

<strong>すべてのISBN番号:</strong>```jsonpath
$.store.book[*].isbn
// ["0-553-21311-3", "0-395-19395-8"]
```

## 高度なフィルタ演算子

| 演算子 | 説明 | 例 |
|----------|-------------|---------|
| `==` | 等しい | `[?(@.color=='red')]` |
| `!=` | 等しくない | `[?(@.color!='red')]` |
| `>` | より大きい | `[?(@.price>10)]` |
| `<` | より小さい | `[?(@.price<10)]` |
| `>=` | 以上 | `[?(@.price>=10)]` |
| `<=` | 以下 | `[?(@.price<=10)]` |
| `=~` | 正規表現マッチ | `[?(@.author =~ /Evelyn.*/)]` |
| `&&` | 論理AND | `[?(@.category=='fiction' && @.price < 10)]` |
| `||` | 論理OR | `[?(@.category=='fiction' || @.price < 10)]` |
| `in` | 配列内 | `[?(@.size in ['M','L'])]` |
| `nin` | 配列外 | `[?(@.size nin ['M','L'])]` |
| `contains` | 文字列/配列を含む | `[?(@.name contains 'Alex')]` |
| `size` | 長さチェック | `[?(@.name size 4)]` |
| `empty` | 空チェック | `[?(@.name empty true)]` |

注: 演算子のサポートは実装によって異なります。RFC 9535はコア演算子を定義していますが、拡張演算子はライブラリ固有の場合があります。

## 主要言語での実装

### JavaScript (Node.js)

**ライブラリ:**jsonpath

```javascript
const jsonpath = require('jsonpath');
const data = require('./data.json');

// すべての本のタイトルを取得
const titles = jsonpath.query(data, '$.store.book[*].title');

// 10ドル未満の本をフィルタ
const cheapBooks = jsonpath.query(data, '$.store.book[?(@.price < 10)]');

// 値を更新
jsonpath.value(data, '$.store.bicycle.price', 25.00);
```

### Python

**ライブラリ:**jsonpath-ng

```python
import json
from jsonpath_ng import parse

with open('data.json') as f:
    data = json.load(f)

# タイトルを抽出
expression = parse('$.store.book[*].title')
titles = [match.value for match in expression.find(data)]

# フィルタ付きで抽出
expression = parse('$.store.book[?(@.price < 10)]')
cheap_books = [match.value for match in expression.find(data)]
```

### Java

**ライブラリ:**JsonPath (Jayway)

```java
import com.jayway.jsonpath.JsonPath;

String json = Files.readString(Paths.get("data.json"));
DocumentContext ctx = JsonPath.parse(json);

// タイトルを読み取り
List<String> titles = ctx.read("$.store.book[*].title");

// フィルタ付きで読み取り
List<Map<String, Object>> cheapBooks = 
    ctx.read("$.store.book[?(@.price < 10)]");
```

### PHP

**ライブラリ:**Flow\JSONPath

```php
use Flow\JSONPath\JSONPath;

$data = json_decode(file_get_contents('data.json'), true);

// タイトルを検索
$titles = (new JSONPath($data))->find('$.store.book[*].title');

// フィルタ付きで検索
$cheapBooks = (new JSONPath($data))
    ->find('$.store.book[?(@.price < 10)]');
```

### SQL Server

**ネイティブJSON Pathサポート:**```sql
-- JSON列をクエリ
SELECT *
FROM Products
WHERE JSON_VALUE(Details, '$.category') = 'fiction';

-- 配列要素を抽出
SELECT value
FROM OPENJSON(@json, '$.store.book')
WHERE JSON_VALUE(value, '$.price') < 10;
```

## 一般的な使用例

### APIテストと自動化

<strong>Postmanの例:</strong>```javascript
// レスポンスに期待値が含まれることをテスト
pm.test("User email is correct", function() {
    const email = jsonpath.query(pm.response.json(), '$.user.email')[0];
    pm.expect(email).to.eql("test@example.com");
});
```

**Rest-Assured (Java):**```java
given()
    .when().get("/api/users")
    .then()
    .body("users[0].email", equalTo("test@example.com"));
```

### データ変換 (ETL)

<strong>ログからエラーを抽出:</strong>```python
from jsonpath_ng import parse

errors = [match.value 
          for match in parse('$..errors[*].message').find(log_data)]
```

### データベースJSONクエリ

**PostgreSQL:**```sql
SELECT data->>'name' as name
FROM users
WHERE data @> '{"active": true}';
```

### 構成管理

<strong>構成値を更新:</strong>```javascript
const config = require('./config.json');
jsonpath.value(config, '$.database.port', 5432);
fs.writeFileSync('config.json', JSON.stringify(config, null, 2));
```

### チャットボットのデータ解析

**ユーザーメッセージを抽出:**```jsonpath
$.conversation[*].user_message
```

<strong>インテントでフィルタ:</strong>```jsonpath
$.messages[?(@.intent == 'purchase')].text
```

## JSON Path vs XPath

| 機能 | JSON Path | XPath |
|---------|-----------|-------|
| データ形式 | JSON | XML |
| ルート記法 | `$` | `/` |
| 再帰的降下 | `..` | `//` |
| フィルタ構文 | `[?(condition)]` | `[condition]` |
| 標準化 | あり (RFC 9535) | あり (W3C) |
| 親/兄弟 | サポートなし | サポートあり |
| 軸 | 限定的 | 包括的 |

**主な違い:**- JSON PathはJSONのよりシンプルな構造専用に設計
- XPathはより複雑なナビゲーション(祖先、兄弟)を提供
- JSON Pathは前方トラバーサルに焦点
- 両方とも類似のフィルタと述語の概念を使用

## ベストプラクティス

**パフォーマンス最適化:**- 可能な限り再帰的降下よりも特定のパスを使用
- パフォーマンスクリティカルなコードではコンパイル済み式をキャッシュ
- 大規模データセットでの繰り返しクエリにはインデックス作成を検討

**エラー処理:**- クエリ前に常にJSONを検証
- strict/laxモードを適切に使用 (SQL Server)
- 空の結果を適切に処理
- 解析例外をキャッチ

**コード構成:**- 複雑なパスを定数として保存
- パスのセマンティクスを文書化
- 結果に意味のある変数名を使用
- サンプルデータでパスをテスト

**セキュリティ上の考慮事項:**- ユーザー提供のパスを検証およびサニタイズ
- 内部データ構造の露出を避ける
- 適切なアクセス制御を使用
- 疑わしいクエリパターンをログ記録

## 参考資料


1. IETF. (2023). RFC 9535: JSONPath仕様. IETF RFC.

2. SmartBear. (n.d.). JSONPath構文ドキュメント. SmartBear Support Documentation.

3. Microsoft. (n.d.). SQL ServerのJSON Path式. Microsoft Learn.

4. Postman. (n.d.). JSONPath変数. Postman Learning Center.

5. ToolsQA. (n.d.). REST-Assured JSONPath. ToolsQA Tutorial.

6. jsonpath. JavaScript Library. URL: https://github.com/dchester/jsonpath

7. jsonpath-ng. Python Library. URL: https://github.com/h2non/jsonpath-ng

8. JsonPath. Java Library. URL: https://github.com/json-path/JsonPath

9. Flow\JSONPath. PHP Library. URL: https://github.com/Flow-Communications/JSONPath
