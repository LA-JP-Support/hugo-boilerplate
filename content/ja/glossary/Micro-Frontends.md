---
title: マイクロフロントエンド
date: 2025-11-25
translationKey: micro-frontends
description: マイクロフロントエンドは、Webアプリケーションをより小さな独立したフロントエンドアプリに分解し、スケーラブルで自律的なチームによって個別に開発・デプロイできるようにするアーキテクチャスタイルです。
keywords: ["マイクロフロントエンド", "フロントエンド開発", "マイクロフロントエンドアーキテクチャ", "Webアプリケーション", "独立デプロイ"]
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Micro-Frontends
term: まいくろふろんとえんど
reading: マイクロフロントエンド
kana_head: ま
---
## 定義

**マイクロフロントエンド**は、単一のアプリケーションを、独立して開発・テスト・デプロイ可能な小規模なフロントエンドアプリケーション(それぞれを*マイクロフロントエンド*と呼ぶ)に分解するウェブ開発のアーキテクチャスタイルです。これらのマイクロアプリは別々のチームが所有し、組み合わせることでシームレスなユーザー体験を創出します。

> 「独立してデリバリー可能なフロントエンドアプリケーションを組み合わせて、より大きな全体を構成するアーキテクチャスタイル」([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html))

この概念はマイクロサービスのパラダイムをフロントエンドに拡張し、その自律性とスケーラビリティの利点をもたらします。各マイクロフロントエンドは異なる技術で構築でき、異なるスケジュールでデプロイでき、さらには異なる組織単位によって保守することも可能です。
## 背景と進化

ウェブアプリケーションの複雑性が増すにつれ、フロントエンドのコードベースは大規模なモノリスへと成長し、スケールと保守が困難になりました。マイクロサービスがバックエンド開発に革命をもたらし、チームが独立したサービスで作業できるようになった一方で、フロントエンド開発は依然として密結合でモノリシックなままでした。

「マイクロフロントエンド」という用語は、[2016年のThoughtWorks Technology Radar](https://www.thoughtworks.com/radar/techniques/micro-frontends)で導入され、[Martin Fowler](https://martinfowler.com/articles/micro-frontends.html)によって広められました。この必要性は以下のような課題から生まれました:

- 新しいフレームワークや機能の統合の困難さ
- 大規模チームでの並行開発の課題
- レガシーUIの近代化における高いリスクとコスト

シングルページアプリケーション(SPA)が標準となるにつれ、フロントエンドのモジュール化の必要性が高まり、チームのスケーラビリティと技術スタックの柔軟性を実現するマイクロフロントエンドパターンの採用につながりました。

## コアコンセプト

### ビジネスドメインによる分解

マイクロフロントエンドは通常、アプリケーションの垂直スライス、つまり「検索」「カート」「プロフィール」などの機能やビジネスドメインを表します。それぞれがクロスファンクショナルチームによってエンドツーエンドで開発されます([micro-frontends.org](https://micro-frontends.org/))。

### チームの自律性

各マイクロフロントエンドチームは、開発、テスト、デプロイ、保守というソフトウェア開発ライフサイクル全体に責任を持ちます。この自律性により、デリバリーが加速し、ボトルネックが削減されます。

### 独立した技術選択

チームはマイクロフロントエンドごとに異なるフレームワーク、ライブラリ、さらにはプログラミング言語を選択できます。例えば、あるチームはReactを、別のチームはVue.jsを、さらに別のチームはAngularを使用することができます。

### 疎結合と明確な契約

マイクロフロントエンドは、明確に定義されたAPIとブラウザイベントを通じて通信し、共有グローバル状態を避けます。これにより偶発的な依存関係が減少し、統合が簡素化されます([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html#Cross-applicationCommunication))。

### ランタイム合成

個々のマイクロフロントエンドは実行時に全体のアプリケーションに合成され、シームレスなユーザー体験を創出します。これはサーバーサイドアセンブリ、クライアントサイド統合、またはハイブリッドアプローチによって実現できます。
## マイクロフロントエンドの利点

### 段階的なアップグレードとマイグレーション

大規模なモノリシックフロントエンドの移行はリスクが高く、時間がかかります。マイクロフロントエンドは「絞め殺しのイチジク」による近代化を可能にし、レガシーセクションを新しいマイクロフロントエンドで段階的に置き換えることで、移行リスクを削減します([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html#IncrementalUpgrades))。

### よりシンプルで疎結合なコードベース

各マイクロフロントエンドはより小規模で焦点が絞られているため、コードベースの理解、テスト、保守が容易になります。これにより開発者の認知負荷とエラー率が削減されます。

### 独立したデプロイ

チームはマイクロフロントエンドを独立してデプロイでき、リリースサイクルの高速化と調整オーバーヘッドの削減が可能になります。あるマイクロフロントエンドの修正や機能追加が、グローバルな再デプロイを必要としません。

### チームの自律性とスケーラビリティ

複数のチームが並行して機能を開発・出荷でき、デリバリーが加速し、開発能力がスケールします。これは複雑な製品を持つ大規模組織にとって不可欠です。

### 再利用性と柔軟性

マイクロフロントエンドは異なるアプリケーションや製品間で再利用できます。チームはアプリケーション全体に影響を与えることなく、新しいフレームワークや言語を試すことができます。

### 改善された回復力とパフォーマンス

あるマイクロフロントエンドの障害は隔離され、ユーザーへの影響が最小化されます。マイクロフロントエンドの遅延ロードにより、ルートごとに必要なものだけを配信することで、初期ロードパフォーマンスが向上します。
## 課題とデメリット

### 運用の複雑性の増加

各マイクロフロントエンドの複数のデプロイパイプライン、バージョン管理、監視の管理により、運用オーバーヘッドが発生します。チーム間の変更調整が複雑になる可能性があります。

### バンドルサイズと重複

チームが同じライブラリの異なるバージョンを使用すると、依存関係の重複によりバンドルサイズが増加し、ロード時間が遅くなる可能性があります([martinfowler.com](https://martinfowler.com/articles/micro-frontends.html#PayloadSize))。

### ガバナンスと一貫性

技術選択の自由度が高すぎると「フレームワーク無政府状態」につながり、一貫したユーザー体験の維持が困難になり、保守コストが増加します。

### CSSとグローバル名前空間の競合

慎重な隔離(CSSモジュール、Shadow DOM、厳格な命名規則の使用など)がないと、スタイルや[グローバル変数](/ja/glossary/global-variables/)がマイクロフロントエンド間で漏洩し、バグや視覚的な不整合を引き起こす可能性があります。

### アプリケーション間通信

複雑なワークフローにおいて、マイクロフロントエンド間の堅牢で疎結合な通信メカニズムを定義することは容易ではありません。

### テストと品質保証

独立してデプロイされた部品から組み立てられたアプリケーションのエンドツーエンド品質を確保するには、効果的な統合テストと回帰テスト戦略が必要です。
## アーキテクチャパターンと統合アプローチ

マイクロフロントエンドはいくつかの方法で合成でき、それぞれに独自の長所と短所があります。

### 1. サーバーサイドテンプレート合成

サーバーが各マイクロフロントエンドから提供されるフラグメントやパーシャルから最終的なHTMLページを組み立てます。  
- **例:** [Nginx SSI](https://nginx.org/en/docs/http/ngx_http_ssi_module.html)  
- **長所:** 強力な隔離、ユニバーサルレンダリング、最小限のクライアントサイドJS  
- **短所:** インタラクティビティの制限、粗い更新、動的UIには遅い  
- **参考:** [martinfowler.com/articles/micro-frontends.html#Server-sideTemplateComposition](https://martinfowler.com/articles/micro-frontends.html#Server-sideTemplateComposition)

### 2. ビルド時統合

マイクロフロントエンドはライブラリ(npmパッケージ)として公開され、ビルド時に「コンテナ」アプリケーションによってインポートされます。  
- **長所:** 重複排除された依存関係、最適化されたバンドル  
- **短所:** 独立したデプロイが失われる、調整されたリリースが必要  
- **参考:** [martinfowler.com/articles/micro-frontends.html#Build-timeIntegration](https://martinfowler.com/articles/micro-frontends.html#Build-timeIntegration)

### 3. ランタイム統合

**a. iframe**  
各マイクロフロントエンドはiframeにロードされ、コンテナアプリケーションがどのiframeを表示するかを管理します。  
- **長所:** 最大限の隔離、セキュリティ  
- **短所:** 不器用なナビゲーション、通信の困難さ、パフォーマンスオーバーヘッド  
- **参考:** [martinfowler.com/articles/micro-frontends.html#Run-timeIntegrationViaIframes](https://martinfowler.com/articles/micro-frontends.html#Run-timeIntegrationViaIframes)

**b. JavaScriptエントリーポイント**  
各マイクロフロントエンドはグローバルなレンダー関数を公開します。コンテナアプリがバンドルをロードし、関数を呼び出してマイクロフロントエンドをマウントします。  
- **長所:** 柔軟性、独立したデプロイ  
- **短所:** 名前空間の衝突、依存関係管理  
- **参考:** [martinfowler.com/articles/micro-frontends.html#Run-timeIntegrationViaJavascript](https://martinfowler.com/articles/micro-frontends.html#Run-timeIntegrationViaJavascript)

**c. Web Components(カスタム要素)**  
マイクロフロントエンドはカスタムHTML要素として配布され、カプセル化のためにShadow DOMを活用します。  
- **長所:** 強力なカプセル化、技術スタック非依存、ネイティブブラウザサポート  
- **短所:** ブラウザ互換性(モダンブラウザは問題なし)、高度な通信が複雑になる可能性  
- **参考資料:**  
  - [Custom Elements入門](https://developers.google.com/web/fundamentals/web-components/customelements)  
  - [micro-frontends.org - DOM is the API](https://micro-frontends.org/#the-dom-is-the-api)  
  - [martinfowler.com/articles/micro-frontends.html#Run-timeIntegrationViaWebComponents](https://martinfowler.com/articles/micro-frontends.html#Run-timeIntegrationViaWebComponents)

**d. Module Federation(Webpack 5+)**  
別々にビルド・デプロイされたアプリケーション間でコードのランタイムロードと共有を可能にします。  
- **長所:** 動的ロード、きめ細かい共有  
- **短所:** 慎重な設定と運用規律が必要  
- **参考資料:**  
  - [Webpack Module Federation](https://webpack.js.org/concepts/module-federation/)  
  - [martinfowler.com/articles/micro-frontends.html](https://martinfowler.com/articles/micro-frontends.html)

## 技術的詳細と例

### 例: フードデリバリーアプリケーション

**ページ:**  
- *レストラン閲覧*: 検索とフィルターオプション  
- *注文ページ*: メニュー項目の選択、注文のカスタマイズ、チェックアウト  
- *ユーザープロフィール*: アカウント設定の管理、注文履歴  

**チーム構造:**  
各ページはマイクロフロントエンドであり、専任チームが所有・運用します。

**統合:**  
コンテナアプリがグローバルレイアウト、ナビゲーション、共有サービスを提供します。マイクロフロントエンドはユーザーのナビゲーションに応じて動的にロードされます。

**Web Componentsコード例:**
```js
class BrowseRestaurants extends HTMLElement { /* ... */ }
window.customElements.define('browse-restaurants', BrowseRestaurants);

class OrderFood extends HTMLElement { /* ... */ }
window.customElements.define('order-food', OrderFood);

class UserProfile extends HTMLElement { /* ... */ }
window.customElements.define('user-profile', UserProfile);
```

**コンテナでの合成:**
```html
<div id="main">
  <browse-restaurants></browse-restaurants>
  <!-- または必要に応じて動的に<order-food>や<user-profile>を挿入 -->
</div>
```

**通信:**  
マイクロフロントエンド間のインタラクションには、ブラウザネイティブの[CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent)、ローカルストレージ、またはイベントバスを使用します。
## ベストプラクティスと設計原則

- **技術非依存性:** チームはスタックを独立して選択・アップグレードできるべきです。統合境界にはブラウザ標準(カスタム要素)を使用します([micro-frontends.org](https://micro-frontends.org/#core-ideas-behind-micro-frontends))。
- **チーム/コードの隔離:** 共有グローバルとランタイム依存関係を避けます。CSS、イベント、ストレージに名前空間を設定して衝突を防ぎます。
- **堅牢性:** 回復力とパフォーマンスのために、ユニバーサル/サーバーサイドレンダリングとプログレッシブエンハンスメントをサポートします。
- **通信パターン:** 疎結合な通信のために、カスタムAPIよりもネイティブブラウザイベントを優先します。
- **共有コンポーネントライブラリ:** 視覚的一貫性のために中央ライブラリを使用しますが、競合を防ぐためにカプセル化を確保します。
- **フレームワークガバナンス:** チームの柔軟性をサポートしながら、断片化を避けるために最小限のフレームワークと規約のセットで合意します。
## マイクロフロントエンド組織の種類

### モノレポ

すべてのマイクロフロントエンドを単一のリポジトリに配置。  
- **長所:** コード共有が容易、アトミックコミット、統一されたCI/CD  
- **短所:** 扱いにくくなる可能性、結合のリスク、ビルドの遅延

### マルチレポ

各マイクロフロントエンドを独自のリポジトリに配置。  
- **長所:** 強力な自律性、独立したパイプライン  
- **短所:** コード共有とリポジトリ間の変更調整が困難

### メタレポ

ハイブリッドアプローチ: 複数のマイクロフロントエンドリポジトリと調整用のメタリポジトリ。  
- **長所:** 自律性と共有ガバナンスのバランス  
- **短所:** 追加のツールと調整が必要
## 使用すべき場合(使用すべきでない場合)

### 使用すべき場合

- 明確なビジネスドメインを持つ大規模で複雑なウェブアプリ
- 独立したデリバリーサイクルを必要とする複数のチーム
- レガシーモノリスからの段階的移行
- 長期的な保守性と機能進化

### 使用すべき*でない*場合

- 小規模または単一チームのアプリケーション
- 不安定または急速に進化するビジネスドメイン
- 組織的オーバーヘッドがモジュール性の利点を上回る場合
- 要件が変化する迅速なプロトタイピング/スタートアップ
## ユースケースと例

- **Eコマース:** 製品カタログ、カート、アカウントを別々のマイクロフロントエンドとして
- **フードデリバリー:** 閲覧、注文、ユーザープロフィールを個別のマイクロフロントエンドとして
- **エンタープライズポータル:** ダッシュボード、分析、管理モジュールを独立してビルド/デプロイ
- **SaaSプラットフォーム:** 独立して開発された機能を単一製品に統合
## 比較表: モノリシック vs. マイクロフロントエンドアーキテクチャ

| 側面                 | モノリシックフロントエンド           | マイクロフロントエンドアーキテクチャ    |
|----------------------|-------------------------------------|-------------------------------------|
| **コードベース**     | 単一、大規模、密結合                | 複数、小規模、疎結合                |
| **デプロイ**         | 全か無か、グローバルリリース        | 独立した段階的リリース              |
| **チーム構造**       | 集中型、チーム間結合                | 分散型、垂直的所有権                |
| **技術スタック**     | すべてに対して単一スタック          | 柔軟、マイクロフロントエンドごと    |
| **スケーリング**     | チームと機能のスケールが困難        | チーム/機能が独立してスケール       |
| **マイグレーション** | 困難、高リスク                      | 段階的、低リスク                    |

## 用語集

- **マイクロフロントエンド:** ビジネスドメインを担当する自己完結型のフロントエンドモジュールで、独立して開発・デプロイされます。
- **コンテナアプリ(シェル):** マイクロフロントエンドをロード・合成し、共有レイアウトとサービスを処理するホストアプリケーション。
- **垂直スライス:** 単一チームによる、UIからバックエンドまでの機能またはビジネスドメインのエンドツーエンド所有権。
- **カスタム要素:** Web Componentの一種。JavaScriptで定義される再利用可能でカプセル化されたカスタムHTMLタグ。
- **Module Federation:** Webpack 5の機能で、アプリ間でモジュールのランタイムロードと共有を可能にします。

## 参考資料

- [Martin Fowler: Micro Frontends](https://martinfowler.com/articles/micro-frontends.html)
- [Micro-Frontends.org](https://micro-frontends.org/)
- [Wikipedia: Micro Frontend](https://en.wikipedia.org/wiki/Micro_frontend)
- [ThoughtWorks Technology Radar: Micro Frontends](https://www.thoughtworks.com/radar/techniques/micro-frontends)
- [Webpack: Module Federation](https://webpack.js.org/concepts/module-federation/)
- [Custom Elements - Google Developers](https://developers.google.com/web/fundamentals/web-components/customelements)
- [YouTube: Edge-Side Includes explained (7:22から)](https://youtu.be/A3n1n5QRmF0?t=442)

## 関連用語

マイクロサービス、シングルページアプリケーション(SPA)、Web Components、Shadow DOM、プログレッシブエンハンスメント、ユニバーサルレンダリング、垂直スライス、モノリシックフロントエンド、Module Federation

*実践的なパターンと実装の詳細については、[martinfowler.com/articles/micro-frontends.html](https://martinfowler.com/articles/micro-frontends.html)と[micro-frontends.org](https://micro-frontends.org/)を参照してください。*

**この用語集は、マイクロフロントエンド、その根拠、パターン、ベストプラクティスについて、包括的で詳細かつ参照リンク付きの概要を提供します。より深い技術的考察と実世界のケーススタディについては、常に[micro-frontends.org](https://micro-frontends.org/)と```js
class BrowseRestaurants extends HTMLElement { /* ... */ }
window.customElements.define('browse-restaurants', BrowseRestaurants);

class OrderFood extends HTMLElement { /* ... */ }
window.customElements.define('order-food', OrderFood);

class UserProfile extends HTMLElement { /* ... */ }
window.customElements.define('user-profile', UserProfile);
```を参照してください。**