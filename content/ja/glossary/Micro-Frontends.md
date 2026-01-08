---
title: マイクロフロントエンド
date: '2025-12-19'
lastmod: '2025-12-19'
translationKey: micro-frontends
description: マイクロフロントエンドは、Webアプリケーションをより小さく独立して開発・デプロイ可能なフロントエンドアプリに分解するアーキテクチャスタイルで、スケーラブルで自律的なチーム運営を実現します。
keywords:
- マイクロフロントエンド
- フロントエンド開発
- マイクロフロントエンドアーキテクチャ
- Webアプリケーション
- 独立デプロイ
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Micro-Frontends
term: まいくろふろんとえんど
url: "/ja/glossary/Micro-Frontends/"
---
## Micro-Frontendsとは?
Micro-Frontendsは、単一のWebアプリケーションを、独立して開発、テスト、デプロイされる小さなフロントエンドアプリケーションに分解するアーキテクチャスタイルです。各アプリケーションは別々のチームが所有し、それらを組み合わせてシームレスなユーザー体験を創出します。このアプローチは、マイクロサービスのパラダイムをフロントエンドに拡張し、Webアプリケーション開発に自律性、スケーラビリティ、技術的柔軟性をもたらします。

各Micro-Frontendは異なるフレームワークで構築でき、異なるスケジュールでデプロイでき、異なる組織単位で保守できます。これにより、チームは独立して作業しながら、統一されたアプリケーションに貢献できます。このアーキテクチャは、アプリケーションの複雑さが増し、チームサイズが拡大する際のフロントエンド開発のスケーリングという課題に対処します。

## 歴史的背景

Webアプリケーションの複雑さが増すにつれ、フロントエンドのコードベースは大規模なモノリスへと進化し、スケーリングと保守が困難になりました。マイクロサービスが独立したサービスを通じてバックエンド開発に革命をもたらした一方で、フロントエンド開発は依然として密結合でモノリシックなままでした。

「Micro-Frontends」という用語は、2016年にThoughtWorks Technology Radarで紹介され、その後Martin Fowlerによって広められました。このアプローチは、新しいフレームワークの統合の難しさ、大規模チームでの並行開発の課題、レガシーUIの近代化における高いリスクといった課題から生まれました。

Single-Page Applicationsが標準となるにつれ、フロントエンドのモジュール化の必要性が高まり、チームのスケーラビリティと技術スタックの柔軟性を可能にするMicro-Frontendパターンの採用につながりました。

## 中核原則

### ドメインベースの分解

Micro-Frontendsは通常、機能やビジネスドメイン(「検索」「カート」「プロフィール」など)の垂直的なスライスを表します。各々は、特定のビジネス機能に責任を持つクロスファンクショナルチームによってエンドツーエンドで開発されます。

### チームの自律性

各Micro-Frontendチームは、開発、テスト、デプロイ、保守という完全なソフトウェア開発ライフサイクルを所有します。この自律性により、デリバリーが加速し、ボトルネックが減少し、チームは自分のドメインに適した技術的決定を行えます。

### 独立した技術選択

チームは、Micro-Frontendごとに異なるフレームワーク、ライブラリ、さらにはプログラミング言語を選択できます。あるチームはReactを使用し、別のチームはVue.js、さらに別のチームはAngularを使用できます。各々が特定の要件に最適化されています。

### 疎結合

Micro-Frontendsは、明確に定義されたAPIとブラウザイベントを通じて通信し、共有グローバル状態を避けます。これにより、偶発的な依存関係が減少し、統合が簡素化され、コンポーネントの独立した進化が可能になります。

### ランタイム合成

個々のMicro-Frontendsは、ランタイムで全体のアプリケーションに合成され、シームレスなユーザー体験を創出します。合成は、サーバーサイドアセンブリ、クライアントサイド統合、またはハイブリッドアプローチを通じて行われます。

## 主な利点

<strong>段階的な近代化:</strong>「strangler figパターン」を可能にし、レガシーセクションを新しいMicro-Frontendsで段階的に置き換えることで、ビッグバン書き換えと比較して移行リスクを軽減します。

<strong>シンプルなコードベース:</strong>各Micro-Frontendは小さく、より焦点が絞られており、開発者の認知負荷とエラー率を削減します。理解、テスト、保守が容易になります。

<strong>独立したデプロイ:</strong>チームはMicro-Frontendsを独立してデプロイでき、リリースサイクルの高速化と調整オーバーヘッドの削減を実現します。修正や機能追加にグローバルな再デプロイは不要です。

<strong>チームのスケーラビリティ:</strong>複数のチームが並行して機能を開発・出荷でき、デリバリーを加速し、開発能力をスケールします。複雑な製品を持つ大規模組織にとって不可欠です。

<strong>技術的柔軟性:</strong>チームはアプリケーション全体に影響を与えることなく、新しいフレームワークや言語を試すことができます。新興技術を段階的に採用しやすくなります。

<strong>回復力の向上:</strong>1つのMicro-Frontendの障害は隔離され、ユーザーへの影響を最小限に抑えます。遅延ロードにより、ルートごとに必要なコンポーネントのみを配信し、初期ロードパフォーマンスが向上します。

## 課題とトレードオフ

<strong>運用の複雑さ:</strong>複数のデプロイパイプライン、バージョン管理、監視の管理はオーバーヘッドを生じます。チーム間の変更調整が複雑になる可能性があります。

<strong>バンドルサイズの懸念:</strong>異なるライブラリバージョンにより、依存関係の重複によってバンドルサイズが増加し、ロード時間が遅くなる可能性があります。慎重な依存関係管理が必要です。

<strong>ガバナンスのバランス:</strong>技術的自由度が高すぎると「フレームワーク無秩序」につながり、一貫したユーザー体験が困難になり、保守コストが増加します。過度な制約なしにガバナンスが必要です。

<strong>CSSと名前空間管理:</strong>分離(CSSモジュール、Shadow DOM、厳格な規約)がないと、スタイルやグローバル変数がMicro-Frontends間で漏れ、バグや視覚的不整合を引き起こします。

<strong>通信の複雑さ:</strong>Micro-Frontends間の堅牢で疎結合な通信メカニズムの定義は容易ではなく、特に調整を必要とする複雑なワークフローでは困難です。

<strong>テスト要件:</strong>独立してデプロイされた部品から組み立てられるアプリケーションのエンドツーエンド品質を確保するには、効果的な統合テストと回帰テスト戦略が必要です。

## 統合パターン

### サーバーサイドテンプレート合成

サーバーが各Micro-Frontendから提供されるフラグメントから最終的なHTMLページを組み立てます。

<strong>利点:</strong>強力な分離、ユニバーサルレンダリング、最小限のクライアントサイドJavaScript。

<strong>欠点:</strong>限定的なインタラクティビティ、粗い更新、動的UIには遅い。

<strong>例:</strong>Nginx SSI (Server Side Includes)。

### ビルドタイム統合

Micro-Frontendsをライブラリ(npmパッケージ)として公開し、ビルド時にコンテナアプリケーションがインポートします。

<strong>利点:</strong>重複排除された依存関係、最適化されたバンドル。

<strong>欠点:</strong>独立したデプロイを失い、調整されたリリースが必要。

### ランタイム統合

<strong>Iframes:</strong>各Micro-Frontendがiframe内にロードされ、コンテナが可視性を管理します。
- 長所: 最大限の分離、セキュリティ
- 短所: 不器用なナビゲーション、貧弱な通信、パフォーマンスオーバーヘッド

<strong>JavaScriptエントリポイント:</strong>各Micro-Frontendがコンテナによって呼び出されるグローバルレンダー関数を公開します。
- 長所: 柔軟性、独立したデプロイ
- 短所: 名前空間の衝突、依存関係管理の課題

<strong>Web Components:</strong>Shadow DOMを活用したカプセル化によりカスタムHTML要素として配布されます。
- 長所: 強力なカプセル化、技術スタック非依存、ネイティブブラウザサポート
- 短所: 高度な通信の複雑さ

<strong>Module Federation (Webpack 5+):</strong>個別にビルドされたアプリケーション間でのコードのランタイムロードと共有。
- 長所: 動的ロード、きめ細かい共有
- 短所: 慎重な設定と運用規律が必要

## 実装例

### フードデリバリーアプリケーションアーキテクチャ

<strong>ドメイン分解:</strong>- レストラン閲覧: 検索とフィルタリング機能
- 注文ページ: メニュー選択、カスタマイズ、チェックアウト
- ユーザープロフィール: アカウント設定、注文履歴

<strong>チーム構造:</strong>各ページは専任チームが所有するMicro-Frontendです。

<strong>統合:</strong>コンテナアプリがグローバルレイアウト、ナビゲーション、共有サービスを提供します。Micro-Frontendsはユーザーがナビゲートする際に動的にロードされます。

<strong>Web Components実装:</strong>```javascript
class BrowseRestaurants extends HTMLElement {
  connectedCallback() {
    this.innerHTML = '<div>Restaurant browsing interface</div>';
  }
}
window.customElements.define('browse-restaurants', BrowseRestaurants);

class OrderFood extends HTMLElement {
  connectedCallback() {
    this.innerHTML = '<div>Order management interface</div>';
  }
}
window.customElements.define('order-food', OrderFood);
```

**コンテナ合成:**```html
<div id="main">
  <browse-restaurants></browse-restaurants>
  <!-- ルーティングに基づいてコンポーネントを動的に切り替え -->
</div>
```

<strong>通信:</strong>ブラウザネイティブのCustomEvent、ローカルストレージ、またはイベントバスを使用して、疎結合を維持しながらMicro-Frontends間のインタラクションを実現します。

## ベストプラクティス

<strong>技術非依存性:</strong>チームが独立してスタックを選択・アップグレードできるようにします。統合境界にはブラウザ標準(Custom Elements)を使用します。

<strong>コード分離:</strong>共有グローバルとランタイム依存関係を避けます。CSS、イベント、ストレージに名前空間を設定し、衝突を防ぎます。

<strong>堅牢性:</strong>回復力とパフォーマンスのために、ユニバーサル/サーバーサイドレンダリングとプログレッシブエンハンスメントをサポートします。

<strong>通信パターン:</strong>Micro-Frontends間の疎結合な通信には、カスタムAPIよりもネイティブブラウザイベントを優先します。

<strong>共有コンポーネントライブラリ:</strong>視覚的一貫性のために中央ライブラリを使用しますが、競合を防ぐカプセル化を確保します。

<strong>フレームワークガバナンス:</strong>断片化を避けるために最小限のフレームワークと規約のセットに合意しつつ、チームの柔軟性をサポートします。

<strong>パフォーマンス監視:</strong>Micro-Frontends全体でバンドルサイズ、ロード時間、ランタイムパフォーマンスを追跡し、最適化の機会を特定します。

## リポジトリ構成

<strong>Monorepo:</strong>すべてのMicro-Frontendsを単一リポジトリに配置。
- 長所: コード共有が容易、アトミックコミット、統一されたCI/CD
- 短所: 扱いにくくなる可能性、結合のリスク、ビルドが遅い

<strong>Multirepo:</strong>各Micro-Frontendを独自のリポジトリに配置。
- 長所: 強力な自律性、独立したパイプライン
- 短所: コード共有が困難、リポジトリ間の変更調整が難しい

<strong>Metarepo:</strong>複数のリポジトリと調整用のメタリポジトリを組み合わせたハイブリッドアプローチ。
- 長所: 自律性と共有ガバナンスのバランス
- 短所: 追加のツールと調整が必要

## 使用すべき場合

<strong>適切なシナリオ:</strong>- 明確なビジネスドメインを持つ大規模で複雑なWebアプリ
- 独立したデリバリーサイクルを必要とする複数のチーム
- レガシーモノリスからの段階的移行
- 長期的な保守性と機能進化の要件

<strong>不適切なシナリオ:</strong>- 小規模または単一チームのアプリケーション
- 不安定または急速に進化するビジネスドメイン
- 組織的オーバーヘッドがモジュール化の利点を上回る場合
- 要件が変化する迅速なプロトタイピングやスタートアップ

## ユースケース

<strong>Eコマース:</strong>商品カタログ、カート、アカウントを個別のMicro-Frontendsとして、各ドメインに特化したチームを可能にします。

<strong>フードデリバリー:</strong>閲覧、注文、ユーザープロフィールを個別のMicro-Frontendsとして、特定のワークフローに最適化します。

<strong>エンタープライズポータル:</strong>ダッシュボード、分析、管理モジュールを独立して構築・デプロイし、異なるリリースサイクルをサポートします。

<strong>SaaSプラットフォーム:</strong>チームの自律性を維持しながら、独立して開発された機能を単一の製品に統合します。

## アーキテクチャ比較

| 側面 | モノリシックフロントエンド | Micro-Frontendアーキテクチャ |
|--------|--------------------|-----------------------------|
| <strong>コードベース</strong>| 単一、大規模、密結合 | 複数、小規模、疎結合 |
| <strong>デプロイ</strong>| オールオアナッシングリリース | 独立した段階的リリース |
| <strong>チーム構造</strong>| 集中型、チーム間結合 | 分散型、垂直的所有権 |
| <strong>技術スタック</strong>| すべてに1つのスタック | Micro-Frontendごとに柔軟 |
| <strong>スケーリング</strong>| チーム/機能で困難 | チーム/機能が独立してスケール |
| <strong>移行</strong>| 高リスク、困難 | 段階的、低リスク |

## 参考文献


1. Fowler, M. (n.d.). Micro Frontends. Martin Fowler.

2. Micro-Frontends.org. (n.d.). Micro Frontends. Micro-Frontends.org.

3. Wikipedia. (n.d.). Micro Frontend. Wikipedia.

4. ThoughtWorks. (n.d.). Micro Frontends. ThoughtWorks Technology Radar.

5. Webpack. (n.d.). Module Federation. Webpack Documentation.

6. Google. (n.d.). Custom Elements. Google Web Fundamentals.

7. Nginx. (n.d.). Server Side Includes Module. Nginx Documentation.

8. Mozilla. (n.d.). CustomEvent. MDN Web Docs.

9. YouTube. (n.d.). Edge-Side Includes. YouTube Video.
