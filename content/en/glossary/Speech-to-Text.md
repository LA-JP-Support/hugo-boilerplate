---
title: Speech-to-Text
date: 2025-12-19
lastmod: 2026-04-02
translationKey: speech-to-text
description: Speech-to-Text (STT) is a technology using automatic speech recognition to convert spoken words into written text, significantly improving accessibility, productivity, and information searchability.
keywords:
- speech-to-text
- automatic speech recognition
- ASR technology
- voice recognition
- audio processing
category: Voice & Communication
type: glossary
draft: false
url: /en/glossary/Speech-to-Text/
---

## What is Speech-to-Text?

**Speech-to-Text (STT, also called Automatic Speech Recognition or ASR) is a technology that automatically converts spoken language into written text.** It analyzes audio from microphones or files and uses [machine learning](Machine-Learning.md) models to estimate the corresponding text. Current technology can process multiple languages, accents, and background noise with high accuracy.

> **In a nutshell:** A computer "listens to" human speech, "understands" it, and "writes it down" as text.

**Key points:**

- **What it does:** Automatically converts audio signals into text strings.
- **Why it's needed:** Accessibility, productivity improvement, and enhanced information searchability.
- **Who uses it:** Deaf and hard-of-hearing people, remote workers, media companies, healthcare organizations.

## Why It Matters

Speech-to-Text is not merely a convenience feature—it's a socially essential accessibility tool. For deaf and hard-of-hearing individuals, live captioning is foundational to education and employment participation. Real-time text conversion also enables efficient meeting note generation, customer call analysis, and court record creation. Converting audio recordings to searchable text dramatically increases data value.

## How It Works

Speech-to-Text combines multiple specialized technologies into a complex process.

**In the feature extraction stage**, audio waveforms are converted into mathematical representations like frequency characteristics, making audio processable by AI. Techniques like [mel-frequency cepstral coefficients (MFCC)](MFCC.md) are commonly used.

**In the acoustic modeling stage**, [deep learning](Deep-Learning.md) models (typically neural networks) predict phonemes (minimal sound units) from features.

**In the language modeling stage**, statistical language models evaluate "are these word combinations plausible?" and select the most likely word sequence, improving grammatical accuracy.

**In the decoding stage**, acoustic and language information combine to generate the final text output.

Algorithms find the optimal match when multiple interpretations exist.

## Real-World Use Cases

**Live Captioning in Online Education**
Lectures are captioned simultaneously, making education accessible to deaf students.

**Medical Dictation**
Doctors dictate notes while meeting patients, automatically converting to electronic records.

**Closed Captioning for News Media**
TV broadcasts and online videos are automatically captioned, improving accessibility and searchability.

## Benefits and Considerations

**Benefits:** Improved accessibility for deaf and hard-of-hearing users, streamlined document creation, and enabled large-scale voice data analysis.

**Considerations:** Background noise significantly reduces accuracy. Domain-specific terminology (medical, legal) is difficult for general models. Privacy is also a concern.

## Related Terms

- **[Automatic Speech Recognition (ASR)](ASR.md)** — The technical foundation for Speech-to-Text.
- **[Deep Learning](Deep-Learning.md)** — Modern STT implementation approach.
- **[Natural Language Processing (NLP)](NLP.md)** — Processing and understanding text output.
- **[Multimodal AI](Multimodal-AI.md)** — Integrated voice and text processing.
- **[Accessibility](Accessibility.md)** — The social importance of STT.

## Frequently Asked Questions

**Q: Can colloquial speech and dialects be recognized?**
A: Models trained on standard language typically have lower accuracy for colloquialisms and dialects. Models trained on diverse data can handle more variation.

**Q: Is there accuracy difference between real-time and post-processing?**
A: Post-processing can reference the full context, typically achieving 10-15% better accuracy.
