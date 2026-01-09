---
title: "Contact Lens for Amazon Connect"
lastmod: 2025-12-18
date: 2025-12-18
translationKey: "contact-lens-for-amazon-connect"
description: "An AI service that automatically transcribes customer calls and chats, analyzes emotions and issues, and protects sensitive information for contact centers."
keywords: ["Contact Lens for Amazon Connect", "Amazon Connect", "conversational analytics", "sentiment analysis", "sensitive data redaction"]
category: "AI-Driven Contact Center Analytics"
type: "glossary"
draft: false
---

## What Is Contact Lens for Amazon Connect?

Contact Lens for Amazon Connect delivers a comprehensive suite of machine learning (ML) analytics to contact centers. Embedded in Amazon Connect, it automates transcription, sentiment analysis, issue detection, sensitive data redaction, and contact categorization for both voice and chat channels. The service leverages natural language processing (NLP) and advanced speech analytics to provide actionable insights into customer-agent and customer-bot conversations.

Contact Lens is fully accessible within the Amazon Connect console—no third-party integration required—and supports granular configuration at the contact flow level. It enables compliance-focused organizations to mask sensitive data and audit interactions for regulatory adherence, while supervisors and analysts gain powerful search, reporting, and workflow automation tools.

<strong>Key Attributes:</strong>- Native to Amazon Connect, available through a simple console toggle
- Supports voice and chat, with real-time and post-call/post-chat analytics
- Automated redaction of PII (personally identifiable information) in transcripts and audio
- Actionable sentiment scoring, issue detection, and customizable categorization
- Secure, compliant, and easily integrated with AWS data lakes and BI tools

## How Contact Lens for Amazon Connect Is Used

Organizations use Contact Lens to automate and supercharge quality assurance, compliance monitoring, operational analytics, and customer experience improvement. It enables:

<strong>Automated QA and Compliance</strong>Reviews 100% of interactions, flags compliance issues, and redacts sensitive data automatically.

<strong>Customer Experience Monitoring</strong>Tracks customer sentiment and identifies pain points in real time and historically.

<strong>Workforce Optimization</strong>Reduces manual after contact work (ACW) via automated summaries and highlights coaching opportunities.

<strong>Actionable Insights</strong>Surfaces trends, emerging issues, and process bottlenecks using advanced metrics and customizable dashboards.

Contact Lens is turned on at the flow level in Amazon Connect via the "Set Recording and Analytics Behavior" block, allowing organizations to tailor analytics to specific interaction types or scenarios.

## Key Features of Contact Lens for Amazon Connect

### 1. Automated Transcription and Indexing

<strong>Functionality:</strong>All voice and chat interactions are automatically transcribed using AWS's advanced speech-to-text and NLP engines.

<strong>Searchability:</strong>Transcripts are indexed, enabling full-text search by keyword, phrase, or sentiment across all historical interactions.

<strong>Supervisor Benefits:</strong>QA and compliance leads can locate relevant calls instantly, eliminating manual audio review.

### 2. Sentiment Analysis

<strong>How It Works:</strong>Each customer and agent utterance is scored for sentiment (positive, negative, or neutral). Scores are aggregated and visualized as sentiment trends throughout the interaction.

<strong>Use Cases:</strong>Supervisors filter for negative sentiment contacts, identify at-risk customers, and monitor agent performance objectively.

### 3. Issue Detection and Non-Talk Time Analytics

<strong>Capabilities:</strong>Identifies call drivers, interruptions, long silences, hold durations, and overlapping speech.

<strong>Value:</strong>Pinpoints root causes, agent or bot training opportunities, and workflow bottlenecks.

<strong>Visualization:</strong>Graphs display talk time split by agent/customer, silence, and hold time.

### 4. Automated Contact Categorization

<strong>How It Works:</strong>Lets users define rules for tagging interactions based on keywords, phrases, or compliance criteria. E.g., script adherence, competitor mentions, escalation triggers.

<strong>Automated Reporting:</strong>Enables dynamic aggregation and reporting for QA, compliance, escalation, and business outcomes.

### 5. Sensitive Data Redaction

<strong>PII Redaction:</strong>Automatically detects and redacts PII such as names, addresses, credit card numbers, and social security numbers from both transcript and audio.

<strong>Compliance:</strong>Supports PCI DSS, GDPR, and other data privacy standards by masking sensitive data in stored records and supervisor/agent views.

<strong>Configuration:</strong>Choose which PII types to redact and whether to output only redacted or both redacted/original files.

### 6. Real-Time and Post-Call Analytics

<strong>Real-Time Analytics:</strong>- Provides live metrics, sentiment tracking, and configurable alerts during active calls or chats
- Enables supervisors to intervene or coach agents based on negative sentiment or key phrase detection

<strong>Post-Call Analytics:</strong>- Delivers detailed post-interaction summaries, insights, and categorization
- Supports trend analysis, coaching, and root cause analysis

### 7. Customizable Workflows and Output

<strong>Language Support:</strong>Supports multiple languages for transcription, sentiment, and redaction. Language can be set per flow or dynamically via Lambda/contact attributes.

<strong>Data Export & Integration:</strong>Detailed analytics, transcripts, and metadata are exportable to Amazon S3. Integrates with BI tools (e.g., Amazon QuickSight, Tableau) and custom ML workflows (e.g., Amazon SageMaker).

## Advanced Configuration and Deployment

### Enabling Contact Lens

1. Access the Amazon Connect Console
2. Navigate to your instance, go to the *Analytics Tools* section, and enable Contact Lens
3. In the contact flow designer, insert a <strong>Set Recording and Analytics Behavior</strong>block where analytics is needed
4. Set recording to *Agent and Customer* for voice analytics
5. Enable Contact Lens analytics, selecting real-time, post-call, or both
6. Configure language, redaction, and analytics settings as needed
7. Save and deploy the flow
8. Repeat for any transfer or specialized flows

<strong>Note:</strong>Recording both agent and customer is mandatory for full voice analytics. For chat analytics, ensure chat recording is enabled.

### Redaction Parameter Options

<strong>Scope:</strong>Redact all supported PII or only selected entities (credit card, address, etc.)

<strong>Output Handling:</strong>Choose between storing only redacted files or both redacted and original versions

<strong>Replacement:</strong>Specify placeholder text (e.g., "[PII]") for redacted sections

<strong>Important:</strong>Automated redaction is not HIPAA-certified; always verify accuracy.

### Sentiment Analysis Options

- Enabled by default when analytics is active and the language is supported
- Can be disabled in the analytics block if not required

### Dynamic Configuration

Use *Set contact attributes* blocks or AWS Lambda to dynamically set analytics parameters (language, redaction, etc.) per contact.

## Example Use Cases

### 1. Quality Assurance and Compliance

A financial services provider ensures script compliance and data privacy:
- Automated transcription enables instant search for required script phrases
- Credit card data is redacted from transcripts and audio
- Calls missing compliance phrases are flagged for supervisor review

### 2. Proactive Customer Experience Management

A retailer uses real-time analytics to intervene during negative interactions:
- Supervisors receive alerts when customer sentiment turns negative or critical keywords are detected
- Supervisors can join live calls or send guidance to agents in real time

### 3. Reducing After Contact Work (ACW)

An e-commerce company automates post-call documentation:
- Contact Lens generates post-call summaries and highlights
- These are automatically attached to contact records, speeding up follow-up actions and reducing manual workload

### 4. Automated Contact Categorization

A technology company tracks frequency of product issues and competitor mentions:
- Custom categories tag contacts with relevant terms
- Aggregated analytics provide trend reports for product and competitive intelligence

### 5. Enhanced Search and Reporting

A service manager investigates negative customer outcomes:
- Filters contacts by sentiment score and specific keywords
- Reviews transcripts and analytics to identify root causes and training needs

### Customer Testimonial

Neo Financial, a leading fintech company, reports a 10% reduction in hold times and a 20% decrease in customer holds after implementing Contact Lens. Automated post-contact summaries save agents 90 seconds per interaction and streamline complaint handling, saving leadership 40 hours per month.

## Best Practices and Considerations

- Always verify redacted transcripts for accuracy, especially with sensitive PII
- Automated redaction does not guarantee regulatory compliance; enforce additional controls as needed
- Ensure analytics blocks are present in all contact flows, including transfers, for comprehensive coverage
- Set up keyword-based real-time alerts to address urgent customer experience or compliance risks promptly
- Export and analyze detailed analytics data in Amazon S3 with Amazon QuickSight or custom ML models via Amazon SageMaker
- Select appropriate languages for highest accuracy; use dynamic language detection for multilingual environments
- Restrict access to unredacted data to authorized personnel only, in line with organizational security policies

## Frequently Asked Questions

<strong>How is Contact Lens for Amazon Connect billed?</strong>Billed per analyzed minute/message. Both real-time and post-call analytics are metered.

<strong>Which languages are supported?</strong>See the Supported Languages for Contact Lens documentation.

<strong>Does Contact Lens analyze all interactions?</strong>Yes, if enabled in relevant flows, all contacts are analyzed.

<strong>Can sentiment analysis be disabled?</strong>Yes, it can be deselected in the analytics block.

<strong>Where are analytics results accessible?</strong>Via the Amazon Connect Console (Contact Details, Contact Search), APIs, and as files in Amazon S3.

<strong>Is Contact Lens the same as Conversational Analytics?</strong>The Contact Lens feature set is now part of Amazon Connect's conversational analytics suite.

## Terminology Reference

| Term | Definition |
|------|------------|
| <strong>Contact Lens for Amazon Connect</strong>| ML-powered call and chat analytics native to Amazon Connect |
| <strong>Conversational Analytics</strong>| Suite including transcription, sentiment, redaction, categorization |
| <strong>Sentiment Score</strong>| Numeric indication of positivity/negativity in conversation turns |
| <strong>Set Recording and Analytics Behavior</strong>| Contact flow block enabling analytics in Amazon Connect |
| <strong>Redaction</strong>| Detection and masking/removal of PII in transcripts and audio |
| <strong>PII</strong>| Personally Identifiable Information (names, addresses, SSNs) |
| <strong>After Contact Work (ACW)</strong>| Agent post-interaction documentation and follow-up |
| <strong>Contact Flow</strong>| Logic/routing process for handling contacts in Amazon Connect |

## References


1. Amazon. (n.d.). Contact Lens Admin Guide. Amazon Connect Documentation.

2. Amazon. (n.d.). Enable Conversational Analytics. Amazon Connect Documentation.

3. Amazon. (n.d.). Analyze Conversations. Amazon Connect Documentation.

4. Amazon. (n.d.). Conversational Analytics Overview. AWS Connect.

5. Amazon. (n.d.). Contact Lens for Amazon Connect GA. AWS Blog.

6. Amazon. (n.d.). Pricing. Amazon Connect.

7. Amazon. (n.d.). Supported Languages. Amazon Connect Documentation.

8. Amazon. (n.d.). Data Privacy FAQs. AWS.

9. Amazon. (n.d.). AI Services Opt-out Policies. AWS Organizations Documentation.

10. Amazon. (n.d.). Set Recording and Analytics Behavior. Amazon Connect Documentation.

11. Amazon. (n.d.). Sensitive Data Redaction. Amazon Connect Documentation.

12. Amazon. (n.d.). Sentiment Scores Guide. Amazon Connect Documentation.

13. Amazon. (n.d.). Real-time Alerts Guide. Amazon Connect Documentation.

14. Amazon. (n.d.). Example Output Locations. Amazon Connect Documentation.

15. Amazon. (n.d.). Contact Analysis Segment Streams. Amazon Connect Documentation.

16. Amazon. (n.d.). Contact Lens API. Amazon Connect Documentation.

17. Amazon. (n.d.). Contact Search. Amazon Connect Documentation.

18. Amazon. (n.d.). Agent Workspace. Amazon Connect Documentation.

19. Amazon. (n.d.). Wisdom. Amazon Connect.

20. Amazon QuickSight. Business Intelligence Tool. URL: https://aws.amazon.com/quicksight/

21. Amazon SageMaker. Machine Learning Platform. URL: https://aws.amazon.com/sagemaker/

22. Amazon Connect Streams API. Open Source Streaming Library. URL: https://github.com/aws/amazon-connect-streams

23. Amazon. (n.d.). Contact Lens for Amazon Connect Overview. YouTube Video.

24. Amazon. (n.d.). Contact Center Case Studies. AWS Connect.
