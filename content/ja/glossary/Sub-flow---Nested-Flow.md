---
title: サブフロー / ネストフロー
translationKey: sub-flow-nested-flow
description: 自動化におけるサブフロー(ネストフロー)について学びます。ワークフローを他のワークフロー内に埋め込むことで、複雑なロジックを簡素化し、再利用性を高め、メンテナンスを改善します。
keywords: ["サブフロー", "ネストフロー", "ワークフロー自動化", "再利用性", "モジュラーワークフロー"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: さぶふろー / ねすとふろー
reading: サブフロー / ネストフロー
kana_head: か
e-title: Sub-flow / Nested Flow
---
## サブフロー / ネストされたフローとは?

**サブフロー**(または**ネストされたフロー**)とは、より大きな親ワークフロー内のステップとして呼び出される、自己完結型のワークフローです。このモジュラーパターンにより、複雑なビジネスロジックを分解し、一貫した再利用と簡素化されたメンテナンスが可能になります。サブフローはソフトウェアの関数に類似しており、複数のコンテキストで再利用可能な特定のロジックをカプセル化します。

- **例:** 従業員のオンボーディングでは、IT セットアップ、HR コンプライアンス、機器のプロビジョニング、アカウント作成をそれぞれ別のサブフローで処理します。各サブフローは一度開発され、必要な場所で呼び出されます。

**参考資料:**  
- [Microsoft Power Automate: サブフローの作成](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)  
- [ServiceNow: サブフローとワークフロー自動化](https://sn.works/CoE/StartFlow)  
- [AWS Step Functions: ネストされたワークフロー](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)

## サブフロー / ネストされたフローを使用する理由

### 主な利点

- **モジュール性:** 複雑なワークフローを管理可能な論理単位に分割します。
- **再利用性:** 共通ロジック(検証、通知、データ変換)を一度構築し、どこでも再利用できます。
- **保守性:** サブフローの変更がすべての親ワークフローに即座に反映され、リスクとオーバーヘッドを削減します。
- **スケーラビリティ:** 小さく明確に定義されたピースを組み合わせることで、大規模な自動化の成長と適応が容易になります。
- **一貫性:** 同一のプロセスがすべてのワークフローで統一的に実行されます。
- **セキュリティの強化:** 機密性の高いロジックへのアクセスが分離され、権限によって保護されます。
- **エラー処理の改善:** サブフローに集中型のエラー管理を適用し、信頼性の高い復旧と統一されたログ記録を実現します。

**参考資料:**  
- [ServiceNow Flow Designer ドキュメント](https://docs.servicenow.com/csh?version=latest&topicname=flow-designer)  
- [AWS Step Functions ドキュメント](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html)

## サブフロー / ネストされたフローの仕組み

### ステップバイステップのプロセス

1. **サブフローの設計:**  
   繰り返し可能なロジック(データ検証、通知など)を特定し、定義された入出力を持つスタンドアロンのワークフローとして構築します。

2. **親ワークフローとの統合:**  
   必要なステップでサブフローを呼び出し、必要なデータを入力として渡します。

3. **実行:**  
   親ワークフローがサブフローをトリガーし、単一の操作として実行されます。実行は同期(親が待機)または非同期(親が継続)の場合があります。

4. **状態と結果の管理:**  
   サブフローの結果が返され、後続の処理で利用可能になります。状態はサブフロー内で管理されますが、必要に応じて親コンテキストにアクセスできます。

5. **ワークフロー間での再利用性:**  
   同じサブフローを複数の親ワークフローから呼び出すことができ、標準化と迅速な開発をサポートします。

**プラットフォームの例:**

- **Microsoft Power Automate for Desktop:**  
  サブフローは Excel、Web、または Windows のアクションを自動化し、メインワークフロー内で呼び出されます。  
  [チュートリアル](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)

- **ServiceNow Workflow Studio:**  
  サブフロー、アクション、テンプレートを再利用可能なロジックとして構築し、任意のフローで呼び出します。  
  [Workflow Studio ドキュメント](https://docs.servicenow.com/csh?version=latest&topicname=workflow-studio)

- **AWS Step Functions:**  
  親ステートマシンが子(ネストされた)ワークフローをオーケストレーションし、複雑な階層とドメイン分離をサポートします。  
  [AWS Step Functions ドキュメント](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html)

## 親ワークフロー vs. サブフロー: 主要な用語

- **親ワークフロー:** プロセスを制御するメイン自動化で、サブフローをステップとして呼び出します。
- **サブフロー / ネストされたフロー:** 親ワークフロー内で実行される、包含された再利用可能なワークフローです。
- **再利用可能なコンポーネント:** 繰り返し使用するために設計されたモジュラーワークフローまたはサブフローです。
- **状態遷移:** サブフローの呼び出しとその結果の処理を含む、ワークフロー状態間の移動です。
- **エラー処理:** サブフローの障害を管理し、問題を親に伝播して復旧するメカニズムです。

## 重要性と価値提案

- **冗長性の削減:** コードの重複を排除し、ロジックを一元的に更新します。
- **更新の一元化:** 一つの変更ですべての依存ワークフローが更新されます。
- **複雑なロジックの簡素化:** 大規模なワークフローの理解とデバッグが容易になります。
- **チームコラボレーションのサポート:** チームが個別のサブフローを所有し、ドメインの専門知識と分散メンテナンスを可能にします。
- **高度なパターンの実現:**  
  - **並列実行:** 複数のサブフローを同時に呼び出します。
  - **条件付きロジック:** 実行時の条件に基づいてサブフローを呼び出します。
  - **ループ処理:** 条件が満たされるまでサブフローを繰り返し実行します。
  - **一時停止/再開:** サブフローの境界でワークフローを一時停止および再開します。

**AWS Step Functions の実世界での価値:**  
ワークフローをサブフローに分解することで、月次コストが削減され、エラーの分離、デバッグ、運用メトリクスが改善されました([AWS の完全な比較](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/))。

## 一般的なユースケース

1. **人事(HR):**
   - **オンボーディング:** IT セットアップ、HR 書類作成、コンプライアンスのサブフロー。
   - **採用:** スクリーニング、面接スケジューリング、オファー作成。

2. **財務:**
   - **支払い処理:** 信用チェック、不正検出、取引ログのサブフロー。
   - **請求書管理:** 検証、承認ルーティング、払い戻し。

3. **カスタマーサポート:**
   - **チケット受付:** データ検証とアカウントチェックのサブフロー。
   - **エスカレーション:** 異なるエスカレーションパスのサブフロー。

4. **マーケティング:**
   - **キャンペーン自動化:** セグメンテーション、パーソナライゼーション、メール配信のサブフロー。

5. **コンプライアンスと監査:**
   - **監査準備:** ドキュメント収集、自己チェック、完了追跡。
   - **インシデント管理:** 通知、調査、報告。

6. **オペレーション:**
   - **在庫管理:** 在庫更新、再注文トリガー、サプライヤー検証。

**例:**  
「信用チェック」サブフローは、ローン申請と新規顧客オンボーディングの両方で再利用され、一貫したコンプライアンスと検証ロジックを保証します。

## 技術パターンと機能

### プラットフォーム実装

- **Microsoft Power Automate:**  
  サブフローは Web/デスクトップアクションを自動化し、結果を返し、エラーを一元的に処理します。  
  [ガイド](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)

- **ServiceNow Workflow Studio:**  
  フロー、サブフロー、カスタムアクションの統合ビルダー。デバッグ、バージョニング、LLM を活用した会話型フローをサポートします。  
  [リリースノート](https://www.servicenow.com/docs/bundle/zurich-release-notes/page/release-notes/now-platform-app-engine/flow-designer-rn.html)

- **AWS Step Functions:**  
  - **親子パターン:** 親ワークフローがサブフロー(子ワークフロー)をオーケストレーションし、それぞれがドメインまたは操作に焦点を当てます。
  - **ドメイン分離:** 支払い、在庫、配送などの個別のワークフロー。
  - **共有ユーティリティ:** 通知、ログ記録、検証のための再利用可能なサブフロー。
  - **エラーワークフロー:** 一貫性と保守性のための集中型エラー処理サブフロー。

**AWS コードスニペットの例(TypeScript 風):**
```typescript
const nestedWorkflow = new LegacyWorkflow({ name: "nested-workflow" })
  .step(stepA)
  .then(stepB)
  .commit();

const parentWorkflow = new LegacyWorkflow({ name: "parent-workflow" })
  .step(nestedWorkflow)
  .then(stepC)
  .commit();
```
- [AWS の追加例とガイダンス](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)

### 主要なプラットフォーム機能

- 呼び出しと結果の受け渡し
- 並列サブフロー実行
- 条件分岐
- 長時間実行フローの一時停止/再開
- 状態監視とエラー伝播

## モノリシック vs. モジュラー(ネストされた)ワークフローアプローチ

| 側面               | モノリシックワークフロー                   | モジュラー/ネストされたワークフロー                  |
|----------------------|---------------------------------------|------------------------------------------|
| **保守性**  | 更新が困難、密結合  | 更新が容易、疎結合          |
| **再利用性**      | 低い(冗長なロジック)                 | 高い(一元化された共通ロジック)          |
| **エラー処理**   | エラーの分離と追跡が困難      | 一元化され、管理が容易            |
| **スケーラビリティ**      | 複雑さによって制限される                 | サブフローの組み合わせで容易にスケール     |
| **デバッグ**        | 状態爆発により複雑      | 分離されたエラードメインでシンプル     |
| **バージョニング**       | フロー全体の再デプロイが必要  | 個別のサブフローを独立して更新|

**出典:**  
- [AWS Compute ブログ: Step Functions のモジュール化](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)

## サブフロー / ネストされたフローのベストプラクティス

1. **モジュール性を考慮した設計:** 関連するステップをカプセル化し、「神」サブフローを避けます。
2. **命名規則:** 明確さと追跡可能性のために説明的な名前を使用します。
3. **入出力契約:** 期待されるデータを明確に定義し、スキーマまたは型を使用します。
4. **エラー処理:** エラーロジックを一元化し、親にエラーを伝播します。
5. **状態管理:** サブフローに独自の状態を管理させ、必要に応じて親コンテキストにアクセスします。
6. **アクセス制御:** 機密性の高いサブフローの権限を制限します。
7. **テストとバージョニング:** 独立してコンテキスト内でテストし、破壊的変更を避けるためにサブフローをバージョン管理します。
8. **ドキュメント:** 保守性のためにインターフェース、ロジック、使用方法を文書化します。

**参考資料:**  
- [ServiceNow: ガイダンスとベストプラクティス](https://sn.works/CoE/StartFlow#h_320418873381665150474199)  
- [AWS Step Functions ベストプラクティス](https://docs.aws.amazon.com/step-functions/latest/dg/best-practices.html)

## サブフロー / ネストされたフローに関する FAQ

**Q: ネストされたフローは複数ステップのワークフローとどう違いますか?**  
A: 複数ステップのワークフローは線形ですが、ネストされたフローは再利用可能なワークフローをコンポーネントとして呼び出します。

**Q: サブフローは並列実行できますか?**  
A: はい、ほとんどのプラットフォームは同時サブフロー実行をサポートしています。

**Q: エラーはどのように処理されますか?**  
A: エラーは上位に伝播し、親ワークフローは再試行、中止、またはエスカレーションできます。

**Q: サブフローは親データにアクセスできますか?**  
A: 定義された入力を受け取ります。より広範なアクセスはプラットフォームのセキュリティ設定に依存します。

**Q: 多くのワークフローで使用されているサブフローを更新するにはどうすればよいですか?**  
A: サブフロー定義を更新すると、すべての親ワークフローが即座に最新バージョンを使用します。

**Q: サブフローが一時停止またはポーズされた場合はどうなりますか?**  
A: 親ワークフローは待機し、必要に応じて再開できます。人間参加型プロセスをサポートします。

**Q: サブフローは複数レベルの深さでネストできますか?**  
A: はい、複雑な階層をサポートします。

## トラブルシューティングとヒント

- **サブフローが予期せず失敗する:** 入力データとパラメータを確認し、エラー処理を見直します。
- **並列サブフローがパフォーマンスを低下させる:** リソース使用状況を監視し、必要に応じてバッチ処理またはスロットリングを行います。
- **結果マッピングが不明確:** 出力を明示的に文書化し、スキーマを使用します。
- **バージョニングの問題:** バージョン管理を実装し、破壊的変更を慎重に管理します。

## 権威あるリソースと参考資料

- [Activepieces 用語集 – ネストされたフロー](https://resources.activepieces.com/glossary/nested-flows)  
- [Way We Do ブログ – サブプロセスの紹介](https://www.waywedo.com/blog/introducing-sub-processes/)  
- [Mastra ドキュメント – ネストされたワークフロー(レガシー)](https://mastra.ai/docs/workflows-legacy/nested-workflows)  
- [AWS Compute ブログ – Step Functions ワークフローのモジュール化](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)  
- [Microsoft Power Automate: サブフローワークショップ](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)  
- [ServiceNow Flow Designer ドキュメント](https://docs.servicenow.com/csh?version=latest&topicname=flow-designer)  

## 詳細なプラットフォームチュートリアルとビデオ

- **Microsoft Power Automate for Desktop:**  
  [サブフローと Web 自動化の作成(公式チュートリアル)](https://learn.microsoft.com/en-us/training/modules/create-subflows-web-automation-online-workshop/)

- **ServiceNow: 会話型 AI のサブフロー**  
  [YouTube – Now Assist 会話からサブフローを実行](https://www.youtube.com/watch?v=jbRhPq6jREY)

## 技術図とバージョンノート

- [ServiceNow Zurich リリース: サブフローとアクション](https://www.servicenow.com/docs/bundle/zurich-release-notes/page/release-notes/now-platform-app-engine/flow-designer-rn.html)
- [AWS Step Functions: 親子ステートマシン図](https://aws.amazon.com/blogs/compute/breaking-down-monolith-workflows-modularizing-aws-step-functions-workflows/)

*プラットフォーム固有のガイダンスと高度なアーキテクチャパターンについては、上記のリソースを参照してください。サブフローの実装は、エンタープライズと中小企業の両方の設定において、スケーラブルで保守可能で回復力のあるワークフロー自動化の基本です。*