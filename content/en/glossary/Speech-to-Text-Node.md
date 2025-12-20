---
title: "Speech-to-Text Node"
translationKey: "speech-to-text-node"
description: "A Speech-to-Text Node converts spoken words in audio files into written text, enabling voice commands, meeting transcriptions, and automated voice-based processes."
keywords: ["Speech-to-Text Node", "Automatic Speech Recognition", "AI workflows", "Audio to Text", "Transcription"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is a Speech-to-Text Node?

A Speech-to-Text Node is a foundational component in conversational AI, automation pipelines, and workflow systems that converts spoken language in audio files—voice recordings, calls, or video soundtracks—into accurate, structured text. This transcription enables downstream analysis, summarization, translation, or automated process triggering, making it essential for voice-enabled applications and knowledge management systems.

The node functions as a modular workflow component that receives audio input, processes it through an Automatic Speech Recognition (ASR) model, and outputs a transcript. This transcript can optionally include word-level timestamps, speaker labels, translations, or structured metadata for further processing.

**Typical Workflow:**
1. Audio input received (file upload, URL, or workflow variable)
2. Processing via ASR model (OpenAI Whisper, Google Speech-to-Text, Azure Speech, Rev AI)
3. Output transcript with optional metadata (timestamps, speaker labels, translations)

**Role in Automation:**
- Enables chatbots to process voice queries
- Transcribes meetings, interviews, and lectures for knowledge management
- Automates content indexing and data extraction from voice interactions

## Key Capabilities

**Automatic Speech Recognition (ASR)**  
Converts audio to text using advanced models with high accuracy across diverse accents and audio conditions.

**Multilingual Support**  
Transcribes speech in 50-125+ languages and dialects, depending on provider. Major models support global language coverage for international deployments.

**Translation**  
Translates non-English speech into English or other supported languages in a single processing step, eliminating the need for separate translation workflows.

**Custom Prompt Instructions**  
Accepts natural language instructions for transcription style, speaker labeling, terminology preferences, or error handling approaches.

**Flexible Audio Input**  
Accepts file uploads, URLs, or variables from previous workflow steps, supporting diverse integration patterns.

**Large File Handling**  
Processes files up to provider-specific limits (typically 25 MB), with guidance on segmenting larger files at logical boundaries.

**Timestamps & Speaker Diarization**  
Optionally includes word-level or utterance-level timing and identifies individual speakers in multi-party conversations.

**Profanity Filtering**  
Removes or masks offensive content according to configuration or model defaults.

**Custom Vocabulary & Model Adaptation**  
Improves recognition of domain-specific terms through vocabulary lists and model fine-tuning.

**Structured Output (JSON)**  
Returns data in schemas suitable for downstream processing, including nested metadata.

## How Speech-to-Text Nodes Work

### Audio Input

The node receives an audio file or URL from user upload, cloud storage, or a previous workflow step. Supported formats typically include MP3, WAV, MP4, M4A, WebM, MPGA, and MPEG.

### Model Selection & Preprocessing

**Choose ASR Provider:** Select from OpenAI Whisper, Google Speech-to-Text, Azure Speech Service, AssemblyAI, Deepgram, or other providers.

**Configure Features:** Enable language detection, translation, timestamps, speaker identification, and custom prompts.

### Transcription Process

The ASR engine processes the audio, applying acoustic and language models to generate text. Optional features like translation, profanity filtering, formatting, and diarization are applied during or after transcription.

### Output Handling

The node outputs the transcript in plain text or structured JSON format. Downstream workflow steps consume this output for summarization, analysis, storage, or user feedback.

## Supported Audio Formats & File Limits

**Audio Formats:**
- M4A, MP3, WebM, MP4, MPGA, WAV, MPEG
- Provider support varies; verify compatibility with your chosen ASR service

**File Size Limits:**
- Typical maximum: 25 MB per file
- Larger files must be split into segments ≤25 MB
- Segment at logical sentence boundaries to preserve context and accuracy

**Input Methods:**
- Direct file upload
- URL reference to hosted audio
- Variable reference from previous workflow steps

Some platforms accept only URLs for security and scalability reasons.

## Configuration Guide

### Prerequisites

- Access to automation platform (Kore.ai, LiveKit, Google Cloud, Azure)
- API key or integration credentials (if required)
- Audio files hosted at accessible URLs or available for upload

### Step-by-Step Configuration

**1. Add Node to Workflow**  
Open your automation builder and drag the Speech-to-Text or Audio to Text node into your workflow.

**2. Configure Node Properties**
- **Node Name:** Assign unique, descriptive name (e.g., "MeetingTranscription")
- **Audio File Input:** Reference variable holding audio URL
- **Model Selection:** Choose ASR provider and specific model
- **Feature Toggles:** Enable translation, timestamps, speaker diarization, profanity filtering

**3. Set Custom Prompt Instructions**  
Define transcription style, speaker labeling requirements, terminology preferences, or error handling approaches in natural language.

Example:
```
Provide a clean transcript, omitting filler words, with clear speaker labels and correct technical terms.
```

**4. Define JSON Schema for Output (Optional)**  
Specify structured output schema for downstream processing:

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

**5. Connect Success & Failure Paths**
- **On Success:** Route to summarization, translation, or analysis nodes
- **On Failure:** Route to error handling or fallback nodes

**6. Test and Validate**  
Run workflow with sample inputs, review output for completeness and correctness, and adjust configuration as needed.

## Configuration Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| Audio Input | URL or reference to uploaded audio file | `https://host/path/audio.mp3` |
| Model | ASR engine/model to use | `OpenAI Whisper-1`, `Chirp 3` |
| Language Code | Language for transcription (BCP-47) | `en-US`, `fr-FR` |
| Translation | Enable translation to English | `true` / `false` |
| Timestamps | Include word/utterance-level timestamps | `true` / `false` |
| Speaker Labels | Diarization, label speakers in multi-party audio | `true` / `false` |
| Profanity Filter | Remove or mask offensive words | `true` / `false` |
| Prompt | Custom instructions for transcription style | See above |
| JSON Schema | Structured output for downstream processing | See above |
| Custom Vocab | Domain-specific words to bias recognition | `["AcmeCorp", "API Gateway"]` |
| Input Variable | Context variable holding input audio file | `{{context.steps.Start.AudioURL}}` |

## Response Formats & Output

**Plain Text Output:**  
Default transcript as continuous text string.

**Structured JSON Output:**  
Includes transcript, timestamps, speaker labels, and confidence scores.

**Example:**
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

**Advanced Features:**  
Rev AI offers sentiment analysis, topic extraction, summarization, and forced alignment as additional output options.

## Common Use Cases

**Meeting and Lecture Transcription**  
Transcribe meetings, interviews, or lectures into searchable, indexable text for knowledge management and compliance.

**Customer Support Automation**  
Transcribe voice interactions for chatbots, CRM systems, and help desk platforms to enable automated routing and analysis.

**Subtitle and Caption Generation**  
Generate subtitles for video content with timestamp alignment for accessibility and localization.

**Voice Command Processing**  
Convert spoken commands into actionable text for voice-enabled applications and smart devices.

**Audio-Based Translation**  
Transcribe and translate multilingual audio in a single step for localization and accessibility.

**Healthcare Documentation**  
Convert medical dictations and consultations into patient records with specialized medical vocabulary support.

**Call Center Analysis**  
Transcribe recorded calls for quality assurance, compliance monitoring, and performance analytics.

**Market Research**  
Transcribe focus group or interview recordings for thematic analysis and reporting.

## Integration Best Practices

**Use Context Variables**  
Reference audio URLs or data dynamically to support flexible workflow design and reusability.

**Employ Prompt Engineering**  
Tailor instructions for speaker labeling, terminology, or formatting to improve accuracy for specific use cases.

**Implement Batch Processing**  
For large volumes, utilize batch or asynchronous modes to optimize resource usage and reduce processing time.

**Preprocess Audio Quality**  
Ensure clear audio, minimal background noise, and compatible format before processing to maximize transcription accuracy.

**Segment Files Strategically**  
Split long recordings at logical breaks (sentence boundaries, speaker changes) to maintain context when approaching size limits.

**Provide Custom Vocabulary**  
Submit domain-specific term lists to improve recognition of technical jargon, product names, or industry terminology.

**Configure Compliance Features**  
Enable profanity filtering and select appropriate data residency options to meet regulatory requirements.

## Error Handling & Monitoring

### Error Types

- Unsupported file format or exceeded size limits
- Invalid or inaccessible audio URLs
- Model selection or configuration errors
- Output schema mismatches

### Error Handling Strategies

- Validate input format and size before processing
- Implement retry logic with exponential backoff
- Design fallback flows for critical workflows
- Log errors with detailed context for troubleshooting

### Performance Metrics

- Minutes of audio processed (for cost/usage tracking)
- Token usage (for LLM-enabled ASR systems)
- Response times and throughput
- Error rates by error type

## Provider Comparison

| Provider | Key Features | Languages | Notes |
|----------|-------------|-----------|-------|
| **OpenAI Whisper** | Multilingual, translation, robust ASR, profanity filtering | 50+ | Best for general-purpose transcription |
| **Google Speech-to-Text** | 125+ languages, streaming & batch, diarization, adaptation | 125+ | Strong enterprise features |
| **Azure Speech** | Real-time/batch, custom models, industry adaptation | 100+ | Deep Microsoft ecosystem integration |
| **Rev AI** | Asynchronous & streaming, human and machine transcription | 58+ | Hybrid human/AI options |
| **LiveKit** | Pluggable models (AssemblyAI, Cartesia, Deepgram) | Model-dependent | Flexible for real-time applications |
| **VectorShift** | Node-based pipelines, LLM integration | Provider-dependent | Best for complex workflows |

## Implementation Examples

### Example 1: Meeting Transcription (Kore.ai)

**Prompt:**  
"Use direct speech and highlight problem or challenge-related vocabulary."

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

### Example 2: Google Speech-to-Text API (Node.js)

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

### Example 3: LiveKit STT Model (Python)

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="assemblyai/universal-streaming:en",
    # ... llm, tts, etc.
)
```

## Technical Considerations

**Token Limits:**  
Some ASR models have input token limits (e.g., Whisper: 224 tokens). Plan segmentation strategies for long-form content.

**Edge Audio Cases:**  
For files near size limits, segment at logical boundaries and maintain sentence integrity when splitting.

**Profanity and Content Filtering:**  
Removal may be default for some models; verify configuration options for your use case.

**Speaker Diarization:**  
Not universally supported across all providers—verify availability and accuracy for multi-speaker scenarios.

**Real-Time vs Batch:**  
Choose between streaming (real-time) and batch processing based on latency requirements and cost optimization.

## References

- [Kore.ai Audio to Text Node Documentation](https://docs.kore.ai/agent-platform/ai-agents/tools/tool-flows/types-of-nodes/audio-to-text-node/)
- [OpenAI Whisper Documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)
- [Google Speech-to-Text Supported Languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
- [Google Speech-to-Text Encoding](https://cloud.google.com/speech-to-text/docs/encoding)
- [Google Speech-to-Text Adaptation](https://cloud.google.com/speech-to-text/docs/adaptation)
- [Google Cloud Monitoring](https://cloud.google.com/monitoring)
- [Azure Speech Service Overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text)
- [Azure Batch Transcription](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription)
- [Rev AI](https://www.rev.ai/)
- [LiveKit STT Documentation](https://docs.livekit.io/agents/models/stt/)
- [LiveKit STT Inference](https://docs.livekit.io/agents/models/stt/#inference)
- [LiveKit STT Plugins](https://docs.livekit.io/agents/models/stt/#plugins)
- [LiveKit STT Usage](https://docs.livekit.io/agents/models/stt/#usage)
- [LiveKit STT Additional Parameters](https://docs.livekit.io/agents/models/stt/#additional-parameters)
- [VectorShift Speech-to-Text Documentation](https://docs.vectorshift.ai/platform/pipelines/multi-modal/speech-to-text)
- [Kore.ai Model Analytics Dashboard](https://docs.kore.ai/agent-platform/settings/monitoring/analytics/model-analytics-dashboard/)
- [Google Codelabs: Cloud Speech Text Node](https://codelabs.developers.google.com/codelabs/cloud-speech-text-node)
