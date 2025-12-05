---
title: ロジックノード / 条件分岐
translationKey: logic-node-conditional-branching
description: ロジックノード(条件分岐)は、チャットボットや自動化ワークフローにおいて条件を評価し、ユーザー入力やコンテキストに基づいて動的にパスを振り分けます。
keywords: ["ロジックノード", "条件分岐", "チャットボット", "自動化", "ワークフロー"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: ろじっくのーど / じょうけんぶんき
reading: ロジックノード / 条件分岐
kana_head: ら
e-title: Logic Node / Conditional Branching
---
## Logic Nodeとは?

**Logic Node**(ロジックノード)は、チャットボットや[自動化ワークフロー](/ja/glossary/automated-workflows/)におけるモジュール式の判断ブロックで、条件(ユーザーの選択、変数、ステータスなど)を評価し、それに応じてフローを分岐させます。ロジックノードは、カスタムルールに基づいてワークフローが分岐する「判断ポイント」(条件分岐)です。

**別名:**
- 条件分岐ノード
- If/Then分岐
- Split Action([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))
- Condition Node([Noca AI](https://support.noca.ai/logic-nodes/))
- Switchノード
- Branchノード

**参考資料:**
- [Kore.ai Logic Node Documentation](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-logic-node/)
- [Yellow.ai Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)
- [HubSpot If/Then Branches](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)
- [Slack Conditional Branching](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic/)

## 条件分岐を使用する理由

ロジックノードにより、ワークフローは以下を実現できます:

- ユーザー入力やコンテキストに**動的に応答**
- 選択やデータに基づいて**ユーザーを特定のアクションにルーティング**
- **ビジネスルールの実装**(適格性チェック、エスカレーション、承認)
- **パーソナライズされた体験の提供**(タグ、ユーザープロパティ、履歴に基づく)
- 複雑なプロセスを自動化することで**手動介入を削減**

**例:**  
顧客が「問題を報告」を選択した場合、ボットは詳細を尋ねます。「注文ステータスを確認」を選択した場合は、注文情報を取得します。

**詳細:**  
- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic)

## ロジックノードの主要機能

1. **条件評価:**  
   変数、ユーザー入力、またはシステム状態を使用して、1つ以上の条件を定義します。

2. **分岐/フロー制御:**  
   どの条件が真であるかに基づいて、異なるノード/アクションにルーティングします。

3. **コンテキスト変数へのアクセス:**  
   会話またはワークフローコンテキスト内の変数を読み書きします。

4. **ネストされたロジック:**  
   多層またはネストされた条件のサポート(例:「Aの場合、Bをチェック。そうでなければCを実行」)。

5. **視覚的表現:**  
   ほとんどのプラットフォームは、ロジックノードの接続と設定のためのビジュアルエディタを提供します。

6. **ノーコード/ローコード設定:**  
   グラフィカルUIで設定可能ですが、高度なロジックはコードまたは疑似コードでサポートされる場合があります。

**参考資料:**  
- [Yellow.ai Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)
- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic)

## ロジックノードと分岐の種類

プラットフォームの提供内容には以下が含まれる場合があります:

- **If/Then分岐:** 二分岐(真/偽)。
- **Switch/Caseノード:** 離散値に基づく多方向分岐。
- **Split Actions:** ユーザー入力、変数、またはランダム化に基づく分岐([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))。
- **Conditionノード:** 汎用の真/偽評価器。
- **Loop、Break、Continue:** 反復ロジック用([Noca AI](https://support.noca.ai/logic-nodes/))。
- **ランダム分岐:** A/Bテストやランダム化されたフロー用。
- **多層分岐:** ネストまたは多層ロジック([Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder))。

## ロジックノードの追加と設定方法

### Kore.aiの例

Kore.aiのロジックノードは、Bot Actionノードの一部としてのみ追加できます。

**手順:**
1. 分岐を追加したいダイアログタスクを開きます。
2. **Bot Action**ノードを追加/展開します([Bot Action Nodeドキュメント](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/bot-action-node/))。
3. **Logic Node**を挿入します。  
   - **Component Properties**タブがデフォルトで表示されます。
   - ![Kore.aiでのロジックノードの追加](https://kore-wordpress.s3.us-east-2.amazonaws.com/developer.kore.ai/wp-content/uploads/20220921084031/add-logic-node-1024x456.gif)
4. 設定:
   - **Component Properties**で**Name**と**Display Name**を設定します。
   - 必要に応じて変数名前空間を割り当てます。
   - **Manage Context Variables**を使用して変数を定義/更新します(例:`_context.BotUserSession.<variable_name>_`)。
   - **Instance Properties**で、タグまたはダイアログ固有のメタデータを設定します。
   - **Connection Properties**で、エンティティ値、コンテキストオブジェクト、またはインテントに基づいて、次に実行されるノードを制御する条件文を定義します。
5. 保存し、視覚的に分岐を接続します。

**参考資料:**  
- [Kore.ai Logic Node Documentation](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-logic-node/)

### プラットフォーム非依存ガイド

ほとんどのプラットフォームは同様のパターンに従います:

1. ボット/自動化ビルダーを開きます(例:[Yellow.ai](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)、[HubSpot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)、[Slack](https://slack.com/blog/news/conditional-branching-workflow-builder)、[TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))。
2. 関連するフローまたはジャーニーに移動します。
3. ロジック/条件/分割ノードを追加します:
   - ノードパレットで**Logic**、**If/Then**、**Condition**、または**Split Action**を探します。
   - キャンバスにドラッグ&ドロップします。
4. 条件を定義します:
   - 評価するプロパティまたは変数を指定します。
   - 比較演算子(等しい、含む、>など)を設定します。
   - 一致させる値を入力します。
5. 分岐を次のステップに接続します。
6. プレビュー/テストツールを使用してフローをテストします。

**参考資料:**  
- [Yellow.ai Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)
- [HubSpot If/Then Branches](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)
- [TextIt: Introduction to Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)

## ロジックノードの設定とプロパティ

### Component Properties

- **Name:** 内部識別子。
- **Display Name:** ユーザーフレンドリーなラベル。
- **Variable Namespaces:** 変数のスコープ(タスクまたはノードレベルの分離)。
- **Manage Context Variables:** 会話コンテキスト内の変数を設定/更新します。

*Component Propertiesの変更は、ロジックノードのすべてのインスタンスに影響します。*

### Instance Properties

- **Tags:** トラッキング/セグメンテーション用のカスタムメタデータまたはタグ。
- **Dialog-Scoped Settings:** 現在のダイアログ/フロー固有の設定。

*Instance Propertiesは現在のノードインスタンスのみに影響します。*

### Connection Properties

- **Conditional Connections:** 条件に基づいて、次に実行されるノードを定義します。
- **Fallback Path:** 条件が満たされない場合のデフォルト分岐。
- **Intents/Entity Values:** 検出されたインテント/エンティティ値を分岐に使用します。

*一部のプラットフォームでは、ロジックノードの接続が特定のスコープに制限されます(例:Kore.aiのBot Actionノード内)。*

**参考資料:**  
- [Kore.ai Logic Node Documentation](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-logic-node/)
- [Yellow.ai Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)

## 条件文と構文

条件文は、分岐がどのように評価されるかを決定します。これらはUI経由で設定されるか、式として記述される場合があります。

**一般的な演算子:**
- equals (==)
- not equals (!=)
- contains
- greater than (>)
- less than (<)
- in(リストメンバーシップ)
- and、or、not(論理演算子)

**疑似コードの例:**
```pseudo
if (user_response == "yes") {
    go_to("ConfirmOrder");
} else if (user_response == "no") {
    go_to("CancelOrder");
} else {
    go_to("ClarifyIntent");
}
```

**プラットフォームUIの例:**
- [HubSpot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)では、**If/then branches**タブを使用して、ユーザー応答、プロパティ、またはエージェントの可用性に基づくルールを追加します。
- [Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)では、ドロップダウン値、フォーム応答、またはチャネルデータなどの基準を選択します。

## 実用的な使用シナリオ

**1. ユーザー応答の処理**  
「はい/いいえ」の回答、オプション選択、または自由テキストに基づいてユーザーをルーティングします。

**2. サポートリクエストのルーティング**  
サポートチケットを適切なチーム(例:技術、請求、機器)に振り分けます。

**3. 多段階承認**  
階層的な承認を実装します(例:マネージャー、次にディレクター)。

**4. パーソナライゼーション**  
ユーザータグやCRMプロパティに基づいて応答を表示します。

**5. データ検証**  
進行する前に、有効な電話番号、メール、または必須フィールドをチェックします。

**6. A/Bテスト**  
実験や機能展開のためにユーザーをランダムに分岐させます。

**7. エラー処理**  
無効/欠落した入力に対して、フォールバックまたは明確化パスにルーティングします。

**参考資料:**  
- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic)
- [TextIt: Introduction to Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)

## 実例:実際の条件分岐

### 例1:はい/いいえの判断
**シナリオ:** ボットが「通知を受け取りますか?」と尋ねます。
- ユーザー応答が「はい」の場合 → **通知を有効化**ノードに移動。
- それ以外 → **通知を無効化**ノードに移動。

### 例2:サポートリクエストのルーティング([Slack Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder))
**シナリオ:** ユーザーが問題タイプを含むサポートリクエストを送信します。
- `issue_type == "technical"`の場合 → `#tech-support`にルーティング
- `issue_type == "billing"`の場合 → `#billing-support`にルーティング
- `issue_type == "equipment"`の場合 → `#equipment-support`にルーティング

### 例3:クイック返信の分岐([HubSpot Bot](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows))
**シナリオ:** ボットが「何をお手伝いしましょうか?」と尋ねます。  
クイック返信:「注文ステータス」、「技術サポート」、「その他」
- **注文ステータス**の場合 → 注文検索に移動
- **技術サポート**の場合 → サポートに移動
- **その他**の場合 → 一般的な問い合わせ

### 例4:多層承認([Slack](https://slack.com/blog/news/conditional-branching-workflow-builder))
- `manager_approval == "approved"`の場合:
  - 財務ディレクターにルーティング。
  - `finance_approval == "approved"`の場合:調達に通知。
  - それ以外:却下を通知。
- それ以外:却下を通知。

### 例5:データ検証のためのSplit Action([TextIt](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/))
- 入力が有効な電話番号の場合 → 続行。
- それ以外 → エラーを送信し、再入力を促します。

## ベストプラクティスとヒント

- フォールバック(「else」)を含むすべての分岐を定義します。
- 明確性のために説明的なノード名を使用します。
- モジュール性のために関連するロジックをグループ化します。
- プレビュー/テストツールを使用してすべての分岐をテストします。
- 分析とパーソナライゼーションのために変数/タグを使用します。
- 過度にネストされたロジックを避け、複雑なロジックを小さなフローに分割します。
- コメントや説明を使用してビジネスルールを文書化します。

**参考資料:**  
- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic)
- [Kore.ai: Custom Meta Tags](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/custom-meta-tags/)

## 制限事項とエッジケース

- **スコープ制限:**  
  - Kore.aiでは、ロジックノードはBot Actionノード内にスコープされます。
- **グローバル設定 vs インスタンス設定:**  
  - Component Propertiesはグローバル、Instance Propertiesはローカルです。
- **ノード制限:**  
  - 一部のプラットフォームにはフローあたりのノード制限があります(例:Yellow.ai:150ノード)。
- **削除の依存関係:**  
  - 親ノードを削除する前に、アクティブな分岐を削除する必要があります(HubSpot)。
- **データ型の考慮事項:**  
  - 条件内のデータ型(文字列 vs 数値)は互換性がある必要があります。
- **ランダム/A/B分岐:**  
  - シード化やトラッキングなしでは予測不可能な結果になる可能性があります。

**参考資料:**
- [Yellow.ai Node Types](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes)
- [Kore.ai Managing Namespace](https://developer.kore.ai/docs/bots/bot-settings/bot-management/managing-namespace/)

## 関連概念と参考資料

- [Bot Action Node (Kore.ai)](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/bot-action-node/)
- [Yellow.ai Node Types](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes)
- [TextIt Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)
- [Slack Workflow Builder Guide](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Noca AI Logic Nodes](https://support.noca.ai/logic-nodes/)
- [HubSpot Chatflows](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)

## ソースリンクと参考資料

- [BotStacks: Use Conditions and Logic Branching](https://docs.botstacks.ai/common-tasks/conversation-design/conditions-logic/)
- [Kore.ai: Working with the Logic Node](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/working-with-the-logic-node/)
- [Yellow.ai: Logic Nodes](https://docs.yellow.ai/docs/platform_concepts/studio/build/nodes/logic-nodes)
- [HubSpot: If/Then Branches](https://knowledge.hubspot.com/chatflows/use-if-then-branches-with-chatflows)
- [Slack: Conditional Branching Workflow Builder](https://slack.com/blog/news/conditional-branching-workflow-builder)
- [TextIt: Introduction to Flows](https://help.textit.com/en/article/introduction-to-flows-1vmh15z/)
- [Kore.ai: Managing Namespace](https://developer.kore.ai/docs/bots/bot-settings/bot-management/managing-namespace/)
- [Kore.ai: Custom Meta Tags](https://developer.kore.ai/docs/bots/bot-builder-tool/dialog-task/custom-meta-tags/)
- [Slack: Workflow Builder Guide](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)
- [Noca AI: Logic Nodes](https://support.noca.ai/logic-nodes/)

**詳細については、常にプラットフォームの公式ドキュメントと開発者ガイドを参照してください。**
