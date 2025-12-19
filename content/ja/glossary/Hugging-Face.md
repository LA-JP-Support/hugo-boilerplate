---
title: Hugging Face
date: '2025-12-19'
lastmod: '2025-12-19'
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
url: "/ja/glossary/Hugging-Face/"
---
## Hugging Faceとは?

Hugging Faceは、機械学習と人工知能の民主化に焦点を当てたオープンソースのAIプラットフォームおよびグローバルコミュニティです。自然言語処理(NLP)、コンピュータビジョン、音声、マルチモーダルAIなどの領域にわたって、機械学習モデル、データセット、アプリケーションの共有、発見、デプロイのための統合されたエコシステムを提供しています。

**ミッション:** AIをすべての人にとってアクセス可能で透明性のあるものにする。

**アプローチ:** オープンソースライブラリ、協調的なモデルとデータセットの共有、シームレスなデプロイツール。

**インパクト:** 数百万人のユーザーをサポートし、200万以上のモデル、50万以上のデータセット、100万以上のデモアプリケーション(「Spaces」)を提供。これらのリソースは、研究者、開発者、企業が最先端のAIソリューションを構築・デプロイするのを支援しています。

Hugging Faceは「AIのためのGitHub」として機能し、誰もが事前学習済みモデルやデータを協力、貢献、活用して高度なAIアプリケーションを構築できます。

## 主要用語

**モデル:**  
特定のタスク(テキスト分類、画像認識、音声テキスト変換)を実行するために訓練された機械学習の成果物。モデルは事前学習済みまたはファインチューニング済みの場合があります。

**Model Hub:**  
機械学習モデルの保存、共有、発見のための集中リポジトリ。モデルカード(ドキュメント)、バージョン管理、ライブデモ、主要なMLライブラリとの統合をサポートします。

**データセット:**  
機械学習モデルの訓練、評価、ベンチマークのためのデータサンプル(テキスト、画像、音声)の構造化されたコレクション。

**Datasets Hub:**  
キュレーションされたデータセットのリポジトリで、データセットカード、バージョン管理、メタデータ、Datasetsライブラリを介したプログラマティックアクセスを提供します。

**Transformers:**  
「Attention is All You Need」論文(Vaswani et al., 2017)で導入された、自己注意機構に基づくニューラルネットワークアーキテクチャ。NLPで広く使用され、ビジョン、音声、マルチモーダルタスクでも増加傾向にあります。

**Transformersライブラリ:**  
Transformerベースのモデル(BERT、GPT、T5)への簡単なアクセス、トークン化、訓練、推論のためのユーティリティを提供するPythonライブラリ。

**Space:**  
インタラクティブなデモ、プロトタイプ、ML駆動アプリケーションのためのHugging Face上でホストされるWebアプリケーション。Gradio、Streamlit、カスタムフレームワークをサポートします。

**LLM(大規模言語モデル):**  
数億から数十億のパラメータを持つTransformerベースのモデルで、高度なテキスト生成、理解、翻訳、推論が可能です。

**ZeroGPU:**  
ユーザーが専用GPUインスタンスを設定または支払う必要なく、SpacesでGPUアクセスを可能にする機能。

## コアプラットフォームコンポーネント

### Model Hub

機械学習モデルの共有、発見、使用のための中心的なプラットフォーム。高品質なモデルをすべての人にアクセス可能にし、研究、開発、本番デプロイを加速するように設計されています。

**主要機能:**

- タスク(テキスト生成、分類)、アーキテクチャ(BERT、GPT)、データセット、言語でモデルを検索・フィルタリング
- モデルカード: 使用目的、訓練データ、制限事項、バイアス、ライセンスをカバーする充実したドキュメント
- バージョン管理: すべてのモデル更新を追跡し、再現性、ロールバック、コラボレーションをサポート
- 主要なMLライブラリ(Transformers、PyTorch、TensorFlow、Flax、JAX)との統合
- インタラクティブな推論とライブデモンストレーションのためのブラウザ内モデルウィジェット
- エコシステムの洞察のためのダウンロード統計、タグ、メタデータ

**メリット:**

- 事前学習済みモデルを活用することで、ゼロからの訓練の必要性を削減
- プロトタイピングと本番デプロイを加速
- 透明性のあるドキュメントを通じて責任あるAIと倫理的なAIを促進

**人気のモデル:**  
BERT、RoBERTa、GPT-2、GPT-3、GPT-4(NLP)、Stable Diffusion、DeepSeek、Z-Image-Turbo(ビジョン/マルチモーダル)、Whisper(音声)

**使用例:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
```

### Datasets Hub

機械学習の研究と本番環境のためのキュレーションされたデータセットのリポジトリで、アクセシビリティ、再現性、コンプライアンスのために設計されています。

**主要機能:**

- NLP、コンピュータビジョン、音声、マルチモーダル領域にわたる50万以上のデータセット
- データセットカード: スキーマ、ソース、使用目的、ライセンス、制限事項をカバーするドキュメント
- 変更の追跡と再現性の確保のためのバージョン管理とメタデータ
- プライバシーと規制要件を満たすための公開および非公開データセット
- Data Studio: ブラウザベースのインタラクティブなデータセット探索
- 大規模MLのためのストリーミングとオンザフライのデータ処理

**統合:**  
高速でプログラマティックなアクセスと効率的なデータ処理のためのHugging Face Datasetsライブラリ。複数のデータフォーマット(CSV、JSON、Parquet、画像、音声、動画)をサポートします。

**人気のデータセット:**  
Common Crawl、OpenWebText(Web規模のLLM訓練)、SQuAD、MNLI、GLUE(NLPベンチマーク)

**使用例:**
```python
from datasets import load_dataset
dataset = load_dataset("squad")
print(dataset["train"][0])
```

### Spaces

機械学習アプリケーションとインタラクティブなWebアプリのホスティング、共有、デモのためのプラットフォーム。個人やチームがバックエンドやインフラストラクチャの手間なしにモデルや実験を紹介できるようにします。

**機能:**

- Gradio、Streamlit、静的HTML/JS、Dockerで構築されたインタラクティブなアプリをホスト
- Hubのモデルとデータセットとの直接統合
- 計算集約的なデモのためのZeroGPUによるGPUアクセラレーション
- データ保持が必要なアプリのための永続ストレージオプション
- ライブ開発とデバッグのためのSpaces Dev Mode
- いいね、タグ、共有を通じたコミュニティエンゲージメント

**メリット:**

- 研究、デモ、プロトタイプをグローバルな視聴者に紹介
- フィードバックを収集し、コラボレーションを促進
- プロフェッショナルなポートフォリオを構築または学習リソースを共有

### Inference Providers

管理されたクラウドインフラストラクチャ上でHugging Faceモデルのスケーラブルでサーバーレスなデプロイを可能にします。ハードウェア、スケーリング、システム信頼性の複雑さを抽象化します。

**仕組み:**

- Hubからモデルを選択
- 推論プロバイダー(SambaNova、Replicate、Together AI)を選択
- 自動スケーリングと監視を備えたREST APIエンドポイント経由でモデルをデプロイ・提供
- 従量課金制の価格設定またはProサブスクリプションでの無料クォータ

**例:**
```python
from huggingface_hub import InferenceClient

client = InferenceClient()
result = client.text_generation("Write a poem about open source AI.")
print(result.generated_text)
```

### コアライブラリ

**Transformers:**  
ドメイン全体でTransformerモデルを扱うためのフラッグシップオープンソースPythonパッケージ。PyTorch、TensorFlow、JAX/Flax互換性を持つ数百のモデルアーキテクチャをロード、ファインチューニング、デプロイします。

**その他の注目すべきライブラリ:**

- **Datasets** – 高速でメモリ効率の良いデータロードと処理
- **Tokenizers** – 高速でカスタマイズ可能なテキストトークン化
- **Diffusers** – 生成AIのための最先端の拡散モデル
- **Safetensors** – 安全で高性能なモデル重みストレージ
- **PEFT** – 大規模言語モデルのパラメータ効率的なファインチューニング
- **Gradio** – 数分でML駆動UIを構築・共有
- **TRL** – 言語モデルのための強化学習アルゴリズムの訓練

## オープンソースとコミュニティ

**コラボレーション:**

- モデル、データセット、Spacesを公開・共有
- 協調的な開発のためのプルリクエスト、バージョン管理、ディスカッション
- Meta、Google、Amazon、Microsoftを含む50,000以上の組織がHugging Faceを使用

**透明性:**

- ドキュメントのためのモデルカードとデータセットカードの広範な使用
- 責任ある使用のためのバージョン追跡、ライセンス、オープンディスカッション

**貢献:**

- 誰でもモデル、データセット、改善、チュートリアルを貢献可能
- コミュニティフォーラム、Discord、イベントが知識共有とメンターシップを促進

## ワークフロー例

**事前学習済みモデルのデプロイ:**
```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator("Hugging Face is", max_length=30)
print(result[0]['generated_text'])
```

**感情分析のためのファインチューニング:**
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

**デモアプリの構築:**

- モデルを使用してGradioまたはStreamlitアプリを開発
- コードと要件をSpaceにアップロード
- 公開URLを介してアプリケーションを共有

## ユースケース

**研究開発:**  
事前学習済みモデルによる迅速なプロトタイピング。標準化されたデータセットでのベンチマーク。モデル改善での協力。

**本番デプロイ:**  
推論エンドポイント経由でモデルを提供。Web/モバイル/バックエンドシステムへの統合。クラウドインフラストラクチャでのスケーリング。

**教育と学習:**  
チュートリアル、コース、ドキュメントへのアクセス。最先端モデルでの実験。ポートフォリオプロジェクトの構築。

**ビジネスアプリケーション:**  
AI駆動のチャットボット、推薦システム、検索エンジンの構築。独自データでのモデルのファインチューニング。プライベートモデルでの安全なデプロイ。

## はじめに

**サインアップ:**  
huggingface.co/joinで無料アカウントを作成

**探索:**

- Model Hubを閲覧: huggingface.co/models
- Datasets Hubを閲覧: huggingface.co/datasets
- Spacesを閲覧: huggingface.co/spaces

**ライブラリのインストール:**
```bash
pip install transformers datasets gradio
```

**最初のモデルを実行:**
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("Hugging Face is amazing!")
print(result)
```

## 参考資料

- [公式Hugging Faceサイト](https://huggingface.co/)
- [Model Hubドキュメント](https://huggingface.co/docs/hub/en/models-the-hub)
- [Datasets Hubドキュメント](https://huggingface.co/docs/hub/en/datasets-overview)
- [Spaces概要](https://huggingface.co/docs/hub/en/spaces-overview)
- [Transformersライブラリドキュメント](https://huggingface.co/docs/transformers/en/index)
- [Datasetsライブラリドキュメント](https://huggingface.co/docs/datasets/index)
- [Diffusersドキュメント](https://huggingface.co/docs/diffusers)
- [Tokenizersドキュメント](https://huggingface.co/docs/tokenizers)
- [Gradioドキュメント](https://gradio.app/docs/)
- [PEFTドキュメント](https://huggingface.co/docs/peft)
- [Safetensorsドキュメント](https://huggingface.co/docs/safetensors)
- [TRLドキュメント](https://huggingface.co/docs/trl)
- [Inference Providersドキュメント](https://huggingface.co/docs/hub/en/models-inference)
- [推論モデルを探索](https://huggingface.co/inference/models)
- [モデルカード](https://huggingface.co/docs/hub/en/model-cards)
- [データセットカード](https://huggingface.co/docs/hub/en/datasets-cards)
- [モデルアップロードガイド](https://huggingface.co/docs/hub/en/models-uploading)
- [モデルリリースチェックリスト](https://huggingface.co/docs/hub/en/model-release-checklist)
- [モデルダウンロードガイド](https://huggingface.co/docs/hub/en/models-downloading)
- [モデルウィジェットドキュメント](https://huggingface.co/docs/hub/en/models-widgets)
- [データセット追加ガイド](https://huggingface.co/docs/hub/en/datasets-adding)
- [Spaces Dev Mode](https://huggingface.co/docs/hub/en/spaces-dev-mode)
- [Spaces GPUアップグレード](https://huggingface.co/docs/hub/en/spaces-gpus)
- [Spacesストレージ](https://huggingface.co/docs/hub/en/spaces-storage)
- [テキスト生成パイプライン](https://huggingface.co/docs/transformers/en/main_classes/pipelines#transformers.TextGenerationPipeline)
- [Trainer API](https://huggingface.co/docs/transformers/en/main_classes/trainer)
- [サインアップ](https://huggingface.co/join)
- [コミュニティガイドライン](https://huggingface.co/code-of-conduct)
- [コンテンツガイドライン](https://huggingface.co/content-guidelines)
- [コミュニティフォーラム](https://discuss.huggingface.co/)
