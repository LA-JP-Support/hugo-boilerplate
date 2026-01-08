---
title: "Contact Lens for Amazon Connect"
date: 2025-12-17
translationKey: "contact-lens-for-amazon-connect"
description: "Contact Lens for Amazon Connect is an ML-driven conversational analytics and compliance suite for Amazon Connect. It offers transcription, sentiment analysis, data redaction, and more."
keywords: ["Contact Lens for Amazon Connect", "Amazon Connect", "conversational analytics", "sentiment analysis", "sensitive data redaction"]
category: "AI-Driven Contact Center Analytics"
type: "glossary"
draft: false
---

## What is Contact Lens for Amazon Connect?

Contact Lens for Amazon Connect delivers a comprehensive suite of machine learning (ML) analytics to contact centers. Embedded in Amazon Connect, it automates transcription, sentiment analysis, issue detection, sensitive data redaction, and contact categorization for both voice and chat channels. The service leverages natural language processing (NLP) and advanced speech analytics to provide actionable insights into customer-agent and customer-bot conversations.

Contact Lens is fully accessible within the Amazon Connect console—no third-party integration required—and supports granular configuration at the contact flow level. It enables compliance-focused organizations to mask sensitive data and audit interactions for regulatory adherence, while supervisors and analysts gain powerful search, reporting, and workflow automation tools.

**Key Attributes:**- Native to Amazon Connect, available through a simple console toggle.
- Supports voice and chat, with real-time and post-call/post-chat analytics.
- Automated redaction of PII (personally identifiable information) in transcripts and audio.
- Actionable sentiment scoring, issue detection, and customizable categorization.
- Secure, compliant, and easily integrated with AWS data lakes and BI tools.

Learn more in the [Amazon Connect Contact Lens Admin Guide](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens.html).

## How Contact Lens for Amazon Connect Is Used

Organizations use Contact Lens to automate and supercharge quality assurance, compliance monitoring, operational analytics, and customer experience improvement. It enables:

- **Automated QA and Compliance:**Reviews 100% of interactions, flags compliance issues, and redacts sensitive data automatically.
- **Customer Experience Monitoring:**Tracks customer sentiment and identifies pain points in real time and historically.
- **Workforce Optimization:**Reduces manual after contact work (ACW) via automated summaries and highlights coaching opportunities.
- **Actionable Insights:**Surfaces trends, emerging issues, and process bottlenecks using advanced metrics and customizable dashboards.

Contact Lens is turned on at the flow level in Amazon Connect via the “Set Recording and Analytics Behavior” block, allowing organizations to tailor analytics to specific interaction types or scenarios. See [Analyze Conversations Using Conversational Analytics](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html) for workflow details.

## Key Features of Contact Lens for Amazon Connect

### 1. Automated Transcription and Indexing

- **Functionality:**All voice and chat interactions are automatically transcribed using AWS’s advanced speech-to-text and NLP engines.
- **Searchability:**Transcripts are indexed, enabling full-text search by keyword, phrase, or sentiment across all historical interactions.
- **Supervisor Benefits:**QA and compliance leads can locate relevant calls instantly, eliminating manual audio review.
- **Documentation:**[Contact Lens Transcription](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

### 2. Sentiment Analysis

- **How It Works:**Each customer and agent utterance is scored for sentiment (positive, negative, or neutral). Scores are aggregated and visualized as sentiment trends throughout the interaction.
- **Use Cases:**Supervisors filter for negative sentiment contacts, identify at-risk customers, and monitor agent performance objectively.
- **Sample Output:**Sentiment graphs are visible in the contact details page (see [Sentiment Scores Guide](https://docs.aws.amazon.com/connect/latest/adminguide/sentiment-scores.html)).
- **Documentation:**[Sentiment Analysis in Contact Lens](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

### 3. Issue Detection and Non-Talk Time Analytics

- **Capabilities:**Identifies call drivers, interruptions, long silences, hold durations, and overlapping speech.
- **Value:**Pinpoints root causes, agent or bot training opportunities, and workflow bottlenecks.
- **Visualization:**Graphs display talk time split by agent/customer, silence, and hold time.
- **Documentation:**[Talk Time and Non-Talk Analytics](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

### 4. Automated Contact Categorization

- **How It Works:**Lets users define rules for tagging interactions based on keywords, phrases, or compliance criteria. E.g., script adherence, competitor mentions, escalation triggers.
- **Automated Reporting:**Enables dynamic aggregation and reporting for QA, compliance, escalation, and business outcomes.
- **Documentation:**[Contact Categorization](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

### 5. Sensitive Data Redaction

- **PII Redaction:**Automatically detects and redacts PII such as names, addresses, credit card numbers, and social security numbers from both transcript and audio.
- **Compliance:**Supports PCI DSS, GDPR, and other data privacy standards by masking sensitive data in stored records and supervisor/agent views.
- **Configuration:**Choose which PII types to redact and whether to output only redacted or both redacted/original files.
- **Documentation:**[Sensitive Data Redaction](https://docs.aws.amazon.com/connect/latest/adminguide/sensitive-data-redaction.html)

### 6. Real-Time and Post-Call Analytics

- **Real-Time Analytics:**- Provides live metrics, sentiment tracking, and configurable alerts during active calls or chats.
  - Enables supervisors to intervene or coach agents based on negative sentiment or key phrase detection.
  - [Real-Time Alerts Guide](https://docs.aws.amazon.com/connect/latest/adminguide/add-rules-for-alerts.html)

- **Post-Call Analytics:**- Delivers detailed post-interaction summaries, insights, and categorization.
  - Supports trend analysis, coaching, and root cause analysis.
  - [Post-Call Analytics Documentation](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

### 7. Customizable Workflows and Output

- **Language Support:**- Supports multiple languages for transcription, sentiment, and redaction.
  - Language can be set per flow or dynamically via Lambda/contact attributes.
  - [Supported Languages List](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html)

- **Data Export & Integration:**- Detailed analytics, transcripts, and metadata are exportable to Amazon S3.
  - Integrates with BI tools (e.g., [Amazon QuickSight](https://aws.amazon.com/quicksight/), Tableau) and custom ML workflows (e.g., [Amazon SageMaker](https://aws.amazon.com/sagemaker/)).
  - [Output Locations](https://docs.aws.amazon.com/connect/latest/adminguide/example-contact-lens-output-locations.html)

## Advanced Configuration and Deployment

### Enabling Contact Lens

1. Access the [Amazon Connect Console](https://console.aws.amazon.com/connect/).
2. Navigate to your instance, go to the *Analytics Tools* section, and enable Contact Lens.
3. In the contact flow designer, insert a **Set Recording and Analytics Behavior**block where analytics is needed.
4. Set recording to *Agent and Customer* for voice analytics.
5. Enable Contact Lens analytics, selecting real-time, post-call, or both.
6. Configure language, redaction, and analytics settings as needed.
7. Save and deploy the flow.
8. Repeat for any transfer or specialized flows ([Set Recording and Analytics Guide](https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-behavior.html)).

**Note:**Recording both agent and customer is mandatory for full voice analytics. For chat analytics, ensure chat recording is enabled.

### Redaction Parameter Options

- **Scope:**Redact all supported PII or only selected entities (credit card, address, etc.).
- **Output Handling:**Choose between storing only redacted files or both redacted and original versions.
- **Replacement:**Specify placeholder text (e.g., “[PII]”) for redacted sections.
- **Important:**Automated redaction is not HIPAA-certified; always verify accuracy ([Redaction Documentation](https://docs.aws.amazon.com/connect/latest/adminguide/sensitive-data-redaction.html)).

### Sentiment Analysis Options

- Enabled by default when analytics is active and the language is supported.
- Can be disabled in the analytics block if not required.
- [Sentiment Analysis Customization](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

### Dynamic Configuration

- Use *Set contact attributes* blocks or AWS Lambda to dynamically set analytics parameters (language, redaction, etc.) per contact.
- [Dynamic Configuration Guide](https://docs.aws.amazon.com/connect/latest/adminguide/enable-analytics.html)

## Example Use Cases

### 1. Quality Assurance and Compliance

A financial services provider ensures script compliance and data privacy:
- Automated transcription enables instant search for required script phrases.
- Credit card data is redacted from transcripts and audio.
- Calls missing compliance phrases are flagged for supervisor review.

### 2. Proactive Customer Experience Management

A retailer uses real-time analytics to intervene during negative interactions:
- Supervisors receive alerts when customer sentiment turns negative or critical keywords are detected.
- Supervisors can join live calls or send guidance to agents in real time.

### 3. Reducing After Contact Work (ACW)

An e-commerce company automates post-call documentation:
- Contact Lens generates post-call summaries and highlights.
- These are automatically attached to contact records, speeding up follow-up actions and reducing manual workload.

### 4. Automated Contact Categorization

A technology company tracks frequency of product issues and competitor mentions:
- Custom categories tag contacts with relevant terms.
- Aggregated analytics provide trend reports for product and competitive intelligence.

### 5. Enhanced Search and Reporting

A service manager investigates negative customer outcomes:
- Filters contacts by sentiment score and specific keywords.
- Reviews transcripts and analytics to identify root causes and training needs.

### Customer Testimonial

Neo Financial, a leading fintech company, reports a 10% reduction in hold times and a 20% decrease in customer holds after implementing Contact Lens. Automated post-contact summaries save agents 90 seconds per interaction and streamline complaint handling, saving leadership 40 hours per month ([Amazon Connect Conversational Analytics Customer Stories](https://aws.amazon.com/connect/conversational-analytics/)).

## Example: Full Contact Center Transcript Analysis Workflow

1. Customer initiates a support call regarding billing.
2. Contact Lens transcribes the call in real time, analyzes sentiment, and detects compliance issues.
3. Agent omits the required greeting; the supervisor receives an immediate alert due to negative sentiment and script deviation.
4. Payment details are automatically redacted from transcript and audio.
5. Post-call, a summary and categorization (e.g., “Billing Issue,” “Negative Sentiment”) are attached to the contact record.
6. Management reviews analytics dashboards for compliance gaps and operational trends.

Visual examples are available in AWS documentation:
- [Sample Contact Detail Pages](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)

## Best Practices and Considerations

- Always verify redacted transcripts for accuracy, especially with sensitive PII.
- Automated redaction does not guarantee regulatory compliance; enforce additional controls as needed.
- Ensure analytics blocks are present in all contact flows, including transfers, for comprehensive coverage.
- Set up keyword-based real-time alerts to address urgent customer experience or compliance risks promptly.
- Export and analyze detailed analytics data in Amazon S3 with [Amazon QuickSight](https://aws.amazon.com/quicksight/) or custom ML models via [Amazon SageMaker](https://aws.amazon.com/sagemaker/).
- Select appropriate languages for highest accuracy; use dynamic language detection for multilingual environments.
- Restrict access to unredacted data to authorized personnel only, in line with organizational security policies.
- Refer to [Amazon Connect Pricing](https://aws.amazon.com/connect/pricing/) for billing details.

## Frequently Asked Questions

**How is Contact Lens for Amazon Connect billed?**Billed per analyzed minute/message. Both real-time and post-call analytics are metered. See [Amazon Connect Pricing](https://aws.amazon.com/connect/pricing/).

**Which languages are supported?**See the [Supported Languages for Contact Lens](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html).

**Does Contact Lens analyze all interactions?**Yes, if enabled in relevant flows, all contacts are analyzed.

**Can sentiment analysis be disabled?**Yes, it can be deselected in the analytics block.

**Where are analytics results accessible?**Via the Amazon Connect Console (Contact Details, Contact Search), APIs, and as files in Amazon S3 ([Contact Search Guide](https://docs.aws.amazon.com/connect/latest/adminguide/contact-search.html)).

**Is Contact Lens the same as Conversational Analytics?**The Contact Lens feature set is now part of Amazon Connect’s conversational analytics suite ([Product Page](https://aws.amazon.com/connect/conversational-analytics/)).

## Terminology Reference

| Term                               | Definition                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Contact Lens for Amazon Connect     | ML-powered call and chat analytics native to Amazon Connect                               |
| Conversational Analytics            | Suite including transcription, sentiment, redaction, categorization, and more             |
| Sentiment Score                     | Numeric indication of positivity/negativity in conversation turns                         |
| Set Recording and Analytics Behavior| Contact flow block enabling analytics and recording in Amazon Connect                     |
| Redaction                           | Detection and masking/removal of PII in transcripts and audio                             |
| PII (Personally Identifiable Info)  | Sensitive information such as names, addresses, credit cards, SSNs                        |
| After Contact Work (ACW)            | Agent post-interaction documentation and follow-up                                        |
| Contact Flow                        | Logic/routing process for handling contacts in Amazon Connect                             |
| Quick Connect                       | Predefined transfer target within Amazon Connect                                          |

## Related Keywords

- contact lens amazon connect
- amazon connect contact lens
- sensitive data redaction
- conversational analytics amazon connect
- set recording analytics behavior
- sentiment analysis
- speech analytics
- customer sentiment
- enable contact lens

## References

1. [Amazon Connect Contact Lens – Admin Guide](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens.html)
2. [Enable Conversational Analytics in Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/enable-analytics.html)
3. [Analyze Conversations Using Conversational Analytics](https://docs.aws.amazon.com/connect/latest/adminguide/analyze-conversations.html)
4. [Amazon Connect Conversational Analytics Overview](https://aws.amazon.com/connect/conversational-analytics/)
5. [Machine Learning-Based Customer Insights with Contact Lens for Amazon Connect – AWS Blog](https://aws.amazon.com/blogs/contact-center/contact-lens-for-amazon-connect-ga/)
6. [Amazon Connect Pricing](https://aws.amazon.com/connect/pricing/)
7. [Languages Supported by Amazon Connect Analytics](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html)
8. [Data Privacy FAQs](https://aws.amazon.com/compliance/data-privacy-faq/)
9. [AI Services Opt-out Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html)
10. [Amazon Connect Admin Guide: Set Recording and Analytics Behavior](https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-behavior.html)
11. [Amazon Connect Admin Guide: Sensitive Data Redaction](https://docs.aws.amazon.com/connect/latest/adminguide/sensitive-data-redaction.html)
12. [Example Contact Lens Output Locations](https://docs.aws.amazon.com/connect/latest/adminguide/example-contact-lens-output-locations.html)
13. [Amazon Kinesis Data Streams for Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/contact-analysis-segment-streams.html)
14. [Amazon Connect Real-time APIs](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-api.html)
15. [Amazon Connect Contact Search](https://docs.aws.amazon.com/connect/latest/adminguide/contact-search.html)
16. [Amazon Connect Agent Workspace](https://docs.aws.amazon.com/connect/latest/adminguide/agent-workspace.html)
17. [Amazon Connect Wisdom](https://aws.amazon.com/connect/wisdom/)
18. [Amazon QuickSight](https://aws.amazon.com/quicksight/)
19. [Amazon SageMaker](https://aws.amazon.com/sagemaker/)
20. [Amazon Connect Streams API](https://github.com/aws/amazon-connect-streams)

## Additional Resources

- [Contact Lens for Amazon Connect – YouTube Overview](https://www.youtube.com/watch?v=HrGgI0bUuC8)
- [AWS Contact Center Case Studies](https://aws.amazon.com/connect/customers/)

This glossary provides a deeply detailed, technically robust foundation for understanding and deploying Contact Lens for Amazon Connect in enterprise contact center environments. For further exploration, follow the documentation links and AWS product pages provided above.

