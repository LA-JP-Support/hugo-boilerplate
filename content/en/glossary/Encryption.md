---
title: "Encryption"
date: 2025-03-01
lastmod: 2026-04-02
description: "A technology that transforms data into a format unreadable to third parties, securing sensitive information through cryptographic methods."
translationKey: "encryption"
category: "Security & Compliance"
type: glossary
draft: false
url: /en/glossary/Encryption/
---

## What is Encryption?

**Encryption is a technology that converts original data (plaintext) into an unreadable format (ciphertext) using a specific cryptographic key.** Only those with the correct key can decrypt (restore) the original data. It is the foundation for protecting highly sensitive data such as credit card numbers, passwords, and medical records.

> **In a nutshell:** It's like placing an important letter in a locked box that only certain people can open. Even if the box is stolen, the contents remain hidden without the key.

**Key points:**

- **What it does:** Converts data into an unreadable form and prevents unauthorized access
- **Why it's needed:** To mitigate risks from cyberattacks and data breaches
- **Who uses it:** Financial institutions, healthcare companies, SaaS providers, and all organizations handling sensitive data

## Why it matters

Data breaches are among the greatest risks to modern businesses. Annually, millions of personal information leaks are reported. However, the majority were due to negligent security practices—specifically, data was not encrypted. In reality, many breaches don't result from cyberattacks but from simple issues like unencrypted data being stolen by insiders or unencrypted hard drives being sold second-hand.

With encryption in place, even if data is stolen, it cannot be read without the key. Regulations like GDPR and APPI explicitly identify encryption as a "fundamental principle" of personal data protection, making it a mandatory requirement in most compliance standards.

Additionally, the presence or absence of encryption affects notification obligations following security breaches. Many laws stipulate that if unencrypted personal information is leaked, organizations must immediately notify users and report to government agencies. Conversely, if data was strongly encrypted, legal notification obligations may be reduced.

## How it works

Encryption comes in two major categories.

**Symmetric key encryption (shared key encryption)** uses the same key for both encryption and decryption. For example, data encrypted with the key "ABCDEFG" is decrypted using the same "ABCDEFG" key. This approach is fast and well-suited for file storage and communication encryption. However, the challenge of how to securely share the key (the "key exchange problem") arises.

**Asymmetric key encryption (public key encryption)** uses two different keys: a "public key" for encryption and a "private key" for decryption. Data encrypted with the public key can only be decrypted with the private key, eliminating the need for key exchange. It is used for internet communication and email encryption, but its slower processing speed makes it unsuitable for large volumes of data.

In practice, both approaches are combined. Data is encrypted using the fast symmetric key, while the symmetric key itself is encrypted with a public key for transmission. This is called "hybrid encryption."

The computational difficulty of decryption is also critical. Strong encryption means that "finding the key through trial and error would take longer than realistic computing power can manage, often many decades or more." For example, AES-256 encryption is said to require decades with current technology and is the standard for financial institutions.

## Real-world use cases

**Credit card payment encryption**

When an e-commerce site receives a customer's credit card number, [End-to-End Encryption](End-to-End-Encryption-E2E.md) encrypts the communication from the user's browser to the server. Additionally, on the server side, the card number is not stored as-is but converted into an encrypted token. Even if the server is compromised, the encrypted token alone is not useful.

**Cloud storage file encryption**

Enterprise storage services like OneDrive and Google Drive encrypt files uploaded by users with the user's encryption key. Even company staff lack the authority to decrypt encrypted files, guaranteeing privacy. This model, called "zero-knowledge architecture," achieves the highest level of privacy protection.

**Medical record protection**

Healthcare providers often encrypt patient identifying information (name, ID) and medical content separately. This makes it difficult for the connection between identity and medical information to be discovered even if data is leaked. This approach is called "key separation."

## Benefits and considerations

The greatest benefit of encryption is that privacy is protected even if data is stolen. Organizations are also recognized as [GDPR](GDPR-General-Data-Protection-Regulation.md)-compliant, reducing regulatory risk. Customer trust increases as well.

However, encryption has drawbacks. Encryption carries computational costs and processing overhead. If all data is protected with strong encryption, system response speed may decrease. Additionally, searching and analyzing encrypted information becomes difficult. For example, searching for "customers aged 18 and over" is fast with unencrypted data, but encrypted data may require full decryption.

Furthermore, key management is complex. Strong encryption becomes meaningless if keys are lost or improperly stored. Many organizations implement "Key Management Systems (KMS)" to automate key generation, storage, and rotation.

## Related terms

- **[End-to-End Encryption](End-to-End-Encryption-E2E.md)** — An encryption method that secures the entire communication path from device to server
- **[Data Minimization](Data-Minimization.md)** — A fundamental data protection principle alongside encryption
- **[GDPR](GDPR-General-Data-Protection-Regulation.md)** — A regulation that positions encryption as a basic security measure
- **[Access Control](Access-Control.md)** — A technology that combines with encryption to achieve layered defense
- **[Security Audit](Security-Audit.md)** — A process to validate the appropriateness of encryption implementation

## Frequently asked questions

**Q: Should all data be encrypted, or just sensitive data?**

A: At minimum, personally identifiable information (name, email, address) and financial data (credit card numbers, bank accounts) must be encrypted. For other data, the decision should depend on the risk level if that data were breached. Access logs and publicly available information have lower encryption priority.

**Q: If encrypted data is breached, must users be notified?**

A: In most GDPR and APPI jurisdictions, notification obligations may be reduced or waived for "strongly encrypted data breaches." However, if encryption is incomplete or keys are also compromised, notification obligations apply. It's best to always err on the side of caution.

**Q: Can cloud companies decrypt and view user data?**

A: It depends on the encryption method the company uses. If the company manages the keys, decryption is theoretically possible. However, trustworthy companies explicitly state in their terms that they will not decrypt without customer consent. For the highest level of privacy, users should choose "client-side encryption" where they manage the keys themselves.
