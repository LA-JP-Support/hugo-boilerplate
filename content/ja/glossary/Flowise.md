---
title: Flowise
translationKey: flowise
description: Flowiseは、LangChainJSを使用してカスタムLLMフローとエージェント型AIシステムを構築するための、オープンソースのビジュアルプラットフォームです。最小限のコードで高度なAIワークフローを設計、オーケストレーション、デプロイできます。
keywords: ["Flowise", "LLMワークフロー", "AIエージェント", "LangChainJS", "オープンソース"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: フローワイズ
reading: Flowise
kana_head: その他
e-title: Flowise
---
## **Flowiseとは?**

Flowiseは、オープンソースの生成AI開発プラットフォームで、LangChainJSをコアオーケストレーターとして、AIエージェント、チャットボット、複雑なLLMワークフローを視覚的に構築することに特化しています。従来の自動化ツールとは異なり、Flowiseは高度なエージェントシステムのオーケストレーションを目的として設計されており、直感的なドラッグ&ドロップUIを通じて、シングルエージェントとマルチエージェントの両方のワークフローを実現します。

- **オープンソース:** Apache 2.0ライセンスにより、制限なくセルフホスティングとコミュニティ主導の機能強化が可能。
- **ビジュアルビルダー:** コードなしでLLMワークフロー、エージェント、パイプラインを視覚的に構成可能。
- **LangChainJSエコシステム:** LangChainJSとの深い統合により、メモリ、検索、埋め込み、複雑なエージェント動作のための強力なツールを提供。
- **3つのビジュアルビルダー:**
  - **Assistant:** 最もシンプルで、フォームベースの迅速なチャットボット作成。
  - **Chatflow:** シングルエージェント向けのノードベースで柔軟なLLMフロー。
  - **Agentflow:** 最も高度で、マルチエージェントオーケストレーション、分岐、ループ、状態管理をサポート。

**参考資料:**
- [FlowiseAI公式ドキュメント](https://docs.flowiseai.com)
- [Agentflow V2詳細](https://docs.flowiseai.com/using-flowise/agentflowv2)

## **主要機能と能力**

### **1. ビジュアルワークフロービルダー**

Flowiseは、LLM駆動のワークフローを構築するためのモジュール式ノードベースキャンバスを提供します:
- **ドラッグ&ドロップインターフェース:** LLM、リトリーバー、データベース、メモリ、ロジックを表すノードを接続してフローを構築。
- **再利用可能なテンプレート:** 事前構築されたテンプレートとコミュニティ提供のフローのマーケットプレイス/ライブラリにアクセス。
- **Assistant、Chatflow、Agentflow:** 初心者向け、シングルエージェント、または高度なマルチエージェントオーケストレーションビルダーから選択。

**参考資料:**
- [ビジュアルビルダー概要](https://docs.flowiseai.com)

### **2. マルチエージェントオーケストレーション**

**Agentflow**はマルチエージェントシステムの設計をサポートします:
- **明示的なワークフローオーケストレーション:** 各ノードが個別の操作を実行し、接続がフローの制御とデータシーケンスを定義。
- **エージェント間通信:** スーパーバイザーエージェントがワーカーにタスクを委任し、結果を集約し、状態を管理。すべてのエージェントが会話履歴と共有フロー状態にアクセス。
- **ループ、分岐、Human-in-the-Loop:** 条件付きロジック、反復ループ、ワークフローの任意の段階での人間の承認またはレビューのための一時停止をサポート。
- **ステートフル、長時間実行エージェント:** 永続的で回復力のあるワークフローのためのチェックポイントと再開ロジック。

**参考資料:**
- [Agentflow V2アーキテクチャ](https://docs.flowiseai.com/using-flowise/agentflowv2#core-concept)

### **3. チャットアシスタント&シングルエージェントフロー**

- **Chatflow:** シングルエージェントボット、RAG(検索拡張生成)チャットボット、シンプルなLLM駆動アプリケーションを構築するための柔軟なキャンバス。
- **Assistant:** フォームによる迅速なセットアップ。ナレッジベース、ファイル、ツールを会話型ボットに添付。
- **高度なRAG:** リトリーバー、リランカー、グラフベース検索などのツールを組み込み、カスタムデータに対する高精度Q&Aを実現。

**参考資料:**
- [AssistantとChatflowドキュメント](https://docs.flowiseai.com#assistant)

### **4. データ接続性と統合**

- **100以上のデータフォーマットをサポート:** TXT、PDF、DOCX、HTML、CSV、MD、JSON、XML、SQLなど。
- **ベクトルデータベース統合:** Pinecone、ChromaDB、[Weaviate](/ja/glossary/weaviate/)、Milvusなどの組み込みサポート。
- **API、SDK、埋め込み:** REST API、Python/Typescript SDK、またはWebに埋め込み可能なチャットウィジェットを介してフローを公開。

**参考資料:**
- [Flowiseデータ統合](https://docs.flowiseai.com)

### **5. 可観測性とモニタリング**

- **実行トレース:** デバッグと最適化のためのステップバイステップの実行とデータフローの可視化。
- **分析とメトリクス:** パフォーマンス、トークン使用量、コスト、その他のメトリクスを追跡。
- **外部モニタリング:** PrometheusやOpenTelemetryなどの可観測性プラットフォームとの統合。

### **6. Human-in-the-Loop (HITL)**

- **タスクレビュー:** 人間の入力、レビュー、または承認のために実行を一時停止するチェックポイントを挿入。これらはステートフルで、アプリケーションの再起動後も存続可能。
- **権限制御:** 自律システムにおける人間の監督と同様に、機密性の高いアクションを実行する前に人間の承認を要求。

### **7. セキュリティとエンタープライズ対応**

- **RBACとSSO:** きめ細かいロールベースアクセス制御、エンタープライズデプロイメント向けシングルサインオン。
- **認証情報管理:** APIキーと[シークレット](/ja/glossary/environment-variables--secrets-/)の暗号化ストレージ。
- **水平スケーラビリティ:** クラスターまたはクラウド環境全体でフローをスケーリングするためのメッセージキューとワーカーベースアーキテクチャ。

### **8. 拡張性**

- **カスタムノード:** 独自のロジック、モデル、または統合を実装して追加。
- **マーケットプレイス/コミュニティコンポーネント:** ノードとフローテンプレートを共有および再利用。

**参考資料:**
- [マーケットプレイスと拡張性](https://cloud.flowiseai.com/marketplace)

## **Flowiseの使用方法**

### **AIエージェントを視覚的に構築**

ユーザーはモジュール式ノードを視覚的にリンクすることで、LLM駆動のワークフローを構築します:
- **ノーコード/ローコード:** フローを視覚的に構築し、モデル、メモリ、ツール、ロジックのノードを設定。
- **シンプルから高度へスケール:** チャットボットの迅速なプロトタイピングから、マルチエージェントまたは自律オーケストレーションへの拡張。

#### **RAG(検索拡張生成)統合**
- **カスタムデータの取り込み:** PDF、DOCX、またはWebサイトのデータソースノードをドラッグ。
- **インデックスと検索:** 効率的な検索のためにベクトルデータベースノードに接続。
- **LLMノード:** 生成のためにGPT-4、Claude、またはローカルモデルノードを添付。
- **メモリノード:** マルチターン会話のためのコンテキスト保持を追加。

#### **ワークフロー作成手順**

1. **Flowiseをインストール:**
   ```bash
   npm install -g flowise
   npx flowise start
   ```
   - または[Flowise Cloud](https://cloud.flowiseai.com/signin)に登録。

2. **新しいフローを作成:**
   - `http://localhost:3000`またはクラウドでダッシュボードにアクセス。
   - Assistant、Chatflow、またはAgentflowを選択。
   - ノードをドラッグして接続し、ワークフローロジックを定義。

3. **ノードを設定:**
   - LLM(OpenAI、Ollamaなど)をセットアップ。
   - リトリーバー、データベース、メモリを統合。
   - 高度なプロンプトとfew-shotテンプレートを使用。

4. **テストとデバッグ:**
   - 組み込みチャットウィンドウでライブテスト。
   - 実行をトレースし、出力を検査し、パフォーマンスをプロファイル。

5. **デプロイ:**
   - REST API、SDK、チャットウィジェットの埋め込み、または公開URLで共有。

**参考資料:**
- [公式スタートガイド](https://docs.flowiseai.com/getting-started)
- [YouTube: 10分でAIチャットボットを構築](https://www.youtube.com/watch?v=riXpu1tHzl0)

## **ユースケースと実例**

### **エンタープライズチャットボット&アシスタント**

- **カスタマーサポート:** FAQ応答の自動化、チケット解決、複雑な問題のエスカレーション。
- **社内ナレッジベース:** 従業員が会話型インターフェースを介して会社のポリシー、技術文書、SOPを検索。

### **マルチエージェントAIシステム**

- **リサーチチーム:** スーパーバイザーエージェントが情報収集を複数のワーカーに委任し、各ワーカーがソースまたは分析に特化。
- **AIチーム:** エージェント階層全体で検索、要約、分析、レポート作成をオーケストレート。

### **SaaS製品への埋め込みAI**

- **InsightSoftware:** AI駆動の会話型インサイトで埋め込み分析を強化。
- **UneeQ Digital Humans:** 高度な[会話型AI](/ja/glossary/conversational-ai/)を備えたデジタルアバターの展開を効率化。

### **カスタム統合と自動化**

- **プロジェクト管理:** LLM駆動ボットを使用してSlackから直接Notionタスクを自動作成。
- **マルチモーダルチャットボット:** 単一の会話フローでテキストと画像処理を融合。

### **教育とパーソナライゼーション**

- **ペルソナボット:** 特定の教育またはメンタリングスタイルをエミュレート。
- **翻訳と多言語ボット:** 迅速な言語適応のための[プロンプトテンプレート](/ja/glossary/prompt-template/)を備えたLLMをデプロイ。

### **開発者プロトタイピングとコミュニティ**

- **迅速なプロトタイピング:** ハッカソン、デモ、本番パイロット向けのドラッグ&ドロップエージェント作成。
- **オープンソースコラボレーション:** フローの共有とトラブルシューティングのための活発なGitHubとDiscordコミュニティ。

**参考資料:**
- [Flowise実例](https://cobusgreyling.medium.com/flowise-for-langchain-b7c4023ffa71)

## **主な利点: Flowiseを使用する理由**

| 機能 | Flowiseの利点 |
|-----|-------------|
| オープンソース | 完全な透明性、ベンダーロックインなし、セルフホスティング |
| ビジュアル開発 | ドラッグ&ドロップインターフェースで開発時間を短縮 |
| モジュール式で柔軟 | チャットボットからマルチエージェントチームまで、あらゆるLLMワークフローを構成 |
| LLM非依存 | ローカルを含む100以上のサポートされたモデルとベクトルDB |
| コミュニティ主導 | 活発なDiscord、GitHub、フローとノードのマーケットプレイス |
| エンタープライズ対応 | RBAC、SSO、暗号化[シークレット](/ja/glossary/environment-variables--secrets-/)、スケーラブル、オンプレミス/クラウド |
| 拡張可能 | カスタムノード、統合、再利用可能なテンプレート |
| 可観測性 | トレース、分析、モニタリングサポート |
| Human in the Loop | ワークフローに組み込まれた人間のレビュー/承認 |
| 簡単なデプロイメント | API、SDK、埋め込みウィジェット、公開URL |

**参考資料:**
- [Flowise機能マトリックス](https://docs.flowiseai.com)

## **技術アーキテクチャと統合**

### **ビジュアルビルダー**

- **Assistant:** 最も簡単で、フォームベース、迅速なチャットボット作成。
- **Chatflow:** ノードベース、シングルエージェントシステム向けの柔軟なフロー。
- **Agentflow (V2):** 高度なオーケストレーション、明示的なワークフロー設計、マルチエージェントコラボレーション、ループ、分岐、human-in-the-loopをサポート。

**参考資料:**
- [Agentflow V2詳細](https://docs.flowiseai.com/using-flowise/agentflowv2#core-concept)

### **サポートされるデータフォーマット**

- **テキスト:** TXT、PDF、DOCX、HTML、MD、CSV、JSON、XML、SQL。
- **マルチメディア:** マルチモーダルフロー用の画像ノード。

### **LLM、ツール、メモリ統合**

- **LLM:** OpenAI(GPT-3/4)、Ollama(ローカルモデル)、Claude、Llama2など。
- **ベクトルDB:** Pinecone、ChromaDB、[Weaviate](/ja/glossary/weaviate/)、Milvusなど。
- **メモリ:** 会話コンテキスト用のバッファ、ウィンドウ、要約、カスタム実装。
- **API/SDK:** REST、Python、Typescript。カスタムツール統合が可能。

### **セキュリティとスケーラビリティ**

- **RBAC/SSO:** エンタープライズグレードのアクセス制御。
- **暗号化認証情報:** 安全なAPIキーとシークレットストレージ。
- **水平スケーリング:** 分散デプロイメント用のメッセージキューとワーカーモデル。

**参考資料:**
- [セキュリティとスケーラビリティドキュメント](https://docs.flowiseai.com)

## **はじめに: インストールと最初のステップ**

### **インストール**

- **ローカル/セルフホスト:**
  ```bash
  npm install -g flowise
  npx flowise start
  ```
  - Node.jsが必要。ダッシュボードは`http://localhost:3000`。

- **クラウド版:**
  - 即座のセットアップのために[Flowise Cloudに登録](https://cloud.flowiseai.com/signin)。

### **最初のフロー**

- **Assistant:** フォームに記入し、シンプルなチャットボット用のツールとファイルを添付。
- **Chatflow/Agentflow:** キャンバスを使用してノードベースのフローを構築し、LLM、リトリーバー、メモリ、ツールを接続。
- **テストとデバッグ:** 統合チャットウィンドウと実行トレースを使用。

### **デプロイメント**

- **埋め込み:** サイトにチャットウィジェットを追加。
- **API/SDK:** REST、Python、またはTypescript SDKと統合。
- **公開リンク:** URLでボットを共有。

### **コミュニティとサポート**

- **ドキュメント:** [https://docs.flowiseai.com](https://docs.flowiseai.com)
- **GitHub:** [https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- **Discord:** [https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW)
- **YouTubeチュートリアル:** [完全なFlowise v3チュートリアル](https://www.youtube.com/watch?v=riXpu1tHzl0)

## **用語集: 関連用語**

- **LLM(大規模言語モデル):** 膨大なテキストデータで訓練された深層ニューラルネットワークで、人間の言語の生成と理解を可能にする。
- **RAG(検索拡張生成):** 外部ソースから関連コンテキストを検索して出力精度を向上させるLLM技術。
- **エージェントシステム:** タスクを解決するために協力または競合する複数の自律AIエージェントを持つアーキテクチャ。
- **ベクトルデータベース:** 埋め込みの高速類似性検索のための特殊なデータストア(例: Pinecone、ChromaDB)。
- **Human-in-the-Loop (HITL):** 人間が自動化されたAI出力をレビュー、承認、または修正するシステム設計パターン。
- **チャットウィンドウ:** Flowiseでボットと対話し、フローをテストするためのUIコンポーネント。
- **API/SDK:** Flowiseボットを外部アプリケーションに統合するための開発者ツール。
- **Few-shot学習:** プロンプト内の少数の入出力例でLLMをガイドする方法。
- **オープンソース:** 公開され、変更可能なソースコードを持つソフトウェアで、コミュニティの貢献を促進。

**拡張用語集:**
- [包括的LLM用語集](https://main--dasarpai.netlify.app/dsblog/Comprehensive-Glossary-of-LLM/#what-is-flowiseai)

## **リンク、コミュニティ、その他のリソース**

- **公式ウェブサイト:** [https://flowiseai.com](https://flowiseai.com/)
- **ドキュメント:** [https://docs.flowiseai.com](https://docs.flowiseai.com)
- **GitHubリポジトリ:** [https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- **YouTubeチュートリアル:** [AIドキュメントチャットボットの構築方法](https://www.youtube.com/watch?v=riXpu1tHzl0)
- **Discordコミュニティ:** [https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW)
- **マーケットプレイス:** [Flowiseコミュニティフローとテンプレート](https://cloud.flowiseai.com/marketplace)
- **サードパーティ用語集:** [包括的LLM用語集](https://main--dasarpai.netlify.app/dsblog/Comprehensive-Glossary-of-LLM/#what-is-flowiseai)

## **よくある質問**

### **Flowiseはn8n、Zapier、Make.comとどう違うのですか?**
Flowiseはエージェント型AIワークフローに特化しており、LLMオーケストレーション、マルチエージェントコラボレーション、RAG、メモリのネイティブサポートを提供します。これらは汎用自動化プラットフォームには存在しない機能です。Flowiseはオープンソースで、セルフホスト可能で、高度なAI/LLMユースケース向けに設計されています。

### **カスタムLLMとデータを使用できますか?**
はい。Flowiseは100以上のLLM(Ollama経由のローカルモデルやオープンソースオプションを含む)をサポートし、RAGベースのフロー用のすべての一般的なデータフォーマットの取り込みをサポートしています。

### **Flowiseはエンタープライズ対応ですか?**
はい。RBAC、SSO、暗号化認証情報管理、水平スケーラビリティ、オンプレミスとクラウドの両方のデプロイメントをサポートしています。

### **どのように貢献またはサポートを受けられますか?**
[Discordコミュニティ](https://discord.gg/jbaHfsRVBW)に参加し、[GitHub](https://github.com/FlowiseAI/Flowise)でPRや問題を提出し、[ドキュメント](https://docs.flowiseai.com)でオンボーディングガイドにアクセスしてください。

## **ユーザーの声**

> "Flowiseにより、既存の埋め込み分析プラットフォームに組み込みAI機能を追加し、クライアントに絶対的に愛されています。"
> — Terrence Sheflin、エンジニアリングディレクター、InsightSoftware

> "Flowiseのおかげで、社内の「独自のAIアシスタントを簡単かつ直感的に構築」イニシアチブを加速できました。私たちの技術の旅における真のゲームチェンジャーです。"
> — Iokin Pardo、シニアディレクター、BTS Digital

> "FlowiseはAIへのアプローチ方法を本当に変えました。数分でアイデアをプロトタイプ化できるほどシンプルでありながら、本番環境まで持っていけるほど強力です。"
> — David Micotto、DX & AIシニアディレクター、Publicis Groupe

## **Flowiseを始めましょう**

- **構築を開始:** [無料でサインアップ](https://cloud.flowiseai.com/signin)または[ローカルにインストール](https://docs.flowiseai.com/getting-started)。
- **コミュニティに参加:** [Discord](https://discord.gg/jbaHfsRVBW)
- **コードを探索:** [GitHub](https://github.com/FlowiseAI/Flowise)
- **チュートリアルを視聴:** [YouTube](https://www.youtube.com/watch?v=ri