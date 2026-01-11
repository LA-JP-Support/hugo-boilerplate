---
title: 出力パース
translationKey: output-parsing
description: 出力パースは、AI言語モデルのテキスト応答から構造化データ(JSON、Pythonオブジェクト)を抽出し、自動化、分析、システム統合に活用する技術です。
keywords:
- 出力パース
- LLM
- 構造化データ
- プロンプトエンジニアリング
- LangChain
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: Output Parsing
term: しゅつりょくぱーす
url: "/ja/glossary/output-parsing/"
aliases:
- "/ja/glossary/Output-Parsing/"
---
## 出力パースとは何か?
出力パースとは、大規模言語モデル(LLM)が生成した非構造化テキストを、ソフトウェアが確実に利用できる構造化フォーマット(JSON、Pythonの辞書、Pydanticモデルなど)に変換することを指します。LLMは決定論的なテキストエンジンではなく、同じプロンプトに対しても出力が変動する可能性があり、しばしば散文、説明、または自動化を複雑にするフォーマットを含んでいます。

**パース:** 一連のルールに従ってデータを分解し、生のインプットを信頼性の高いソフトウェア処理のための構造化アウトプットに変換すること。

## 出力パースが必要な理由

GPT-4、Claude、GeminiなどのLLMは自然言語で応答を生成しますが、これはユーザー向けチャットには理想的ですが、コード、RPAボット、分析ワークフローには問題があります。ビジネスロジックを自動化したり、APIと統合したりするには、一貫性のある機械可読な出力が必要です。

### 解決される問題

**一貫性のない出力:** LLMは異なるフォーマットで情報を返す可能性があり、直接抽出が信頼できません。

**下流の自動化:** ワークフローは頻繁に特定のデータのみを必要とし、完全なテキスト応答は不要です。

**検証と信頼性:** 出力が予測可能なスキーマに準拠することを保証します。

**統合:** 自然言語モデルが、構造化入力を必要とするアプリケーション、API、データベースと相互作用できるようにします。

## 主要概念

| 用語 | 定義 |
|------|------|
| **出力パーサー** | 非構造化LLM出力を構造化フォーマットに変換するソフトウェアコンポーネントまたはライブラリ |
| **スキーマ** | 出力データの期待される構造と型、多くの場合PydanticまたはJSON Schemaで強制される |
| **プロンプトエンジニアリング** | LLMが機械に優しいフォーマットで応答するように促すプロンプトの設計 |
| **関数呼び出し** | LLMが事前定義された署名に一致する出力を返す機能(主にOpenAI APIで提供) |
| **Pydanticモデル** | データ検証とパースにPydanticを使用するPythonクラス |
| **ストリーミング** | 生成される出力を段階的に処理すること、リアルタイムアプリケーションに有用 |
| **エラー修正パーサー** | LLMからの不正な形式の出力を修正または修復しようとするコンポーネント |

## 出力パースの使用方法

出力パースは、自動化、APIワークフロー、データパイプラインの中心です。AIと下流のビジネスロジック間の構造化された引き渡しを可能にします。

**API統合:** API/Webhook用の機械可読ペイロードを抽出します。

**データパイプライン:** モデル出力を検証し、分析またはレポートに供給します。

**自動化:** RPAボットまたはビジネスワークフローでアクションをトリガーします。

**会話エージェント:** フロントエンドレンダリングまたはロジック分岐のために応答が構造化されることを保証します。

### 使用例

**感情分析:**
```python
class Review(BaseModel):
    sentiment: str
    score: int
    themes: list[str]
```
出力: `{'sentiment': 'positive', 'score': 8, 'themes': ['friendly staff', 'quality food', 'parking']}`

**請求書抽出:** 請求書テキストを`invoice_number`、`date`、`amount`を含む構造化オブジェクトにパースします。

**レシピ生成:** LLM出力をレシピスキーマ(`name`、`ingredients`、`steps`)にパースします。

**エンティティ抽出:** 構造化データベースで使用するために名前、日付、場所を抽出します。

## 出力パースの戦略

### プロンプトエンジニアリング

LLMに特定の構造(JSON、YAML、XMLなど)で返信するよう指示します。

**プロンプト例:**
```
sentiment、score、themesのフィールドを含むJSONオブジェクトで応答してください。
```

**長所:** シンプル、依存関係なし。

**短所:** LLMが指示を無視し、無効な出力を生成することがあります。

### 出力パーサー

専門ライブラリ(例:LangChain Output Parsers)がLLM出力を処理し、スキーマを強制し、エラーを処理します。

**例:**
```python
from langchain_core.output_parsers import JsonOutputParser
parser = JsonOutputParser(pydantic_object=Review)
```

**長所:** 検証、エラー処理、スキーマ強制。

**短所:** 依存関係の追加、セットアップが必要。

### 関数/ツール呼び出し

LLM(特にOpenAIのGPT-4/3.5-turbo)は、関数署名に一致する方法で応答するようプロンプトでき、構造化データをネイティブに返します。

**例:**
```python
tool_def = {
    "type": "function",
    "function": {
        "name": "analyse_review",
        ...
    }
}
```

**長所:** 高度に決定論的な出力。

**短所:** 特定のAPI/モデルでのみサポート。

### ファインチューニング

特定のフォーマットで常に出力するようにLLMをカスタムトレーニングします。

**長所:** 専門的で大量のユースケースに対する最大の信頼性。

**短所:** コストが高く、大規模なデータセットが必要、柔軟性が低い。

## 実装例

### LangChainでのJSON出力のパース

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class MovieQuote(BaseModel):
    character: str = Field(description="The character who said the quote")
    quote: str = Field(description="The quote itself")

parser = JsonOutputParser(pydantic_object=MovieQuote)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

model = ChatOpenAI(temperature=0)
chain = prompt | model | parser

response = chain.invoke({"query": "Give me a famous movie quote with the character name."})
print(response)
```

**サンプル出力:**
```json
{
  "character": "Darth Vader",
  "quote": "I am your father."
}
```

### 構造化出力のストリーミング

```python
for chunk in chain.stream({"query": "Give me a famous movie quote with the character name."}):
    print(chunk)
```

ストリーミングにより部分的な結果とリアルタイム処理が可能になります。

### XMLとYAMLのパース

**XML例:**
```python
from langchain_core.output_parsers import XMLOutputParser

parser = XMLOutputParser(tags=["author", "book", "genre", "year"])
prompt = PromptTemplate(
    template="{query}\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
chain = prompt | model | parser

query = "Provide a detailed list of books by J.K. Rowling, including genre and publication year."
custom_output = chain.invoke({"query": query})
print(custom_output)
```

**YAML例:**
```python
from langchain.output_parsers import YamlOutputParser

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    steps: list[str]

parser = YamlOutputParser(pydantic_object=Recipe)
```

## 機能とメリット

**構造化出力生成:** 応答がJSON、辞書、リスト、またはPydanticオブジェクトとしてフォーマットされることを保証します。

**スキーマ強制:** 厳格なスキーマに対して出力を検証します。

**エラー処理と修正:** 不正な形式の出力を自動修正(OutputFixingParser、RetryOutputParser)。

**ストリーミングサポート:** 段階的処理のためのリアルタイム出力。

**チェーンとの統合:** LangChain、LlamaIndex、その他のフレームワークと連携します。

**複数のパーサータイプ:** JSON、XML、YAML、String、List、カスタムパーサー。

**検証:** Pydanticによる型とロジックの検証。

**互換性:** API、データベース、UIフレームワーク、分析ツールと統合します。

## 課題とエラー処理

### 一般的な問題

**不正な形式の出力:** LLM応答が有効なJSON/XML/YAMLではありません。

**一貫性のないフィールド:** キーの欠落または名前変更、または余分なフィールド。

**スキーマの不一致:** 出力タイプがスキーマと一致しません。

**非決定論的出力:** LLMは同じプロンプトに対して変動を出力する可能性があります。

### エラー処理技術

**Try/Exceptブロック:** 標準的なPythonエラー処理。

**OutputFixingParser:** LLM自体を使用して不正な形式の出力を再プロンプトまたは修復します。

**RetryOutputParser:** エラー時に出力を再パースまたは再生成しようとします。

**スキーマ検証:** 厳格な型/フィールド強制のためにPydanticまたはJSON Schemaを使用します。

**例:**
```python
from langchain.output_parsers import OutputFixingParser

parser = OutputFixingParser.from_parser(JsonOutputParser(pydantic_object=Review), llm=model)
```

## ベストプラクティス

- `parser.get_format_instructions()`を使用してプロンプトを明示的にする
- 厳格なフォーマットを期待する場合、より決定論的なLLM出力のために`temperature=0`を設定する
- パースされた出力を常に検証およびサニタイズする
- 大規模またはリアルタイム出力にはストリーミングを使用する
- 信頼性のためにエラー修正でパーサーをラップする
- 最大の決定論性のために、利用可能な場合は組み込みの関数呼び出しを優先する

## パース方法の比較

| 方法 | 使用例 | 強み | 制限事項 |
|------|--------|------|----------|
| **プロンプトエンジニアリング** | アドホック、シンプルな出力 | 簡単、依存関係なし | 一貫性がなく、エラーが発生しやすい |
| **出力パーサー** | 一般的なパース/検証 | スキーマ強制、堅牢 | 追加のライブラリ/セットアップ |
| **関数/ツール呼び出し** | APIベースの構造化出力 | 決定論的、信頼性が高い | モデル/APIサポートが必要 |
| **ファインチューニング** | 専門的、大量 | 究極の一貫性 | 高価、柔軟性がない |

## アプリケーション

**顧客レビュー分析:** 構造化された感情、トピック、スコアの抽出。

**リード資格認定:** 非構造化履歴書またはフォームを候補者オブジェクトにパース。

**スパム検出:** 自動分類のために提出物を構造化。

**ペルソナ分類:** 職種/ペルソナのセグメント化。

**請求書処理:** PDFまたはスキャンデータをERP用の行項目JSONに変換。

**調査自動化:** 自由形式の調査回答を分類。

## 重要なポイント

出力パースは、LLMが生成する自然言語と下流のソフトウェアおよび自動化の厳格な要件との間のギャップを埋めます。

適切なパース戦略と堅牢なエラー処理の選択は、信頼性にとって不可欠です。

スキーマ強制とプロンプトエンジニアリングは基礎です。

エコシステム(LangChain、OpenAI、Pydantic)は、すべてのユースケースに対応する豊富なツールとパターンを提供します。

## よくある質問

**Q: LLM出力が有効なJSONでない場合はどうすればよいですか?**
A: OutputFixingParserのようなエラー修正パーサーを使用するか、RetryOutputParserで再試行します。使用前に常に出力を検証してください。

**Q: どのLLMでも出力パースを使用できますか?**
A: はい、プロンプトエンジニアリングとパーサーを介して可能です。関数呼び出しにはモデル/APIサポートが必要です。

**Q: ストリーミング出力をどのように処理しますか?**
A: ストリーミング互換パーサーを使用し、到着した結果を処理します。

**Q: 出力パースの代わりにファインチューニングを検討すべきなのはいつですか?**
A: 絶対的な一貫性を必要とする大量の専門的なタスクの場合。

## 参考文献

- [Analytics Vidhya: Comprehensive Guide to Output Parsers](https://www.analyticsvidhya.com/blog/2024/11/output-parsers/)
- [Deepchecks: LLM Output Parsing Glossary](https://www.deepchecks.com/glossary/llm-output-parsing/)
- [LangChain: Output parsers Reference](https://reference.langchain.com/python/langchain_core/output_parsers/)
- [OpenAI: JSON Mode Documentation](https://platform.openai.com/docs/guides/text-generation/json-mode)
- [Xcitium: What is Parsing?](https://www.xcitium.com/blog/news/what-is-parsing/)
- [GeeksforGeeks: Output Parsers in LangChain](https://www.geeksforgeeks.org/artificial-intelligence/output-parsers-in-langchain/)
