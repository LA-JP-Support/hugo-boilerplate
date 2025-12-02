---
title: 条件付きルーター
translationKey: conditional-router
description: 条件付きルーターはデータをルールに照らして評価し、特定のルートに振り分けます。自動化パイプライン、AIチャットボット、ソフトウェアにおける動的なルールベースの分岐に不可欠です。
keywords:
- 条件付きルーター
- ワークフロー自動化
- ルールベース分岐
- AIチャットボット
- データルーティング
category: General
type: glossary
date: 2025-12-02
draft: false
term: じょうけんつきるーたー
---

## 定義

**条件付きルーター**は、ワークフローコンポーネントまたはノードであり、入力データをユーザー定義の1つ以上のルールと照合し、どの条件が一致するかに基づいて特定の下流ルートにデータを振り分けます。その目的は、自動化パイプライン、AIチャットボット、ビジネスプロセス自動化、ソフトウェアアーキテクチャにおいて、動的でルールベースの分岐を可能にすることです。各出力ポートは、さまざまな演算子を使用したカスタマイズ可能なルールによって決定される、可能なルーティング結果に対応しています。

- **信頼できる情報源:** [AWS Glue 条件付きルーター](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)、[FlowHunt 条件付きルーター](https://www.flowhunt.io/components/ConditionalRouter/)

**主な機能:**
- 入力（テキスト、構造化オブジェクト、メタデータなど）を受け取る
- ユーザー定義の条件（例：`equals`、`contains`、`is_email`、`regex`）を適用する
- 評価ごとに正確に1つの出力（ルート）を有効にする（一部のETLコンテキストを除く、[AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)を参照）
- 複雑な自動化における決定論的で管理可能なフローをサポートする

---

## 条件付きルーターの仕組み

### コアロジック

条件付きルーターは、設定可能な演算子を使用して、入力データを指定された値や論理式と比較します。各条件は名前付き出力にリンクされています。ルーターは条件を順番にチェックし、最初に`true`となる条件が出力ルートを決定します。条件が一致しない場合、ルーターはデフォルトまたはフォールバックルート（設定されている場合）をトリガーします。

- **単一パスルーティング:** 評価ごとに1つの出力のみが有効化される（排他的ルーティング）。ただし、一部のETLフレームワークを除く（[AWS Glue: 複数グループ](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)を参照）。
- **設定可能なルール:** 条件は演算子で定義され、ネストされたデータを含む複数のフィールドを参照できる。
- **拡張可能:** 論理的な構成、ネストされた条件、カスタム式をサポート。

### 評価シーケンス

1. **入力受信:** データとオプションのメタデータまたはパラメータを受信。
2. **条件評価:** 設定された演算子を使用して、定義された各条件を順番に評価。
3. **ルーティング決定:** 最初に`true`と評価される条件が出力を決定。
4. **デフォルト処理:** 条件が一致しない場合、データはデフォルトルート（定義されている場合）に送信される。
5. **下流処理:** データは次のコンポーネントまたはアクションに渡される。

- **実世界の例:** [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)では、ユーザーはフォーム入力やメッセージメタデータに基づいて、コードなしでマルチブランチワークフローを作成できます。

---

## 入力

条件付きルーターの入力パラメータはプラットフォームによって異なる場合がありますが、一般的には以下を含みます：

| 入力名          | 型            | 説明                                                       | 必須 | 高度 |
|----------------|---------------|-----------------------------------------------------------|------|------|
| 入力データ/テキスト | 文字列/オブジェクト | 評価する主要データ（ユーザー入力、APIレスポンスなど）              | はい  | いいえ |
| 一致値          | 文字列/オブジェクト | 比較する値または式                                           | いいえ | いいえ |
| 演算子          | 文字列         | 比較演算子（[利用可能な演算子](#available-operators)を参照）      | はい  | はい  |
| 大文字小文字の区別 | ブール値        | 大文字小文字を区別する比較を有効にする                           | いいえ | はい  |
| メタデータ/パラメータ | オブジェクト    | ルーティング用の追加フィールド（user_plan、region、modelなど）    | いいえ | はい  |
| メッセージオブジェクト | オブジェクト    | ルートに沿って渡すペイロード                                  | いいえ | いいえ |

- **情報源:** [FlowHunt 入力](https://www.flowhunt.io/components/ConditionalRouter/)、[AWS Glue ドキュメント](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- 多くのプラットフォーム（例：[Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter)）は、動的変数を使用したテンプレートベースのルーティングをサポートしています。

---

## 利用可能な演算子

条件付きルーターは、柔軟なルーティングのために様々な演算子をサポートしています：

| 演算子             | 説明                                     | 使用例                                |
|-------------------|----------------------------------------|--------------------------------------|
| `equals` / `$eq`   | 値が一致と等しい                           | `"status" == "active"`              |
| `not equals`/ `$ne`| 値が一致と等しくない                        | `"role" != "admin"`                 |
| `contains`         | 値が部分文字列を含む                        | `"hello@example.com" contains "@"`  |
| `starts with`      | 値が部分文字列で始まる                      | `"prefix"` starts with "pre"        |
| `ends with`        | 値が部分文字列で終わる                      | `"file.pdf"` ends with ".pdf"       |
| `is empty`         | 値が空/null/未定義                        | `""`                                |
| `is not empty`     | 値が空でない                              | `"not empty"`                       |
| `is_url`           | 値がURL形式に一致する                      | `"https://..."`                     |
| `is_email`         | 値がメール形式に一致する                    | `"name@domain.com"`                 |
| `is_number`        | 値が数値                                 | `123`                               |
| `$in`              | 値が配列/リスト内にある                     | `tier in ["pro", "enterprise"]`     |
| `$nin`             | 値が配列/リスト内にない                     | `status not in ["error"]`           |
| `$regex`           | 値が正規表現に一致する                      | `input matches /pattern/`           |
| `$gt`, `$gte`      | より大きい/以上（数値）                     | `score >= 0.8`                      |
| `$lt`, `$lte`      | より小さい/以下（数値）                     | `temperature < 0.7`                 |

- **論理演算子:** `$and`（すべての条件が真である必要がある）、`$or`（いずれかの条件が真）
- **情報源:** [FlowHunt 演算子リスト](https://www.flowhunt.io/components/ConditionalRouter/)、[Portkey 条件付きルーティング](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)、[AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)

---

## 出力

各条件付きルーターノードは複数の出力ポートを提供します：

| 出力名         | トリガー条件                      | 出力データ型        |
|---------------|--------------------------------|-------------------|
| True ルート     | 条件が`true`と評価された場合       | メッセージ/オブジェクト |
| False ルート    | 条件が`false`と評価された場合      | メッセージ/オブジェクト |
| カスタムルート   | 各条件に対する名前付き出力         | メッセージ/オブジェクト |
| デフォルトルート  | 条件が一致しない場合              | メッセージ/オブジェクト |

- **名前付き出力ポート:** 各条件は名前付き出力にリンクされています。
- **デフォルト出力:** 一致しないデータを処理します。
- **データ転送:** 元の（または変換された）メッセージ/データが有効化された出力を通過します。

- **情報源:** [FlowHunt 出力](https://www.flowhunt.io/components/ConditionalRouter/)、[AWS Glue ルーティング](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)

---

## 高度な設定

### 論理演算子

単一ルートに対して複数条件のロジックを定義するには、論理演算子を使用します：

**例 ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing))**
```json
{
  "query": {
    "$and": [
      { "metadata.user_type": { "$eq": "pro" } },
      { "params.model": { "$eq": "gpt-4" } }
    ]
  },
  "then": "pro_gpt4_target"
}
```

- `$and`、`$or`、さらにはネストされた論理ブロックもサポートします。

### 大文字小文字の区別

文字列比較で大文字小文字を区別するかどうかを設定します：

- `case_sensitive: true` で完全一致
- `case_sensitive: false` で大文字小文字を区別しない

### 安全でないテンプレート処理

一部のプラットフォーム（例：[Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter)）では、複雑なオブジェクトを出力に渡すなどの高度なシナリオのために、安全でないテンプレートレンダリングを許可しています。これを有効にするとリモートコード実行などのセキュリティリスクが生じる可能性があるため、注意して使用してください。

---

## 実用的な例

### 例1: 単純なテキスト一致 ([FlowHunt](https://www.flowhunt.io/components/ConditionalRouter/))
ユーザーメッセージに「help」というキーワードが含まれている場合はサポートにルーティングし、それ以外の場合はボットにルーティングします。

```json
{
  "input_text": "I need help with my order",
  "match_text": "help",
  "operator": "contains",
  "case_sensitive": false
}
```

### 例2: パラメータベースのモデル選択 ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing))
`model`パラメータに基づいてリクエストを異なるモデルにルーティングします。

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": { "params.model": { "$eq": "fastest" } },
        "then": "fast-model"
      },
      {
        "query": { "params.model": { "$eq": "smartest" } },
        "then": "smart-model"
      }
    ],
    "default": "balanced-model"
  }
}
```

### 例3: データ検証 ([Haystack](https://docs.haystack.deepset.ai/docs/conditionalrouter))
入力の長さに基づいてルーティングします：

```python
routes = [
  {
    "condition": "{{ query|length > 10 }}",
    "output": ["{{ query }}", "{{ query|length }}"],
    "output_name": ["ok_query", "length"],
    "output_type": [str, int],
  },
  {
    "condition": "{{ query|length <= 10 }}",
    "output": ["query too short: {{ query }}", "{{ query|length }}"],
    "output_name": ["too_short_query", "length"],
    "output_type": [str, int],
  },
]
```

### 例4: メタデータとパラメータを組み合わせたルーティング ([Portkey](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing#combined-routing-with-multiple-conditions))
創造性の高いリクエストを持つエンタープライズユーザーをプレミアムモデルにルーティングします。

```json
{
  "strategy": {
    "mode": "conditional",
    "conditions": [
      {
        "query": {
          "$and": [
            { "metadata.user_tier": { "$eq": "enterprise" } },
            { "params.temperature": { "$gte": 0.7 } }
          ]
        },
        "then": "creative-premium-target"
      }
    ],
    "default": "standard-target"
  }
}
```

### 実世界のワークフロー例

- **Slack:** [サポートリクエストワークフローの自動化](https://slack.com/blog/news/conditional-branching-workflow-builder)では、フォーム入力に基づいてリクエストを異なるチームに振