---
title: Docker
date: 2025-11-25
translationKey: docker
description: Dockerについて学びましょう。Dockerは、軽量でポータブルなコンテナでアプリケーションをパッケージ化、配布、実行するためのオープンソースプラットフォームです。そのアーキテクチャ、メリット、ユースケースを理解できます。
keywords:
- Docker
- コンテナ
- コンテナ化
- マイクロサービス
- Kubernetes
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Docker
term: ドッカー
reading: Docker
kana_head: その他
---
## Dockerとは?

Dockerは、開発者やシステム管理者がアプリケーションをコンテナとしてビルド、パッケージ化、配布、実行できるオープンソースプラットフォームです。コンテナは、アプリケーションの実行に必要なすべてのもの(コード、ランタイム、システムツール、ライブラリ、設定)をカプセル化した、軽量でスタンドアロンな実行可能ユニットです。このカプセル化により、開発、テスト、ステージング、本番環境など、異なる環境間でソフトウェアが同一に動作することが保証されます。

Dockerの革新性は、アプリケーションの開発、配布、デプロイを標準化する方法を提供し、悪名高い「私のマシンでは動く」問題を解消することにあります。Dockerコンテナはポータブルで一貫性があり、開発者のラップトップ、オンプレミスのデータセンター、AWS、Azure、Google Cloudなどのパブリッククラウドを含む、Dockerをサポートするあらゆるインフラストラクチャで実行できます。

**参考資料:**
- [Docker公式概要](https://docs.docker.com/get-started/docker-overview/)
- [Docker Curriculum入門](https://docker-curriculum.com#what-is-docker-)

## コンテナ化が重要な理由

従来のデプロイメントでは、環境の不整合がしばしば発生します。たとえば、Webアプリケーションが開発者のマシンでは動作するのに、ソフトウェアのバージョン、設定、または依存関係の欠落の違いにより、本番環境では失敗することがあります。

[コンテナ化](/en/glossary/containerization/)は、アプリケーションが必要とするすべてのものを単一の分離されたユニット(コンテナ)にパッケージ化することで、この問題を解決します。Dockerは、名前空間やcgroupsなどのLinuxカーネル機能を活用して、プロセスの分離、リソース割り当て、セキュリティ境界を提供します。このモデルにより、以下が可能になります:

- **一貫した環境:** 同じコンテナイメージがどこでも同一に実行されます。
- **効率的なリソース使用:** コンテナはホストOSカーネルを共有し、オーバーヘッドを削減します。
- **迅速なデプロイとスケーリング:** コンテナは数秒で起動し、複製やスケーリングが容易です。
- **簡素化された管理:** コンテナは迅速に起動、停止、置換でき、デプロイと運用プロセスを効率化します。

**参考文献:**
- [DockerコンテナとVM](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Docker Curriculum: コンテナを使用する理由](https://docker-curriculum.com#why-use-containers-)

## Dockerの仕組み

Dockerは、オペレーティングシステムレベルの仮想化を利用して、分離されたコンテナを作成します。各コンテナは、ホスト上で実行される分離されたプロセスであり、ホストOSカーネルを共有しながらも、独自のファイルシステム、ネットワークスタック、プロセス空間を持ちます。

**運用ワークフロー:**
1. **ビルド:** Dockerfile(アプリケーション環境、依存関係、ビルドステップを定義するテキストファイル)を使用してDockerイメージを作成します。
2. **配布:** コンテナレジストリ(Docker Hubやプライベートレジストリなど)を介してイメージを保存・配布します。
3. **実行:** レジストリからイメージをプルし、Dockerがサポートされている場所ならどこでもコンテナを起動します。

**例:**
- Dockerfileを使用してWebアプリケーションイメージをビルドし、Docker Hubにプッシュして、クラウドVM上で実行します。

**関連情報:**
- [公式Dockerfileリファレンス](https://docs.docker.com/engine/reference/builder/)
- [Docker Hub](https://hub.docker.com)

## Dockerアーキテクチャ

Dockerのアーキテクチャは、クライアント・サーバーモデルに基づいており、いくつかの主要コンポーネントが連携して動作します:

### 1. Dockerデーモン(`dockerd`)
- Dockerデーモンは、Dockerオブジェクト(イメージ、コンテナ、ネットワーク、ボリューム)を管理するバックグラウンドサービスです。
- Docker APIリクエストをリッスンし、それに応じて操作を実行します。
- システムプロセスとして実行され、root権限または適切なユーザーグループメンバーシップが必要です。

**出典:**  
[Dockerデーモンドキュメント](https://docs.docker.com/engine/reference/commandline/dockerd/)

### 2. Dockerクライアント(`docker`)
- Dockerの主要なユーザーインターフェースです。
- コマンドラインツール(`docker`)で、`docker build`、`docker run`、`docker ps`などのコマンドを発行します。
- UNIXソケットまたはネットワーク経由のREST APIを介してDockerデーモンと通信します。

### 3. Dockerレジストリ
- Dockerイメージのストレージおよび配布システムです。
- **Docker Hub**はデフォルトのパブリックレジストリで、数百万のイメージが利用可能です。
- 組織は内部使用のためにプライベートレジストリを運用できます。

**参照:**  
[Dockerレジストリドキュメント](https://docs.docker.com/registry/)

### 4. Dockerイメージ
- コンテナを作成するための命令を含む読み取り専用テンプレートです。
- レイヤーで構築されます。各Dockerfileコマンド(RUN、COPYなど)が新しいレイヤーを作成します。
- イメージは他のイメージから継承でき、モジュール式のビルドが可能です。

**詳細:**  
[Dockerイメージとは?(公式ドキュメント)](https://docs.docker.com/get-started/overview/)

### 5. Dockerコンテナ
- イメージの実行可能インスタンスです。
- ホストや他のコンテナから分離されていますが、Dockerネットワークを介して通信できます。
- デフォルトでは一時的ですが、永続データにはボリュームを使用できます。

### 6. Docker Compose
- YAMLファイル(`docker-compose.yml`)を使用してマルチコンテナアプリケーションを定義・管理するツールです。
- サービス、ネットワーク、ボリュームの宣言的な設定を可能にします。

**参考:**  
[Docker Composeドキュメント](https://docs.docker.com/compose/)

### 7. Dockerネットワークとボリューム
- **ネットワーク:** コンテナ通信と分離のための仮想ネットワーク(bridge、host、overlayなど)。
- **ボリューム:** コンテナデータの永続ストレージで、再起動やコンテナの破棄後も存続します。

**図:**  
[Dockerアーキテクチャ図を参照](https://docs.docker.com/get-started/overview/#the-docker-architecture)

## 主要な技術用語の定義

- **コンテナ:** アプリケーションとその依存関係をカプセル化した分離されたプロセス。分離には名前空間、リソース管理にはcgroupsなどのカーネル機能を使用します。[コンテナとは?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- **Dockerイメージ:** コンテナを作成するための読み取り専用のレイヤー化されたテンプレート。
- **Dockerfile:** Dockerイメージをビルドするための命令を含むスクリプト。
- **Dockerデーモン(`dockerd`):** Dockerオブジェクトを管理するサービス。
- **Dockerクライアント(`docker`):** Dockerデーモンと対話するためのCLIまたはAPI。
- **レジストリ:** イメージを保存・配布するためのリポジトリ。
- **Docker Compose:** マルチコンテナアプリケーションをオーケストレーションするツール。
- **名前空間:** プロセス分離のためのLinuxカーネル機能。
- **ボリューム:** コンテナにマウントされる永続ストレージ。
- **ネットワーク:** コンテナ間およびコンテナ・ホスト間通信のための仮想ネットワーク。

## Dockerの利点

Dockerコンテナは、従来のデプロイメントモデルや仮想マシンに比べて多くの利点を提供します:

### 1. ポータビリティ
- コンテナは異なるOSやインフラストラクチャで同じように実行されます。
- ローカル、オンプレミス、クラウド環境間でワークロードをシームレスに移動できます。

### 2. 速度
- コンテナはミリ秒または数秒で起動します(OS起動不要)。
- ビルド、テスト、デプロイサイクルが迅速化されます。

### 3. リソース利用
- コンテナはホストOSカーネルを共有し、オーバーヘッドを削減します。
- ホストあたりのアプリケーション密度が高くなります。

### 4. 分離とセキュリティ
- コンテナはプロセスを分離し、競合のリスクを減らし、セキュリティ態勢を改善します。
- Linux名前空間とcgroupsが境界を強制します。

### 5. スケーラビリティと柔軟性
- コンテナの起動/停止によりアプリケーションをスケールします。
- マイクロサービスと動的デプロイメントをサポートします。

### 6. 一貫性と再現性
- 開発から本番まで同一の環境を実現します。

### 7. CI/CDとの統合
- 最新のDevOpsワークフローでビルド、テスト、デプロイステップを自動化します。

**参考文献:**
- [なぜDocker?(Docker公式)](https://www.docker.com/resources/what-container/)
- [コンテナの利点](https://aws.amazon.com/docker/)

## Docker vs. 仮想マシン(VM)

| 機能                  | Dockerコンテナ                       | 仮想マシン(VM)                     |
|----------------------|-------------------------------------|-----------------------------------|
| 分離                 | OSレベル(名前空間、cgroups)          | ハードウェアレベル(ハイパーバイザー)|
| リソース使用         | 軽量、最小限のオーバーヘッド          | 各VMが完全なゲストOSを実行         |
| 起動時間             | 数秒以下                             | 数分                              |
| ポータビリティ       | 高度にポータブル                     | ポータビリティが低い(ハイパーバイザー固有)|
| スケーラビリティ     | 容易にスケール可能、低オーバーヘッド  | スケーラビリティが低い、高オーバーヘッド|
| 密度(ホストあたり)   | 高い                                 | 低い                              |

**追加の洞察:**
- コンテナはVM上で実行でき、クラウド環境で両方の利点を組み合わせることができます。
- コンテナはホストのカーネルを使用するため、ホストとは異なるOSを実行するのには適していません。

**参考資料:**  
[コンテナとVM(Dockerドキュメント)](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms)

## Dockerの一般的なユースケース

### 1. マイクロサービスアーキテクチャ
- モノリシックアプリケーションを独立してデプロイ可能なサービスに分解します。
- 各マイクロサービスは独自のコンテナで実行され、独立したスケーリングと更新が可能です。

### 2. 継続的インテグレーション/継続的デプロイメント(CI/CD)
- 自動化パイプラインのためにビルド/テスト環境を標準化します。
- 環境のドリフトとデプロイメントエラーを最小限に抑えます。

### 3. クラウドネイティブアプリケーション開発
- マルチクラウドまたはハイブリッドデプロイメントを簡素化します。
- 迅速なプロトタイピングとリリースサイクルを可能にします。

### 4. ビッグデータと分析
- 再現可能な実行のためにデータ処理ジョブと分析ツールをパッケージ化します。
- コンピューティングリソースを動的にスケールします。

### 5. 開発/テスト環境
- 開発者とテスターのために使い捨ての一貫した環境をプロビジョニングします。
- オンボーディングとトラブルシューティングを加速します。

### 6. Webアプリケーションのデプロイメント
- Webサーバー、API、フロントエンドを分離されたコンテナとしてデプロイします。
- 迅速なスケーリングと一貫したパフォーマンスを実現します。

### 7. Containers as a Service(CaaS)
- チームや顧客向けにマネージドコンテナプラットフォームを提供します。

**実例:**
- [Netflix](https://netflixtechblog.com/)、[Uber](https://eng.uber.com/)、[Airbnb](https://medium.com/airbnb-engineering)は、マイクロサービスとスケーラブルなインフラストラクチャにDockerを活用しています。
- 企業は再現性とスケーラビリティのためにコンテナを使用して機械学習モデルをデプロイしています。

## Dockerを始める

### 1. Dockerのインストール

- Windows、macOS、またはLinux用のDocker Desktopをインストールします。
- 公式インストールガイド: [Dockerを入手](https://docs.docker.com/get-docker/)

### 2. Dockerfileの作成

Dockerfileはイメージのビルドステップを定義します。

**例:**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 3. イメージのビルド

ターミナルコマンド:
```bash
docker build -t my-python-app .
```

### 4. コンテナの実行

```bash
docker run -d -p 5000:5000 my-python-app
```
- `-d`: デタッチドモード
- `-p`: ホストポートをコンテナポートにマッピング

### 5. イメージのプッシュ/プル

プッシュ:
```bash
docker push username/my-python-app
```
プル:
```bash
docker pull username/my-python-app
```

### 6. Docker Composeの使用

**`docker-compose.yml`の例:**
```yaml
version: '3'
services:
  web:
    image: my-python-app
    ports:
      - "5000:5000"
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
```

すべてのサービスを起動:
```bash
docker-compose up
```

**ハンズオンチュートリアル:**  
[Docker Curriculum: DockerでWebアプリ](https://docker-curriculum.com#webapps-with-docker)

## ベストプラクティス

- **最小限のイメージ:** 公式/最小限のベースイメージを使用し、不要なファイルを削除します。
- **マルチステージビルド:** ビルドとランタイムの依存関係を分離してイメージを軽量化します。
- **rootを避ける:** セキュリティ向上のために非rootユーザーを使用します。
- **イメージのタグ付け:** セマンティックバージョニングと明確なタグを使用します。
- **環境変数:** 設定には[環境変数](/ja/glossary/environment-variables--secrets-/)を使用し、[シークレット](/en/glossary/environment-variables--secrets-/)をハードコードしません。
- **監視/ログ:** ログを集中化し、ヘルスを監視します。
- **イメージの更新:** 脆弱性にパッチを当てるために、イメージと依存関係を定期的に更新します。
- **ボリューム:** 永続データに使用します。

**参考資料:**  
[Dockerベストプラクティス](https://docs.docker.com/develop/dev-best-practices/)

## AIインフラストラクチャとデプロイメントにおけるDocker

- **モデルのパッケージング:** コンテナは機械学習モデルとその依存関係をカプセル化し、再現可能なデプロイメントを実現します。
- **リソース効率:** 同じハードウェア上で複数のデータパイプラインを分離されたコンテナで実行します。
- **スケーラブルなサービング:** AI推論サービスをスケーラブルで独立したコンテナとしてデプロイします。
- **CI/CD統合:** コンテナ化されたステージでテスト、検証、デプロイメントを自動化します。

**例:**  
データサイエンティストが訓練済みモデルとAPIを含むDockerイメージをビルドし、スケーラブルな推論のためにKubernetesにデプロイします。

**ケーススタディ:**  
[機械学習のためのDocker](https://www.docker.com/blog/tag/machine-learning/)

## 高度なトピック

### コンテナオーケストレーション

- **Kubernetes**と**Docker Swarm:** クラスター全体でのコンテナのデプロイメント、スケーリング、運用を管理するツールです。
- **サービスディスカバリ、ロードバランシング、自動スケーリング、自己修復**はオーケストレーターによって処理されます。

**詳細:**  
[Kubernetesドキュメント](https://kubernetes.io/docs/)

### セキュリティの考慮事項

- 信頼できるイメージ(公式または検証済みパブリッシャー)を使用します。
- イメージの脆弱性を定期的にスキャンします([Docker Scout](https://docs.docker.com/scout/))。
- 最小権限の原則: コンテナの権限を制限します。
- 専用ホストで機密ワークロードを分離します。

### ネットワーキングとサービスディスカバリ

- **Bridge:** 単一ホストコンテナのデフォルトネットワーク。
- **Host:** ホストのネットワークスタックを共有します。
- **Overlay:** マルチホスト通信を可能にします(オーケストレーターで使用)。

**参考:**  
[Dockerネットワーキング](https://docs.docker.com/network/)

## よく使用されるDockerコマンド

- `docker run` — 新しいコンテナを起動
- `docker ps` — 実行中のコンテナをリスト
- `docker images` — イメージをリスト
- `docker build` — Dockerfileからイメージをビルド
- `docker pull` — レジストリからイメージをダウンロード
- `docker push` — レジストリにイメージをアップロード
- `docker exec` — 実行中のコンテナでコマンドを実行
- `docker logs` — コンテナログを取得
- `docker stop` — 実行中のコンテナを停止
- `docker rm` — コンテナを削除

**完全なCLIリファレンス:**  
[Docker CLIドキュメント](https://docs.docker.com/engine/reference/commandline/cli/)

## 用語集: 主要なDocker用語

| 用語                  | 定義                                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------|
| コンテナ              | アプリケーションとその依存関係を実行する分離されたプロセス。                                |
| イメージ              | コンテナ作成のための命令を含む読み取り専用テンプレート。                                    |
| Dockerfile            | Dockerイメージのビルドステップを定義するファイル。                                          |
| レジストリ            | イメージを保存・配布するサービス(例: Docker Hub)。                                          |
| Dockerデーモン        | Dockerオブジェクトを管理するバックグラウンドプロセス。                                      |
| Dockerクライアント    | DockerデーモンへのインターフェースとなるCLI/API。                                           |
| ボリューム            | コンテナの永続ストレージ。                                                                  |
| ネットワーク          | コンテナ用の仮想ネットワーキング。                                                          |
| Compose               | マルチコンテナアプリケーションを定義/実行するツール。                                       |
| オーケストレーション  | コンテナのデプロイメント、スケーリング、管理の自動化。                                      |
| 名前空間              | リソース/プロセス分離のためのLinuxカーネル機能。                                            |
| cgroup                | リソース割り当て/制御のためのLinuxカーネル機能。                                            |
| オーバーレイネットワーク | マルチホストコンテナ通信を可能にする仮想ネットワーク。                                    |
| マルチステージビルド  | ビルド/ランタイム依存関係を分離するDockerfile技術。                                         |
| Docker Swarm          | Docker用のネイティブクラスタリング/オーケストレーションツール。                             |

## 参考資料

- [Docker公式ドキュメント](https://docs.docker.com/get-started/docker-overview/)
- [Docker: コンテナとは?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Docker Curriculum(初心者から上級者まで)](https://docker-curriculum.com)
- [AWS: Dockerとは?](https://aws.amazon.com/docker/)
- [Oracle: Dockerとは?](https://www.oracle.com/cloud/cloud-native/container-registry/what-is-docker/)
- [GeeksforGeeks: Dockerを使用したコンテナ化](https://www.geeksforgeeks.org/blogs/containerization-using-docker/)
- [Docker Composeドキュメント](https://docs.docker.com/compose/)
- [Kubernetesドキュメント](https://kubernetes.io/docs/)
- [Docker CLIリファレンス](https://docs.docker.com/engine/reference/commandline/cli/)
- [Dockerベストプラクティス](https://docs.docker.com/develop/dev-best-practices/)
- [Docker Hub](https://hub.docker.com)
- [Dockerネットワーキング](https://docs.docker.com/network/)

**まとめ:**  
Dockerはアプリケーションをコンテナにパッケージ化することを標準化し、多様な環境間での迅速、一貫性、ポータブルなデプロイメントを可能にします。その軽量設計、リソース効率、豊富なエコシステムにより、最新のソフトウェア開発、クラウド運用、AIインフラストラクチャの基盤となっています。Dockerアーキテクチャ、ベストプラクティス、オーケストレーションおよびCI/CDシステムとの統合を習得することで、効率的でスケーラブルかつ信頼性の高いソフトウェアデリバリーが実現されます。

**権威ある参考文献:**
- [Dockerドキュメント: コンテナとは?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Docker Curriculum](https://docker-curriculum.com)
- [Dockerベストプラクティス](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetesドキュメント](https://kubernetes.io/docs/)