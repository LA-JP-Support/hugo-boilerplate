---
title: ループノード
translationKey: loop-node
description: ループノードは、ワークフロー内で反復的なアクションを自動化し、条件が満たされるまで、固定回数、またはコレクション内の各アイテムに対してタスクを繰り返します。自動化に不可欠な機能です。
keywords: ["ループノード", "ワークフロー自動化", "AIチャットボット", "RPA", "反復処理"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: ループノード
reading: ループノード
kana_head: ら
e-title: Loop Node
---
## Loop Nodeとは?

**Loop Node**(ループノード)は、ワークフロー内でアクションの繰り返しを自動化します。アイテムのリストを処理したり、特定の回数タスクを繰り返したり、条件が満たされるまで実行したりできます。Loop Nodeは、ワークフロー自動化、RPA、AIチャットボットプラットフォームにおいて、ユーザーリストへのメール送信、入力検証、失敗したアクションの再試行など、反復的な操作を処理するために不可欠です。

- **典型的な使用例:**
  - リスト/コレクションの処理(例:各連絡先へのメッセージ送信)
  - 反復的なタスクの自動化(例:複数部門のレポート生成)
  - バッチ処理(例:API呼び出しをグループで処理)
  - 入力検証(例:有効な入力が得られるまでプロンプト表示)

**出典:**  
- [MindPal Docs: Loop Node](https://docs.mindpal.space/workflow/build/loop-node)  
- [n8n Docs: Looping](https://docs.n8n.io/flow-logic/looping/)  
- [Power Automate: Using loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

## Loop Nodeの動作原理

Loop Nodeの基本的なロジックは、各サイクルでループを継続するか終了するかを評価することです。この評価は以下に基づいて行われます:

- 現在の反復回数(固定ループの場合)
- 現在のアイテムの内容またはプロパティ(コレクションループの場合)
- 論理条件または式の結果(条件付きループの場合)

### 一般的なLoop Nodeのフロー

1. **入力:** 前のノードからリスト、カウント、またはトリガーを受け取ります。
2. **条件チェック:** ループのタイプに基づいて継続するかどうかを判断します。
3. **実行:** 含まれるアクション/サブノードを実行します。
4. **反復:** 次のアイテムに進むか、カウンターを増やすか、条件を再評価します。
5. **終了:** 終了条件が満たされるか、リストが尽きたときに停止します。

**ビジュアルリファレンス:**  
![n8n Loop Node Example](https://docs.n8n.io/_images/flow-logic/looping/example_workflow.png)

**出典:**  
- [MindPal Docs: How a Loop Node Works](https://docs.mindpal.space/workflow/build/loop-node#how-a-loop-node-works)  
- [n8n Docs: Creating loops](https://docs.n8n.io/flow-logic/looping/#creating-loops)

## Loop Nodeの種類とループ方法

ループノードは、終了基準または反復メカニズムによって分類できます:

### 1. 固定回数ループ(シンプルループ)

- 指定された回数だけアクションを繰り返します。
- 開始値、終了値、増分値で設定します。
- **最適な用途:** 繰り返し回数が事前にわかっているシナリオ。

**例:** リマインダーメールを3回送信する。

### 2. For Each / Loop Over Items

- リスト、配列、またはテーブル内の各アイテムを反復処理します。
- 各反復で1つの要素を処理します。
- **最適な用途:** データコレクションの処理、例:パーソナライズされたメールの送信。

### 3. 条件付きループ(While / Until)

- 条件が真である限りアクションを繰り返します。
- 論理演算子とオペランドで設定します。
- **最適な用途:** 入力検証、再試行ロジック、動的ワークフロー。

### 4. バッチループ

- アイテムをグループで処理し、一括操作やレート制限に便利です。
- **最適な用途:** リクエストをチャンク化する必要があるAPI統合。

**出典:**  
- [Power Automate: Loops actions reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)  
- [n8n Docs: Loop Over Items](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/)

## Loop Nodeの使用方法

### 一般的な手順(MindPal、n8n、Power Automateなどに適用可能)

1. **Loop Nodeを挿入:**  
   ワークフローデザイナーで、ロジック/フロー制御セクションからLoop Nodeを追加します。

2. **ループを設定:**
   - **固定回数:** 開始、終了、増分を指定します。
   - **For Each:** 反復処理するコレクション/リストを選択します。
   - **条件付き:** 論理式で終了条件を定義します。

3. **ループ内にアクションを追加:**  
   各サイクルで実行される他のノード/アクションをループ内にドラッグ&ドロップ(または接続)します。

4. **出力を処理:**  
   ループされたアクションからの出力を、後続のワークフローステップの入力として使用します。

**MindPalの例:**  
- アイテムのリストを定義します(「For each item in」フィールド)。
- エージェント(処理ロジックまたはAI)を選択します。
- 処理のための明確で変数駆動型の指示を記述します。
- [参照](https://docs.mindpal.space/workflow/build/loop-node#configuring-a-loop-node)

**n8nの例:**  
- ほとんどのノードは自動的にすべてのアイテムを処理します。
- バッチまたはチャンク処理には「Loop Over Items」を使用します。
- 配線とIFノードを使用した手動ループも可能です。
- [参照](https://docs.n8n.io/flow-logic/looping/#creating-loops)

**Power Automateの例:**  
- 「Loop」、「Loop Condition」、または「For Each」から選択します。
- 必要に応じて開始、終了、増分、または入力リストを設定します。
- 制御には「Exit loop」と「Next loop」を使用します。
- [参照](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

## Loop Node設定:主要パラメータ

| パラメータ            | 説明                                                                                | 例の値                |
|----------------------|--------------------------------------------------------------------------------------------|----------------------|
| **Start From**       | カウンターの初期値(固定回数ループ)                                       | 1                    |
| **End To**           | 停止する値(固定回数ループ)                                             | 10                   |
| **Increment By**     | 各反復でカウンターを増やす量                                            | 1                    |
| **Collection**       | 反復処理する配列またはリスト(for-eachループ)                                        | `[{"name":"A"}]`     |
| **Batch Size**       | バッチごとに処理するアイテム数                                                       | 5                    |
| **Exit Condition**   | ループ終了を制御する論理式                                            | `input == valid`     |
| **Current Item**     | 現在処理中のアイテム                                                           | `{ "email": ... }`   |
| **Output**           | 各反復で実行されたアクションの結果                                          | `{"status":"sent"}`  |

**Power Automateの例:**  
- Start from: 1、Increment by: 1、End to: 5  
- For Each: ファイル名のリスト  
- Loop Condition: `count < 10`  
- [参照](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)

## Loop Nodeの実例

### 1. バッチメール送信
**シナリオ:** 顧客リストにメールを送信する。
**ワークフロー:** 顧客を取得 → Loop Node(for each) → メール送信

### 2. 入力検証(チャットボット)
**シナリオ:** 正しいメールアドレスが入力されるまでユーザーにプロンプト表示。
**ワークフロー:** Loop Node(有効になるまで終了) → プロンプト表示と検証

### 3. APIリクエストの再試行
**シナリオ:** 成功するまで最大3回API呼び出しを再試行する。
**ワークフロー:** Loop Node(成功または最大試行回数で終了) → API呼び出し

### 4. 在庫チェック(Eコマース)
**シナリオ:** カタログ内の製品の在庫をチェックする。
**ワークフロー:** カタログを取得 → Loop Node(for each) → 在庫チェック

**出典:**  
- [MindPal: Loop Node Scenarios](https://docs.mindpal.space/workflow/build/loop-node#when-to-use-a-loop-node)  
- [Power Automate: Loop Examples](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

## Loop Nodeの使用例

- **リストの処理:** データベースやスプレッドシート内の各アイテムに対して、通知、メール、更新の送信、または計算を実行します。
- **バッチ処理:** レート制限を回避するためにレコードをグループで処理します(例:API呼び出しをチャンクで)。
- **再試行ロジック:** 成功するか制限に達するまで操作(ファイルダウンロードやAPIリクエストなど)を再試行します。
- **入力検証:** 正しいデータが入力されるまでユーザーに継続的にプロンプト表示します。
- **条件付き反復:** ビジネスルールが満たされるまでステップを実行します。
- **動的シーケンス:** 動的な質問、タスク、またはロジック分岐のセットをループ処理します。

## プラットフォーム固有の注意事項

### MindPal

- **Loop Node:** リストを受け取り、エージェントを割り当て、特定の指示で各アイテムを処理します。
- **変数:** 変数を使用してループサイクル間および他のノード間でデータを渡します。
- [MindPal Loop Node Docs](https://docs.mindpal.space/workflow/build/loop-node)

### n8n

- **暗黙的な反復:** ノードは通常、すべての入力アイテムを個別に処理します。
- **Loop Over Items Node:** バッチ処理と明示的なチャンク化用。
- **手動ループ:** カスタムロジックのために配線とIFノードを使用して可能です。
- **ノードの例外:** 一部のノード([Node exceptions](https://docs.n8n.io/flow-logic/looping/#node-exceptions)を参照)は手動ループが必要です。
- [n8n Looping Docs](https://docs.n8n.io/flow-logic/looping/)

### Power Automate

- **3つのループタイプ:** Simple Loop(固定回数)、Loop Condition(while/until)、For Each(コレクション)。
- **制御アクション:** 早期に抜けるための「Exit loop」、現在の反復をスキップするための「Next loop」。
- **変数:** ループはアクション内で使用するためのインデックスまたは現在のアイテム変数を生成します。
- [Power Automate Loops Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)
- [Power Automate Using Loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

### Node.jsイベントループ

- **ワークフローLoop Nodeとは異なる:** Node.jsイベントループは、JavaScriptで非同期、ノンブロッキング操作を可能にする低レベルのメカニズムです。
- **フェーズ:** timers、pending callbacks、poll、check、close callbacks。
- **動作原理:** JavaScriptは同期的に実行されます。非同期操作(I/O、タイマー)はlibuvによって処理され、コールバックはキューに入れられ、イベントループフェーズで実行されます。
- **関連性:** setTimeout、setInterval、イベント駆動型プログラミングなどのコード内の非同期「ループ」の基盤。
- [Node.js Event Loop Official Guide](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [GeeksforGeeks Event Loop Article](https://www.geeksforgeeks.org/node-js/node-js-event-loop/)

## 特別な考慮事項とベストプラクティス

- **無限ループ:** 意図しない無限ループを避けるために、常に明確な終了条件を定義してください。
- **パフォーマンスとレート制限:** 大規模または無制限のループはパフォーマンスに悪影響を及ぼし、APIまたはプラットフォームのレート制限をトリガーする可能性があります。
- **バッチサイズ:** 効率と外部システム制限への準拠のバランスを取るためにバッチ処理を調整してください。
- **エラー処理:** 信頼性の低いサービスと対話するループには、再試行制限と適切なエラー処理を実装してください。
- **ノードの例外:** すべてのワークフローノードが自動反復するわけではありません。プラットフォームのドキュメントを参照してください。
- **変数スコープ:** カウンター、現在のアイテム、結果の変数がループ内外で正しくスコープされていることを確認してください。

**参照:**  
- [n8n Docs: Node Exceptions](https://docs.n8n.io/flow-logic/looping/#node-exceptions)  
- [Power Automate Loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)

## 主要用語と関連概念

| 用語                   | 定義                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------|
| **Loop Node**          | 条件が満たされるかアイテムが処理されるまでアクションを繰り返すノード/関数。          |
| **Iteration**          | ループのアクションを通る1つの完全なサイクル。                                                 |
| **Exit Condition**     | ループがいつ終了するかを決定するロジック。                                                  |
| **For Each Loop**      | コレクションまたは配列内のすべてのアイテムを処理します。                                                 |
| **Batch Processing**   | 大きなセットを処理のために小さなグループに分割すること。                                       |
| **Event Loop**         | (Node.js)非同期コールバックとタスクを管理するシステム。                              |
| **Pending Callbacks**  | イベントループのフェーズで処理を待っているコールバック。                                  |
| **Timers**             | 遅延後に実行されるスケジュールされたコールバック(Node.jsのsetTimeout/setInterval)。                |
| **Flow Logic**         | ワークフロー内でノードがどのように実行されるかを管理するシーケンスとルール。                              |

## さらなる読み物とリソース

- [MindPal Docs: Loop Node](https://docs.mindpal.space/workflow/build/loop-node)
- [n8n Looping Documentation](https://docs.n8n.io/flow-logic/looping/)
- [Power Automate Loops Reference](https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)
- [Power Automate Using Loops](https://learn.microsoft.com/en-us/power-automate/desktop-flows/use-loops)
- [Node.js Event Loop Guide](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [Node.js Event Loop (GeeksforGeeks)](https://www.geeksforgeeks.org/node-js/node-js-event-loop/)
- [Master Loop Node in n8n (YouTube)](https://www.youtube.com/watch?v=acFkskQj-kw)
- [Loops in Microsoft Power Automate (YouTube)](https://www.youtube.com/watch?v=54ZFR4SCkO0)

この用語集ページには、Loop Nodeに関する権威ある説明、プラットフォーム固有の設定、技術的な例、ベストプラクティスが含まれており、すべての主要なワークフロー自動化環境の最新の公式ドキュメントへの直接リンクが記載されています。