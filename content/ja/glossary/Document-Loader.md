---
title: ドキュメントローダー
translationKey: document-loader
description: ドキュメントローダーは、生データを自動的に取り込み、LLMパイプラインやベクトルストアのインデックス化などのAIタスク向けに構造化されたDocumentオブジェクトに変換するソフトウェアモジュールです。
keywords:
- Document Loader
- AIパイプライン
- LLM
- データ取り込み
- LangChain
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: Document Loader
term: どきゅめんとろーだー
url: "/ja/glossary/Document-Loader/"
---
## ドキュメントローダーとは?
ドキュメントローダーは、ファイル、Webページ、クラウドドキュメント、データベースエントリなどの生データの取り込みと変換を自動化するソフトウェアモジュールです。これらのデータをDocument オブジェクトと呼ばれる構造化された形式に変換します。このオブジェクトは、情報検索、LLM(大規模言語モデル)パイプライン、ベクトルストアのインデックス化、ワークフロー自動化などの下流AIタスクに最適化されています。

ドキュメントローダーは、多様な非構造化または半構造化コンテンツソースの処理の複雑さを抽象化します。意味のあるテキストを解析・抽出し、コンテキストメタデータで強化し、元のファイルタイプやデータソースに関係なく、標準化された一貫性のある構造を出力します。この統一性は、AIチャットボット、検索エンジン、データ分析パイプラインなど、予測可能で豊富な入力データを必要とするアプリケーションにとって重要です。

ドキュメントローダーは、生の多様なデータソースと標準化された入力を必要とするAIシステムの間の橋渡しとして機能します。データの抽出、変換、強化という重労働を処理することで、開発者は各データソースに対してカスタム解析コードを書くのではなく、AIアプリケーションの構築に集中できます。

## ドキュメントローダーを使用する理由

<strong>標準化</strong>- 無数の形式、エンコーディング、レイアウトからデータを統一
- PDF、HTML、CSV、JSONを一貫したスキーマに変換
- 各ソースに対するカスタム解析ロジックを排除

<strong>自動化</strong>- 定型的な抽出・解析スクリプトを排除
- 再利用可能で十分にテストされたツールを提供
- 開発オーバーヘッドとメンテナンスを最小化

<strong>コンテキストの保持</strong>- 重要なメタデータ(ソースの場所、ページ番号、タイムスタンプ)を付加
- トレーサビリティ、コンプライアンス、きめ細かい検索を可能に
- コンテンツとその起源の関係を保持

<strong>スケーラビリティ</strong>- 大規模な取り込みシナリオに対応
- バッチ処理とストリーミングをサポート
- 遅延読み込みによるパフォーマンスとメモリ効率の最適化

<strong>プラグアンドプレイ統合</strong>- LangChainなどのフレームワークとシームレスに連携
- ベクトルデータベース用の標準インターフェースを提供
- AIパイプライン全体での接続性を確保

## Documentオブジェクトの構造

ドキュメントローダーがデータソースを処理すると、Documentオブジェクトを生成します。これは、LLMパイプライン、ベクトルストアの取り込み、RAGシステムの基本単位です。

<strong>コアフィールド:</strong>

<strong>page_content(文字列)</strong>- ソースから抽出された主要なテキストまたはコンテンツ
- 下流タスク用にクリーニング、デコード、前処理済み
- 例:PDFページのテキスト、CSVの行データ、HTMLの段落コンテンツ

<strong>metadata(辞書)</strong>- コンテキスト、説明、ソース関連のキーと値のペア
- 一般的なフィールド:source、page、row、title、filetype、created_at、last_modified、category、section
- 検索とフィルタリングに必要な情報でコンテンツを強化

<strong>id(オプションの文字列)</strong>- ドキュメントの一意の識別子
- 重複排除、相互参照、データベースインデックス化に不可欠

<strong>Pythonでの例:</strong>```python
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

## ドキュメントローダーの種類

### ファイルタイプ別

**PDFローダー**- PDFファイルからテキストとメタデータを抽出
- 複数ページのレイアウトとスキャン画像(OCR使用)に対応
- 参照用にページ番号を保持
- 例:PyPDFLoader、PDFPlumberLoader、UnstructuredPDFLoader

**テキストファイルローダー**- プレーンテキスト形式(.txt、.md、.log)を処理
- ファイル全体を抽出、または行/セクションで分割
- 例:TextLoader

**CSVローダー**- 行または列を個別のドキュメントとして抽出
- ソース、行インデックス、選択された列のメタデータを含む
- 例:CSVLoader

**JSONローダー**- 構造化またはネストされたデータを処理
- 必要に応じてフィールドをフラット化または抽出

**MS Officeローダー**- .docx、.xlsx、.pptxファイルをサポート
- 段落、表、スライド、セルを抽出

**HTML/Markdownローダー**- Webページ、ドキュメント、Wikiを解析
- 読みやすいテキストを抽出し、構造メタデータを保持

### データソース別

**ローカルファイルシステムローダー**- ファイルパスまたはディレクトリパターンを使用してディスクからファイルを読み込み

**Web URLローダー**- Webページからコンテンツをスクレイピングまたはダウンロード
- 例:WebBaseLoader、SitemapLoader、RecursiveURLLoader

**クラウドストレージローダー**- AWS S3、Azure Blob、Google Driveからドキュメントを取得
- 例:S3DirectoryLoader

**API・サードパーティプラットフォーム**- YouTube、Wikipedia、Notion、Slack、GitHubなどのサービスからデータを取り込み

**データベースローダー**- SQLまたはNoSQLデータベースから行またはレコードを抽出

### 特殊なローダー

**DirectoryLoader:**パターンに一致するすべてのファイルをディレクトリから再帰的に読み込み

**再帰ローダー:**深いフォルダ構造を走査、またはWebサイト全体をクロール

**カスタムローダー:**独自または一般的でないデータソース用の拡張可能な基底クラス

## 標準インターフェース

すべてのLangChain互換ドキュメントローダーは`BaseLoader`クラスを拡張し、2つの主要なメソッドを提供します:

**load()**- ソースからすべてのドキュメントを一度に読み込み
- Documentオブジェクトのリストを返す
- 管理可能なデータセットまたは即時処理のニーズに適している

```python
documents = loader.load()
```

**lazy_load()**- Documentオブジェクトを一度に1つずつ生成
- 大きなファイルやディレクトリのコンテンツをストリーミング
- メモリオーバーロードを回避し、効率的なパイプライン処理を可能に

```python
for doc in loader.lazy_load():
    process(doc)
```

LangChainなどのフレームワークは、完全な互換性のために両方のメソッドを必要とし、バッチとストリーミングのワークフローを可能にします。カスタムローダーは、最適な統合のために両方を実装する必要があります。

## パラメータとカスタマイズ

**ファイルローダー:**- `file_path`: ファイルの場所
- `encoding`: ファイルエンコーディング(例:「utf-8」)
- `chunk_size`: 大きなドキュメントを分割するサイズ
- `metadata_columns`: メタデータとして含める列またはフィールド

**Webローダー:**- `urls`: 読み込むWebアドレス
- `depth`: 再帰ローダーのクロール深度
- `parsing_strategy`: パーサーの選択(BeautifulSoup、Unstructured)
- `filter_rules`: URLまたはコンテンツの包含/除外パターン

**クラウドローダー:**- `bucket_name`: ストレージバケット識別子
- `authentication`: 認証情報またはトークン
- `file_patterns`: バッチファイル選択用のGlobパターン

**データベースローダー:**- `connection_string`: データベースURI
- `query`: レコードを抽出するSQLまたはNoSQLクエリ
- `batch_size`: 抽出中のメモリ使用量を制御

## 実用例

### PDFの読み込み
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("example.pdf")
documents = loader.load()

print(documents[0].page_content)  # 最初のページのテキスト
print(documents[0].metadata)      # {'source': 'example.pdf', 'page': 1}
```

### CSVファイルの読み込み
```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="data.csv",
    csv_args={"delimiter": ",", "quotechar": '"'}
)
documents = loader.load()
```

### Webコンテンツの取り込み
```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com/article")
documents = loader.load()
```

### データベースローダー
```python
from langchain_community.document_loaders import SQLDatabaseLoader

loader = SQLDatabaseLoader(
    query="SELECT * FROM articles",
    db=database_connection
)
documents = loader.load()
```

### クラウドストレージ
```python
from langchain_community.document_loaders import S3DirectoryLoader

loader = S3DirectoryLoader("s3://my-bucket/documents/")
documents = loader.load()
```

## ベストプラクティス

**ソースデータの検証**- 読み込み前に破損、欠落、サポートされていないファイルをチェック
- 早期に問題を検出するためのエラーハンドリングを実装

**ローダーの選択**- データタイプとソースに合わせたローダーを使用
- 抽出品質を最適化し、エラーを最小化

**メタデータの保持**- メタデータに明確なソース識別子を含める
- トレーサビリティのためにページまたは行番号を含める
- 検索と取得に必要なコンテキストを追加

**ファイルのチャンク化**- 大きなファイルには組み込みのチャンク化を使用
- 検索と埋め込みプロセスを最適化
- チャンクサイズとコンテキスト保持のバランスを取る

**バッチ処理**- 大きなディレクトリのファイルをバッチで処理
- メモリとリソース使用率を効果的に管理

**遅延読み込み**- 大規模データセットには`lazy_load()`を使用
- ストリーミングパイプラインでRAM使用量を最小化
- 段階的な処理を可能に

**並行処理**- 大規模取り込みにはマルチスレッド/マルチプロセッシングを活用
- クラウドバケットやディレクトリの処理を高速化

**カスタム開発**- ローダーを拡張する際は`load()`と`lazy_load()`の両方を実装
- Document構造への厳密な準拠を維持
- 既存のフレームワークとの互換性を確保

**エラーハンドリング**- 堅牢なエラーハンドリングとロギングを組み込む
- 抽出または接続の問題を捕捉
- 十分なメタデータで問題のあるファイルを報告

## 一般的なユースケース

**AIチャットボット**- 社内ドキュメント、FAQ、ナレッジベースを取り込み
- 検索拡張LLMパイプラインを強化
- コンテキストを考慮した質問応答を可能に

**検索エンジン**- 企業ドキュメントと出版物をインデックス化
- 高速でセマンティックまたはメタデータ駆動の検索を可能に
- 高度な検索機能をサポート

**エンタープライズ自動化**- 契約書やレポートから情報を抽出・構造化
- ワークフロー自動化とコンプライアンスチェックを可能に
- 自動レポート作成と分析をサポート

**学術研究**- 科学論文を集約・分析
- 研究論文とデータリポジトリを処理
- 発見と系統的レビューを可能に

**要約と分析**- 自動要約のために大量のコンテンツセットを読み込み
- トレンド分析と規制チェックを実行
- コンプライアンス監視をサポート

**コンテンツモデレーション**- チャットログ、ソーシャルメディア投稿、メールを取り込み
- 自動レビューとフィルタリングを可能に
- コンプライアンス監視をサポート

## トラブルシューティング

**ファイルが読み込まれない**- ファイル形式がサポートされているか確認
- パスまたはURLの有効性をチェック
- 必要な依存関係がインストールされているか確認

**大きなファイルの処理**- 段階的な処理には`lazy_load()`を使用
- 埋め込み前にコンテンツをチャンクに分割
- ストリーミングワークフローを実装

**カスタムメタデータ**- ローダーパラメータを介して追加のメタデータを注入
- サブクラス化によってローダーを拡張
- ドキュメント間でメタデータの一貫性を確保

**カスタムローダーの作成**- `BaseLoader`クラスを拡張
- `load()`と`lazy_load()`の両方を実装
- 出力がDocumentオブジェクト構造に準拠していることを確認

**認証**- 適切な認証情報を持つクラウド固有のローダーを使用
- 認証トークンまたはAPIキーを設定
- 安全な認証情報管理を実装

## 参考文献


1. Latenode. (2025). LangChain Document Loaders: Complete Guide to Loading Files + Code Examples. Latenode Blog.

2. Sharma, A. (n.d.). Feeding Your LLM Right: Mastering LangChain's Document Loaders. Medium.

3. LangChain. (n.d.). LangChain Document Loaders. Official Documentation.

4. LangChain. (n.d.). PyPDFLoader. Official Documentation.

5. LangChain. (n.d.). PDFPlumberLoader. Official Documentation.

6. LangChain. (n.d.). UnstructuredPDFLoader. Official Documentation.

7. LangChain. (n.d.). TextLoader. Official Documentation.

8. LangChain. (n.d.). CSVLoader. Official Documentation.

9. LangChain. (n.d.). WebBaseLoader. Official Documentation.

10. LangChain. (n.d.). SitemapLoader. Official Documentation.

11. LangChain. (n.d.). RecursiveURLLoader. Official Documentation.

12. LangChain. (n.d.). S3DirectoryLoader. Official Documentation.
