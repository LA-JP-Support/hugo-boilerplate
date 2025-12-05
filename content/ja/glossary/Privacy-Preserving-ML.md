---
title: プライバシー保護機械学習(PPML)
date: 2025-11-25
translationKey: privacy-preserving-machine-learning-ppml
description: プライバシー保護機械学習(PPML)について探求します。差分プライバシー、準同型暗号、マルチパーティ計算、連合学習などの手法を用いて、機械学習モデルにおける機密データを保護する方法を解説します。
keywords: ["プライバシー保護機械学習", "差分プライバシー", "準同型暗号", "マルチパーティ計算", "連合学習"]
category: Machine Learning
type: glossary
draft: false
e-title: Privacy-Preserving Machine Learning (PPML)
term: プライバシーほごきかいがくしゅう(ピーピーエムエル)
reading: プライバシー保護機械学習(PPML)
kana_head: は
---
# プライバシー保護機械学習(PPML)とは何か?

プライバシー保護機械学習(PPML)は、基盤となる機密データを公開することなく、機械学習モデルのトレーニング、デプロイメント、使用を可能にするように設計された一連の手法とシステムアーキテクチャを包括する用語です。PPMLは、個人識別情報(PII)、健康記録、財務詳細、または企業の機密情報などの個々のデータポイントが、敵対者がモデルやその出力に大幅なアクセス権を持っている場合でも、漏洩、再構築、または再識別されないことを保証します。

PPMLの中核となる技術には、**差分プライバシー**、**準同型暗号**、**マルチパーティ計算(MPC)**、**連合学習**が含まれます。これらの手法により、組織は[EU一般データ保護規則(GDPR)](https://gdpr-info.eu/)、HIPAA、CCPAなどの厳格なプライバシー規制に準拠しながら、機械学習の力を活用できます。
- 詳細な紹介:[Microsoft Research – Privacy Preserving Machine Learning](https://www.microsoft.com/en-us/research/blog/privacy-preserving-machine-learning-maintaining-confidentiality-and-preserving-trust/)
- 調査と分類:[arXiv: Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417)

## 機械学習においてプライバシーが重要な理由

### 機密データの露出

機械学習は大規模なデータセットに依存しており、多くの場合、非常に機密性の高い情報が含まれています。プライバシー保護の保護措置がなければ、このデータは以下を通じて露出される可能性があります:
- データの取り込み、前処理、またはトレーニング中の生データへの直接アクセス。
- 特に過学習や記憶が発生する可能性のあるディープラーニング環境において、トレーニング済みモデルを介した間接的な漏洩。
- APIまたはモデル出力を通じた推論中の不正アクセス。

### モデル漏洩リスク

研究により、トレーニング済みモデルは、モデルAPIへのアクセスが制限されている場合でも、トレーニングデータを無意識に記憶し漏洩する可能性があることが示されています。攻撃者は、メンバーシップ推論、モデル反転、またはトレーニングデータ抽出技術を使用して、これらの脆弱性を悪用する可能性があります。
- [Model Extraction and Membership Inference Attacks](https://arxiv.org/pdf/1804.11238)

### 規制遵守

[GDPR](https://gdpr-info.eu/)、米国のHIPAAなどの法律は、PIIやその他の機密データの収集、処理、共有方法を厳格に規制しています。非遵守は、深刻な法的および財政的罰則をもたらす可能性があります。

### 協調的MLとデータサイロ

医療や金融などのセクターでは、データは組織間でサイロ化されていることがよくあります。PPMLは、データの所有権やコンプライアンスを損なうことなく、協調的な分析とモデル構築を可能にします。
- [ScienceDirect: Privacy Preserving Machine Learning](https://www.sciencedirect.com/topics/computer-science/privacy-preserving-machine-learning)

## プライバシー保護MLはどのように使用されるか?

PPML技術は、MLライフサイクル全体に統合されています:

- **データ収集:** データはトレーニングパイプラインに入る前に匿名化または仮名化されます。暗号技術が安全な集約に使用される場合があります。
- **モデルトレーニング:** プライバシー保護アルゴリズム(例:DP、MPC、HE)により、トレーニング済みモデルが個々のレコードを漏洩できないことが保証されます。
- **モデル推論:** 暗号化推論やアクセス制御などの技術により、機密性の高いユーザー入力と出力が不正な露出から保護されます。
- **モデル共有とデプロイメント:** PPMLメカニズムにより、第三者とモデルを共有したり、クラウド/エッジにデプロイしたりしても、プライバシー侵害が発生しないことが保証されます。

フェーズと保証の構造化された概要については、[arXiv: Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417)を参照してください。

## 主要なPPML技術

### 1. 差分プライバシー(DP)

**定義:**  
差分プライバシーは、計算またはモデルがデータセット内の単一のデータポイントについて明らかにする情報を定量化し制限する、数学的に厳密なフレームワークです。
- 「メカニズムは、単一のデータポイントの削除または追加が出力に大きな影響を与えない場合、差分プライベートです。」([Wikipedia: Differential Privacy](https://en.wikipedia.org/wiki/Differential_privacy))

**メカニズム:**  
- **ノイズ注入:** データクエリまたはモデル更新にランダムノイズが追加され、個々のレコードの存在または不在を統計的に推測することが困難になります。
- **プライバシー予算(ε):** プライバシーと有用性のトレードオフを制御します。εが低いほど、プライバシーが強化されます(ただし有用性は低下します)。
- **合成:** プライバシー損失は複数のクエリまたはエポックにわたって累積されます。慎重な会計処理が必要です。

**主要な特性:**
- 証明可能で定量化可能なプライバシー保証。
- 補助情報を持つ攻撃者に対する耐性。
- 業界で広く採用されています(例:Google Chromeのテレメトリ、AppleのiOS、Microsoft Windows)。

**制限事項:**
- 特に低εでモデルの精度が低下する可能性があります。
- 反復的またはストリーミングタスクの複雑なプライバシー会計処理。
### 2. 準同型暗号(HE)

**定義:**  
暗号化されたデータに対して直接計算を可能にする暗号技術であり、復号化された結果が平文で計算を実行した結果と一致します。
- 「HEは暗号文に対する加算および/または乗算をサポートし、プライバシー保護のアウトソース計算を可能にします。」([Nightfall AI: Homomorphic Encryption](https://www.nightfall.ai/ai-security-101/homomorphic-encryption))

**タイプ:**
- **部分準同型暗号(PHE):** 1つの演算(加法または乗法)のみをサポート。
- **やや準同型暗号(SHE):** 限定的な演算をサポート。
- **完全準同型暗号(FHE):** 暗号文に対する任意の計算をサポート。

**MLでの応用:**
- データ所有者が機密データを暗号化し、トレーニングまたは推論のためにサーバーと共有します。
- サーバーは暗号化されたデータを操作します。所有者のみが結果を復号化できます。

**強み:**
- データはエンドツーエンドで暗号化されたままです。生データの露出はありません。
- 計算の安全なアウトソーシング(クラウドまたは第三者)を可能にします。

**制限事項:**
- 計算集約的(特にFHE)。
- シンプルなモデルに実用的。効率を改善する研究が活発に行われています。
### 3. マルチパーティ計算(MPC)

**定義:**  
複数の当事者が、それらの入力を互いに明らかにすることなく、プライベート入力に対する関数を共同で計算できるようにする暗号アプローチ。
- 「MPCプロトコルは、分散データに対する計算を可能にし、相互に不信な当事者間でもプライバシーを保証します。」([GeeksforGeeks: Secure Multiparty Computation](https://www.geeksforgeeks.org/blogs/what-is-secure-multiparty-computation/))

**仕組み:**
- 各当事者がデータを暗号化または秘密分散します。
- ガーブルド回路やシャミアの秘密分散などのプロトコルを使用して共同計算が実行されます。
- 結果のみが明らかにされます。個々の入力は秘密のままです。

**使用例:**
- 顧客データを公開せずに銀行間で協調的な不正検出。
- 病院間での安全な医療分析。

**強み:**
- 多様なMLシナリオに対応する柔軟なプロトコル設計。
- 敵対的な環境でも強力なプライバシー。

**制限事項:**
- 計算および通信のオーバーヘッドの増加。
- 参加者間の同期が必要。
### 4. 連合学習(FL)

**定義:**  
分散型デバイスまたは組織間でモデルが協調的にトレーニングされる分散MLパラダイムであり、生データを中央に集約しません。
- 「連合学習により、分散データでモデルをトレーニングでき、プライバシーが強化され、データ転送が削減されます。」([IBM Research: What is Federated Learning?](https://research.ibm.com/blog/what-is-federated-learning))

**仕組み:**
- グローバルモデルがローカルノード(デバイス、組織)に配布されます。
- 各ノードはローカルデータでモデルをトレーニングし、モデル更新(データではなく)のみを中央サーバーに送信します。
- サーバーは更新を集約してグローバルモデルを改良します。

**強み:**
- 生データはデバイスまたは組織を離れません。
- 大規模な実世界のデプロイメント(例:モバイルキーボード、医療)をサポート。

**制限事項:**
- モデル更新は依然として情報を漏洩する可能性があります。多くの場合DPと組み合わせられます。
- 非IIDデータ、信頼性の低い接続、遅延ノードが課題となります。
## PPMLにおける脅威モデルと攻撃タイプ

### 一般的な脅威モデル

- **正直だが好奇心旺盛な敵対者:** プロトコルに従いますが、プライベートデータを推測しようとします。
- **悪意のある敵対者:** データを抽出または汚染するためにプロトコルから逸脱します。
- **外部攻撃者:** モデルまたは通信から機密情報を抽出しようとします。

### 特定の攻撃タイプ

- **メンバーシップ推論攻撃:**  
  攻撃者が特定のデータサンプルがトレーニングで使用されたかどうかを判断します([Shokri et al., 2017](https://ieeexplore.ieee.org/document/7958568)を参照)。
- **モデル反転攻撃:**  
  モデル出力または勾配から入力特徴またはデータを再構築します。
- **トレーニングデータ抽出:**  
  特にLLMから、モデルから逐語的またはほぼ逐語的なトレーニングデータを抽出します。
- **汚染攻撃:**  
  漏洩または誤ったモデル動作を誘発するためのトレーニングデータの悪意のある操作。([Property Inference from Poisoning](https://arxiv.org/pdf/2101.11073.pdf))
- **モデル更新攻撃:**  
  更新前後のモデル状態を比較することで機密データを推測します([Analyzing Information Leakage of Updates to Natural Language Models](https://www.microsoft.com/en-us/research/publication/analyzing-information-leakage-of-updates-to-natural-language-models/))。

**参考文献と詳細調査:**
- [arXiv: Privacy Preserving Machine Learning: Threats and Solutions](https://arxiv.org/pdf/1804.11238)
- [ScienceDirect: Privacy Preserving Machine Learning](https://www.sciencedirect.com/topics/computer-science/privacy-preserving-machine-learning)
- [Tandfonline: Privacy Threats in Machine Learning](https://www.tandfonline.com/doi/full/10.1080/19361610.2025.2562401?src=)

## 業界のデプロイメント、ツールキット、フレームワーク

### 業界のデプロイメント

- **Microsoft**  
    - [Officeでのパーソナライズされたテキスト予測](https://insider.office.com/en-us/blog/text-predictions-in-word-outlook)
    - [差分プライバシーを使用したWindowsテレメトリ](https://www.microsoft.com/en-us/research/publication/collecting-telemetry-data-privately/)
    - [Viva Insights: DP従業員分析](https://docs.microsoft.com/en-us/viva/insights/Privacy/differential-privacy)
    - [CryptFlowを使用した安全な医療画像分析](https://www.microsoft.com/en-us/research/publication/secure-medical-image-analysis-with-cryptflow/)
- **医療:**  
    - 協調的な診断モデル構築のための連合学習([IBM Research – Federated Learning](https://research.ibm.com/blog/what-is-federated-learning))
- **金融:**  
    - 銀行間でMPCを使用した不正検出モデル。

### ツールキットとフレームワーク

- **[ScienceDirect: Preserving data privacy in machine learning systems](https://www.sciencedirect.com/science/article/pii/S0167404823005151):** TensorFlow用の差分プライバシーツール。
- **[IRJET: PPML Techniques, Challenges and Research Directions (PDF)](https://www.irjet.net/archives/V11/i3/IRJET-V11I360.pdf):** PyTorch/TensorFlow用の連合学習、DP、MPC。
- **[Differentially private fine-tuning of language models](https://www.microsoft.com/en-us/research/publication/differentially-private-fine-tuning-of-language-models/):** 準同型暗号ライブラリ。
- **[Private Synthetic Data for Generative AI](https://www.microsoft.com/en-us/research/blog/the-crossroads-of-innovation-and-privacy-private-synthetic-data-for-generative-ai/):** MLコード用のMPCコンパイラ。
- **[Azure Confidential Computing](https://azure.microsoft.com/en-us/solutions/confidential-compute/):** プライバシーリスク評価ツールキット。
- **[EU Trustworthy AI](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence):** 一般的なプライバシー保護MLフレームワーク。
- **[ResearchGate: PPML Techniques, Challenges And Research Directions](https://www.researchgate.net/publication/379244515_Privacy-Preserving_Machine_Learning_Techniques_Challenges_And_Research_Directions):** キュレーションされたリソースリスト。

## トレードオフと制限事項

- **有用性 vs. プライバシー:**  
  より厳格なプライバシー(低ε、より強力な暗号化)は、モデルの精度を低下させ、および/またはノイズを増加させます。
- **計算オーバーヘッド:**  
  暗号技術(HE、MPC)は、特に大規模モデルではリソース集約的です。
- **使いやすさ:**  
  既存のMLワークフローへの統合には、大幅な変更が必要になる場合があります。
- **脅威カバレッジ:**  
  単一の手法ですべての攻撃タイプをカバーすることはできません。多層防御が推奨されます。

**詳細なトレードオフ分析:**  
- [ScienceDirect: Preserving data privacy in machine learning systems](https://www.sciencedirect.com/science/article/pii/S0167404823005151)
- [IRJET: PPML Techniques, Challenges and Research Directions (PDF)](https://www.irjet.net/archives/V11/i3/IRJET-V11I360.pdf)

## 進行中の研究と将来の方向性

- **高度な差分プライバシー:**  
  より正確なプライバシー会計処理と効率的なプライベートファインチューニング([Differentially private fine-tuning of language models](https://www.microsoft.com/en-us/research/publication/differentially-private-fine-tuning-of-language-models/))。
- **プライベート合成データ:**  
  実際のレコードを漏洩させることなく、生成AIのための高忠実度合成データ([Private Synthetic Data for Generative AI](https://www.microsoft.com/en-us/research/blog/the-crossroads-of-innovation-and-privacy-private-synthetic-data-for-generative-ai/))。
- **連合学習の進歩:**  
  非IIDデータの処理、敵対的堅牢性、DP/HE統合。
- **機密コンピューティング:**  
  スケーラブルな安全なMLのためのハードウェアベースの信頼実行環境(TEE)([Azure Confidential Computing](https://azure.microsoft.com/en-us/solutions/confidential-compute/))。
- **形式的検証:**  
  MLパイプライン全体にわたるエンドツーエンドのプライバシー保証。
- **ポリシーと規制の整合性:**  
  技術的プライバシー保証をコンプライアンスに変換([EU Trustworthy AI](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence))。

**研究調査:**  
- [ResearchGate: PPML Techniques, Challenges And Research Directions](https://www.researchgate.net/publication/379244515_Privacy-Preserving_Machine_Learning_Techniques_Challenges_And_Research_Directions)

## 主要用語の用語集

| **用語**              | **定義**                                                                                                                                                      |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 差分プライバシー  | 単一のデータポイントの削除または追加が計算の出力に大きな影響を与えないという保証であり、個人のプライバシーを保護します。([Glossary](https://desfontain.es/blog/differential-privacy-glossary.html)) |
| プライバシー予算(ε)    | DPにおいて許容される最大プライバシー損失を定量化するパラメータ。値が低いほど、プライバシーが強化されます。                                                                        |
| 準同型暗号| 暗号文に対する計算を可能にする暗号化であり、安全に復号化できる暗号化された結果を生成します。                                                            |
| マルチパーティ計算(MPC) | 複数の当事者が、入力を互いに明らかにすることなく、入力に対する関数を共同で計算できるようにするプロトコル。                                          |
| 連合学習    | 生データを交換せずに分散データでモデルがトレーニングされる分散ML。                                                                          |
| メンバーシップ推論攻撃 | レコードがモデルトレーニングで使用されたかどうかを判断する攻撃。                                                            |
| モデル反転攻撃| モデル出力またはパラメータから入力特徴を再構築する攻撃。                                                       |
| プライバシー-有用性トレードオフ | モデルのパフォーマンスとプライバシー保証のバランス。                                                            |
| 信頼実行環境(TEE) | コード/データの機密性と整合性を保護する安全なプロセッサ領域。                                       |

## まとめ表:PPML技術

| **技術**           | **プライバシー目標**              | **強み**                      | **制限事項**                        | **ツール/プロジェクトの例**         |
|------------------------|-------------------------------|-------------------------------------|----------------------------------------|------------------------------------|
| 差分プライバシー   | 個人データ保護     | 数学的保証、スケーラブル   | 有用性の損失、プライバシー予算の調整     | TensorFlow Privacy、PySyft         |
| 準同型暗号 | 暗号化データに対する計算  | データが決して明らかにされない、強力なプライバシー | 高いオーバーヘッド、限定的な演算      | Microsoft SEAL                     |
| マルチパーティ計算| 協調的な安全な計算   | 強力なプライバシー、柔軟            | 通信/計算のオーバーヘッド     | EzPC、CrypTen                      |
| 連合学習     | 生データの共有なし            | スケーラブル、協調的             | 依然として推論攻撃に対して脆弱  | PySyft、TensorFlow Federated       |

## 実務者への推奨事項

1. **脅威モデリングの実施:** MLユースケースのプライバシーリスクと攻撃ベクトルを評価します。
2. **技術の階層化:** より強力な保護のためにPPML手法(例:FL + DP)を組み合わせます。
3. **監視と測定:** プライバシーリスクを定量化し、情報漏洩を監視します。
4. **ポリシーの整合性:** 技術的保護措置が規制要件を満たすことを確認します。
5. **オープンツールの活用:** 合理化された採用のためにオープンソースフレームワークを使用します。
6. **最新情報の把握:** 研究を追跡し、手法の進歩に応じて実践を更新します。

## 参考資料

- [Microsoft Research: Privacy Preserving Machine Learning](https://www.microsoft.com/en-us/research/blog/privacy-preserving-machine-learning-maintaining-confidentiality-and-preserving-trust/)