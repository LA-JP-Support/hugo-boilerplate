---
title: クエリ拡張
translationKey: query-expansion
description: クエリ拡張は、検索エンジン、AIチャットボット、RAGシステムにおいて、ユーザーの検索クエリに同義語や関連用語を追加することで再構成し、意図のギャップを埋めて関連性を向上させる手法です。
keywords: ["クエリ拡張", "情報検索", "AIチャットボット", "RAG", "検索エンジン"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: クエリかくちょう
reading: クエリ拡張
kana_head: か
e-title: Query Expansion
---
## クエリ拡張とは?

クエリ拡張は、情報検索および検索システムにおける技術であり、ユーザーの元のクエリに関連用語、同義語、または文脈的に関連するフレーズを追加することで、検索精度と再現率を大幅に向上させます。例えば、「心臓病」を検索すると、「心血管疾患」「心筋梗塞」「心臓発作」などの用語が自動的に含まれ、より広範囲の関連文書を捕捉できます([ITU Online](https://www.ituonline.com/tech-definitions/what-is-query-expansion/)、[Stanford NLP](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf))。

クエリ拡張は、現代の検索エンジン、エンタープライズ検索、医学文献データベース、法律検索システム、AIチャットボット、そしてユーザークエリを多様で大規模な情報リソースにマッチングする必要があるあらゆるシステムにとって不可欠です。人間の言語が持つ自然な変動性と曖昧性を補完します。

### 基本原則

- **同義性:** 異なる単語が同じ意味を持つ(「car」と「automobile」)。
- **多義性:** 同じ単語が異なる意味を持つ(「spring」は季節またはコイル)。
- **文脈マッチング:** 文字通りのクエリを超えてユーザーの意図を理解する。

## なぜクエリ拡張が必要なのか?その動機

### 語彙不一致問題

ユーザーは、関連文書に存在する単語とは異なる単語を使用することがよくあります。例えば、ユーザーが「格安航空券」を検索しても、「割引航空運賃」や「予算旅行」を使用している文書を見逃す可能性があります。この語彙不一致は、検索と情報検索における中心的な問題です([ITU Online](https://www.ituonline.com/tech-definitions/what-is-query-expansion/))。

### 短く曖昧なクエリ

多くのユーザークエリは短いか曖昧です。例えば、「Spring」は季節、コイル、またはJavaフレームワークを指す可能性があります。文脈がなければ、システムはユーザーの真の意図を推測するのに苦労します。

### 暗黙的なユーザー意図

ユーザーはすべての文脈的詳細を指定することはほとんどありません。「最高のレストラン」の検索は、場所、料理、予算、営業時間を暗示している可能性がありますが、これらは何も指定されていません。

クエリ拡張は、人間の意図と機械の理解の間のこのコミュニケーションギャップを埋めます。

## クエリ拡張の種類と技術

クエリ拡張は、古典的な同義語拡張から高度な機械学習モデルまで、さまざまな方法を包含します。

### 古典的技術

- **同義語拡張:** 元の用語の同義語を追加(「car」→「automobile」、「vehicle」)。
- **ステミング/レンマ化:** 単語を語根形式に縮小(「running」、「ran」、「runs」→「run」)。
- **関連用語拡張:** 文脈的に関連する用語を追加(「糖尿病」→「インスリン」、「グルコース」)。
- **自動シソーラス生成:** キュレーションされた、または機械構築されたシソーラスを使用([Stanford NLP](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf))。
- **文脈拡張:** クエリの文脈またはユーザープロファイルを考慮(例:開発者向けの「Spring」を「Javaフレームワーク」として)。

### 高度/AI駆動技術

- **適合性フィードバック:** ユーザーが結果を関連性ありまたはなしとマークし、システムが拡張を改善([Stanford NLP、第9章](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf))。
- **疑似適合性フィードバック:** システムが上位N件の結果を関連性ありと仮定し、拡張用の用語を抽出。
- **意味埋め込み:** Word2Vec、GloVe、BERTなどのモデルを使用して意味的に類似した用語を見つける。
- **共起分析:** 関連文書で頻繁に一緒に出現する用語を特定。
- **ハイブリッドアプローチ:** 手動キュレーションと自動拡張を組み合わせる([ITU Online](https://www.ituonline.com/tech-definitions/what-is-query-expansion/))。

### 実装アプローチ

- **手動拡張:** 人間の専門家によってキュレーション(法律、医学で一般的)。
- **自動拡張:** データ駆動およびアルゴリズム的。
- **ハイブリッド拡張:** 人間の専門知識と自動化を融合。

**包括的参照表**

| 技術                  | 動作方法                                              | 例                                      |
|----------------------|-----------------------------------------------------|----------------------------------------|
| 同義語拡張            | 同義語を追加                                          | 「car」→「automobile」、「vehicle」      |
| ステミング/レンマ化    | 単語形式を正規化                                      | 「running」→「run」                     |
| 関連用語拡張          | 文脈的に関連する用語を追加                             | 「心臓発作」→「心筋梗塞」                |
| 適合性フィードバック   | ユーザーフィードバックから拡張を改善                    | クリックされた文書が追加用語に影響       |
| 埋め込みベース拡張     | ベクトル空間での意味的類似性を使用                     | 「AI」→「人工知能」、「ML」             |
| 共起分析             | 頻繁に一緒に見つかる用語を追加                         | 「太陽」+「エネルギー」                 |
| 文脈拡張             | ユーザー/場所/文脈を活用して拡張                       | 「Spring」+開発者プロファイル→「Java」   |

**参考文献:**  
- [Stanford NLP - Relevance Feedback and Query Expansion PDF](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf)  
- [ITU Online - Query Expansion](https://www.ituonline.com/tech-definitions/what-is-query-expansion/)

## クエリ拡張の仕組み:ステップバイステップ

### パイプライン例

1. **クエリ分析:** システムがユーザーのクエリを受信(例:「気候変動」)。
2. **用語選択:** 主要用語、同義語、および可能な曖昧性を特定。
3. **拡張生成:** 関連用語/フレーズを生成(例:「地球温暖化」、「温室効果ガス排出」)。
4. **クエリ再構成:** 元の用語と拡張用語を組み合わせて新しいクエリを作成。
5. **検索実行:** 拡張されたクエリを実行して、より広範で関連性の高い結果セットを取得。

AI駆動パイプライン、特にRetrieval-Augmented Generation(RAG)システムの場合、プロセスにはクエリをベクトルとしてエンコードし、意味的に関連する文書を取得し、それらをランク付けし、クエリと取得した文書の両方を言語モデルに供給して最終的な回答を生成することが含まれます([Glean RAG Examples](https://www.glean.com/blog/rag-examples)、[Signity Solutions - RAG](https://www.signitysolutions.com/blog/real-world-examples-of-retrieval-augmented-generation))。

**Python例(Haystack):**
```python
query_expander = QueryExpander()
retriever = MultiQueryInMemoryBM25Retriever(InMemoryBM25Retriever(document_store=doc_store))

expanded_retrieval_pipeline = Pipeline()
expanded_retrieval_pipeline.add_component("expander", query_expander)
expanded_retrieval_pipeline.add_component("keyword_retriever", retriever)

expanded_retrieval_pipeline.connect("expander.queries", "keyword_retriever.queries")

results = expanded_retrieval_pipeline.run({"expander": {"query": "climate change"}}, include_outputs_from=["expander"])
```
**詳細は[Haystackの公式ガイド](https://haystack.deepset.ai/blog/query-expansion)を参照してください。**

## クエリ拡張の歴史的進化

| 時代                  | 主要技術                | 特徴/強み                    | 制限事項                            |
|----------------------|------------------------|----------------------------|-------------------------------------|
| 初期Web(1990年代)     | 同義語リスト            | 高速、予測可能               | 硬直的、文脈認識なし                 |
| 2000年代             | 統計分析               | データ駆動、一部パーソナル化  | 大規模データが必要、プライバシー問題  |
| 2010年代             | 疑似適合性フィードバック | 文脈的、自己改善             | ノイズを導入する可能性               |
| 2020年代             | LLM、埋め込み          | 深い文脈、曖昧性解消         | リソース集約的、過剰拡張のリスク      |

**参考文献:**  
- [Stanford NLP - Query Expansion PDF](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf)  
- [Sandgarden - Query Expansion Revolution](https://www.sandgarden.com/learn/query-expansion)

## クエリ拡張の利点

- **再現率の向上:** 異なる用語を使用する関連文書を回収。
- **検索精度の向上:** 文字通りの入力だけでなく、ユーザーの意図により良くマッチ。
- **ユーザーエクスペリエンスの向上:** 繰り返し検索が減少し、フラストレーションが軽減。
- **曖昧性解消:** 文脈を使用して短いまたは曖昧なクエリを処理。
- **自然言語サポート:** ユーザーが自分の言葉で検索可能。
- **パーソナライゼーション:** ユーザー履歴とプロファイルに合わせて拡張を調整可能。

**出典:**  
- [ITU Online - Benefits of Query Expansion](https://www.ituonline.com/tech-definitions/what-is-query-expansion/)  
- [Glean - RAG Examples](https://www.glean.com/blog/rag-examples)

## 課題と考慮事項

- **過剰拡張:** 過度または無関係な用語が精度を低下させる。
- **計算オーバーヘッド:** より多くの用語がシステム負荷と遅延を増加させる。
- **関連性の維持:** 追加された用語はユーザーの意図と一致する必要がある。
- **プライバシー:** 個人データの使用は規制上の懸念を引き起こす可能性がある。
- **バイアスの増幅:** 拡張アルゴリズムがバイアスを永続化する可能性がある。
- **透明性:** 拡張が不透明な場合、ユーザーが結果を理解できない可能性がある。
- **敵対的操作:** SEOやスパム攻撃が拡張を悪用する可能性がある。

**Stanford NLP:**
> 「過剰拡張は、無関係な用語が検索プロセスに含まれるため、精度の低下につながる可能性があります。」([Stanford PDF、セクション9.2](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf))

## ビジネスおよび業界アプリケーション

### 検索エンジン

Google、Bing、およびエンタープライズ検索エンジンは、より正確で文脈認識の高い検索のためにクエリ拡張を使用します([ITU Online](https://www.ituonline.com/tech-definitions/what-is-query-expansion/))。

### AIチャットボット&カスタマーサポート

チャットボットは、クエリ拡張とRAGを使用して、さまざまなユーザーの言い回しを解釈し、クエリを解決します([Signity Solutions](https://www.signitysolutions.com/blog/real-world-examples-of-retrieval-augmented-generation))。

### Eコマース

「ランニングシューズ」を「アスレチックフットウェア」、「ジョギングスニーカー」などに拡張し、製品発見とコンバージョンを改善します。

### ヘルスケア

医療検索は「心臓発作」を「心筋梗塞」に拡張し、臨床医のための包括的な検索を保証します([Glean - Healthcare RAG](https://www.glean.com/blog/rag-examples))。

### 法律&リサーチ

「契約紛争」を関連する法令や判例法に拡張し、法律調査とコンプライアンスをサポートします。

### Retrieval-Augmented Generation(RAG)

LLM駆動システムは、回答を生成する前にすべての関連コンテキストを取得するために拡張を使用します([Glean RAG Examples](https://www.glean.com/blog/rag-examples))。

### 教育

学習プラットフォームは、学生の文脈に基づいてクエリを拡張し、関連リソースの発見を保証します。

### 多言語アプリケーション

言語/文化を超えてクエリを拡張し、意味的ギャップを埋めます。

## 実装ノートとパイプライン例

### 拡張を伴うキーワードベース検索

```python
expander = QueryExpander()
expanded_queries = expander.run(query="open source NLP frameworks", number=4)
# 出力: ['natural language processing tools', 'free nlp libraries', ...]
```

### BM25 + クエリ拡張

マルチクエリ検索には`MultiQueryInMemoryBM25Retriever`を使用:
```python
expanded_retrieval_pipeline = Pipeline()
expanded_retrieval_pipeline.add_component("expander", query_expander)
expanded_retrieval_pipeline.add_component("keyword_retriever", retriever)
expanded_retrieval_pipeline.connect("expander.queries", "keyword_retriever.queries")
```
([Haystack: Query Expansion Demo](https://haystack.deepset.ai/blog/query-expansion))

### 埋め込み/意味検索

ベクトルベースの意味拡張にはWord2Vec、GloVe、BERTなどを使用します。

## 新たなトレンドと将来の方向性

- **大規模言語モデル(LLM):** GPT-4、BERTなどは、文脈認識型の適応的拡張を可能にします([Glean RAG Examples](https://www.glean.com/blog/rag-examples))。
- **パーソナライズされた拡張:** ユーザープロファイル、検索履歴、デバイスコンテキストへのリアルタイム適応。
- **マルチモーダル拡張:** テキスト、画像、音声、その他のモダリティを使用したクエリ拡張。
- **説明可能なAI(XAI):** ユーザーに対して拡張プロセスを透明化。
- **リアルタイムフィードバック:** ユーザーインタラクションからの継続的学習。
- **多言語拡張:** 多言語クエリとコンテンツの処理。
- **公平性と責任あるAI:** バイアス、プライバシー、説明可能性への対処。

**参考文献と例:**  
- [Medium: Query Expansion in RAG](https://medium.com/@sahin.samia/query-expansion-in-enhancing-retrieval-augmented-generation-rag-d41153317383)  
- [Glean: RAG Examples](https://www.glean.com/blog/rag-examples)  
- [Signity Solutions: RAG Examples](https://www.signitysolutions.com/blog/real-world-examples-of-retrieval-augmented-generation)

## よくある質問

**Q: 情報検索におけるクエリ拡張とは何ですか?**  
A: ユーザーの元のクエリに同義語、関連用語、または文脈的に関連するフレーズを追加して再構成し、関連文書の検索を改善する技術です([ITU Online](https://www.ituonline.com/tech-definitions/what-is-query-expansion/))。

**Q: 同義語拡張はどのように検索結果を改善しますか?**  
A: 同義語を含めることで、同じ概念に対して異なる単語を使用している文書の検索が可能になり、再現率が向上します。

**Q: 主な課題は何ですか?**  
A: 過剰拡張、計算の複雑さ、関連性、プライバシー/バイアスの問題、透明性の欠如です。

**Q: クエリ拡張は曖昧なクエリに役立ちますか?**  
A: はい。文脈拡張は、短いまたは曖昧なクエリの背後にある可能性の高い意図を推測するのに役立ちます。

**Q: クエリ拡張はどこで使用されていますか?**  
A: 検索エンジン、AIチャットボット、Eコマース、ヘルスケア、法律調査、教育プラットフォーム、RAGシステムで使用されています。

**Q: クエリ拡張は常に結果を改善しますか?**  
A: 必ずしもそうではありません。調整が不十分な拡張は精度を低下させる可能性があり、慎重なバランスが必要です。

**Q: クエリ拡張はどのように実装されますか?**  
A: 同義語リスト、統計分析、機械学習、埋め込み、LLMを通じて、多くの場合検索パイプラインに統合されます。

## 参考文献とリソース

- [ITU Online: What Is Query Expansion?](https://www.ituonline.com/tech-definitions/what-is-query-expansion/)
- [Stanford NLP: Relevance Feedback and Query Expansion (PDF)](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf)
- [Medium: Query Expansion in Enhancing RAG](https://medium.com/@sahin.samia/query-expansion-in-enhancing-retrieval-augmented-generation-rag-d41153317383)
- [Glean: RAG Use Cases](https://www.glean.com/blog/rag-examples)
- [Signity Solutions: 10 Real-World RAG Examples](https://www.signitysolutions.com/blog/real-world-examples-of-retrieval-augmented-generation)
- [Haystack: Advanced RAG: Query Expansion](https://haystack.deepset.ai/blog/query-expansion)
- [MongoDB: Maximizing Search Efficiency with Query Expansion](https://www.mongodb.com/resources/basics/search-relevance-query-expansion)
- [YouTube: Query Expansion in Information Retrieval](https://www.youtube.com/results?search_query=query+expansion+information+retrieval)

**基礎および上級読者向け:**  
- [Stanford NLP - IR Book, Chapter 9](https://nlp.stanford.edu/IR-book/pdf/09expand.pdf)
- [Sandgarden: How Query Expansion Revolutionized AI Search](https://www.sandgarden.com/learn/query-expansion)
- [Haystack: Query Expansion in RAG](https://haystack.deepset.ai/blog/query-expansion)