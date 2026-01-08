---
title: 投機的デコーディング
date: '2025-12-19'
lastmod: '2025-12-19'
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
url: "/ja/glossary/Speculative-Decoding/"
---
## Speculative Decoding(投機的デコーディング)とは?
Speculative Decoding(投機的デコーディング)は、大規模言語モデル(LLM)の推論最適化技術であり、小型で高速なドラフトモデルを活用して複数のトークンを事前に提案し、大型で正確なターゲットモデルがドラフトを検証して最長一致プレフィックスを受け入れることで、より高速なトークン生成を実現します。このプロセスはターゲットモデルの出力分布を維持し、純粋な逐次デコーディングと数学的に同一の結果を保証しながら、レイテンシを大幅に削減します。

重要な洞察は、LLM出力シーケンスの多くのトークンは、はるかに小型のモデルでも正確に推測でき、大型モデルで複数のトークンをまとめて検証する方が、各トークンを厳密に順次生成するよりも効率的であるということです。

Speculative Decodingは、ターゲットモデルの正確な出力品質を維持しながら、本番システムで2~3倍以上のレイテンシ削減を実現する<strong>ドラフト-検証</strong>プロセスとして構成されています。

## Speculative Decodingの仕組み

### ドラフト-検証プロセス

<strong>1. ドラフトステップ</strong>ドラフトモデル(小型で高速なLLM)が、候補となる次のトークンのバッチ(通常3~8個)を生成します。このモデルは「先読み推測」を行うように設計されており、ターゲットモデルが受け入れる可能性の高いトークンを生成します。

<strong>2. 検証ステップ</strong>大型で正確なターゲットモデルが、同じコンテキスト(入力とこれまでに生成されたすべてのトークン)を評価し、次のトークンバッチの確率分布を計算します。ターゲットモデルは、どのドラフトトークンが自身の最も確率の高い次トークン予測と一致するかをチェックします。最長一致プレフィックスを受け入れます。これは、すべて、一部、またはドラフトトークンのいずれも含まない場合があります。

<strong>3. 継続</strong>ドラフトが完全に受け入れられた場合、出力は継続されます。不一致がある場合、ターゲットモデル自身が次のトークンを生成し、それが次の投機的ラウンドの新しいコンテキストになります。

<strong>4. 繰り返し</strong>このプロセスは、出力シーケンスが完了するまで続きます。

<strong>保証:</strong>最終的な出力は、ターゲットモデルが単純な逐次デコーディングで生成するものと証明可能に同一です。

## 主要な用語

<strong>自己回帰生成(Autoregressive Generation):</strong>トークンを一度に1つずつ生成し、各トークンが以前のすべてのトークンに依存します。これはGPT、T5、LlamaなどのLLMの標準です。

<strong>ドラフトモデル(Draft Model):</strong>候補トークンを事前に提案するために使用される小型で高速なモデル。ターゲットモデルの出力分布にできるだけ近づくように訓練または微調整する必要があります。

<strong>ターゲットモデル(Target Model):</strong>出力を正確に保持する必要がある大型で正確なLLM。

<strong>ドラフトトークン(Draft Tokens):</strong>ドラフトモデルが次のシーケンス位置のために推測したトークンのバッチ。

<strong>棄却サンプリング(Rejection Sampling):</strong>ターゲットモデルが自身の最も確率の高い予測と一致するドラフトトークンのみを受け入れることで、ターゲットの出力分布を保持する統計的メカニズム。

<strong>受け入れ率(Acceptance Rate、α):</strong>ターゲットモデルが受け入れたドラフトトークンの割合。高いαは、ドラフトモデルがターゲットモデルによく整合していることを意味します。

<strong>投機的トークン数(Speculative Token Count、γ):</strong>各投機的ラウンドでドラフトモデルが生成するトークンの数。

<strong>受け入れ長(Acceptance Length、τ):</strong>投機的ラウンドごとに受け入れられるドラフトトークンの平均数:τ = (1 - α^(γ+1)) / (1 - α)

<strong>トークン間レイテンシ(Inter-Token Latency、ITL):</strong>1つの出力トークンを発行してから次のトークンまでの時間。

<strong>EAGLE-3:</strong>ターゲットモデル自体の内部レイヤーに軽量な予測ヘッドを接続し、別個のドラフトモデルを不要にする高度なSpeculative Decoding技術。

## 動機

### LLM推論のボトルネック

<strong>問題:</strong>- 新しいトークンを生成するたびに、ターゲットモデル全体を通じた完全なフォワードパスが必要であり、これは遅い(特に10Bパラメータ以上のモデルの場合)
- この逐次依存性により、高いレイテンシと最新のGPUにおける並列計算の活用不足が生じる

<strong>解決策:</strong>- ドラフトモデルに「先読み推測」を許可し、検証のためにのみ大型モデルを呼び出すことで、トークン生成を並列化できる
- これにより、全体的なレイテンシが削減され、スループットが向上し、よりレスポンシブなLLM駆動アプリケーション(チャットボット、コードアシスタント、リアルタイム要約)が可能になる

<strong>業界のニーズ:</strong>Google SearchのAI Overviewsなどの実世界の製品は、Speculative Decodingを活用して、数十億のユーザーに高品質で低レイテンシの結果を提供しています。

## コアアルゴリズム

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

### 詳細なアルゴリズム

<strong>1. 初期化:</strong>ターゲットモデルが標準デコーディングを使用して最初のトークンを生成します。

<strong>2. ドラフト:</strong>ドラフトモデルが現在のコンテキストを受け取り、γ個のトークンを提案します。

<strong>3. 検証:</strong>ターゲットモデルが次のγ個のトークンに対する確率分布を計算し、ドラフトの提案と比較します。一致するトークンの最長プレフィックスを受け入れます。不一致が発生した場合、それ以上のドラフトトークンの受け入れを停止します。

<strong>4. ターゲットトークン生成:</strong>h個のトークン(h ≤ γ)を受け入れた後、ターゲットモデルが次のトークンを生成します。

<strong>5. 繰り返し:</strong>コンテキストが更新され、シーケンスが終了するまでプロセスが続きます。

## パフォーマンス指標

### 主要指標

<strong>受け入れ率(Acceptance Rate、α):</strong>α = (受け入れられたドラフトトークン数) / (ドラフトモデルが提案したトークン数)

<strong>投機的トークン数(Speculative Token Count、γ):</strong>投機的ラウンドごとに提案されるトークンの数。γの調整は、高速化とリソース使用に影響します。

<strong>受け入れ長(Acceptance Length、τ):</strong>投機的ラウンドごとに受け入れられるドラフトトークンの平均数

<strong>トークン間レイテンシ(Inter-Token Latency、ITL):</strong>生成されたトークン間の時間

<strong>スループット(Throughput):</strong>1秒あたりに生成されるトークン数

### 実用例

仮定:
- ターゲットモデル生成:10 ms/トークン
- ドラフトモデル:γ=4トークンで1 ms
- ターゲット検証:γ=4トークンで1 ms

ラウンドごとに平均2.5個のドラフトトークンが受け入れられる場合、15 ms(1 msドラフト、1 ms検証、受け入れられなかったトークンに10 ms)で3.5トークンを取得します。

<strong>実効トークン時間:</strong>≈4.3 ms/トークン(ベースライン10 ms/トークンと比較)

### 主要要因

<strong>ドラフトモデルの整合性:</strong>高い受け入れ率は、出力分布がターゲットモデルの分布に密接に一致するドラフトモデルから得られます。

<strong>モデルサイズ/アーキテクチャ:</strong>大型モデルはSpeculative Decodingからより多くの恩恵を受けます。ドラフトモデルは大幅に高速である必要がありますが、ターゲットを不十分に予測するほど小さくてはいけません。

<strong>ハードウェア制約:</strong>両方のモデルとそのキー-バリューキャッシュがメモリに収まる必要があります。

<strong>バッチサイズ:</strong>Speculative Decodingは、低バッチサイズ(レイテンシクリティカルなアプリケーション)で最も効果的です。

<strong>オーケストレーションオーバーヘッド:</strong>モデル間の効率的な通信とスケジューリングが重要です。

## 利点

<strong>2~3倍以上のレイテンシ削減:</strong>Google製品や学術ベンチマークで実証的に証明された高速化。

<strong>出力品質の保証:</strong>出力はターゲットモデルの逐次デコーディングと数学的に同一です。

<strong>ハードウェア活用の向上:</strong>トークンチェックをバッチ処理することで、GPU/TPUの潜在的な計算能力を解放します。

<strong>再訓練不要:</strong>事前訓練済みのモデルをドラフト/ターゲットとして使用できますが、より高いαのためにドラフトを微調整することは有益です。

<strong>サービング費用の削減:</strong>同じスループットに必要なマシンが少なくなります。

<strong>主要な本番システムで使用:</strong>Google Search AI Overviews、コードアシスタント、要約ツール。

## 制限と注意事項

<strong>メモリ使用量の増加:</strong>両方のモデル(キャッシュ付き)がメモリに収まる必要があり、バッチサイズが減少します。

<strong>スループットのトレードオフ:</strong>高バッチサイズでは、Speculative Decodingは改善されず、競合によりスループットが低下する可能性があります。

<strong>ドラフトの整合性が低い場合の無駄:</strong>受け入れ率が低い場合(例:0.5未満)、Speculative Decodingは高速化なしにオーバーヘッドを追加します。

<strong>モデル互換性の制約:</strong>最良の結果を得るには、ドラフトとターゲットは同じトークナイザーと類似のアーキテクチャを使用する必要があります。

<strong>オーケストレーションの複雑さ:</strong>効率的なモデル相互作用とキャッシュ管理のための慎重なエンジニアリングが必要です。

<strong>小型モデルまたは高バッチ負荷では効果が低い:</strong>高速化は、大型モデルとレイテンシに敏感なアプリケーションで最も顕著です。

## 実装ガイダンス

### Speculative Decodingを使用すべき場合

<strong>レイテンシクリティカルなアプリケーション:</strong>チャットボット、コード補完、リアルタイム要約。

<strong>大型モデル:</strong>10Bパラメータ以上で、トークンあたりのレイテンシが最も高い場合。

<strong>低~中程度のバッチサイズ:</strong>ユーザー向けレイテンシがスループットよりも重要な場合。

### 避けるべき場合

<strong>GPUメモリが最大:</strong>大きなバッチサイズ、長いコンテキストウィンドウ。

<strong>低いドラフト受け入れ率:</strong>ドラフトモデルがターゲットを模倣するのに苦労する場合。

<strong>小型LLM:</strong>わずかな利益が複雑さを正当化しない場合。

### 設定と調整

<strong>ドラフトモデルの選択:</strong>ターゲットの小型バージョンから始め、可能であれば微調整します。

<strong>投機的トークン数(γ):</strong>典型的:ラウンドあたり3~8。ワークロードに合わせて調整します。

<strong>受け入れ率の監視:</strong>本番環境でαを追跡します。α < 0.6の場合、調整またはフォールバックを検討します。

<strong>メモリ管理:</strong>GPUメモリを監視します。必要に応じて量子化またはモデル分割を使用します。

### 例:vLLM Python API

```python
from vllm import LLM, SamplingParams

llm = LLM(model="your-target-model", draft_model="your-draft-model")
params = SamplingParams(max_tokens=100, speculative_tokens=4)
output = llm.generate("Prompt text", sampling_params=params)
print(output)
```

## ユースケースと例

### 実世界のデプロイメント

<strong>Google Search AI Overviews:</strong>数十億のユーザーに高品質で低レイテンシの要約を提供します。

<strong>コード生成ツール:</strong>高速なコード補完のためにIDEアシスタントで使用されます。

<strong>エンタープライズチャットボット:</strong>ユーザーエクスペリエンスを向上させ、大量のカスタマーサポートのサービング費用を削減します。

<strong>バッチ翻訳/要約:</strong>サンプルあたりのレイテンシが高い長いドキュメントの高速出力を可能にします。

### 研究ベンチマーク

<strong>T5-XXL(11B)とT5-small(60M):</strong>翻訳タスクで2~3倍の高速化を示します。

<strong>Llama 70B:</strong>Speculative Decodingによる大幅なレイテンシ改善を報告しています。

## ベストプラクティスと調整

<strong>1. ドラフトモデルの選択:</strong>同じファミリーとトークナイザーの小型モデルを使用します。可能であれば、ユースケースに合わせて微調整します。

<strong>2. γの調整:</strong>γ=3~5から始め、αが高いままであれば増やします。

<strong>3. αの監視:</strong>αが0.5を下回る場合、γを減らすか、ドラフトモデルを再整合します。

<strong>4. メモリの最適化:</strong>必要に応じて量子化、マルチGPU、またはバッチ/コンテキストの削減を使用します。

<strong>5. ベンチマーク:</strong>実際のワークロードとハードウェアでテストします。

<strong>6. フォールバックの自動化:</strong>αまたはメモリ圧力がしきい値を超えた場合、Speculative Decodingを無効にします。

## オープンソースツールとフレームワーク

<strong>vLLM:</strong>Speculative Decodingを備えた高スループットLLM推論エンジン。

<strong>BentoML:</strong>ガイドとフレームワーク統合。

<strong>Modular MAX:</strong>設定による標準サポート。

<strong>TensorRT-LLM(Baseten):</strong>Speculative Decodingを備えた高性能デプロイメント。

## 参考文献


1. Google Research. (n.d.). Looking Back at Speculative Decoding. Google Research Blog.

2. Anonymous. (2022). Fast Inference from Transformers via Speculative Decoding. arXiv.

3. NVIDIA. (n.d.). An Introduction to Speculative Decoding for Reducing Latency in AI Inference. NVIDIA Technical Blog.

4. BentoML. (n.d.). Speculative Decoding. URL: https://bentoml.com/llm/inference-optimization/speculative-decoding

5. Baseten. (n.d.). A Quick Introduction to Speculative Decoding. Baseten Blog.

6. Stern et al. (2018). Speculative Sampling. arXiv.

7. Anonymous. (2023). Distributed Speculative Decoding. arXiv.

8. vLLM. (n.d.). Speculative Decoding. vLLM Documentation.

9. BentoML. (n.d.). Structured Decoding in vLLM: A Gentle Introduction. BentoML Blog.

10. Modular MAX. (n.d.). Speculative Decoding Documentation. URL: https://docs.modular.com/max/serve/speculative-decoding

11. vLLM Project. (n.d.). vLLM Project Repository. URL: https://github.com/vllm-project/vllm
