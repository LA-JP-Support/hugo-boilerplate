---
title: GDPR Glossary and Deep-Dive Reference
date: 2025-12-17
translationKey: gdpr
description: Understand GDPR, the EU's comprehensive data protection regulation. Learn
  about its principles, compliance requirements, data subject rights, and impact on
  AI chatbots.
keywords:
- GDPR
- data protection
- personal data
- AI chatbots
- data subject rights
category: AI Chatbot & Automation
type: glossary
draft: false
---

## What is GDPR?

<strong>GDPR</strong>stands for <strong>General Data Protection Regulation</strong>([Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). It is the most robust and comprehensive data privacy framework in effect globally, directly applicable in all EU and EEA member states since May 25, 2018. GDPR replaced the 1995 Data Protection Directive, modernizing and harmonizing privacy laws across Europe and extending protections to all individuals within the EU/EEA, regardless of nationality or residency.

<strong>Key Attributes:</strong>- Legally binding across all EU/EEA member states; applies to any entity processing EU/EEA residents’ data, even outside Europe ([source](https://gdpr.eu/)).
- Regulates the collection, processing, storage, and transfer of personal data.
- Empowers individuals with enforceable rights over their personal information.
- Imposes strict obligations and accountability on organizations.

<strong>Purpose:</strong>GDPR’s core aim is to give individuals greater control over their personal data, ensure consistent data protection across the EU, and require organizations to treat personal information with transparency and respect.  
- [Detailed guide from OneTrust](https://www.onetrust.com/blog/gdpr-compliance/)

## How is GDPR Used?

GDPR governs every aspect of handling personal data, from collection to deletion, including:
- Gathering data via websites, mobile apps, chatbots, and IoT devices.
- Processing data for customer service, marketing, research, or analytics.
- Sharing or transferring data inside or outside the EU/EEA.
- Using AI, profiling, or automated decision-making that impacts individuals.

Organizations must demonstrate compliance throughout the lifecycle of data—design, deployment, and ongoing operations ([GDPR.eu: GDPR compliance](https://gdpr.eu/compliance/)).

<strong>Example in Practice:</strong>A SaaS company offering chatbot services to EU customers must ensure every stage—from initial chat to data storage and analytics—meets GDPR standards, including obtaining valid user consent, ensuring security, and providing data subject rights.

## Key Terms and Definitions

- <strong>Personal Data:</strong>Any information relating to an identified or identifiable natural person (“data subject”)—including names, email addresses, ID numbers, online identifiers (IP addresses, cookies), location data, and more ([GDPR Article 4(1)](https://gdpr-info.eu/art-4-gdpr/)).
- <strong>Data Subject:</strong>The individual whose personal data is processed.
- <strong>Data Controller:</strong>The entity determining the purposes and means of processing personal data (e.g., a company, public body).
- <strong>Data Processor:</strong>A party processing data on behalf of the controller (e.g., cloud providers, outsourced support).
- <strong>Processing:</strong>Any operation—automated or manual—performed on personal data, such as collection, storage, retrieval, use, disclosure, or deletion.
- <strong>Consent:</strong>A freely given, specific, informed, and unambiguous indication of a data subject’s agreement to processing ([EDPB guidelines on consent](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2018/guidelines-052020-consent-under-regulation-eu_en)).
- <strong>Special Categories of Personal Data:</strong>Sensitive information requiring enhanced protection, such as data revealing racial or ethnic origin, political opinions, religious beliefs, trade union membership, genetic or biometric data, health data, and data concerning sexual life or orientation ([GDPR Article 9](https://gdpr-info.eu/art-9-gdpr/)).
- <strong>Automated Decision-Making/Profiling:</strong>Use of algorithms or AI to assess or decide about individuals without human intervention ([GDPR Article 22](https://gdpr-info.eu/art-22-gdpr/)).

For a full glossary, see [GDPR.eu Glossary](https://gdpr.eu/glossary/).

## GDPR in Context: AI Chatbots & Automation

AI chatbots and automation systems frequently collect, process, and store personal data, such as names, emails, preferences, and user behaviors. GDPR applies if:
- The user is located in the EU/EEA.
- The chatbot processes data that can identify a person—even indirectly.
- Automated decision-making or profiling is used.

<strong>Key Compliance Factors:</strong>- Chatbots must be transparent about data collection and processing.
- Users must be able to give, refuse, or withdraw consent at any time.
- Mechanisms must be provided for users to exercise their GDPR rights.
- For automated decisions that have legal or significant effects, human review must be available.

<strong>Example:</strong>A customer support chatbot collecting user queries and storing chat logs must obtain consent, provide clear privacy notices, and allow users to request deletion of their data.

- [EDPB Guidelines on AI and Data Protection](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2021/guidelines-052021-artificial-intelligence-and_en)
- [GDPR.eu on AI](https://gdpr.eu/artificial-intelligence/)

## Core Principles of GDPR

GDPR is built on seven foundational principles ([GDPR Article 5](https://gdpr-info.eu/art-5-gdpr/)):
1. <strong>Lawfulness, Fairness, and Transparency:</strong>Data must be processed lawfully and fairly, with clear information provided to individuals.
2. <strong>Purpose Limitation:</strong>Data collected for specified, explicit, and legitimate purposes cannot be used for incompatible purposes.
3. <strong>Data Minimization:</strong>Only necessary data should be collected and processed.
4. <strong>Accuracy:</strong>Personal data must be accurate and kept up to date.
5. <strong>Storage Limitation:</strong>Data should not be kept longer than necessary.
6. <strong>Integrity and Confidentiality:</strong>Personal data must be protected against unauthorized access, loss, or damage.
7. <strong>Accountability:</strong>Controllers must document and demonstrate compliance with all principles ([OneTrust: GDPR Principles](https://www.onetrust.com/blog/gdpr-compliance/#gdpr-principles)).

## Who Must Comply with GDPR?

<strong>GDPR applies to:</strong>- All organizations established in the EU/EEA, regardless of where processing occurs.
- Any organization (worldwide) offering goods/services to, or monitoring the behavior of, individuals in the EU/EEA.

<strong>Examples:</strong>- A US-based website selling to EU customers.
- An AI chatbot provider with EU client data.

<strong>Territorial Scope:</strong>GDPR’s extraterritorial reach means global businesses must assess their exposure and compliance obligations ([GDPR territorial scope explained](https://gdpr.eu/companies-outside-of-europe/)).

## Special Categories of Personal Data

GDPR identifies specific categories of data requiring heightened protection ([GDPR Article 9](https://gdpr-info.eu/art-9-gdpr/)), including:
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Biometric data for identification
- Health data
- Data concerning a person’s sex life or orientation

Processing these data is generally prohibited unless an explicit legal basis exists, such as explicit consent, vital interests, or legal obligations.

<strong>Example:</strong>A health chatbot collecting symptoms from users must get explicit consent and implement robust security ([OneTrust: Special Category Data](https://www.onetrust.com/blog/gdpr-compliance/#special-categories-of-personal-data)).

## Obtaining Valid Consent

Consent must meet strict requirements ([EDPB Guidelines on Consent](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2018/guidelines-052020-consent-under-regulation-eu_en)):

- <strong>Freely given:</strong>No coercion or forced consent.
- <strong>Specific:</strong>Covering each separate processing purpose.
- <strong>Informed:</strong>Users know what they are consenting to.
- <strong>Unambiguous:</strong>Clear affirmative action, not silence or pre-ticked boxes.

<strong>Best Practices:</strong>- Use granular consent forms.
- Log and document all consents (with time, method, and purpose).
- Allow users to withdraw consent as easily as it was given.

<strong>Example:</strong>Before a chatbot stores user preferences, it must clearly state how data will be used and allow users to opt in or out ([GDPR.eu: Consent](https://gdpr.eu/consent/)).

## Data Subject Rights

GDPR grants data subjects powerful rights ([GDPR Articles 12–23](https://gdpr-info.eu/chapter-3/)):
1. <strong>Right to be Informed:</strong>About data collection and use.
2. <strong>Right of Access:</strong>To their personal data.
3. <strong>Right to Rectification:</strong>To correct inaccurate data.
4. <strong>Right to Erasure (“Right to be Forgotten”):</strong>To have data deleted under certain conditions.
5. <strong>Right to Restrict Processing:</strong>To limit how data is used.
6. <strong>Right to Data Portability:</strong>To receive data in a structured, machine-readable format.
7. <strong>Right to Object:</strong>To processing for legitimate interests, public tasks, or direct marketing.
8. <strong>Rights Related to Automated Decision-Making and Profiling:</strong>To not be subject to decisions based solely on automated processing.

<strong>Example:</strong>A user requests deletion of all their chatbot conversation logs; the provider must comply unless a legal retention obligation exists ([GDPR.eu: Rights](https://gdpr.eu/rights/)).

## Practical Use Cases & Examples

<strong>1. AI Chatbot for Customer Support</strong>- <strong>Scenario:</strong>Handles customer inquiries from EU residents.
- <strong>GDPR Requirements:</strong>Inform users about chat recording, obtain consent for special data, allow data access and deletion ([OneTrust: Chatbots and GDPR](https://www.onetrust.com/blog/gdpr-compliance/#ai-chatbots)).

<strong>2. Automated Loan Approval</strong>- <strong>Scenario:</strong>Algorithm decides on loan applications.
- <strong>GDPR Requirements:</strong>Explain automated decision logic, offer human review, prevent discrimination ([EDPB on Automated Decisions](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2018/guidelines-022018-automated-individual_en)).

<strong>3. Data Transfer to Third Countries</strong>- <strong>Scenario:</strong>EU chatbot provider stores data in the US.
- <strong>GDPR Requirements:</strong>Use Standard Contractual Clauses, inform users, ensure third-country protections ([EDPB: International Transfers](https://www.edpb.europa.eu/our-work-tools/our-documents/topic/international-transfers-data_en)).

## Compliance Requirements in Practice

<strong>Key Organizational Steps:</strong>1. <strong>Appoint a Data Protection Officer (DPO):</strong>Needed for public authorities or if core activities involve large-scale, regular monitoring or special category data ([GDPR Article 37](https://gdpr-info.eu/art-37-gdpr/)).
2. <strong>Maintain Processing Records:</strong>Document data types, purposes, retention, and sharing ([GDPR Article 30](https://gdpr-info.eu/art-30-gdpr/)).
3. <strong>Conduct Data Protection Impact Assessments (DPIAs):</strong>For high-risk processing (e.g., profiling, large-scale data) ([EDPB Guidelines on DPIAs](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2017/guidelines-012017-data-protection-impact_en)).
4. <strong>Implement Privacy by Design and by Default:</strong>Embed data protection in systems from the outset ([GDPR Article 25](https://gdpr-info.eu/art-25-gdpr/)).
5. <strong>Consent Management:</strong>Enable users to give, refuse, and withdraw consent easily.
6. <strong>Incident Response:</strong>Prepare to detect, report, and communicate data breaches within 72 hours ([GDPR Article 33](https://gdpr-info.eu/art-33-gdpr/)).
7. <strong>Staff Training:</strong>Make GDPR awareness and procedures standard across teams.
8. <strong>Review Cross-Border Transfers:</strong>Use legally approved mechanisms for data leaving the EU/EEA ([EDPB: International Transfers](https://www.edpb.europa.eu/our-work-tools/our-documents/topic/international-transfers-data_en)).
9. <strong>Regular Audits:</strong>Review and update compliance measures ([OneTrust: GDPR Checklist](https://www.onetrust.com/blog/gdpr-compliance/#11-step-gdpr-checklist)).

## Automated Decision-Making and Profiling

<strong>Article 22 GDPR</strong>grants individuals the right not to be subject to decisions based solely on automated processing (including profiling) that produce legal or similarly significant effects.

<strong>Exceptions:</strong>- Necessary for contract performance.
- Authorized by EU or member state law.
- Based on explicit consent.

<strong>Safeguards:</strong>- Human intervention and review.
- Right to express a viewpoint and contest decisions.

<strong>Example:</strong>A recruitment chatbot that filters candidates must allow rejected applicants to request a human review ([EDPB Guidelines on Automated Decisions](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2018/guidelines-022018-automated-individual_en)).

## Penalties for Non-Compliance

GDPR enforcement is strict and fines are substantial ([GDPR Article 83](https://gdpr-info.eu/art-83-gdpr/)):
- Up to €20 million or 4% of worldwide annual turnover (whichever is higher) for severe breaches.
- Up to €10 million or 2% of turnover for less serious violations.
- Other consequences include lawsuits, reputational damage, and regulatory scrutiny.

<strong>Notable Cases:</strong>- [Google fined €50 million for lack of transparency and valid consent](https://www.cnil.fr/en/cnils-restricted-committee-imposes-financial-penalty-50-million-euros-against-google-llc).
- [British Airways fined £20 million for security failures](https://www.ico.org.uk/about-the-ico/news-and-events/news-and-blogs/2020/10/ico-fines-british-airways-20m-for-data-breach/).

## Summary Table: GDPR Compliance Steps

| Step                        | Description                                              |
|-----------------------------|----------------------------------------------------------|
| Appoint DPO (if required)   | Assign responsibility for data protection                |
| Maintain records            | Document what data you process and why                   |
| Conduct DPIAs               | Assess and mitigate high-risk processing                 |
| Privacy by design           | Integrate data protection at every stage                 |
| Consent & rights mechanisms | Enable users to manage data and consents                 |
| Breach notification         | Establish rapid response to data incidents               |
| Staff training              | Educate all personnel on GDPR                            |
| Secure transfers            | Use approved mechanisms for data leaving EU/EEA          |
| Audit regularly             | Review, update, and document compliance practices        |

## Frequently Asked Questions (FAQ)

<strong>Q1: Does GDPR apply to my company if I’m outside the EU?</strong>Yes—if you process personal data of EU/EEA residents by offering goods or services, or monitoring behavior.

<strong>Q2: What is considered “personal data” under GDPR?</strong>Any information relating to an identified or identifiable person, including digital identifiers.

<strong>Q3: How does GDPR affect AI chatbots?</strong>If chatbots interact with EU/EEA users and process their data, GDPR rules—lawful processing, transparency, consent, and rights—apply.

<strong>Q4: Can I use automated profiling under GDPR?</strong>Yes, but you must inform users, obtain explicit consent if profiling has significant effects, and provide human review ([GDPR Article 22](https://gdpr-info.eu/art-22-gdpr/)).

<strong>Q5: What happens if I violate GDPR?</strong>You risk major fines, legal action, and reputational harm.

## References

1. [GDPR.eu – What is the GDPR?](https://gdpr.eu/)
2. [OneTrust – Your complete guide to General Data Protection Regulation (GDPR) compliance](https://www.onetrust.com/blog/gdpr-compliance/)
3. [European Data Protection Board (EDPB) – Guidelines, Recommendations, Best Practices](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en)
4. [GDPR – Full legal text (gdpr-info.eu)](https://gdpr-info.eu/)
5. [EDPB Guidelines on AI and Data Protection](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2021/guidelines-052021-artificial-intelligence-and_en)
6. [EDPB Guidelines on Consent](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2018/guidelines-052020-consent-under-regulation-eu_en)
7. [EDPB Guidelines on Automated Individual Decision-Making and Profiling](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2018/guidelines-022018-automated-individual_en)
8. [EDPB Guidelines on DPIAs](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2017/guidelines-012017-data-protection-impact_en)
9. [ICO – British Airways fine](

