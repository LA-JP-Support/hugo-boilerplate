---
title: Speech-to-Textノード
translationKey: speech-to-text-node
description: Speech-to-Textノードは、自動音声認識(ASR)を使用して音声言語を機械可読テキストに変換する、自動化プラットフォームやAIワークフローにおけるモジュール型コンポーネントです。
keywords: ["Speech-to-Textノード", "自動音声認識", "AIワークフロー", "音声からテキスト", "文字起こし"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: スピーチ・トゥ・テキスト・ノード
reading: Speech-to-Textノード
kana_head: その他
e-title: Speech-to-Text Node
---
## 概要

**音声テキスト変換ノード**は、音声ファイル(音声録音、通話、動画のサウンドトラック)内の話し言葉を正確で構造化されたテキストに変換することで、会話型AI、自動化パイプライン、ワークフローシステムの基盤を形成します。この文字起こしは、分析、要約、翻訳、またはさらなる自動化プロセスのトリガーに使用できます。

**典型的なワークフロー:**
1. 音声入力を受信(ファイルアップロード、URL、またはワークフロー内の変数として)。
2. [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text)、[Google Speech-to-Text](https://cloud.google.com/speech-to-text)、[Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text)、または[Rev AI](https://www.rev.ai/)などのサードパーティプロバイダーといったASRモデルを使用して音声を処理。
3. 文字起こし結果を出力(オプションで単語レベルのタイムスタンプ、話者ラベル、または翻訳を含む)。

**自動化における役割:**
- チャットボットが音声クエリを処理できるようにする。
- 会議、インタビュー、講義を文字起こしして知識管理に活用。
- 音声インタラクションやメディアからのコンテンツインデックス作成とデータ抽出を自動化。

**参考資料:**  
- [Kore.ai Audio to Text Node Documentation](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)  
- [LiveKit STT Models Overview](https://docs.livekit.io/agents/models/stt/)

## 主要機能

- **自動音声認識(ASR):** 高度なモデルを使用して音声をテキストに変換([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)、[LiveKit](https://docs.livekit.io/agents/models/stt/)、[Rev AI](https://www.rev.ai/))。
- **多言語サポート:** 複数の言語と方言で音声を文字起こし([Google対応言語](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)、[OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text#supported-languages))。
- **翻訳:** 英語以外の音声を英語または他の対応言語に翻訳(プロバイダー固有)。
- **カスタムプロンプト指示:** 文字起こしスタイル、話者ラベリング、用語、エラー処理の指示を受け付け。
- **柔軟な音声入力:** ファイルアップロード、URL、または前のワークフローステップからの変数を受け付け。
- **大容量ファイル処理:** プロバイダー固有の制限(多くの場合25 MB)までのファイルを処理し、より大きなファイルのセグメント化をサポート。
- **タイムスタンプと話者分離:** オプションで単語/発話レベルのタイミングと話者ラベルを含む([LiveKit Plugins](https://docs.livekit.io/agents/models/stt/#plugins)参照)。
- **不適切な言葉のフィルタリング:** 設定またはモデルのデフォルトに従って不適切なコンテンツを削除またはマスク。
- **カスタム語彙とモデル適応:** ドメイン固有の用語の認識を改善([Google Adaptation](https://cloud.google.com/speech-to-text/docs/adaptation)参照)。
- **構造化出力(JSON):** 下流処理に適したスキーマでデータを返す。

## 動作原理

1. **音声入力:**  
   - ノードは音声ファイルまたはURL(ユーザーアップロード、クラウドストレージ、または前のワークフローステップから)を受信。
   - 対応フォーマットには通常、MP3、WAV、MP4、M4A、WebM、MPGA、MPEGが含まれる([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)、[Rev AI](https://www.rev.ai/))。

2. **モデル選択と前処理:**
   - ASRモデル/プロバイダーを選択(例:Whisper、Google、Azure、AssemblyAI、Deepgram)。
   - 言語、翻訳、追加機能(タイムスタンプ、話者ID、カスタムプロンプト)を設定。

3. **文字起こしプロセス:**
   - 選択されたASRエンジンが音声を処理し、テキスト文字起こしを生成。
   - オプション機能:翻訳、不適切な言葉のフィルタリング、フォーマット、話者分離。

4. **出力処理:**
   - ノードは文字起こし結果(プレーンテキストまたは構造化JSON)を出力。
   - 出力は下流ステップ(要約、分析、ユーザーフィードバック)で使用される。

**図の例:**  
![Speech to Text Node Workflow](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/images/how-audio-to-text-works.png)  
([出典:Kore.ai Documentation](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))

**LiveKitの場合:**  
- [LiveKit Inference](https://docs.livekit.io/agents/models/stt/#inference)は、AssemblyAI、Cartesia Ink Whisper、Deepgram Novaモデルを提供し、さまざまな言語と専門オプションに対応。

## 対応音声フォーマットとファイル制限

- **音声フォーマット:**  
  - M4A、MP3、WebM、MP4、MPGA、WAV、MPEG([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)、[Google](https://cloud.google.com/speech-to-text/docs/encoding)、[Rev AI](https://www.rev.ai/))。

- **ファイルサイズ制限:**  
  - 一般的な最大値:**ファイルあたり25 MB**(プロバイダーによって異なる)。
  - より大きなファイルは25 MB以下のセグメントに分割する必要があり、コンテキストと精度を保持するために論理的な文の境界で分割することが理想的([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))。

> **注意:** セキュリティとスケーラビリティのため、一部のプラットフォームは入力としてURLのみを受け付けます。

## ステップバイステップ設定ガイド

### 例:音声テキスト変換ノードの設定(Kore.ai)

**前提条件:**
- 自動化プラットフォームへのアクセス(例:[Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)、[LiveKit](https://docs.livekit.io/agents/models/stt/)、[Google Cloud](https://cloud.google.com/speech-to-text)、[Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text))。
- APIキーまたは統合認証情報(必要な場合)。
- アクセス可能なURLでホストされている、またはアップロードによって提供される音声ファイル。

#### 1. ワークフローにノードを追加
- 自動化ビルダー(例:Kore.aiボットフローデザイナー)を開く。
- **音声テキスト変換**(または**Audio to Text**)ノードを見つけてワークフローにドラッグ。

#### 2. ノードプロパティを設定
- **ノード名:** 一意でわかりやすい名前を割り当て(例:「会議文字起こし」)。
- **音声ファイル入力:** 音声ファイルURLを保持する変数を参照、例:`{{context.steps.Start.MeetingAudioUrl}}`。
- **モデル選択:** ASRモデル/プロバイダーを選択(例:OpenAI Whisper、AssemblyAI、Deepgram)。
- **機能トグル:** 必要に応じて翻訳、タイムスタンプ、話者分離、不適切な言葉のフィルタリングを有効化。

#### 3. カスタムプロンプト指示を設定
- 文字起こし指示を定義(例:スタイル、話者ラベル、エラー処理)。
- 例:  
  ```
  フィラーワードを省略し、明確な話者ラベルと正確な技術用語を含むクリーンな文字起こしを提供してください。
  ```

#### 4. (オプション)出力用のJSONスキーマを定義
- 構造化出力のレスポンススキーマを指定。
- 例:
  ```json
  {
    "type": "object",
    "properties": {
      "transcript": {"type": "string"},
      "timestamps": {"type": "array", "items": {"type": "object", "properties": {
        "word": {"type": "string"},
        "start": {"type": "number"},
        "end": {"type": "number"}
      }}}
    }
  }
  ```

#### 5. 成功と失敗のパスを接続
- **成功時:** 要約、翻訳、または他の下流ノードにルーティング。
- **失敗時:** エラー処理またはフォールバックノードにルーティング。

#### 6. テストと検証
- サンプル入力でワークフローを実行。
- 出力の完全性と正確性を確認。
- 必要に応じて設定を調整。

**完全ガイド:** [Kore.ai Audio to Text Node Documentation](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)

## 設定パラメータと高度な機能

| パラメータ        | 説明                                                         | 例/オプション                  |
|------------------|-------------------------------------------------------------|-------------------------------|
| 音声入力         | アップロードされた音声ファイルへのURLまたは参照                | `https://host/path/audio.mp3` |
| モデル           | 使用するASRエンジン/モデル                                    | `OpenAI Whisper-1`、`Chirp 3`、`AssemblyAI Universal-Streaming` |
| 言語コード       | 文字起こし用の言語(BCP-47コード)                              | `en-US`、`fr-FR`              |
| 翻訳             | 英語への翻訳を有効化(サポートされている場合)                   | `true` / `false`              |
| タイムスタンプ   | 単語/発話レベルのタイムスタンプを含む                          | `true` / `false`              |
| 話者ラベル       | 話者分離、複数話者の音声で話者をラベル付け                     | `true` / `false`              |
| 不適切な言葉フィルター | 不適切な言葉を削除またはマスク                            | `true` / `false`              |
| プロンプト       | 文字起こしスタイルのカスタム指示                               | 上記参照                      |
| JSONスキーマ     | 下流処理用の構造化出力                                        | 上記参照                      |
| カスタム語彙     | 認識をバイアスするドメイン固有の単語リスト                     | `["AcmeCorp", "API Gateway"]` |
| 入力変数         | 入力音声ファイルURL/参照を保持するコンテキスト変数             | `{{context.steps.Start.AudioURL}}` |

> **LiveKit:** [高度なパラメータとカスタムSTT](https://docs.livekit.io/agents/models/stt/#additional-parameters)

## レスポンスフォーマットと出力処理

**出力タイプ:**
- **プレーンテキスト:** デフォルトの文字起こし。
- **構造化JSON:** 文字起こし、タイムスタンプ、話者ラベル、(オプションで)信頼度スコアを含む。

**出力例:**
```json
{
  "transcript": "こんにちは、AcmeCorpにお電話いただきありがとうございます。本日はどのようなご用件でしょうか?",
  "timestamps": [
    { "word": "こんにちは", "start": 0.0, "end": 0.5 },
    { "word": "お電話", "start": 0.6, "end": 0.8 }
  ],
  "speakers": [
    { "segment": "顧客", "start": 0.0, "end": 3.0 }
  ]
}
```

- **Rev AI:** 感情分析、トピック抽出、要約、強制アライメントなどのインサイトを提供([Rev AI Features](https://www.rev.ai/))。

## 一般的な使用例

- **会議と講義の文字起こし:**  
  会議、インタビュー、講義を検索可能でインデックス化可能なテキストに文字起こし。
- **カスタマーサポート自動化:**  
  チャットボット、CRM、ヘルプデスクシステム用に音声インタラクションを文字起こし。
- **字幕とキャプション生成:**  
  タイムスタンプアライメント付きで動画コンテンツの字幕を生成。
- **音声コマンド処理:**  
  音声対応アプリ用に話された命令を実行可能なテキストに変換。
- **音声ベースの翻訳:**  
  ローカライゼーションとアクセシビリティのために多言語音声を文字起こしして翻訳。
- **医療文書作成:**  
  医療口述や診察を患者記録に変換。
- **コールセンター分析:**  
  品質保証、コンプライアンス、分析のために録音された通話を文字起こし。
- **市場調査:**  
  さらなる分析のためにフォーカスグループやインタビューの録音を文字起こし。

- [Rev AI Use Cases](https://www.rev.ai/)

## 統合のヒントとベストプラクティス

- **コンテキスト変数:** 変数を使用して音声URLやデータを動的に参照。
- **プロンプトエンジニアリング:** 精度向上のため、話者ラベリング、用語、フォーマットの指示を調整。
- **バッチ処理:** 大量の場合、バッチまたは非同期モードを利用([Google Batch Transcription](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription))。
- **音声前処理:** クリアな音声、最小限のノイズ、互換性のあるフォーマットを確保。
- **ファイルセグメント化:** 長い録音を論理的な区切りで分割。
- **モデル適応:** 専門ドメインでのパフォーマンス向上のためにカスタム語彙リストを提供([Google Adaptation](https://cloud.google.com/speech-to-text/docs/adaptation))。
- **コンプライアンスとプライバシー:** 不適切な言葉のフィルタリングを有効化し、適切なデータレジデンシーオプションを選択。

## エラー処理とパフォーマンス監視

- **エラータイプ:**
  - 非対応のファイルフォーマットまたはサイズ制限超過。
  - 無効/アクセス不可能な音声URL。
  - モデル選択/設定エラー。
  - 出力スキーマの不一致。

- **エラー処理:**
  - 処理前に入力を検証。
  - リトライロジックまたはフォールバックフローを実装。
  - エラーをログに記録し、分析ダッシュボードで監視。

- **パフォーマンス指標:**
  - 処理された音声の分数(コスト/使用量追跡用)。
  - トークン使用量(LLM対応ASRシステムの場合)。
  - レスポンス時間とスループット。

- [Kore.ai Model Analytics Dashboard](https://docs.kore.ai/agent-platform/settings/monitoring/analytics/model-analytics-dashboard/)  
- [Google Speech-to-Text Monitoring](https://cloud.google.com/monitoring)

## プロバイダー比較

| プロバイダー            | 主要機能                                                                   | 言語        | 注記/リンク |
|---------------------|-------------------------------------------------------------------------|------------|-----------|
| **OpenAI Whisper**  | 多言語、英語への翻訳、堅牢なASR、不適切な言葉のフィルタリング                  | 50以上      | [Whisper Docs](https://platform.openai.com/docs/guides/speech-to-text) |
| **Google Speech-to-Text** | 125以上の言語、ストリーミングとバッチ、話者分離、適応、フィルタリング    | 125以上     | [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text) |
| **Azure Speech**    | リアルタイム/バッチ、カスタムモデル、業界適応、CLIとSDK                       | 100以上     | [Azure Speech Overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text) |
| **Rev AI**          | 非同期とストリーミング、人間と機械の文字起こし、インサイト、低WER              | 58以上      | [Rev AI](https://www.rev.ai/) |
| **LiveKit**         | プラグイン可能なモデル(AssemblyAI、Cartesia、Deepgram)、自動モデル選択      | モデル依存  | [LiveKit STT](https://docs.livekit.io/agents/models/stt/) |
| **VectorShift**     | ノードベースのパイプライン、変数/アップロード入力、LLM統合                    | プロバイダー依存| [VectorShift Docs](https://docs.vectorshift.ai/platform/pipelines/multi-modal/speech-to-text) |

## 実例

### 例1:会議文字起こしノード(Kore.ai)

**プロンプト:**  
「直接話法を使用し、問題や課題に関連する語彙を強調してください。」

**入力:**
```json
{
  "audioFile": "https://example.com/meeting-2024-06-10.mp3"
}
```

**出力:**
```
話者1:APIゲートウェイで繰り返し問題が発生しています。
話者2:主な課題は外部認証の統合です。
```
([Kore.ai Example](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))

### 例2:Google Speech-to-Text API(Node.js)

**コードサンプル:**
```javascript
const speech = require('@google-cloud/speech');
const client = new speech.SpeechClient();

async function transcribe() {
  const audio = { uri: 'gs://cloud-samples-data/speech/brooklyn_bridge.raw' };
  const config = { encoding: 'LINEAR16', sampleRateHertz: 16000, languageCode: 'en-US' };
  const request = { audio, config };
  const [response] = await client.recognize(request);
  const transcription = response.results.map(r => r.alternatives[0].transcript).join('\n');
  console.log(`Transcription: ${transcription}`);
}

transcribe();
```
[Full Google Codelab](https://codelabs.developers.google.com/codelabs/cloud-speech-text-node)

### 例3:LiveKit STTモデルの使用(Python)

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="assemblyai/universal-streaming:en",
    # ... llm, tts, etc.
)
```
[LiveKit Usage Docs](https://docs.livekit.io/agents/models/stt/#usage)

## 技術的注意事項とエッジケース

- **トークン制限:** 一部のASRモデルには入力トークン制限がある(例:Whisper:224トークン)。
- **エッジ音声ケース:**  
  - サイズ制限に近いファイルの場合、論理的な境界でセグメント化。
  - 分割時に文の整合性を維持。
- **不適切な言葉とコンテンツフィルタリング:**  
  - 一部のモデルではデフォルトで削除、他では設定可能。
- **話者分離:**  
  - 普遍的にサポートされていない—プロバイダーで確認