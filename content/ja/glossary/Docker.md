---
title: Docker
date: '2025-12-19'
lastmod: '2025-12-19'
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
url: "/ja/glossary/Docker/"
---
## Dockerとは?

Dockerは、開発者やシステム管理者がアプリケーションをコンテナとしてビルド、パッケージ化、配布、実行できるオープンソースプラットフォームです。コンテナは、アプリケーションの実行に必要なすべてを内包する軽量でスタンドアロンな実行可能ユニットです。具体的には、コード、ランタイム、システムツール、ライブラリ、設定などが含まれます。このカプセル化により、開発、テスト、ステージング、本番環境など、異なる環境間でソフトウェアが同一に動作することが保証されます。

Dockerの革新性は、アプリケーションの開発、配布、デプロイを標準化する方法を提供し、悪名高い「私のマシンでは動く」問題を解消する点にあります。Dockerコンテナはポータブルで一貫性があり、開発者のラップトップ、オンプレミスのデータセンター、AWS、Azure、Google Cloudなどのパブリッククラウドを含む、Dockerをサポートするあらゆるインフラストラクチャで実行できます。

コンテナ化は、アプリケーションが必要とするすべてを単一の隔離されたユニットにパッケージ化することで、環境の不整合を解決します。Dockerは、名前空間やcgroupsなどのLinuxカーネル機能を活用して、プロセスの分離、リソース割り当て、セキュリティ境界を提供します。このモデルにより、一貫した環境、効率的なリソース使用、迅速なデプロイとスケーリング、簡素化された管理が実現されます。コンテナはホストOSカーネルを共有するため、従来の仮想マシンと比較してオーバーヘッドが削減されます。

## Dockerの仕組み

Dockerは、オペレーティングシステムレベルの仮想化を利用して隔離されたコンテナを作成します。各コンテナは、ホスト上で実行される隔離されたプロセスであり、ホストOSカーネルを共有しながらも、独自のファイルシステム、ネットワークスタック、プロセス空間を持ちます。

**運用ワークフロー:**1.**ビルド:**Dockerfile(アプリケーション環境、依存関係、ビルド手順を定義するテキストファイル)を使用してDockerイメージを作成
2. **配布:**コンテナレジストリ(Docker Hubまたはプライベートレジストリ)を介してイメージを保存・配布
3. **実行:**レジストリからイメージをプルし、Dockerがサポートされている場所ならどこでもそこからコンテナを起動**例:**Dockerfileでウェブアプリケーションイメージをビルドし、Docker Hubにプッシュし、クラウドVM上で実行することで、完全なワークフローを実証できます。

## Dockerアーキテクチャ

Dockerのアーキテクチャは、いくつかの主要コンポーネントを持つクライアント・サーバーモデルに基づいています。

**Docker Daemon (dockerd)**- Dockerオブジェクト(イメージ、コンテナ、ネットワーク、ボリューム)を管理するバックグラウンドサービス
- Docker APIリクエストをリッスンし、操作を実行
- root権限または適切なユーザーグループメンバーシップを必要とするシステムプロセスとして実行

**Docker Client (docker)**- Dockerのプライマリユーザーインターフェース
- `docker build`、`docker run`、`docker ps`などのコマンドを発行するコマンドラインツール
- UNIXソケットまたはネットワーク経由でREST APIを介してDocker daemonと通信

**Dockerレジストリ**- Dockerイメージの保存・配布システム
- Docker Hubは、数百万のイメージを持つデフォルトのパブリックレジストリ
- 組織は内部使用のためにプライベートレジストリを運用可能

**Dockerイメージ**- コンテナを作成するための命令を含む読み取り専用テンプレート
- レイヤーで構築され、各Dockerfileコマンドが新しいレイヤーを作成
- イメージは他のイメージから継承でき、モジュール式のビルドが可能

**Dockerコンテナ**- イメージの実行可能インスタンス
- ホストや他のコンテナから隔離されているが、Dockerネットワークを介して通信可能
- デフォルトでは一時的だが、ボリュームを使用して永続的なデータを保持可能

**Docker Compose**- YAMLファイルを使用してマルチコンテナアプリケーションを定義・管理するツール
- サービス、ネットワーク、ボリュームの宣言的な設定を可能にする

**Dockerネットワークとボリューム**- ネットワーク: コンテナ通信のための仮想ネットワーク(bridge、host、overlay)
- ボリューム: コンテナデータの永続的ストレージで、再起動やコンテナ破棄後も存続

## 主な利点

**ポータビリティ**- コンテナは異なるOSやインフラストラクチャ間で同一に実行
- ローカル、オンプレミス、クラウド環境間でのシームレスなワークロード移動

**速度**- コンテナはミリ秒または数秒で起動(OS起動不要)
- より迅速なビルド、テスト、デプロイサイクル

**リソース利用効率**- コンテナはホストOSカーネルを共有し、オーバーヘッドを削減
- ホストあたりの高いアプリケーション密度

**分離とセキュリティ**- コンテナはプロセスを分離し、競合リスクを軽減
- Linux名前空間とcgroupsが境界を強制

**スケーラビリティと柔軟性**- コンテナの起動/停止によりアプリケーションをスケール
- マイクロサービスと動的デプロイをサポート

**一貫性と再現性**- 開発から本番まで同一の環境
- 「私のマシンでは動く」問題を解消

**CI/CD統合**- DevOpsワークフローでビルド、テスト、デプロイステップを自動化
- パイプラインステージ全体で環境を標準化

## Docker vs. 仮想マシン

| 機能 | Dockerコンテナ | 仮想マシン |
|---------|------------------|------------------|
| 分離 | OSレベル(名前空間、cgroups) | ハードウェアレベル(ハイパーバイザー) |
| リソース使用 | 軽量、最小限のオーバーヘッド | 各VMが完全なゲストOSを実行 |
| 起動時間 | 数秒以下 | 数分 |
| ポータビリティ | 高いポータビリティ | 低いポータビリティ(ハイパーバイザー固有) |
| スケーラビリティ | 容易にスケール可能、低オーバーヘッド | スケーラビリティが低い、高オーバーヘッド |
| 密度 | 高い | 低い |

**主な洞察:**- コンテナはVM上で実行でき、クラウド環境で両方の利点を組み合わせ可能
- コンテナはホストのカーネルを使用するため、VMと比較して異なるOSサポートが制限される

## 一般的なユースケース

**マイクロサービスアーキテクチャ**- モノリシックアプリケーションを独立してデプロイ可能なサービスに分解
- 各マイクロサービスが独自のコンテナで実行
- 独立したスケーリングと更新を可能にする

**継続的インテグレーション/継続的デプロイメント**- 自動化パイプラインのためにビルド/テスト環境を標準化
- 環境のドリフトとデプロイエラーを最小化

**クラウドネイティブアプリケーション開発**- マルチクラウドまたはハイブリッドデプロイを簡素化
- 迅速なプロトタイピングとリリースサイクルを実現

**ビッグデータと分析**- 再現可能な実行のためにデータ処理ジョブと分析ツールをパッケージ化
- 計算リソースを動的にスケール

**開発/テスト環境**- 使い捨ての一貫した環境をプロビジョニング
- オンボーディングとトラブルシューティングを加速

**ウェブアプリケーションデプロイ**- ウェブサーバー、API、フロントエンドを隔離されたコンテナとしてデプロイ
- 迅速なスケーリングと一貫したパフォーマンスを実現

## Dockerを始める

### インストール
公式DockerウェブサイトからWindows、macOS、またはLinux用のDocker Desktopをインストールします。

### Dockerfileの作成
Pythonアプリケーションの例:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### イメージのビルド
```bash
docker build -t my-python-app .
```

### コンテナの実行
```bash
docker run -d -p 5000:5000 my-python-app
```
- `-d`: デタッチモード
- `-p`: ホストポートをコンテナポートにマッピング

### イメージのプッシュ/プル
```bash
docker push username/my-python-app
docker pull username/my-python-app
```

### Docker Composeの使用
`docker-compose.yml`の例:
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

## ベストプラクティス

**イメージの最適化**- 公式/最小限のベースイメージを使用
- 不要なファイルを削除
- マルチステージビルドを実装してビルドとランタイムの依存関係を分離

**セキュリティ**- より良いセキュリティのために非rootユーザーを使用
- イメージの脆弱性を定期的にスキャン
- 最小権限の原則を適用

**設定管理**- 設定には環境変数を使用
- ハードコードされたシークレットを避ける
- セマンティックバージョニングでイメージにタグ付け

**モニタリングとロギング**- 簡単なデバッグのためにログを集中化
- コンテナの健全性とリソース使用状況を監視
- ヘルスチェックを実装

**データの永続化**- 永続的なデータにはボリュームを使用
- 重要なデータを定期的にバックアップ
- ステートフルコンポーネントとステートレスコンポーネントを分離

## AI基盤におけるDocker

**モデルのパッケージング**- コンテナは機械学習モデルと依存関係をカプセル化
- 環境間での再現可能なデプロイを保証

**リソース効率**- 同じハードウェア上で複数のデータパイプラインを隔離されたコンテナで実行
- リソース割り当てと利用を最適化

**スケーラブルなサービング**- AI推論サービスをスケーラブルで独立したコンテナとしてデプロイ
- 需要に基づいた水平スケーリングを実現

**CI/CD統合**- コンテナ化されたステージでテスト、検証、デプロイを自動化
- MLモデルデプロイパイプラインを合理化

**例:**データサイエンティストが訓練済みモデルとAPIを含むDockerイメージをビルドし、スケーラブルな推論のためにKubernetesにデプロイします。

## 高度なトピック

**コンテナオーケストレーション**- KubernetesとDocker Swarmがデプロイ、スケーリング、運用を管理
- サービスディスカバリ、ロードバランシング、自動スケーリング、自己修復を処理

**セキュリティの考慮事項**- 公式または検証済みパブリッシャーからの信頼できるイメージを使用
- イメージの脆弱性を定期的にスキャン
- コンテナの権限を制限し、機密ワークロードを隔離

**ネットワーキング**- Bridge: 単一ホストコンテナのデフォルトネットワーク
- Host: ホストのネットワークスタックを共有
- Overlay: マルチホスト通信を可能にする(オーケストレーターが使用)

## よく使用されるコマンド

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

## 主要な技術用語

**コンテナ:**名前空間やcgroupsなどのカーネル機能を使用して、アプリケーションと依存関係をカプセル化する隔離されたプロセス**Dockerイメージ:**コンテナを作成するための読み取り専用のレイヤー化されたテンプレート**Dockerfile:**Dockerイメージをビルドするための命令を含むスクリプト**Docker Daemon:**Dockerオブジェクトを管理するサービス**Docker Client:**Docker daemonと対話するためのCLIまたはAPI**レジストリ:**イメージを保存・配布するためのリポジトリ**名前空間:**プロセス分離のためのLinuxカーネル機能**ボリューム:**コンテナにマウントされる永続的ストレージ**ネットワーク:**コンテナ通信のための仮想ネットワーク

## 参考文献


1. Docker. (n.d.). Docker Overview. Docker Official Documentation. URL: https://docs.docker.com/get-started/docker-overview/

2. Docker. (n.d.). What is a Container?. Docker Official Documentation. URL: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/

3. Docker Curriculum. (n.d.). Docker Curriculum for Beginners to Advanced. URL: https://docker-curriculum.com

4. AWS. (n.d.). What is Docker?. AWS Documentation. URL: https://aws.amazon.com/docker/

5. Oracle. (n.d.). What is Docker?. Oracle Cloud Documentation. URL: https://www.oracle.com/cloud/cloud-native/container-registry/what-is-docker/

6. GeeksforGeeks. (n.d.). Containerization Using Docker. GeeksforGeeks Blog. URL: https://www.geeksforgeeks.org/blogs/containerization-using-docker/

7. Docker. (n.d.). Docker Compose Documentation. Docker Official Documentation. URL: https://docs.docker.com/compose/

8. Kubernetes. (n.d.). Kubernetes Documentation. URL: https://kubernetes.io/docs/

9. Docker. (n.d.). Docker CLI Reference. Docker Official Documentation. URL: https://docs.docker.com/engine/reference/commandline/cli/

10. Docker. (n.d.). Docker Development Best Practices. Docker Official Documentation. URL: https://docs.docker.com/develop/dev-best-practices/

11. Docker Hub. Container Registry Service. URL: https://hub.docker.com

12. Docker. (n.d.). Docker Networking. Docker Official Documentation. URL: https://docs.docker.com/network/

13. Docker. (n.d.). Docker Registry Documentation. Docker Official Documentation. URL: https://docs.docker.com/registry/

14. Docker. (n.d.). Docker for Machine Learning. Docker Blog. URL: https://www.docker.com/blog/tag/machine-learning/

15. Docker Scout. Container Security Scanning Tool. URL: https://docs.docker.com/scout/

16. Docker. (n.d.). Containers vs. Virtual Machines. Docker Official Documentation. URL: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms
