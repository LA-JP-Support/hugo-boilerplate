---
title: オートスケーリング
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: autoscaling
description: オートスケーリングは、リアルタイムの需要に基づいてクラウドコンピューティングリソース(VM、コンテナ)を自動的に調整し、パフォーマンス、可用性、コスト効率を最適化します。
keywords:
- オートスケーリング
- クラウドコンピューティング
- リソース割り当て
- 水平スケーリング
- 垂直スケーリング
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Autoscaling
term: オートスケーリング
url: "/ja/glossary/Autoscaling/"
---
## オートスケーリングとは?

オートスケーリングは、リアルタイムのワークロード需要とポリシー駆動型ルールに基づいて、計算リソース(仮想マシン、コンテナ、サーバーレス関数、ストレージ)を自動的に割り当てまたは解放するクラウドコンピューティング機能です。この弾力性により、アプリケーションは一貫した可用性とパフォーマンスを維持しながら、過剰プロビジョニングと低利用率を削減することでコストを最小化します。

クラウドプロバイダー(AWS、Azure、Google Cloud、IBM、Oracle)は、コンピューティング、メモリ、その他のサービスに対する動的なリソース割り当てを可能にする中核機能として、オートスケーリングを提供しています。

## オートスケーリングの仕組み

<strong>主要コンポーネント</strong>

<strong>起動設定</strong>- 新しいリソースのプロビジョニング方法を定義
- AMI、インスタンスタイプ、ストレージ、ネットワーキング、セキュリティ、IAMロール、ブートストラップスクリプトを指定

<strong>Auto Scaling Group (ASG)</strong>- 一緒に管理されるリソースの論理グループ
- 最小、最大、希望容量を設定

<strong>スケーリングポリシー</strong>- リソースの追加/削除のタイミングと方法を制御するルール
- タイプ:ターゲット追跡、ステップスケーリング、シンプルスケーリング、スケジュールスケーリング
- CPU、メモリ、ネットワークI/O、リクエスト数、カスタムメトリクスによってトリガー

<strong>ヘルスチェック</strong>- EC2およびELBチェックを使用してインスタンスの健全性を継続的に監視
- 不健全なインスタンスを自動的に終了して置き換え

<strong>容量設定</strong>- 希望容量:目標インスタンス数
- 最小容量:維持される最低数
- 最大容量:過剰プロビジョニングを防ぐ上限

<strong>インスタンスタイプと購入オプション</strong>- 複数のインスタンスタイプをサポート
- 購入モデル:オンデマンド、リザーブド、スポットインスタンス

<strong>アベイラビリティゾーン</strong>- 高可用性のために複数のAZ間でインスタンスを分散
- 有効化されたゾーン間でインスタンスをバランス

<strong>Elastic Load Balancing統合</strong>- 健全なASGインスタンス間でトラフィックを分散
- タイプ:ALB、NLB、CLB
- インスタンスを自動的に登録/登録解除

<strong>ライフサイクルフック</strong>- 特定のライフサイクルポイントでカスタムスクリプトを実行
- 設定、ドレイン、クリーンアップタスクを処理

<strong>プロセス</strong>1. <strong>監視</strong>:すべてのリソースからリアルタイムメトリクスを収集
2. <strong>評価</strong>:メトリクスをスケーリングポリシーのしきい値と比較
3. <strong>決定</strong>:スケールアウト(追加)またはスケールイン(削除)アクションを決定
4. <strong>アクション</strong>:インスタンスをプロビジョニングまたは終了
5. <strong>ヘルスチェックとフック</strong>:新しいリソースを検証して設定
6. <strong>クールダウン</strong>:さらなるスケーリングの前に安定化を待機
7. <strong>フィードバックループ</strong>:ワークロードの進化に応じて継続的に繰り返し

## オートスケーリングのタイプ

<strong>水平スケーリング(スケールアウト/イン)</strong>- リソースインスタンスの数を調整
- 例:トラフィック急増時にWebサーバーを追加
- 利点:ダウンタイムなし、高いスケーラビリティ、フォールトトレランスの向上
- 最適用途:マイクロサービス、Webアプリ、API、コンテナ

<strong>垂直スケーリング(スケールアップ/ダウン)</strong>- 既存インスタンスのリソース割り当てを変更
- 例:VMを2 vCPU/8GBから8 vCPU/32GBに増強
- 利点:モノリシックまたはステートフルアプリケーションに有用
- 制限:ダウンタイムが必要な場合あり、ハードウェアによる制限
- 最適用途:レガシーアプリ、データベース、非分散ワークロード

| 側面 | 水平 | 垂直 |
|--------|-----------|----------|
| 変更内容 | インスタンス数 | インスタンスサイズ |
| ダウンタイム | 通常なし | 時々あり |
| スケーラビリティ | 高い(無制限) | ハードウェアによる制限 |
| 最適用途 | ステートレス、分散型 | ステートフル、モノリシック |

## スケーリングポリシー

<strong>しきい値ベース(リアクティブ)</strong>- メトリクスが定義されたしきい値を超えたときにトリガー
- 例:CPUが5分間80%超

<strong>ターゲット追跡</strong>- 特定のメトリクスの目標値を維持
- 例:平均CPUを60%に保つ

<strong>予測型(プロアクティブ)</strong>- 履歴パターンまたはMLを使用して需要を予測
- 予想されるスパイクに先立ってスケール

<strong>スケジュールスケーリング</strong>- 事前に決められた時間にリソースをスケール
- 例:営業時間中にスケールアップ

<strong>手動スケーリング</strong>- 管理者制御の調整
- フォールバックまたは計画されたイベントに使用

## 主な利点

<strong>パフォーマンス最適化</strong>- 需要急増時にアプリケーション速度を維持
- 速度低下や停止を防止

<strong>コスト効率</strong>- アイドルリソースへの支払いを排除
- クラウドの無駄を削減

<strong>可用性と信頼性の向上</strong>- 障害が発生したリソースを自動的に置き換え
- サービス継続性を維持

<strong>運用の俊敏性</strong>- 手動介入なしで動的なワークロード変化に対応

<strong>ユーザーエクスペリエンス</strong>- 一貫したサービス品質
- パフォーマンス低下を防止

<strong>エネルギー効率</strong>- 不要な電力消費を最小化

## 一般的な課題

<strong>設定の複雑さ</strong>- 効果的なポリシーを設計するには専門知識が必要

<strong>反応の遅延</strong>- プロビジョニング時間により、急激なスパイク時にパフォーマンス遅延が発生する可能性

<strong>メトリクス選択</strong>- 非効果的な選択(例:メモリがボトルネックの場合にCPU)は非効率を引き起こす

<strong>コストの予期しない増加</strong>- 過度に積極的なスケーリングまたは設定ミスにより予期しない費用が発生

<strong>アプリケーション設計の制約</strong>- ステートレスで水平スケーラブルなアーキテクチャに最も効果的

<strong>監視と可観測性</strong>- 可視性の低さはスケーリング問題を不明瞭にする

## 実世界のユースケース

<strong>Eコマースプラットフォーム</strong>- ブラックフライデーのトラフィック急増には追加サーバーが必要
- 可用性と高速チェックアウトを確保

<strong>メディアストリーミングサービス</strong>- バイラルイベントにより同時視聴者が増加
- スムーズな再生のためにストリーミングサーバーをスケール

<strong>SaaSスタートアップ</strong>- バイラルマーケティングにより突然のユーザー増加
- 過剰プロビジョニングなしでバックエンドをスケール

<strong>ビッグデータとAI/MLワークロード</strong>- モデルトレーニングには変動するコンピューティングが必要
- 並列処理のためにクラスターをスケール

<strong>APIとマイクロサービス</strong>- エンドポイント間で変動するリクエストレート
- 各サービスが独立してオートスケール

## ベストプラクティス

- <strong>主要メトリクスの監視</strong>:堅牢なツールでCPU、メモリ、アプリケーションメトリクスを追跡
- <strong>明確なポリシーの定義</strong>:保守的に開始し、シミュレートされた負荷下でテスト
- <strong>クールダウンの実装</strong>:スラッシングを避けるために安定化期間を設定
- <strong>ステートレスサービスの設計</strong>:セッション状態を外部に保存
- <strong>AZ間での分散</strong>:リソースを分散して回復力を向上
- <strong>定期的なレビュー</strong>:スケーリングアクションを分析してポリシーを調整
- <strong>クラウドクォータの理解</strong>:プロバイダーの制限を把握し、積極的に増加を要求
- <strong>戦略の組み合わせ</strong>:既知のパターンには予測型/スケジュール型を使用し、バックアップとしてリアクティブを使用
- <strong>アラートの設定</strong>:予期しないイベントやコスト急増の通知を設定

## オートスケーリング vs. ロードバランシング

| 側面 | オートスケーリング | ロードバランシング |
|--------|------------|----------------|
| 目的 | リソース数/サイズを調整 | トラフィックを分散 |
| 機能 | インスタンスを追加/削除 | リクエストをサーバーにルーティング |
| トリガー | メトリクスまたはスケジュール | 各リクエスト |
| 影響 | 容量を変更 | 利用率を最適化 |
| 範囲 | インフラストラクチャレベル | ネットワーク/アプリケーションレベル |
| 例 | CPU > 70%時に5台のVMを追加 | HTTPを最も負荷の低いVMにルーティング |

オートスケーリングは弾力的な容量を提供し、ロードバランシングは効率的なトラフィック分散を保証します。

## クラウドプロバイダーの機能

| プロバイダー | サービス | 主な機能 |
|----------|---------|--------------|
| <strong>AWS</strong>| EC2 Auto Scaling、Application Auto Scaling | EC2、ECS、DynamoDB、Aurora;ターゲット/予測/スケジュールポリシー |
| <strong>Azure</strong>| VM Scale Sets、Azure Autoscale | VM、App Services;メトリクスベースおよびスケジュール |
| <strong>GCP</strong>| Managed Instance Groups、GKE Cluster Autoscaler | Compute Engine、Kubernetes;カスタムメトリクス、HTTP負荷 |
| <strong>IBM Cloud</strong>| VPC Auto Scaling、Kubernetes Autoscaler | VM、Kubernetesクラスター |
| <strong>Oracle Cloud</strong>| Instance Pools & Autoscaling | コンピューティングプール;メトリクスベースおよびスケジュール |

## よくある質問

<strong>良いオートスケーリング戦略とは?</strong>予測可能なワークロードにはターゲット追跡から始め、既知のパターンには予測型を組み合わせ、セーフティネットとしてリアクティブを使用します。

<strong>オートスケーリングでどれくらい節約できますか?</strong>節約額はワークロードによって異なりますが、インフラストラクチャコストの30〜50%の削減が一般的です。

<strong>オートスケーリングはコンテナで機能しますか?</strong>はい。Kubernetesおよびコンテナオーケストレーションプラットフォームは、ポッドとノードに対する堅牢なオートスケーリングを提供します。

<strong>どのメトリクスを監視すべきですか?</strong>CPU、メモリ、ネットワークスループット、アプリケーション固有のメトリクス(リクエスト数、キュー深度、データベース接続)。

## 参考文献


1. IBM. (n.d.). What is Auto Scaling?. IBM Think Topics. URL: https://www.ibm.com/think/topics/autoscaling

2. AWS. (n.d.). Auto Scaling Overview. AWS Documentation. URL: https://aws.amazon.com/autoscaling/

3. DigitalOcean. (n.d.). Cloud Auto Scaling Techniques. DigitalOcean Community Tutorials. URL: https://www.digitalocean.com/community/tutorials/auto-scaling-techniques-guide

4. Datadog. (n.d.). Auto-scaling Knowledge Center. Datadog Knowledge Base. URL: https://www.datadoghq.com/knowledge-center/auto-scaling/

5. GeeksforGeeks. (n.d.). What is Auto Scaling?. GeeksforGeeks System Design. URL: https://www.geeksforgeeks.org/system-design/what-is-auto-scaling/

6. Hydrolix. (n.d.). Autoscaling in Cloud Computing. Hydrolix Glossary. URL: https://hydrolix.io/glossary/autoscaling/

7. Middleware. (n.d.). What is Autoscaling?. Middleware Blog. URL: https://middleware.io/blog/what-is-autoscaling/

8. Zesty. (n.d.). Autoscaling Glossary. Zesty FinOps Glossary. URL: https://zesty.co/finops-glossary/autoscaling/
