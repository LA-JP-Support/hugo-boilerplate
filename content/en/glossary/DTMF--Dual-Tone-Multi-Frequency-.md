---
title: DTMF (Dual-Tone Multi-Frequency)
translationKey: dtmf-dual-tone-multi-frequency
description: A communication signaling system using unique audio tones from keypads to interpret commands, route calls, enable automatic menu navigation, remote control, and secure data entry across telephone networks and digital platforms.
keywords:
- DTMF
- Communication
- IVR
- VoIP
- PCI DSS
category: Voice & Communication
type: glossary
date: '2025-12-19'
lastmod: 2026-04-02
draft: false
url: "/en/glossary/dtmf--dual-tone-multi-frequency-/"
---

## What is DTMF?

**Dual-Tone Multi-Frequency (DTMF) is a signaling technology used in communication networks and digital communication platforms where each keypad button press generates a unique combination of two audio frequencies—one from a "low frequency" group and one from a "high frequency" group.** These tones are the audio beeps you hear when making phone calls or operating automatic systems. DTMF enables both humans and machines to transmit commands, route calls, and securely enter data.

> **In a nutshell:** Just as a phone keypad generates beeps when you press buttons, DTMF uses unique tone pairs to tell telephone systems which button you pressed and what action to take.

**Key points:**

- **What it does:** Generates unique tone pairs when keypad buttons are pressed to signal commands and data entry
- **Why it's needed:** Enables reliable, secure command transmission and data entry in voice systems without requiring human interpretation
- **Who uses it:** Call centers, telephone banking systems, automated voice systems, and security access systems

## How DTMF Works

### Frequency Matrix and Keypad Mapping

DTMF operates by pairing two specific frequencies each time a button is pressed. The telephone keypad is arranged in a matrix:

- **Rows:** Each row is assigned a low frequency (697 Hz, 770 Hz, 852 Hz, 941 Hz)
- **Columns:** Each column is assigned a high frequency (1209 Hz, 1336 Hz, 1477 Hz, 1633 Hz for A-D keys)

**Technical mechanism:** When a key is pressed, electronic circuitry generates two tones—one from the row (low frequency group) and one from the column (high frequency group). The resulting signal is a combination of these two frequencies, sent as a single audio signal over the audio channel. A decoder on the receiving end separates the tones and identifies which key was pressed.

**Why two tones?** Using two simultaneous frequencies per key makes it nearly impossible for random sounds or human voices to accidentally trigger commands, ensuring reliability and security.

## Historical Background

Before DTMF, telephone systems used **pulse dialing** (loop disconnection), where dial phones interrupted the electrical current on the local loop. Each number was represented by a specific number of rapid interruptions. This was slow, unreliable over long distances, and limited to mechanical operation.

DTMF was introduced in 1963 by Bell System (marketed as "Touch-Tone"), improving dialing speed, enabling automation, and supporting new services. The first public push-button telephones became available November 18, 1963, revolutionizing telephone interaction.

## Applications and Use Examples

### Customer Service and Call Centers

**Interactive Voice Response (IVR):** Callers press numbers to select options, interacting with automated menus.
**Sensitive information entry:** Account numbers, PINs, and order numbers are entered via keypad and processed securely.
**Call routing:** DTMF signals direct calls to the appropriate department or agent.

### Other DTMF Uses

**Telephone banking:** DTMF tones operate banking menus and process transactions.
**Remote system control:** Technicians control gates, alarms, and equipment via phone lines.
**Voicemail navigation:** Users press keypad numbers to manage voicemail.
**Teleconferencing:** Participants use DTMF to mute/unmute and record.
**Amateur radio:** DTMF controls radio relays and remote equipment.
**Credit card processing:** Public phones and IVR systems use DTMF to securely transmit card data.
**Home automation:** Legacy systems use DTMF for remote control via phone lines.

## DTMF in Modern (VoIP) versus Legacy Systems

### Legacy (Analog) Systems

DTMF is generated as an analog audio signal and sent over the Public Switched Telephone Network (PSTN). Telephone switches decode the tones to interpret input.

### Digital and VoIP Systems

Modern VoIP networks may send DTMF signals as:
- **In-band:** As audio tones within the audio stream (e.g., RTP)
- **Out-of-band:** As digital events within signaling protocols (e.g., SIP INFO, RFC 2833/4733)

**Interoperability:** VoIP platforms must relay DTMF signals in formats compatible with both legacy and current digital systems.

## DTMF and PCI DSS Compliance

**Why DTMF masking matters:** When customers enter payment card information via phone keypad, resulting DTMF signals can be captured by call recordings or agents, creating security and compliance risks.

**DTMF masking** intercepts and conceals DTMF tones before they reach agents or recordings, replacing tones with asterisks or blanks. This removes contact centers from PCI DSS scope and prevents sensitive data exposure.

**Benefits:**
- Reduced fraud risk
- Simplified PCI DSS compliance
- Enhanced customer trust
- Enables agent assist without compromising security

## Related terms

- **[IVR (Interactive Voice Response)](IVR.md)** — DTMF is the primary input mechanism for IVR systems
- **[VoIP](VoIP.md)** — DTMF transmission requires special handling in VoIP networks
- **[Call Center Technology](Call-Center.md)** — DTMF is fundamental to call routing and automation
- **[PCI Compliance](PCI-Compliance.md)** — DTMF masking is essential for payment security
- **[Telecommunications](Telecommunications.md)** — DTMF is a core telephony signaling protocol

## Frequently asked questions

**Q: Why do I hear different beep sounds when pressing different keypad buttons?**

A: Each button produces a unique combination of two frequencies. Different buttons create different frequency pairs, resulting in distinct tone patterns you can hear and recognize.

**Q: How reliable is DTMF for sensitive data like credit card numbers?**

A: DTMF itself is reliable, but transmitting sensitive data requires additional security like DTMF masking to prevent capture by call recordings or monitoring systems.

**Q: Will DTMF become obsolete with modern technology?**

A: DTMF remains widely used due to its reliability and simplicity, though modern alternatives like voice recognition are emerging for certain applications.
