---
title: モデル量子化:包括的ガイド
date: 2025-11-25
translationKey: model-quantization-a
description: モデル量子化は、機械学習モデルの精度を削減(例:FP32からINT8へ)し、より小さく高速なモデルを作成します。メモリを節約し、推論を高速化し、消費電力を削減し、エッジデバイスへの展開を可能にします。
keywords:
- モデル量子化
- 機械学習
- ディープラーニング
- LLM
- AI最適化
category: AI Infrastructure & Deployment
type: glossary
draft: false
e-title: 'Model Quantization: A Comprehensive'
term: もでるりょうしか:ほうかつてきがいど
reading: モデル量子化:包括的ガイド
kana_head: ま
---
## モデル量子化とは?

モデル量子化は、機械学習モデルのパラメータ(重み)とアクティベーションの数値精度を削減するモデル最適化技術です。32ビット(FP32)や16ビット(FP16)浮動小数点数などの高精度数値を使用する代わりに、量子化はこれらの値を8ビット(INT8)や4ビット(INT4)整数、または固定小数点形式などの低精度表現にマッピングします。このプロセスにより、モデルサイズの大幅な削減、計算の高速化、消費電力の低減が実現され、リソースが限られたハードウェア(エッジデバイス、モバイルフォン、組み込みシステムなど)への展開が可能になります。

量子化は、CPU、GPU、AIアクセラレータ、さらにはIoTデバイスを含むエッジおよび組み込みハードウェア上で大規模ニューラルネットワークを効率的に実行するための重要な技術です。メモリと計算要件の両方を削減することで、量子化されたモデルは、レイテンシとリソースに制約のある環境、および高スループットのクラウド推論環境に展開できます。

**参考文献:**  
- [Hugging Face Optimum: Quantization Guide](https://huggingface.co/docs/optimum/en/concept_guides/quantization)  
- [GeeksforGeeks: Quantization in Deep Learning](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)  

### 直感的な例え

小数点付きの温度を表示するデジタル温度計(例:23.487°C)で温度を記録することを考えてみてください。おおよその温度だけが必要な場合、最も近い整数に丸めることができます(例:23°C)。量子化はニューラルネットワークに同様の原理を適用し、精密な連続値をより効率的に保存および処理できる、より小さな有限の離散値セットに丸めたりマッピングしたりします。

**出典:** [GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)

## 量子化が使用される理由

### 動機

1. **メモリ効率:**  
   低精度数値は必要なビット数が少なく、メモリフットプリントを大幅に削減します。例えば、FP32からINT8への量子化により、メモリ使用量が75%削減されます。数百億または数千億のパラメータを持つ大規模言語モデル(LLM)の場合、これは小型GPUやエッジデバイスにモデルを収めるために不可欠です。

2. **推論の高速化:**  
   整数演算は、ほとんどのハードウェアで浮動小数点演算よりも効率的です。量子化されたモデルは推論で2〜3倍の高速化を実現でき、専用アクセラレータではワットあたりのパフォーマンスが最大16倍向上します。

3. **消費電力の低減:**  
   より小さく量子化されたモデルは消費エネルギーが少なく、バッテリー駆動デバイスや持続可能性を重視した展開にとって重要な要素です。

4. **エッジおよびモバイル展開:**  
   多くのエッジデバイス(IoT、スマートフォン、ウェアラブル)は、高精度演算をサポートするハードウェアを備えていません。量子化により、リソースに制約のあるハードウェアでも高度なAIモデルを実行できます。

5. **コスト削減:**  
   計算とメモリの要件を削減することで、量子化はクラウドおよびデータセンター展開における運用コストを削減します。

#### 例

700億パラメータのLLMは、FP32精度で約280GBを必要とします。INT8への量子化により、これを約70GBに縮小できます。これにより、単一のハイエンドGPUや小型デバイスでの実行が可能になります。

**参考文献:**  
- [GeeksforGeeks: Quantization in Deep Learning](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)  
- [arXiv: A Comprehensive Study on Quantization Techniques for Large Language Models](https://arxiv.org/abs/2411.02530)

## 量子化の仕組み

量子化は、高精度値を低精度ドメインにマッピングし、通常は連続値をスケーリングして有限セットに離散化します。

### 数学的基礎

最も一般的な量子化スキームはアフィン量子化です。範囲\([a, b]\)の浮動小数点値\( x \)に対して:

**スケール(S):**  
連続浮動小数点範囲が離散整数範囲にどのようにマッピングされるかを決定します。

**ゼロポイント(Z):**  
浮動小数点のゼロを整数として正確に表現できるようにします。これはニューラルネットワークでの正確な計算に不可欠です。

- **量子化:**  
  \[
  x_q = \text{round}\left(\frac{x}{S} + Z\right)
  \]
  ここで、\(x_q\)は量子化された整数値です。

- **逆量子化:**  
  \[
  x = S \times (x_q - Z)
  \]
  ここで、\(x\)は再構築された浮動小数点値です。

参照:  
- [GeeksforGeeks: Mathematical Details](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)
- [Hugging Face Optimum: Quantization Theory](https://huggingface.co/docs/optimum/en/concept_guides/quantization)

### 対称量子化と非対称量子化

- **対称:** 整数範囲がゼロを中心としています(\(Z=0\));ゼロを中心としたデータに最適です。
- **非対称(アフィン):** \(Z\)は任意の整数にでき、浮動小数点のゼロを任意の整数に整列させることができます;偏った分布に有用です。

### テンソル単位とチャネル単位の量子化

- **テンソル単位:** 同じ\(S\)と\(Z\)がテンソル全体に適用されます(例:レイヤー内のすべての重み)。
- **チャネル単位:** 各チャネル(例:各畳み込みフィルタ)が独自の\(S\)と\(Z\)を持ちます;特に畳み込みニューラルネットワークで精度が向上します。

## 量子化の種類と技術

量子化はいくつかの方法で適用でき、それぞれ異なるトレードオフがあります。

### 1. 学習後量子化(PTQ)

学習済みモデルに量子化を適用し、再学習は行いません。

- **静的PTQ:**  
  - キャリブレーションデータセットを使用してアクティベーション範囲を推定します。
  - 推論前に重みとアクティベーションを量子化します。
  - より良い精度を提供しますが、キャリブレーションデータが必要です。

- **動的PTQ:**  
  - 重みは静的に量子化されますが、アクティベーションは推論中にその場で量子化されます。
  - キャリブレーションデータは不要です。
  - 静的よりもわずかに精度が低く遅いですが、実装が容易です。

**使用例:**  
再学習が不可能な場合やデータが限られている場合;多くのNLPトランスフォーマーモデルに適しています。

**参考文献:**  
- [GeeksforGeeks: Post-Training Quantization](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)

### 2. 量子化認識学習(QAT)

計算グラフに「疑似量子化」操作を挿入することで、モデル学習中に量子化効果をシミュレートします。モデルは量子化誤差を補償することを学習し、特に非常に低いビット幅(例:INT4)で、一般的に量子化後の精度が高くなります。

**使用例:**  
最大の精度が必要で再学習が可能な場合;コンピュータビジョンやエッジ展開シナリオでよく使用されます。

### 3. 均一量子化と非均一量子化

- **均一:** 範囲を等間隔の区間に分割します(線形マッピング)。
- **非均一:** 可変サイズの区間を使用します(例:対数スケール、k-meansクラスタリング)。データが密集している、または重要な場所により多くの精度を割り当てます。

### 4. 重みのみ、アクティベーションのみ、ハイブリッド量子化

- **重みのみ:** 重みのみが量子化され、アクティベーションは高精度のままです。
- **アクティベーションのみ:** あまり一般的ではありません;アクティベーションのみが量子化されます。
- **ハイブリッド:** 重みとアクティベーションの両方が量子化され、異なる精度になる可能性があります。

### 5. 整数のみの量子化

累積を含むすべての計算が整数演算を使用して実行されます。これは、浮動小数点サポートがないハードウェアアクセラレータにとって重要です。

### 6. 高度で専門的な技術

- **GPTQ(勾配学習後量子化):** トランスフォーマー用のレイヤー単位の量子化で、元の出力と量子化された出力の間の平均二乗誤差を最小化します。多くの場合、混合INT4/FP16精度を使用します。
- **QLoRA(量子化低ランク適応):** 低ランク適応(LoRA)と量子化を組み合わせ、LLMの効率的なファインチューニングを可能にします。
- **ZeroQAT、FlatQuant:** 精度損失を最小限に抑えてLLMを量子化するための最近の研究手法です。

**参考文献:**  
- [arXiv: A Comprehensive Study on Quantization Techniques for Large Language Models](https://arxiv.org/abs/2411.02530)  
- [GeeksforGeeks: QLoRA & GPTQ](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)

## ステップバイステップの例:大規模言語モデルの量子化

以下は、[Hugging Face](/en/glossary/hugging-face/) TransformersとBitsAndBytesを使用したTinyLlamaモデルの4ビット量子化(QLoRA)の実用的なワークフローです:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# ステップ1:モデル選択
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# ステップ2:量子化設定
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",   # NormalFloat4
    bnb_4bit_compute_dtype=torch.float16
)

# ステップ3:モデルとトークナイザーの読み込み
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

# ステップ4:推論の例
def ask_question(question, max_new_tokens=128):
    prompt = f"<|system|>\nYou are a helpful assistant.<|user|>\n{question}<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "<|assistant|>" in response:
        response = response.split("<|assistant|>")[-1].strip()
    return response

print(ask_question("What are the advantages of 4-bit quantization in LLMs?"))
```

**参考文献:**  
- [Hugging Face BitsAndBytes Quantization](https://huggingface.co/docs/transformers/en/quantization/bitsandbytes)  
- [Hugging Face Optimum Quantization](https://huggingface.co/docs/optimum/en/concept_guides/quantization)

## 課題とトレードオフ

### 1. 精度損失

精度を削減すると量子化誤差が発生し、特に敏感なレイヤー(例:トランスフォーマーのアテンションメカニズム)でパフォーマンスが低下する可能性があります。QATと高度なキャリブレーションがこれを軽減するのに役立ちます。

### 2. 外れ値への感度

大きな外れ値は量子化範囲を歪め、一般的な値を忠実に表現することを困難にします。外れ値チャネル分割やパーセンタイルキャリブレーションなどの技術がこれに対処します。

### 3. キャリブレーションの複雑さ

各レイヤーまたはチャネルに適切なスケールとゼロポイントパラメータを選択することは簡単ではありません。不適切なキャリブレーションは深刻な精度低下につながる可能性があります。

### 4. ハードウェアの制約

すべてのハードウェアがすべての量子化タイプ(例:INT4、INT8、FP8)をサポートしているわけではありません。最適な高速化のために、量子化スキームはハードウェア機能と一致する必要があります。

### 5. 公平性とバイアス

不適切なキャリブレーションや量子化は、特にキャリブレーションデータが代表的でない場合、バイアスを導入または増幅する可能性があります。

**参考文献:**  
- [arXiv: A Comprehensive Study on Quantization Techniques for Large Language Models](https://arxiv.org/abs/2411.02530)  
- [Hugging Face Optimum Quantization](https://huggingface.co/docs/optimum/en/concept_guides/quantization)

## アプリケーションと使用例

### 1. エッジおよび組み込みデバイス
スマートフォン、IoTセンサー、ドローン、ウェアラブルでのビジョンモデル、音声認識、LLMの展開。

### 2. ヘルスケア
リアルタイム分析のためのポータブル医療機器での診断モデルの実行。

### 3. 自動運転車
リアルタイムの物体検出とセンサーフュージョンには、組み込みハードウェアでの高速で効率的な推論が必要です。

### 4. 音声アシスタント
量子化されたニューラルネットワークは、Alexa、Siri、Google Assistantなどの製品でのデバイス上音声認識と自然言語理解を支えています。

### 5. 産業用IoT
厳格な[レイテンシ](/en/glossary/latency/)と電力要件を持つ異常検知、予知保全、制御システム。

### 6. クラウド推論の高速化
クラウド内の大規模LLMとレコメンダーシステムは、メモリ帯域幅の削減と高速サービングの恩恵を受けます。

#### 例の表:量子化の効果

| 精度 | モデルサイズ削減 | 高速化 | 精度低下(典型的) |
|------|-----------------|--------|-----------------|
| FP32 | 1倍             | 1倍    | なし            |
| FP16 | 2倍             | 1.5〜2倍 | <0.5%         |
| INT8 | 4倍             | 2〜3倍  | <1%            |
| INT4 | 8倍             | 3〜5倍  | 1〜2%(QAT/高度な手法使用時) |

**参考文献:**  
- [GeeksforGeeks: Quantization in Deep Learning](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)  
- [arXiv: A Comprehensive Study on Quantization Techniques for Large Language Models](https://arxiv.org/abs/2411.02530)

## ハードウェアとフレームワークのサポート

### ハードウェア

- **CPU:**  
  最新のCPUのほとんどがINT8をサポートし、INT4操作も増えています(例:Intel AVX-512 VNNI、AMD Zen4、Apple Silicon、ARM NEON)。
- **GPU:**  
  NVIDIA(Tensor Cores、Hopper FP8)、AMD(Radeon AI)、Apple Neural Engineがさまざまな量子化形式をサポートしています。
- **AIアクセラレータ:**  
  Google Edge TPU、Intel Gaudi、AWS Inferentia、Qualcomm Hexagon、モバイル/エッジデバイス用の専用AIチップ。
- **FPGA/ASIC:**  
  カスタムハードウェアは、柔軟な量子化(ユーザー指定のビット幅)をサポートすることがよくあります。

### フレームワーク

- **PyTorch:**  
  ネイティブ量子化API(QAT/PTQを含む)、[torch.quantization](https://pytorch.org/docs/stable/quantization.html)、INT8/FP16のサポート。
- **TensorFlow Lite:**  
  学習後量子化とエッジ展開に焦点を当てています。
- **ONNX Runtime:**  
  クロスプラットフォームで、量子化拡張機能付き。
- **Hugging Face Optimum:**  
  TransformersとONNXの量子化を統合:[Optimum Quantization](https://huggingface.co/docs/optimum/en/concept_guides/quantization)
- **BitsAndBytes:**  
  LLMと4ビット/8ビット量子化に焦点を当てています:[BitsAndBytes Quantization](https://huggingface.co/docs/transformers/en/quantization/bitsandbytes)

## 用語集:主要な量子化用語

- **ビット幅:** 各値を表すために使用されるビット数(例:INT8の場合は8)。
- **キャリブレーションデータセット:** 量子化のためのアクティベーション範囲を推定するために使用される代表的なサンプルのセット。
- **スケール(S):** 浮動小数点範囲を整数範囲にマッピングするために使用される係数。
- **ゼロポイント(Z):** 浮動小数点空間のゼロに対応する整数値。
- **動的量子化:** 推論時に決定される量子化パラメータ。
- **静的量子化:** キャリブレーションを使用して事前計算された量子化パラメータ。
- **量子化認識学習(QAT):** シミュレートされた量子化効果を使用してモデルを学習すること。
- **チャネル単位の量子化:** 各チャネルに個別の量子化パラメータ。
- **学習後量子化(PTQ):** 事前学習済みモデルに量子化を適用すること。
- **整数のみの量子化:** すべての操作(累積を含む)が整数演算を使用すること。
- **均一/非均一量子化:** 量子化区間が等しいサイズかどうか。
- **アフィン量子化:** スケールとゼロポイントを使用した浮動小数点から整数への線形マッピング。
- **対称量子化:** ゼロを中心とした整数範囲。
- **非対称量子化:** 必ずしもゼロを中心としない整数範囲。

**さらなる読み物:**  
- [Hugging Face Quantization Glossary](https://huggingface.co/docs/optimum/en/concept_guides/quantization)  
- [arXiv: Quantization for LLMs](https://arxiv.org/abs/2411.02530)

## 参考文献とさらなる読み物

- [Hugging Face Optimum: Quantization Guide](https://huggingface.co/docs/optimum/en/concept_guides/quantization)
- [IBM: What is Quantization?](https://www.ibm.com/think/topics/quantization)
- [DigitalOcean: Model Quantization in LLMs](https://www.digitalocean.com/community/tutorials/model-quantization-large-language-models)
- [Clarifai: Model Quantization – Meaning, Benefits & Techniques](https://www.clarifai.com/blog/model-quantization)
- [GeeksforGeeks: Quantization in Deep Learning](https://www.geeksforgeeks.org/deep-learning/quantization-in-deep-learning/)
- [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference (arXiv)](https://arxiv.org/abs/1712.05877)
- [Lei Mao's Blog: Neural Networks Quantization](https://leimao.github.io/article/Neural-Networks-Quantization/)
- [arXiv: A Comprehensive Study on Quantization Techniques for Large Language Models](https://arxiv.org/abs/2411.02530)
- [Hugging Face BitsAndBytes Quantization](https://huggingface.co/docs/transformers/en/quantization/bitsandbytes)

## Q&Aの例

**Q: モデル量子化とは何ですか?**  
A: モデル量子化は、モデルのパラメータとアクティベーションの数値精度を削減するプロセスです。通常、高精度浮動小数点(例:FP32)から低精度整数(例:INT8)に変換し、モデルサイズ、計算要件、メモリ使用量を削減します。