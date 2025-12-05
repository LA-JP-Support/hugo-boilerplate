---
title: 用語集:PagedAttentionとLLM推論のための高度なメモリ管理
date: 2025-11-25
translationKey: glossary-pagedattention-and-advanced-memory-management-for-llm-inference
description: PagedAttentionは、LLMのKVキャッシュを固定サイズのブロックに分割するメモリ管理アルゴリズムで、推論時のGPUメモリの無駄を削減し、vLLMを支える技術です。
keywords:
- PagedAttention
- LLM推論
- KVキャッシュ
- vLLM
- メモリ管理
category: LLM Inference
type: glossary
draft: false
e-title: 'Glossary: PagedAttention and Advanced Memory Management for LLM Inference'
term: ようごしゅう ぺーじどあてんしょん と えるえるえむすいろん の ための こうど な めもりかんり
reading: 用語集:PagedAttentionとLLM推論のための高度なメモリ管理
kana_head: その他
---
## PagedAttention

PagedAttentionは、大規模言語モデル(LLM)のKey-Value(KV)キャッシュを固定サイズのブロック(「ページ」)に分割し、非連続的な割り当てを可能にすることで、推論時のGPUメモリの無駄を劇的に削減するメモリ管理アルゴリズムです。この手法はKwonらによる論文["Efficient Memory Management for Large Language Model Serving with PagedAttention"](https://arxiv.org/abs/2309.06180)で発表され、[vLLM](https://github.com/vllm-project/vllm)推論エンジンの基盤となっています。

**主な特徴:**
- KVキャッシュは、大きな連続バッファではなく、小さな固定サイズのブロック(ページ)に分割されます。
- 各シーケンスは、ブロックテーブル(ページテーブル)を介して論理-物理メモリマッピングを追跡します。
- シーケンスのブロックはメモリ全体に分散配置でき、内部および外部フラグメンテーションの両方を削減します。
- メモリはシーケンス間で共有可能で、効率的な並列サンプリングと高度なデコーディングを実現します。
- オンデマンド割り当てとプロンプトブロックの再利用により、メモリ不足(OOM)エラーを防止します。

**技術概要とビジュアル:**  
- 従来のLLMサービングでは、各リクエストのKVキャッシュは単一の連続チャンクとして事前割り当てされるため、シーケンスが短い場合やバッチサイズ/シーケンス長が変動する場合に大きなメモリの無駄が生じます。
- PagedAttentionは、OSの仮想メモリページングに着想を得て、シーケンスが必要な分だけメモリを使用できるようにし、ほぼ最適な利用率を実現します([vLLMブログ](https://blog.vllm.ai/2023/06/20/vllm.html)、[Hopsworks辞書](https://www.hopsworks.ai/dictionary/pagedattention))。

> アニメーション図とより詳細な説明については、公式[vLLMブログ](https://blog.vllm.ai/2023/06/20/vllm.html)をご覧ください。

## KVキャッシュ

Key-Value(KV)キャッシュは、トランスフォーマーベースのLLM推論の中核コンポーネントです。各デコーディングステップで、モデルは各トークンに対してキーと値のテンソルを生成し、アテンションメカニズムのためのコンテキスト関係をエンコードします。

- **目的:** 事前計算されたアテンションキーと値を保存することで、モデルがすべてのトークンに対してそれらを再計算する必要をなくし、推論を大幅に高速化します。
- **サイズ:** LLaMA-13Bのようなモデルでは、単一シーケンスのKVキャッシュは1.7GBに達することがあり、[バッチ処理](/en/glossary/batch-processing/)と長いシーケンスの場合、合計キャッシュサイズは40GBに達することがあります([出典](https://arxiv.org/pdf/2309.06180)、[Hopsworks](https://www.hopsworks.ai/dictionary/pagedattention))。
- **課題:** キャッシュは大きく動的です—そのサイズはアクティブなシーケンスの数、その長さ、バッチサイズに依存します。
- **影響:** 非効率なKVキャッシュ管理は、並列処理できるリクエスト数を大幅に制限し、コストを増加させ、ハードウェア利用率を低下させます。

LLMにおけるKVキャッシュの役割と最適化の詳細については、["KV Cache Optimization: A Deep Dive"](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8)をご覧ください。

## メモリフラグメンテーション

フラグメンテーションとは、硬直的な割り当てと解放スキームによる利用可能メモリの非効率的な使用を指し、GPU上のLLM推論における重要な問題です。

### 内部フラグメンテーション

事前割り当てされたメモリブロックがシーケンスが実際に必要とするメモリよりも大きい場合に発生し、割り当ての「内部」に未使用スペースが残ります。

- **例:** 各シーケンスに2048トークン分のスペースが割り当てられているが、実際には200しか使用しない場合、残りは無駄になります。
- **深刻度:** 従来のLLMサービングシステムは、内部フラグメンテーションによりGPUメモリの最大80%を無駄にする可能性があります([arXiv論文、図2](https://arxiv.org/pdf/2309.06180)、[Doubleword技術ガイド](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention))。

### 外部フラグメンテーション

さまざまな長さのシーケンスが開始および終了するにつれて発生します。空きメモリは、新しい割り当てに使用するには小さすぎる、小さな非連続チャンクに分散します。

- **結果:** 合計空きメモリが十分であっても、連続スペースの不足により新しいリクエストに使用できません。

PagedAttentionは、OSの仮想メモリページングと同様に、小さなブロックをオンデマンドで割り当てと解放することで、両方のタイプのフラグメンテーションを排除します([Red Hat開発者記事](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems))。

## 仮想メモリとページング

PagedAttentionでLLMに適用された古典的なオペレーティングシステムの概念です。

- **仮想メモリ:** 論理メモリアドレス(プロセス/シーケンスが使用)を物理メモリ位置から分離し、非連続ストレージと効率的な割り当てを可能にします。
- **ページング:** メモリは小さな固定サイズのページ(ブロック)に分割されます。論理ページはページテーブルを介して物理メモリにマッピングされます。
- **LLMサービングにおいて:** 各シーケンスのKVキャッシュはブロックに分割され、各ブロックはGPUメモリのどこにでも配置できます。シーケンスは、論理トークン位置を物理メモリブロックにマッピングするブロックテーブルを保持します。

この抽象化は以下をサポートします:
- オンデマンド割り当て
- 解放されたブロックの即座の再利用
- シーケンス間のメモリ共有(変更時のコピーオンライト)

技術的背景については:["Operating Systems: Three Easy Pieces" (Virtual Memory)](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-intro.pdf)。

## ブロックテーブル(ページテーブル)

PagedAttentionによって維持される、シーケンス内のトークンの論理的順序を実際の物理メモリブロックにマッピングするデータ構造です。

- **目的:** 各シーケンスが、ブロックが物理的にどこに保存されているかに関係なく、アテンション計算のためにコンテキストを再構築できるようにします。
- **機能:** トークンが生成されたりシーケンスが終了したりする際の、ブロックの高速ルックアップと割り当て/解放をサポートします。
- **オーバーヘッド:** ルックアップテーブルは小さな計算オーバーヘッドを導入しますが、メモリ無駄の削減がこのコストをはるかに上回ります([arXiv論文、セクション4.1](https://arxiv.org/pdf/2309.06180))。

## メモリ共有

PagedAttentionは、シーケンスとリクエスト間でメモリブロックを共有できるようにし、特に並列サンプリングと高度なデコーディングに有益です。

### 並列サンプリング

- **ユースケース:** 同じプロンプトから複数の補完を生成します。
- **利点:** プロンプトのKVキャッシュブロックはすべての出力間で共有され(複製されず)、メモリ使用量を削減し、より高いスループットを実現します([vLLMブログ、並列サンプリング図](https://blog.vllm.ai/2023/06/20/vllm.html))。
- **技術的メカニズム:** 各サンプルのブロックテーブルは、シーケンスの共有部分について同じ物理ブロックを指します。

### ビームサーチと混合デコーディング

- **ビームサーチ:** 複数のビームは同じプレフィックスを共有することが多く、PagedAttentionはプレフィックスブロックをビーム間で共有できるようにします。
- **混合デコーディング:** 貪欲法、サンプリング、ビームサーチ戦略を持つリクエストを、冗長なメモリ割り当てなしで同時に処理します。

## コピーオンライト

共有メモリブロックの安全な変更を保証するメモリ管理技術です。

- **仕組み:** シーケンスが共有されているブロック(複数の参照)を変更する必要がある場合、そのシーケンスのみに新しいコピーが作成されます。他のシーケンスは元のブロックを参照し続けます。
- **利点:** データ破損や競合状態のリスクなしにメモリ共有を可能にします。
- **参照カウント:** 各ブロックは何個のシーケンスがそれを参照しているかを追跡し、書き込みが必要でカウント > 1の場合にコピーをトリガーします([vLLMブログ、アニメーション](https://blog.vllm.ai/2023/06/20/vllm.html))。

## ページングを使用したアテンション計算

従来のアテンションカーネルは、キーと値のための連続メモリ領域を期待します。PagedAttentionは、ブロックテーブルで指定された非連続ブロックからキーと値を効率的に取得できるカスタムアテンションカーネルを導入します。

- **実装:** 各推論ステップで、カーネルはブロックテーブルを参照して、潜在的に分散したブロックから必要なすべてのキーと値のベクトルを収集します([arXivセクション4.1](https://arxiv.org/pdf/2309.06180))。
- **パフォーマンス:** わずかな計算オーバーヘッドですが、無駄なメモリの大幅な削減と対応するスループットの向上があります。

## vLLM

[vLLM](https://github.com/vllm-project/vllm)は、UC Berkeleyで開発されたオープンソースの高性能LLM推論およびサービングエンジンです。PagedAttentionをコアメモリ管理アルゴリズムとして実装しています。

- **主な特徴:**
    - 最先端のスループット(HuggingFace Transformersの最大24倍)
    - 劇的に低いメモリ無駄(60〜80%から4%未満へ)
    - 大規模バッチサイズ、長いシーケンス、高度なデコーディングのサポート
    - HuggingFaceモデル、PyTorch、OpenAI APIとの互換性
    - LMSYS Chatbot Arena、Databricks、Dropbox、AWS、AMD、NVIDIAなどで使用

ベンチマークとデプロイメントガイドについては、[vLLMドキュメント](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)をご覧ください。

## 実装の詳細と使用方法

PagedAttentionは[vLLM](https://github.com/vllm-project/vllm)を介してアクセスできます。  
**インストール:**
```bash
pip install vllm
```
**モデルの実行:**
```bash
python -m vllm.entrypoints.openai.api_server --model <model_name>
```
- `<model_name>`を任意の[サポートされているモデル](https://docs.vllm.ai/en/latest/models/supported_models.html)に置き換えてください。

**主な使用シナリオ:**
- 高スループットチャットボット(例:Chatbot Arena)
- バッチドキュメント/質問サービング
- 並列サンプリングとビームサーチ
- 混合デコーディングワークロード
- エッジおよびリソース制約のあるデプロイメント

サーバーレスデプロイメントについては、[Runpodガイド](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention)をご覧ください。

**サポートされているモデル:**  
クラシックトランスフォーマー(Llama、GPT-2、GPT-J)、Mixture-of-Experts(Mixtral、Qwen2MoE)、マルチモーダルLLM(LLaVA、StableLM)。[完全なリスト](https://docs.vllm.ai/en/latest/models/supported_models.html)。

## 技術ベンチマークと業界での採用

**定量的改善:**
- スループット:HuggingFace Transformersの最大24倍、TGIの3.5倍([vLLMブログ](https://blog.vllm.ai/2023/06/20/vllm.html))
- メモリ無駄:60〜80%から4%未満に削減([Doubleword](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention))
- LMSYS Chatbot Arena:1秒あたり2〜3倍のリクエスト、GPU使用量50%削減([Runpodブログ](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention))

**実世界での使用:**
- LMSYS Chatbot Arena、Databricks、Dropbox、AWS、AMD、NVIDIA、Roblox、および数千人の開発者。
- [オープンソースエコシステム](https://github.com/vllm-project/vllm):GitHubスター数20,000以上、アクティブなコミュニティ、頻繁な更新。

## 参考文献とさらなる読み物

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (arXiv論文)](https://arxiv.org/abs/2309.06180)
- [vLLMブログ:Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html)
- [Hopsworks辞書:PagedAttention](https://www.hopsworks.ai/dictionary/pagedattention)
- [Doubleword:Optimizing GPU Memory for LLMs – Deep Dive](https://www.doubleword.ai/resources/optimizing-gpu-memory-for-llms-a-deep-dive-into-paged-attention)
- [Runpodブログ:Introduction to vLLM and PagedAttention](https://www.runpod.io/blog/introduction-to-vllm-and-pagedattention)
- [KV Cache Optimization:Medium Deep Dive](https://medium.com/foundation-models-deep-dive/kv-cache-guide-part-4-of-5-system-superpowers-framework-realities-kv-cache-in-action-6fb4fb575cf8)
- [Red Hat Developer:How PagedAttention resolves memory waste of LLM systems](https://developers.redhat.com/articles/2025/07/24/how-pagedattention-resolves-memory-waste-llm-systems)
- [YouTube:vLLM/PagedAttention Technical Explanation](https://www.youtube.com/watch?v=5ZlavKF_98U&t=351s)
- [vLLMドキュメント](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)

*最新のガイド、コミュニティサポート、更新情報については、[vLLM on GitHub](https://github.com/vllm-project/vllm)および[公式ドキュメント](https://docs.vllm.ai/en/latest/)をご覧ください。*