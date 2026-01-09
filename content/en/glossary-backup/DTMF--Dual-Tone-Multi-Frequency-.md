---
title: "DTMF (Dual-Tone Multi-Frequency)"
translationKey: "dtmf-dual-tone-multi-frequency"
description: "DTMF (Dual-Tone Multi-Frequency) is a telecommunication signaling system using unique audio tones from keypad presses to interpret commands, route calls, and enable automated menu navigation, remote control, and secure data entry in telephone networks and digital platforms."
keywords: ["DTMF", "telecommunication", "IVR", "VoIP", "PCI DSS"]
category: "AI Chatbot & Automation, Telecommunication Systems"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What is DTMF?

Dual-tone multi-frequency (DTMF) is a signaling technology used in telecommunication networks and digital communication platforms. Each key press on a keypad transmits a distinct combination of two audio frequencies—one from a "low" group and one from a "high" group. These tones are the audible beeps you hear when dialing a phone or navigating an automated system. DTMF enables both people and machines to communicate commands, route calls, and securely enter data.

<strong>Everyday context:</strong>Pressing numbers on a phone keypad for menu navigation or entering a PIN for telephone banking produces DTMF tones. Automated systems such as IVR (Interactive Voice Response) and chatbots detect these tones to process input.  
- [Sycurio Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)  
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)

## How Does DTMF Work?

### Frequency Matrix and Keypad Mapping

DTMF operates by pairing two specific frequencies for each button press. The telephone keypad is arranged in a matrix:

- <strong>Rows:</strong>Each assigned a low frequency (697 Hz, 770 Hz, 852 Hz, 941 Hz)
- <strong>Columns:</strong>Each assigned a high frequency (1209 Hz, 1336 Hz, 1477 Hz, 1633 Hz for A-D keys)

<strong>Technical mechanism:</strong>- When a key is pressed, the electronic circuit generates two tones: one from the row (low group), one from the column (high group).
- The resulting signal is a combination of these two frequencies, sent as a single audio signal over the voice channel.
- Decoders at the receiving end separate the tones and identify the pressed key.

<strong>Why two tones?</strong>Using two simultaneous frequencies for each key makes it virtually impossible for random sounds or the human voice to trigger commands, ensuring reliability and security.  
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)

### Visual: DTMF Frequency Table

<strong>Standard 12-Key DTMF Keypad Frequency Mapping (ITU-T Q.23):</strong>|        | 1209 Hz | 1336 Hz | 1477 Hz |
|--------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |
| 770 Hz |   4     |   5     |   6     |
| 852 Hz |   7     |   8     |   9     |
| 941 Hz |   *     |   0     |   #     |

<strong>Extended 16-Key (A–D) Keypad:</strong>|        | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
|--------|---------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |   A     |
| 770 Hz |   4     |   5     |   6     |   B     |
| 852 Hz |   7     |   8     |   9     |   C     |
| 941 Hz |   *     |   0     |   #     |   D     |

Visual reference:  
![DTMF Frequency Chart](https://www.techtarget.com/rms/onlineimages/ns-dtmf_frequencies-h_half_column_mobile.png)  
- [TechTarget: DTMF Frequency Table](https://www.techtarget.com/searchnetworking/definition/DTMF)

## Historical Context

### Replacement of Pulse Dialing

Before DTMF, telephone systems used <strong>pulse dialing</strong>(loop disconnect), which involved interrupting the current in the local loop with a rotary dial. Each number was represented by a specific number of rapid line interruptions.  
<strong>Limitations:</strong>- Slow dialing, especially for high digits.
- Restricted to direct metallic links; not reliable over long distances.
- More complex and less reliable due to mechanical parts.

DTMF was introduced in 1963 by Bell System (marketed as "Touch-Tone"), speeding up dialing, enabling automation, and supporting new services. The first public push-button telephone was available on November 18, 1963.  
- [Twilio: The Introduction of Touch Tone Phones](https://www.twilio.com/docs/glossary/what-is-dtmf#the-introduction-of-touch-tone-phones)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)

## Applications and Use Cases

### Customer Service and Call Centers

- <strong>Interactive Voice Response (IVR):</strong>Callers interact with automated menus by pressing numbers for options ("Press 1 for account info").
- <strong>Input of Sensitive Information:</strong>Entering account numbers, PINs, or order numbers via keypad for secure processing.
- <strong>Call Routing:</strong>DTMF signals direct calls to the right department or agent.

### Other DTMF Use Cases

- <strong>Telephone Banking:</strong>DTMF tones navigate banking menus and process transactions.
- <strong>Remote System Control:</strong>Technicians control gates, alarms, or equipment via telephone lines.
- <strong>Voicemail Navigation:</strong>Users manage voicemail by pressing keypad numbers.
- <strong>Conference Calls:</strong>Participants use DTMF to mute/unmute, record, or initiate actions during teleconferences.
- <strong>Ham Radio:</strong>DTMF controls radio repeaters and remote equipment.
- <strong>Credit Card Processing:</strong>Payphones or IVR systems use DTMF for secure card data transmission.
- <strong>Home Automation:</strong>Legacy systems use DTMF for remote control via phone line.

- [Sycurio: Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)

## DTMF in Modern (VoIP/Digital) and Legacy Systems

### Legacy (Analog) Systems

- DTMF generated and transmitted as analog audio signals over the Public Switched Telephone Network (PSTN).
- Telephone exchange decodes tones to interpret input.

### Digital and VoIP (Voice over IP) Systems

- Modern VoIP networks do not natively transmit analog DTMF tones.
- DTMF signals may be sent:
  - <strong>In-band:</strong>As audio tones within the voice stream (e.g., RTP).
  - <strong>Out-of-band:</strong>As digital events in the signaling protocol (e.g., SIP INFO, RFC 2833/4733, KPML).
- <strong>Interoperability:</strong>VoIP platforms must relay DTMF signals in a format compatible with legacy and current digital systems.
- <strong>Mobile (Cellular) Phones:</strong>Modern mobile devices transmit dialed numbers digitally but can generate DTMF tones during calls for menu navigation.

- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)

## Technical Standards for DTMF

### ITU-T Q.23 and Keypad Mapping

- <strong>ITU-T Recommendation Q.23:</strong>Defines the frequency pairs, tone duration, and keypad layout for DTMF signaling, ensuring consistent global signaling.
- <strong>RFC 2833/4733:</strong>Specifies DTMF relay in VoIP (RTP payload for telephony events).
- <strong>SIP INFO/KPML:</strong>Alternative methods for DTMF signaling in SIP environments.

- [ITU-T Recommendation Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [Twilio: DTMF Tones & Standards](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)

## DTMF Signaling: In-Band vs. Out-of-Band

- <strong>In-Band Signaling:</strong>DTMF tones sent as audible signals in the same channel as voice audio (PSTN, analog, some VoIP RTP streams). Any participant can hear the tones.
- <strong>Out-of-Band Signaling:</strong>DTMF digits sent digitally outside the voice channel, using signaling protocols (e.g., SIP INFO, RFC 2833/4733).
- <strong>Security Note:</strong>In-band is susceptible to interception and fraud; out-of-band is preferred for secure, reliable transmission in digital networks.

- [Twilio: In-Band vs. Out-of-Band Signaling](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)

## DTMF, AI Chatbots, and Automation

- DTMF enables direct interaction with automated systems (IVR, chatbots, virtual agents) via keypad input.
- AI-powered platforms listen for DTMF to process menu selections, collect data, and route calls.
- <strong>Advantages:</strong>- Faster menu navigation.
  - Reduced errors in noisy environments compared to speech recognition.
  - Secure entry of sensitive data (PINs, card numbers) without verbalizing.
  - Lower operational costs by reducing live agent involvement.

- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)

## DTMF and PCI DSS Compliance

<strong>Why DTMF masking matters:</strong>When customers enter payment card details using the phone keypad, the resulting DTMF signals can be captured in call recordings or by agents, posing a security and compliance risk.

<strong>DTMF masking</strong>intercepts and obscures DTMF tones before they reach agents or recordings, replacing the tones with asterisks or blanking them out. This keeps the contact center out of PCI DSS scope and prevents sensitive data exposure.

<strong>Benefits:</strong>- Reduces fraud risk.
- Simplifies PCI DSS compliance.
- Improves customer trust.
- Enables agent-assisted or IVR payment flows without pausing recordings.

<strong>How it works:</strong>- Real-time interception: As the customer enters digits, the system detects and removes tones before they reach the agent or recording.
- Masking is available for both on-premise and cloud-based contact centers and works across SIP/ISDN infrastructures.

<strong>Demonstration:</strong>Watch a real-world DTMF masking and PCI DSS compliant payment demo in NICE CXone:  
[YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)

- [Sycurio: What is DTMF Masking?](https://sycurio.com/blog/dtmf-masking)
- [PCI Pal Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)

## Examples and Practical Scenarios

<strong>IVR Menu Navigation:</strong>"Press 1 for account balance, 2 for transactions, 3 to speak to a representative." The system detects DTMF for "1" and routes the call.

<strong>Secure Payment Entry:</strong>A customer enters their credit card number using the phone keypad. DTMF tones are masked and securely processed.

<strong>Conference Call Controls:</strong>A host mutes all participants by pressing "*5"; the system detects the DTMF and executes the command.

<strong>Remote Access:</strong>A facility manager calls a security system and enters a code via DTMF to open a remote gate.

<strong>Ham Radio Repeater Activation:</strong>An operator sends a DTMF sequence to activate a repeater or control equipment.

## Further Reading & Related Terms

- [Interactive Voice Response (IVR)](https://www.nice.com/products/interactive-voice-response-ivr)
- [Session Initiation Protocol (SIP)](https://www.techtarget.com/searchunifiedcommunications/definition/Session-Initiation-Protocol)
- [Pulse Dialing](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [In-Band vs. Out-of-Band Signaling](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [ITU-T Recommendation Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [PCI DSS Compliance](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [SIP INFO, KPML, RFC 2833](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP (Voice over IP)](https://www.techtarget.com/searchunifiedcommunications/definition/VoIP)

<strong>See Also:</strong>- Touch-Tone Phones
- Band Signaling
- Call Centers
- Customer Experience Automation
- Telecommunication Systems

## References

- [Sycurio: DTMF Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [Sycurio: DTMF Masking Guide](https://sycurio.com/blog/dtmf-masking)
- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)
- [YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)
- [PCI Pal Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)

### Visual Aids Suggestions
- DTMF keypad matrix with frequency labels.
- Block diagram showing DTMF generation and detection in IVR.
- Flowchart of DTMF signaling in PSTN vs. VoIP networks.

<strong>Summary:</strong>DTMF (Dual-Tone Multi-Frequency) is the global standard for encoding keypad signals into pairs of audio frequencies, enabling telephones, IVR systems, and automation platforms to interpret input. DTMF replaced pulse dialing, supports secure data entry, drives automation in call centers, and remains indispensable in both legacy analog and modern digital VoIP telecommunication networks. For further technical depth, protocol specifics, and compliance guidance, consult the references and linked resources throughout this glossary.

<strong>For in-depth technical videos:</strong>- [YouTube: DTMF Explainer Video](https://www.youtube.com/watch?v=bAbNl8O6sSY)
- [YouTube: Sycurio DTMF Masking & PCI DSS Demo](https://www.youtube.com/watch?v=-iMrUREflUY)
