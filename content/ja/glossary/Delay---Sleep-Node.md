---
title: ディレイ / スリープノード
url: "/ja/glossary/Delay---Sleep-Node/"
translationKey: delay-sleep-node
description: ディレイ/スリープノードは、AIチャットボットや自動化ワークフローにおいて、設定された期間または条件が満たされるまで実行を一時停止します。APIレート制限やオーケストレーションに不可欠な機能です。
keywords:
- ディレイノード
- スリープノード
- 自動化ワークフロー
- AIチャットボット
- ワークフローオーケストレーション
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: Delay / Sleep Node
term: でぃれい / すりーぷのーど
---
## Delay / Sleep ノードとは？
Delay または Sleep ノードは、設定可能な期間または条件が満たされるまで実行を一時停止するコンポーネントです。コード（JavaScript/Node.js）では、`sleep`、`delay` などの関数として実装され、Promise と async/await を使用して非ブロッキング方式で実行を一時停止します。ワークフロー自動化ツール（n8n、Make、AWS SSM、Cognigy、Jira）では、特定の時間またはイベントに対して設定可能なビジュアルノード/ブロックとして提供されます。

<strong>なぜ実行を一時停止するのか？</strong>API 呼び出しの間隔を空けてレート制限を防ぐため、外部プロセス（ファイルアップロード、支払い確認など）を待つため、時間ベースまたはイベントベースの条件でワークフローを調整するため、テストで遅い操作やネットワーク遅延をシミュレートするため、指数バックオフによるリトライを実装するため、そして続行前にデータ同期の時間を確保するためです。

## 目的と使用例

### Delay/Sleep ノードが使用される場面と理由

<strong>API レート制限：</strong>リクエストの間隔を空けてクォータ超過を防ぐ。  
<strong>ワークフロー調整：</strong>制御された間隔で特定の順序でステップが実行されるようにする。  
<strong>ポーリング/条件待機：</strong>外部イベントまたは条件が満たされるまで一時停止する。  
<strong>テスト & シミュレーション：</strong>遅い操作やネットワーク遅延をシミュレートする。  
<strong>リトライ & バックオフ：</strong>指数バックオフによるリトライを実装する。  
<strong>外部システムのバッファ：</strong>続行前にデータ同期の時間を確保する。

<strong>例：</strong>- 通知メールの間に数秒待機する
- ファイルアップロードが確認されるまで一時停止する
- ステータスが「完了」になるまで 1 分ごとに API をポーリングする

## Delay / Sleep の実装方法

### JavaScript & Node.js

JavaScript と Node.js はシングルスレッドの非ブロッキング環境です。組み込みの `sleep()` 関数はありません。標準的なパターンは、非同期アプローチ（Promise、async/await）を使用してイベントループをブロックせずに遅延を挿入することです。

<strong>コミュニティのベストプラクティス：</strong>```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

**モダンな sleep 関数：**```js
async function main() {
  console.log('Start');
  await sleep(2000);
  console.log('End after 2 seconds');
}
```

<strong>ワンライナー：</strong>```js
await new Promise(resolve => setTimeout(resolve, 5000));
```

### 自動化プラットフォーム

ワークフローツールは、設定オプション付きのビジュアル Delay/Sleep ノードを提供します：
- **Duration：**固定時間（秒、分、時間、ISO 8601）
- **Condition/Event-based：**論理条件が真になるまで待機
- **Timeouts：**無期限の待機を防ぐ
- **Exponential Backoff：**インテリジェントなポーリングまたはリトライ用

## JavaScript/Node.js での実装テクニック

### setTimeout とコールバック

**パターン：**```js
function sleep(ms, callback) {
  setTimeout(callback, ms);
}
console.log('Start');
sleep(2000, () => console.log('End after 2 seconds'));
```

<strong>欠点：</strong>コールバック地獄、連続操作のチェーンが困難。

### Promise & async/await

<strong>モダンなアプローチ：</strong>```js
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

**利点：**クリーンで読みやすく、非ブロッキング、簡単に組み合わせ可能。

### サードパーティパッケージ

**例（sleep-promise）：**```js
const sleep = require('sleep-promise');
await sleep(5000); // 5 秒待機
```

<strong>利点：</strong>キャンセル、タイムアウトなどの機能、より良いクロスプラットフォームサポート。

### ブロッキング & 同期 Sleep メソッド

<strong>本番環境では推奨されません。</strong>イベントループ全体をブロックし、すべての並行タスクのパフォーマンスを低下させます。

<strong>例（Node.js、Unix のみ）：</strong>```js
const { execSync } = require('child_process');
function sleep(seconds) {
  execSync(`sleep ${seconds}`);
}
```

### 高度：AbortController、タイムアウト、インテリジェントポーリング

**キャンセル可能な sleep：**```js
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

<strong>インテリジェントポーリング（指数バックオフ）：</strong>```js
let interval = 1000, maxInterval = 30000;
while (!conditionMet) {
  await sleep(interval);
  if (checkCondition()) break;
  interval = Math.min(interval * 2, maxInterval);
}
```

## 自動化ワークフローでの Delay/Sleep ノード

### AWS SSM (Systems Manager) Automation

**ノード：**`aws:sleep`  
**設定：**Duration（ISO 8601、例：`PT10M`）または Timestamp（例：`2020-01-01T01:00:00Z`）  
**最大遅延：**7 日間（604799 秒）

**例：**```yaml
name: sleep
action: aws:sleep
inputs:
  Duration: PT10M
```

### Cognigy

<strong>ノード：</strong>Sleep Node  
<strong>機能：</strong>チャットボットフローを設定された期間一時停止  
<strong>設定：</strong>ミリ秒、秒などでの期間

### n8n & Make

<strong>ノード：</strong>Delay/Sleep/Wait Node  
<strong>設定：</strong>期間、単位、場合によってはイベントベースの待機

<strong>ベストプラクティス：</strong>- 実行リソースを節約するため、Delay/Wait ノードは控えめに使用する
- 遅延を伴う配列処理では、ループで各アイテムを処理し、反復間に遅延を挿入する
- 並列実行の影響を考慮する

### Jira Automation

<strong>コンポーネント：</strong>Delay / Pause / Wait Step  
<strong>機能：</strong>レースコンディションを防ぎ、自動化を確実にシーケンス化するために一時停止を挿入  
<strong>設定：</strong>期間、または長時間待機のために複数の遅延を積み重ねる

<strong>ベストプラクティス：</strong>- Jira 自動化のブランチは並列実行される可能性があることに注意
- 遅延でアクションをシリアル化するか、別のルールに分割する必要がある場合がある

## ベストプラクティス

<strong>1. 常に非ブロッキング遅延を使用する</strong>（Promise、async/await、またはプラットフォームネイティブの遅延ノード）  
<strong>2. サーバーや本番環境で同期/ブロッキング sleep を避ける</strong> 
<strong>3. タイムアウトを使用する</strong>無期限の待機を防ぐため  
<strong>4. 指数バックオフを適用する</strong>外部システムのポーリングやリトライ用  
<strong>5. 遅延の範囲を制限する</strong>必要な場所のみに  
<strong>6. キャンセルをサポートする</strong>（JS では AbortController、ワークフローでは中止/タイムアウト設定など）  
<strong>7. 過度な遅延を避ける</strong>実行リソースを節約し、クォータ超過を回避するため  
<strong>8. 遅延を分散する</strong>n8n などのプラットフォームでボトルネックやリソース競合を避けるため

## トラブルシューティング / FAQ

<strong>Node.js に組み込みの sleep() 関数がないのはなぜですか？</strong>Node.js は非同期、非ブロッキング I/O 用に設計されています。イベントループをブロックすると、すべての並行タスクのパフォーマンスが低下します。async/await または Promise を使用してください。

<strong>遅延ノードが他のフローをブロックしているようです！</strong>Node.js でブロッキング sleep（while ループや execSync など）を誤って使用していないか確認してください。自動化プラットフォームでは、共有（シングルスレッド）環境で過度または長時間の遅延を避けてください。

<strong>固定時間ではなく、条件を待つにはどうすればよいですか？</strong>増加する遅延（指数バックオフ）でポーリングループを使用するか、プラットフォームがサポートしている場合は「wait until」ノードを使用してください。

<strong>遅延/sleep 操作をキャンセルできますか？</strong>モダンな JavaScript では AbortController を使用します。ワークフローツールでは、中止/タイムアウトをサポートするノードを探してください。

## パラメータ表：Delay/Sleep ノード（一般化）

| パラメータ | 型 | 説明 | 例の値 |
|-----------|------|-------------|---------------|
| <strong>Duration</strong>| Number/String | 遅延時間（ms/s/min/h、ISO 8601） | `5000`、`"PT10M"` |
| <strong>Condition</strong>| Function/String | オプション：条件が満たされるまで待機 | `status === "done"` |
| <strong>Max Wait</strong>| Number | 最大待機時間 | `60000`（1 分） |
| <strong>Abort Signal</strong>| Object | JS 用：`AbortController.signal` | - |
| <strong>Timeout</strong>| Number | ポーリングまたは待機のタイムアウト | `30000`（30 秒） |

## 使用例

### チャットボットフロー

<strong>シナリオ：</strong>ユーザー入力後、処理をシミュレートするために応答前に 3 秒待機する。  
<strong>方法：</strong>Cognigy または n8n で「Sleep」ノード（例：3000 ms）を配置する。

### API レート制限

<strong>シナリオ：</strong>統合が 1 req/sec の制限でリクエストを送信する。  
<strong>方法：</strong>Node.js で `await sleep(1000)` を使用するか、自動化で 1 秒の Delay ノードを使用する。

### インテリジェントポーリング（イベント待機）

<strong>シナリオ：</strong>支払い確認を待つが、過度な API 呼び出しを避ける。  
<strong>方法：</strong>指数バックオフポーリングループを使用：

```js
let delay = 1000, maxDelay = 30000;
while (!(await isConfirmed())) {
  await sleep(delay);
  delay = Math.min(delay * 2, maxDelay);
}
```

## まとめ

Delay/Sleep ノードは、コードとモダンなワークフロー自動化プラットフォームの両方で、時間ベースおよび条件付きフローを調整するための基本的な構成要素です。JavaScript での現在のベストプラクティスは、非ブロッキングで読みやすいコードのために Promise と async/await を使用することです。自動化プラットフォームでは、遅延/待機ノードは慎重に使用する必要があります—信頼性と効率を最大化するように設定し、常にリソース管理と実行の明確性を念頭に置いてください。

## 参考文献


1. Stack Overflow. (n.d.). What is the JavaScript version of sleep()?. Stack Overflow.

2. Mimo. (n.d.). JavaScript Sleep Function. Mimo Glossary.

3. Zignuts. (n.d.). Nodejs Sleep Function: Pause for a Period of Time. Zignuts Blog.

4. Index.dev. (n.d.). JavaScript Sleep, Wait & Delay Guide. Index.dev Blog.

5. AWS. (n.d.). SSM Sleep Action. AWS Documentation.

6. Cognigy. (n.d.). Sleep Node. Cognigy Documentation.

7. n8n Community. (n.d.). Delays Between Array Items. n8n Community Forum.

8. n8n Community. (n.d.). Wait Node & Parallel Execution. n8n Community Forum.

9. Jira. (n.d.). Support for delay / pause / wait step. Jira Issue Tracker.

10. Atlassian Community. (n.d.). Can I set a delay in Jira Automation?. Atlassian Community Forum.

11. LinkedIn. (n.d.). Intelligent Delay Node. LinkedIn Post.

12. Real Python. (n.d.). LangChain Chatbot Tutorial. Real Python.
