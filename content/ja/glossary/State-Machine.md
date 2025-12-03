---
title: ステートマシン
translationKey: state-machine
description: システムの状態遷移を表現する計算モデル、ステートマシンについて解説します。基本概念、種類、AIチャットボットや自動化における活用方法、実装手法、利点、課題について学びましょう。
keywords:
- ステートマシン
- AIチャットボット
- 自動化
- 有限状態機械
- ステートチャート
category: General
type: glossary
date: 2025-12-03
draft: false
term: すてーとましん
reading: ステートマシン
kana_head: か
e-title: State Machine
---

## ステートマシンとは?

ステートマシンは、システムが外部イベントや入力に応じて有限の状態セット間をどのように遷移するかを記述する、形式的な計算モデルです。各状態はシステム動作中の明確な状況を表し、遷移は特定のトリガーに基づいてシステムがある状態から別の状態へどのように移動するかを定義します。

チャットボット開発や自動化において、ステートマシンは会話フロー、ワークフローステップ、またはプロセス段階を明示的に追跡・制御します。可能な状態の完全な構造(「ユーザー入力待ち」、「リクエスト処理中」、「支払い待ち」など)、遷移を引き起こすトリガー、およびこれらの遷移を管理するルールを定義します。

**参考文献:**
- [XState: State Machines and Statecharts](https://stately.ai/docs/state-machines-and-statecharts)
- [Tencent Cloud: Conversational State Machines](https://www.tencentcloud.com/techpedia/127736)
- [Guiding AI Conversations through Dynamic State Transitions](https://promptengineering.org/guiding-ai-conversations-through-dynamic-state-transitions/)

## 中核概念

### 状態

状態は、特定の瞬間におけるシステムのスナップショットです。チャットボットでは、状態には`GREETING`、`ASK_FOR_INFORMATION`、`PROCESSING`、`PROVIDE_SOLUTION`、`GOODBYE`などが含まれる場合があります。システムは常に任意の時点で正確に1つの状態にあります。

**例:**
- 注文処理の状態:`Pending`、`Shipped`、`Delivered`、`Returned`
- チャットボットの状態:`GREETING`、`ASK_FOR_ISSUE`、`PROCESS_ISSUE`、`PROVIDE_SOLUTION`、`GOODBYE`
- 音楽プレーヤーの状態:`Paused`、`Playing`、`Stopped`

### イベント

イベントは、状態遷移を促すトリガー(入力、アクション、または発生)です。イベントは、ユーザーメッセージ、システムアクション、タイマー、または外部信号である可能性があります。

**例:**
- `user says hello`
- `item shipped`
- `play button pressed`
- `timeout occurred`

### 遷移

遷移は、イベントによってトリガーされる、ある状態から別の状態への移動を定義します。遷移は方向性があり、多くの場合トリガーとなるイベントでラベル付けされます。

**例:**
- `Pending`(状態)から、`item shipped`(イベント)で、`Shipped`(状態)へ:

  `Pending` + `item shipped` → `Shipped`

**図:**  
ステートマシンは、多くの場合、円(状態)を矢印(遷移)で接続したものとして視覚化され、各矢印には遷移を引き起こすイベントがラベル付けされます。

## ステートマシンの種類

### 有限ステートマシン(FSM)

有限ステートマシンは標準的なタイプで、限定された既知の数の状態を持ちます。各状態とイベントに対して定義された遷移があり、予測可能で決定論的な動作を保証します。

**参考文献:**  
- [freeCodeCamp: State Machines Basics](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/)

### 階層的ステートマシン

階層的ステートマシン(ステートチャートとも呼ばれる)は、状態のネストを可能にします。親状態は複数の子状態をカプセル化でき、大規模システムの複雑さを軽減します。

**例:**  
`Booking`親状態には、サブ状態として`FlightBooking`、`HotelBooking`、`CarBooking`が含まれる場合があります。

**参考文献:**  
- [Stately: Statecharts](https://stately.ai/docs/state-machines-and-statecharts)

### 決定論的 vs. 非決定論的

- **決定論的:** 状態と入力の各組み合わせは、正確に1つの可能な次の状態につながります。
- **非決定論的:** 特定の状態と入力に対して複数の遷移が可能な場合があります。理論モデルやパターン認識でより一般的に使用されます。

## ステートマシンの使用方法

### AIチャットボット & 会話フロー

ステートマシンは、チャットボット会話の「メモリ」とフローを管理します。各会話状態は、独自の段階(挨拶、問題詳細の収集、処理、解決策の提供など)を反映します。イベント(通常はユーザー入力)が遷移をトリガーします。

**例:**  
カスタマーサポートチャットボットは、ユーザーの挨拶を受け取ると、`GREETING`から`ASK_FOR_ISSUE`に遷移する場合があります。

**参考文献:**  
- [Tencent Cloud: Building Conversational State Machines](https://www.tencentcloud.com/techpedia/127736)
- [Stately: XState in Conversational UIs](https://stately.ai/docs/xstate)

### 自動化 & ワークフロー管理

ステートマシンは、プロセス自動化とワークフロー管理で広く使用され、`Pending`、`Approved`、`Shipped`などのステップを表します。「承認済み」や「商品発送済み」などのイベントが遷移をトリガーしてワークフローを進めます。

**参考文献:**  
- [Stately: Workflow Modeling](https://stately.ai/docs/xstate)

### その他のドメイン

- **ゲームAI:** NPCの動作をモデル化(待機、巡回、追跡、攻撃)。
- **ロボティクス:** シーケンスを制御(移動、ピック、配置、充電)。
- **ビジネスプロセス自動化:** 承認、エスカレーション、タスクルーティングを管理。

## 実用例

### 例1: 注文処理

**状態:**  
`Pending` → `Shipped` → `Delivered` → `Returned`

**遷移:**  
- `Pending` + `item shipped` → `Shipped`
- `Shipped` + `item delivered` → `Delivered`
- `Delivered` + `item returned` → `Returned`

**図:**  
[Order States Example](https://stately.ai/blog/2023-10-02-what-is-a-state-machine/order-states-light.png)

### 例2: チャットボット会話

**状態:**  
`GREETING` → `ASK_FOR_ISSUE` → `PROCESS_ISSUE` → `PROVIDE_SOLUTION` → `FOLLOW_UP` → `GOODBYE`

**Pythonサンプル実装:**

```python
class ChatbotFSM:
    def __init__(self):
        self.state = 'GREETING'
    def transition(self, user_input):
        if self.state == 'GREETING':
            print("Hello! How can I help you?")
            self.state = 'ASK_FOR_ISSUE'
        elif self.state == 'ASK_FOR_ISSUE':
            print(f"You mentioned: {user_input}. Let me process that.")
            self.state = 'PROCESS_ISSUE'
        elif self.state == 'PROCESS_ISSUE':
            print("Here's what I found: [Solution]")
            self.state = 'GOODBYE'
        elif self.state == 'GOODBYE':
            print("Goodbye!")
```
(出典: [Tencent Cloud](https://www.tencentcloud.com/techpedia/127736))

### 例3: 音楽プレーヤー

- `Paused`から開始
- 「再生」で`Playing`に遷移
- 「一時停止」で`Paused`に戻る
- 「スキップ」は任意の状態から機能

### 例4: 旅行予約フロー

**状態:**  
`Idle`、`Booking Flight`、`Booking Hotel`、`Booking Car`、`Confirmation`、`Error`

「フライト予約完了」、「ホテル予約失敗」、「タイムアウト」などのイベントが遷移をトリガーします。エラー処理には階層的状態を使用できます。

## 実装ガイダンス

### モジュラー設計

- **関心の分離:** 保守性のために、各状態を個別の関数またはクラスとして実装します。
- **状態ハンドラーのマッピング:** 辞書またはオブジェクトを使用して、状態をハンドラー関数にマッピングします。

### 状態とコンテキストの永続化

- **セッション管理:** インメモリストレージまたはデータベースを使用して、現在の状態とコンテキスト(ユーザー入力、会話履歴など)を保存します。

**例:**
```python
user_sessions = {user_id: {'state': 'PROCESS_ISSUE', 'issue': 'login problem'}}
```
(出典: [Tencent Cloud](https://www.tencentcloud.com/techpedia/127736))

### ツールとライブラリ

- **[XState](https://stately.ai/docs/xstate):** ステートマシンとステートチャート用のJavaScript/TypeScriptライブラリ。
- **[Stately Editor](https://state.new):** ステートマシンを設計およびエクスポートするためのビジュアルエディター。
- **[Mermaid](https://mermaid-js.github.io/mermaid/):** ステートチャート用の図作成ツール。
- Python、Javaなどの**言語固有のライブラリ**。

### サンプルコードスニペット

**Python FSMスケルトン:**

```python
class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state
        self.transitions = {
            'Pending': {'item shipped': 'Shipped'},
            'Shipped': {'item delivered': 'Delivered'},
            'Delivered': {'item returned': 'Returned'},
        }
    def on_event(self, event):
        if event in self.transitions[self.state]:
            self.state = self.transitions[self.state][event]
        else:
            print("Invalid transition")
```

**XStateの例:**
```javascript
import { createMachine } from 'xstate';
const orderMachine = createMachine({
  initial: 'pending',
  states: {
    pending: { on: { SHIP: 'shipped' } },
    shipped: { on: { DELIVER: 'delivered' } },
    delivered: { on: { RETURN: 'returned' } },
    returned: {}
  }
});
```
(出典: [XState Documentation](https://stately.ai/docs/xstate))

## ステートマシンの利点

- **明確性:** 状態図はロジックを視覚化し、コミュニケーションを改善します。
- **一貫性:** 明示的な状態と遷移の定義により、予期しない動作を防ぎます。
- **モジュール性:** 各状態のロジックが分離されており、保守とスケーラビリティが容易です。
- **網羅的テスト:** すべてのパスを列挙してテストできます。
- **明示的コンテキスト:** 会話またはワークフローの状態を確実に維持します。
- **予測可能性:** 決定論的遷移により、定義された結果が保証されます。

## 課題と制限

- **複雑性:** 多数の状態と遷移は状態爆発につながり、図の管理が困難になる可能性があります。
- **スケーラビリティ:** オープンエンドまたは高度に動的なシステムでは、階層的または構成的なステートマシンが必要になる場合があります。
- **柔軟性:** 厳格な状態モデルは硬直的である可能性があり、創造的または非線形のフローを捉えることが難しい場合があります。
- **統合:** データベース、API、または外部サービスとの組み合わせは複雑さを増します。
- **コンテキストの制限:** LLM駆動のボットでは、コンテキストウィンドウサイズが状態の想起を制限する可能性があります。明示的なコンテキスト管理が不可欠です。

**緩和戦略:**
- モジュラー状態ハンドラーと階層的ステートマシンを使用します。
- 外部ストレージにコンテキストを永続化します。
- 複雑さを管理可能に保つために、状態図を定期的にリファクタリングします。

## 高度な概念

### 階層的 & ネストされたステートマシン

- 階層的ステートマシン(ステートチャート)は、状態がネストされたサブ状態を持つことを可能にし、複雑なフローをカプセル化し、冗長性を削減します。
- ステートチャートは、並列状態、履歴、エントリ/エグジットアクションなどの機能を追加します。

**参考文献:**  
- [XState: Statecharts](https://stately.ai/docs/state-machines-and-statecharts)
- [Stately Visual Editor](https://state.new)

### 機械学習との統合

- **ハイブリッドモデル:** 適応的遷移のためにステートマシンとMLモデルを組み合わせます(例:MLがユーザーの意図を分類し、ステートマシンが会話フローを管理)。
- **強化学習:** エージェントは経験から最適な遷移を学習できます。
- **動的遷移ロジック:** MLモデルは豊富なコンテキストに基づいて次の状態を予測できます。

**参考文献:**  
- [Guiding AI Conversations through Dynamic State Transitions](https://promptengineering.org/guiding-ai-conversations-through-dynamic-state-transitions/)

### 動的ペルソナ生成

- 複雑なチャットボットでは、ステートマシンはコンテキストに基づいてボットのペルソナや役割を切り替えることができます(例:一般エージェントから専門家へ)。

## 関連用語集

- **状態空間:** すべての可能な状態の完全なセット。
- **遷移関数:** 現在の状態とイベントが与えられた場合の次の状態を定義します。
- **初期状態:** 開始状態。
- **最終状態:** プロセスを終了する状態。
- **イベント:** 遷移をトリガーする可能性のある入力、アクション、または発生。
- **セッション:** インタラクション間で保持されるコンテキスト。
- **決定論的FSM:** 状態からの各入力は1つの次の状態につながります。
- **非決定論的FSM:** 入力が複数の次の状態につながる可能性があります。
- **状態エージェント:** 状態遷移を管理するソフトウェア(またはエージェント)。

## 参考文献 & 参考資料

- [Understanding State Machines (freeCodeCamp)](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/)
- [What is a State Machine? (Stately Blog)](https://stately.ai/blog/2023-10-05-what-is-a-state-machine)
- [Guiding AI Conversations](https://promptengineering.org/guiding-ai-conversations-through-dynamic-state-transitions/)
- [XState Documentation](https://stately.ai/docs/xstate)
- [Stately Editor – Try Online](https://state.new)
- [Tencent Cloud: Conversational FSM](https://www.tencentcloud.com/techpedia/127736)
- [Stately YouTube Video Introduction](https://www.youtube.com/watch?v=EzYIerEutgk)
- [Building a Chatbot with State Machines (Medium)](https://rogerjunior.medium.com/how-to-build-a-chatbot-from-scratch-with-javascript-using-state-machines-95597c436517)

## その他のリソース

- [Stately Visual Editor](https://state.new) – ステートマシンを視覚的に設計およびエクスポート。
- [XState VS Code Extension](https://marketplace.visualstudio.com/items?itemName=statelyai.stately-vscode)
- [State Machine Based Human-Bot Conversation Model (NCBI)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7266438/)

*実践的な探索には、[Statelyのオンラインエディター](https://state.new)を試すか、[このビデオ紹介](https://www.youtube.com/watch?v=EzYIerEutgk)をご覧ください。*

**関連項目:**
- [XState: Example State Machine Registry](https://stately.ai/registry)
- [Mermaid Statecharts Documentation](https://mermaid-js.github.io/mermaid/#/stateDiagram)

この用語集は生きたドキュメントです。最新のベストプラクティスとコード例については、常に[XState](https://stately.ai/docs/xstate)と[Stately](https://stately.ai/)の公式ドキュメントを参照してください。

**出典は全体に含まれています。主要な技術コンテンツとコード例は、[Tencent Cloud](https://www.tencentcloud.com/techpedia/127736)と[Stately/XState](https://stately.ai/docs/xstate)からのものです。**