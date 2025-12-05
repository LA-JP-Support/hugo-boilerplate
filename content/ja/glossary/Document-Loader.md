---
title: ドキュメントローダー
translationKey: document-loader
description: ドキュメントローダーは、生データを自動的に取り込み、LLMパイプラインやベクトルストアのインデックス作成などのAIタスク向けに構造化されたDocumentオブジェクトに変換するソフトウェアモジュールです。
keywords: ["Document Loader", "AIパイプライン", "LLM", "データ取り込み", "LangChain"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: どきゅめんとろーだー
reading: ドキュメントローダー
kana_head: た
e-title: Document Loader
---
## Document Loaderとは?

**Document Loader**は、ファイル、Webページ、クラウドドキュメント、データベースエントリなどの生データを自動的に取り込み、*Documentオブジェクト*と呼ばれる構造化フォーマットに変換するソフトウェアモジュールまたはコンポーネントです。これらのオブジェクトは、情報検索、LLM(大規模言語モデル)パイプライン、ベクトルストアのインデックス化、ワークフロー自動化などの下流AIタスクに最適化されています。

Document loaderは、多様な非構造化または半構造化コンテンツソースを扱う複雑さを抽象化するために構築されています。意味のあるテキストを解析・抽出し、コンテキストメタデータで強化し、元のファイルタイプやデータソースに関係なく、標準化された一貫性のある構造を出力します。この統一性は、AIチャットボット、検索エンジン、データ分析パイプラインなど、予測可能で豊富な入力データを必要とするアプリケーションにとって重要です。

**参考資料:**  
- [LangChain: Document Loaders - 公式ドキュメント](https://docs.langchain.com/oss/python/integrations/document_loaders)

## Document Loaderが使用される理由

- **標準化:**  
  現実世界のデータは無数のフォーマット、エンコーディング、レイアウトで存在します。Document loaderはこの入力を調和させ、PDF、HTML、CSV、JSONなどのソースを、各ソースごとにカスタム解析ロジックを必要とせずに、AIシステムやデータベースが利用できる一貫したスキーマに変換します。

- **自動化:**  
  Document loaderは、新しいデータソースごとに抽出・解析スクリプトを繰り返し書く必要性を排除します。代わりに、開発オーバーヘッドとメンテナンスを最小限に抑える、再利用可能でよくテストされたツールを提供します。

- **コンテキストの保持:**  
  Loaderは単に生テキストを抽出するだけでなく、ソースの場所、ページまたは行番号、タイムスタンプ、コンテンツタイプなどの重要なメタデータも付加します。このコンテキストは、AI駆動アプリケーションにおける検索、トレーサビリティ、コンプライアンス、きめ細かい検索に不可欠です。

- **スケーラビリティ:**  
  Loaderは大規模な取り込みシナリオを処理するように設計されており、[バッチ処理](/ja/glossary/batch-processing/)、ストリーミング、ローカルおよびクラウドベースのリソースの両方をサポートします。特に遅延読み込みメカニズムを通じて、パフォーマンスとメモリ効率の両方を最適化します。

- **プラグアンドプレイ統合:**  
  [LangChain](https://www.langchain.com/)などのフレームワークやベクトルデータベースは、標準的なDocumentフォーマットでの入力を期待します。Document loaderはこの標準インターフェースを提供し、AIパイプライン全体でシームレスな接続を保証します。

**参考資料:**  
- [LangChain Document Loaders: ファイル読み込みの完全ガイド + コード例 (Latenode)](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-document-loaders-complete-guide-to-loading-files-code-examples-2025)
- [LLMに適切な情報を与える: LangChainのDocument Loaderをマスターする (Medium)](https://medium.com/@ashutoshsharmaengg/feeding-your-llm-right-mastering-langchains-document-loaders-64ff06675c7b)

## Documentオブジェクトの構造

Document loaderがデータソースを処理すると、**Documentオブジェクト**を生成します。このオブジェクトは、LLMパイプライン、ベクトルストアの取り込み、検索拡張生成(RAG)システムの基本単位です。

**コアフィールド:**

### page_content

- **定義:** PDFページ、CSV行、HTMLパラグラフなど、ソースから抽出された主要なテキストまたはコンテンツ。
- **型:** 文字列
- **詳細:** コンテンツは通常、クリーニング、デコードされ、下流のAIタスクでの使用を保証するために前処理される場合があります(例:空白の正規化、定型文の削除)。

### metadata

- **定義:** コンテキスト、説明、ソース関連のキーと値のペアを保持する辞書またはマップで、検索、フィルタリング、トレーサビリティに必要な追加情報でメインコンテンツを強化します。
- **一般的なメタデータフィールド:**
    - `source`: ファイルパス、URL、データベース識別子、またはクラウドURI
    - `page`: ページ番号(ページ分割されたドキュメントの場合)
    - `row`: 行インデックス(表形式データの場合)
    - `title`: タイトルまたは見出し(ソースから抽出された場合)
    - `filetype`: ファイル拡張子またはMIMEタイプ
    - `created_at`、`last_modified`: 出所のタイムスタンプ
    - `category`、`section`: フィルタリングまたは分析のための組織フィールド

### id (オプション)

- **定義:** ドキュメントの一意の識別子(文字列またはUUID)で、重複排除、相互参照、データベースインデックス化に不可欠です。

#### 例: PythonでのDocumentオブジェクト(LangChainスタイル)
```python
from langchain_core.documents import Document

doc = Document(
    page_content="This is a page from a PDF.",
    metadata={
        "source": "report.pdf",
        "page": 2,
        "created_at": "2024-07-21"
    },
    id="doc-002"
)
```

**参考資料:**  
- [LangChain: Documentオブジェクトリファレンス](https://reference.langchain.com/python/langchain_core/documents/#langchain_core.documents.base.Document)

## Document Loaderの種類

Document loaderは、処理するデータソースまたはファイルタイプによって分類されます。このモジュール性により、起源に関係なく、あらゆるデータを同じDocumentオブジェクト構造に変換できます。

### ファイルタイプ別

- **PDF Loader:**  
  PDFファイルからテキストとメタデータを抽出することに特化し、複数ページのレイアウト、スキャン画像(OCR付き)を処理し、ページ番号を保持します。  
  例: [PyPDFLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader)、[PDFPlumberLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/pdfplumber)、[UnstructuredPDFLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/unstructured_file)

- **テキストファイルLoader:**  
  `.txt`、`.md`、`.log`などのプレーンテキストフォーマットを処理し、ファイル全体を抽出するか、行/セクションで分割します。  
  例: [TextLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/text)

- **CSV Loader:**  
  行または列を個別のDocumentオブジェクトとして抽出し、ソース、行インデックス、選択された列のメタデータを含めます。  
  例: [CSVLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/csv)

- **JSON Loader:**  
  構造化またはネストされたデータ用に設計され、必要に応じてフィールドをフラット化または抽出します。

- **MS Office Loader:**  
  `.docx`、`.xlsx`、`.pptx`ファイルをサポートし、段落、表、スライド、またはセルを抽出します。

- **HTML/Markdown Loader:**  
  Webページ、ドキュメント、またはWikiを解析し、読みやすいテキストを抽出し、構造メタデータを保持します。

### データソース別

- **ローカルファイルシステムLoader:**  
  ファイルパスまたはディレクトリパターンを使用してディスクからファイルを読み取ります。

- **Web URL Loader:**  
  Webページまたはサイト全体からコンテンツをスクレイピングまたはダウンロードします。  
  例: [WebBaseLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/web_base)、[SitemapLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/sitemap)、[RecursiveURLLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/recursive_url)

- **クラウドストレージLoader:**  
  AWS S3、Azure Blob、Google Driveからドキュメントを取得します。  
  例: [S3DirectoryLoader](https://docs.langchain.com/oss/python/integrations/document_loaders/aws_s3_directory)

- **API & サードパーティプラットフォーム:**  
  YouTube(トランスクリプト)、Wikipedia、Notion、Slack、GitHubなどのサービスからデータを取り込みます。

- **データベースLoader:**  
  SQLまたはNoSQLデータベースから行またはレコードを抽出します。

#### 特殊なLoader

- **DirectoryLoader:**  
  ディレクトリからパターンに一致するすべてのファイルを再帰的に読み込みます。

- **Recursive Loader:**  
  深いフォルダ構造を走査するか、Webサイト全体をクロールします。

- **カスタムLoader:**  
  独自または一般的でないデータソース用の拡張可能な基底クラス。

**参考資料:**  
- [カテゴリ別Document Loader - LangChainドキュメント](https://docs.langchain.com/oss/python/integrations/document_loaders#by-category)

## Document Loaderの動作: 技術概要

### 標準インターフェース: `load()`と`lazy_load()`

すべてのLangChain互換Document loaderは`BaseLoader`クラスを拡張し、2つの主要なメソッドを提供する必要があります:

- **`load()`**  
    ソースからすべてのドキュメントを一度に読み込み、Documentオブジェクトのリストを返します。管理可能なデータセットまたはすべてのコンテンツが即座の処理に必要な場合に適しています。

    ```python
    documents = loader.load()
    ```

- **`lazy_load()`**  
    Documentオブジェクトを一度に1つずつ生成し、大きなファイルやディレクトリのコンテンツをストリーミングしてメモリオーバーロードを回避します。効率的なパイプライン処理と低いメモリフットプリントを可能にします。

    ```python
    for doc in loader.lazy_load():
        process(doc)
    ```

**技術的注意:**  
LangChainなどのフレームワークは、バッチおよびストリーミングワークフローを可能にするために、両方のメソッドを完全な互換性のために必要とします。カスタムLoaderは、最適な統合のために両方のメソッドが実装されていることを確認する必要があります。

**参考資料:**  
- [BaseLoaderインターフェース - LangChainドキュメント](https://docs.langchain.com/oss/python/integrations/document_loaders#interface)

### パラメータとカスタマイズ

各Loaderは、抽出を微調整するためのパラメータを提供します:

- **ファイルLoader:**  
    - `file_path` (文字列): ファイルの場所
    - `encoding` (文字列): ファイルエンコーディング、例: `"utf-8"`
    - `chunk_size` (整数): 大きなドキュメントを分割するサイズ
    - `metadata_columns` (リスト): メタデータとして含めるCSVの列またはJSONのフィールド

- **Web Loader:**  
    - `urls` (リストまたは文字列): 読み込むWebアドレス
    - `depth` (整数): 再帰的Loaderのクロール深度
    - `parsing_strategy` (文字列): パーサー選択(例: BeautifulSoup、Unstructured)
    - `filter_rules` (辞書): URLまたはコンテンツの包含/除外パターン

- **クラウドLoader:**  
    - `bucket_name` (文字列): ストレージバケット識別子
    - `authentication`: 認証情報またはトークン
    - `file_patterns` (文字列またはリスト): バッチファイル選択のためのGlobパターン

- **データベースLoader:**  
    - `connection_string` (文字列): データベースURI
    - `query` (文字列): レコードを抽出するためのSQLまたはNoSQLクエリ
    - `batch_size` (整数): 抽出中のメモリ使用量を制御

カスタムLoaderはさらにパラメータを追加する場合がありますが、すべてDocumentオブジェクトの`metadata`が包括的で一貫していることを確認する必要があります。

**参考資料:**  
- [LangChain Document Loaderリファレンス](https://docs.langchain.com/oss/python/integrations/document_loaders)

## 実用例

### PDFの読み込み

複数ページのPDFからテキストとメタデータを抽出:

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("example.pdf")
documents = loader.load()

print(documents[0].page_content)  # 最初のページのテキスト
print(documents[0].metadata)      # {'source': 'example.pdf', 'page': 1}
```

**パラメータ例:**  
- `file_path` (文字列): PDFファイルへのパス
- `strategy` (文字列、UnstructuredPDFLoaderの場合): 抽出モード、例: OCR対応抽出のための`"hi_res"`

**サンプル出力:**
```
Page content: "Introduction to Document Loaders ..."
Metadata: {'source': 'example.pdf', 'page': 1}
```

### CSVおよびテキストファイルの読み込み

**CSV例:**
```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="data.csv",
    csv_args={"delimiter": ",", "quotechar": '"'}
)
documents = loader.load()
print(documents[0].page_content)
print(documents[0].metadata)  # {'source': 'data.csv', 'row': 0}
```

**テキスト例:**
```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("notes.txt", encoding="utf-8")
documents = loader.load()
print(documents[0].metadata)  # {'source': 'notes.txt'}
```

### Webコンテンツの取り込み

WebページをDocumentオブジェクトに抽出および変換:

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com/article")
documents = loader.load()
print(documents[0].metadata)  # {'source': 'https://example.com/article'}
```

**サイトマップ例:**
```python
from langchain_community.document_loaders import SitemapLoader

loader = SitemapLoader("https://example.com/sitemap.xml")
documents = loader.load()
```

### データベースおよびクラウドLoader

**SQLデータベース例:**
```python
from langchain_community.document_loaders import SQLDatabaseLoader

loader = SQLDatabaseLoader(
    query="SELECT * FROM articles",
    db=database_connection
)
documents = loader.load()
```

**AWS S3例:**
```python
from langchain_community.document_loaders import S3DirectoryLoader

loader = S3DirectoryLoader("s3://my-bucket/documents/")
documents = loader.load()
```

**参考資料:**  
- [Document Loader: 公式例](https://docs.langchain.com/oss/python/integrations/document_loaders)

## ベストプラクティスと最適化

- **ソースデータの検証:**  
  実行時エラーを回避するために、読み込み前に破損、欠落、またはサポートされていないファイルをチェックします。

- **適切なLoaderの選択:**  
  最適な抽出品質とエラーの少なさのために、データタイプとソースに合わせたLoaderを使用します。

- **メタデータの保持:**  
  メタデータに明確な`source`識別子、ページまたは行番号、トレーサビリティと検索に必要なコンテキストが含まれていることを常に確認します。

- **大きなファイルのチャンク化:**  
  組み込みのチャンク化またはテキスト分割ユーティリティを使用して、大きなファイルを効率的に処理し、検索と埋め込みを最適化します。

- **バッチ処理:**  
  大きなディレクトリやデータセットの場合、メモリとリソース使用率を管理するためにファイルをバッチで処理します。

- **遅延読み込み:**  
  大規模なデータセットやファイルの場合、RAM使用量を最小限に抑え、ストリーミングパイプラインを可能にするために`lazy_load()`メソッドを使用します。

- **マルチスレッディング/マルチプロセッシング:**  
  大規模なクラウドバケットやディレクトリの場合、取り込みを加速するために並行性を活用します。

- **カスタムLoaderの開発:**  
  新しいLoaderを拡張または作成する場合、常に`load()`と`lazy_load()`の両方を実装し、互換性のためにDocument構造への厳格な準拠を維持します。

- **エラーハンドリング:**  
  抽出または接続の問題をキャッチするために堅牢なエラーハンドリングとロギングを組み込み、デバッグに十分なメタデータを持つ問題のあるファイルを報告します。

**参考資料:**  
- [LangChain Document Loader: ベストプラクティス (Medium)](https://medium.com/@ashutoshsharmaengg/feeding-your-llm-right-mastering-langchains-document-loaders-64ff06675c7b)
- [LangChain Document Loader - 公式ドキュメント](https://docs.langchain.com/oss/python/integrations/document_loaders)

## 一般的なユースケース

- **AIチャットボット:**  
  検索拡張LLMパイプラインのために内部ドキュメント、FAQ、ナレッジベースを取り込み、コンテキスト認識型の質問応答を実現します。

- **検索エンジン:**  
  高速、セマンティック、またはメタデータ駆動型の検索のために、企業ドキュメント、学術出版物、またはオンライン記事をインデックス化します。

- **エンタープライズ自動化:**  
  ワークフロー自動化、コンプライアンス、レポート作成のために、契約書、レポート、またはログから情報を抽出して構造化します。

- **学術研究:**  
  発見とレビューのために、科学論文、研究記事、またはデータリポジトリを集約して分析します。

- **要約と分析:**  
  自動要約、トレンド分析、または規制チェックのために大規模なコンテンツセットを読み込みます。

- **コンテンツモデレーション:**  
  自動レビュー、フィルタリング、またはコンプライアンス監視のために、チャットログ、ソーシャルメディア投稿、または電子メールを取り込みます。

**参考資料:**  
- [LangChain Document Loader - ユースケース](https://docs.langchain.com/oss/python/integrations/document_loaders)

## トラブルシューティングとFAQ

**Q: ファイルが読み込まれないのはなぜですか?**  
A: ファイルフォーマットがサポートされているか、パスまたはURLが有効か、必要なすべての依存関係(例: PDFの場合は`pypdf`)がインストールされているかを確認してください。

**Q: 非常に大きなファイルをどのように処理しますか?**  
A: 段階的な処理のために`lazy_load()`を使用し、埋め込みまたは検索の前にコンテンツをチャンクに分割します。

**Q: カスタムメタデータを追加できますか?**  
A: はい。ほとんどのLoaderは、パラメータを介して、またはサブクラス化してLoaderを拡張することで、追加のメタデータを注入できます。

**Q: カスタムLoaderを作成するにはどうすればよいですか?**  
A: `BaseLoader`クラスを拡張し、`load()`と`lazy_load()`を実装し、出力がDocumentオブジェクト構造に準拠していることを確認します。

**Q: ドキュメントに認証が必要な場合、またはプライベートにホストされている場合はどうすればよいですか?**  
A: クラウド固有のLoaderを使用し、適切な認証情報またはトークンで認証を構成します。

**Q: