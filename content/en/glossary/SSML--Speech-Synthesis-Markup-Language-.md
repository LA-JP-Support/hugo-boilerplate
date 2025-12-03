---
title: "SSML (Speech Synthesis Markup Language)"
translationKey: "ssml-speech-synthesis-markup-language"
description: "SSML is an XML-based markup language for controlling synthetic speech output, including pronunciation, intonation, pacing, and emotion, used by major TTS providers."
keywords: ["SSML", "Speech Synthesis Markup Language", "Text-to-Speech", "TTS", "W3C", "prosody", "phonetics", "voice user interfaces", "AI chatbot"]
category: "AI Chatbot & Automation / Text-to-Speech / Voice User Interfaces"
type: "glossary"
date: 2025-12-03
draft: false
---
## What is SSML?

Speech Synthesis Markup Language (SSML) is an XML-based markup standard developed and maintained by the [W3C](https://www.w3.org/TR/speech-synthesis11/). SSML enables developers, designers, and linguists to describe precisely how a piece of text should be rendered in synthetic (machine-generated) speech. This is essential for applications that require a natural, expressive, and contextually appropriate spoken output.

**Key Features:**
- Fine-grained control over pronunciation (using phonetic alphabets like IPA/XSAMPA)
- Direct specification of prosody: pitch, rate, volume, and emphasis
- Insertion of natural pauses, sentence and paragraph structuring
- Explicit handling of special content (dates, times, acronyms, currency, telephone numbers)
- Ability to switch between different voices or languages mid-stream
- Embedding of external audio files
- Support for vendor-specific extensions (e.g., emotions and roles in Amazon Alexa, neural voice styles in Azure)

**Industry Adoption:**  
SSML is the de facto standard for all major cloud TTS providers, including:
- [Amazon Alexa Skills Kit](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs/ssml)
- [Microsoft Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)
- [IBM Watson Text-to-Speech](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-ssml)
- [Speechify](https://docs.sws.speechify.com/docs/features/ssml)

## Purpose and Importance

### Why Use SSML?

Text-to-speech (TTS) systems convert plain text into spoken audio. Without SSML, TTS outputs are often robotic, monotonous, and prone to mispronunciations or awkward intonation. SSML solves these issues by allowing the creator to:

- **Control Prosody:** Adjust how text is spoken by setting attributes for pitch, rate (speed), and volume, making speech sound more human.
- **Improve Pronunciation:** Override default pronunciations for technical terms, brand names, or foreign words using phonetic alphabets or substitutions.
- **Clarify Special Content:** Direct explicit reading of dates, times, abbreviations, numbers, emails, and currency.
- **Add Expressiveness:** Inject emphasis, style, and emotional nuance using attributes or vendor-specific extensions.
- **Enhance Accessibility:** Make speech output clearer and more understandable for users relying on assistive technology.
- **Insert Pauses and Audio:** Use pauses to match natural conversational flow or insert sounds/music to enhance user experience.
- **Switch Voices or Languages:** Seamlessly transition between different voices, accents, or languages within the same output.

**Common Problems Solved:**
- Flat, robotic-sounding speech
- Mispronunciation of uncommon or ambiguous words
- Unnatural pacing or sentence grouping
- Inability to convey emotion or style
- Difficulty understanding numbers, dates, or special sequences

**Platform Notes:**
- [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html) supports a subset of W3C SSML, with Alexa-specific tags for emotion and style.
- [Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml) and [Microsoft Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup) both implement vendor-specific extensions and neural voice technologies.

## SSML: Basic Structure and Usage

### The Root Element: `<speak>`

All valid SSML documents begin with the `<speak>` root element, which defines the boundaries of the speech synthesis content. This is required by all TTS engines that support SSML.

```xml
<speak>
  Welcome to your AI assistant.
</speak>
```

- **Tip:** Omitting the `<speak>` tag will result in errors or the TTS engine falling back to plain text rendering.

**Provider Documentation:**  
- [Google Cloud SSML Syntax](https://cloud.google.com/text-to-speech/docs/ssml)
- [Amazon Alexa SSML Syntax](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)
- [Microsoft Azure SSML Overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup)

## Core SSML Tags and Features

### Overview Table: Common SSML Tags

| Tag           | Purpose                                        | Typical Attributes                | Supported By                |
|---------------|------------------------------------------------|-----------------------------------|-----------------------------|
| `<speak>`     | Encloses SSML content (root)                   | N/A                               | All providers               |
| `<break>`     | Inserts a pause                                | `time`, `strength`                | All providers               |
| `<prosody>`   | Modifies pitch, rate, volume                   | `pitch`, `rate`, `volume`         | All providers               |
| `<emphasis>`  | Adds emphasis to enclosed text                 | `level`                           | All providers               |
| `<say-as>`    | Specifies interpretation of special content    | `interpret-as`, `format`, `detail`| All providers               |
| `<phoneme>`   | Specifies phonetic pronunciation               | `alphabet`, `ph`                  | All providers               |
| `<sub>`       | Substitutes alias text for enclosed text       | `alias`                           | All providers               |
| `<audio>`     | Inserts audio file                             | `src`, `clipBegin`, etc.          | All, with limitations       |
| `<voice>`     | Changes speaker characteristics/persona        | `name`, `language`, `gender`      | All providers               |
| `<p>`, `<s>`  | Paragraph and sentence structure               | N/A                               | All providers               |
| `<lang>`      | Specifies language for enclosed text           | `xml:lang`                        | All providers               |

**Full Supported Tag List:**  
- [Amazon Alexa Supported SSML Tags](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)
- [Google Cloud Supported SSML Tags](https://cloud.google.com/text-to-speech/docs/ssml#supported_ssml)
- [Microsoft Azure Supported SSML Tags](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#ssml-supported-elements)

### Tag-by-Tag Reference with Deep Dives

#### `<speak>`: Root Element

- **Purpose:** Required root for all SSML documents.
- **Example:**
    ```xml
    <speak>
      This is a simple SSML example.
    </speak>
    ```
- **Best Practice:** Always enclose your entire SSML script in `<speak>` tags. Provider SDKs (e.g., Alexa SDKs for Node.js/Java) may wrap this for you, but explicit markup is safest for cross-platform compatibility ([source](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#ssml-supported)).

#### `<break>`: Insert Pauses

- **Purpose:** Adds a pause or controls the boundary between words or phrases.
- **Attributes:**
    - `time`: Exact pause duration (e.g., "500ms", "2s")
    - `strength`: Relative pause strength ("none", "x-weak", "weak", "medium", "strong", "x-strong")
- **Example:**
    ```xml
    <speak>
      Please wait.<break time="1s"/>Processing your request.
    </speak>
    ```
- **Provider Nuances:**  
    - Google Cloud and Amazon Alexa both support the `time` and `strength` attributes, but maximum/minimum pause values may differ ([Google docs](https://cloud.google.com/text-to-speech/docs/ssml#break-tag), [Alexa docs](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#break)).
    - Microsoft Azure supports `<break>` for fine pause control ([Azure docs](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#break-element)).

#### `<prosody>`: Control Pitch, Rate, Volume

- **Purpose:** Changes expressiveness of speech.
- **Attributes:**
    - `pitch`: "x-low", "low", "medium", "high", "x-high", or percentage (e.g., "+20%")
    - `rate`: "x-slow", "slow", "medium", "fast", "x-fast", or percentage (e.g., "-20%")
    - `volume`: "silent", "x-soft", "soft", "medium", "loud", "x-loud", decibel (e.g., "-6dB"), or percentage
- **Example:**
    ```xml
    <speak>
      <prosody pitch="high" rate="fast" volume="+20%">
        This is spoken with higher pitch, faster, and louder.
      </prosody>
    </speak>
    ```
- **Best Practice:** Avoid extreme values; subtle changes produce more natural speech ([Google best practices](https://cloud.google.com/text-to-speech/docs/ssml#prosody-tag), [Azure best practices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#prosody-element)).

#### `<emphasis>`: Highlight Words

- **Purpose:** Increases or reduces emphasis on specific words/phrases.
- **Attribute:** `level` ("strong", "moderate", "reduced")
- **Example:**
    ```xml
    <speak>
      You must <emphasis level="strong">complete</emphasis> the task.
    </speak>
    ```
- **Nuances:** Some TTS engines may interpret emphasis differently, and overuse can make speech sound unnatural ([Amazon Alexa emphasis docs](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#emphasis)).

#### `<say-as>`: Interpret Content Type

- **Purpose:** Directs TTS to read text as a specific type (e.g., date, time, currency, telephone, characters).
- **Attributes:**
    - `interpret-as`: Accepts values such as "cardinal", "ordinal", "characters", "date", "time", "telephone", "currency", "fraction", "unit", "expletive".
    - `format`, `detail`: For dates/times, defines structure.
- **Examples:**
    - Acronym as characters:
        ```xml
        <speak>
          <say-as interpret-as="characters">SSML</say-as>
        </speak>
        ```
    - Date:
        ```xml
        <speak>
          <say-as interpret-as="date" format="yyyymmdd" detail="2">20230610</say-as>
        </speak>
        ```
    - Currency:
        ```xml
        <speak>
          <say-as interpret-as="currency" language="en-US">$19.99</say-as>
        </speak>
        ```
- **Full Attribute Documentation:**  
  - [Google say-as](https://cloud.google.com/text-to-speech/docs/ssml#say-as-tag)
  - [Amazon Alexa say-as](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#say-as)

#### `<phoneme>`: Custom Pronunciation

- **Purpose:** Specifies exact pronunciation using phonetic alphabets (IPA, XSAMPA, etc.).
- **Attributes:**
    - `alphabet`: E.g., "ipa", "x-sampa"
    - `ph`: Phonetic string
- **Example:**
    ```xml
    <speak>
      <phoneme alphabet="ipa" ph="ˈniːʃ">niche</phoneme>
    </speak>
    ```
- **Best Practice:** Use [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) for clarity; validate with [TTS provider tools](https://speech.microsoft.com/portal/voicegallery).
- **Docs:** [Google phoneme](https://cloud.google.com/text-to-speech/docs/ssml#phoneme-tag), [Alexa phoneme](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#phoneme)

#### `<sub>`: Substitute Text

- **Purpose:** Reads the alias value instead of the enclosed text.
- **Attribute:** `alias`
- **Example:**
    ```xml
    <speak>
      Welcome to the <sub alias="World Wide Web Consortium">W3C</sub>.
    </speak>
    ```
- **Use Cases:** Brand names, acronyms, foreign words.
- **Docs:** [Google sub](https://cloud.google.com/text-to-speech/docs/ssml#sub-tag), [Alexa sub](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#sub)

#### `<audio>`: Insert Audio Clips

- **Purpose:** Embeds recorded audio in speech output (e.g., effects, music).
- **Attribute:** `src` (HTTPS URL)
- **Example:**
    ```xml
    <speak>
      Please listen to this sound. <audio src="https://www.example.com/sound.mp3">Unable to play audio.</audio>
    </speak>
    ```
- **Provider Limitations:**  
  - [Google Cloud](https://cloud.google.com/text-to-speech/docs/ssml#audio-tag): Only certain formats supported, time limits may apply.
  - [Amazon Alexa](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#audio): 240-second max, HTTPS required, size limits.
  - [Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-structure#audio-element): Supported with restrictions.

#### `<voice>`: Change Voice or Persona

- **Purpose:** Switches to a different voice, language, or persona.
- **Attributes:** `name`, `language`, `gender`
- **Example:**
    ```xml
    <speak>
      <voice name="en-US-Wavenet-D">Hello, I am the default voice.</voice>
      <voice name="en-GB-Wavenet-B">And I am a British voice.</voice>
    </speak>
    ```
- **Vendor Extensions:**  
  - Azure supports [neural voice styles and roles](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#style-attribute).
  - Alexa supports [emotion and domain](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion).

#### `<p>` and `<s>`: Structure Text

- **Purpose:** Defines paragraphs (`<p>`) and sentences (`<s>`) for better pacing and grouping.
- **Example:**
    ```xml
    <speak>
      <p>
        <s>This is the first sentence.</s>
        <s>This is the second sentence.</s>
      </p>
    </speak>
    ```

#### `<lang>`: Specify Language

- **Purpose:** Specifies language for a text segment, enabling proper pronunciation and accent.
- **Attribute:** `xml:lang`
- **Example:**
    ```xml
    <speak>
      Here is a word in French: <lang xml:lang="fr-FR">bonjour</lang>.
    </speak>
    ```
- **Note:** Not all voices support all languages; check provider [language support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts).

### Provider-Specific Extensions

- **Amazon Alexa:**  
  - `<amazon:emotion>`: Adds "excited" or "disappointed" emotion ([docs](https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion)).
  - `<amazon:domain>`: Changes delivery style (e.g., "news", "music", "conversational").
- **Microsoft Azure:**  
  - `<mstts:express-as>`: Neural voice styles/roles ([docs](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#microsoft-extensions)).
- **Speechify:**  
  - `<speechify:style>`: Proprietary style control ([docs](https://docs.sws.speechify.com/docs/features/ssml)).

## Practical SSML Examples

### Example 1: Comprehensive TTS Output

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
**Expected Output:**  
"Welcome to the demo. [pause] Your appointment is on June tenth, twenty

