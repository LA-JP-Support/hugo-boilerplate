---
title: 埋め込みスクリプト：用語集と包括的ガイド
translationKey: embed-script-glossary-comprehensive-guide
description: 埋め込みスクリプトについて学びましょう。AIチャットボットや動的コンテンツをあらゆるウェブサイトに統合するために使用されるJavaScriptスニペットです。使用方法、例、カスタマイズ、ベストプラクティスをご紹介します。
keywords:
- 埋め込みスクリプト
- チャットボット
- JavaScript
- ウェブサイト統合
- AI自動化
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: うめこみスクリプト：ようごしゅうとほうかつてきガイド
reading: 埋め込みスクリプト：用語集と包括的ガイド
kana_head: その他
e-title: 'Embed Script: Glossary & Comprehensive Guide'
---

## Embed Scriptとは何か?

**Embed Script(埋め込みスクリプト)**とは、ウェブサイトのHTMLに挿入される、コンパクトで自己完結型のJavaScriptスニペットで、動的なサードパーティコンテンツ(主にAIチャットボットやウィジェット)を読み込んで表示します。サイトに追加されると、スクリプトはプロバイダーのサーバーからチャットボットのコードとリソースを取得し、ブラウザ上でウィジェットをレンダリングします。

**主な特徴:**
- **プラグアンドプレイ:** HTMLにコピー&ペーストするだけで、高度なコーディングは不要。
- **動的:** プロバイダーから依存関係とUIをオンザフライで読み込む。
- **独立性:** サンドボックス化されたブラウザコンテキストで実行され、他のサイト要素への干渉リスクを最小限に抑える。
- **汎用性:** カスタムHTMLまたはJavaScriptを許可する、ほぼすべてのウェブサイトプラットフォームで動作。

**AIチャットボット&自動化のコンテキスト:**  
Embed Scriptを使用することで、AIを活用したチャットボットを、営業、サポート、リード獲得、エンゲージメントのために、サイトやウェブアプリに直接デプロイできます。訪問者はチャットボットとリアルタイムでやり取りし、自動化されたパーソナライズされた応答を受け取ります。

**参考資料:**  
- [Chatbase JavaScript Embed Script Guide](https://chatbase.co/docs/developer-guides/javascript-embed)
- [ChatBot.com Widget API](https://www.chatbot.com/docs/chat-widget-api/)
- [Pickaxe: How to Embed AI Chatbots](https://pickaxe.co/post/how-to-embed-ai-chatbots-into-your-website-a-step-by-step-guide)

## Embed Scriptの使用方法

### 基本的な統合

ほとんどのチャットボットプロバイダーは、アカウントまたはインスタンスに紐付けられた、すぐに使用できるEmbed Scriptを提供しています。基本的なワークフローは以下の通りです:

1. **Embed Scriptの取得:**  
   - ダッシュボードにサインイン(例:[Chatbase](https://chatbase.co/)、[ChatBot.com](https://www.chatbot.com/)、[Pickaxe](https://pickaxe.co/))。
   - 「Deploy」、「Publish」、または「Integrations」セクションに移動。
   - 提供されたJavaScriptスニペットをコピー([Chatbaseの例](https://chatbase.co/docs/developer-guides/javascript-embed#quick-start-guide))。

2. **ウェブサイトへの追加:**  
   - スクリプトをHTMLの`<head>`内、または最適なパフォーマンスのために`</body>`タグの直前に貼り付ける。
   - 保存してサイトを再デプロイまたは更新。

**例:**
```html
<!-- Chatbase Example Embed Script -->
<script src="https://www.chatbase.co/embed.min.js" agent-id="YOUR_AGENT_ID" async></script>
```
または高度な設定の場合:
```html
<script>
  window.chatbaseConfig = {
    agentId: 'YOUR_AGENT_ID',
    user: { name: 'Jane Doe', email: 'jane@example.com' }
  };
</script>
<script src="https://www.chatbase.co/embed.min.js" async></script>
```
**結果:**  
ウェブサイトにチャットバブルが表示され、訪問者に即座にAI駆動のインタラクションを提供します。

**参考資料:**  
- [Chatbase: JavaScript Embed Script Guide](https://chatbase.co/docs/developer-guides/javascript-embed)
- [Pickaxe Step-by-Step Guide](https://pickaxe.co/post/how-to-embed-ai-chatbots-into-your-website-a-step-by-step-guide)

### 高度な統合方法

基本的な埋め込みを超えて、スクリプトはより深い統合をサポートします:

- **本人確認:**  
  ユーザーデータ(名前、メール、ユーザーIDなど)を渡して、パーソナライズされた挨拶、コンテキストに応じた応答、安全なアクションを実現。  
  [Chatbase Identity Verificationを参照](https://chatbase.co/docs/developer-guides/identity-verification)

- **イベントリスナー:**  
  ユーザーまたはボットのアクション(会話のログ記録、アナリティクスのトリガー、ウィジェットのプログラム的な開閉など)に反応。  
  ```javascript
  window.chatbase.addEventListener("user-message", (event) => {
    console.log("User said:", event.content);
    // カスタムロジック
  });
  ```
  [Chatbase Event Listeners](https://chatbase.co/docs/developer-guides/javascript-embed#advanced-features)

- **カスタムアクション:**  
  チャットインターフェースからフォーム、ワークフロー、またはAPI呼び出しをトリガー。

- **動的コンテンツ:**  
  ページコンテンツやユーザーセッションに基づいて、挨拶、ウィジェットの外観、会話コンテキストを変更。

- **ウィジェット制御(API):**  
  JS APIを使用してウィジェットをプログラム的に開く、閉じる、非表示にする、または破棄([ChatBot.com Widget API](https://www.chatbot.com/docs/chat-widget-api/)を参照):
  ```javascript
  OpenWidget.call('maximize');    // チャットを開く
  OpenWidget.call('minimize');    // チャットを最小化
  OpenWidget.call('hide');        // チャットを非表示
  OpenWidget.call('destroy');     // チャットを削除
  ```

### プラットフォーム固有の使用方法

**WordPress:**  
- 公式プラグインを使用(例:[ChatBot.com for WordPress](https://wordpress.org/plugins/chatbot/))。
- プラグイン設定でAPIキーまたはエージェントIDを入力。
- 手動でのスクリプト編集は不要。

**Shopify、Wix、Squarespace:**  
- アプリマーケットプレイスを使用するか、テーマ/カスタムコードセクション経由で埋め込みコードを挿入。
- [Shopifyアプリの例](https://apps.shopify.com/)、[Wixカスタムコードガイド](https://support.wix.com/en/article/embedding-custom-code-to-your-site)。

**カスタムHTML/CMS:**  
- テンプレートファイルまたはコードインジェクターに埋め込みコードを直接貼り付け。

**Knack、Webflow、ノーコードビルダー:**  
- HTMLが制限されている場合、JavaScriptを介してスクリプトを動的に注入:
  ```javascript
  (function() {
      var script = document.createElement('script');
      script.src = 'https://cdn.customgpt.ai/js/chat.js';
      script.defer = true;
      script.onload = function() {
          CustomGPT.init({
              p_id: '#####',  // プロジェクトID
              p_key: '################' // プロジェクトキー
          });
      };
      document.head.appendChild(script);
  })();
  ```
  ([Knack Communityの例](https://forums.knack.com/t/embed-chatbot/18777))

**参考資料:**  
- [Chatbase Embed Guide](https://chatbase.co/docs/developer-guides/javascript-embed)
- [Knack Community: Embed Chatbot](https://forums.knack.com/t/embed-chatbot/18777)
- [ChatBot.com Install Guide](https://www.chatbot.com/help/install-chatbot/widget-installation/)

## Embed Scriptの例

### 基本的なチャットボットEmbed Script

```html
<script src="https://cdn.example.com/chatbot.js" defer></script>
<script>
  window.ChatBot.init({
    apiKey: 'YOUR_API_KEY',
    position: 'bottom-right',
    language: 'en'
  });
</script>
```

### 本人確認付きEmbed Script

```html
<script src="https://cdn.chatbase.co/widget.js" defer></script>
<script>
  window.chatbaseConfig = {
    agentId: 'AGENT_ID',
    user: {
      name: 'Jane Doe',
      email: 'jane@example.com'
    }
  };
</script>
```
([Chatbase Identity Verification](https://chatbase.co/docs/developer-guides/identity-verification))

### 動的スクリプト注入(HTML制限のあるプラットフォーム向け)

```javascript
(function() {
  var script = document.createElement('script');
  script.src = 'https://cdn.customgpt.ai/js/chat.js';
  script.defer = true;
  script.onload = function() {
    CustomGPT.init({
      p_id: '#####',  // プロジェクトIDに置き換え
      p_key: '################'  // プロジェクトキーに置き換え
    });
  };
  document.head.appendChild(script);
})();
```
([Knack Communityの例](https://forums.knack.com/t/embed-chatbot/18777))

## 一般的な使用例

| 使用例                | 説明                                                                                   | プラットフォーム例             |
|-------------------------|----------------------------------------------------------------------------------------|-------------------------------|
| カスタマーサポート        | FAQやサポートクエリに対して即座に自動回答を提供。                              | Quidget、Chatbase、ChatBot.com|
| リード獲得         | 質問をして連絡先情報を収集することでリードを選別。              | Drift、Intercom、Chatbase     |
| Eコマースアシスタンス   | 買い物客をガイドし、商品を推奨し、リアルタイムでパーソナライズされた割引を提供。            | Shopify、WooCommerce          |
| ナレッジベース検索   | ユーザーがチャットボットウィジェットから直接ドキュメントや製品情報を検索できるようにする。              | ChatBot.com、Freshdesk        |
| 社内ツール          | イントラネットやSaaSダッシュボード内で従業員のオンボーディングやITヘルプデスク用にチャットボットを埋め込む。     | カスタムHTML、Webflow          |
| 多言語サポート    | チャットボットの言語設定を構成することで、複数の言語で顧客にサービスを提供。          | Quidget、Chatbase             |
| 予約スケジューリング  | 予約またはカレンダーウィジェットをチャットに統合して、スムーズなスケジューリングを実現。               | Calendly、Acuity(チャットボット経由)  |
| アクセシビリティ           | 障害を持つユーザーを含むすべてのユーザーがチャットボットとやり取りできるようにする。          | すべての最新プラットフォーム          |

**参考資料:**  
- [Pickaxe Guide: Use Cases](https://pickaxe.co/post/how-to-embed-ai-chatbots-into-your-website-a-step-by-step-guide)
- [ChatBot.com Use Cases](https://www.chatbot.com/solutions/)

## 主な機能とカスタマイズオプション

### 機能比較表

| 機能                     | 基本Embed Script | 高度な統合 | プラットフォームプラグイン/アプリ |
|-----------------------------|-------------------|---------------------|--------------------|
| クイックコピー&ペースト設定      | ✔️                | ✔️                  | ✔️                 |
| 外観のカスタマイズ    | ✔️                | ✔️                  | ✔️(UIベース)      |
| 位置制御            | ✔️                | ✔️                  | ✔️                 |
| カスタム挨拶            | ✔️                | ✔️                  | ✔️                 |
| ブランディング(ロゴ、色)     | ✔️                | ✔️                  | ✔️                 |
| APIキーセキュリティ            | 手動            | 強化            | 組み込み           |
| イベントリスナー             | ❌                | ✔️                  | ❌                 |
| 本人確認       | ❌                | ✔️                  | 部分的            |
| アナリティクス                   | プラットフォームベース    | プラットフォームベース      | プラットフォームベース     |
| コンプライアンス(GDPR、CCPA)     | プラットフォームサポート  | プラットフォームサポート    | プラットフォームサポート   |
| アクセシビリティ機能      | 通常含まれる  | 通常含まれる    | 通常含まれる   |

### カスタマイズオプション

- **視覚的外観:**
  - チャットバブルの色、ウィジェットの背景、フォントを変更。
  - カスタム企業ロゴまたはアバターをアップロード。
  - ホワイトラベルまたはプロバイダーブランディングを削除(特定プランで)。

- **挨拶メッセージ:**
  - 静的または動的なウェルカムメッセージを設定。
  - 初期ウィンドウにカスタムリンク、ボタン、またはコールトゥアクションを表示。

- **ウィジェット位置:**
  - ウィジェットを左下、右下に配置、またはカスタム座標を割り当て。
  - 自動起動を選択するか、ユーザーがクリックして開くようにする。

- **動作:**
  - 自由テキスト入力を有効/無効化。
  - 会話フロー、ボットの「個性」、フォールバック応答、人間エージェントへの引き継ぎを構成。

- **言語とローカライゼーション:**
  - デフォルト言語を設定。
  - 多言語検出を有効にするか、ユーザーが言語を切り替えられるようにする。
  - [Chatbase Language Options](https://chatbase.co/docs/developer-guides/javascript-embed#user-experience)

- **アクセシビリティ:**
  - キーボードナビゲーション、ARIAロール、スクリーンリーダーサポート、ハイコントラストモード。

**参考資料:**  
- [Chatbase Customization](https://chatbase.co/docs/developer-guides/javascript-embed#user-experience)
- [ChatBot.com Widget API](https://www.chatbot.com/docs/chat-widget-api/)

## セキュリティとコンプライアンスの考慮事項

### APIキーセキュリティ

- **公開スクリプトでシークレットまたは特権APIキーを公開しないでください。**
- クライアント側での使用を目的とした公開または制限付きキーのみを使用。
- ユーザー認証には、安全な本人確認を使用(バックエンドからトークンまたはユーザーコンテキストを渡す)。
- 機密または特権操作にはサーバー側プロキシの使用を検討。

**セキュリティチェックリストの例:**

| セキュリティタスク                                   | 推奨事項                                               |
|-------------------------------------------------|--------------------------------------------------------------|
| 公開/制限付きAPIキーを使用                  | ✔️                                                           |
| スクリプトにシークレット/プライベートキーを埋め込まない  | ✔️                                                           |
| バックエンド経由で機密データを難読化またはプロキシ   | ✔️                                                           |
| すべてのウィジェットとAPI通信にHTTPSを使用 | ✔️                                                           |
| チャットボット設定で許可されたドメインを検証    | ✔️                                                           |

**参考資料:**  
- [Chatbase Security Guide](https://chatbase.co/docs/developer-guides/javascript-embed#security-considerations)

### プライバシーと法的コンプライアンス

- **GDPR / CCPA:**  
  チャットボットを通じて個人データを収集する前に、ユーザーの同意を取得。
- **データアクセスと削除:**  
  ユーザーが自分のデータをリクエスト、アクセス、または削除できるようにする。
- **暗号化:**  
  転送中および保存中のすべてのデータが暗号化されていることを確認。
- **監査とログ:**  
  コンプライアンスのためにチャットボットのやり取りのログを保持。

ほとんどの信頼できるプロバイダーは、組み込みのコンプライアンス機能とドキュメントを提供しています。

**参考資料:**  
- [Chatbase Compliance](https://chatbase.co/docs/developer-guides/javascript-embed#security-considerations)
- [ChatBot.com Compliance](https://www.chatbot.com/solutions/)

### アクセシビリティ

- ARIAロール、スクリーンリーダー互換性、キーボードナビゲーションをサポートするウィジェットを使用。
- 色のコントラスト、フォントサイズ、フォーカスインジケーターをテスト。

**参考資料:**  
- [Chatbase Accessibility](https://chatbase.co/docs/developer-guides/javascript-embed#user-experience)

## Embed Scriptのトラブルシューティング

| 問題                                 | 考えられる原因                               | 解決策                                               |
|------------------------------------------|----------------------------------------------|--------------------------------------------------------|
| ウィジェットが表示されない                     | スクリプトの配置が間違っている、エージェントIDが間違っている    | 配置、エージェントID/APIキー、許可されたドメインを確認      |
| ウィジェットの読み込みが遅い                      | スクリプトがレンダリングをブロックしている                    | スクリプトタグに`async`または`defer`を追加                   |
| チャットが応答しない                      | APIキーが欠落/無効、ネットワークの問題      | APIキーを確認、ネットワークコンソールをチェック                  |
| カスタムイベントが機能しない                | スクリプト読み込み前のイベントリスナー          | スクリプト読み込み後にリスナーを追加                       |
| ウィジェットがサイトコンテンツと重なる             | CSSの競合                                | カスタムCSSでウィジェット位置またはz-indexを調整        |
| モバイルデバイスでウィジェットにアクセスできない  | ウィジェットがモバイル最適化されていない                  | デバイス間でテスト、モバイル設定を調整            |

**ステップバイステップの診断:**
1. ブラウザコンソールを開き、JavaScriptエラーを確認。
2. スクリプトURL、パラメータ、エージェントIDを検証。
3. チャットボット設定でウェブサイトドメインが許可されていることを確認。
4. ブラウザ拡張機能を無効にするか、シークレットモードでテスト。
5. 公式トラブルシューティングドキュメントを確認:
   - [Chatbase Troubleshooting](https://chatbase.co/docs/developer-guides/javascript-embed#troubleshooting)
   - [ChatBot.com Widget Installation Guide](https://www.chatbot.com/help/install-chatbot/widget-installation/)

## Embed Scriptのベストプラクティス

- **常にチャットボットプロバイダーから最新の公式埋め込みコードを使用してください。**
- **サイトのレンダリングをブロックしないように、スクリプトを非同期で読み込む(`async`または`defer`)。**
- **すべての主要なブラウザとモバイルデバイスでチャットボットをテストする。**
- **潜在的なセキュリティリスクを減らすために、サードパーティスクリプトの数を最小限に抑える。**
- **アナリティクスとユーザーフィードバックを定期的に確認して、チャットボットのパフォーマンスとUXを最適化する。**
- **プロバイダーが新しいバージョンをリリースした場合、スクリプトを更新する。**

**アクセシビリティのヒント:**
- キーボードナビゲーションとフォーカス状態が機能することを確認。
- アイコンとアバターにテキスト代替を提供。
- [WCAGガイドライン](https://www.w3.org/WAI/standards-guidelines/wcag/)に従う。

**コンプライアンスのヒント:**
- 情報を収集する前にプライバシー/データ同意通知を表示。
- ユーザーにオプトアウトとデータリクエストオプションを提供。

**参考資料:**  
- [Chatbase Best Practices](https://chatbase.co/docs/developer-guides/javascript-embed#best-practices)
- [ePhost Best Practices for Integrating AI Chatbots](https://www.ephost.com/blog/best-practices-for-integrating-ai-chatbots-into-your-website-design/)

## よくある質問(FAQ)

**Q: Embed Scriptとは何ですか?**  
A: HTMLに貼り付けることで、AIチャットボットまたはウィジェットをウェブサイトに読み込むJavaScriptスニペットです。

**Q: Embed Scriptはどこに配置すればよいですか?**  
A: パフォーマンスのために`</body>`タグの直前が望ましいですが、ウィジェットの高速読み込みのために`<head>`内でも可能です。一部のプラットフォームでは正確な場所を指定しているため、ドキュメントを確認してください。

**Q: チャットボットの外観と挨拶をカスタマイズできますか?**  
A: はい。ほとんどのプロバイダーは、ダッシュボードまたはスクリプト設定を介して、外観、挨拶、ブランディングなどを構成できます。

**Q: Embed ScriptにAPIキーを含めても安全ですか?**  
A: キーがクライアント側での使用を目的とした公開または制限付きの場合のみ。シークレットまたは特権キーを公開しないでください。

**Q: GDPR/CCPAコンプライアンスを確保するにはどうすればよいですか?**  
A: 組み込みのコンプライアンス機能を使用し、プライバシー通知を表示し、ユーザーが自分のデータを管理できるようにします。

**Q: チャットボットウィジェットが表示されない場合はどうすればよいですか?**  
A: スクリプトの配置、APIキー/エージェントID、ブラウザコンソールのエラー、ドメインのホワイトリスト登録を再確認してください。