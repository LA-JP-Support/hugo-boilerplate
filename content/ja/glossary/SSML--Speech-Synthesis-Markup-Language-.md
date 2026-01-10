---
title: SSML(音声合成マークアップ言語)
translationKey: ssml-speech-synthesis-markup-language
description: SSMLは、合成音声の出力を制御するためのXMLベースのマークアップ言語で、発音、イントネーション、ペース、感情などを調整でき、主要なTTSプロバイダーで使用されています。
keywords:
- SSML
- 音声合成マークアップ言語
- Text-to-Speech
- TTS
- W3C
- プロソディ
- 音声学
- 音声ユーザーインターフェース
- AIチャットボット
category: AI Chatbot & Automation / Text-to-Speech / Voice User Interfaces
type: glossary
date: '2025-12-19'
lastmod: '2025-12-19'
draft: false
e-title: SSML (Speech Synthesis Markup Language)
term: エスエスエムエル(おんせいごうせいマークアップげんご)
url: "/ja/glossary/SSML--Speech-Synthesis-Markup-Language-/"
---
## SSMLとは?

Speech Synthesis Markup Language(SSML)は、W3Cによって開発・維持されているXMLベースのマークアップ標準であり、開発者、デザイナー、言語学者がテキストを合成音声(機械生成音声)でどのようにレンダリングするかを正確に制御できるようにします。SSMLは、AIチャットボットや音声アシスタントから、アクセシビリティツールやインタラクティブ音声応答システムまで、自然で表現豊かな、文脈に適した音声出力を必要とするアプリケーションに不可欠です。

SSMLがない場合、テキスト読み上げ(TTS)出力はロボット的で単調になりがちで、発音ミスや不自然なイントネーションが発生しやすくなります。SSMLは、音声アルファベット(IPA、X-SAMPA)を使用した発音の細かい制御、韻律仕様(ピッチ、速度、音量、強調)、自然な間の挿入と文構造、特殊コンテンツ(日付、時刻、頭字語、通貨)の明示的な処理、音声と言語の途中切り替え、音声ファイルの埋め込みを提供することで、これらの問題を解決します。

**業界での採用:**SSMLは、Amazon Alexa Skills Kit、Google Cloud Text-to-Speech、Microsoft Azure Speech Service、IBM Watson Text-to-Speech、Speechifyを含むすべての主要なクラウドTTSプロバイダーで事実上の標準となっています。

## 主要機能

### 韻律制御

ピッチ、速度、音量の属性を設定してテキストの読み上げ方を調整し、音声をより人間的で表現豊かにします。微妙な韻律の変化は、自然さとエンゲージメントを劇的に向上させます。

### 発音管理

専門用語、ブランド名、外国語の単語について、音声アルファベットやテキスト置換を使用してデフォルトの発音を上書きします。これにより、プロフェッショナルなアプリケーションでの恥ずかしい発音ミスを防ぎます。

### 特殊コンテンツの処理

日付、時刻、略語、数字、メールアドレス、通貨を明示的に読み上げます。SSMLは「12/25」を「12月25日」として、「$19.99」を「19ドル99セント」として読み上げることを保証します。

### 表現力とスタイル

属性やベンダー固有の拡張機能を使用して、強調、感情的なニュアンス、スタイルのバリエーションを注入します。Amazon Alexaは興奮や失望の感情をサポートし、Azureはニュース読み上げ、カスタマーサービス、陽気な配信のためのニューラル音声スタイルを提供します。

### アクセシビリティの向上

支援技術に依存するユーザーのために音声出力をより明確で理解しやすくし、視覚障害のあるユーザーの理解を向上させます。

### 音声統合

自然な会話の流れに合った間を挿入したり、サウンドや音楽を埋め込んでユーザー体験を向上させます。バックグラウンドミュージック、効果音、音声キューは音声インタラクションを豊かにします。

## 基本構造

### ルート要素: `<speak>`

すべての有効なSSMLドキュメントは、音声合成コンテンツの境界を定義する`<speak>`ルート要素で始まります。これは、SSMLをサポートするすべてのTTSエンジンで必須です。

```xml
<speak>
  Welcome to your AI assistant.
</speak>
```

`<speak>`タグを省略すると、エラーが発生するか、TTSエンジンがプレーンテキストレンダリングにフォールバックします。

## 必須のSSMLタグ

### `<break>`: 間を挿入

単語やフレーズの間に間を追加したり、境界を制御します。

**属性:**- `time`: 正確な間の長さ(例:「500ms」、「2s」)
- `strength`: 相対的な間(「none」、「x-weak」、「weak」、「medium」、「strong」、「x-strong」)

```xml
<speak>
  Please wait.<break time="1s"/>Processing your request.
</speak>
```

### `<prosody>`: ピッチ、速度、音量を制御

音声の表現力を変更します。

**属性:**- `pitch`: 「x-low」、「low」、「medium」、「high」、「x-high」、またはパーセンテージ(「+20%」)
- `rate`: 「x-slow」、「slow」、「medium」、「fast」、「x-fast」、またはパーセンテージ(「-20%」)
- `volume`: 「silent」、「x-soft」、「soft」、「medium」、「loud」、「x-loud」、デシベル(「-6dB」)、またはパーセンテージ

```xml
<speak>
  <prosody pitch="high" rate="fast" volume="+20%">
    This is spoken with higher pitch, faster, and louder.
  </prosody>
</speak>
```

**ベストプラクティス:**極端な値は避けてください。微妙な変化がより自然な音声を生み出します。

### `<emphasis>`: 単語を強調

特定の単語やフレーズの強調を増減します。

```xml
<speak>
  You must <emphasis level="strong">complete</emphasis> the task.
</speak>
```

レベル:「strong」、「moderate」、「reduced」

### `<say-as>`: コンテンツタイプを解釈

TTSにテキストを特定のタイプとして読み上げるよう指示します。

**一般的なinterpret-as値:**- 「cardinal」: 数字(123 → 「123」)
- 「ordinal」: 序数(1st → 「1番目」)
- 「characters」: スペルアウト(「SSML」 → 「エス エス エム エル」)
- 「date」: フォーマット指定付きの日付
- 「time」: 時刻値
- 「telephone」: 電話番号
- 「currency」: 通貨金額
- 「fraction」: 分数(「3/4」 → 「4分の3」)
- 「unit」: 測定値

**例:**```xml
<speak>
  <say-as interpret-as="characters">SSML</say-as>
</speak>
```

```xml
<speak>
  <say-as interpret-as="date" format="yyyymmdd">20230610</say-as>
</speak>
```

```xml
<speak>
  <say-as interpret-as="currency" language="en-US">$19.99</say-as>
</speak>
```

### `<phoneme>`: カスタム発音

音声アルファベットを使用して正確な発音を指定します。

**属性:**- `alphabet`: 「ipa」、「x-sampa」
- `ph`: 音声文字列

```xml
<speak>
  <phoneme alphabet="ipa" ph="ˈniːʃ">niche</phoneme>
</speak>
```

### `<sub>`: テキストを置換

囲まれたテキストの代わりにエイリアス値を読み上げます。

```xml
<speak>
  Welcome to the <sub alias="World Wide Web Consortium">W3C</sub>.
</speak>
```

**使用例:**ブランド名、頭字語、外国語

### `<audio>`: 音声クリップを挿入

音声出力に録音された音声(効果音、音楽)を埋め込みます。

```xml
<speak>
  Please listen to this sound.
  <audio src="https://www.example.com/sound.mp3">
    Unable to play audio.
  </audio>
</speak>
```

**プロバイダーの制限:**- Google Cloud: フォーマットと時間の制限が適用されます
- Amazon Alexa: 最大240秒、HTTPS必須、サイズ制限あり
- Azure: 制限付きでサポート

### `<voice>`: 音声またはペルソナを変更

別の音声、言語、またはペルソナに切り替えます。

```xml
<speak>
  <voice name="en-US-Wavenet-D">Hello, I am the default voice.</voice>
  <voice name="en-GB-Wavenet-B">And I am a British voice.</voice>
</speak>
```

### `<p>`と`<s>`: テキストを構造化

段落(`<p>`)と文(`<s>`)を定義して、より良いペーシングとグループ化を実現します。

```xml
<speak>
  <p>
    <s>This is the first sentence.</s>
    <s>This is the second sentence.</s>
  </p>
</speak>
```

### `<lang>`: 言語を指定

テキストセグメントの言語を指定し、適切な発音とアクセントを可能にします。

```xml
<speak>
  Here is a word in French: <lang xml:lang="fr-FR">bonjour</lang>.
</speak>
```

## プロバイダー固有の拡張機能

### Amazon Alexa

**`<amazon:emotion>`:**「excited」または「disappointed」の感情を追加

```xml
<speak>
  <amazon:emotion name="excited" intensity="medium">
    Congratulations on your achievement!
  </amazon:emotion>
</speak>
```

**`<amazon:domain>`:**配信スタイルを変更(ニュース、音楽、会話)

### Microsoft Azure

**`<mstts:express-as>`:**ニューラル音声スタイルとロール

```xml
<speak>
  <mstts:express-as style="cheerful">
    Welcome to our service!
  </mstts:express-as>
</speak>
```

スタイルには以下が含まれます:cheerful、sad、angry、fearful、friendly、hopeful、newscast、customer-service

### Speechify

**`<speechify:style>`:**読書体験を向上させるための独自のスタイル制御

## 実用例

```xml
<speak>
  Welcome to the demo.
  <break time="500ms"/>
  Your appointment is on
  <say-as interpret-as="date" format="yyyymmdd">20230610</say-as>.
  The amount due is
  <say-as interpret-as="currency" language="en-US">$19.99</say-as>.
  For assistance, call
  <say-as interpret-as="telephone">18001234567</say-as>.
  <prosody rate="slow">Thank you for using our service.</prosody>
</speak>
```

**期待される出力:**「Welcome to the demo. [間] Your appointment is on June tenth, twenty twenty-three. The amount due is nineteen dollars and ninety-nine cents. For assistance, call one eight hundred one two three four five six seven. [遅く] Thank you for using our service.」

## 一般的な使用例

### AIチャットボットと仮想アシスタント

自然な響きの応答、適切な間、感情表現で会話型AIを強化

### カスタマーサービスIVRシステム

明確な発音とプロフェッショナルなトーンで発信者をメニューに案内

### アクセシビリティアプリケーション

スクリーンリーダーや支援技術のための高品質な音声出力を提供

### eラーニングプラットフォーム

多様な音声と適切なペーシングで魅力的な教育コンテンツを作成

### オーディオブック制作

キャラクターの音声と感情表現を持つ自然な響きのナレーションを生成

### スマートホームデバイス

適切な文脈と感情で通知と応答を配信

## ベストプラクティス

**微妙な調整:**小さな韻律の変化は、極端な変更よりも効果的です**プラットフォーム間でテスト:**ターゲットTTSプロバイダー間でSSMLレンダリングを検証**音声記号は控えめに使用:**必要な場合にのみ発音を上書き**論理的に構造化:**自然なペーシングのために`<p>`と`<s>`タグを使用**速度のバランス:**自然な速度を維持し、過度に速いまたは遅い音声を避ける**音声品質:**埋め込み音声ファイルが適切にエンコードされ、ホストされていることを確認**アクセシビリティ重視:**支援技術を使用するユーザーを含むすべてのユーザーを考慮

## 実装上の考慮事項

**プラットフォーム互換性:**プロバイダーによってサポートされるタグのサブセットと拡張機能が異なります**フォールバックコンテンツ:**サポートされていないタグのためのフォールバックテキストを提供**文字数制限:**プラットフォーム固有のテキスト長制限に注意**処理オーバーヘッド:**複雑なSSMLは応答時間を増加させる可能性があります**コスト管理:**一部のプロバイダーはマークアップを含む文字数に基づいて課金します**テストプロトコル:**デバイスとプラットフォーム間で包括的なテストを確立

## 参考文献


1. W3C. (n.d.). Speech Synthesis Markup Language (SSML) Version 1.1. W3C Technical Report.

2. Amazon. (n.d.). Alexa: SSML Reference. Amazon Developer Documentation.

3. Google Cloud. (n.d.). SSML Documentation. Google Cloud Documentation.

4. Microsoft. (n.d.). Azure: Speech Synthesis Markup. Microsoft Learn.

5. IBM Watson. (n.d.). SSML Elements. IBM Cloud Documentation.

6. Speechify. (n.d.). SSML Features. Speechify Documentation.

7. Wikipedia. (n.d.). International Phonetic Alphabet (IPA). Wikipedia.

8. Microsoft. (n.d.). Azure Speech Voice Gallery. URL: https://speech.microsoft.com/portal/voicegallery

9. Google Cloud. (n.d.). Supported SSML Elements. Google Cloud Documentation.

10. Microsoft. (n.d.). Azure Supported SSML Elements. Microsoft Learn.

11. Adaptive Cards. (n.d.). Adaptive Cards Designer. URL: https://adaptivecards.io/designer/
