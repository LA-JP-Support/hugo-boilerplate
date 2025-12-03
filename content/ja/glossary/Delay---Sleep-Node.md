---
title: Delay / Sleepノード
translationKey: delay-sleep-node
description: Delay/Sleepノードは、AIチャットボットや自動化ワークフローにおいて、設定された期間または条件が満たされるまでワークフローの実行を一時停止します。APIレート制限やオーケストレーションにおいて重要な役割を果たします。
keywords:
- Delayノード
- Sleepノード
- 自動化ワークフロー
- AIチャットボット
- ワークフローオーケストレーション
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: ディレイ スリープ ノード
reading: Delay / Sleep ノード
kana_head: その他
e-title: Delay / Sleep Node
---

## Delay / Sleep Nodeとは?

Delay / Sleep Nodeは、自動化プラットフォームやコード内の関数として見られるコンポーネントで、設定可能な期間または条件が満たされるまで実行を一時停止します。
- コード(JavaScript/Node.js)では、非ブロッキング方式で実行を中断する関数(`sleep`、`delay`など)として実装されます。例えば、Promiseとasync/awaitを使用します。
- ワークフロー自動化ツール(n8n、Make、AWS SSM、Cognigy、Jira)では、特定の時間またはイベントに対して設定可能なビジュアルノード/ブロックとして提供されます。

**なぜ実行を一時停止するのか?**
- API呼び出しの間隔を空けて、レート制限を防ぐため。
- 外部プロセス(ファイルアップロード、支払い確認など)を待つため。
- 時間ベースまたはイベントベースの条件でワークフローを調整するため。

**参考資料:**
- [JavaScript version of sleep() (Stack Overflow)](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep)
- [Mimo: JavaScript Sleep Function](https://mimo.org/glossary/javascript/sleep-function)

## 目的と使用例

**Delay/Sleep Nodeはいつ、なぜ使用されるのか?**
- **APIレート制限:** リクエストの間隔を空けて、クォータ超過を防ぐ。
- **ワークフローオーケストレーション:** 制御された間隔で特定の順序でステップが実行されることを保証する。
- **ポーリング/条件待機:** 外部イベントまたは条件が満たされるまで一時停止する。
- **テスト&シミュレーション:** 遅い操作やネットワーク遅延をシミュレートする。
- **リトライ&バックオフ:** 指数バックオフを使用したリトライを実装する。
- **外部システムのバッファ:** 続行する前にデータ同期の時間を確保する。

**例:**
- 通知メールの間に数秒待機する。
- ファイルアップロードが確認されるまで一時停止する。
- ステータスが「完了」になるまで1分ごとにAPIをポーリングする。

## Delay / Sleepの実装方法

### JavaScript & Node.js

JavaScriptとNode.jsはシングルスレッド、非ブロッキング環境です。組み込みの`sleep()`関数はありません。
- 標準的なパターンは、イベントループをブロックせずに遅延を挿入するために非同期アプローチ(Promise、async/await)を使用することです。
- コミュニティのベストプラクティスは、`setTimeout`をPromiseでラップすることです:

```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```
- [Stack Overflow: JS sleep best practice](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep)
- [Mimo Glossary: JavaScript Sleep Function](https://mimo.org/glossary/javascript/sleep-function)

### 自動化プラットフォーム(n8n、Make、AWS SSM、Cognigy、Jira)

ワークフローツールはビジュアルDelay/Sleep Nodeを提供します:
- **期間:** 固定時間(秒、分、時間、ISO 8601)。
- **条件/イベントベース:** 論理条件が真になるまで待機。
- **タイムアウト:** 無期限の待機を防ぐ。
- **指数バックオフ:** インテリジェントなポーリングまたはリトライのため。

## JavaScript/Node.jsでの実装テクニック

### `setTimeout`とコールバック

**パターン:**
```js
function sleep(ms, callback) {
  setTimeout(callback, ms);
}
console.log('Start');
sleep(2000, () => console.log('End after 2 seconds'));
```
- **使用例:** シンプルな単発の遅延。
- **欠点:** コールバック地獄、連続した操作の連鎖が困難。

### Promiseと`async`/`await`

**モダンなsleep関数:**
```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function main() {
  console.log('Start');
  await sleep(2000);
  console.log('End after 2 seconds');
}
main();
```
- **利点:** クリーンで読みやすく、非ブロッキング、簡単に組み合わせ可能。
- **欠点:** `async`関数の使用が必要。

**ワンライナー:**
```js
await new Promise(resolve => setTimeout(resolve, 5000));
```

**参考:**
- [Stack Overflow: Best sleep pattern](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep)
- [Mimo: JavaScript Sleep Function](https://mimo.org/glossary/javascript/sleep-function)

### サードパーティパッケージ(例:`sleep-promise`)

**例:**
```js
const sleep = require('sleep-promise');
await sleep(5000); // 5秒待機
```
- **利点:** キャンセル、タイムアウトなどの機能、より良いクロスプラットフォームサポート。
- **欠点:** 追加の依存関係。

### ブロッキング&同期Sleep方式

**本番環境では推奨されません。**
- イベントループ全体をブロックし、すべての並行タスクのパフォーマンスを低下させます。
- 例(Node.js、Unixのみ):
```js
const { execSync } = require('child_process');
function sleep(seconds) {
  execSync(`sleep ${seconds}`);
}
```
- **使用例:** デバッグまたはクイックスクリプト、本番環境では決して使用しない。

### 高度な機能:AbortController、タイムアウト、インテリジェントポーリング

**キャンセル可能なsleep:**
```js
const sleep = (ms, { signal, timeout } = {}) => {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(resolve, ms);
    if (signal) {
      signal.addEventListener('abort', () => {
        clearTimeout(timer);
        reject(new Error('Sleep aborted'));
      });
    }
    if (timeout) {
      setTimeout(() => reject(new Error('Timeout')), timeout);
    }
  });
};
```
- **使用例:** 長時間実行される待機の中止またはタイムアウト。

**インテリジェントポーリング(指数バックオフ):**
```js
let interval = 1000, maxInterval = 30000;
while (!conditionMet) {
  await sleep(interval);
  if (checkCondition()) break;
  interval = Math.min(interval * 2, maxInterval);
}
```
- **使用例:** 非同期外部イベントを待つ。

**参考資料:**
- [JavaScript Sleep, Wait & Delay Guide](https://www.index.dev/blog/javascript-sleep-wait-delay-guide)
- [LinkedIn: Intelligent Delay Node](https://www.linkedin.com/posts/muhammedadnanvv_alright-lets-cut-through-the-noise-youre-activity-7341374262135373825-6xUv)

## 自動化ワークフローにおけるDelay/Sleep Node

### AWS SSM (Systems Manager) Automation

- **ノード:** `aws:sleep`
- **設定:**
    - `Duration` (ISO 8601、例:`PT10M`)
    - `Timestamp` (例:`2020-01-01T01:00:00Z`)
- **最大遅延:** 7日間(604799秒)
- **参考資料:**
    - [AWS SSM Sleep Action](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-sleep.html)

**例:**
```yaml
name: sleep
action: aws:sleep
inputs:
  Duration: PT10M
```

### Cognigy

- **ノード:** Sleep Node
- **機能:** チャットボットフローを設定された期間一時停止する。
- **設定:** ミリ秒、秒などでの期間。
- **公式ドキュメント:**
    - [Cognigy Sleep Node](https://docs.cognigy.com//ai/agents/develop/node-reference/logic/sleep)

### n8n & Make

- **ノード:** Delay/Sleep/Wait Node
- **設定:** 期間、単位、場合によってはイベントベースの待機。
- **ベストプラクティス:**
    - 実行リソースを節約するため、Delay/Wait Nodeは控えめに使用する。
    - 遅延を伴う配列の処理では、各アイテムをループで処理し、反復の間に遅延を挿入する。
    - [n8n Community: Delays Between Array Items](https://community.n8n.io/t/processing-array-items-individually-with-delays-between-each-item/86897)
    - [n8n Community: Wait Node & Parallel Execution](https://community.n8n.io/t/wait-node-parelle-node-workflow-execution/154867)

### Jira Automation

- **コンポーネント:** Delay / Pause / Wait Step
- **機能:** 競合状態を防ぎ、自動化を確実に順序付けるために一時停止を挿入する。
- **設定:** 期間、または長い待機のために複数の遅延を重ねる。
- **ベストプラクティス:**
    - Jira自動化のブランチは並列実行される可能性があることに注意する。遅延でアクションをシリアル化するか、別々のルールに分割する必要がある場合がある。
    - [Jira Issue: Support for delay / pause / wait step](https://jira.atlassian.com/browse/AUTO-238)
    - [Atlassian Community: Can I set a delay in Jira Automation?](https://community.atlassian.com/forums/Jira-questions/Can-I-set-a-delay-in-Jira-Automation/qaq-p/3074180)

## ベストプラクティス

- **常に非ブロッキング遅延(Promise、async/await、またはプラットフォームネイティブの遅延ノード)を使用する。**
- **サーバーまたは本番環境では同期/ブロッキングsleepを避ける。**
- **無期限の待機を防ぐためにタイムアウトを使用する。**
- **外部システムのポーリングまたはリトライには指数バックオフを適用する。**
- **遅延の範囲を必要な場所のみに制限する。**
- **キャンセルをサポートする(例:JSのAbortController、またはワークフローの中止/タイムアウト設定)。**
- **実行リソースを節約し、特にクラウド自動化プラットフォームでクォータに達するのを避けるため、過度または不要な遅延を避ける。**
- **n8nのようなプラットフォームでは、ボトルネックやリソース競合を避けるために遅延を分散させる。**

## トラブルシューティング / FAQ

**Node.jsに組み込みの`sleep()`関数がないのはなぜですか?**
Node.jsは非同期、非ブロッキングI/O用に設計されています。イベントループをブロックすると、すべての並行タスクのパフォーマンスが低下します。`async`/`await`またはPromiseを使用してください。

**遅延ノードが他のフローをブロックしているようです!**
Node.jsでのブロッキングsleepの誤った使用(例:whileループまたはexecSync)を確認してください。自動化プラットフォームでは、共有(シングルスレッド)環境での過度または長い遅延を避けてください。

**固定時間ではなく、条件を待つにはどうすればよいですか?**
増加する遅延(指数バックオフ)を使用したポーリングループを使用するか、プラットフォームがサポートしている場合は「wait until」ノードを使用してください。
- [LinkedIn: Intelligent Delay Node](https://www.linkedin.com/posts/muhammedadnanvv_alright-lets-cut-through-the-noise-youre-activity-7341374262135373825-6xUv)

**delay/sleep操作をキャンセルできますか?**
モダンなJavaScriptでは、`AbortController`を使用してください。ワークフローツールでは、中止/タイムアウトをサポートするノードを探してください。

## 参考資料&参考文献

- [What is the JavaScript version of sleep()? (Stack Overflow)](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep)
- [Mimo: JavaScript Sleep Function](https://mimo.org/glossary/javascript/sleep-function)
- [Nodejs Sleep Function: Pause for a Period of Time](https://www.zignuts.com/blog/nodejs-sleep-function)
- [JavaScript Sleep, Wait & Delay Guide](https://www.index.dev/blog/javascript-sleep-wait-delay-guide)
- [AWS SSM Sleep Action](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-sleep.html)
- [Cognigy Sleep Node](https://docs.cognigy.com//ai/agents/develop/node-reference/logic/sleep)
- [n8n Community: Delays Between Array Items](https://community.n8n.io/t/processing-array-items-individually-with-delays-between-each-item/86897)
- [n8n Community: Wait Node & Parallel Execution](https://community.n8n.io/t/wait-node-parelle-node-workflow-execution/154867)
- [Jira Issue: Support for delay / pause / wait step](https://jira.atlassian.com/browse/AUTO-238)
- [Atlassian Community: Can I set a delay in Jira Automation?](https://community.atlassian.com/forums/Jira-questions/Can-I-set-a-delay-in-Jira-Automation/qaq-p/3074180)
- [LangChain Chatbot Real Python Tutorial](https://realpython.com/build-llm-rag-chatbot-with-langchain/)

## パラメータ表:Delay/Sleep Node(汎用)

| パラメータ | 型 | 説明 | 例の値 |
|--------------|-----------------|-----------------------------------------------|-----------------------|
| Duration     | Number/String   | 遅延する時間(ms/s/min/h、ISO 8601) | `5000`、`"PT10M"` |
| Condition    | Function/String | オプション:条件が満たされるまで待機 | `status === "done"` |
| Max Wait     | Number          | 待機する最大時間 | `60000`(1分) |
| Abort Signal | Object          | JS用:`AbortController.signal` | - |
| Timeout      | Number          | ポーリングまたは待機のタイムアウト | `30000`(30秒) |

## 使用例

### チャットボットフロー

- **シナリオ:** ユーザー入力後、処理をシミュレートするために応答前に3秒待機する。
- **方法:** Cognigyまたはn8nで「Sleep」ノード(例:3000 ms)を配置する。

### APIレート制限

- **シナリオ:** 統合が1 req/sec制限でリクエストを送信する。
- **方法:** Node.jsで`await sleep(1000)`を使用するか、自動化で1秒のDelayノードを使用する。

### インテリジェントポーリング(イベント待機)

- **シナリオ:** 支払い確認を待つが、過度なAPI呼び出しを避ける。
- **方法:** 指数バックオフポーリングループを使用する:

```js
let delay = 1000, maxDelay = 30000;
while (!(await isConfirmed())) {
  await sleep(delay);
  delay = Math.min(delay * 2, maxDelay);
}
```

## 関連キーワード&概念

sleep function、pause period time、await promise resolve、asynchronous operations、await sleep、delay automation、return promise resolve、sleep promise、function sleep、const sleep、delay node、sleep delay、event loop、async function、async await syntax、sleep 2000

## まとめ

Delay/Sleep Nodeは、コードとモダンなワークフロー自動化プラットフォームの両方で、時間ベースおよび条件付きフローを調整するための基本的な構成要素です。JavaScriptでの現在のベストプラクティスは、非ブロッキングで読みやすいコードのためにPromiseとasync/awaitを使用することです。自動化プラットフォームでは、delay/waitノードは慎重に使用する必要があります—信頼性と効率を最大化するように設定し、常にリソース管理と実行の明確性を念頭に置いてください。

コードサンプル、ワークフロー図、より高度な使用パターンについては、[参考資料&参考文献](#参考資料参考文献)セクションを参照してください。

*この用語集エントリは、自動化およびチャットボットワークフローにおける時間管理、ペーシング、条件付き待機のための堅牢なソリューションを求める開発者のために維持されています。*