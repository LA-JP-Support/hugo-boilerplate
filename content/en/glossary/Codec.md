---
title: Codec
lastmod: 2026-04-02
translationKey: codec
description: A codec is technology for compressing and decompressing audio, video, and data to enable efficient storage and transmission.
keywords:
- codec
- compression
- encoding
- decoding
- multimedia
category: Cloud & Infrastructure
type: glossary
date: 2025-12-19
draft: false
url: "/en/glossary/codec/"
---

## What is a Codec?

**A codec is technology that compresses large amounts of audio, video, and image data into smaller sizes and decompresses when needed.** The term combines "coder" (compression) and "decoder" (decompression), with both functions included. YouTube delivers video fast, messaging apps send voice, and TV broadcasts distribute efficiently—all thanks to codec technology.

> **In a nutshell:** "Magic technology that compresses files to send small, then expands them on arrival." Like packing bulky items compressed into boxes for shipping, then expanding them at destination.

**Key points:**

- **What it does:** Compresses video, audio, and images for storage and transmission, decompressing for playback
- **Why it's needed:** Uncompressed video requires massive data—1/100th size or smaller while keeping quality—codec makes transmission and storage possible
- **Who uses it:** Video streaming services, TV broadcasts, Zoom and video conferencing, smartphones, digital devices

## Why It Matters

Digital content grows rapidly—one minute HD video needs gigabytes. Internet bandwidth is limited, storage finite. Without codec technology, YouTube, movie delivery, and fast video streaming wouldn't exist. Compression method choice significantly affects quality and speed, making codec selection a crucial decision affecting delivery experience.

## How It Works

Codecs combine multiple compression techniques. First, they remove information human perception doesn't need. Human ears don't hear high frequencies sensitively, so that audio data can be omitted without notice. Second, they copy unchanged parts (like backgrounds) across video frames and record differences only, reducing data by 50x while barely compromising quality.

During decoding (playback), the process reverses, restoring nearly original form. Not all information returns, but restoration reaches human imperceptible differences. This "unchanged appearance/sound but smaller data" balance is codec's core.

## Real-World Use Cases

**Streaming Video Services**
Netflix and YouTube auto-select appropriate codec based on user connection speed. Slow connections lower quality; fast connections deliver full HD. All environments stream smoothly.

**TV Broadcast**
Digital terrestrial broadcasting delivers multiple channels within limited radio spectrum bands using efficient codecs (like H.264). Same bandwidth carries higher-quality programs than before.

**Video Conferencing**
Zoom and Microsoft Teams dynamically adjust codec settings based on participant environments. Stable connections maintain full quality; unstable ones still minimize delay while preserving quality.

## Benefits and Considerations

Codec advantages are clear: dramatic data compression speeds delivery, saves storage, cuts costs. Higher compression ratios bring slight quality loss though. Old codecs lose support on new devices, creating compatibility issues. Organizations choosing codecs should consider future compatibility requirements.

## Related Terms

- **[Bitrate](./Bitrate.md)** — Data processed per second by codec, directly affecting quality
- **[Compression](./Compression.md)** — Core data-size reduction technology of codecs
- **[H.264/H.265](./H264-H265.md)** — Most-used industry-standard video codecs
- **[Perceptual Encoding](./Perceptual-Encoding.md)** — Compression removing imperceptible information
- **[Network Bandwidth](./Bandwidth.md)** — Critical environmental factor determining codec choice

## Frequently Asked Questions

**Q: Which codec should I choose?**
A: Depends on target environment and compatibility. YouTube uses H.264; 4K needs H.265; web uses newer VP9 or AV1. If old environment support is required, choose widely-supported codecs.

**Q: Can I re-compress already-compressed files?**
A: Possible but quality drops further. Lossy compression (MP4) permanently loses information. Re-compress from original files instead unless truly necessary.

**Q: What's the difference between lossless and lossy compression?**
A: Lossless (FLAC, PNG) fully restores original but has lower compression. Lossy (MP3, JPEG) compresses more but permanently loses some data.

## Reference Materials

- [H.264 Video Compression Standard](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC)
- [HEVC (H.265) Specification](https://www.itu.int/rec/T-REC-H.265/en)
- [AV1 Codec Overview](https://www.aomedia.org/av1-specification/)
- [VP9 Codec Documentation](https://www.webmproject.org/vp9/)
- [Codec Selection Guide](https://www.ffmpeg.org/general.html)
- [Video Compression Basics](https://www.techsmith.com/blog/video-compression/)
- [Audio Codec Comparison](https://www.soundonsound.com/reviews/audio-codecs)
- [Streaming Video Codec Best Practices](https://developer.apple.com/documentation/http_live_streaming)
- [NIST Multimedia Compression Standards](https://www.nist.gov/)
- [ACM Multimedia Codec Research](https://dl.acm.org/journal/tom)
