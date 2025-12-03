---
title: パーシステントメニュー
translationKey: persistent-menu
description: チャットボットにおけるパーシステントメニューについて学びます:その定義、使用する理由、実装方法、そしてユーザーナビゲーションと体験を向上させるためのベストプラクティスを解説します。
keywords:
- Persistent Menu
- チャットボット
- Facebook Messenger
- ナビゲーションメニュー
- メニュー項目
category: General
type: glossary
date: 2025-12-03
draft: false
term: ぱーしすてんとめにゅー
reading: パーシステントメニュー
kana_head: は
e-title: Persistent Menu
---

## Persistent Menu(パーシステントメニュー)とは?

**Persistent Menu(パーシステントメニュー)**は、チャットボットに組み込まれた常時表示の静的メニューインターフェースで、セッション全体を通じてユーザーに表示されます。メッセージのコンテキストや会話フローに関係なく、チャットボットの重要なアクションへ即座にアクセスできます。メニューは通常、認識しやすいアイコン(多くの場合ハンバーガーメニュー)から表示され、再起動、ヘルプ、配信停止、ナビゲーションショートカットなどの重要なアクションがリストされます。

- **主な特徴:**
  - 常にアクセス可能—ボタン使用後も消えません。
  - 会話やオンボーディングのどの段階でも利用可能。
  - 明確で一貫したユーザーオプションを提供。
  - 初回ユーザーとリピーターの両方に最適。

**参考資料:**
- [ChatbotBuilder.ai: Persistent Menu](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Meta for Developers: Persistent Menu Overview](https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu/)

## Persistent Menuを使用する理由(主なメリット)

適切に設定されたPersistent Menuは、明確なユーザー価値を提供し、ビジネス目標をサポートします:

- **高速ナビゲーション:** ユーザーは頻繁に必要な機能や情報に即座にアクセス可能—コマンドを記憶したり会話スレッドを検索する必要がありません。
- **摩擦の軽減:** ユーザーが迷ったりフラストレーションを感じることを防ぎ、混乱するフローからの直接的な脱出ルートを提供します。
- **機能の発見:** 新規ユーザーとリピーターがボットの主要機能を一目で確認できます。
- **ビジネスとの整合性:** ビジネス価値を生み出すコアアクション(例:商品クイズ、サポート連絡、注文追跡)を促進します。
- **アクセシビリティ:** アクセシビリティニーズを持つユーザーは、明確に構造化された常時利用可能なアクションから恩恵を受けます。

**参考資料:**
- [Chatfuel Blog: Persistent Menu](https://chatfuel.com/blog/persistent-menu)
- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

## Persistent Menuの使用方法

Persistent Menuは通常、チャットウィンドウ内のメニューアイコン(一般的にはハンバーガーアイコン)をクリックまたはタップしてアクセスします。その内容は会話の段階に関係なく、いつでも利用可能です。

**ユーザーエクスペリエンスのハイライト:**
- ユーザーはオンボーディング中、会話の途中、またはアクション完了後にメニューを開くことができます。
- 典型的なアクション:ボットの再起動、ヘルプ/FAQへのアクセス、メインメニューへのジャンプ、配信停止、外部URLを開く、クイズの開始。

**参考資料:**
- [YouTube: How to Setup Persistent Menu In Website Chatbot (BotSailor)](https://www.youtube.com/watch?v=4kAlBEgCvwM)

## サポートされるチャネルとプラットフォームの制限

Persistent Menuは主要なメッセージングおよびWebプラットフォームでサポートされていますが、機能と制限はプラットフォームによって異なります:

| プラットフォーム              | サポートレベル           | 注意事項/制限事項                                                                            |
|-----------------------|------------------------|----------------------------------------------------------------------------------------------|
| Facebook Messenger    | 完全対応                   | 最大3つのトップレベル項目、ネストメニュー対応、ユーザー入力制御対応。                            |
| Instagram             | 対応(API経由)    | Messengerと同様、最新情報はプラットフォーム固有のドキュメントを確認してください。                      |
| Webチャットウィジェット       | 完全対応(ほとんどのビルダー)   | ボタンの外観、ユーザー入力制御、ネスト機能はベンダーによって異なります。                            |
| WhatsApp、Telegram    | 制限あり/異なる         | 各ボットビルダーのドキュメントでサポートと制限を確認してください。                           |

- **ボタン制限:** Messengerはメニューレベルごとに最大3つのボタンをサポート。
- **外観:** メニューアイコンと位置はチャネルによって異なる場合があります。
- **メニュースコープ:** 一部のプラットフォームではボットインスタンスごとに1つのメニューのみ許可。
- **入力の無効化:** 多くの場合、フローごとではなくグローバルに適用されます。

**参考資料:**
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Certainly: Channel Limitations](https://support.certainly.io/knowledge/Overview-of-channel-limitations)
- [Meta for Developers: Persistent Menu](https://developers.facebook.com/docs/messenger-platform/send-messages/persistent-menu/)

## メニュー項目のタイプと構造

### ボタンアクション

Persistent Menuには複数のタイプのアクションを含めることができます:

- **メッセージ送信:** 特定のボットフローをトリガーするか、定義されたメッセージを送信します。
- **URLを開く:** 指定されたWebページを開きます(多くの場合アプリ内ブラウザで)。
- **ボットの再起動:** 会話を開始またはウェルカムステップにリセットします。
- **配信停止:** ユーザーを今後のメッセージやインタラクションからオプトアウトします。
- **クイズを受ける:** 商品またはフィードバッククイズを開始します。
- **ヘルプ/FAQ:** サポートまたはよくある質問への回答を表示します。

### ネストメニュー

一部のプラットフォーム(Messengerなど)では、メニューのネストが可能で、関連するアクションを1つのラベルの下にグループ化できます。例:「アカウント」→「プロフィール」、「設定」。

- **制限事項:** すべてのプラットフォームやビルダーがネスト(サブ)メニューをサポートしているわけではありません。

### メニュー項目の例

| ボタンラベル       | アクション                         | 説明                                      |
|--------------------|-------------------------------|--------------------------------------------------|
| 🏠 メインメニュー       | メインメニューフローへ移動           | ユーザーをメインナビゲーションに戻す                   |
| 🔁 再起動         | 会話をリセット             | ユーザーが最初からやり直せるようにする                             |
| ❌ 配信停止     | オプトアウトアクション                 | ユーザーへのさらなるメッセージを終了                |
| 📝 クイズを受ける       | レコメンデーション/クイズを開始     | 情報を収集し、パーソナライズされた提案を提供 |
| ❓ ヘルプ            | FAQ/連絡先オプションを表示        | 即座のサポートを提供                           |
| 📦 注文状況    | 注文を確認                    | Eコマースボット向け                              |
| 💬 サポートに連絡 | サポートフロー/メールを開く         | 人間のエージェントまたはさらなるヘルプ                      |

*1つのメニュー内で異なるアクションタイプを混在させることができます。*

**参考資料:**
- [Messenger Platform API: persistent_menu](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/)
- [ChatbotBuilder.ai Guide](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)

## ステップバイステップ:Persistent Menuの追加方法

プロセスはチャットボットビルダー/プラットフォームによって異なります。以下は一般的なガイドと、人気のあるプラットフォームの具体的な手順です。

### 一般的な手順

1. **ボットプラットフォームダッシュボードにログイン**
2. **ボット設定またはフロービルダーを開く**
   - 「Persistent Menu」、「Menu」、または「Navigation」セクションを見つけます。
3. **Persistent Menuを作成/編集**
   - 通常、「Create」または「Edit」ボタンから行います。
4. **メニュー項目を追加**
   - 各スロットに対して:アクションタイプ、ラベル、ターゲット(フロー、URLなど)を選択します。
5. **順序を整理**
   - ドラッグアンドドロップで並べ替え、最も重要なアクションを最初に配置します。
6. **詳細オプション**
   - メニューのローカライズ、ユーザー入力の有効化/無効化、サポートされている場合はサブメニューの追加。
7. **保存と公開**
   - 「Save」、「Publish」をクリックするか、メニューをライブに切り替えます。

**参考資料:**  
- [YouTube: Persistent Menu Setup Tutorial (BotSailor)](https://www.youtube.com/watch?v=4kAlBEgCvwM)

### プラットフォーム固有の手順

#### **Facebook Messenger(Chatfuel経由)**

1. [Chatfuel Dashboard](https://dashboard.chatfuel.com)にアクセスします。
2. Flowタブを開き、フローを作成/選択します。
3. キャンバスをダブルクリックし、「Entry Points → Persistent Menu」を選択します。
4. 最大3つのボタンを追加します(例:「Restart Bot」、「Help」、「Unsubscribe」)。
5. ドラッグして並べ替え、トグルでメニューを有効化します。
6. ローカライゼーションの場合、「Localization」をクリックして翻訳を追加します。

![Persistent Menu Example in Chatfuel](https://storage.googleapis.com/chatfuel-cms-staging/pic/original_persistent_menu_0_8a23ef77c3/original_persistent_menu_0_8a23ef77c3.webp)

- [Chatfuel: Persistent Menu Docs](https://chatfuel.com/blog/persistent-menu)

#### **ChatbotBuilder.ai**

1. Settings → Channels → Facebook Messenger/Instagram → Persistent Menuに移動します。
2. 「Edit」をクリックしてセットアップウィザードを開きます。
3. 必要に応じてメニュー項目を追加します。
4. ユーザー入力を無効にするには、「Allow Keyboard Input」のチェックを外します。
5. 保存して公開します。

- [ChatbotBuilder.ai: Persistent Menu](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)

#### **Certainly**

1. [Bot Settings](https://support.certainly.io/knowledge/Individualize-your-chatbot-in-Bot-Settings)を開きます。
2. Persistent Menuタブを選択します。
3. 項目を追加します(Open URL、Send message、Nested)。
4. 変更を保存します。

- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

#### **Webチャットウィジェット(BotSailorの例)**

1. BotSailorダッシュボードにログインします。
2. Webチャットボットマネージャーに移動します。
3. 「Persistent Menu」をクリックします。
4. 「Create」をクリックし、ポップアップでメニューを設定します。
5. 必要に応じてユーザー入力を完全に無効化できます。
6. 保存してWebチャットウィジェットをテストします。

- [YouTube Tutorial: Persistent Menu in Website Chatbot](https://www.youtube.com/watch?v=4kAlBEgCvwM)

## Persistent Menuのカスタマイズ

### ローカライゼーション(多言語対応)

- 「Localization」または「Add Language」ボタンから翻訳を追加します。
- ターゲット言語を選択し、翻訳されたボタンラベルを入力します。
- メニューボタンのテキストのみがローカライズされ、会話フロー全体ではありません。

**ベストプラクティス:**  
ボットがユーザージャーニー全体でその言語をサポートしている場合のみローカライズしてください。

### ユーザー入力の無効化

- フリーテキスト入力を無効にして、ユーザーをメニュー/クイック返信のみに制限します。
- 厳格なフロー(例:クイズ、フォーム)に便利ですが、注意:通常、入力はグローバルに無効化されます。
- オープンレスポンス(メール、住所)を収集するには、ユーザー入力を有効のままにします。

### メニューの外観と順序

- メニューは通常右下(Messenger)ですが、プラットフォームによって異なります。
- 順序が重要:最も重要なアクションを上部に配置します。
- 説明的で短いラベルを使用します(30文字制限が一般的)。
- 絵文字は認識を助けますが、プロフェッショナルな使用を心がけます。
- ボタンはURLを開くかボットフローをトリガーできます。

## Persistent Menuのベストプラクティス

- **シンプルに保つ:** 2〜3の主要アクションに制限し、メニューの混雑を避けます。
- **重要な機能を優先:** 「Restart」、「Help」、「Unsubscribe」は簡単にアクセスできるようにします。
- **明確なラベル:** 曖昧な用語(「Again」)ではなく、「Restart Bot」のような用語を使用します。
- **アクションタイプを混在:** 必要に応じてリンク、フロー、サブメニューを組み合わせます。
- **徹底的にテスト:** すべてのチャネルとデバイスで確認します。
- **アクセシビリティを維持:** 読みやすいフォントと明確なコントラストを使用します。
- **定期的に更新:** 分析とユーザーフィードバックに基づいてメニューを調整します。

**参考資料:**  
- [Chatfuel Blog: Persistent Menu Best Practices](https://chatfuel.com/blog/persistent-menu)
- [Certainly: Menu Design Tips](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

## 一般的なユースケースと例

### Eコマースチャットボットメニュー

| ボタン         | アクション                 |
|----------------|-----------------------|
| 🛒 ショップ        | メインショッピングフローを開く|
| 🚚 注文を追跡 | 注文状況を表示      |
| ❓ ヘルプ        | FAQまたはサポートフロー    |

### 商品レコメンデーションクイズ

| ボタン           | アクション                        |
|------------------|------------------------------|
| 📝 クイズを受ける     | 商品クイズフローを開始       |
| 🔁 ボットを再起動   | 会話をリセット            |
| ❌ 配信停止   | ボットメッセージをオプトアウト       |

### レストラン予約ボット

| ボタン          | アクション                    |
|-----------------|--------------------------|
| 📅 テーブルを予約   | 予約フローを開始    |
| 📖 メニュー        | メニューURLを開く             |
| 🏠 メインメニュー   | ホームフローに戻る       |

## トラブルシューティングと考慮事項

- **メニューが表示されない:** メニューが有効化され公開されていることを確認し、チャネルサポートを確認します。
- **ユーザー入力が意図せず無効化:** 入力の無効化は多くの場合ボット全体に適用されることを覚えておいてください。
- **ローカライゼーションの問題:** 言語設定が正しいことを確認し、ボタンテキストのみがローカライズされます。
- **ボタンが多すぎる:** プラットフォームの制限を尊重します(例:Messenger = メニューレベルごとに3つ)、サポートされている場合はネストを使用します。
- **テスト:** すべてのターゲットチャネルとデバイスで可視性と機能をテストします。

**参考資料:**  
- [ChatbotBuilder.ai Troubleshooting](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Certainly: Menu Troubleshooting](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

## さらなるリソースと次のステップ

- [Chatfuel Blog: Persistent Menu](https://chatfuel.com/blog/persistent-menu)
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)
- [Certainly Knowledge Base: Add a Persistent Menu](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)
- [Messenger Platform API: persistent_menu](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/)
- [YouTube: Persistent Menu in Website Chatbot](https://www.youtube.com/watch?v=4kAlBEgCvwM)
- [YouTube: Using Persistent Menu Entry Point in Chatfuel](https://www.youtube.com/watch?v=DWovaAjFOOk)

## 自分で試してみましょう!

**チャットボットにPersistent Menuを追加:**
- チャットボットビルダーにログインします。
- プラットフォームのセットアップ手順に従います。
- ユーザーフィードバックに基づいてテストと改善を行います。

**サポートが必要ですか?**  
上記にリンクされているドキュメントとビデオチュートリアルを参照するか、プラットフォームのサポートチームにお問い合わせください。

## 関連キーワード

persistent menuの追加、ボタンpersistent menu、persistent menu追加、persistent menuの作成、ナビゲーションメニュー、ユーザー入力の無効化、レコメンデーションクイズ、facebook messenger、ボットの再起動、チャットボット、メニュー項目、ボタンの追加、メニューユーザー、メインメニュー

**包括的な詳細ガイド**  
この用語集は、プラットフォームドキュメント、ベストプラクティス、実装の詳細を統合しています。公式の技術API詳細については、[MetaのPersistent Menu APIリファレンス](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu/)を参照してください。

ビジュアルおよびステップバイステップのチュートリアルについては、以下をご覧ください:  
- [How to Setup Persistent Menu In Website Chatbot (YouTube)](https://www.youtube.com/watch?v=4kAlBEgCvwM)  
- [How to Use the Persistent Menu Entry Point in Chatfuel (YouTube)](https://www.youtube.com/watch?v=DWovaAjFOOk)

カスタマイズと高度な使用に関するさらなる情報については、以下をご覧ください:  
- [ChatbotBuilder.ai Documentation](https://docs.chatbotbuilder.ai/support/solutions/articles/150000166613-persistent-menu)  
- [Certainly Knowledge Base](https://support.certainly.io/knowledge/add-a-persistent-menu-to-your-chat)

**これらのリソースを活用し、ユーザーのニーズとビジネス目標に適したPersistent Menuを構築して、今すぐチャットボットを強化しましょう。**