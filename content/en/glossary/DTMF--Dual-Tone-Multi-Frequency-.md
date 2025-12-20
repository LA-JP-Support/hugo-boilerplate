---
title: "DTMF (Dual-Tone Multi-Frequency)"
translationKey: "dtmf-dual-tone-multi-frequency"
description: "DTMF is the beeping sound system that lets phones recognize which number you pressed, enabling automated menus and secure data entry like PIN codes."
keywords: ["DTMF", "telecommunication", "IVR", "VoIP", "PCI DSS"]
category: "AI Chatbot & Automation, Telecommunication Systems"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What Is DTMF?

Dual-tone multi-frequency (DTMF) is a signaling technology used in telecommunication networks and digital communication platforms. Each key press on a keypad transmits a distinct combination of two audio frequencies—one from a "low" group and one from a "high" group. These tones are the audible beeps you hear when dialing a phone or navigating an automated system. DTMF enables both people and machines to communicate commands, route calls, and securely enter data.

**Everyday context:** Pressing numbers on a phone keypad for menu navigation or entering a PIN for telephone banking produces DTMF tones. Automated systems such as IVR (Interactive Voice Response) and chatbots detect these tones to process input.

## How Does DTMF Work?

### Frequency Matrix and Keypad Mapping

DTMF operates by pairing two specific frequencies for each button press. The telephone keypad is arranged in a matrix:

- **Rows:** Each assigned a low frequency (697 Hz, 770 Hz, 852 Hz, 941 Hz)
- **Columns:** Each assigned a high frequency (1209 Hz, 1336 Hz, 1477 Hz, 1633 Hz for A-D keys)

**Technical mechanism:** When a key is pressed, the electronic circuit generates two tones: one from the row (low group), one from the column (high group). The resulting signal is a combination of these two frequencies, sent as a single audio signal over the voice channel. Decoders at the receiving end separate the tones and identify the pressed key.

**Why two tones?** Using two simultaneous frequencies for each key makes it virtually impossible for random sounds or the human voice to trigger commands, ensuring reliability and security.

### DTMF Frequency Table

**Standard 12-Key DTMF Keypad Frequency Mapping (ITU-T Q.23):**

|        | 1209 Hz | 1336 Hz | 1477 Hz |
|--------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |
| 770 Hz |   4     |   5     |   6     |
| 852 Hz |   7     |   8     |   9     |
| 941 Hz |   *     |   0     |   #     |

**Extended 16-Key (A–D) Keypad:**

|        | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
|--------|---------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |   A     |
| 770 Hz |   4     |   5     |   6     |   B     |
| 852 Hz |   7     |   8     |   9     |   C     |
| 941 Hz |   *     |   0     |   #     |   D     |

## Historical Context

### Replacement of Pulse Dialing

Before DTMF, telephone systems used **pulse dialing** (loop disconnect), which involved interrupting the current in the local loop with a rotary dial. Each number was represented by a specific number of rapid line interruptions.

**Limitations:**
- Slow dialing, especially for high digits
- Restricted to direct metallic links; not reliable over long distances
- More complex and less reliable due to mechanical parts

DTMF was introduced in 1963 by Bell System (marketed as "Touch-Tone"), speeding up dialing, enabling automation, and supporting new services. The first public push-button telephone was available on November 18, 1963.

## Applications and Use Cases

### Customer Service and Call Centers

**Interactive Voice Response (IVR):** Callers interact with automated menus by pressing numbers for options ("Press 1 for account info").  
**Input of Sensitive Information:** Entering account numbers, PINs, or order numbers via keypad for secure processing.  
**Call Routing:** DTMF signals direct calls to the right department or agent.

### Other DTMF Use Cases

**Telephone Banking:** DTMF tones navigate banking menus and process transactions.  
**Remote System Control:** Technicians control gates, alarms, or equipment via telephone lines.  
**Voicemail Navigation:** Users manage voicemail by pressing keypad numbers.  
**Conference Calls:** Participants use DTMF to mute/unmute, record, or initiate actions during teleconferences.  
**Ham Radio:** DTMF controls radio repeaters and remote equipment.  
**Credit Card Processing:** Payphones or IVR systems use DTMF for secure card data transmission.  
**Home Automation:** Legacy systems use DTMF for remote control via phone line.

## DTMF in Modern (VoIP/Digital) and Legacy Systems

### Legacy (Analog) Systems

DTMF generated and transmitted as analog audio signals over the Public Switched Telephone Network (PSTN). Telephone exchange decodes tones to interpret input.

### Digital and VoIP (Voice over IP) Systems

Modern VoIP networks do not natively transmit analog DTMF tones. DTMF signals may be sent:
- **In-band:** As audio tones within the voice stream (e.g., RTP)
- **Out-of-band:** As digital events in the signaling protocol (e.g., SIP INFO, RFC 2833/4733, KPML)

**Interoperability:** VoIP platforms must relay DTMF signals in a format compatible with legacy and current digital systems.

**Mobile (Cellular) Phones:** Modern mobile devices transmit dialed numbers digitally but can generate DTMF tones during calls for menu navigation.

## Technical Standards for DTMF

### ITU-T Q.23 and Keypad Mapping

**ITU-T Recommendation Q.23:** Defines the frequency pairs, tone duration, and keypad layout for DTMF signaling, ensuring consistent global signaling.

**RFC 2833/4733:** Specifies DTMF relay in VoIP (RTP payload for telephony events).

**SIP INFO/KPML:** Alternative methods for DTMF signaling in SIP environments.

## DTMF Signaling: In-Band vs. Out-of-Band

**In-Band Signaling:** DTMF tones sent as audible signals in the same channel as voice audio (PSTN, analog, some VoIP RTP streams). Any participant can hear the tones.

**Out-of-Band Signaling:** DTMF digits sent digitally outside the voice channel, using signaling protocols (e.g., SIP INFO, RFC 2833/4733).

**Security Note:** In-band is susceptible to interception and fraud; out-of-band is preferred for secure, reliable transmission in digital networks.

## DTMF, AI Chatbots, and Automation

DTMF enables direct interaction with automated systems (IVR, chatbots, virtual agents) via keypad input. AI-powered platforms listen for DTMF to process menu selections, collect data, and route calls.

**Advantages:**
- Faster menu navigation
- Reduced errors in noisy environments compared to speech recognition
- Secure entry of sensitive data (PINs, card numbers) without verbalizing
- Lower operational costs by reducing live agent involvement

## DTMF and PCI DSS Compliance

**Why DTMF masking matters:** When customers enter payment card details using the phone keypad, the resulting DTMF signals can be captured in call recordings or by agents, posing a security and compliance risk.

**DTMF masking** intercepts and obscures DTMF tones before they reach agents or recordings, replacing the tones with asterisks or blanking them out. This keeps the contact center out of PCI DSS scope and prevents sensitive data exposure.

**Benefits:**
- Reduces fraud risk
- Simplifies PCI DSS compliance
- Improves customer trust
- Enables agent-assisted or IVR payment flows without pausing recordings

**How it works:** Real-time interception: As the customer enters digits, the system detects and removes tones before they reach the agent or recording. Masking is available for both on-premise and cloud-based contact centers and works across SIP/ISDN infrastructures.

## Examples and Practical Scenarios

**IVR Menu Navigation:** "Press 1 for account balance, 2 for transactions, 3 to speak to a representative." The system detects DTMF for "1" and routes the call.

**Secure Payment Entry:** A customer enters their credit card number using the phone keypad. DTMF tones are masked and securely processed.

**Conference Call Controls:** A host mutes all participants by pressing "*5"; the system detects the DTMF and executes the command.

**Remote Access:** A facility manager calls a security system and enters a code via DTMF to open a remote gate.

**Ham Radio Repeater Activation:** An operator sends a DTMF sequence to activate a repeater or control equipment.

## References

- [Sycurio: DTMF Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [Sycurio: DTMF Masking Guide](https://sycurio.com/blog/dtmf-masking)
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [Twilio: The Introduction of Touch Tone Phones](https://www.twilio.com/docs/glossary/what-is-dtmf#the-introduction-of-touch-tone-phones)
- [Twilio: In-Band vs. Out-of-Band Signaling](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)
- [NICE: IVR Products](https://www.nice.com/products/interactive-voice-response-ivr)
- [ITU-T: Recommendation Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [PCI Pal: Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)
- [YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)
- [YouTube: DTMF Explainer Video](https://www.youtube.com/watch?v=bAbNl8O6sSY)
