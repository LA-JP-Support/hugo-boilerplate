---
title: KVキャッシュ
date: 2025-11-25
translationKey: kv-cache
description: KVキャッシュは、TransformerモデルとLLMの推論時最適化技術であり、KeyとValueテンソルを保存することで、自己回帰的なトークン生成を劇的に高速化し、計算コストを削減します。
keywords:
- KVキャッシュ
- LLM
- Transformerモデル
- 推論最適化
- トークン生成
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: KV Cache
term: ケーブイキャッシュ
---
## KVキャッシュとは?

**KVキャッシュ**(Key-Value Cache)は、トランスフォーマーモデル、特に*大規模言語モデル*(LLM)における推論時の最適化手法であり、アテンション計算時に生成されたキー(K)とバリュー(V)のテンソルを、処理済みの全トークンについて保存します。推論の各ステップでこれらのテンソルを再計算する代わりに、モデルはキャッシュから再利用し、新しいトークンのKとVのみを計算します。このアプローチは、効率的で高速な自己回帰型テキスト生成の基盤となっています。

**要約:**  
> KVキャッシュは、以前のトークンから得られた中間的なキーとバリューのテンソルを保持する補助メモリであり、新しいトークンが生成される際、新しいトークンのKとVのみを計算して追加すればよいようにします。以前の全てのK/Vはキャッシュから即座に利用可能です。

### 権威ある情報源:
- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Sebastian Raschka: Understanding and Coding the KV Cache in LLMs from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## KVキャッシュはどのように使用されるか?

KVキャッシュは、トランスフォーマーベースのモデルにおいて、トークンごとにテキストを生成する推論時にのみ使用されます。

### 主な使用パターン:
- **自己回帰型生成:** LLMは一度に1トークンずつテキストを生成し、各予測は全ての先行トークンに条件付けられます。
- **各推論ステップで:** モデルは次のトークンのアテンションを計算するために、これまでの全シーケンスのKとVを必要とします。
- **KVキャッシュを使用すると:** 全ての以前のトークンのKとVを毎ステップ再計算する代わりに、新しいトークンのKとVのみを計算してキャッシュに追加します。
- **結果:** 計算量の大幅な削減、[レイテンシ](/en/glossary/latency/)の低減、推論時のコスト削減が実現されます—特に長いシーケンスにおいて顕著です。

### 一般的な使用コンテキスト:
- LLMによるテキスト生成(例: GPT、Llama、Claude、Gemini)
- チャットボットと対話エージェント
- コード補完とコードアシスタント
- リアルタイムおよびバッチ推論サービング

#### 追加資料:
- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Transformers Documentation: Generation Strategies - KV Caching](https://huggingface.co/docs/transformers/main/en/generation_strategies#kv-caching)

## 大規模言語モデル(LLM)においてKVキャッシュが重要な理由

### KVキャッシュなしの課題

トランスフォーマーのアテンションメカニズムは、トークンごとに3つの射影を含みます:
- **クエリ(Q):** 現在のトークンが「知りたいこと」。
- **キー(K):** 各トークンの「アドレスラベル」。
- **バリュー(V):** 各トークンの「内容」。

推論時、LLMは入力を一度に1トークンずつ処理します。標準的な推論では、既に処理されたトークンを含む現在のシーケンス内の全トークンについて、KとVを毎回再計算します。これは長いシーケンスにおいて非常に非効率的です。

#### 非効率性の例:
「The cat sits」を生成する場合:
- 「The」を生成: 「The」のK/Vを計算。
- 「The cat」を生成: 「The」と「cat」の両方のK/Vを再計算。
- 「The cat sits」を生成: 3つ全てのトークンのK/Vを再計算。

#### KVキャッシュを使用すると:
- 「The」のK/Vを一度計算し、保存。
- 「cat」では、「cat」のK/Vを計算し、キャッシュに追加。
- 「sits」では、「sits」のK/Vを計算し、キャッシュに追加;「The」と「cat」のK/Vは再利用。

**最適化が重要な理由:**
- **速度:** 推論が最大5〜20倍高速化。
- **コスト:** 計算とAPIコストの大幅な削減。
- **スケーラビリティ:** 長いコンテキストと複数ターンの会話を可能に。

##### さらなる権威ある情報:
- [Neptune: Transformers Key-Value Caching Explained](https://neptune.ai/blog/transformers-key-value-caching)
- [Hugging Face Blog: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)

## 詳細な例: KVキャッシュの動作方法

### トークン生成のステップバイステップ

#### KVキャッシュなし:
プロンプト: `["The", "cat", "sits"]`
- 各ステップで現在のシーケンス内の全トークンのKとVを再計算。

**図:**
```
ステップ1: "The"           --> K1, V1    (計算)
ステップ2: "The cat"       --> K1, V1, K2, V2  (K1, V1を再計算)
ステップ3: "The cat sits"  --> K1, V1, K2, V2, K3, V3 (K1, V1, K2, V2を再計算)
```

#### KVキャッシュあり:
- 各ステップで新しいトークンのK/Vのみを計算/追加;キャッシュは以前のK/Vを保持。

**図:**
```
ステップ1: "The"      --> K1, V1    (キャッシュに保存)
ステップ2: "cat"      --> K2, V2    (キャッシュに追加)
ステップ3: "sits"     --> K3, V3    (キャッシュに追加)
```
**ステップ3後のキャッシュ:**
```
Kキャッシュ: [K1, K2, K3]
Vキャッシュ: [V1, V2, V3]
```

##### 視覚的な図解:
![KV Cache Illustration](https://cdn-uploads.huggingface.co/production/uploads/6527e89a8808d80ccff88b7a/ZiRajz9XfXiPT3NIM05FS.png)
[出典: Hugging Face Blog](https://huggingface.co/blog/not-lain/kv-caching#how-does-kv-caching-work)

## 技術的詳細: KVキャッシュの実装

### 数学的定式化

n個の入力トークンのシーケンスに対して、トランスフォーマー層は以下を計算します:
\[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right)V
\]

- **訓練時:** 全トークンのQ、K、Vが並列に計算されます。
- **KVキャッシュを使用した推論時:** 新しいトークンのQ、K、Vのみが計算され;以前のKとVはキャッシュから取得されます。

### PyTorch KVキャッシュの例

```python
class KVCache:
    def __init__(self):
        self.cache = {"key": None, "value": None}

    def update(self, key, value):
        if self.cache["key"] is None:
            self.cache["key"] = key
            self.cache["value"] = value
        else:
            self.cache["key"] = torch.cat([self.cache["key"], key], dim=1)
            self.cache["value"] = torch.cat([self.cache["value"], value], dim=1)

    def get_cache(self):
        return self.cache
```

### Hugging Face Transformersでの使用

最新のライブラリの多くは、KVキャッシュを自動的に処理します。

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')

tokens = tokenizer.encode("The cat sits", return_tensors="pt")
output = model.generate(tokens, max_new_tokens=10, use_cache=True)
print(tokenizer.decode(output[0]))
```
- `use_cache`パラメータがKVキャッシングを有効化します(デフォルト: `True`)。

#### さらなるコードと説明:
- [Sebastian Raschka: Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
- [Hugging Face Blog: Practical Implementation](https://huggingface.co/blog/not-lain/kv-caching#practical-implementation)

## パフォーマンスへの影響: 速度、メモリ、コストのトレードオフ

### 定量的影響

| 特徴                | 標準推論                        | KVキャッシング                      |
|---------------------|--------------------------------|-------------------------------------|
| 単語あたりの計算    | 計算を繰り返す                  | キャッシュされた値を再利用          |
| メモリ使用量        | ステップごとに少ない、テキストで増加 | キャッシュ用の追加メモリ、しかし効率的 |
| 速度                | 長いテキストで遅くなる          | 長いテキストでも高速を維持          |
| コスト              | 高い計算量、長いレイテンシ      | 低い計算量、削減されたレイテンシ    |

#### ベンチマーク:
- T4 GPU上(SmolLM2-1.7B):
    - 標準推論(KVキャッシュなし): **61秒**
    - KVキャッシング有効: **11.7秒**
    - **約5.2倍の高速化**
- 多くのAPIプロバイダー(例: Anthropic、OpenAI)は、キャッシュされたトークンに対して低料金を請求します。キャッシュされたトークンは最大10倍安価になることがあります(例: 100万あたり$0.30 vs $3)。

##### 出典:
- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching#comparison-kv-caching-vs-standard-inference)
- [Sebastian Raschka: KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## KVキャッシュの効率を最大化するベストプラクティス

### プロンプトエンジニアリングとコンテキスト管理

- **安定したプロンプトプレフィックス:**  
  プロンプトプレフィックスはターン間で同一である必要があります。どんな変更(1トークンでも)もその時点からキャッシュを無効化します。
- **追加専用コンテキスト:**  
  常に新しい情報を追加;以前のコンテキストを書き換えたり並べ替えたりしないでください。
- **決定論的な順序:**  
  構造化データは、偶発的なキャッシュ無効化を避けるために一貫した順序を持つ必要があります。
- **明示的なキャッシュブレークポイント:**  
  マルチターンエージェントの場合、コンテキストが変更される場所をマークして、フレームワークが効率を維持できるようにします。

### 本番環境でのキャッシュ管理

- **キャッシュサイズ:**  
  K/Vテンソルはコンテキスト長に対して線形にスケールします。非常に長いシーケンスでは、メモリ使用量がボトルネックになる可能性があります。
- **キャッシュの有効期間:**  
  コンテキストが変更されたとき、またはメモリを解放する必要があるときに、キャッシュエントリを無効化/期限切れにします。
- **並行性:**  
  各並行リクエストは独自のキャッシュスペースを必要とする場合があります。

**ヒント:**  
> キャッシュ効率を最大化するには、プロンプトプレフィックスを安定させ、コンテキストを追加専用に保ちます。古いエントリを変更する動的なコンテキストは避けてください。

##### さらなる資料:
- [Hugging Face: How Does KV Caching Work?](https://huggingface.co/blog/not-lain/kv-caching#how-does-kv-caching-work)

## 高度なKVキャッシュ技術

### ページドアテンション
- コンテキストを「ページ」(チャンク)に分割。
- 関連するページのみを高速メモリに保持;古いページはオフロードまたは必要に応じて再計算。
- GPUメモリを使い果たすことなく、非常に長いコンテキスト(数万トークン)の処理を可能にします。

### ラディックスアテンション
- キャッシュされたトークンをラディックスツリー構造で整理。
- 対数スケーリング: トークンのグループに階層的にアテンション。

### マルチクエリアテンション
- アテンションヘッド間でキー/バリューを共有することで、KVキャッシュメモリを削減。

#### 新たなトレンド
- **予測的キャッシュウォーミング:** 予想されるニーズに基づいてキャッシュを事前に入力。
- **階層的キャッシング:** マルチレベルキャッシュ戦略(GPU、CPU、ディスク)。
- **動的キャッシュサイジング:** リアルタイムでキャッシュサイズを調整。

##### 詳細:
- [Sebastian Raschka: Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## ユースケースと実世界のアプリケーション

### チャットボットと対話エージェント
- マルチターン会話でプロンプトプレフィックスを再利用。
- KVキャッシュは最初のトークンまでの時間(TTFT)と全体的なレイテンシを削減。

### コード生成と補完
- コードアシスタント(例: Copilot)は、即座の補完のためにKVキャッシュを使用。

### カスタマーサポート自動化
- コンテキスト付きチャット履歴が効率的に管理され、低レイテンシの応答を実現。

### ドキュメントとコンテンツ生成
- 長文コンテンツ作成はプロンプトキャッシングの恩恵を受け、効率的な編集と反復的なワークフローを可能にします。

### ゲームとインタラクティブストーリーテリング
- ゲーム内対話エンジンは、没入感のある低レイテンシのプレイヤー体験のためにストーリーコンテキストをキャッシュ。

**ケーススタディ:**  
Anthropic ClaudeのAPIは、キャッシュされたトークンに対して10分の1の料金を請求します。カスタマーサポートチャットボットで安定したプレフィックスを維持することで、運用コストを削減し、応答性を向上させることができます。

## 制限と課題

- **メモリの増加:**  
  K/Vキャッシュはコンテキストに対して線形に増加します。非常に長いコンテキストはGPUメモリを使い果たす可能性があります。
- **キャッシュの無効化:**  
  以前のトークンへの変更(プロンプト編集、コンテキスト変更)は、キャッシュの一部/全体を無効化します。
- **管理の複雑さ:**  
  マルチユーザー/マルチターンシステムは、慎重なキャッシュ管理を必要とします。
- **訓練時には使用されない:**  
  KVキャッシュは推論専用の最適化です。

##### 権威ある情報:
- [Hugging Face: Standard Inference and the Rise of KV Caching](https://huggingface.co/blog/not-lain/kv-caching#standard-inference-and-the-rise-of-kv-caching)
- [Sebastian Raschka: KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)

## 関連用語の用語集

| 用語                 | 定義                                                                                                          |
|----------------------|---------------------------------------------------------------------------------------------------------------------|
| **アテンションメカニズム** | トランスフォーマーが各トークン出力のために入力シーケンスのどの部分に注目するかを決定するプロセス。        |
| **キー(K)**          | 各トークンのベクトル表現で、アテンション計算における「アドレス」として使用されます。                              |
| **バリュー(V)**        | 各トークンに関連付けられたコンテンツベクトルで、出力のコンテキストベクトルを生成するために使用されます。                          |
| **クエリ(Q)**        | 現在のトークンのベクトルで、「コンテキストから何が必要か?」を尋ねます。                                                  |
| **マルチヘッドアテンション** | 異なる部分空間から情報を捉えるために、複数のQ/K/V射影セットを使用するアテンションメカニズム。         |
| **自己回帰型デコーディング** | 一度に1トークンずつテキストを生成し、各出力を全ての先行トークンに条件付けます。                              |
| **因果アテンション** | 将来のトークンをマスクして、モデルが「後ろを見る」だけで「前を見ない」ようにします。                                           |
| **フォワードパス**     | 与えられた入力に対してニューラルネットワークの出力を計算するプロセス。                                              |
| **最初のトークンまでの時間(TTFT)** | プロンプトをモデルに送信してから、応答の最初のトークンを受信するまでの時間。                      |

## 参考文献とさらなる資料

- [Hugging Face Blog: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Neptune: Transformers Key-Value Caching Explained](https://neptune.ai/blog/transformers-key-value-caching)
- [Sebastian Raschka: Understanding and Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
- [Data Science Dojo: Unlocking the Power of KV Cache](https://datasciencedojo.com/blog/kv-cache-how-to-speed-up-llm-inference/)
- [Kapil Sharma: KV Caching Illustrated](https://kapilsh.github.io/posts/kv-caching-visualized/)
- [Akira AI: KV Caches and Time-to-First-Token](https://www.akira.ai/blog/kv-caches-and-time-to-first-token)
- [Andrew Szot: KV Cache](https://www.andrewszot.com/posts/kv_cache/)
- [Transformers Documentation: Generation Strategies - KV Caching](https://huggingface.co/docs/transformers/main/en/generation_strategies#kv-caching)
- [Joaolages: KV Caching Explained](https://medium.com/@joaolages/kv-caching-explained-276520203249)

## さらなる探求

トランスフォーマーの内部構造、プロンプトエンジニアリング、LLM最適化についてさらに詳しく知るには、上記の参考文献を参照し、高度なアテンションメカニズムとコンテキスト管理に関する追加リソースを探索してください。

*KVキャッシングに関する実装や設計決定は、上記にリストされた最新の本番環境LLM技術と権威ある情報源を参照して行う必要があります。図、PyTorchコード、エッジケースエンジニアリングを含む最も深い技術的詳細については、以下をレビューしてください:*

- [Hugging Face: KV Caching Explained](https://huggingface.co/blog/not-lain/kv-caching)
- [Sebastian Raschka: Coding the KV Cache in LLMs](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)