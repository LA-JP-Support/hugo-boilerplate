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
url: "/ja/glossary/Conditional-Router/"
---
## Conditional Routerとは?
Conditional Router(条件付きルーター)は、受信データを1つ以上のユーザー定義ルールに対して評価し、一致する条件に基づいて特定の下流ルートにデータを振り分けるワークフローコンポーネントまたはノードです。その目的は、自動化パイプライン、AIチャットボット、ビジネスプロセス自動化、ソフトウェアアーキテクチャにおいて、動的でルールベースの分岐を可能にすることです。各出力ポートは、さまざまな演算子を使用したカスタマイズ可能なルールによって決定される、ルーティング結果の可能性に対応しています。

<strong>主な機能:</strong>- 入力(テキスト、構造化オブジェクト、メタデータなど)を受信
- ユーザー定義の条件を適用(例:`equals`、`contains`、`is_email`、`regex`)
- 評価ごとに正確に1つの出力(ルート)を有効化(一部のETLコンテキストを除く)
- 複雑な自動化における決定論的で管理可能なフローをサポート

## Conditional Routerの動作原理

### コアロジック

Conditional Routerは、設定可能な演算子のセットを使用して、受信データを指定された値または論理式と比較します。各条件は名前付き出力にリンクされています。ルーターは条件を順番にチェックし、最初に`true`となった条件が出力ルートを決定します。どの条件にも一致しない場合、ルーターはデフォルトまたはフォールバックルート(設定されている場合)をトリガーします。

<strong>単一パスルーティング:</strong>評価ごとに1つの出力のみが有効化されます(排他的ルーティング)。ただし、一部のETLフレームワークでは例外があります。

<strong>設定可能なルール:</strong>条件は演算子で定義され、ネストされたデータを含む複数のフィールドを参照できます。

<strong>拡張可能:</strong>論理的な組み合わせ、ネストされた条件、カスタム式をサポートします。

### 評価シーケンス

1. <strong>入力受信:</strong>データと、オプションのメタデータまたはパラメータを受信
2. <strong>条件評価:</strong>設定された演算子を使用して、定義された各条件を順次評価
3. <strong>ルーティング決定:</strong>`true`と評価された最初の条件が出力を決定
4. <strong>デフォルト処理:</strong>どの条件にも一致しない場合、データはデフォルトルート(定義されている場合)に送信
5. <strong>下流処理:</strong>データは次のコンポーネントまたはアクションに渡される

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

<strong>論理演算子:</strong>`$and`(すべての条件が真である必要がある)、`$or`(いずれかの条件が真)

## 出力

各Conditional Routerノードは複数の出力ポートを提供します:

| 出力名 | トリガー条件 | 出力データ型 |
|-------------|-------------------|------------------|
| True Route | 条件が`true`と評価されたとき | Message/Object |
| False Route | 条件が`false`と評価されたとき | Message/Object |
| Custom Routes | 各条件の名前付き出力 | Message/Object |
| Default Route | どの条件にも一致しないとき | Message/Object |

<strong>名前付き出力ポート:</strong>各条件は名前付き出力にリンクされます。  
<strong>デフォルト出力:</strong>一致しないデータを処理します。  
<strong>データ転送:</strong>元の(または変換された)メッセージ/データは、有効化された出力を通じて渡されます。

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

<strong>条件の順序</strong>早期の一致を防ぐために、汎用的な条件の前に具体的な条件を配置します。

<strong>フェイルセーフデフォルト</strong>一致しないデータのために常にデフォルト出力を設定します。

<strong>テスト</strong>テストデータでロジックを検証して正しいルーティングを確保し、ログと分析を使用してルーティング決定を監視します。

<strong>ドキュメント</strong>保守性のために複雑な条件にコメントまたはドキュメントを付けます。

<strong>セキュリティ</strong>必須でない限り、また入力が信頼できる場合を除き、安全でないテンプレート評価を避けます。

<strong>パフォーマンス</strong>ルーティングを高速で保守可能に保つために、過度なネストや極端に複雑な条件を避けます。

<strong>ノーコードアクセシビリティ</strong>より広いアクセシビリティのために、グラフィカルまたはノーコードインターフェースを提供するプラットフォームを使用します。

## トラブルシューティングとFAQ

<strong>Q: 複数の条件が一致した場合はどうなりますか?</strong>A: (順序で)最初に一致した条件のみが選択されます。後続の一致は無視されます。一部のETLツールでは、データを複数の出力にルーティングできます。

<strong>Q: 複数のフィールドに基づいてルーティングするにはどうすればよいですか?</strong>A: 論理演算子(`$and`、`$or`)を使用して、複数のフィールドの条件を組み合わせます。

<strong>Q: 参照されたフィールドが存在しない場合はどうなりますか?</strong>A: 通常、条件は`false`と評価され、ルーターは次の条件またはデフォルトに進みます。

<strong>Q: 正規表現や高度なマッチングを使用できますか?</strong>A: はい、多くのルーターは`$regex`またはパターンベースの演算子をサポートしています。

<strong>Q: これは非開発者に適していますか?</strong>A: 多くのプラットフォームはノーコード設定を提供しています。

<strong>Q: 並列ルーティングを実行できますか?</strong>A: ほとんどのルーターは排他的(評価ごとに単一パス)です。並列アクションの場合は、専用のマルチルートまたは分岐コンポーネントを使用します。

## 参考文献


1. AWS. (n.d.). AWS Glue: Conditional Router. AWS Documentation.
2. FlowHunt. (n.d.). FlowHunt: Conditional Router. FlowHunt Documentation.
3. Haystack. (n.d.). Haystack: ConditionalRouter. Haystack Documentation.
4. Portkey AI. (n.d.). Portkey AI: Conditional Routing. Portkey AI Documentation.
5. Portkey AI. (n.d.). Portkey AI: Combined Routing with Multiple Conditions. Portkey AI Documentation.
6. Fluix. (n.d.). Fluix: Conditional Logic Tutorial. Fluix Help.
7. Slack. (n.d.). Slack: Conditional Branching Workflow Builder. Slack Blog.
8. Slack. (n.d.). Slack: Guide to Slack Workflow Builder. Slack Help.
9. Frontline AI. (n.d.). Frontline AI: Understanding Conditional Routing in AI Agent Flows. Frontline AI Help.
10. Rapidomize. (n.d.). Rapidomize: Conditional Routing. Rapidomize Documentation.
11. FlowHunt. (n.d.). FlowHunt: Live Demo. FlowHunt Website.
12. Unknown. (n.d.). Conditional Routing in Slack Workflow Builder. YouTube.
13. Unknown. (n.d.). How to Use Conditional Router in FlowHunt. YouTube.
14. Unknown. (n.d.). AWS Glue Conditional Router Tutorial. YouTube.
