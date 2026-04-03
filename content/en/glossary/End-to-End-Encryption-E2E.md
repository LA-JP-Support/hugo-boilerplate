---
title: "End-to-End Encryption (E2E)"
date: 2025-03-01
lastmod: 2026-04-02
description: "An encryption method that secures the entire communication path from sender to receiver, preventing eavesdropping along the transmission route."
translationKey: "end-to-end-encryption-e2e"
category: "Security & Compliance"
type: glossary
draft: false
url: /en/glossary/End-to-End-Encryption-E2E/
---

## What is End-to-End Encryption (E2E)?

**End-to-end encryption is a method that encrypts all communication from the sender's device to the receiver's device.** Even server companies cannot decrypt or view exchanged messages. Messaging apps like WhatsApp, Signal, and Telegram employ this approach, achieving the highest level of privacy protection.

> **In a nutshell:** You place a letter in a locked box and send it to the recipient, who is the only one who can open it. The shipping company (server company) cannot see the contents.

**Key points:**

- **What it does:** Consistently encrypts communication content from sending to receiving
- **Why it's needed:** To prevent eavesdropping by ISPs, server companies, and government agencies
- **Who uses it:** Messaging apps, email, cloud storage, and all services requiring confidential communication

## Why it matters

In traditional web communication, while communication between users and servers was encrypted, data was stored in plaintext on the server. This meant that server companies or hackers gaining access to the server could read all messages.

End-to-end encryption fundamentally solves this problem. Messages remain encrypted even when stored on servers, and not even the server company can decrypt them. Even if government requests for information are made, there is nothing to provide.

The importance of this security model continues to grow as privacy rights are recognized as fundamental human rights. In particular, for journalists, human rights activists, and medical consultants—those whose communication secrecy is literally life-threatening—end-to-end encryption is essential.

However, companies face trade-offs. Message companies cannot monitor user communications to detect spam or illegal content.

## How it works

End-to-end encryption functions through broadly four steps.

The first step is "key exchange." Before A sends a message to B, both parties must safely exchange a "shared key" for encryption. In this process, public key cryptography is employed. A encrypts the message using B's public key, and only B can decrypt it with the private key. By repeating this, even if someone intercepts the communication, without the correct private key, data remains unreadable.

The next step is "message encryption." A encrypts the message they want to send using the shared key or public key. At this point, the message becomes meaningless characters.

The third step is "sending the encrypted message." The encrypted message is transmitted via the server to B's device. The server company cannot view the contents.

The final step is "decryption by the receiver." B uses the private key to decrypt the encrypted message and read the original content. Throughout this entire process, intermediaries (ISPs, server companies, government agencies) cannot intercept communications.

## Real-world use cases

**Confidential communication by human rights activists**

Human rights activists in countries with high risks of government repression use messaging apps that employ end-to-end encryption (such as Signal). Even if government agencies attempt to eavesdrop, their messages are impossible to intercept. Without this protection, activists' identities and plans could become known to authorities, risking arrest.

**Telemedicine communication between doctors and patients**

When healthcare providers offer telemedicine services, patient medical information is highly confidential. End-to-end encryption ensures that patient-doctor communications cannot be viewed by healthcare staff or cybercriminals. This allows patients to report symptoms without hesitation.

**Communication between journalists and sources**

When investigative journalists communicate with sources holding confidential information (whistleblowers, etc.), the secrecy of that communication is extremely important. Without end-to-end encryption, if governments or companies intercept communications, the source's identity could be exposed, creating risk of retaliation.

## Benefits and considerations

The greatest benefit of end-to-end encryption is absolute privacy protection—only the sender and receiver can read messages. Since even server companies cannot decrypt, the highest standards of customer data protection required by [GDPR](GDPR-General-Data-Protection-Regulation.md) and national regulations are achieved. Customer trust also increases, forming an image of a "privacy-respecting company."

However, service providers face challenges. They can no longer conduct "crime prevention" or "spam detection" on end-to-end encrypted communications. Terrorists and spammers could potentially misuse end-to-end encryption for illegal activity. Additionally, if users lose their keys, messages become unreadable forever. Backup mechanisms are important.

Furthermore, because of its complex security model, implementation errors are common. Incomplete end-to-end encryption can give users a false sense of security—feeling "this is safe"—which can actually be more dangerous.

## Related terms

- **[Encryption](Encryption.md)** — The fundamental technology underlying end-to-end encryption
- **[GDPR](GDPR-General-Data-Protection-Regulation.md)** — A privacy regulation that recommends end-to-end encryption
- **[Public Key Infrastructure (PKI)](Public-Key-Infrastructure-PKI.md)** — The foundational infrastructure enabling end-to-end encryption
- **[Data Minimization](Data-Minimization.md)** — A privacy protection principle parallel to end-to-end encryption
- **[Privacy by Design](Privacy-by-Design.md)** — An implementation approach for end-to-end encryption

## Frequently asked questions

**Q: If end-to-end encryption is in place, what about backups?**

A: Backup mechanisms create a conflict between security and user convenience. True [End-to-End Encryption](End-to-End-Encryption-E2E.md) cannot support backups. Many apps allow users to optionally "enable" backups, delegating responsibility by having users understand the security implications.

**Q: If companies implement end-to-end encryption, can they address illegal content?**

A: In theory, companies cannot detect encrypted message contents. However, indirect detection using "metadata" (sender, receiver, send time, etc.) is possible. For example, "sending messages to an unusually large number of users" suggests spam potential.

**Q: Can governments ban the use of end-to-end encryption apps?**

A: Legal bans are possible, but enforcement is difficult. Encryption is mathematics—bans don't make the technology disappear. For example, Russia and China have attempted to restrict encrypted app usage, but users circumvent this through VPNs from other countries. Balancing privacy rights and law enforcement authority remains an important policy challenge.
