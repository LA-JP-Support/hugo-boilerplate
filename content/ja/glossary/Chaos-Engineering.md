---
title: カオスエンジニアリング
date: 2025-11-25
translationKey: chaos-engineering
description: カオスエンジニアリングは、システムの弱点を発見し、その回復力に対する信頼性を構築するために、意図的にシステムに実験を行う手法です。脆弱性を事前に特定する方法を学びましょう。
keywords: ["カオスエンジニアリング", "システムレジリエンス", "障害注入", "分散システム", "SRE"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Chaos Engineering
term: かおすえんじにありんぐ
reading: カオスエンジニアリング
kana_head: か
---
## 定義

カオスエンジニアリングは、制御された障害を意図的に注入することで、ソフトウェアシステムの弱点を発見し、レジリエンスを向上させることに焦点を当てた構造化された規律です。システムをランダムに破壊するのではなく、科学的で仮説駆動型の実験を通じて、システムの動作に関する仮定を検証し、インシデントになる前に脆弱性を積極的に特定します。特に分散型、クラウドネイティブ、マイクロサービスベースのアーキテクチャにおいて重要であり、これらの環境では創発的な相互作用と依存関係により障害の予測が困難になります。

- [IBM: What is Chaos Engineering?](https://www.ibm.com/think/topics/chaos-engineering)
- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- [eG Innovations: What is Chaos Engineering?](https://www.eginnovations.com/glossary/chaos-engineering)
- [phoenixNAP: Chaos Engineering – Definition, Principles, Best Practices](https://phoenixnap.com/blog/chaos-engineering)

## カオスエンジニアリングの使用方法

カオスエンジニアリングは、さまざまなIT環境で適用されます:

- **分散システム:** 1つのサービスやノードの障害が複雑なアーキテクチャ全体にどのように波及するかを特定するため([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering))。
- **クラウドネイティブアプリケーション:** オートスケーリング、一時的なインフラストラクチャ、マネージドサービスを持つ環境でのレジリエンスを検証するため([IBM](https://www.ibm.com/think/topics/chaos-engineering))。
- **本番環境:** 実際のトラフィックでの制御された実験は最も現実的な洞察をもたらしますが、慎重な影響範囲の管理が必要です([eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering))。
- **本番前/テスト環境:** カオスプラクティスに不慣れなチームにとって安全な出発点。
- **CI/CDパイプライン:** カオステストを組み込むことで、新しいコードやインフラストラクチャの変更がシステムのレジリエンスを低下させないことを保証します。

**主な実践者:** サイトリライアビリティエンジニア(SRE)、DevOpsおよびプラットフォームチーム、QA/パフォーマンスエンジニア、セキュリティ/インシデント対応チーム。

**類推:**  
カオスエンジニアリングは、しばしば防災訓練(システムとチームが準備できるように緊急事態をシミュレート)やワクチン(免疫を構築するために制御された「用量」の障害を導入)に例えられます。

## 中核原則

カオスエンジニアリングは、実験が科学的、制御的、価値あるものであることを保証する原則に基づいています([Principles of Chaos Engineering](https://principlesofchaos.org/)):

1. **定常状態に関する仮説を構築する:**  
   観測可能なメトリクス(エラー率、レイテンシ、スループット)で「正常な」システム動作を定義します。
2. **現実世界のイベントをシミュレートする:**  
   もっともらしい障害を注入します:サーバークラッシュ、ネットワーク分断、依存関係の停止、負荷スパイク。
3. **本番環境で実験を実行する(安全な場合):**  
   本番実験は、真のユーザートラフィックと依存関係を反映します。最小限の影響範囲から始め、信頼が高まるにつれて拡大します。
4. **自動化して継続的に実行する:**  
   自動化により、システムが進化してもレジリエンスが維持されます([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering))。
5. **影響範囲を最小化する:**  
   サービスやユーザーのサブセットをターゲットにし、[フィーチャーフラグ](/ja/glossary/feature-flags/)を使用し、時間制限を設定し、明確な中止/ロールバック手順を確立します。

## カオスエンジニアリングの方法論

カオスエンジニアリングは、科学的で反復的なアプローチに従います([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering)、[IBM](https://www.ibm.com/think/topics/chaos-engineering)):

1. **定常状態とKPIを定義する:**  
   健全なシステム動作を表すベースラインメトリクス(例:レイテンシ、エラー率、可用性)を確立します。
2. **仮説を立てる:**  
   明確でテスト可能な声明を作成します(例:「サービスXが失敗しても、ユーザーログイン率は影響を受けない」)。
3. **実験を計画する:**  
   どの障害を注入するか、どのコンポーネントをターゲットにするか、システムの応答をどのように監視するかを決定します。
4. **安全対策を準備する:**  
   堅牢な可観測性、アラート、ロールバック/中止制御を確保します。ステークホルダーとコミュニケーションを取ります。
5. **実験を実行する:**  
   ツールを使用して制御された方法で障害を注入します(例:プロセスを終了する、レイテンシを導入する)。
6. **監視してデータを収集する:**  
   実験中/後のメトリクス、ログ、トレース、アプリケーションの動作を観察します。
7. **結果を分析する:**  
   実際のシステム動作を仮説と比較し、発見事項、予期しない動作、パフォーマンスの問題を文書化します。
8. **改善して反復する:**  
   発見された弱点に対処し、将来の実験の範囲や複雑さを拡大します。

**例:**  
サードパーティの決済サービスに依存するeコマースアプリケーションが停止をシミュレートします。仮説は、システムが注文をキューに入れ、ユーザーに通知するというものです。代わりに、テストは未処理の例外を明らかにし、改善されたエラー処理とさらなる検証を促します([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering))。

## カオスエンジニアリング実験の種類

カオス実験は、現実世界の障害シナリオをシミュレートします([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering)、[eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering)):

- **レイテンシ注入:** ネットワーク通信やサービス応答を人為的に遅延させます。
- **障害注入:** サーバークラッシュ、プロセス終了、ハードウェア障害などのエラーを強制します。
- **負荷生成:** トラフィックスパイクをシミュレートして、スケーリングとオートスケーリングメカニズムをテストします。
- **リソース枯渇:** リソース(CPU、メモリ、ディスク、ネットワーク)を消費して、ストレス動作を観察します。
- **ネットワーク分断/停止:** ネットワーク障害、パケット損失、スプリットブレインシナリオをシミュレートします。
- **依存関係障害シミュレーション:** 外部API、データベース、マイクロサービスを利用不可または遅延させます。
- **カナリアテスト:** 完全なロールアウト前に、ユーザー/サービスのサブセットに変更をデプロイして影響を検証します。
- **セキュリティカオスエンジニアリング:** セキュリティインシデントをシミュレートして、検出と対応をテストします([Gremlin's Security Chaos Engineering](https://www.gremlin.com/chaos-engineering/security/)を参照)。

## 一般的なツールとテクノロジー

オープンソースおよび商用ツールが幅広く利用可能です([eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering#section4)、[phoenixNAP](https://phoenixnap.com/blog/chaos-engineering)):

- **Chaos Monkey:** Netflixのクラウドインスタンスをランダムに終了するオリジナルツール([Netflix Chaos Monkey](https://netflix.github.io/chaosmonkey/))。
- **Gremlin:** 幅広い制御された障害と統合を提供する商用プラットフォーム([Gremlin](https://www.gremlin.com/chaos-engineering))。
- **Chaos Toolkit:** カオス実験のためのオープンソースで拡張可能なフレームワーク([Chaos Toolkit](https://chaostoolkit.org/))。
- **Chaos Mesh:** コンテナ化環境での障害をシミュレートするKubernetesネイティブプラットフォーム([Chaos Mesh](https://chaos-mesh.org/))。
- **Pumba:** Dockerコンテナ用のオープンソースツール(ネットワーク遅延、パケット損失、再起動)([Pumba](https://github.com/alexei-led/pumba))。
- **LitmusChaos:** Kubernetesカオステスト用のCNCFプロジェクト([LitmusChaos](https://litmuschaos.io/))。
- **AWS Fault Injection Simulator (FIS):** カオステスト用のマネージドAWSサービス([AWS FIS](https://aws.amazon.com/fis/))。
- **Google DiRT:** Googleの内部災害テストプログラム([Google SRE Book - DiRT](https://sre.google/sre-book/disaster-testing-dirt/))。

## 例とユースケース

### 業界の例

- **Netflix:** クラウドベースのグローバルストリーミングサービスのレジリエンスを検証するために、Chaos MonkeyとSimian Armyを開発しました([Netflix Tech Blog](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116))。
- **Amazon (AWS):** AWS Fault Injection Simulatorと内部プラクティスを使用して、クラウドサービスの信頼性を確保しています([AWS FIS](https://aws.amazon.com/fis/))。
- **Google:** データセンター全体のシャットダウンをシミュレートするなど、DiRT(Disaster Recovery Testing)演習を実施しています([Google SRE Book](https://sre.google/sre-book/disaster-testing-dirt/))。

### 典型的なユースケース

- **オートスケーリングとフェイルオーバーの検証:** 障害後にトラフィックが正常なノードに再ルーティングされることを確認します。
- **災害復旧訓練:** 停止や地域的な障害をシミュレートします。
- **インシデント対応の検証:** SRE GameDaysの一環として、検出と修復を実践します([GameDay at Gremlin](https://www.gremlin.com/gameday/))。
- **規制コンプライアンス:** 金融、医療、その他の規制対象セクターのレジリエンスを実証します。
- **単一障害点の特定:** 冗長性のない重要な依存関係を明らかにします。
- **CI/CDの安全性:** 本番デプロイ前にリグレッションを捕捉します。

## メリット

カオスエンジニアリングは重要なメリットをもたらします([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering)、[eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering#section6)、[IBM](https://www.ibm.com/think/topics/chaos-engineering)):

- **システムレジリエンスの向上:** 弱点を積極的に特定して解決します。
- **ダウンタイムと停止コストの削減:** より迅速な検出、診断、復旧。
- **インシデント対応の強化:** チームが障害への対処経験を積みます。
- **スケーラビリティとパフォーマンスの向上:** ボトルネックとスケーリングの問題が明らかになります。
- **文化的変革:** 障害から学ぶ文化を奨励します。
- **規制/契約コンプライアンス:** 災害復旧と事業継続性の証拠を提供します。
- **顧客の信頼:** 停止の減少、より迅速な復旧、より良いユーザーエクスペリエンス。

## 課題とリスク

カオスエンジニアリングに関連するリスクと課題([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering)、[eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering#section7)):

- **組織的な抵抗:** 本番システムを「壊す」ことへの躊躇。
- **顧客への潜在的な影響:** 範囲が不適切な実験は実際の停止を引き起こす可能性があります。
- **分散システムの複雑さ:** カスケード障害の予測が困難。
- **定常状態の定義:** 関連するメトリクスの特定と監視が困難。
- **リソース要件:** 熟練した人材、可観測性、インフラストラクチャが必要。
- **安全性の懸念:** 中止、ロールバック、コミュニケーション手順が重要。

## ベストプラクティス

推奨されるベストプラクティス([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering)、[IBM](https://www.ibm.com/think/topics/chaos-engineering)、[eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering#section6)):

- **小さく始める:** 非クリティカルまたは本番前環境から始めます。
- **監視とロールバックを自動化する:** 可観測性と自動化を使用して迅速な復旧を実現します。
- **影響範囲を最小化する:** サービスやユーザーの小さなサブセットをターゲットにします。
- **明確にコミュニケーションする:** 実験を実行する前にすべてのステークホルダーに通知します。
- **CI/CDと統合する:** カオステストをデプロイサイクルの定期的な部分にします。
- **学びを文書化して共有する:** 徹底的な記録とポストモーテムを維持します。
- **継続的に反復する:** 信頼が高まるにつれて実験を拡大し、洗練させます。

## カオスエンジニアリングの始め方

### ステップバイステップガイダンス

1. **チームを教育する:**  
   エンジニアとステークホルダーにカオスの原則についてトレーニングします([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering))。
2. **準備状況を評価する:**  
   堅牢な可観測性とロールバックメカニズムを確保します。
3. **重要なコンポーネントを特定する:**  
   ビジネスクリティカルなユーザージャーニーと依存関係に焦点を当てます。
4. **定常状態メトリクスを定義する:**  
   システムの健全性を表す実用的なKPIを選択します。
5. **仮説を立てる:**  
   「もし〜だったら」シナリオから始めます(例:「データベースを5分間失ったらどうなるか?」)。
6. **ツールを選択してセットアップする:**  
   スタックに適したカオスツールを選択します([Chaos Toolkit](https://chaostoolkit.org/)、[Gremlin](https://www.gremlin.com/chaos-engineering))。
7. **小規模な実験を設計して実行する:**  
   テスト環境でシンプルな障害から始めます。
8. **監視、分析、文書化する:**  
   発見事項を記録し、インシデント対応とアーキテクチャを更新します。
9. **反復して範囲を拡大する:**  
   徐々に実験の複雑さと本番環境への露出を増やします。
10. **組織に統合する:**  
    カオスエンジニアリングを信頼性、セキュリティ、開発プロセスに組み込みます。

**さらなる読み物:**
- [Google Cloud: Getting Started with Chaos Engineering](https://cloud.google.com/blog/products/devops-sre/getting-started-with-chaos-engineering)
- [Harness: What is Chaos Engineering?](https://www.harness.io/harness-devops-academy/what-is-chaos-engineering)

## 参考資料

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- [IBM: What is Chaos Engineering?](https://www.ibm.com/think/topics/chaos-engineering)
- [eG Innovations: Chaos Engineering Glossary](https://www.eginnovations.com/glossary/chaos-engineering)
- [phoenixNAP: Chaos Engineering](https://phoenixnap.com/blog/chaos-engineering)
- [Gremlin: Chaos Engineering](https://www.gremlin.com/chaos-engineering)
- [Dynatrace: What is Chaos Engineering?](https://www.dynatrace.com/news/blog/what-is-chaos-engineering/)
- [Chaos Toolkit Documentation](https://chaostoolkit.org/)
- [Google Cloud: Chaos Engineering Recipes](https://github.com/GoogleCloudPlatform/chaos-engineering/blob/main/Chaos-Engineering-Recipes-Book.md)
- [Netflix Tech Blog - Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116)
- [GameDay: Chaos Engineering Exercises](https://www.gremlin.com/gameday/)

## 関連項目

- [Site Reliability Engineering (SRE)](https://www.ibm.com/topics/site-reliability-engineering)
- [Resilience Testing](https://phoenixnap.com/blog/resilience-testing)
- [Performance Engineering](https://phoenixnap.com/blog/performance-engineering)
- [Incident Response](https://phoenixnap.com/blog/incident-response)
- [Disaster Recovery](https://phoenixnap.com/blog/disaster-recovery)
- [Observability](https://www.ibm.com/cloud/learn/observability)
- [Microservices Architecture](https://phoenixnap.com/blog/microservices-architecture)
- [Continuous Integration / Continuous Delivery (CI/CD)](https://phoenixnap.com/blog/ci-cd-pipeline)
- [Fault Injection](https://phoenixnap.com/blog/fault-injection-testing)

## 関連用語集

- **影響範囲(Blast Radius):** カオス実験の最大範囲または影響領域。リスクを軽減するために最小化する必要があります([Gremlin Glossary](https://www.gremlin.com/chaos-engineering/))。
- **定常状態(Steady State):** 観測可能なメトリクスで定義される、システムの正常で健全な動作状態([phoenixNAP](https://phoenixnap.com/blog/chaos-engineering))。
- **障害注入(Fault Injection):** システムの動作を観察し改善するために、意図的に障害を導入すること([eG Innovations](https://www.eginnovations.com/glossary/chaos-engineering))。
- **GameDay:** インシデント対応を実践するためのスケジュールされたチームベースのカオスエンジニアリングイベント([Gremlin GameDay](https://www.gremlin.com/gameday/))。
- **レジリエンス(Resilience):** 障害から回復し適応するシステムの能力([IBM](https://www.ibm.com/think/topics/chaos-engineering))。
- **可観測性(Observability):** メトリクス、ログ、トレースを通じてシステムの状態と動作を理解する能力([IBM Observability](https://www.ibm.com/cloud/learn/observability))。

**権威あるコミュニティ主導のベストプラクティスについては、[IBM Observability](https://www.ibm.com/cloud/learn/observability)をご覧ください。**
この用語集は、カオスエンジニアリングの決定的なリファレンスガイドとして、初心者と上級実践者の両方をサポートするように設計されています。すべてのセクションは業界をリードするリソースから調達されており、ドキュメント、チュートリアル、実世界のケーススタディへのリンクが含まれています。コミュニティと関わり、[Principles of Chaos Engineering](https://principlesofchaos.org/)を読み、構造化されたカオスプラクティスを適用して、自身のシステムのレジリエンスを向上させることで、探求を続けてください。