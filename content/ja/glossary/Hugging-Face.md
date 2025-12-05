---
title: Hugging Face
date: 2025-11-25
translationKey: hugging-face
description: Hugging Faceは、機械学習を民主化するオープンソースAIプラットフォームおよびグローバルコミュニティです。自然言語処理、コンピュータビジョンなどのモデル、データセット、ツールをご紹介します。
keywords:
- Hugging Faceモデル
- 大規模言語モデル
- Transformersライブラリ
- モデルハブ
- Hugging Faceデータセット
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Hugging Face
term: ハギング フェイス
reading: Hugging Face
kana_head: その他
---
## Hugging Faceとは?

Hugging Faceは、機械学習と人工知能の民主化に焦点を当てたオープンソースAIプラットフォームおよびグローバルコミュニティです。[自然言語処理(NLP)](/en/glossary/natural-language-processing--nlp-/)、コンピュータビジョン、音声、マルチモーダルAIなどの領域にわたって、機械学習モデル、データセット、アプリケーションの共有、発見、デプロイのための統合エコシステムを提供しています。

- **ミッション:** AIをすべての人にアクセス可能で透明性のあるものにする。
- **アプローチ:** オープンソースライブラリ、協調的なモデルとデータセットの共有、シームレスなデプロイツール。
- **影響:** Hugging Faceは数百万人のユーザーをサポートし、200万以上のモデル、50万以上のデータセット、100万以上のデモアプリケーション(「Spaces」)を提供しています。これらのリソースは、研究者、開発者、企業が最先端のAIソリューションを構築・デプロイし、イノベーションと責任あるAI開発を加速させることを支援しています。

Hugging Faceは「AI版GitHub」として機能し、誰でも協力、貢献、または事前学習済みモデルとデータを活用して高度なAIアプリケーションを構築できます。

- [Hugging Face公式サイト](https://huggingface.co/)

## コア用語集

この用語集は、Hugging Faceのコア概念、モデルとデータサイエンスの用語、オープンソースAI技術に関する権威ある定義と背景を提供します。

**完全な公式用語集については、以下を参照してください:**  
- [Transformers用語集](https://huggingface.co/docs/transformers/en/glossary)

### モデル
テキスト分類、画像認識、音声テキスト変換などの特定のタスクを実行するように訓練された機械学習成果物。Hugging Faceのモデルは、事前学習済み(公開データで訓練)または微調整済み(特定のデータセットやタスクに適応)の場合があります。

### Model Hub
機械学習モデルの保存、共有、発見のためのHugging Faceの集中リポジトリ。Model Hubは[モデルカード](/en/glossary/model-cards/)(ドキュメント)、バージョン管理、ライブデモ、主要なMLライブラリとの統合をサポートしています。

- [Model Hubドキュメント](https://huggingface.co/docs/hub/en/models-the-hub)

### データセット
機械学習モデルの訓練、評価、ベンチマークのためのデータサンプル(テキスト、画像、音声など)の構造化されたコレクション。

### Datasets Hub
キュレーションされたデータセットのリポジトリで、データセットカード(ドキュメント)、バージョン管理、メタデータ、Datasetsライブラリを介したプログラマティックアクセスを提供します。

- [Datasets Hubドキュメント](https://huggingface.co/docs/hub/en/datasets-overview)

### Transformers
「Attention is All You Need」論文(Vaswani et al., 2017)で導入された、自己注意機構に基づくニューラルネットワークアーキテクチャ。NLPで広く使用され、ビジョン、音声、マルチモーダルタスクでも増加しています。

### Transformersライブラリ
Hugging Faceが開発したPythonライブラリで、トランスフォーマーベースのモデル(BERT、GPT、T5など)への簡単なアクセス、トークン化、訓練、推論のためのユーティリティを提供します。

- [Transformersライブラリドキュメント](https://huggingface.co/docs/transformers/en/index)

### トークナイザー
生の入力(例:テキスト)をモデル処理用のトークン(サブワード単位)に変換し、モデル出力を人間が読める形式にデコードするユーティリティ。

### 微調整
事前学習済みモデルを特定のデータセットやタスクに適応させるプロセスで、通常は追加の訓練を伴います。

### Inference Provider
スケーラブルでサーバーレスな方法でモデルを提供するために、Hugging Faceと統合されたクラウドインフラストラクチャまたはマネージドサービス。

- [Inference Providersドキュメント](https://huggingface.co/docs/hub/en/models-inference)

### Space
Hugging Faceでホストされるウェブアプリケーションで、通常はインタラクティブなデモ、プロトタイプ、ML駆動アプリケーションに使用されます。SpacesはGradio、Streamlit、カスタムフレームワークをサポートしています。

- [Spaces概要](https://huggingface.co/docs/hub/en/spaces-overview)

### モデルカード
モデルの意図された用途、訓練データ、制限事項、倫理的考慮事項、ライセンスを記述する標準化されたドキュメントファイル。

- [モデルカード](https://huggingface.co/docs/hub/en/model-cards)

### データセットカード
モデルカードと同様ですが、データセット用です。データセットのソース、構造、意図された用途、倫理的考慮事項を記述します。

- [データセットカード](https://huggingface.co/docs/hub/en/datasets-cards)

### LLM(大規模言語モデル)
数億から数十億のパラメータを持つトランスフォーマーベースのモデルで、高度なテキスト生成、理解、翻訳、推論が可能です。

### ZeroGPU
ユーザーが専用GPUインスタンスを設定または支払う必要なく、SpacesでGPUアクセスを可能にする機能。

### コミット履歴/バージョン管理
モデル、データセット、コードリポジトリの時間経過に伴う変更を追跡し、再現性とコラボレーションをサポートします。

### ゲート付きモデル/データセット
コンプライアンスやライセンスの理由で、作成者による明示的なアクセス承認を必要とするリソース。

## コアプラットフォームコンポーネント

### Model Hub

Model Hubは、機械学習モデルの共有、発見、使用のためのHugging Faceの中心的なプラットフォームです。高品質なモデルをすべての人にアクセス可能にし、研究、開発、本番デプロイを加速させるように設計されています。

**主な機能:**
- タスク(例:テキスト生成、分類)、アーキテクチャ(例:BERT、GPT)、データセット、言語でモデルを検索・フィルタリング。
- モデルカード:意図された用途、訓練データ、制限事項、バイアス、ライセンスをカバーする豊富なドキュメント。
- バージョン管理:すべてのモデル更新が追跡され、再現性、ロールバック、コラボレーションをサポート。
- Transformers、PyTorch、TensorFlow、Flax、JAXを含む主要な機械学習ライブラリとの統合。
- インタラクティブな推論とライブデモのためのブラウザ内モデルウィジェット。
- エコシステムの洞察のためのダウンロード統計、タグ、メタデータ。

**メリット:**
- 事前学習済みモデルを活用することで、ゼロからの訓練の必要性を削減。
- プロトタイピングと本番デプロイを加速。
- 透明性のあるドキュメントを通じて責任ある倫理的なAIを促進。

**人気のモデル例:**
- BERT、RoBERTa、GPT-2、GPT-3、GPT-4(NLP)
- Stable Diffusion、DeepSeek、Z-Image-Turbo(ビジョン/マルチモーダル)
- Whisper(音声)
- ドメイン固有のLLM(法律、生物医学、コード)

**Model Hubを閲覧:**  
- [https://huggingface.co/models](https://huggingface.co/models)

**モデルのアップロードと共有:**  
- [モデルアップロードガイド](https://huggingface.co/docs/hub/en/models-uploading)
- [モデルリリースチェックリスト](https://huggingface.co/docs/hub/en/model-release-checklist)

**モデルのダウンロードと使用:**  
- [モデルダウンロードガイド](https://huggingface.co/docs/hub/en/models-downloading)
- 例:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
```

**モデルウィジェット:**  
ウェブページにモデルデモを埋め込むか、Spacesでウィジェットを使用して即座にテストします。

- [モデルウィジェットドキュメント](https://huggingface.co/docs/hub/en/models-widgets)

### Datasets Hub

Datasets Hubは、機械学習研究と本番環境のためのキュレーションされたデータセットのリポジトリで、アクセシビリティ、再現性、コンプライアンスのために設計されています。

**主な機能:**
- NLP、コンピュータビジョン、音声、マルチモーダル領域にわたる50万以上のデータセット。
- データセットカード:スキーマ、ソース、意図された用途、ライセンス、制限事項をカバーするドキュメント。
- 変更の追跡と再現性の確保のためのバージョン管理とメタデータ。
- プライバシーと規制要件を満たすための公開および非公開データセット。
- Data Studio:ブラウザベースのインタラクティブなデータセット探索。
- 大規模MLのためのストリーミングとオンザフライデータ処理。

**統合:**
- 高速でプログラマティックなアクセスと効率的なデータ処理のためのHugging Face Datasetsライブラリ。
- 複数のデータ形式(CSV、JSON、Parquet、画像、音声、動画)をサポート。

**人気のデータセット:**
- Common Crawl、OpenWebText(ウェブスケールLLM訓練)
- SQuAD、MNLI、GLUE(NLPベンチマーク)
- nvidia/PhysicalAI-Autonomous-Vehicles(ビジョン)
- openai/gdpval(NLP評価)

**Datasets Hubを閲覧:**  
- [https://huggingface.co/datasets](https://huggingface.co/datasets)

**Datasetsドキュメント:**  
- [Datasetsライブラリドキュメント](https://huggingface.co/docs/datasets/index)
- [データセット追加ガイド](https://huggingface.co/docs/hub/en/datasets-adding)
- [データセットカード](https://huggingface.co/docs/hub/en/datasets-cards)

**使用例:**
```python
from datasets import load_dataset
dataset = load_dataset("squad")
print(dataset["train"][0])
```

### Spaces

Spacesは、機械学習アプリケーションとインタラクティブなウェブアプリのホスティング、共有、デモのためのHugging Faceのプラットフォームです。Spacesは、個人やチームがバックエンドやインフラストラクチャの手間なしにモデルや実験を紹介できるようにします。

**機能:**
- Gradio、Streamlit、静的HTML/JS、または[Docker](/en/glossary/docker/)で構築されたインタラクティブアプリをホスト。
- Hubのモデルとデータセットとの直接統合。
- 計算集約的なデモのためのZeroGPUによる[GPUアクセラレーション](/en/glossary/gpu-acceleration/)。
- データ保持を必要とするアプリのための永続ストレージオプション。
- ライブ開発とデバッグのためのSpaces Dev Mode。
- いいね、タグ、共有を通じたコミュニティエンゲージメント。

**メリット:**
- 研究、デモ、プロトタイプをグローバルな聴衆に紹介。
- フィードバックを収集し、コラボレーションを促進。
- プロフェッショナルなポートフォリオを構築するか、学習リソースを共有。

**人気のSpaces例:**
- [Tongyi-MAI/Z-Image-Turbo(画像生成)](https://huggingface.co/spaces/Tongyi-MAI/Z-Image-Turbo)
- [Dream-wan2-2-faster-Pro(動画生成)](https://huggingface.co/spaces/dream2589632147/Dream-wan2-2-faster-Pro)

**Spacesを閲覧:**  
- [https://huggingface.co/spaces](https://huggingface.co/spaces)

**Spacesドキュメント:**  
- [Spaces概要](https://huggingface.co/docs/hub/en/spaces-overview)
- [Spaces Dev Mode](https://huggingface.co/docs/hub/en/spaces-dev-mode)
- [Spaces GPUアップグレード](https://huggingface.co/docs/hub/en/spaces-gpus)
- [Spacesストレージ](https://huggingface.co/docs/hub/en/spaces-storage)

### Inference ProvidersとEndpoints

Inference Providersは、マネージドクラウドインフラストラクチャ上でHugging Faceモデルのスケーラブルでサーバーレスなデプロイを可能にします。これにより、ハードウェア、スケーリング、システム信頼性の複雑さが抽象化されます。

**仕組み:**
- Hubからモデルを選択。
- Inference Provider(例:SambaNova、Replicate、Together AI)を選択。
- REST APIエンドポイントを介してモデルをデプロイおよび提供し、自動スケーリングと監視を実現。
- 従量課金制の価格設定、またはProサブスクリプションでの無料クォータ。

**メリット:**
- インフラストラクチャを管理せずにモデルを迅速にテストまたはデプロイ。
- ウェブ/モバイル/バックエンドシステムにML推論を統合。
- コスト、速度、コンプライアンス、地理的位置を最適化。

**コード例:**
```python
from huggingface_hub import InferenceClient

client = InferenceClient()
result = client.text_generation("Write a poem about open source AI.")
print(result.generated_text)
```

- [Inference Providersドキュメント](https://huggingface.co/docs/hub/en/models-inference)
- [Inferenceモデルを探索](https://huggingface.co/inference/models)

### Transformersと関連ライブラリ

Transformersライブラリは、ドメイン全体でトランスフォーマーモデルを扱うためのHugging Faceの主力オープンソースPythonパッケージです。

**主な機能:**
- 数百のモデルアーキテクチャのロード、微調整、デプロイ。
- PyTorch、TensorFlow、JAX/Flax互換性。
- トークン化、分散訓練、評価、量子化のためのユーティリティ。
- マルチモーダルサポート(テキスト、ビジョン、音声)。
- モデルのダウンロード/アップロードのためのHugging Face Hub統合。
- 広範なチュートリアルとAPIリファレンス。

**その他の注目すべきライブラリ:**
- **Datasets:** 高速でメモリ効率の良いデータロードと処理。
- **Tokenizers:** 高速でカスタマイズ可能なテキストトークン化。
- **Diffusers:** 生成AIのための最先端の拡散モデルを実装。
- **Safetensors:** 安全で高性能なモデル重みストレージ。
- **PEFT:** 大規模言語モデルのパラメータ効率的な微調整。
- **Gradio:** 数分でML駆動UIを構築・共有。
- **TRL:** 言語モデルのための強化学習アルゴリズムの訓練。

- [Transformersドキュメント](https://huggingface.co/docs/transformers)
- [Datasetsドキュメント](https://huggingface.co/docs/datasets)
- [Diffusersドキュメント](https://huggingface.co/docs/diffusers)
- [Tokenizersドキュメント](https://huggingface.co/docs/tokenizers)
- [Gradioドキュメント](https://gradio.app/docs/)
- [PEFTドキュメント](https://huggingface.co/docs/peft)
- [Safetensorsドキュメント](https://huggingface.co/docs/safetensors)
- [TRLドキュメント](https://huggingface.co/docs/trl)

## オープンソースとコミュニティ

Hugging Faceエコシステムは、オープンソースの原則とコミュニティのコラボレーションを基盤に構築されています。

**コラボレーション:**
- モデル、データセット、Spacesを公開・共有。
- 協調的な開発のためのプルリクエスト、バージョン管理、ディスカッション。
- Meta、Google、Amazon、Microsoft、AI2を含む50,000以上の組織が、モデルの共有とデプロイにHugging Faceを使用。

**透明性:**
- ドキュメントのためのモデルカードとデータセットカードの広範な使用。
- 責任ある使用のためのバージョン追跡、ライセンス、オープンディスカッション。

**貢献:**
- 誰でもモデル、データセット、改善、チュートリアルを貢献可能。
- コミュニティフォーラム、Discord、イベント(例:JAX/Flaxコミュニティウィーク、ワークショップ)が知識共有とメンターシップを促進。

**参加方法:**
- [サインアップ](https://huggingface.co/join)
- [コミュニティガイドライン](https://huggingface.co/code-of-conduct)
- [コンテンツガイドライン](https://huggingface.co/content-guidelines)
- [コミュニティフォーラム](https://discuss.huggingface.co/)

## Hugging Faceの使用方法

### ワークフロー例

#### 1. テキスト生成のための事前学習済みモデルのデプロイ

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator("Hugging Face is", max_length=30)
print(result[0]['generated_text'])
```
- [テキスト生成パイプライン](https://huggingface.co/docs/transformers/en/main_classes/pipelines#transformers.TextGenerationPipeline)

#### 2. 感情分析のためのモデルの微調整

```python
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
dataset = load_dataset("imdb")

def tokenize(batch):
    return tokenizer(batch["text"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    num_train_epochs=3,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
)
trainer.train()
```
- [Trainer API](https://huggingface.co/docs/transformers/en/main_classes/trainer)

#### 3. コミュニティとのモデル共有

- Hub上で新しいリポジトリを作成。
- モデルをアップロードし、モデルカードを追加。
- 可視性(公開/非公開)を設定。
- プルリクエスト、ディスカッション、バージョン管理を通じてコラボレーション。

- [モデル共有ガイド](https://huggingface.co/docs/hub/en/models-uploading)

#### 4. Spacesでのデモアプリの構築

- モデルを使用してGradioまたはStreamlitアプリを開発。
- コードと要件をSpaceにアップロード。
- 公開URLを介してアプリケーションを共有。

- [Spacesドキュメント](https://huggingface.co/docs/hub/en/spaces-overview)

### コードスニペット

**モデルのダウンロード:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
```

**データセットへのアクセス:**
```python
from datasets import load_dataset
dataset = load_dataset("squad")
print(dataset["train"][0])
```

**REST API推論の例:**
```python
import requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"}
payload = {"inputs": "Hugging Face is