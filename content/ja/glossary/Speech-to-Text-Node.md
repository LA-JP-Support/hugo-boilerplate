---
title: Speech-to-Textノード
translationKey: speech-to-text-node
description: Speech-to-Textノードは、自動音声認識(ASR)を使用して音声言語を機械可読テキストに変換する、自動化プラットフォームやAIワークフローにおけるモジュール型コンポーネントです。
keywords:
- Speech-to-Textノード
- 自動音声認識
- AIワークフロー
- 音声からテキスト
- 文字起こし
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: Speech-to-Text Node
term: スピーチ・トゥ・テキスト・ノード
url: "/ja/glossary/Speech-to-Text-Node/"
---
## Speech-to-Textノードとは?
Speech-to-Textノードは、会話型AI、自動化パイプライン、ワークフローシステムにおける基盤コンポーネントであり、音声ファイル(音声録音、通話、動画のサウンドトラック)内の話し言葉を正確で構造化されたテキストに変換します。この文字起こしにより、下流での分析、要約、翻訳、または自動プロセスのトリガーが可能になり、音声対応アプリケーションやナレッジマネジメントシステムにとって不可欠な要素となっています。

このノードは、音声入力を受け取り、自動音声認識(ASR)モデルを通じて処理し、トランスクリプトを出力するモジュール式ワークフローコンポーネントとして機能します。このトランスクリプトには、オプションで単語レベルのタイムスタンプ、話者ラベル、翻訳、または構造化されたメタデータを含めることができ、さらなる処理に利用できます。

**典型的なワークフロー:**1. 音声入力の受信(ファイルアップロード、URL、またはワークフロー変数)
2. ASRモデルによる処理(OpenAI Whisper、Google Speech-to-Text、Azure Speech、Rev AI)
3. オプションのメタデータ(タイムスタンプ、話者ラベル、翻訳)を含むトランスクリプトの出力

**自動化における役割:**- チャットボットが音声クエリを処理できるようにする
- 会議、インタビュー、講義をナレッジマネジメント用に文字起こし
- 音声インタラクションからのコンテンツインデックス作成とデータ抽出を自動化

## 主要機能

**自動音声認識(ASR)**多様なアクセントや音声条件に対して高精度で、先進的なモデルを使用して音声をテキストに変換します。**多言語サポート**プロバイダーに応じて50~125以上の言語と方言で音声を文字起こしします。主要なモデルは国際展開のためのグローバルな言語カバレッジをサポートしています。**翻訳**英語以外の音声を英語または他のサポート言語に単一の処理ステップで翻訳し、別個の翻訳ワークフローの必要性を排除します。**カスタムプロンプト指示**文字起こしスタイル、話者ラベリング、用語の好み、またはエラー処理アプローチに関する自然言語の指示を受け付けます。**柔軟な音声入力**ファイルアップロード、URL、または前のワークフローステップからの変数を受け付け、多様な統合パターンをサポートします。**大容量ファイル処理**プロバイダー固有の制限(通常25 MB)までのファイルを処理し、より大きなファイルを論理的な境界でセグメント化するガイダンスを提供します。**タイムスタンプと話者ダイアライゼーション**オプションで単語レベルまたは発話レベルのタイミングを含め、複数参加者の会話で個々の話者を識別します。**不適切な言葉のフィルタリング**設定またはモデルのデフォルトに従って、不快なコンテンツを削除またはマスクします。**カスタム語彙とモデル適応**語彙リストとモデルのファインチューニングを通じて、ドメイン固有の用語の認識を改善します。**構造化出力(JSON)**ネストされたメタデータを含む、下流処理に適したスキーマでデータを返します。

## Speech-to-Textノードの動作原理

### 音声入力

ノードは、ユーザーアップロード、クラウドストレージ、または前のワークフローステップから音声ファイルまたはURLを受け取ります。サポートされる形式には通常、MP3、WAV、MP4、M4A、WebM、MPGA、MPEGが含まれます。

### モデル選択と前処理

**ASRプロバイダーの選択:**OpenAI Whisper、Google Speech-to-Text、Azure Speech Service、AssemblyAI、Deepgram、またはその他のプロバイダーから選択します。**機能の設定:**言語検出、翻訳、タイムスタンプ、話者識別、カスタムプロンプトを有効にします。

### 文字起こしプロセス

ASRエンジンが音声を処理し、音響モデルと言語モデルを適用してテキストを生成します。翻訳、不適切な言葉のフィルタリング、フォーマット、ダイアライゼーションなどのオプション機能は、文字起こし中または後に適用されます。

### 出力処理

ノードはプレーンテキストまたは構造化JSON形式でトランスクリプトを出力します。下流のワークフローステップは、この出力を要約、分析、保存、またはユーザーフィードバックのために利用します。

## サポートされる音声形式とファイル制限

**音声形式:**- M4A、MP3、WebM、MP4、MPGA、WAV、MPEG
- プロバイダーのサポートは異なります。選択したASRサービスとの互換性を確認してください

**ファイルサイズ制限:**- 典型的な最大値:ファイルあたり25 MB
- より大きなファイルは25 MB以下のセグメントに分割する必要があります
- コンテキストと精度を保持するため、論理的な文の境界でセグメント化してください

**入力方法:**- 直接ファイルアップロード
- ホストされた音声へのURL参照
- 前のワークフローステップからの変数参照

一部のプラットフォームは、セキュリティとスケーラビリティの理由からURLのみを受け付けます。

## 設定ガイド

### 前提条件

- 自動化プラットフォームへのアクセス(Kore.ai、LiveKit、Google Cloud、Azure)
- APIキーまたは統合認証情報(必要な場合)
- アクセス可能なURLでホストされているか、アップロード可能な音声ファイル

### ステップバイステップ設定

**1. ワークフローにノードを追加**自動化ビルダーを開き、Speech-to-TextまたはAudio to Textノードをワークフローにドラッグします。**2. ノードプロパティの設定**-**ノード名:**一意で説明的な名前を割り当てます(例:「MeetingTranscription」)
- **音声ファイル入力:**音声URLを保持する変数を参照
- **モデル選択:**ASRプロバイダーと特定のモデルを選択
- **機能トグル:**翻訳、タイムスタンプ、話者ダイアライゼーション、不適切な言葉のフィルタリングを有効化**3. カスタムプロンプト指示の設定**文字起こしスタイル、話者ラベリング要件、用語の好み、またはエラー処理アプローチを自然言語で定義します。

例:
```
フィラーワードを省略し、明確な話者ラベルと正確な技術用語を含むクリーンなトランスクリプトを提供してください。
```

**4. 出力用のJSONスキーマを定義(オプション)**下流処理用の構造化出力スキーマを指定します:

```json
{
  "type": "object",
  "properties": {
    "transcript": {"type": "string"},
    "timestamps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "word": {"type": "string"},
          "start": {"type": "number"},
          "end": {"type": "number"}
        }
      }
    }
  }
}
```

**5. 成功と失敗のパスを接続**-**成功時:**要約、翻訳、または分析ノードにルーティング
- **失敗時:**エラー処理またはフォールバックノードにルーティング**6. テストと検証**サンプル入力でワークフローを実行し、出力の完全性と正確性を確認し、必要に応じて設定を調整します。

## 設定パラメータ

| パラメータ | 説明 | 例 |
|-----------|-------------|---------|
| Audio Input | アップロードされた音声ファイルへのURLまたは参照 | `https://host/path/audio.mp3` |
| Model | 使用するASRエンジン/モデル | `OpenAI Whisper-1`、`Chirp 3` |
| Language Code | 文字起こし用の言語(BCP-47) | `en-US`、`fr-FR` |
| Translation | 英語への翻訳を有効化 | `true` / `false` |
| Timestamps | 単語/発話レベルのタイムスタンプを含める | `true` / `false` |
| Speaker Labels | ダイアライゼーション、複数参加者音声で話者をラベル付け | `true` / `false` |
| Profanity Filter | 不適切な言葉を削除またはマスク | `true` / `false` |
| Prompt | 文字起こしスタイルのカスタム指示 | 上記参照 |
| JSON Schema | 下流処理用の構造化出力 | 上記参照 |
| Custom Vocab | 認識をバイアスするドメイン固有の単語 | `["AcmeCorp", "API Gateway"]` |
| Input Variable | 入力音声ファイルを保持するコンテキスト変数 | `{{context.steps.Start.AudioURL}}` |

## レスポンス形式と出力

**プレーンテキスト出力:**連続したテキスト文字列としてのデフォルトトランスクリプト。**構造化JSON出力:**トランスクリプト、タイムスタンプ、話者ラベル、信頼度スコアを含みます。**例:**```json
{
  "transcript": "こんにちは、AcmeCorpにお電話いただきありがとうございます。本日はどのようなご用件でしょうか?",
  "timestamps": [
    { "word": "こんにちは", "start": 0.0, "end": 0.5 },
    { "word": "AcmeCorpに", "start": 0.6, "end": 0.8 }
  ],
  "speakers": [
    { "segment": "顧客", "start": 0.0, "end": 3.0 }
  ]
}
```**高度な機能:**Rev AIは、追加の出力オプションとして感情分析、トピック抽出、要約、強制アライメントを提供します。

## 一般的なユースケース

**会議と講義の文字起こし**会議、インタビュー、講義を検索可能でインデックス化可能なテキストに文字起こしし、ナレッジマネジメントとコンプライアンスに活用します。**カスタマーサポート自動化**チャットボット、CRMシステム、ヘルプデスクプラットフォーム用に音声インタラクションを文字起こしし、自動ルーティングと分析を可能にします。**字幕とキャプションの生成**アクセシビリティとローカライゼーションのため、タイムスタンプアライメントを使用してビデオコンテンツの字幕を生成します。**音声コマンド処理**音声対応アプリケーションとスマートデバイス用に、話された命令を実行可能なテキストに変換します。**音声ベースの翻訳**ローカライゼーションとアクセシビリティのため、多言語音声を単一ステップで文字起こしおよび翻訳します。**医療文書作成**専門的な医療語彙サポートを使用して、医療口述や診察を患者記録に変換します。**コールセンター分析**品質保証、コンプライアンス監視、パフォーマンス分析のため、録音された通話を文字起こしします。**市場調査**テーマ分析とレポート作成のため、フォーカスグループやインタビューの録音を文字起こしします。

## 統合のベストプラクティス

**コンテキスト変数の使用**柔軟なワークフロー設計と再利用性をサポートするため、音声URLまたはデータを動的に参照します。**プロンプトエンジニアリングの活用**特定のユースケースの精度を向上させるため、話者ラベリング、用語、またはフォーマットの指示を調整します。**バッチ処理の実装**大量の場合、リソース使用を最適化し処理時間を短縮するため、バッチまたは非同期モードを利用します。**音声品質の前処理**文字起こし精度を最大化するため、処理前にクリアな音声、最小限の背景ノイズ、互換性のある形式を確保します。**ファイルの戦略的セグメント化**サイズ制限に近づいたときにコンテキストを維持するため、長い録音を論理的な区切り(文の境界、話者の変更)で分割します。**カスタム語彙の提供**技術用語、製品名、または業界用語の認識を改善するため、ドメイン固有の用語リストを提出します。**コンプライアンス機能の設定**規制要件を満たすため、不適切な言葉のフィルタリングを有効にし、適切なデータレジデンシーオプションを選択します。

## エラー処理とモニタリング

### エラータイプ

- サポートされていないファイル形式またはサイズ制限の超過
- 無効またはアクセス不可能な音声URL
- モデル選択または設定エラー
- 出力スキーマの不一致

### エラー処理戦略

- 処理前に入力形式とサイズを検証
- 指数バックオフを使用した再試行ロジックの実装
- 重要なワークフロー用のフォールバックフローの設計
- トラブルシューティング用の詳細なコンテキストを含むエラーのログ記録

### パフォーマンスメトリクス

- 処理された音声の分数(コスト/使用量追跡用)
- トークン使用量(LLM対応ASRシステム用)
- レスポンス時間とスループット
- エラータイプ別のエラー率

## プロバイダー比較

| プロバイダー | 主要機能 | 言語 | 備考 |
|----------|-------------|-----------|-------|
| **OpenAI Whisper**| 多言語、翻訳、堅牢なASR、不適切な言葉のフィルタリング | 50以上 | 汎用文字起こしに最適 |
| **Google Speech-to-Text**| 125以上の言語、ストリーミングとバッチ、ダイアライゼーション、適応 | 125以上 | 強力なエンタープライズ機能 |
| **Azure Speech**| リアルタイム/バッチ、カスタムモデル、業界適応 | 100以上 | Microsoftエコシステムとの深い統合 |
| **Rev AI**| 非同期とストリーミング、人間と機械の文字起こし | 58以上 | ハイブリッド人間/AIオプション |
| **LiveKit**| プラグイン可能なモデル(AssemblyAI、Cartesia、Deepgram) | モデル依存 | リアルタイムアプリケーションに柔軟 |
| **VectorShift**| ノードベースのパイプライン、LLM統合 | プロバイダー依存 | 複雑なワークフローに最適 |

## 実装例

### 例1:会議の文字起こし(Kore.ai)

**プロンプト:**「直接話法を使用し、問題または課題に関連する語彙を強調してください。」**入力:**```json
{
  "audioFile": "https://example.com/meeting-2024-06-10.mp3"
}
```**出力:**```
話者1:APIゲートウェイで繰り返し発生する問題が起きています。
話者2:主な課題は外部認証の統合です。
```

### 例2:Google Speech-to-Text API(Node.js)

```javascript
const speech = require('@google-cloud/speech');
const client = new speech.SpeechClient();

async function transcribe() {
  const audio = { uri: 'gs://cloud-samples-data/speech/brooklyn_bridge.raw' };
  const config = { 
    encoding: 'LINEAR16', 
    sampleRateHertz: 16000, 
    languageCode: 'en-US' 
  };
  const request = { audio, config };
  const [response] = await client.recognize(request);
  const transcription = response.results
    .map(r => r.alternatives[0].transcript)
    .join('\n');
  console.log(`Transcription: ${transcription}`);
}

transcribe();
```

### 例3:LiveKit STTモデル(Python)

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="assemblyai/universal-streaming:en",
    # ... llm, tts, etc.
)
```

## 技術的考慮事項

**トークン制限:**一部のASRモデルには入力トークン制限があります(例:Whisper:224トークン)。長編コンテンツのセグメント化戦略を計画してください。**エッジ音声ケース:**サイズ制限に近いファイルの場合、論理的な境界でセグメント化し、分割時に文の整合性を維持してください。**不適切な言葉とコンテンツフィルタリング:**一部のモデルでは削除がデフォルトの場合があります。ユースケースに応じて設定オプションを確認してください。**話者ダイアライゼーション:**すべてのプロバイダーで普遍的にサポートされているわけではありません。複数話者シナリオの可用性と精度を確認してください。**リアルタイム vs バッチ:**レイテンシ要件とコスト最適化に基づいて、ストリーミング(リアルタイム)とバッチ処理のいずれかを選択してください。

## 参考文献


1. Kore.ai. (n.d.). Audio to Text Node Documentation. Kore.ai Documentation.
2. OpenAI. (n.d.). Whisper Documentation. OpenAI Platform.
3. Google Cloud. (n.d.). Speech-to-Text. Google Cloud Documentation.
4. Google Cloud. (n.d.). Speech-to-Text Supported Languages. Google Cloud Documentation.
5. Google Cloud. (n.d.). Speech-to-Text Encoding. Google Cloud Documentation.
6. Google Cloud. (n.d.). Speech-to-Text Adaptation. Google Cloud Documentation.
7. Google Cloud. (n.d.). Cloud Monitoring. Google Cloud Documentation.
8. Microsoft. (n.d.). Azure Speech Service Overview. Microsoft Learn.
9. Microsoft. (n.d.). Azure Batch Transcription. Microsoft Learn.
10. Rev AI. Speech-to-Text Service. URL: https://www.rev.ai/
11. LiveKit. (n.d.). STT Documentation. LiveKit Documentation.
12. LiveKit. (n.d.). STT Inference. LiveKit Documentation.
13. LiveKit. (n.d.). STT Plugins. LiveKit Documentation.
14. LiveKit. (n.d.). STT Usage. LiveKit Documentation.
15. LiveKit. (n.d.). STT Additional Parameters. LiveKit Documentation.
16. VectorShift. (n.d.). Speech-to-Text Documentation. VectorShift Documentation.
17. Kore.ai. (n.d.). Model Analytics Dashboard. Kore.ai Documentation.
18. Google. (n.d.). Codelabs: Cloud Speech Text Node. Google Codelabs.
