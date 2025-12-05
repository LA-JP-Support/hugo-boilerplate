---
title: ロードバランシング用語集:詳細解説と高度なリファレンス
date: 2025-11-25
translationKey: load-balancing-glossary-deep-dive-advanced
description: ロードバランシングについて学ぶ:アプリケーションの可用性、信頼性、パフォーマンスを最適化するために、ネットワークトラフィックを複数のサーバーに分散する技術。AI基盤における種類、アルゴリズム、メリットを詳しく解説します。
keywords:
- ロードバランシング
- ロードバランサー
- ネットワークトラフィック
- サーバースケーラビリティ
- アプリケーションパフォーマンス
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: 'Load Balancing Glossary: Deep Dive & Advanced Reference'
term: ろーどばらんしんぐようごしゅう:しょうさいかいせつとこうどなりふぁれんす
---
## 1. 定義:ロードバランシングとは?

**ロードバランシング**とは、受信するネットワークトラフィックやアプリケーショントラフィックを、バックエンドサーバーのグループ(サーバーファームまたはプールと呼ばれることが多い)に対して、単一のサーバーに負荷が集中しないよう、インテリジェントに分散するプロセスです。ロードバランサーは、クライアントリクエストを受信し、アルゴリズムとリアルタイムのサーバー健全性データを使用して各リクエストを最適なサーバーにルーティングする中央ゲートウェイとして機能することで、アプリケーションの可用性、信頼性、パフォーマンスを最適化します。

**参考資料:**  
- [Kemp: What Is Load Balancing?](https://kemptechnologies.com/what-is-load-balancing)  
- [IBM: What Is Load Balancing?](https://www.ibm.com/think/topics/load-balancing)

## 2. ロードバランシングが重要な理由

現代のアプリケーション、特にAI駆動型サービス、高トラフィックのウェブサイト、クラウドネイティブワークロードは、最小限の[レイテンシ](/en/glossary/latency/)と最大限のアップタイムで、数百万の同時リクエストに対応する必要があります。ロードバランシングがなければ、単一のサーバーがボトルネックとなり、速度低下や障害につながる可能性があります。ロードバランシングは以下を保証します:

- **高可用性:** サーバーに障害が発生した場合、ロードバランサーは健全なサーバーにトラフィックを再ルーティングし、継続性を維持します。
- **レジリエンス:** 障害時やメンテナンス中に再ルーティングすることで、災害復旧をサポートします。
- **スケーラビリティ:** 需要に応じてサーバーを簡単に追加または削除でき、計画的な成長と突発的なトラフィック急増の両方に対応します。
- **一貫したユーザーエクスペリエンス:** 応答時間を最小化し、予測可能なパフォーマンスを保証します。

**詳細:**  
- [AWS: What is Load Balancing?](https://aws.amazon.com/what-is/load-balancing/)

## 3. ロードバランシングの仕組み

### a. ハードウェアロードバランサー vs. ソフトウェアロードバランサー

- **ハードウェアロードバランサー:**  
  高スループットと信頼性のために構築された物理ネットワークアプライアンスで、オンプレミスデータセンターに展開されることが多いです。SSL/TLSオフロード、高度なヘルスチェック、レイヤー4/7トラフィック管理などの機能を提供しますが、多額の設備投資と継続的なメンテナンスが必要です。  
  例: [F5 BIG-IP](https://www.f5.com/products/big-ip-services.html)、[Kemp LoadMaster](https://kemptechnologies.com/load-balancer)

- **ソフトウェアロードバランサー:**  
  汎用ハードウェア、仮想マシン、またはクラウドマネージドサービスで実行されるソフトウェアとして実装されます。柔軟性、迅速なスケーリング、自動化フレームワーク(Kubernetes、OpenShiftなど)との深い統合を提供します。  
  例: [NGINX Plus](https://www.nginx.com/products/nginx/)、[HAProxy](https://www.haproxy.org/)、[AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

**詳細:**  
- [F5: Hardware vs. Software Load Balancers](https://www.f5.com/glossary/load-balancer)

### b. リアルタイムリクエストルーティングとバックエンド選択

- **リクエスト処理:**  
  ロードバランサーはすべてのクライアントリクエストを受信し、ルールとリアルタイムの健全性データを使用して、各リクエストに最適なバックエンドサーバーを選択します。
- **サーバー選択:**  
  サーバー選択に影響する要因には、現在の健全性ステータス、アクティブな接続数、応答時間、サーバーウェイト、カスタムビジネスルールなどがあります。

**参考:**  
- [Kemp: Load Balancing Algorithms and Techniques](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques)

### c. ヘルスチェックとフェイルオーバー

- ロードバランサーは、バックエンドサーバーの可用性を確認するために、継続的にヘルスチェック(TCP/HTTP ping、アプリケーションレベルプローブなど)を実行します。
- サーバーに障害が発生すると、自動的にプールから削除されます。回復してヘルスチェックに合格すると、再び組み込まれます。

**詳細:**  
- [Google Cloud: Backend Health Checks](https://cloud.google.com/load-balancing/docs/health-check-concepts)

### d. セッション永続性(「スティッキーセッション」)

一部のアプリケーションでは、セッションデータ(ショッピングカート、認証コンテキストなど)を同じサーバー上に保持する必要があります。ロードバランサーは、多くの場合Cookieまたはipハッシュ技術を使用してセッション永続性を強制し、セッション内のすべてのリクエストが同じバックエンドにルーティングされるようにします。

**参考:**  
- [NGINX: Session Persistence](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/#sticky)

### e. 実世界のアナロジー

ロードバランサーは、レストランのマネージャーが食事客をテーブルに割り当てるようなものです。あるウェイターが過負荷になっている場合、マネージャーは新しいゲストを他のウェイターに案内し、迅速でスムーズなサービスを保証します。

## 4. ロードバランサーの種類

ロードバランサーは、展開方法、OSIレイヤー、アーキテクチャによって分類されます:

| **種類**                        | **OSIレイヤー** | **説明**                                                                                     |
|----------------------------------|---------------|-----------------------------------------------------------------------------------------------------|
| **ネットワークロードバランサー(NLB)**  | L4            | TCP/UDPヘッダー(IPアドレス、ポート)に基づいてトラフィックをルーティング。高パフォーマンス、低レイテンシワークロードに最適。 |
| **アプリケーションロードバランサー(ALB)** | L7         | HTTPヘッダー、URL、Cookieに基づいてルーティング。最新のWeb/APIアプリに適しています。 |
| **グローバルサーバーロードバランサー(GSLB)** | DNS      | 地理的な場所/データセンター間でトラフィックを分散し、災害復旧と地理的冗長性を実現します。 |
| **ハードウェアロードバランサー**       | L4/L7         | 堅牢で高スループットのロードバランシングのための物理アプライアンス。エンタープライズデータセンターで使用されます。 |
| **ソフトウェアロードバランサー**       | L4/L7         | アプリケーションベースで柔軟性があり、クラウド/仮想化環境に適しています。 |
| **仮想ロードバランサー**        | L4/L7         | 仮想マシンまたはコンテナ内で実行され、オーケストレーションツール(Kubernetesなど)と統合されます。 |
| **エラスティックロードバランサー**        | L4/L7         | クラウドネイティブで、需要に応じて[オートスケーリング](/en/glossary/autoscaling/)。動的なクラウドデプロイメントに最適です。 |

**レイヤー4(トランスポート層):** ルーティングのためにTCP/UDPを検査します。  
**レイヤー7(アプリケーション層):** 高度なルーティングのためにHTTP/HTTPS/アプリケーションデータを検査します。

**詳細:**  
- [Loadbalancer.org: Comparing Layer 4, Layer 7, and GSLB](https://www.loadbalancer.org/blog/comparing-layer-4-layer-7-and-gslb-load-balancing-techniques/)

## 5. ロードバランシングアルゴリズム

ロードバランシングアルゴリズムは、リクエストの分散方法を定義します:

### a. 静的アルゴリズム

- **ラウンドロビン:**  
  サーバーを順番に巡回し、各新しいリクエストを次のサーバーに割り当てます。容量が等しいサーバーに最適です。  
  [ラウンドロビンの説明](https://kemptechnologies.com/load-balancer/round-robin-load-balancing)

- **重み付きラウンドロビン:**  
  割り当てられたウェイトに基づいて、より多くのリクエストを高容量サーバーに割り当てます。  
  [重み付きラウンドロビンの説明](https://kemptechnologies.com/load-balancer/weighted-round-robin-load-balancing)

- **IPハッシュ:**  
  クライアントIPをハッシュ化してサーバーを選択し、再訪問クライアントのセッション永続性を実現します。

### b. 動的アルゴリズム

- **最小接続数:**  
  アクティブセッションが最も少ないサーバーにルーティングします。  
  [最小接続数の説明](https://kemptechnologies.com/load-balancer/least-connections-load-balancing)

- **重み付き最小接続数:**  
  最小接続数と同様ですが、サーバーウェイト(容量)を考慮します。

- **最小応答時間:**  
  平均応答時間が最も短く、接続数が最も少ないサーバーにリクエストを送信します。

- **リソースベース(エージェントベース):**  
  サーバーが報告するメトリクス(CPU、メモリ、ディスク)を使用して、動的にトラフィックをルーティングします。  
  [リソースベースロードバランシング](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques)

- **コンシステントハッシング:**  
  サーバー/クライアントをハッシュリングにマッピングし、サーバーの追加/削除時の中断を最小限に抑えます。

- **2つの選択肢からのランダム(「2の累乗」):**  
  ランダムに2つのサーバーを選択し、負荷の少ない方にリクエストを割り当てます。

**高度なアルゴリズムオプション(Google Cloud Service Mesh):**  
- リージョン別ウォーターフォール  
- リージョンへのスプレー  
- ワールドへのスプレー  
- ゾーン別ウォーターフォール  
[Google Cloudでの高度なロードバランシング](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-load-balancing-overview)

## 6. ロードバランシングの主な利点

- **可用性:**  
  ヘルスチェック、フェイルオーバー、冗長性により、継続的なアップタイムとゼロダウンタイムメンテナンスを実現します。

- **スケーラビリティ:**  
  サーバーを追加/削除することでトラフィック急増に容易に対応。クラウドネイティブロードバランサーは[オートスケーリング](/ja/glossary/autoscaling/)をサポートします。

- **セキュリティ:**  
  WAFと統合し、SSL/TLSオフロードを提供し、DDoS攻撃トラフィックを吸収します。  
  [F5: SSL Offloading](https://f5.com/glossary/ssl-termination)

- **パフォーマンス:**  
  応答時間を短縮し、帯域幅を最適化し、ユーザーを最も近いまたは最も負荷の少ないサーバーにルーティングします。

**詳細:**  
- [Kemp: Load Balancer Benefits](https://kemptechnologies.com/what-is-load-balancing)

## 7. ユースケースと例

- **Eコマース:**  
  高トラフィックイベント(フラッシュセールなど)中、ロードバランサーはリクエストを分散して高速なページ読み込みを保証し、スティッキーセッションを介してカート状態を維持します。

- **ストリーミングサービス:**  
  ユーザーを最も近い/最も負荷の少ないサーバーにルーティングし、バッファリングとダウンタイムを最小限に抑えます。

- **クラウドAIデプロイメント:**  
  推論APIリクエストをコンテナまたはVM間で均等に分散し、低レイテンシの予測を実現します。

- **災害復旧:**  
  グローバルサーバーロードバランシングは、健全で地理的に分散したデータセンターにトラフィックを再ルーティングします。

- **メンテナンス:**  
  ダウンタイムなしで更新のためにサーバーをドレインできます。トラフィックは健全なサーバーにルーティングされます。

## 8. プラットフォーム固有の実装

| **ベンダー/プラットフォーム** | **ソリューション** | **ドキュメント** |
|----------------------|-----------------|-------------------|
| **AWS** | [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) | [AWS Load Balancing Docs](https://aws.amazon.com/what-is/load-balancing/) |
| **Google Cloud** | [Cloud Load Balancing](https://cloud.google.com/load-balancing) | [Google Cloud Load Balancing Overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) |
| **F5** | [BIG-IP](https://www.f5.com/products/big-ip-services.html)、[NGINX Plus](https://www.f5.com/products/nginx) | [F5 Load Balancer Glossary](https://www.f5.com/glossary/load-balancer) |
| **Kemp** | [LoadMaster](https://kemptechnologies.com/load-balancer) | [Kemp Load Balancing Overview](https://kemptechnologies.com/what-is-load-balancing) |

各ソリューションは、独自の機能(グローバルロードバランシング、WAF統合、SSLオフロード、Kubernetesサポートなど)を提供します。

## 9. ビジュアルエイドとアーキテクチャ図

- **典型的なロードバランサーデプロイメント:**  
  ![ロードバランサー図](https://cdn.studio.f5.com/images/k6fem79d/production/a430050f25e3b35af49298281ad58f5a0f20fd83-909x557.svg)
  _ロードバランサーはクライアントリクエストを受信し、複数のバックエンドサーバー間で分散します。サーバーに障害が発生すると、ロードバランサーは健全なサーバーにトラフィックを再ルーティングします。_

- **アルゴリズムフローの例:**  
  ![ラウンドロビン vs. 最小接続数](https://kemptechnologies.com/images/kemptechnologieslibraries/illustrations/what-is-a-load-balancer-diagram-desktop.svg?sfvrsn=41cd660d_2)
  _ラウンドロビンはすべてのサーバーを順番に巡回します。最小接続数は、アクティブセッションが最も少ないサーバーにルーティングします。_

- **グローバルロードバランシング:**  
  ![グローバルサーバーロードバランシング](https://docs.cloud.google.com/static/load-balancing/images/load-balancing-overview.svg)
  _ユーザーリクエストは、地理的に最も近いまたは最も健全なデータセンターにルーティングされます。_

## 10. その他のリソース

- [IBM: What Is Load Balancing?](https://www.ibm.com/think/topics/load-balancing)
- [AWS: What is Load Balancing?](https://aws.amazon.com/what-is/load-balancing/)
- [Kemp: What Is Load Balancing & How Do Load Balancers Work](https://kemptechnologies.com/what-is-load-balancing)
- [F5: What Is a Load Balancer?](https://www.f5.com/glossary/load-balancer)
- [Google Cloud: Load Balancing Overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
- [NGINX: Load Balancing Algorithms and Techniques](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)
- [Kubernetes: Service Load Balancing](https://kubernetes.io/docs/concepts/services-networking/service/)

## サマリーテーブル:ロードバランサーの種類

| **種類**                        | **OSIレイヤー** | **デプロイメント**          | **主なユースケース**                                    |
|----------------------------------|---------------|------------------------|-----------------------------------------------------|
| ネットワークロードバランサー(NLB)      | レイヤー4       | ハードウェア/ソフトウェア/クラウド | 高スループット、TCP/UDPトラフィック、低レイテンシ       |
| アプリケーションロードバランサー(ALB)  | レイヤー7       | ハードウェア/ソフトウェア/クラウド | HTTP/HTTPS、Web API、高度なルーティング              |
| グローバルサーバーロードバランサー(GSLB) | DNS         | ハードウェア/クラウド         | 災害復旧、地理的に分散したアプリケーション      |
| ハードウェアロードバランサー           | L4/L7         | オンプレミス            | レガシーデータセンター、高パフォーマンス環境   |
| ソフトウェアロードバランサー           | L4/L7         | クラウド/仮想          | 柔軟性、クラウドネイティブ、DevOps中心のデプロイメント   |
| 仮想ロードバランサー            | L4/L7         | VM/コンテナ           | Kubernetes、マイクロサービス、仮想化データセンター  |
| エラスティックロードバランサー            | L4/L7         | クラウド                  | オートスケーリング、動的、需要ベースのアプリケーション     |

## 用語集

- **バックエンドサーバー:** アプリケーションロジックまたはデータ処理を実行する実際のサーバー。
- **ヘルスチェック:** サーバーの可用性を確認するための定期的なテスト(ping、HTTPリクエストなど)。
- **セッション永続性(スティッキーセッション):** ユーザーのセッションが特定のサーバー上に留まることを保証します。
- **リバースプロキシ:** バックエンドサーバーにリクエストを転送し、クライアントに応答を返すサーバー(多くの場合ロードバランサー)。
- **アプリケーションデリバリーコントローラー(ADC):** ロードバランシング、SSLオフロード、WAF、高度なトラフィック管理を実行するアプライアンスまたはソフトウェア。

**ロードバランシングは、信頼性が高く、スケーラブルで、高パフォーマンスなAIインフラストラクチャとデプロイメントの基盤です。詳細とアーキテクチャ固有のガイダンスについては、上記にリンクされている公式ベンダードキュメントを参照してください。**

**権威ある参考資料と詳細な技術ガイド:**

- [Kemp: Load Balancing Algorithms and Techniques (Deep Dive)](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques)
- [Loadbalancer.org: Best Load Balancing Methods, Techniques and Algorithms](https://www.loadbalancer.org/blog/load-balancing-methods/)
- [Google Cloud: Advanced Load Balancing Overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-load-balancing-overview)

この用語集は、多様な環境で最新のロードバランシングを扱うアーキテクト、エンジニア、AI実務者のための詳細で実用的なリファレンスとして設計されています。