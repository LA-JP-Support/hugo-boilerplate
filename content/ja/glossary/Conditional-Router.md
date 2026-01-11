---
title: コンディショナルルーター
lastmod: '2025-12-19'
translationKey: conditional-router
description: コンディショナルルーターは、データをルールに照らして評価し、特定のルートに振り分けます。自動化パイプライン、AIチャットボット、ソフトウェアにおける動的でルールベースの分岐処理に不可欠です。
keywords:
- コンディショナルルーター
- ワークフロー自動化
- ルールベース分岐
- AIチャットボット
- データルーティング
category: General
type: glossary
date: '2025-12-19'
draft: false
e-title: Conditional Router
term: こんでぃしょなるるーたー
url: "/ja/glossary/conditional-router/"
aliases:
- "/ja/glossary/Conditional-Router/"
---
## Conditional Routerとは?
Conditional Router(条件付きルーター)は、受信データを1つ以上のユーザー定義ルールに対して評価し、一致する条件に基づいて特定の下流ルートにデータを振り分けるワークフローコンポーネントまたはノードです。その目的は、自動化パイプライン、AIチャットボット、ビジネスプロセス自動化、ソフトウェアアーキテクチャにおいて、動的でルールベースの分岐を可能にすることです。各出力ポートは、さまざまな演算子を使用したカスタマイズ可能なルールによって決定される、ルーティング結果の可能性に対応しています。

**主な機能:**
- 入力(テキスト、構造化オブジェクト、メタデータなど)を受信
- ユーザー定義の条件を適用(例:`equals`、`contains`、`is_email`、`regex`)
- 評価ごとに正確に1つの出力(ルート)を有効化(一部のETLコンテキストを除く)
- 複雑な自動化における決定論的で管理可能なフローをサポート

## Conditional Routerの動作原理

### コアロジック

Conditional Routerは、設定可能な演算子のセットを使用して、受信データを指定された値または論理式と比較します。各条件は名前付き出力にリンクされています。ルーターは条件を順番にチェックし、最初に`true`となった条件が出力ルートを決定します。どの条件にも一致しない場合、ルーターはデフォルトまたはフォールバックルート(設定されている場合)をトリガーします。

**単一パスルーティング:** 評価ごとに1つの出力のみが有効化されます(排他的ルーティング)。ただし、一部のETLフレームワークでは例外があります。

**設定可能なルール:** 条件は演算子で定義され、ネストされたデータを含む複数のフィールドを参照できます。

**拡張可能:** 論理的な組み合わせ、ネストされた条件、カスタム式をサポートします。

### 評価シーケンス

1. **入力受信:** データと、オプションのメタデータまたはパラメータを受信
2. **条件評価:** 設定された演算子を使用して、定義された各条件を順次評価
3. **ルーティング決定:** `true`と評価された最初の条件が出力を決定
4. **デフォルト処理:** どの条件にも一致しない場合、データはデフォルトルート(定義されている場合)に送信
5. **下流処理:** データは次のコンポーネントまたはアクションに渡される

## 入力

Conditional Routerの入力パラメータはプラットフォームによって異なる場合がありますが、通常は以下を含みます:

| 入力名 | 型 | 説明 | 必須 |
|-----------|------|-------------|----------|
| Input Data/Text | String/Object | 評価する主要データ | はい |
| Match Value | String/Object | 比較対象の値または式 | いいえ |
| Operator | String | 比較演算子 | はい |
| Case Sensitive | Boolean | 大文字小文字を区別する比較を有効化 | いいえ |
| Metadata/Params | Object | ルーティング用の追加フィールド | いいえ |
| Message Object | Object | ルートに沿って渡すペイロード | いいえ |

## 利用可能な演算子

Conditional Routerは、柔軟なルーティングのために多様な演算子をサポートしています:

| 演算子 | 説明 | 使用例 |
|----------|-------------|---------------|
| `equals` / `$eq` | 値が一致と等しい | `"status" == "active"` |
| `not equals`/ `$ne` | 値が一致と等しくない | `"role" != "admin"` |
| `contains` | 値が部分文字列を含む | `"hello@example.com" contains "@"` |
| `starts with` | 値が部分文字列で始まる | `"prefix"` starts with "pre" |
| `ends with` | 値が部分文字列で終わる | `"file.pdf"` ends with ".pdf" |
| `is empty` | 値が空/null/未定義 | `""` |
| `is not empty` | 値が空でない | `"not empty"` |
| `is_url` | 値がURL形式に一致 | `"https://..."` |
| `is_email` | 値がメール形式に一致 | `"name@domain.com"` |
| `is_number` | 値が数値 | `123` |
| `$in` | 値が配列/リストに含まれる | `tier in ["pro", "enterprise"]` |
| `$nin` | 値が配列/リストに含まれない | `status not in ["error"]` |
| `$regex` | 値が正規表現に一致 | `input matches /pattern/` |
| `$gt`, `$gte` | より大きい / 以上 | `score >= 0.8` |
| `$lt`, `$lte` | より小さい / 以下 | `temperature < 0.7` |

**論理演算子:** `$and`(すべての条件が真である必要がある)、`$or`(いずれかの条件が真)

## 出力

各Conditional Routerノードは複数の出力ポートを提供します:

| 出力名 | トリガー条件 | 出力データ型 |
|-------------|-------------------|------------------|
| True Route | 条件が`true`と評価されたとき | Message/Object |
| False Route | 条件が`false`と評価されたとき | Message/Object |
| Custom Routes | 各条件の名前付き出力 | Message/Object |
| Default Route | どの条件にも一致しないとき | Message/Object |

**名前付き出力ポート:** 各条件は名前付き出力にリンクされます。  
**デフォルト出力:** 一致しないデータを処理します。  
**データ転送:** 元の(または変換された)メッセージ/データは、有効化された出力を通じて渡されます。

## 高度な設定

### 論理演算子

単一ルートの複数条件ロジックを定義するには、論理演算子を使用します:

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

`$and`、`$or`、さらにネストされた論理ブロックをサポートします。

### 大文字小文字の区別

文字列比較で大文字小文字を区別するかどうかを設定します:
- `case_sensitive: true` 完全一致の場合
- `case_sensitive: false` 大文字小文字を区別しない場合

## 実用例

### 例1: シンプルなテキストマッチ
ユーザーメッセージにキーワード「help」が含まれている場合はサポートにルーティングし、それ以外はボットにルーティングします。

```json
{
  "input_text": "I need help with my order",
  "match_text": "help",
  "operator": "contains",
  "case_sensitive": false
}
```

### 例2: パラメータベースのモデル選択
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

### 例3: データ検証
入力の長さに基づいてルーティングします:

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

### 例4: メタデータとパラメータの組み合わせルーティング
高い創造性リクエストを持つエンタープライズユーザーをプレミアムモデルにルーティングします。

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

## 典型的なユースケース

### 1. 分岐ロジック
インテント、コンテンツ、または属性に基づいて、ユーザーを異なるダイアログまたはプロセスパスに誘導します。イベントまたはメッセージデータに応じて分岐する自動化ワークフローを調整します。

### 2. 検証とフィルタリング
入力検証を実施します(例:必須フィールド、正しい形式)。スパムや不適切なコンテンツを検出してフィルタリングします。

### 3. パーソナライゼーションとユーザーセグメンテーション
プレミアムユーザーと無料ユーザーを異なるフローにルーティングします。ユーザーを実験的な分岐に割り当てることでA/Bテストを実装します。

### 4. モデル選択と機能フラグ
ユーザーセグメントまたはリクエストプロパティに基づいてAIモデルを動的に選択します。設定フラグを使用して機能を有効/無効にします。

### 5. アクセス制御とコンプライアンス
規制コンプライアンスのために地域に基づいたデータルーティングを確保します。メタデータを使用してロールベースのアクセス制限を適用します。

## ベストプラクティス

**条件の順序**  
早期の一致を防ぐために、汎用的な条件の前に具体的な条件を配置します。

**フェイルセーフデフォルト**  
一致しないデータのために常にデフォルト出力を設定します。

**テスト**  
テストデータでロジックを検証して正しいルーティングを確保し、ログと分析を使用してルーティング決定を監視します。

**ドキュメント**  
保守性のために複雑な条件にコメントまたはドキュメントを付けます。

**セキュリティ**  
必須でない限り、また入力が信頼できる場合を除き、安全でないテンプレート評価を避けます。

**パフォーマンス**  
ルーティングを高速で保守可能に保つために、過度なネストや極端に複雑な条件を避けます。

**ノーコードアクセシビリティ**  
より広いアクセシビリティのために、グラフィカルまたはノーコードインターフェースを提供するプラットフォームを使用します。

## トラブルシューティングとFAQ

**Q: 複数の条件が一致した場合はどうなりますか?**  
A: (順序で)最初に一致した条件のみが選択されます。後続の一致は無視されます。一部のETLツールでは、データを複数の出力にルーティングできます。

**Q: 複数のフィールドに基づいてルーティングするにはどうすればよいですか?**  
A: 論理演算子(`$and`、`$or`)を使用して、複数のフィールドの条件を組み合わせます。

**Q: 参照されたフィールドが存在しない場合はどうなりますか?**  
A: 通常、条件は`false`と評価され、ルーターは次の条件またはデフォルトに進みます。

**Q: 正規表現や高度なマッチングを使用できますか?**  
A: はい、多くのルーターは`$regex`またはパターンベースの演算子をサポートしています。

**Q: これは非開発者に適していますか?**  
A: 多くのプラットフォームはノーコード設定を提供しています。

**Q: 並列ルーティングを実行できますか?**  
A: ほとんどのルーターは排他的(評価ごとに単一パス)です。並列アクションの場合は、専用のマルチルートまたは分岐コンポーネントを使用します。

## 参考文献

- [AWS Glue: Conditional Router](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html)
- [FlowHunt: Conditional Router](https://www.flowhunt.io/components/ConditionalRouter/)
- [Haystack: ConditionalRouter](https://docs.haystack.deepset.ai/docs/conditionalrouter)
- [Portkey AI: Conditional Routing](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing)
- [Portkey AI: Combined Routing with Multiple Conditions](https://docs.portkey.ai/docs/product/ai-gateway/conditional-routing#combined-routing-with-multiple-conditions)
- [Fluix: Conditional Logic Tutorial](https://fluix.io/help/conditional-logic-tutorial)
- [Slack: Conditional Branching Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [Slack: Guide to Slack Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Frontline AI: Understanding Conditional Routing in AI Agent Flows](https://help.getfrontline.ai/en/articles/10174140-understanding-conditional-routing-in-ai-agent-flows)
- [Rapidomize: Conditional Routing](https://rapidomize.com/docs/services/router/)
- [FlowHunt: Live Demo](https://www.flowhunt.io/demo/)
- [Conditional Routing in Slack Workflow Builder (YouTube)](https://www.youtube.com/watch?v=3O4c7iYhD5Y)
- [How to Use Conditional Router in FlowHunt (YouTube)](https://www.youtube.com/watch?v=rgqX7Qj3QAo)
- [AWS Glue Conditional Router Tutorial (YouTube)](https://www.youtube.com/watch?v=90p4Vq8F9pQ)
