---
title: 投機的デコーディング
date: 2025-11-25
translationKey: speculative-decoding
description: 投機的デコーディングは、高速なドラフトモデルを使用してトークンを提案し、より大規模なターゲットモデルで検証することで、LLM推論を高速化します。出力品質を維持しながらレイテンシを削減します。
keywords:
- 投機的デコーディング
- LLM推論
- ドラフトモデル
- ターゲットモデル
- レイテンシ削減
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: Speculative Decoding
term: とうきてきでこーでぃんぐ
reading: 投機的デコーディング
kana_head: その他
---
## 定義

**投機的デコーディング(Speculative Decoding)**は、大規模言語モデル(LLM)の推論最適化技術であり、小型で高速なドラフトモデルを活用して複数のトークンを事前に提案し、大型で高精度なターゲットモデルがドラフトを検証して最長一致プレフィックスを受け入れることで、より高速なトークン生成を実現します。このプロセスはターゲットモデルの出力分布を維持し、純粋な逐次デコーディングと数学的に同一の結果を保証しながら、[レイテンシ](/en/glossary/latency/)を大幅に削減します。

> *「投機的デコーディングは、複数のトークンを同時に予測・検証することで大規模言語モデル(LLM)を高速化し、出力品質を保ちながらレイテンシを削減する推論最適化技術です。」*  
> — [NVIDIA Technical Blog](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)

重要な洞察は、LLM出力シーケンスの多くのトークンは、はるかに小型のモデルで正しく推測でき、大型モデルでトークンのバッチをまとめて検証する方が、各トークンを厳密に順次生成するよりも効率的であるということです。

**主要参考文献:**
- [arXiv: Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
- [Google Research Blog: Looking back at speculative decoding](https://research.google/blog/looking-back-at-speculative-decoding/)
- [NVIDIA Technical Blog: An introduction to speculative decoding](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)

## 投機的デコーディングの仕組み

投機的デコーディングは**ドラフト→検証**プロセスとして構成されています:

### ステップ

1. **ドラフトステップ**
   - ドラフトモデル(小型で高速なLLM)が、候補となる次のトークンのバッチ(通常3〜8個)を生成します。
   - このモデルは「先読み推測」を行うように設計されており、ターゲットモデルが受け入れる可能性の高いトークンを生成します。

2. **検証ステップ**
   - 大型で高精度なターゲットモデルが、同じコンテキスト(入力+これまでに生成されたすべてのトークン)を評価し、次のトークンバッチの確率分布を計算します。
   - ターゲットモデルは、どのドラフトトークンが自身の最も確率の高い次トークン予測と一致するかをチェックします。最長一致プレフィックスを受け入れます(すべて、一部、またはゼロの場合もあります)。

3. **継続**
   - ドラフトが完全に受け入れられた場合、出力は継続されます。不一致がある場合、ターゲットモデル自身が次のトークンを生成し、それが次の投機的ラウンドの新しいコンテキストとなります。

4. **繰り返し**
   - このプロセスは、出力シーケンスが完了するまで続きます。

**視覚化:**  
![Speculative Decoding Flow](https://developer-blogs.nvidia.com/wp-content/uploads/2025/09/inference-speculative-decoding-llama-eagle-1024x576-jpg.webp)

**保証:**  
最終出力は、ターゲットモデルが単純な逐次デコーディングで生成するものと証明可能に同一です。

**参考資料:**  
- [NVIDIA: Speculative Decoding Overview](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)
- [arXiv Paper (PDF)](https://arxiv.org/pdf/2211.17192)

## 技術用語

**自己回帰生成(Autoregressive Generation):**  
トークンを一度に1つずつ生成し、各トークンが以前のすべてのトークンに依存します。これはGPT、T5、LlamaなどのLLMの標準です。

**ドラフトモデル(Draft Model):**  
候補トークンを事前に提案するために使用される小型で高速なモデル。ターゲットモデルの出力分布にできるだけ近づくように訓練または微調整する必要があります。

**ターゲットモデル(Target Model):**  
出力を正確に保持する必要がある大型で高精度なLLM。

**ドラフトトークン(Draft Tokens):**  
ドラフトモデルが次のシーケンス位置のために推測したトークンのバッチ。

**棄却サンプリング(Rejection Sampling):**  
ターゲットモデルが自身の最も確率の高い予測と一致するドラフトトークンのみを受け入れることで、ターゲットの出力分布を保持する統計的メカニズム。

**受入率(Acceptance Rate、α):**  
ターゲットモデルが受け入れたドラフトトークンの割合。高いαは、ドラフトモデルがターゲットモデルとよく整合していることを意味します。

**投機的トークン数(Speculative Token Count、γ):**  
各投機的ラウンドでドラフトモデルが生成するトークンの数。

**受入長(Acceptance Length、τ):**  
投機的ラウンドごとに受け入れられるドラフトトークンの平均数。

**トークン間レイテンシ(Inter-token Latency、ITL):**  
1つの出力トークンを発行してから次のトークンまでの時間。

**EAGLE-3:**  
ターゲットモデル自体の内部レイヤーに軽量な予測ヘッドを接続し、別個のドラフトモデルを不要にする高度な投機的デコーディング技術([NVIDIA EAGLE-3](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/))。

## 動機:なぜ投機的デコーディングを使用するのか?

**LLM推論のボトルネック:**  
- 新しいトークンを生成するたびに、ターゲットモデル全体を通じた完全なフォワードパスが必要であり、これは遅い(特に10B以上のパラメータを持つモデルの場合)。
- この逐次依存性により、高レイテンシと最新GPUの並列計算能力の活用不足が生じます([Google Research](https://research.google/blog/looking-back-at-speculative-decoding/))。

**なぜ投機的デコーディングなのか?**  
- ドラフトモデルに「先読み推測」を許可し、検証のためにのみ大型モデルを呼び出すことで、トークン生成を並列化できます。
- これにより全体的なレイテンシが削減され、スループットが向上し、よりレスポンシブなLLM駆動アプリケーション(チャットボット、コードアシスタント、リアルタイム要約)が可能になります。

**業界のニーズ:**  
- Google SearchのAI Overviewsなどの実世界の製品は、投機的デコーディングに依存して、数十億のユーザーに高品質で低レイテンシの結果を提供しています([Google Research Blog](https://research.google/blog/looking-back-at-speculative-decoding/))。

## コアアルゴリズム:ステップバイステップ

### 疑似コード

```python
context = input_tokens
while not finished:
    draft_tokens = draft_model.generate(context, num_tokens=γ)
    target_distributions = target_model.predict(context, num_tokens=γ)
    accepted = []
    for i in range(γ):
        if draft_tokens[i] == argmax(target_distributions[i]):
            accepted.append(draft_tokens[i])
        else:
            break
    context += accepted
    next_token = target_model.generate(context, num_tokens=1)
    context.append(next_token)
    if next_token == stop_token:
        finished = True
```

### 詳細アルゴリズム

1. **初期化**:  
   ターゲットモデルが標準デコーディングを使用して最初のトークンを生成します。

2. **ドラフト**:  
   ドラフトモデルが現在のコンテキストを受け取り、γ個のトークンを提案します。

3. **検証**:  
   ターゲットモデルが次のγ個のトークンの確率分布を計算し、ドラフトの提案と比較します。
   - 一致するトークンの最長プレフィックスを受け入れます。
   - 不一致が発生した場合、それ以降のドラフトトークンの受け入れを停止します。

4. **ターゲットトークン生成**:  
   h個のトークン(h ≤ γ)を受け入れた後、ターゲットモデルが次のトークンを生成します。

5. **繰り返し**:  
   コンテキストが更新され、シーケンスが終了するまでプロセスが続きます。

**技術参考文献:**  
- [arXiv: Fast Inference from Transformers via Speculative Decoding, Algorithm 1](https://arxiv.org/pdf/2211.17192)

## パフォーマンス指標と主要要因

### 主要指標

- **受入率(α):**  
  α = (受け入れられたドラフトトークン数) / (ドラフトモデルが提案したトークン数)
  
- **投機的トークン数(γ):**  
  投機的ラウンドごとに提案されるトークンの数。γの調整は高速化とリソース使用に影響します。

- **受入長(τ):**  
  投機的ラウンドごとに受け入れられるドラフトトークンの平均数:  
  τ = (1 - α^(γ+1)) / (1 - α)

- **トークン間レイテンシ(ITL):**  
  生成されたトークン間の時間。

- **スループット:**  
  1秒あたりに生成されるトークン数。

### 実用例

仮定:
- ターゲットモデル生成:10 ms/トークン
- ドラフトモデル:γ=4トークンで1 ms
- ターゲット検証:γ=4トークンで1 ms

ラウンドごとに平均2.5個のドラフトトークンが受け入れられる場合、15 ms(1 msドラフト、1 ms検証、10 ms非受入トークン)で3.5トークンが得られます。  
**実効トークン時間:** ≈4.3 ms/トークン(ベースライン10 ms/トークンと比較)

### 主要要因

- **ドラフトモデルの整合性:**  
  出力分布がターゲットモデルと密接に一致するドラフトモデルから、より高い受入率が得られます。
- **モデルサイズ/アーキテクチャ:**  
  大型モデルほど投機的デコーディングの恩恵が大きい。ドラフトモデルは大幅に高速である必要がありますが、ターゲットの予測が不十分になるほど小さくてはいけません。
- **ハードウェア制約:**  
  両方のモデルとそのキー・バリューキャッシュがメモリに収まる必要があります。
- **バッチサイズ:**  
  投機的デコーディングは、低バッチサイズ(レイテンシ重視のアプリケーション)で最も効果的です。
- **オーケストレーションオーバーヘッド:**  
  モデル間の効率的な通信とスケジューリングが重要です。

**参考文献:**  
- [NVIDIA Blog: Speculative Decoding Math](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)
- [arXiv: Section 3, Theoretical Analysis](https://arxiv.org/pdf/2211.17192)

## メリット

- **2〜3倍以上のレイテンシ削減:**  
  Google製品や学術ベンチマークで実証された高速化([arXiv](https://arxiv.org/abs/2211.17192)、[Google Research](https://research.google/blog/looking-back-at-speculative-decoding/))。
- **出力品質の保証:**  
  出力はターゲットモデルの逐次デコーディングと数学的に同一です。
- **ハードウェア利用率の向上:**  
  トークンチェックを[バッチ処理](/ja/glossary/batch-processing/)することで、GPU/TPUの潜在的な計算能力を解放します。
- **再訓練不要:**  
  事前訓練済みモデルをドラフト/ターゲットとして使用できますが、より高いαのためにドラフトを微調整することは有益です。
- **サービング費用の削減:**  
  同じスループットに必要なマシンが少なくて済みます。
- **主要な本番システムで使用:**  
  Google Search AI Overviews、コードアシスタント、要約ツール。

**リンク:**  
- [NVIDIA Blog](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)
- [Google Research Blog](https://research.google/blog/looking-back-at-speculative-decoding/)

## 制限事項と注意点

- **メモリ使用量の増加:**  
  両方のモデル(キャッシュ付き)がメモリに収まる必要があり、バッチサイズが減少します。
- **スループットのトレードオフ:**  
  高バッチサイズでは、投機的デコーディングは改善せず、競合によりスループットが低下する可能性があります。
- **ドラフトの整合性が低い場合の無駄:**  
  受入率が低い場合(例:0.5未満)、投機的デコーディングは高速化なしにオーバーヘッドを追加します。
- **モデル互換性の制約:**  
  ドラフトとターゲットは、最良の結果を得るために同じトークナイザーと類似のアーキテクチャを使用する必要があります。
- **オーケストレーションの複雑さ:**  
  効率的なモデル相互作用とキャッシュ管理のための慎重なエンジニアリングが必要です。
- **小型モデルや高バッチ負荷では効果が低い:**  
  高速化は、大型モデルとレイテンシに敏感なアプリケーションで最も顕著です。

**参考文献:**  
- [NVIDIA EAGLE-3](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)
- [arXiv: Discussion](https://arxiv.org/abs/2211.17192)

## 実装ガイダンス

### 投機的デコーディングを使用すべき場合

- **レイテンシ重視のアプリケーション:**  
  チャットボット、コード補完、リアルタイム要約。
- **大型モデル:**  
  10B以上のパラメータで、トークンごとのレイテンシが最も高い場合。
- **低〜中程度のバッチサイズ:**  
  ユーザー向けレイテンシがスループットよりも重要な場合。

### 避けるべき場合

- **GPUメモリが最大:**  
  大きなバッチサイズ、長いコンテキストウィンドウ。
- **低いドラフト受入率:**  
  ドラフトモデルがターゲットを模倣するのに苦労している場合。
- **小型LLM:**  
  わずかな利益が複雑さを正当化しない。

### 設定と調整

- **ドラフトモデルの選択:**  
  ターゲットの小型バージョンから始め、可能であれば微調整します。
- **投機的トークン数(γ):**  
  典型的:ラウンドごとに3〜8。ワークロードに合わせて調整します。
- **受入率の監視:**  
  本番環境でαを追跡します。α < 0.6の場合、調整またはフォールバックを検討します。
- **メモリ管理:**  
  GPUメモリを監視。必要に応じて量子化またはモデル分割を使用します。

### 例:vLLM Python API

```python
from vllm import LLM, SamplingParams

llm = LLM(model="your-target-model", draft_model="your-draft-model")
params = SamplingParams(max_tokens=100, speculative_tokens=4)
output = llm.generate("Prompt text", sampling_params=params)
print(output)
```

**参考文献:**  
- [vLLM Speculative Decoding](https://docs.vllm.ai/en/latest/features/spec_decode/)
- [BentoML vLLM Example](https://docs.bentoml.com/en/latest/examples/vllm.html)

## 例とユースケース

### 実世界の展開

- **Google Search AI Overviews:**  
  数十億のユーザーに高品質で低レイテンシの要約を提供([Google Research](https://research.google/blog/looking-back-at-speculative-decoding/))。
- **コード生成ツール:**  
  高速なコード補完のためにIDEアシスタントで使用されます。
- **エンタープライズチャットボット:**  
  ユーザーエクスペリエンスを向上させ、大量のカスタマーサポートのサービング費用を削減します。
- **バッチ翻訳/要約:**  
  サンプルごとのレイテンシが高い長文書の高速出力を可能にします。

### 研究ベンチマーク

- **T5-XXL(11B)とT5-small(60M):**  
  [arXiv](https://arxiv.org/abs/2211.17192)は、翻訳タスクで2〜3倍の高速化を示しています。
- **Llama 70B:**  
  [vLLM](https://docs.vllm.ai/en/latest/features/spec_decode/)と[BentoML](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction)は、大幅なレイテンシ改善を報告しています。

## ベストプラクティスと調整

1. **ドラフトモデルの選択:**  
   同じファミリーとトークナイザーの小型モデルを使用。可能であればユースケースに合わせて微調整します。
2. **γの調整:**  
   γ=3〜5から始め、αが高いままであれば増やします。
3. **αの監視:**  
   αが0.5を下回る場合、γを減らすかドラフトモデルを再整合します。
4. **メモリの最適化:**  
   必要に応じて量子化、マルチGPU、またはバッチ/コンテキストの削減を使用します。
5. **ベンチマーク:**  
   実際のワークロードとハードウェアでテストします。
6. **フォールバックの自動化:**  
   αまたはメモリ圧力がしきい値を超えた場合、投機的デコーディングを無効にします。

## オープンソースツールとフレームワーク

- **[vLLM](https://github.com/vllm-project/vllm):**  
  投機的デコーディングを備えた高スループットLLM推論エンジン。
- **[BentoML](https://bentoml.com/llm/inference-optimization/speculative-decoding):**  
  ガイドとフレームワーク統合。
- **[Modular MAX](https://docs.modular.com/max/serve/speculative-decoding):**  
  設定による即座のサポート。
- **[TensorRT-LLM (Baseten)](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/):**  
  投機的デコーディングを備えた高性能デプロイメント。

## 参考資料

- [Google Research Blog: Looking back at speculative decoding](https://research.google/blog/looking-back-at-speculative-decoding/)
- [Fast Inference from Transformers via Speculative Decoding (arXiv)](https://arxiv.org/abs/2211.17192)
- [NVIDIA Technical Blog: Speculative Decoding](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/)
- [BentoML: Speculative decoding](https://bentoml.com/llm/inference-optimization/speculative-decoding)
- [Baseten: Quick introduction to speculative decoding](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/)
- [Speculative Sampling (Stern et al., 2018, precursor)](https://arxiv.org/abs/1811.03115)
- [Distributed Speculative Decoding](https://arxiv.org/abs/2302.01318)

## 関連用語

- [LLM inference](https://bentoml.com/llm/inference-optimization/speculative-decoding)
- [Speculative execution](https://en.wikipedia.org/wiki/Speculative_execution)
- [Rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling)