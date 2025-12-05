---
title: スロットフィリング
translationKey: slot-filling-the-definitive-glossary-for-conversational
description: スロットフィリングは、会話型AIにおいてユーザーのクエリから特定のパラメータを抽出し、タスクを完了させる技術です。データ収集、自然な対話の実現、タスク完了の保証に不可欠な要素となっています。
keywords: ["スロットフィリング", "会話型AI", "チャットボット", "エンティティ", "インテント"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: すろっとふぃりんぐ
reading: スロットフィリング
kana_head: か
e-title: Slot Filling
---
## スロットフィリングとは?

スロットフィリングは、[会話型AI](/ja/glossary/conversational-ai/)のタスク指向対話システムにおける中核的な技術です。ユーザーのクエリから必要なパラメータ(スロットと呼ばれる)を識別・抽出することに焦点を当てています。これらのスロットは、フライトの予約、食事の注文、予約のスケジュール設定など、特定のアクションを実行するために必要です。

例えば、次のクエリの場合:

> 「7月20日にニューヨークからロンドンへのフライトを予約して。」

会話エージェントは以下を抽出する必要があります:
- **出発都市:** ニューヨーク
- **目的地都市:** ロンドン
- **日付:** 7月20日

スロットフィリングは、AIがこの情報を解析し、保存し、ユーザーに代わって応答またはアクションを実行するために効果的に使用できるようにするメカニズムです。情報が不足している場合、システムはユーザーに提供を促し、タスクに必要な完全なデータセットを確保します。

**権威ある情報源:**  
- [Microsoft Copilot Studio: Use entities and slot filling in agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)  
- [Dydu documentation: Slot filling](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling)  
- [Just AI Conversational Cloud: Slot filling](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling)  

## スロットフィリングが重要な理由

スロットフィリングは、AIシステムが以下を実現するために不可欠です:
- ユーザーのリクエストを完了するために必要なすべてのデータを収集する(例:予約、注文、カスタマーサポート)。
- ユーザーが自然に、任意の順序で、複数の会話ターンにわたって情報を提供できるようにする。
- 初期クエリから最大限の情報を抽出し、不足している部分のみを促すことで、不要なやり取りを削減する。
- アクションを実行する前に完全性と正確性を確保し、エラーや誤解を最小限に抑える。

スロットフィリングは、自由形式のユーザー入力から構造化データを抽出する必要がある会話インターフェースの基盤です([Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)、[Dydu](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling))。

## 主要概念:スロット、エンティティ、インテント

- **インテント:** ユーザーの目標または目的(例:「ホテルを予約する」、「ピザを注文する」)。
- **スロット:** インテントを実行するために必要な、または任意の情報のプレースホルダー(例:「チェックイン日」、「ピザのサイズ」)。
- **エンティティ:** スロットが期待するデータ型または情報のカテゴリー(例:都市、日付、数値、アイテムタイプ)。

**関係性:**  
インテントはアクションを定義し、スロットはそのアクションに必要なパラメータであり、エンティティは各スロットが期待するデータの種類を記述します([Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)、[Just AI](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling))。

## スロットフィリングで使用されるエンティティの種類

エンティティは、チャットボットがユーザー入力から関連データを認識・抽出できるようにします。主なカテゴリー:

### 1. 組み込み/システムエンティティ
会話プラットフォームによって事前定義されており、以下のような一般的なデータ型を処理します:
- 日付と時刻
- メールアドレス
- 電話番号
- 都市と場所
- 色、数値、通貨

[Microsoft Copilot Studio Prebuilt Entities](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-about#entities)

### 2. カスタムエンティティ
ドメイン固有のニーズに合わせて開発者が定義します。
- **クローズドリストエンティティ:** 許容される値の列挙セット(例:ピザのトッピング、製品SKU)。
- **正規表現(RegEx):** 構造化データを抽出するためのパターン(例:「INC000123」のようなチケット番号)。

カスタムエンティティは、専門的な語彙やデータ型を処理するボットの能力を拡張します。([Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling#closed-list-entities)、[Just AI entities guide](https://help.cloud.just-ai.com/en/jaicp/platform_ux/nlu_core/entities))

**ヒント:**  
同義語とファジーマッチングを使用してエンティティ認識を拡大します(例:「NYC」を「New York City」の同義語として)。

## スロットフィリングプロセス:ステップバイステップ

**1. 必要なスロットを定義:**  
特定のインテントを達成するために必要なすべての情報をリストアップします。

**2. 各スロットにエンティティを関連付ける:**  
各スロットが受け入れるべきデータ型またはパターンを指定します。

**3. ユーザー入力からスロット値を抽出:**  
NLU(自然言語理解)を使用して、各スロットの値を識別・抽出します。

**4. 不足しているスロットを促す:**  
必須スロットが未入力の場合、ボットは不足している情報を収集するための質問をします。

**5. マルチターン対話を処理:**  
ユーザーが複数のメッセージにわたって、任意の順序でスロットを埋められるようにします。

**6. 収集したスロット値を確認:**  
アクションを実行する前に、収集した情報をユーザーに提示して確認することもできます。

**7. タスクを実行:**  
すべての必須スロットが入力され、確認されたら、実行(例:予約、注文、サポート)に進みます。

**視覚的な例(Dyduより):**

- ユーザー:「ピザを注文したい。」
- ボット:「何切れ欲しいですか?」
- ユーザー:「8切れ」
- ボット:「どのタイプのピザが欲しいですか?」
- ユーザー:「ペパロニ」
- ボット:「8切れのペパロニピザですね。これで正しいですか?」
- ユーザー:「はい」
- ボット:「注文が確定しました!」

([Dydu slot filling documentation, with images and full dialog flow](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling))

## スロット設定:パラメータとオプション

スロットを定義する際の設定オプションには以下が含まれます:

- **名前:** スロットの識別子(例:`departure_city`)。
- **エンティティ:** 期待されるデータ型—組み込みまたはカスタム。
- **必須:** このスロットはタスクに必須ですか?はいの場合、ボットは入力されるか終了するまで促し続けます。
- **配列:** スロットは複数の値を受け入れるべきですか(例:「ピザを2枚注文:1枚はマルゲリータ、1枚はペパロニ」)?
- **明確化質問:** 不足しているスロット値を要求する際に使用するプロンプト。
- **デフォルト値:** スロットがオプションで未入力の場合のフォールバック値。
- **リセット/上書き:** ユーザーが新しい情報を提供した場合、スロットの値を上書きすべきですか?
- **最大リトライ/ガベージカウント:** プロセスを放棄する前に必要な情報を促す最大回数。
- **確認:** アクションを進める前にユーザーとスロット値を確認するオプション。

([Just AI Slot Parameter Details](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-parameters)、[Dydu Slot Options](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#id-1-configuration-of-the-slots))

## 実装戦略と技術的詳細

### 一般的なワークフロー

1. **インテント認識:**  
   NLUモデルを使用してインテントを検出し、適用されるスロットを識別します。

2. **エンティティ抽出:**  
   エンティティ認識を適用して、ユーザー入力からスロット値を抽出します。

3. **スロット追跡:**  
   会話全体を通じて、入力済み/未入力スロットの状態を維持します。

4. **プロンプトロジック:**  
   未入力の必須スロットについてユーザーに促すロジックを実装し、リトライや中断を管理します。

5. **スクリプト/コードアクセス:**  
   会話スクリプトまたはバックエンドコードで入力済みスロットにアクセスします。

6. **完了と確認:**  
   すべての必須スロットが入力されたら、バックエンドアクションを実行する前にユーザーと確認することもできます。

**例:コードでのスロット抽出(疑似コード)**
```python
if not slots['city']:
    prompt("どの都市に旅行しますか?")
elif not slots['date']:
    prompt("いつ旅行したいですか?")
else:
    confirm(f"{slots['date']}に{slots['city']}へのチケットを予約します。これで正しいですか?")
```

### プラットフォーム固有の詳細

- **Copilot Studio:**  
  - 事前構築済みおよびカスタムエンティティを使用。
  - ファジーマッチングと自動修正のために「スマートマッチング」を有効化。
  - クローズドリストエンティティに同義語を追加。
  - 構造化データ抽出のために正規表現を使用。

([Copilot Studio Entity & Slot Documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling))

- **Just AI Conversational Cloud:**  
  - `chatbot.yaml`で必須/オプションスロット、配列タイプ、リトライ/タイムアウトロジックを設定。
  - `$parseTree`または関連変数を介してスロットにアクセス。

([Just AI Slot Filling Guide](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling))

- **Dydu:**  
  - スロットナレッジタイプを定義し、スロットフィリングプロセスを視覚的に設定。
  - 導入文、確認文、終了文を使用してユーザーフローを管理。

([Dydu Slot Filling Setup Guide](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#id-1-configuration-of-the-slots))

## 実用例と対話スニペット

### 例1:ピザ注文(Dydu)
- **必須スロット:** 切れ数、ピザタイプ

```
ユーザー:「ピザを注文したい。」
ボット:「何切れ欲しいですか?」
ユーザー:「8切れ」
ボット:「どのタイプのピザが欲しいですか?」
ユーザー:「ペパロニ」
ボット:「8切れのペパロニピザですね。これで正しいですか?」
ユーザー:「はい」
ボット:「注文が確定しました!」
```
([Dydu slot filling example](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#use-case-order-a-pizza))

### 例2:電車のチケット予約
- **必須スロット:** 目的地都市、日付

```
ユーザー:「パリ行きの電車のチケットを買いたい。」
ボット:「いつ旅行したいですか?」
ユーザー:「来週の月曜日。」
ボット:「来週の月曜日のパリ行きチケットですね。進めてよろしいですか?」
```
([Dydu train ticket example](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling#use-case-buy-a-train-ticket))

### 例3:天気照会(Just AI)
- **スロット:** 都市(必須)、日付(オプション)

```
ユーザー:「今日のロンドンの天気はどう?」
ボット:「今日のロンドンの天気は晴れで20°Cです。」
```
日付が不足している場合:
```
ユーザー:「パリの天気はどう?」
ボット:「いつの予報が必要ですか?」
```
([Just AI slot filling example](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-extraction))

## スロットフィリングのベストプラクティス

1. **可能な限り組み込みエンティティを使用:**  
   一般的なデータ型の堅牢な処理のために、プラットフォーム提供のエンティティを活用します。

2. **クローズドリストエンティティに同義語を追加:**  
   バリエーションや関連用語で認識を拡大します。

3. **スマートまたはファジーマッチングを有効化:**  
   スペルミスや類似用語を許容してエンティティ認識を拡大します。

4. **正規表現を創造的に使用:**  
   特にコードやIDなどの構造化データ形式にはRegExを使用します。

5. **重要なスロット値を確認:**  
   重要なアクションを実行する前に、常にユーザーと確認します。

6. **最大リトライ/プロンプト制限を設定:**  
   未入力スロットのプロンプトを制限することで、無限ループを防ぎます。

7. **中断に対応した設計:**  
   ユーザーがスロットフィリングフローを終了したり、トピックをスムーズに切り替えられるようにします。

8. **配列と複数のスロット値を処理:**  
   ユーザーが同じスロットに複数の値を提供するシナリオをサポートします。

([Just AI Best Practices](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#interruption-of-slot-filling)、[Microsoft Copilot Studio Best Practices](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/slot-filling-best-practices))

## よくある落とし穴と回避方法

- **明確化質問の欠如:**  
  必須スロットにプロンプトが指定されていない場合、インテントがマッチしない可能性があります。

- **過度に厳格なエンティティ定義:**  
  エンティティを狭いリストに制限しないでください。同義語とスマートマッチングを使用します。

- **スロットフィリング中断の未処理:**  
  ユーザーが行き詰まった場合、スロットフィリングを放棄またはリセットする方法を常に提供します。

- **確認ステップの無視:**  
  スロット値の確認を怠ると、エラーやユーザーの不満につながる可能性があります。

- **マルチターン/順不同入力の未サポート:**  
  ユーザーは複数のメッセージにわたって任意の順序で情報を提供することを期待しています。

- **最大リトライ/タイムアウトの未処理:**  
  ユーザーを無限の明確化ループに閉じ込めないよう、適切な制限を設定します。

([Just AI Pitfalls](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#interruption-of-slot-filling)、[Microsoft Copilot Studio Pitfalls](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/slot-filling-best-practices))

## 高度なアプローチ:BERTとその先

### スロットフィリングにBERTを使用

BERT(Bidirectional Encoder Representations from Transformers)は、深い文脈的言語理解を活用することで、スロットフィリングに革命をもたらしました:

- **文脈的表現:** BERTは入力全体から文脈を捉え、正確なスロット境界検出を支援します。
- **曖昧性の解決:** ユーザークエリの曖昧な表現や略語を処理します。
- **OOV処理:** サブワードトークン化により、ユーザーが稀な用語やスペルミスした用語を使用しても抽出をサポートします。
- **ファインチューニング:** 事前学習済みBERTモデルは、ドメイン適応のためにスロットフィリングデータセットでファインチューニングできます。

**実装ステップ:**
1. **データ準備:** ラベル付きデータセット(トークン+スロットラベル)を作成。
2. **BERTトークン化:** テキストをトークン/サブワードに変換。
3. **モデルアーキテクチャ:** BERTをエンコーダーとして使用し、スロット分類層を追加。
4. **ファインチューニング:** クロスエントロピー損失を使用してスロットラベル付きデータで学習。
5. **推論:** ユーザー入力の各トークンのスロットラベルを予測。

**Pythonの例([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/conversational-ai-with-bert/)):**
```python
from transformers import BertTokenizer, BertForTokenClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=num_labels)

# トークン化してスロットを予測
inputs = tokenizer("Book a flight from New York to London", return_tensors='pt')
outputs = model(**inputs)
```

**リソース:**  
- [Enhancing Conversational AI with BERT: The Power of Slot Filling - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/conversational-ai-with-bert/)

## ユースケースと実世界のアプリケーション

スロットフィリングは、幅広い[会話型AI](/ja/glossary/conversational-ai/)アプリケーションを支えています:

- **旅行予約:** 出発/到着都市、日付、乗客数、クラスなど。
- **Eコマース注文:** 製品タイプ、数量、サイズ、色、配送先住所。
- **カスタマーサポート:** チケット番号、アカウントID、問題の説明。
- **レストラン予約:** レストラン名、日付、時間、人数、特別なリクエスト。
- **スマートホーム/ユーティリティ:** デバイス名、アクション、スケジュール、設定。
- **ヘルスケアチャットボット:** 症状、予約日、医師名、保険情報。

([Dydu Use Cases](https://docs-en.dydu.ai/contents/knowledge/knowledge-types/slot-filling)、[Just AI Use Cases](https://help.cloud.just-ai.com/en/jaicp/NLU_core/slot_filling#slot-extraction))

## 重要なポイント

- スロットフィリングは、タスク指向会話型AIの基本であり、ボットがインテント実行に必要なすべてのデータを収集できるようにします。
- インテント、スロット、エンティティの定義と、抽出のための堅牢なNLUに依存しています。
- マルチターンで柔軟な対話と確認ステップにより、使いやすさと正確性が向上します。
- ベストプラクティスには、組み込みエンティティの活用、同義語とファジーマッチングの使用、適切なリトライ制限の設定が含まれます。
- BERTのような最先端モデルにより、高度で高精度なスロット抽出が可能になります。

## よくある質問(FAQ)

**Q1: スロットとエンティティの違いは何ですか?**  
スロットは、タスクを完了するために必要な特定の情報のプレースホルダー(例:チケット予約の「日付」)であり、エンティティはそのスロットを埋めることができるデータカテゴリーまたはタイプ(例:「都市」、「数値」、「日付」)です。

**Q2: チャットボットはどのスロットを埋めるべきかをどのように知るのですか?**  
各インテントは、必須およびオプションのスロットのセットに関連付けられています。チャットボットは、どれが入力されたかを追跡し、ユーザー入力と対話状態に基づいて、不足しているものを促します。

**Q3: ユーザーが必須スロット値をすべて提供しない場合はどうなりますか?**  
チャットボットは、不足している必須スロットについて明確化質問で促し、最大リトライ制限に達するか、ユーザーがプロセスを放棄するまで続けます。

**Q4: ユーザーは1つのメッセージで複数のスロットを埋めることができますか?**