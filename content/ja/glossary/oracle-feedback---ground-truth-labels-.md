---
title: オラクルフィードバック(正解ラベル)
url: "/ja/glossary/oracle-feedback---ground-truth-labels-/"
lastmod: '2025-12-19'
date: '2025-12-19'
translationKey: oracle-feedback-ground-truth-labels
description: AI/MLにおけるオラクルフィードバックと正解ラベルについて解説します。Oracle Select AIやHCM Cloudが、モデルのトレーニング、評価、継続的改善のために権威あるデータをどのように活用しているかを学びます。
keywords:
- オラクルフィードバック
- 正解ラベル
- AI
- 機械学習
- Select AI
category: AI
type: glossary
draft: false
e-title: Oracle Feedback (Ground-Truth Labels)
term: オラクルフィードバック(せいかいラベル)
---
## はじめに
Oracleフィードバック(「オラクルフィードバック(正解ラベル)」と呼ばれる)は、AIおよび機械学習(ML)モデルのトレーニング、評価、継続的改善のために、権威ある正しい回答を提供するシステムです。Oracleのエコシステム、特に[Oracle Select AI](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html)や[Oracle HCM Cloud](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm)などの製品において、オラクルフィードバックは教師あり学習、プロンプトチューニング、適応型自動化の基盤を形成します。「オラクル」とは、信頼できる権威(通常は人間またはゴールドスタンダードプロセス)を指し、参照、検証、反復的なモデル改善のためにこれらの正解ラベルを提供します。

## 用語集と主要定義

### Oracleフィードバック

Oracleフィードバックは、AI/MLシステムに正しい回答(正解ラベル)が提供されるプロセスです。これらの回答は、専門家または信頼できるアノテーション手法によって作成または検証され、モデルのトレーニング、検証、改善の参照として機能します。

#### 主要ポイント:
- 各入力が既知の正しい出力とペアになる教師あり機械学習で主に使用されます。
- AIシステムが例によって入力と望ましい出力の間のマッピングを学習できるようにします。
- Oracleプラットフォームでは、ユーザーインターフェース、API、または特定のプロシージャを介してフィードバックを提供できます。

**リンク:**
- [Oracle ML Fundamentals](https://www.oracle.com/artificial-intelligence/machine-learning/what-is-machine-learning/)
- [Labeling Data for ML (LabelYourData)](https://labelyourdata.com/articles/label-data-for-machine-learning)
- [OCI Data Labeling](https://www.oracle.com/artificial-intelligence/data-labeling/)

### 正解ラベル

正解ラベルは、権威あるプロセスまたは専門家のアノテーションによって確立された、特定のデータセットに対する正しい回答のセットです。これらのラベルは、AIモデルのトレーニング、検証、評価のためのゴールドスタンダードです。

- **自然言語処理(NLP)の場合:** 自然言語プロンプトに対する正しいSQLクエリ。
- **コンピュータビジョンの場合:** 画像に対する正しいクラス、バウンディングボックス、またはセグメンテーションマスク。
- **分類の場合:** データポイントに対する正しいクラスまたはカテゴリ。

### オラクル(権威)

AI/MLにおけるオラクルとは、正しい出力がどうあるべきかについて決定的なフィードバックまたは検証を提供する信頼できる情報源を指します。多くの場合、これは人間の専門家ですが、信頼できる自動化システムまたはプロセスである場合もあります。

## Oracle AIと自動化におけるOracleフィードバックの仕組み

### 1. データラベリングと収集

プロセスは、データサンプルに正しい回答を割り当てる行為であるデータラベリングから始まります。Oracleの[OCI Data Labeling](https://www.oracle.com/artificial-intelligence/data-labeling/)は、AIモデルのトレーニングに不可欠なデータセットの組み立てとアノテーションのための堅牢なサービスを提供します。

#### ステップ:
- データがアップロードされます(テキスト、画像、ドキュメント)。
- アノテーターが各データ項目に正しい出力でラベル付けします。
- ラベル付けされたデータは、Oracle AIおよびデータサイエンスサービスとの直接統合のためにJSON形式でエクスポートできます。

**機能:**  
- カスタムテンプレートとアノテーション形式。
- GUIおよびAPIベースのアノテーション。
- シームレスなモデルトレーニングのためのOCI VisionおよびOCI Languageとの統合。

### 2. モデルトレーニング(教師あり学習)

ラベル付けされたデータは教師あり学習に使用され、モデルは各例に対して正しい回答を明示的に示されます。

- **アルゴリズムの例:** ニューラルネットワーク、決定木、SVM。
- **プロセス:** 各入力はそのラベルとペアになり、モデルは予測と正しい出力の間の誤差を最小化するために内部パラメータを調整します。

### 3. モデル評価と検証

トレーニング後、モデルは新しいラベル付きデータでテストされます。出力は正解ラベルと比較され、精度、適合率、再現率、F1スコアなどのメトリクスが計算されます。

- **目的:** AI予測が正解から逸脱する箇所を特定し、集中的な改善を可能にします。
- **ベストプラクティス:** 信頼できるオラクル提供のラベルを持つ別個のテストセットを使用します。

### 4. Oracleプラットフォームにおけるフィードバックメカニズム

#### **Oracle Select AI (NL2SQL) フィードバックループ**

[Select AI](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html)は、ユーザーがAI生成のSQLクエリに直接フィードバックを提供できるようにし、自然言語からSQLへのパフォーマンスを向上させます。

- **プロセス:**
  - ユーザーが自然言語プロンプトを発行します。
  - AIがSQLクエリを生成します。
  - ユーザーがSQLをレビューします:
    - 正しい場合、肯定的なフィードバックが与えられます。
    - 正しくない場合、ユーザーは修正されたSQLまたは説明的なフィードバックを提供します。
  - フィードバックはベクトルインデックス(例: `<profile_name>_FEEDBACK_VECINDEX`)に記録されます。

- **技術的インターフェース:**
  - フィードバックはUIを通じて、または`DBMS_CLOUD_AI.FEEDBACK`プロシージャを呼び出すことで提供できます。
    - [DBMS_CLOUD_AI Package Reference](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-package.html)
  - フィードバックは将来のプロンプトの参照として使用され、LLMのコンテキスト理解と精度を向上させます。

- **例:**
```sql
-- 正しいSQLに対する肯定的なフィードバック
EXEC DBMS_CLOUD_AI.FEEDBACK(
    ai_profile    => 'my_profile',
    prompt        => 'Show me all sales from last quarter',
    feedback_type => 'positive',
    feedback      => 'The generated SQL is correct.'
);

-- 正しいSQLを含む否定的なフィードバック
EXEC DBMS_CLOUD_AI.FEEDBACK(
    ai_profile    => 'my_profile',
    prompt        => 'Show me all sales from last quarter',
    feedback_type => 'negative',
    feedback      => 'The SQL should include date filtering for last quarter.',
    correct_sql   => 'SELECT * FROM sales WHERE sale_date BETWEEN :start AND :end;'
);
```

- **基盤メカニズム:**  
  ベクトルインデックスはフィードバックを保存し、Select AIが新しい類似のプロンプトに対してコンテキスト的に関連するフィードバックを取得して使用できるようにし、時間の経過とともに出力を改善します。

#### **Oracle HCM Cloud: AI支援フィードバック**

Oracle HCM Cloudの[AI Assistance for Giving Feedback](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm)機能は、生成AIを活用して、ユーザーが同僚や直属の部下に対する効果的なフィードバックを書くのを支援します。

- **ワークフロー:**
  - ユーザーが初期フィードバックを入力します。
  - AI Assistアイコンをクリックすると、システムが初期テキストに基づいてドラフトを生成します。
  - ユーザーがレビュー、編集し、フィードバックを送信します。
  - 人間がレビューした最終的なフィードバックは正解として保存され、将来のAI生成ドラフトを改善します。

- **設定手順:**
  - ドキュメントに記載されているように、Redwood Anytime FeedbackおよびVisual Builder Studio機能を有効にします。
  - プロファイルオプション(例: `ORA_HCM_VBCS_PWA_ENABLED`、`ORA_HRT_ANYTIME_FEEDBACK_REDWOOD_ENABLED`)を使用して機能を有効化します。
  - [Set Profile Option Values](https://docs.oracle.com/pls/topic/lookup?ctx=fa-latest&id=s20052787)
  - [Visual Builder Studio Overview](https://docs.oracle.com/pls/topic/lookup?ctx=fa-latest&id=s20072861)

- **メリット:**
  - フィードバックプロセスを加速します。
  - フィードバックの品質と一貫性を確保します。
  - システムが時間の経過とともに組織およびマネジメントスタイルに適応します。

### 5. フィードバックループと継続的改善

Oracleのフィードバックシステムは、クローズドフィードバックループをサポートします:  
- 新しいフィードバックがシステムに継続的に組み込まれます。
- 保存されたフィードバックが将来のモデル出力をコンテキスト化し、チューニングします。
- モデルは完全な再トレーニングを必要とせずに、進化するユーザーニーズとドメイン固有の要件に適応します。

## Oracleフィードバックと正解ラベルのメリット

- **精度:** モデルが正しい例から直接学習し、より信頼性の高い出力につながります。
- **透明性:** 人間が検証した回答は、トレーサビリティとアカウンタビリティを提供します。
- **適応学習:** システムは新しいフィードバックを組み込むことで進化し、プロンプトチューニングと継続的な精度をサポートします。
- **効率的な評価:** 正解ベンチマークに対する客観的な測定により、堅牢なモデル評価が可能になります。
- **パーソナライゼーション:** ユーザーフィードバックが組織またはドメイン固有の要件に対してAIの動作を改善します。
- **バイアス削減:** 多様でよくラベル付けされたデータセットは、望ましくないモデルバイアスに対抗するのに役立ちます。
- **スケーラブルな自動化:** フィードバックループは、完全な再トレーニングなしで継続的な改善とデプロイメントをサポートします。

## 例とユースケース

### Oracle Select AI: NL2SQLフィードバックループ

- ユーザーが自然言語でレポートを要求します。
- Select AIがSQLクエリを生成します。
- ユーザーがSQLを確認または修正します。
- 修正されたSQLが正解として保存されます。
- システムは保存されたフィードバックを使用して、将来のSQL生成を改善します。

**ドキュメント:**  
[Select AI Feedback](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html)

### Oracle HCM Cloud: AI生成従業員フィードバック

- HRマネージャーが従業員レビューの初期コメントを書きます。
- AI Assistがドラフトを生成します。
- マネージャーがレビュー/編集して送信します。
- 人間がレビューしたフィードバックは、将来のAI提案のための正解コーパスの一部になります。

**ドキュメント:**  
[AI Assistance for Giving Feedback](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm)

### コンピュータビジョンにおける教師あり学習

- 人間のアノテーターが画像にラベル付けします(例: 「欠陥あり」対「欠陥なし」製品)。
- これらのラベルでトレーニングされたモデルは、新しい画像の欠陥を検出できます。

### スパム検出

- アノテーターがメールを「スパム」または「スパムでない」とラベル付けします。
- モデルは、これらのオラクル提供のラベルに基づいて新しいメールを分類することを学習します。

## ベストプラクティスと実装のヒント

- **正解作成にはドメイン専門家または堅牢なアノテーションガイドラインを使用します。**
- **スケーラブルなアノテーションのためにOCI Data Labelingなどのツールを活用します。**
- **進化する要件に適応するために、フィードバックを継続的に組み込みます。**
- **フィードバックへの過学習を防ぐために、別個の検証およびテストセットを使用します。**
- **トレーサビリティと再現性のために、フィードバックとアノテーションプロセスを文書化します。**

## 技術的詳細: Select AIフィードバックとDBMS_CLOUD_AI.FEEDBACK

**フィードバックメカニズム:**
- Oracle AI Database 26aiでのみ利用可能です。
- Select AIアクション(`runsql`、`showsql`、`explainsql`)と併用されます。
- フィードバックアクションまたは`DBMS_CLOUD_AI.FEEDBACK`プロシージャがユーザーの応答を記録します。
- フィードバック参照を保存するためのデフォルトベクトルインデックス(`<profile_name>_FEEDBACK_VECINDEX`)を作成します。

**DBMS_CLOUD_AI.FEEDBACKの構文と使用法:**
- LLM生成のSQLが正しくない場合、または改善が必要な場合に使用されます。
- 肯定的(確認)および否定的(修正)フィードバックの両方を許可します。
- フィードバックは、将来の類似クエリの参照として使用されます。

**ドキュメント:**  
[DBMS_CLOUD_AI Package Reference](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-package.html)

## 参考文献とさらなる読み物

1. [Oracle Documentation – Select AI Feedback](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-feedback.html)
2. [Oracle Documentation – DBMS_CLOUD_AI.FEEDBACK Procedure](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbms-cloud-ai-package.html)
3. [OCI Data Labeling](https://www.oracle.com/artificial-intelligence/data-labeling/)
4. [AI Assistance for Giving Feedback – Oracle HCM Cloud](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tama-24a/24A-talent-mgmt-wn-f31188.htm)
5. [What is Machine Learning? (Oracle)](https://www.oracle.com/artificial-intelligence/machine-learning/what-is-machine-learning/)
6. [Labeling Data for Machine Learning (LabelYourData)](https://labelyourdata.com/articles/label-data-for-machine-learning)
7. [Supervised vs Unsupervised Learning (Viso.ai)](https://viso.ai/deep-learning/supervised-vs-unsupervised-learning/)

## 付録: 関連するOracleドキュメント

- [Select AI Overview](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/select-ai.html)
- [Autonomous AI Database Supplied Package Reference](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/dbmscloud-reference.html)
- [Oracle Cloud HCM: Implementing Generative AI](https://blogs.oracle.com/fusionhcmcoe/implementing-generative-ai-oracle-cloud-hcm)

**この用語集は、Oracleフィードバックと正解ラベリングに関する包括的で技術的に詳細なカバレッジを提供し、さらなる探索と実装のためのOracleおよび業界ドキュメントへの直接リンクを含んでいます。**
