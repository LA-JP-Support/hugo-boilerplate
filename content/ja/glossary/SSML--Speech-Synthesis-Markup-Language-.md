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
date: 2025-12-03
draft: false
term: エスエスエムエル(おんせいごうせいマークアップげんご)
reading: SSML(音声合成マークアップ言語)
kana_head: その他
e-title: SSML (Speech Synthesis Markup Language)
---

## SSMLとは？

Speech Synthesis Markup Language（SSML）は、[W3C](https://www.w3.org/TR/speech-synthesis11/)によって開発・維持されているXMLベースのマークアップ標準です。SSMLにより、開発者、デザイナー、言語学者は、テキストが合成音声（機械生成音声）でどのように表現されるべきかを正確に記述できます。これは、自然で表現豊かな、文脈に適した音声出力を必要とするアプリケーションにとって不可欠です。

**主な機能:**
- 発音の細かい制御(IPA/XSAMPAなどの音声記号を使用)
- プロソディの直接指定:ピッチ、速度、音量、強調
- 自然な間の挿入、文や段落の構造化
- 特殊コンテンツの明示的な処理(日付、時刻、頭字語、通貨、電話番号)
- 異なる音声や言語への途中切り替え機能
- 外部音声ファイルの埋め込み
- ベンダー固有の拡張機能のサポート(例:Amazon Alexaの感情とロール、Azureのニューラル音声スタイル)

**業界での採用:**  
SSMLは、以下を含むすべての主要なクラウドTTSプロバイダーの事実上の標準です:
- [Amazon Alexa Skills Kit](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs/ssml)
- [Microsoft Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)
- [IBM Watson Text-to-Speech](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-ssml)
- [Speechify](https://docs.sws.speechify.com/docs/features/ssml)

## 目的と重要性

### なぜSSMLを使用するのか?

テキスト読み上げ(TTS)システムは、プレーンテキストを音声に変換します。SSMLがない場合、TTS出力はしばしばロボット的で単調、発音ミスや不自然なイントネーションが発生しやすくなります。SSMLは、作成者が以下を可能にすることで、これらの問題を解決します:

- **プロソディの制御:** ピッチ、速度、音量の属性を設定することで、テキストの話し方を調整し、音声をより人間らしくします。
- **発音の改善:** 音声記号や置換を使用して、技術用語、ブランド名、外来語のデフォルト発音を上書きします。
- **特殊コンテンツの明確化:** 日付、時刻、略語、数字、メール、通貨の明示的な読み上げを指示します。
- **表現力の追加:** 属性やベンダー固有の拡張機能を使用して、強調、スタイル、感情的なニュアンスを注入します。
- **アクセシビリティの向上:** 支援技術に依存するユーザーにとって、音声出力をより明確で理解しやすくします。
- **間と音声の挿入:** 自然な会話の流れに合わせて間を使用したり、ユーザー体験を向上させるために音や音楽を挿入します。
- **音声や言語の切り替え:** 同じ出力内で異なる音声、アクセント、言語間をシームレスに移行します。

**解決される一般的な問題:**
- 平坦でロボット的な音声
- 珍しい単語や曖昧な単語の発音ミス
- 不自然なペースや文のグループ化
- 感情やスタイルを伝えることができない
- 数字、日付、特殊なシーケンスの理解困難

**プラットフォームに関する注意:**
- [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html)は、W3C SSMLのサブセットをサポートし、感情とスタイルのためのAlexa固有のタグを持っています。
- [Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml)と[Microsoft Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)は、どちらもベンダー固有の拡張機能とニューラル音声技術を実装しています。

## SSML:基本構造と使用方法

### ルート要素:`<speak>`

すべての有効なSSMLドキュメントは、音声合成コンテンツの境界を定義する`<speak>`ルート要素で始まります。これは、SSMLをサポートするすべてのTTSエンジンで必須です。

```xml
<speak>
  Welcome to your AI assistant.
</speak>
```

- **ヒント:** `<speak>`タグを省略すると、エラーが発生するか、TTSエンジンがプレーンテキストレンダリングにフォールバックします。

**プロバイダードキュメント:**  
- [Google Cloud SSML構文](https://cloud.google.com/text-to-speech/docs/ssml)
- [Amazon Alexa SSML構文](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)
- [Microsoft Azure SSML概要](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)

## コアSSMLタグと機能

### 概要表:一般的なSSMLタグ

| タグ           | 目的                                        | 一般的な属性                | サポートプロバイダー                |
|---------------|------------------------------------------------|-----------------------------------|-----------------------------|
| `<speak>`     | SSMLコンテンツを囲む(ルート)                   | N/A                               | すべてのプロバイダー               |
| `<break>`     | 間を挿入                                | `time`、`strength`                | すべてのプロバイダー               |
| `<prosody>`   | ピッチ、速度、音量を変更                   | `pitch`、`rate`、`volume`         | すべてのプロバイダー               |
| `<emphasis>`  | 囲まれたテキストに強調を追加                 | `level`                           | すべてのプロバイダー               |
| `<say-as>`    | 特殊コンテンツの解釈を指定    | `interpret-as`、`format`、`detail`| すべてのプロバイダー               |
| `<phoneme>`   | 音声発音を指定               | `alphabet`、`ph`                  | すべてのプロバイダー               |
| `<sub>`       | 囲まれたテキストのエイリアステキストを置換       | `alias`                           | すべてのプロバイダー               |
| `<audio>`     | 音声ファイルを挿入                             | `src`、`clipBegin`など          | すべて、制限あり       |
| `<voice>`     | 話者の特性/ペルソナを変更        | `name`、`language`、`gender`      | すべてのプロバイダー               |
| `<p>`、`<s>`  | 段落と文の構造               | N/A                               | すべてのプロバイダー               |
| `<lang>`      | 囲まれたテキストの言語を指定           | `xml:lang`                        | すべてのプロバイダー               |

**完全なサポートタグリスト:**  
- [Amazon Alexaサポート対象SSMLタグ](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)
- [Google Cloudサポート対象SSMLタグ](https://cloud.google.com/text-to-speech/docs/ssml#supported_ssml)
- [Microsoft Azureサポート対象SSMLタグ](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#ssml-supported-elements)

### タグごとの詳細リファレンス

#### `<speak>`:ルート要素

- **目的:** すべてのSSMLドキュメントに必須のルート。
- **例:**
    ```xml
    <speak>
      This is a simple SSML example.
    </speak>
    ```
- **ベストプラクティス:** 常にSSMLスクリプト全体を`<speak>`タグで囲みます。プロバイダーSDK(例:Node.js/Java用Alexa SDK)がこれを自動的にラップする場合がありますが、クロスプラットフォーム互換性のためには明示的なマークアップが最も安全です([ソース](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported))。

#### `<break>`:間を挿入

- **目的:** 間を追加するか、単語やフレーズ間の境界を制御します。
- **属性:**
    - `time`:正確な間の長さ(例:"500ms"、"2s")
    - `strength`:相対的な間の強さ("none"、"x-weak"、"weak"、"medium"、"strong"、"x-strong")
- **例:**
    ```xml
    <speak>
      Please wait.<break time="1s"/>Processing your request.
    </speak>
    ```
- **プロバイダーのニュアンス:**  
    - Google CloudとAmazon Alexaは両方とも`time`と`strength`属性をサポートしていますが、最大/最小の間の値は異なる場合があります([Googleドキュメント](https://cloud.google.com/text-to-speech/docs/ssml#break-tag)、[Alexaドキュメント](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#break))。
    - Microsoft Azureは、細かい間の制御のために`<break>`をサポートしています([Azureドキュメント](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#break-element))。

#### `<prosody>`:ピッチ、速度、音量の制御

- **目的:** 音声の表現力を変更します。
- **属性:**
    - `pitch`:"x-low"、"low"、"medium"、"high"、"x-high"、またはパーセンテージ(例:"+20%")
    - `rate`:"x-slow"、"slow"、"medium"、"fast"、"x-fast"、またはパーセンテージ(例:"-20%")
    - `volume`:"silent"、"x-soft"、"soft"、"medium"、"loud"、"x-loud"、デシベル(例:"-6dB")、またはパーセンテージ
- **例:**
    ```xml
    <speak>
      <prosody pitch="high" rate="fast" volume="+20%">
        This is spoken with higher pitch, faster, and louder.
      </prosody>
    </speak>
    ```
- **ベストプラクティス:** 極端な値は避けてください。微妙な変化がより自然な音声を生み出します([Googleベストプラクティス](https://cloud.google.com/text-to-speech/docs/ssml#prosody-tag)、[Azureベストプラクティス](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#prosody-element))。

#### `<emphasis>`:単語を強調

- **目的:** 特定の単語/フレーズの強調を増減します。
- **属性:** `level`("strong"、"moderate"、"reduced")
- **例:**
    ```xml
    <speak>
      You must <emphasis level="strong">complete</emphasis> the task.
    </speak>
    ```
- **ニュアンス:** 一部のTTSエンジンは強調を異なる方法で解釈する場合があり、過度の使用は音声を不自然に聞こえさせる可能性があります([Amazon Alexa強調ドキュメント](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#emphasis))。

#### `<say-as>`:コンテンツタイプの解釈

- **目的:** TTSに特定のタイプ(例:日付、時刻、通貨、電話、文字)としてテキストを読むよう指示します。
- **属性:**
    - `interpret-as`:"cardinal"、"ordinal"、"characters"、"date"、"time"、"telephone"、"currency"、"fraction"、"unit"、"expletive"などの値を受け入れます。
    - `format`、`detail`:日付/時刻の場合、構造を定義します。
- **例:**
    - 頭字語を文字として:
        ```xml
        <speak>
          <say-as interpret-as="characters">SSML</say-as>
        </speak>
        ```
    - 日付:
        ```xml
        <speak>
          <say-as interpret-as="date" format="yyyymmdd" detail="2">20230610</say-as>
        </speak>
        ```
    - 通貨:
        ```xml
        <speak>
          <say-as interpret-as="currency" language="en-US">$19.99</say-as>
        </speak>
        ```
- **完全な属性ドキュメント:**  
  - [Google say-as](https://cloud.google.com/text-to-speech/docs/ssml#say-as-tag)
  - [Amazon Alexa say-as](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#say-as)

#### `<phoneme>`:カスタム発音

- **目的:** 音声記号(IPA、XSAMPAなど)を使用して正確な発音を指定します。
- **属性:**
    - `alphabet`:例:"ipa"、"x-sampa"
    - `ph`:音声文字列
- **例:**
    ```xml
    <speak>
      <phoneme alphabet="ipa" ph="ˈniːʃ">niche</phoneme>
    </speak>
    ```
- **ベストプラクティス:** 明確さのために[IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet)を使用し、[TTSプロバイダーツール](https://speech.microsoft.com/portal/voicegallery)で検証してください。
- **ドキュメント:** [Google phoneme](https://cloud.google.com/text-to-speech/docs/ssml#phoneme-tag)、[Alexa phoneme](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#phoneme)

#### `<sub>`:テキストの置換

- **目的:** 囲まれたテキストの代わりにエイリアス値を読みます。
- **属性:** `alias`
- **例:**
    ```xml
    <speak>
      Welcome to the <sub alias="World Wide Web Consortium">W3C</sub>.
    </speak>
    ```
- **使用例:** ブランド名、頭字語、外来語。
- **ドキュメント:** [Google sub](https://cloud.google.com/text-to-speech/docs/ssml#sub-tag)、[Alexa sub](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#sub)

#### `<audio>`:音声クリップの挿入

- **目的:** 音声出力に録音された音声を埋め込みます(例:効果音、音楽)。
- **属性:** `src`(HTTPS URL)
- **例:**
    ```xml
    <speak>
      Please listen to this sound. <audio src="https://www.example.com/sound.mp3">Unable to play audio.</audio>
    </speak>
    ```
- **プロバイダーの制限:**  
  - [Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml#audio-tag):特定のフォーマットのみサポート、時間制限が適用される場合があります。
  - [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#audio):最大240秒、HTTPS必須、サイズ制限あり。
  - [Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#audio-element):制限付きでサポート。

#### `<voice>`:音声またはペルソナの変更

- **目的:** 異なる音声、言語、またはペルソナに切り替えます。
- **属性:** `name`、`language`、`gender`
- **例:**
    ```xml
    <speak>
      <voice name="en-US-Wavenet-D">Hello, I am the default voice.</voice>
      <voice name="en-GB-Wavenet-B">And I am a British voice.</voice>
    </speak>
    ```
- **ベンダー拡張機能:**  
  - Azureは[ニューラル音声スタイルとロール](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#style-attribute)をサポートしています。
  - Alexaは[感情とドメイン](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion)をサポートしています。

#### `<p>`と`<s>`:テキストの構造化

- **目的:** より良いペースとグループ化のために段落(`<p>`)と文(`<s>`)を定義します。
- **例:**
    ```xml
    <speak>
      <p>
        <s>This is the first sentence.</s>
        <s>This is the second sentence.</s>
      </p>
    </speak>
    ```

#### `<lang>`:言語の指定

- **目的:** テキストセグメントの言語を指定し、適切な発音とアクセントを可能にします。
- **属性:** `xml:lang`
- **例:**
    ```xml
    <speak>
      Here is a word in French: <lang xml:lang="fr-FR">bonjour</lang>.
    </speak>
    ```
- **注意:** すべての音声がすべての言語をサポートしているわけではありません。プロバイダーの[言語サポート](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)を確認してください。

### プロバイダー固有の拡張機能

- **Amazon Alexa:**  
  - `<amazon:emotion>`:「excited」または「disappointed」の感情を追加([ドキュメント](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion))。
  - `<amazon:domain>`:配信スタイルを変更(例:"news"、"music"、"conversational")。
- **Microsoft Azure:**  
  - `<mstts:express-as>`:ニューラル音声スタイル/ロール([ドキュメント](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#microsoft-extensions))。
- **Speechify:**  
  - `<speechify:style>`:独自のスタイル制御([ドキュメント](https://docs.sws.speechify.com/docs/features/ssml))。

## 実用的なSSMLの例

### 例1:包括的なTTS出力

```xml
<speak>
  Welcome to the demo.
  <break time="500ms"/>
  Your appointment is on
  <say-as interpret-as="date" format="yyyymmdd">20230610</say-as>.
  The amount due is
  <say-as interpret-as="currency" language="en-US">$19.99</say-as>.
  For assistance, call <say-as interpret-as="telephone">18001234567</say-as>.
  <prosody rate="slow">Thank you for using our service.</prosody>
</speak>
```
**期待される出力:**  
「Welcome to the demo. [間] Your appointment is on June tenth, twenty