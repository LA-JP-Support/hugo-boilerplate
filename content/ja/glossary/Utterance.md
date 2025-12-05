---
title: 発話
date: 2025-11-25
translationKey: utterance
description: 会話型AIにおける発話とは何か、NLU/NLPにおける役割、種類、ワークフロー、課題、そしてチャットボットを効果的にトレーニングするためのベストプラクティスについて学びます。
keywords:
- 発話
- 会話型AI
- チャットボット
- NLU
- NLP
category: AI Chatbot & Automation
type: glossary
draft: false
e-title: Utterance
term: はつわ
reading: 発話
kana_head: その他
---
## 会話型AIにおける発話(Utterance)とは?

**発話(Utterance)**とは、ユーザーがチャットボットや[会話型AI](/en/glossary/conversational-ai/)との対話中に、タイピングまたは音声で伝えるあらゆる入力、フレーズ、または文のことです。文、質問、断片など、各メッセージやコマンドが発話となります。例えば:

- ユーザー:「私の口座残高は?」*(発話)*
- ユーザー:「最後の注文をキャンセルして。」*(発話)*
- ユーザー:「こんにちは!」*(発話)*

発話は、[会話型AI](/ja/glossary/conversational-ai/)システムがユーザーのニーズを理解し、適切な応答を生成するために解釈する基本要素です。**自然言語理解(NLU)**と**自然言語処理(NLP)**に依存するシステムの中核を成しています。

**権威ある参考資料:**  
- [SiteSpeakAI: What is an Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: AI Utterances Documentation](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: Utterance, Intent & Entity in Conversational AI](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## 詳細解説:発話の実践的な例

発話は、複雑さ、長さ、意図において多様です。簡単な挨拶から具体的なコマンド、オープンエンドの質問まで幅広く存在します。一般的な例:

| 発話の例                        | 想定される意図             |
|-------------------------------------------|-----------------------------|
| 「今日の天気はどう?」          | 天気照会             |
| 「来週パリ行きの飛行機を予約して。」   | 飛行機予約                  |
| 「助けて!」                                  | 支援要請          |
| 「近くのイタリアンレストランを見せて。」     | レストラン検索           |
| 「パスワードを変更したい。」           | アカウント管理          |
| 「ジョークを言ってくれる?」                 | エンターテインメント要求       |
| 「こんにちは」                                     | 挨拶                    |

### 実世界のユースケース

- **銀行チャットボット:**  
  - 「残高を確認するにはどうすればいい?」
  - 「貯蓄口座に100ドル振り込んで。」

- **Eコマースボット:**  
  - 「注文を追跡して。」
  - 「この靴を返品したい。」

- **カスタマーサポート:**  
  - 「アカウントにログインできない。」
  - 「パスワードをリセットして。」

各ユーザー入力は、チャットボットがリクエストを満たすために理解しなければならない発話です。幅広い発話を収集することは、[会話型AI](/ja/glossary/conversational-ai/)を効果的にトレーニングするために不可欠です。([SiteSpeakAI](https://sitespeak.ai/ai-chatbot-terms/utterance))

## 発話の種類とカテゴリー

発話の多様性を理解することは、堅牢なチャットボット設計と効果的な[意図認識](/en/glossary/intent-recognition/)の中心です。

### 1. 構造化発話 vs. 非構造化発話

- **構造化:**明確で予測可能な形式。
  - 例:「注文状況:#12345」
- **非構造化:**自由形式で自然な表現。
  - 例:「最後の注文がどこにあるか教えてくれる?」

### 2. 文脈依存発話 vs. 文脈非依存発話

- **文脈依存:**以前の会話やユーザーデータに依存。
  - 例:「いつ届く?」(注文について話した後)
- **文脈非依存:**独立しており、単独で理解可能。
  - 例:「営業時間は?」

### 3. ポジティブ発話 vs. ネガティブ発話

- **ポジティブ:**満足または同意。
  - 「ありがとう、役に立った!」
- **ネガティブ:**不満または苦情。
  - 「これは私には合わない。」

### 4. 意図指向のカテゴリー

- **直接的なコマンド:**「予約をキャンセルして。」
- **丁寧な依頼:**「予約をキャンセルしていただけますか?」
- **質問:**「予約をキャンセルするにはどうすればいい?」
- **意図の表明:**「予約をキャンセルしたい。」
- **仮定:**「予約をキャンセルしたらどうなる?」
- **部分的/断片的:**「予約キャンセル」
- **感情またはフィードバック:**「これは遅すぎる。」/「素晴らしいサービス!」

### 5. 言語的バリエーション

- **フォーマル vs. インフォーマル:**「〜したいのですが」vs.「〜したい」
- **スラング、略語、タイポ:**「そこにいる?」「助けてplz」「ログインできない」

#### カテゴリー表

| カテゴリー                | 例                                 | ユースケース                        |
|-------------------------|--------------------------------------------|----------------------------------|
| 直接的なコマンド          | 「アカウントを削除」                           | アクション要求                  |
| 丁寧な依頼          | 「プロフィールを削除していただけますか?」             | 礼儀正しいユーザー                  |
| 質問                | 「パスワードをリセットするにはどうすればいい?」              | ガイダンスを求める                 |
| 意図の表明     | 「メールアドレスを変更したい」        | 明確なユーザー目標               |
| 部分的/断片        | 「パスワードリセット」                           | 省略された入力                |
| 仮定            | 「アカウントを削除したらどうなる?」             | 結果を探る           |
| フィードバック(ポジティブ)     | 「助けてくれてありがとう!」                    | 感謝の表現             |
| フィードバック(ネガティブ)     | 「これは機能していない」                       | フラストレーションの表現           |
| 挨拶/別れ       | 「こんにちは!」/「さようなら」                       | 会話の流れ                |

## チャットボットワークフローにおける発話

発話を処理するチャットボットワークフローには、いくつかのステップがあります:

1. **ユーザーが発話を送信:**ユーザーがメッセージをタイプまたは話す。
2. **自然言語処理(NLP):**チャットボットが以下を使用して発話を分析:
   - **トークン化:**発話を単語またはトークンに分解。
   - **ステミング/レンマ化:**単語を基本形に還元。
   - **品詞タグ付け:**文法的役割の識別。
   - **固有表現認識(NER):**重要な詳細(日付、場所など)の抽出。
   - **感情分析:**感情的なトーンの評価。
3. **意図分類:**ユーザーが達成したいことを判断。
   - 例:「東京行きの飛行機を予約したい。」→意図:飛行機予約
4. **エンティティ抽出:**発話から具体的な詳細を引き出す。
   - 例:目的地=東京
5. **応答生成:**識別された意図、エンティティ、文脈を使用して返答を生成。

### 関係性:発話、意図、エンティティ

| 用語       | 説明                                                        | 例                                 |
|------------|--------------------------------------------------------------------|-----------------------------------------|
| 発話  | ユーザーが言うこと                                                 | 「来週末のパリ行きの便を探して」 |
| 意図     | 発話の背後にある目標または目的                           | 飛行機予約                              |
| エンティティ     | 発話内の重要な詳細                                   | 目的地:パリ、日付:来週末  |

**さらに読む:**  
- [Microsoft LUIS: Utterances](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)  
- [IBM Watson: Intents and Entities](https://www.ibm.com/cloud/learn/natural-language-processing)  
- [LinkedIn: What is Utterance, Intent & Entity?](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## 発話処理における課題

### 1. 言語的曖昧性

- **同音異義語:**  
  - 「テーブルを予約する」(予約)vs.「本を読む」(物体)
- **暗黙の意図:**  
  - 「ここは寒すぎる」(暗示:暖房を上げて)

### 2. スラング、略語、インフォーマルな言語

- 「残高チェックしたい」
- 「助けてplz」

### 3. スペルミスとタイポグラフィーエラー

- 「ログインできない」
- 「資金を振り込んで」

### 4. 多言語およびコードスイッチング発話

- 「Quiero order pizza」(スペイン語と英語の混合)

### 5. 文脈依存性

- 「送料はいくら?」(商品について話した後)

### 6. 意図の重複

- 類似した発話が複数の意図にマッピングされ、混乱を引き起こす可能性がある。

### 7. エンティティのバリエーション

- 「NYC」、「ニューヨーク市」、「ビッグアップル」(同じ目的地)

**出典:**  
- [SiteSpeakAI: Utterance FAQ](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [LinkedIn: Utterance, Intent & Entity](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)

## 発話の設計と収集のベストプラクティス

### 1. 多様で代表的な発話を収集

実際のユーザーデータ、チャットログ、ブレインストーミング、実際の会話からのアクティブラーニングを使用します。表現、構造、形式のバリエーションを含めます。

### 2. 意図間の重複を避ける

異なる意図の発話が明確に区別されるようにし、誤分類を防ぎます。冗長性や曖昧性を定期的にレビューします。

### 3. 自然なユーザー言語を使用

スラング、スペルミス、インフォーマルな表現を含む、ユーザーが実際に話したりタイプしたりする方法を優先します。

### 4. 意図間で発話数のバランスを取る

各意図に対して同様の数の発話を維持することで、バイアスを回避します。

### 5. 文脈依存および文脈非依存のバリエーションを組み込む

独立したクエリと以前の会話に依存するクエリの両方でトレーニングします。

### 6. 発話ライブラリを定期的に更新および改善

ライブデータをレビューし、新しい発話を追加し、パフォーマンスの低い発話を削除します。AIツール(例:Emplifi、Microsoft LUIS、IBM Watson)を活用して発話を拡張および検証します。

### 7. 特殊なケースのカバレッジを提供

挨拶、別れ、ヘルプリクエスト、苦情、フィードバックを含めます。断片的またはエラーが発生しやすい発話を考慮します。

### 8. テストと検証

実際の会話をシミュレートし、ユーザーフィードバックとチャットボットログに基づいて反復します。

### 9. 多言語および地域的バリエーションを処理

グローバルなオーディエンスのために、サポートされているすべての言語と方言の発話を含めます。

### 10. 機密情報や個人情報を避ける

発話データに個人情報や機密情報が含まれていないことを確認します。

#### ベストプラクティスチェックリストのサンプル

| プラクティス                                 | 説明                                  |
|-------------------------------------------|----------------------------------------------|
| 構造と長さを変える                 | 短い、中程度、長い発話               |
| 同義語と異なる表現を使用        | 「予約」/「リザーブ」/「スケジュール」              |
| 意図の重複を避ける                      | 各意図に対して明確な発話          |
| 実際のユーザーデータを使用                        | 本物の言語とタイポ                 |
| 定期的に更新                          | ライブユーザーフィードバックを組み込む               |
| 意図ごとの発話数のバランスを取る        | バイアスを防ぐ                                 |
| 特殊なケースをカバー                       | 挨拶、別れ、エラー処理         |

**参考資料:**  
- [Emplifi: AI Utterances - How To](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [Microsoft LUIS: Best Practices](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)

## 発話の種類、課題、および解決策

| カテゴリー            | 例                           | 対処される課題             | 解決策/ベストプラクティス                     |
|---------------------|-----------------------------------|-------------------------------|--------------------------------------------|
| 構造化          | 「注文状況:#12345」            | 形式の遵守               | 構造化/非構造化の両方の形式を含める |
| 非構造化        | 「ピザはどこ?」               | 表現のバリエーション             | 実際のインフォーマルな発話を収集           |
| 断片的          | 「アカウントキャンセル」                      | 部分的な入力                  | 不完全なフレーズでトレーニング              |
| スペルミス     | 「ログインできない」                     | タイポ/スペルミス             | スペル修正を使用するか、エラーでトレーニング  |
| 多言語        | 「Bonjour, je veux un café」        | 言語の多様性             | 多言語発話セット                |
| 文脈依存          | 「どのくらいかかる?」          | 文脈依存性             | 文脈認識NLUエンジン                  |
| ネガティブフィードバック   | 「機能していない」                     | 感情、サポートエスカレーション  | [感情分析](/en/glossary/sentiment-analysis/)、エスカレーショントリガー    |

**さらに読む:**  
- [IBM Watson: NLP in Chatbots](https://www.ibm.com/cloud/learn/natural-language-processing)
- [CogniTech: Intents, Entities, Synonyms](https://www.cognitech.systems/blog/artificial-intelligence/entry/intents-entities-synonyms-retrieval-natural-language-understanding)
- [BotPenguin: Utterance Glossary](https://botpenguin.com/glossary/utterance)

## 発話に関するよくある質問(FAQ)

**Q:チャットボットのトレーニングに複数の発話が必要なのはなぜですか?**  
A:ユーザーは同じ意図を多くの方法で表現します。多様な発話でトレーニングすることで、チャットボットは幅広い表現を認識でき、精度とユーザーエクスペリエンスが向上します。([SiteSpeakAI FAQ](https://sitespeak.ai/ai-chatbot-terms/utterance))

**Q:新しいチャットボットの発話を収集するにはどうすればいいですか?**  
A:過去のチャットログ、ユーザー調査、ブレインストーミング、実際の会話からのアクティブラーニングを使用します。

**Q:意図ごとに推奨される発話数は?**  
A:業界のガイダンス(例:Microsoft LUIS、Emplifi)では、意図ごとに10〜20の適切に選択された発話を推奨しています。多すぎると混乱を招き、少なすぎると精度が制限される可能性があります。([Emplifi Utterance Guide](https://docs.emplifi.io/platform/latest/home/ai-utterances))

**Q:スペルミスやスラングを含めるべきですか?**  
A:はい。一般的なタイポ、略語、スラングを含めることで、堅牢性が向上します。

**Q:発話に複数の意図を含めることはできますか?**  
A:一部のユーザーメッセージは複数の意図を表現する場合があります。チャットボットを設計して、優先順位付け、明確化、または複数意図の発話を処理します。

**Q:発話ライブラリはどのくらいの頻度で更新すべきですか?**  
A:継続的に。ライブインタラクションを定期的にレビューし、新しい発話を追加し、古い例を削除します。

**Q:発話はユーザー入力のみですか?**  
A:主にそうですが、一部のシステムは高度な[対話管理](/en/glossary/dialogue-management/)のためにボット/システムの発話もモデル化します。

## さらに読むためのリソース

- [Microsoft LUIS: Utterances](https://learn.microsoft.com/en-us/azure/ai-services/luis/concepts/utterances)
- [IBM Cloud: What is Conversational AI? (YouTube Search)](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [SiteSpeakAI: What is an Utterance?](https://sitespeak.ai/ai-chatbot-terms/utterance)
- [Emplifi: AI Utterances Documentation](https://docs.emplifi.io/platform/latest/home/ai-utterances)
- [LinkedIn: What is Utterance, Intent & Entity?](https://www.linkedin.com/pulse/what-utterance-intent-entity-conversational-ai-paul-blocchi)
- [CogniTech: Intents, Entities, Synonyms](https://www.cognitech.systems/blog/artificial-intelligence/entry/intents-entities-synonyms-retrieval-natural-language-understanding)
- [BotPenguin: Utterance—Types and Challenges](https://botpenguin.com/glossary/utterance)

## 重要なポイント

- **発話**とは、チャットボットや[会話型AI](/ja/glossary/conversational-ai/)に提供されるあらゆるユーザー入力(テキストまたは音声)です。
- 発話は、ユーザーの意図を理解し、意味のある応答のためにエンティティを抽出するプロセスを推進します。
- 多様で自然で代表的な発話を収集することは、効果的な会話型AIを構築するために不可欠です。
- 発話ライブラリを定期的にレビューおよび更新し、意図の重複を避け、実際のユーザー言語を反映します。
- スラング、タイポ、文脈、多言語入力などのバリエーションを処理することで、チャットボットの堅牢性とユーザー満足度が向上します。

## ビデオリソース

視覚的な学習とデモンストレーションについては、以下を参照してください:
- [YouTube: IBM Cloud Conversational AI](https://www.youtube.com/results?search_query=ibm+cloud+conversational+ai)
- [Microsoft Azure AI: NLP and Chatbots](https://www.youtube.com/results?search_query=microsoft+azure+ai+chatbot)

*カテゴリー:AIチャットボット&オートメーション*