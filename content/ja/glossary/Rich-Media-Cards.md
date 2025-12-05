---
title: リッチメディアカード
translationKey: rich-media-cards
description: リッチメディアカードは、チャットストリーム内のインタラクティブなUIコンポーネントで、画像、動画、ボタンなどのマルチメディアコンテンツとアクション可能な要素を提供し、魅力的な会話を実現します。
keywords: ["リッチメディアカード", "チャットボット", "対話型AI", "メッセージングプラットフォーム", "ユーザーエンゲージメント"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: りっちめでぃあかーど
reading: リッチメディアカード
kana_head: ら
e-title: Rich Media Cards
---
## 定義

リッチメディアカードは、チャットストリーム内に埋め込まれた構造化されたインタラクティブなUIコンポーネントであり、会話の中で直接、魅力的なマルチメディアコンテンツとアクション可能な要素を提供します。プレーンテキストメッセージとは異なり、リッチメディアカードは画像、GIF、動画、タイトル、サブタイトル、ボタンをまとめて提供し、ユーザーに視覚的に魅力的でアクション可能な体験を提供します。これらのカードはチャット内のミニランディングページのように機能し、アクションを促進し、情報を収集し、ユーザビリティとコンバージョンの両方を向上させることができます。

**権威ある参考資料:**  
- [Google RCS Business Messaging: Rich Cards](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards)  
- [Microsoft Bot Framework: Add Rich Card Attachments](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)  
- [Sprinklr: Chatbot Analytics](https://www.sprinklr.com/blog/chatbot-analytics/)  
- [Tars: Rich Media for Chatbots](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)  
- [Kommunicate: Best Chatbot Practices](https://www.kommunicate.io/blog/best-chatbot-practices/)  
- [Quickchat: Chatbot Analytics Deep Dive](https://quickchat.ai/post/chatbot-analytics)  

## リッチメディアカードの構造

リッチメディアカードは、それぞれが機能的および/または視覚的な目的を果たす標準コンポーネントのセットから構築されます。これには以下が含まれます:

- **メディア要素:** 画像(JPEG、PNG、GIF)、アニメーション、動画(MP4、M4V、WebMなど)、またはPDF(プラットフォームに依存)。メディアは注目を集め、製品を説明し、キャラクターを追加するために使用されます。
  - [Google RCSでサポートされている形式とメディアの高さを参照](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#media)
- **サムネイル:** メディアファイル、特に大きなファイルやPDFのカスタムまたはデフォルトのアイコンプレビュー。サムネイルは最適な読み込み時間のために100KB未満にする必要があります。
- **タイトル:** 見出しまたはメインラベル、通常は最大200文字(プラットフォームに依存)。簡潔で情報量が多い必要があります。
- **サブタイトル/説明:** サポートテキスト、多くの場合最大2,000文字で、追加のコンテキスト、メリット、またはコールトゥアクション(CTA)情報を提供します。
- **アクションボタン:** 即座のアクション(Web ナビゲーション、ポストバック、電話、ダウンロードなど)をトリガーするクリック可能な要素。ボタンの制限とタイプはプラットフォームによって異なります。
- **提案された返信:** チップまたはボタンとして表示される事前定義されたユーザー応答で、会話を最適なボットフレンドリーなパスに導きます。
- **オプションのインタラクティブ要素:** カルーセル(スクロール可能なカードのグループ)、フォーム(データキャプチャ用)、クイック返信、リストピッカー、カスタムペイロード。

**図解と参考資料:**  
- [Google: リッチカードのコンポーネント](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#rich-card-components)
- [Microsoft: カードタイプ](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0#types-of-rich-cards)

## リッチメディアカードの使用方法

### 1. 会話エンゲージメント

リッチメディアカードは、会話をよりアクション可能で表現力豊かで視覚的に魅力的にすることで、チャットボットのインタラクションを劇的に向上させます。一般的なチャットボットのユースケースには以下が含まれます:

- **製品推奨:** 製品画像、価格、「今すぐ購入」ボタンの表示。
- **リード生成:** チャット内でユーザー詳細をキャプチャするためのフォームの埋め込み。
- **カスタマーサポート:** ステップバイステップのトラブルシューティングガイドを、それぞれに「これは役に立ちましたか?」ボタンを付けて提示。
- **予約/スケジューリング:** 利用可能な時間枠またはサービスを即座予約ボタン付きのカードとして表示。
- **調査とフィードバック:** カード要素を通じて直接評価、コメント、または選択を要求。
- **インタラクティブFAQ:** サポートコンテンツを閲覧するための展開/折りたたみ可能なカードを備えたナビゲート可能なヘルプトピック。

**ベストプラクティス:** リッチメディアカードを使用して自然な会話フローを模倣し、ワンタップオプションを提供してユーザーの摩擦を減らし、完了率を高めます。[Tars: リッチメディアを使用してチャットボットの完了率を向上させる方法](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)

### 2. マルチプラットフォームメッセージング

リッチメディアカードのサポートと機能は、メッセージングプラットフォームによって異なります。主な環境には以下が含まれます:

- **Webチャットウィジェット:** 完全なカード、カルーセル、フォームのサポート、カスタマイズ可能なレイアウト(例:Intercom、Drift、Kommunicate)。
- **ソーシャルメッセージング:**  
  - **Facebook Messenger:** カードテンプレート、カルーセル、クイック返信、カルーセルあたり最大10枚のカード。
  - **WhatsApp:** 限定的なリストとボタンテンプレート(カルーセルなし)、メッセージあたり最大3つのボタン。
  - **Apple Business Chat:** 高度なカードタイプ、Apple Pay、フォーム、リストピッカー。
  - **Telegram、Viber、Slack:** カード、ボタン、メディアのサポートはさまざま。
- **エンタープライズソリューション:**  
  - **Microsoft Dynamics 365、Salesforce:** Adaptive Cards(JSONベース)、カルーセル、カスタムデータ収集、深い統合。
  - **API:** プログラム可能なペイロードとUIレンダリングを備えたカスタムボット。

**参考資料:**  
- [Google: プラットフォームの制約とメディアガイドライン](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#media)
- [Microsoft: チャネルサポートマトリックス](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-channels-reference?view=azure-bot-service-4.0)

## 技術的実装とサポートされているプラットフォーム

### カード構造とペイロード

リッチメディアカードは通常、JSONなどの構造化形式で定義されます。各プラットフォームには独自のスキーマがある場合がありますが、共通の要素がほとんどに表示されます:

**例: 一般的な製品カード(JSON)**

```json
{
  "type": "card",
  "title": "Wireless Headphones",
  "subtitle": "Noise-cancelling, 20h battery life",
  "image_url": "https://example.com/img/headphones.png",
  "buttons": [
    {
      "type": "web_url",
      "title": "Buy Now",
      "url": "https://example.com/buy/headphones"
    },
    {
      "type": "postback",
      "title": "More Info",
      "payload": "INFO_HEADPHONES"
    }
  ]
}
```
- [Google: RCSリッチカードのJSON構造](https://developers.google.com/business-communications/rcs-business-messaging/guides/build/messages/send)
- [Microsoft: Bot Frameworkカードスキーマ](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0)

### カルーセル(スクロール可能なカードセット)

カルーセルは、水平方向にスクロール可能な形式で複数のカードを提示し、製品発見やオプション選択に最適です。

**例: カルーセル(JSON)**

```json
{
  "type": "carousel",
  "cards": [
    {
      "title": "Product 1",
      "image_url": "https://example.com/img/p1.png",
      "buttons": [ ... ]
    },
    {
      "title": "Product 2",
      "image_url": "https://example.com/img/p2.png",
      "buttons": [ ... ]
    }
  ]
}
```

### サポートされているカードタイプ(Microsoft Bot Framework)

- **HeroCard:** 大きな画像、テキスト、ボタン。
- **ThumbnailCard:** 小さな画像、テキスト、ボタン。
- **AnimationCard/VideoCard/AudioCard:** 埋め込みメディア再生。
- **ReceiptCard:** アイテム、価格、合計を含む構造化されたレシート。
- **SignInCard:** OAuthまたはサードパーティ認証フロー。
- **AdaptiveCard:** リッチなUI要素、レイアウト、フォームを備えた高度にカスタマイズ可能なカード。[Adaptive Cards Designer](https://adaptivecards.io/designer/)

**詳細な参考資料:**  
- [Microsoft Bot Frameworkカードタイプ](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0#types-of-rich-cards)

### プラットフォーム固有の制約

| プラットフォーム               | カードサポート        | 最大カード数/カルーセル | 画像サイズ制限 | ボタン制限 | 注目すべき機能                  |
|------------------------|--------------------|-------------------|------------------|-------------|-----------------------------------|
| Webチャットウィジェット       | 完全(カード、フォーム)| さまざま(最大10) | 画像あたり約1MB   | 3〜5/ボタン  | カスタムレイアウト、クイック返信     |
| WhatsApp               | 限定的(リスト、ボタン)| 1〜3/行           | <1MB             | 3           | シンプルなカード、カルーセルなし        |
| Apple Business Chat    | 高度           | さまざま            | 約1MB             | 3〜5         | Apple Pay、フォーム、リストピッカー    |
| Facebook Messenger     | 完全(カード、カルーセル)| 10/カルーセル     | 1MB              | 3           | テンプレート、クイック返信          |
| Microsoft Dynamics 365 | 完全(カード、JSON) | 10/カルーセル       | 1MB              | 5           | Adaptive cards、フォーム、カスタムJSON|

**技術的注意事項:**
- 特にモバイルユーザーのために速度を向上させるため、常に画像と動画を圧縮してください。
- プラットフォーム固有の文字制限(タイトル、ボタンなど)を尊重してください。
- デバイスとチャネル全体でインタラクティビティとフォーマットをテストしてください。
- ボタンクリック、カードビュー、ユーザーアクションの分析と追跡を使用してください。
- [Google: メディアアップロードとサムネイルガイドライン](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#thumbnail)

## リッチメディアカードの主な利点

### 1. より高いエンゲージメント

リッチメディアカードは、エンゲージメントの面でテキストのみのメッセージを一貫して上回ります。データは以下を示しています:
- 画像が豊富な会話は**2〜3倍高いエンゲージメント**を促進できます([Conferbot](https://www.conferbot.com/features/rich-media)、[Tars](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media))
- ビジュアルとボタンは注目を集め、より多くのインタラクションを促進します。
- 摩擦がない:ユーザーはワンタップでアクション(購入、予約、返信)できます。

### 2. コンバージョン率の向上

- リッチメディア要素を備えたチャットボットは、シンプルなテキストボットと比較して**最大85%高いコンバージョン率**を提供します([Tars](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media))。
- インタラクティブなフォーム、カルーセル、CTAはユーザージャーニーを合理化し、離脱を減らします。

### 3. ブランド体験の向上

- カードは、カスタム画像、色、トーンを通じてブランドアイデンティティを強化します。
- より記憶に残り楽しいため、ブランド想起率が高くなります。
- GIF、絵文字、または動画を追加してチャットボットを人間化します。

### 4. 運用効率

- ユーザーをセルフサービスの回答に導くことで、カスタマーサポートの作業負荷を軽減します。
- 応答を標準化し、一貫性と正確性を確保します。

### 5. 高度な追跡と分析

リッチメディアカードは追跡可能であり、どのカード、ボタン、フローがエンゲージメントを促進するかを測定できます。主な分析には以下が含まれます:
- ボタンのクリックスルー率
- カードビュー数
- 離脱ポイントとファネル分析
- ゴール完了率

**参考資料:**  
- [Sprinklr: チャットボット分析メトリクス](https://www.sprinklr.com/blog/chatbot-analytics/)
- [Quickchat: チャットボット分析の完全ガイド](https://quickchat.ai/post/chatbot-analytics)

## ユースケースと実例

### リード生成

**シナリオ:** ウェブサイトチャットボットがサービスのカルーセルを提示し、それぞれに「お問い合わせ」ボタンがあります。ユーザーはチャット内で直接連絡先情報を送信します。  
**メリット:** 摩擦のないデータキャプチャがリードの量と質を増加させます。

### Eコマース製品発見

**シナリオ:** Messengerボットがベストセラーのカルーセルを送信し、各カードに製品画像、価格、「今すぐ購入」ボタンが表示されます。  
**メリット:** 合理化されたブラウジングと購入がコンバージョンを促進します。

### カスタマーサポート

**シナリオ:** ボットがトラブルシューティング手順をカードとして提示し、それぞれに「これは役に立ちましたか?」ボタンがあります。  
**メリット:** エージェントの作業負荷を軽減し、解決速度を向上させます。

### 予約予約

**シナリオ:** ボットが利用可能な時間枠をカードとして表示し、ユーザーがタップして確認します。  
**メリット:** スケジューリングを簡素化し、放棄を減らします。

### 調査とフィードバック

**シナリオ:** インタラクション後、カードが星評価とオプションのコメントを要求します。  
**メリット:** 調査完了率と実用的なフィードバックを向上させます。

### 不動産とリスティング

**シナリオ:** 不動産ボットが利用可能な住宅をカードとして表示し、それぞれに画像と「ツアーをスケジュール」ボタンがあります。  
**メリット:** 購入者を引き付け、即座のアクションを可能にします。

### コンテンツ配信

**シナリオ:** メディアボットがニュース記事をサムネイル、見出し、「続きを読む」ボタン付きのカードとして送信します。  
**メリット:** コンテンツ消費とエンゲージメントを増加させます。

**追加リソース:**  
- [Sendbird: リッチメディアとは?](https://sendbird.com/learn/what-is-rich-media)  
- [Madgicx: リッチメディア広告](https://madgicx.com/blog/rich-media)

## リッチメディアカードのベストプラクティス

1. **明確さとシンプルさを優先する**
   - カルーセルあたりのカード数を制限する(プラットフォームに応じて3〜10)。
   - 簡潔なテキスト、高品質の画像、焦点を絞ったアクションを使用します。
2. **パフォーマンスを最適化する**
   - 画像/動画を1MB未満に保つ、サムネイルは50〜100KBを推奨。
   - 高速CDNでメディアをホストし、低速接続での読み込み時間をテストします。
3. **モバイルファーストデザイン**
   - ボタンが大きくタッチフレンドリーであることを確認します。
   - 密集したレイアウトを避け、コンテンツを読みやすくアクション可能に保ちます。
4. **アクション指向のボタン**
   - 明確で具体的なCTAを使用します(例:「今すぐ予約」、「見積もりを取得」)。
   - プラットフォームに基づいて、カードあたり3〜5のアクションに制限します。
5. **パーソナライゼーション**
   - ユーザーのコンテキスト、履歴、または好みに基づいてカードコンテンツを調整します。
6. **アクセシビリティ**
   - 画像に説明的な代替テキストを追加します。
   - ボタンラベルがスクリーンリーダーフレンドリーであることを確認します。
7. **A/Bテスト**
   - カードの順序、ビジュアル、メッセージングを実験します。
   - 実際の使用状況に基づいて分析を使用して反復します。
8. **高度な分析**
   - カードインプレッション、ボタンクリック、離脱、ゴール完了を追跡します。
   - 最適化のためにダッシュボードとファネル可視化を使用します([Quickchat AIガイド](https://quickchat.ai/post/chatbot-analytics))。
9. **ブランドの一貫性**
   - ブランド承認済みの色、ロゴ、タイポグラフィを使用します。
   - メッセージングがブランドトーンと一致することを確認します。

**避けるべき落とし穴:**
- テキストまたはボタンが多すぎるカードの過負荷。
- 画像の最適化を怠る—読み込み時間が遅いとエンゲージメントが低下します。
- 一般的または無関係なビジュアルの使用。
- プラットフォーム固有のカード制限と制約を無視する。

**参考資料:**  
- [Kommunicate: チャットボットのベストプラクティス](https://www.kommunicate.io/blog/best-chatbot-practices/)  
- [Tars: リッチメディアをいつどのように使用するか](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)

## 高度な分析と測定

### リッチメディアカードパフォーマンスの主要メトリクス

- **総ユーザー数:** ボットとインタラクションしたユニークユーザーの数。
- **アクティブ/エンゲージユーザー:** ウェルカムメッセージを超えてインタラクションしたユーザー。
- **カードビュー:** カードが表示された回数。
- **ボタンクリック/CTAエンゲージメント:** 各アクションボタンのクリックスルー率。
- **離脱率:** ユーザーが会話を放棄するポイント。
- **ゴール完了率:** 望ましいアクション(フォーム記入、購入など)を完了したユーザーの割合。
- **セルフサービス率:** 人間の介入なしにボットによって解決された問題。
- **デフレクション率:** ボットによって処理された問い合わせの割合で、人間の作業負荷を軽減します。
- **CSAT/NPS:** 顧客満足度スコア、多くの場合リッチメディア調査カードを通じて収集されます。

### 分析を使用して結果を最適化する

- **ファネル分析:** ユーザーがカルーセル/カードをどのように移動するかを追跡し、離脱ポイントを特定します。
- **コンテンツ最適化:** カードレベルの分析を使用して、画像、タイトル、またはCTAを改善します。
- **A/Bテスト:** カードの順序、ボタンの配置、またはCTAの文言を実験して完了率を向上させます。
- **パーソナライゼーション:** 分析を活用してユーザーをセグメント化し、ターゲットを絞ったカードを配信します。

**ダッシュボードとツール:**  
- [Sprinklr: チャットボット分析ダッシュボード](https://www.sprinklr.com/blog/chatbot-analytics/)
- [Quickchat: AIエージェント分析](https://quickchat.ai/post/chatbot-analytics)

## プラットフォーム固有の技術ガイド

- [Google: RCSリッチカードの機能と制約](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards)
- [Microsoft: Bot Frameworkカードタイプとチャネルマトリックス](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)
- [Adaptive Cards Designer](https://adaptivecards.io/designer/)
- [Facebook Messenger Platformテンプレート](https://developers.facebook.com/docs/messenger-platform/send-messages/template/)
- [WhatsApp Business Messagingテンプレート](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates)

## よくある質問(FAQ)

### リッチメディアカードと標準メッセージの違いは何ですか?
標準メッセージはプレーンテキストです。リッチメディアカードには、画像、動画、カルーセル、ボタンを含めることができ、インタラクティブで視覚的に魅力的な体験を可能にします。

### リッチメディアカードを作成するにはデザインスキルが必要ですか?
ほとんどのチャットボットプラットフォームは、ドラッグアンドドロップのカード作成機能を備えたビジュアルビルダーを提供しています(例:Kommunicate、Tars、Microsoft Adaptive Cards Designer)。最小限のデザインスキルが必要ですが、明確さとブランディングへの注意が重要です。

### リッチメディアはチャットボットを遅くしますか?
最適化された画像と動画(できれば1MB未満)は速度低下を防ぎます。すべてのメディアを圧縮し、大きなファイルにはCDNホスティングを使用してください。

### リッチメディアカードとのユーザーインタラクションを追跡できますか?
はい。ほとんどのプラットフォームは、ボタンクリック、カードビュー、離脱、ゴール完了の分析を提供します(詳細については上記を参照)。

### リッチメディアカードはすべてのメッセージングアプリでサポートされていますか?
サポートはプラットフォームによって異なります。Webチャット、Messenger、Apple Business Chatは堅牢なサポートを提供します。WhatsAppとSMSは