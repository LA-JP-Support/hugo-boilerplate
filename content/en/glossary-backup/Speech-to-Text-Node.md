---
title: "Speech-to-Text Node"
translationKey: "speech-to-text-node"
description: "A Speech-to-Text Node is a modular component in automation platforms and AI workflows that transcribes spoken language into machine-readable text using ASR."
keywords: ["Speech-to-Text Node", "Automatic Speech Recognition", "AI workflows", "Audio to Text", "Transcription"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## Overview

A **Speech-to-Text Node** forms the foundation of [conversational AI](/en/glossary/conversational-ai/), automation pipelines, and workflow systems by converting spoken language in audio files (voice recordings, calls, or video soundtracks) into accurate, structured text. This transcription can then be analyzed, summarized, translated, or used to trigger further automated processes.

**Typical Workflow:**
1. Receives audio input (as a file upload, URL, or variable in the workflow).
2. Processes the audio using an ASR model such as [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text), [Google Speech-to-Text](https://cloud.google.com/speech-to-text), [Azure Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text), or third-party providers like [Rev AI](https://www.rev.ai/).
3. Outputs a transcript (optionally with word-level timestamps, speaker labels, or translations).

**Role in Automation:**
- Enables chatbots to process voice queries.
- Transcribes meetings, interviews, or lectures for knowledge management.
- Automates content indexing and data extraction from voice interactions or media.
## Key Capabilities

- **Automatic Speech Recognition (ASR):** Converts audio to text using advanced models ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [LiveKit](https://docs.livekit.io/agents/models/stt/), [Rev AI](https://www.rev.ai/)).
- **Multilingual Support:** Transcribes speech in multiple languages and dialects ([Google Supported Languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages), [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text#supported-languages)).
- **Translation:** Translates non-English speech into English or other supported languages (provider-specific).
- **Custom Prompt Instructions:** Accepts instructions for transcription style, speaker labeling, terminology, or error handling.
- **Flexible Audio Input:** Accepts file uploads, URLs, or variables from previous workflow steps.
- **Large File Handling:** Processes files up to provider-specific limits (often 25 MB), with support for segmenting larger files.
- **Timestamps & Speaker Diarization:** Optionally includes word/utterance-level timing and speaker labels (see [LiveKit Plugins](https://docs.livekit.io/agents/models/stt/#plugins)).
- **Profanity Filtering:** Removes or masks offensive content according to configuration or model defaults.
- **Custom Vocabulary & Model Adaptation:** Improves recognition of domain-specific terms (see [Google Adaptation](https://cloud.google.com/speech-to-text/docs/adaptation)).
- **Structured Output (JSON):** Returns data in schemas suitable for downstream processing.

## How It Works

1. **Audio Input:**  
   - The node receives an audio file or URL (e.g., from user upload, cloud storage, or a previous workflow step).
   - Supported formats typically include MP3, WAV, MP4, M4A, WebM, MPGA, and MPEG ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [Rev AI](https://www.rev.ai/)).

2. **Model Selection & Preprocessing:**
   - Choose an ASR model/provider (e.g., Whisper, Google, Azure, AssemblyAI, Deepgram).
   - Configure language, translation, and additional features (timestamps, speaker IDs, custom prompts).

3. **Transcription Process:**
   - The selected ASR engine processes the audio, generating a text transcript.
   - Optional features: translation, profanity filtering, formatting, diarization.

4. **Output Handling:**
   - The node outputs the transcript (plain text or structured JSON).
   - The output is consumed by downstream steps—summarization, analysis, or user feedback.

**Diagram Example:**  
![Speech to Text Node Workflow](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/images/how-audio-to-text-works.png)  
([Source: Kore.ai Documentation](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))

**For LiveKit:**  
- [LiveKit Inference](https://docs.livekit.io/agents/models/stt/#inference) offers AssemblyAI, Cartesia Ink Whisper, and Deepgram Nova models with various language and specialty options.

## Supported Audio Formats & File Limits

- **Audio Formats:**  
  - M4A, MP3, WebM, MP4, MPGA, WAV, MPEG ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [Google](https://cloud.google.com/speech-to-text/docs/encoding), [Rev AI](https://www.rev.ai/)).

- **File Size Limits:**  
  - Typical maximum: **25 MB** per file (varies by provider).
  - Larger files must be split into segments ≤25 MB, ideally at logical sentence boundaries to preserve context and accuracy ([Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)).

> **Note:** Some platforms accept only URLs as input for security and scalability.

## Step-by-Step Configuration Guide

### Example: Configuring a Speech-to-Text Node (Kore.ai)

**Prerequisites:**
- Access to the automation platform (e.g., [Kore.ai](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/), [LiveKit](https://docs.livekit.io/agents/models/stt/), [Google Cloud](https://cloud.google.com/speech-to-text), [Azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text)).
- API key or integration credentials (if required).
- Audio files hosted at accessible URLs or provided by upload.

#### 1. Add the Node to Your Workflow
- Open your automation builder (e.g., Kore.ai bot flow designer).
- Locate and drag the **Speech-to-Text** (or **Audio to Text**) node into your workflow.

#### 2. Configure Node Properties
- **Node Name:** Assign a unique, descriptive name (e.g., “MeetingTranscription”).
- **Audio File Input:** Reference the variable holding the audio file URL, e.g., `{{context.steps.Start.MeetingAudioUrl}}`.
- **Model Selection:** Choose the ASR model/provider (e.g., OpenAI Whisper, AssemblyAI, Deepgram).
- **Feature Toggles:** Enable translation, timestamps, speaker diarization, or profanity filtering as required.

#### 3. Set Custom Prompt Instructions
- Define transcription instructions (e.g., style, speaker labels, error handling).
- Example:  
  ```
  Provide a clean transcript, omitting filler words, with clear speaker labels and correct technical terms.
  ```

#### 4. (Optional) Define JSON Schema for Output
- Specify a response schema for structured output.
- Example:
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

#### 5. Connect Success & Failure Paths
- **On Success:** Route to summarization, translation, or other downstream nodes.
- **On Failure:** Route to error handling or a fallback node.

#### 6. Test and Validate
- Run the workflow with sample inputs.
- Review the output for completeness and correctness.
- Adjust configuration as needed.

**Full Guide:** [Kore.ai Audio to Text Node Documentation](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)

## Configuration Parameters & Advanced Features

| Parameter        | Description                                                         | Example / Options                  |
|------------------|---------------------------------------------------------------------|------------------------------------|
| Audio Input      | URL or reference to uploaded audio file                             | `https://host/path/audio.mp3`      |
| Model            | ASR engine/model to use                                             | `OpenAI Whisper-1`, `Chirp 3`, `AssemblyAI Universal-Streaming` |
| Language Code    | Language for transcription (BCP-47 code)                            | `en-US`, `fr-FR`                   |
| Translation      | Enable translation to English (if supported)                        | `true` / `false`                   |
| Timestamps       | Include word/utterance-level timestamps                             | `true` / `false`                   |
| Speaker Labels   | Diarization, label speakers in multi-party audio                    | `true` / `false`                   |
| Profanity Filter | Remove or mask offensive words                                      | `true` / `false`                   |
| Prompt           | Custom instructions for transcription style                         | See above                          |
| JSON Schema      | Structured output for downstream processing                         | See above                          |
| Custom Vocab     | List of domain-specific words to bias recognition                   | `["AcmeCorp", "API Gateway"]`      |
| Input Variable   | Context variable holding input audio file URL/reference             | `{{context.steps.Start.AudioURL}}` |

> **LiveKit:** [Advanced parameters and custom STT](https://docs.livekit.io/agents/models/stt/#additional-parameters)

## Response Formats & Output Handling

**Output Types:**
- **Plain Text:** Default transcript.
- **Structured JSON:** Includes transcript, timestamps, speaker labels, and (optionally) confidence scores.

**Example Output:**
```json
{
  "transcript": "Hello, thank you for calling AcmeCorp. How may I assist you today?",
  "timestamps": [
    { "word": "Hello", "start": 0.0, "end": 0.5 },
    { "word": "thank", "start": 0.6, "end": 0.8 }
  ],
  "speakers": [
    { "segment": "Customer", "start": 0.0, "end": 3.0 }
  ]
}
```

- **Rev AI:** Offers insights such as [sentiment analysis](/en/glossary/sentiment-analysis/), topic extraction, summarization, and forced alignment ([Rev AI Features](https://www.rev.ai/)).

## Common Use Cases

- **Meeting and Lecture Transcription:**  
  Transcribe meetings, interviews, or lectures into searchable, indexable text.
- **Customer Support Automation:**  
  Transcribe voice interactions for chatbots, CRM, and help desk systems.
- **Subtitle and Caption Generation:**  
  Generate subtitles for video content, with timestamp alignment.
- **Voice Command Processing:**  
  Convert spoken commands into actionable text for voice-enabled apps.
- **Audio-based Translation:**  
  Transcribe and translate multilingual audio for localization and accessibility.
- **Healthcare Documentation:**  
  Convert medical dictations and consultations into patient records.
- **Call Center Analysis:**  
  Transcribe recorded calls for quality assurance, compliance, or analytics.
- **Market Research:**  
  Transcribe focus group or interview recordings for further analysis.

- [Rev AI Use Cases](https://www.rev.ai/)

## Integration Tips & Best Practices

- **Context Variables:** Use variables to reference audio URLs or data dynamically.
- **Prompt Engineering:** Tailor instructions for speaker labeling, terminology, or formatting for accuracy.
- **Batch Processing:** For large volumes, utilize batch or asynchronous modes ([Google Batch Transcription](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription)).
- **Audio Preprocessing:** Ensure clear audio, minimal noise, and compatible format.
- **File Segmentation:** Split long recordings at logical breaks.
- **Model Adaptation:** Provide custom vocabulary lists for better performance in specialized domains ([Google Adaptation](https://cloud.google.com/speech-to-text/docs/adaptation)).
- **Compliance & Privacy:** Enable profanity filtering, and select appropriate data residency options.

## Error Handling & Performance Monitoring

- **Error Types:**
  - Unsupported file format or exceeded size limits.
  - Invalid/inaccessible audio URLs.
  - Model selection/configuration errors.
  - Output schema mismatches.

- **Error Handling:**
  - Validate input before processing.
  - Implement retry logic or fallback flows.
  - Log errors and monitor via analytics dashboards.

- **Performance Metrics:**
  - Minutes of audio processed (for cost/usage tracking).
  - Token usage (for LLM-enabled ASR systems).
  - Response times and throughput.

- [Kore.ai Model Analytics Dashboard](https://docs.kore.ai/agent-platform/settings/monitoring/analytics/model-analytics-dashboard/)  
- [Google Speech-to-Text Monitoring](https://cloud.google.com/monitoring)

## Provider Comparison

| Provider            | Key Features                                                                   | Languages        | Notes / Links |
|---------------------|--------------------------------------------------------------------------------|------------------|---------------|
| **OpenAI Whisper**  | Multilingual, translation to English, robust ASR, profanity filtering          | 50+              | [Whisper Docs](https://platform.openai.com/docs/guides/speech-to-text) |
| **Google Speech-to-Text** | 125+ languages, streaming & batch, diarization, adaptation, filtering    | 125+             | [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text) |
| **Azure Speech**    | Real-time/batch, custom models, industry adaptation, CLI & SDK                 | 100+             | [Azure Speech Overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text) |
| **Rev AI**          | Asynchronous & streaming, human and machine transcription, insights, low WER   | 58+              | [Rev AI](https://www.rev.ai/) |
| **LiveKit**         | Pluggable models (AssemblyAI, Cartesia, Deepgram), automatic model selection   | Model-dependent  | [LiveKit STT](https://docs.livekit.io/agents/models/stt/) |
| **VectorShift**     | Node-based pipelines, variable/upload input, LLM integration                   | Provider-dependent| [VectorShift Docs](https://docs.vectorshift.ai/platform/pipelines/multi-modal/speech-to-text) |

## Illustrative Examples

### Example 1: Meeting Transcription Node (Kore.ai)

**Prompt:**  
“Use direct speech and highlight problem or challenge-related vocabulary.”

**Input:**
```json
{
  "audioFile": "https://example.com/meeting-2024-06-10.mp3"
}
```

**Output:**
```
Speaker 1: We're experiencing recurring issues with our API gateway.
Speaker 2: The main challenge is integrating external authentication.
```
([Kore.ai Example](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/))

### Example 2: Google Speech-to-Text API (Node.js)

**Code Sample:**
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

### Example 3: LiveKit STT Model Usage (Python)

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="assemblyai/universal-streaming:en",
    # ... llm, tts, etc.
)
```
[LiveKit Usage Docs](https://docs.livekit.io/agents/models/stt/#usage)

## Technical Notes & Edge Cases

- **Token Limits:** Some ASR models have input token limits (e.g., Whisper: 224 tokens).
- **Edge Audio Cases:**  
  - For files near the size limit, segment at logical boundaries.
  - Maintain sentence integrity when splitting.
- **Profanity and Content Filtering:**  
  - Removal is default for some models; configurable in others.
- **Speaker Diarization:**  
  - Not universally supported—verify with provider
