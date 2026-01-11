---
title: ステートマシン
translationKey: state-machine
description: システムの状態遷移を表現する計算モデル、ステートマシンについて解説します。基本概念、種類、AIチャットボットや自動化での活用方法、実装方法、利点、課題について学びましょう。
keywords:
- ステートマシン
- AIチャットボット
- 自動化
- 有限ステートマシン
- ステートチャート
category: General
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: State Machine
term: すてーとましん
url: "/ja/glossary/state-machine/"
aliases:
- "/ja/glossary/State-Machine/"
---
## ステートマシンとは何か?
ステートマシンは、システムが外部イベントや入力に応じて有限の状態セット間をどのように遷移するかを記述する、形式的な計算モデルです。各状態はシステム動作中の明確な状況を表し、遷移は特定のトリガーに基づいてシステムがある状態から別の状態へどのように移動するかを定義します。

チャットボット開発や自動化において、ステートマシンは会話フロー、ワークフローステップ、またはプロセス段階を明示的に追跡・制御します。可能な状態の完全な構造(「ユーザー入力待ち」、「リクエスト処理中」、「支払い待ち」など)、遷移を引き起こすトリガー、およびこれらの遷移を管理するルールを定義します。

## 中核概念

### 状態

状態は、特定の瞬間におけるシステムのスナップショットです。チャットボットでは、状態には`GREETING`、`ASK_FOR_INFORMATION`、`PROCESSING`、`PROVIDE_SOLUTION`、`GOODBYE`などが含まれる場合があります。システムは常に任意の時点で正確に1つの状態にあります。

**例:**
- **注文処理:** `Pending`、`Shipped`、`Delivered`、`Returned`
- **チャットボット会話:** `GREETING`、`ASK_FOR_ISSUE`、`PROCESS_ISSUE`、`PROVIDE_SOLUTION`、`GOODBYE`
- **音楽プレーヤー:** `Paused`、`Playing`、`Stopped`

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
`Pending`(状態)から、`item shipped`(イベント)で、`Shipped`(状態)へ:  
`Pending` + `item shipped` → `Shipped`

ステートマシンは、多くの場合、円(状態)を矢印(遷移)で接続したものとして視覚化され、各矢印は遷移を引き起こすイベントでラベル付けされます。

## ステートマシンの種類

### 有限ステートマシン(FSM)

有限ステートマシンは標準的なタイプで、限定された既知の数の状態を持ちます。各状態とイベントに対して定義された遷移があり、予測可能で決定論的な動作を保証します。

### 階層型ステートマシン

階層型ステートマシン(ステートチャートとも呼ばれる)は、状態のネストを可能にします。親状態は複数の子状態をカプセル化でき、大規模システムの複雑さを軽減します。

**例:** `Booking`親状態には、サブ状態として`FlightBooking`、`HotelBooking`、`CarBooking`が含まれる場合があります。

### 決定論的 vs 非決定論的

**決定論的:** 状態と入力の各組み合わせは、正確に1つの可能な次の状態につながります。

**非決定論的:** 特定の状態と入力に対して複数の遷移が可能な場合があります。理論モデルやパターン認識でより一般的に使用されます。

## ステートマシンの使用方法

### AIチャットボットと会話フロー

ステートマシンは、チャットボット会話の「メモリ」とフローを管理します。各会話状態は、独自の段階(挨拶、問題詳細の収集、処理、解決策の提供など)を反映します。イベント(通常はユーザー入力)が遷移をトリガーします。

**例:** カスタマーサポートチャットボットは、ユーザーの挨拶を受け取ると、`GREETING`から`ASK_FOR_ISSUE`に遷移する場合があります。

### 自動化とワークフロー管理

ステートマシンは、プロセス自動化とワークフロー管理で広く使用され、`Pending`、`Approved`、`Shipped`などのステップを表します。「承認済み」や「商品発送済み」などのイベントが遷移をトリガーしてワークフローを進行させます。

### その他のドメイン

**ゲームAI:** NPCの動作をモデル化(idle、patrol、chase、attack)

**ロボティクス:** シーケンスを制御(move、pick、place、recharge)

**ビジネスプロセス自動化:** 承認、エスカレーション、タスクルーティングを管理

## 実践例

### 例1: 注文処理

**状態:** `Pending` → `Shipped` → `Delivered` → `Returned`

**遷移:**
- `Pending` + `item shipped` → `Shipped`
- `Shipped` + `item delivered` → `Delivered`
- `Delivered` + `item returned` → `Returned`

### 例2: チャットボット会話

**状態:** `GREETING` → `ASK_FOR_ISSUE` → `PROCESS_ISSUE` → `PROVIDE_SOLUTION` → `FOLLOW_UP` → `GOODBYE`

**サンプルPython実装:**

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

### 例3: 音楽プレーヤー

- `Paused`で開始
- 「再生」で`Playing`に遷移
- 「一時停止」で`Paused`に戻る
- 「スキップ」は任意の状態から機能

### 例4: 旅行予約フロー

**状態:** `Idle`、`Booking Flight`、`Booking Hotel`、`Booking Car`、`Confirmation`、`Error`

「フライト予約完了」、「ホテル予約失敗」、「タイムアウト」などのイベントが遷移をトリガーします。エラー処理には階層状態を使用できます。

## 実装ガイダンス

### モジュラー設計

**関心の分離:** 保守性のために、各状態を個別の関数またはクラスとして実装します。

**状態ハンドラーのマッピング:** 辞書またはオブジェクトを使用して、状態をハンドラー関数にマップします。

### 状態とコンテキストの永続化

**セッション管理:** インメモリストレージまたはデータベースを使用して、現在の状態とコンテキスト(ユーザー入力、会話履歴など)を保存します。

**例:**
```python
user_sessions = {
    user_id: {
        'state': 'PROCESS_ISSUE',
        'issue': 'login problem'
    }
}
```

### ツールとライブラリ

**XState:** ステートマシンとステートチャート用のJavaScript/TypeScriptライブラリ

**Stately Editor:** ステートマシンを設計およびエクスポートするためのビジュアルエディター

**Mermaid:** ステートチャート用のダイアグラムツール

**言語固有のライブラリ** Python、Javaなど

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

## ステートマシンの利点

**明確性:** 状態図はロジックを視覚化し、コミュニケーションを改善します

**一貫性:** 明示的な状態と遷移の定義により、予期しない動作を防ぎます

**モジュール性:** 各状態のロジックが分離され、保守とスケーラビリティが容易になります

**網羅的なテスト:** すべてのパスを列挙してテストできます

**明示的なコンテキスト:** 会話またはワークフローの状態を確実に維持します

**予測可能性:** 決定論的な遷移により、定義された結果が保証されます

## 課題と制限

**複雑性:** 多数の状態と遷移は状態爆発につながり、図の管理が困難になる可能性があります

**スケーラビリティ:** オープンエンドまたは高度に動的なシステムでは、階層型または構成型のステートマシンが必要になる場合があります

**柔軟性:** 厳格な状態モデルは硬直的である可能性があり、創造的または非線形のフローをキャプチャするのが難しい場合があります

**統合:** データベース、API、または外部サービスとの組み合わせは複雑さを増します

**コンテキストの制限:** LLM駆動のボットでは、コンテキストウィンドウサイズが状態の想起を制限する可能性があります。明示的なコンテキスト管理が不可欠です

### 緩和戦略

- モジュラー状態ハンドラーと階層型ステートマシンを使用する
- 外部ストレージにコンテキストを永続化する
- 複雑さを管理可能に保つために、状態図を定期的にリファクタリングする

## 高度な概念

### 階層型およびネスト型ステートマシン

階層型ステートマシン(ステートチャート)は、状態にネストされたサブ状態を持つことを可能にし、複雑なフローをカプセル化し、冗長性を削減します。ステートチャートは、並列状態、履歴、エントリ/イグジットアクションなどの機能を追加します。

### 機械学習との統合

**ハイブリッドモデル:** 適応的な遷移のためにステートマシンとMLモデルを組み合わせます(例:MLがユーザーの意図を分類し、ステートマシンが会話フローを管理)

**強化学習:** エージェントは経験から最適な遷移を学習できます

**動的遷移ロジック:** MLモデルは豊富なコンテキストに基づいて次の状態を予測できます

### 動的ペルソナ生成

複雑なチャットボットでは、ステートマシンはコンテキストに基づいてボットのペルソナや役割を切り替えることができます(例:一般エージェントから専門家へ)。

## ベストプラクティス

**シンプルに始める:** 階層的な複雑さを追加する前に、基本的なFSMから始めます

**徹底的に文書化する:** 状態、イベント、遷移の明確なドキュメントを維持します

**厳密にテストする:** すべての可能な状態遷移とエッジケースを検証します

**パフォーマンスを監視する:** 状態遷移を追跡し、ボトルネックを特定します

**継続的に反復する:** 実際の使用状況に基づいてステートマシン設計を改善します

## ユースケースシナリオ

### カスタマーサービスチャットボット

挨拶から問題解決まで会話フローを管理し、コンテキストを維持し、インタラクション全体で一貫した応答を提供します。

### Eコマース注文処理

注文のライフサイクルを配置から配達まで追跡し、在庫、配送、顧客通知のための明確な状態遷移とイベント処理を行います。

### ゲーム開発

プレイヤーの近接性とゲームイベントに基づいて、idle、patrol、chase、attack状態を切り替えながら、NPCの動作パターンを制御します。

### IoTデバイス管理

センサーデータとユーザーコマンドに基づいた自動遷移により、デバイス状態(active、standby、maintenance、error)を管理します。

## 参考文献

- [freeCodeCamp: Understanding State Machines](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/)
- [Stately Blog: What is a State Machine?](https://stately.ai/blog/2023-10-05-what-is-a-state-machine)
- [Prompt Engineering: Guiding AI Conversations](https://promptengineering.org/guiding-ai-conversations-through-dynamic-state-transitions/)
- [XState Documentation](https://stately.ai/docs/xstate)
- [Stately Editor](https://state.new)
- [Tencent Cloud: Conversational FSM](https://www.tencentcloud.com/techpedia/127736)
- [YouTube: Stately Introduction](https://www.youtube.com/watch?v=EzYIerEutgk)
- [Medium: Building a Chatbot with State Machines](https://rogerjunior.medium.com/how-to-build-a-chatbot-from-scratch-with-javascript-using-state-machines-95597c436517)
- [XState VS Code Extension](https://marketplace.visualstudio.com/items?itemName=statelyai.stately-vscode)
- [NCBI: State Machine Based Human-Bot Conversation Model](https://pmc.ncbi.nlm.nih.gov/articles/PMC7266438/)
- [Mermaid Diagramming Tool](https://mermaid-js.github.io/mermaid/)
- [Stately.ai](https://stately.ai/)
