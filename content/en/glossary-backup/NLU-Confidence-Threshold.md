---
title: "NLU Confidence Threshold"
translationKey: "nlu-confidence-threshold"
description: "The NLU confidence threshold is the minimum confidence score an NLU engine requires to trigger a specific intent for a user’s utterance. It's central to conversational AI."
keywords: ["NLU confidence threshold", "natural language understanding", "confidence scores", "chatbot", "intent classification"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## Definition

<strong>NLU Confidence Threshold:</strong>The NLU (Natural Language Understanding) confidence threshold is the minimum confidence score an NLU engine requires to trigger a specific intent for a user’s utterance. If the top intent’s confidence score is below this threshold, the NLU typically triggers fallback logic—such as asking the user to rephrase, confirming the intent, or routing to a human agent. The threshold is tunable (usually 0.0–1.0), and is central to how conversational AI systems interpret input and manage uncertainty.

## 1. What is an NLU Confidence Score?

When an NLU model processes a user utterance, it predicts the most likely intent and assigns a confidence score to each candidate. This score is a scalar (typically 0–1) reflecting how strongly the model believes the input matches a particular intent.

<strong>Example:</strong>A user types “I forgot my password.” The NLU model might evaluate:
- `ResetPassword` — 0.92
- `ChangeEmail` — 0.12
- `AccountLockout` — 0.08

The top intent, `ResetPassword`, has a confidence score of 0.92.

<strong>Key Point:</strong>The confidence score expresses the model’s internal certainty about its prediction. It is not a calibrated probability, but rather a comparative value for choosing between intents.
## 2. Distinction: Confidence Score vs. Statistical Probability

<strong>Confidence Score:</strong>- An internal metric from the NLU engine, not a true probability.
- Not guaranteed to be calibrated or to sum to 1 across all intents.
- Indicates relative certainty, not absolute likelihood.

<strong>Statistical Confidence/Probability:</strong>- In statistics, a confidence interval (e.g., 95%) defines the range for a result.
- Statistical probability is mathematically calibrated; NLU confidence scores are not.

<strong>Caution:</strong>Do not interpret a confidence score of 0.9 as a 90% chance of correctness. Treat it as “the model is much more certain about this intent than others right now.”
## 3. Role of Confidence Threshold in Chatbot Workflows

The confidence threshold acts as a gate in conversational AI decision logic. It determines what happens if the model is not confident enough in its classification.

### Typical Workflow

1. <strong>NLU Model Processes Input:</strong>The model assigns scores to all candidate intents.

2. <strong>Compare to Threshold:</strong>If the top intent’s score ≥ threshold, proceed with that intent.  
   If not, trigger fallback logic.

3. <strong>Fallback Logic Examples:</strong>- Ask the user to confirm the detected intent.
   - Request the user to rephrase.
   - Route to a human agent.
   - Trigger a fallback intent (e.g., `AMAZON.FallbackIntent` in Amazon Lex).

<strong>Diagram (Described):</strong>User Input → NLU Model → [Is Top Confidence ≥ Threshold?] → (Yes: Proceed with Intent) / (No: Fallback/Confirmation)
## 4. Types of Confidence Thresholds

NLU systems can implement several thresholds for different behaviors:

- <strong>Confirmation Threshold:</strong>If the top intent’s confidence is below this (but above rejection), the bot asks the user to confirm, e.g., “Did you mean to reset your password?”

- <strong>Rejection Threshold:</strong>If the confidence is below this value, the bot triggers fallback, e.g., “I didn’t understand that. Could you rephrase?”

- <strong>Ambiguity Threshold (Optional):</strong>If top two intents have close scores, the bot may prompt the user to choose.

<strong>Example Table:</strong>| Threshold Type | Confidence Range | Bot Action           |
|---------------|------------------|----------------------|
| Rejection     | < 0.2            | Fallback/Reject      |
| Confirmation  | 0.2 – 0.4        | Ask for confirmation |
| Acceptance    | > 0.4            | Proceed with intent  |
## 5. How Confidence Thresholds Are Used

<strong>Operational Usage:</strong>- <strong>Intent Filtering:</strong>Intents below the threshold are not considered valid.
- <strong>Fallback Routing:</strong>If no intent exceeds the threshold, fallback/default intent is triggered.
- <strong>User Experience Control:</strong>Thresholds balance strictness (avoiding errors) and user convenience (minimizing unnecessary prompts).

<strong>Example (Amazon Lex):</strong>If all intent scores are below the threshold, Lex triggers `AMAZON.FallbackIntent` and prompts the user to clarify ([docs](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)).

## 6. Selecting and Tuning Confidence Thresholds

### Step-by-Step Process

1. <strong>Gather Annotated Test Data:</strong>Use a dataset of real-world user utterances with known intent labels.

2. <strong>Run Model Predictions:</strong>For each utterance, get the model’s intent confidence scores.

3. <strong>Evaluate at Multiple Thresholds:</strong>For thresholds (e.g., 0.0–1.0 in 0.05 increments), record:
   - Correct acceptances (true positives)
   - Incorrect acceptances (false positives)
   - Correct rejections (true negatives)
   - Incorrect rejections (false negatives)

4. <strong>Plot ROC Curve:</strong>Receiver Operating Characteristic (ROC) curve plots true positive rate vs. false positive rate for different thresholds.

5. <strong>Calculate F1 Score:</strong>F1 combines precision and recall into one metric, especially useful for imbalanced datasets.

6. <strong>Select Threshold(s):</strong>Choose threshold(s) that balance:
   - User friction (too many confirmations)
   - Accuracy (minimizing misclassifications)
   - Business risk (cost of errors vs. interruptions)

<strong>Tip:</strong>The criticality of errors can justify higher or lower thresholds. In regulated or high-risk domains, favor higher thresholds and confirmations.
## 7. Technical Evaluation: Metrics and Tools

<strong>Metrics:</strong>- <strong>Precision:</strong>Proportion of accepted intents that are correct.
- <strong>Recall:</strong>Proportion of correct intents that are accepted.
- <strong>F1 Score:</strong>Harmonic mean of precision and recall.

<strong>Visualization:</strong>- <strong>ROC Curve:</strong>For binary intent classification.
- <strong>Custom Plots:</strong>For multi-class systems, plot correct/incorrect acceptances and rejections per threshold.

<strong>Example Graph (Described):</strong>Line graphs showing:
- Correct Accept (true positive)
- False Accept (false positive)
- Correct Reject (true negative)
- False Reject (false negative)
## 8. Variations Across NLU Engines

Different NLU engines have unique approaches to confidence scores and thresholds:

- <strong>Amazon Lex:</strong>Returns scores per intent. Lets you set a custom threshold per language. Fallback is triggered if all scores are below threshold. [Amazon Lex docs](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

- <strong>Genesys:</strong>Default threshold is 0.4 (40%). If the top intent is below threshold, fallback/None intent is used.
  [Genesys best practices](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)

- <strong>ServiceNow:</strong>Confidence thresholds determine which intent is triggered. Upgrades to the model may cause score distributions to shift, requiring threshold review.
  [ServiceNow Community Q&A](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

- <strong>Voiceflow:</strong>Recommends dataset balance and real-world testing for thresholds.
  [Voiceflow NLU design principles](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)

<strong>Caution:</strong>Thresholds are not portable across engines. Each NLU's scoring is unique and may change over time.

## 9. Ongoing Monitoring and Adjustment

<strong>Why Continuous Tuning Is Necessary:</strong>- <strong>Model Updates:</strong>Retraining or upgrading NLU can shift score distributions.
- <strong>Dataset Drift:</strong>User language and patterns evolve, affecting threshold effectiveness.
- <strong>Engine Changes:</strong>Vendor upgrades may alter optimal thresholds.

<strong>Best Practices:</strong>- Periodically re-evaluate thresholds with fresh annotated data.
- Monitor metrics (precision, recall, F1) in production.
- Adjust thresholds in response to performance changes or business feedback.
- Test thresholds after any NLU engine change, even if data/model are unchanged.
## 10. Practical Examples and Use Cases

### Example 1: Banking Chatbot with Overlapping Intents

- <strong>Scenario:</strong>“Check balance” and “Manage credit card” both have utterances like “What’s my credit card balance?”
- <strong>Issue:</strong>High utterance overlap lowers confidence scores.
- <strong>Solution:</strong>Refine utterances to minimize overlap and adjust thresholds after retraining.

### Example 2: Contact Center Virtual Agent

- <strong>Scenario:</strong>NLU returns multiple close-scoring intents for “error.”
- <strong>Observed:</strong>“SearchKnowledgeBase” and “ProvideVirtualAgentFeedback” return 85%; “RaiseIncident” returns 70%.
- <strong>Analysis:</strong>Scoring mechanism may favor certain patterns. Adjust threshold and improve training data.

### Example 3: Amazon Lex Fallback

- <strong>Scenario:</strong>User: “I need help with my bill.”
- <strong>NLU Output:</strong>- “BillingHelp” — 0.61
  - “AccountHelp” — 0.58
- <strong>Threshold:</strong>Set at 0.65.
- <strong>Result:</strong>Both below threshold; Lex triggers `AMAZON.FallbackIntent`.
## 11. Common Pitfalls and Best Practices

### Pitfalls

- <strong>Overly High Thresholds:</strong>Excessive fallback/confirmation prompts, poor UX.
- <strong>Overly Low Thresholds:</strong>Accepts incorrect intents, misrouted conversations.
- <strong>Assuming Threshold Portability:</strong>Thresholds for one engine/dataset won’t generalize.
- <strong>Ignoring Dataset Imbalance:</strong>Skewed training leads to biased scores.
- <strong>Not Monitoring in Production:</strong>Accuracy can drift unnoticed.

### Best Practices

- Use representative, annotated data for evaluation.
- Tune confirmation and rejection thresholds separately.
- Visualize performance across thresholds.
- Balance intent training data.
- Regularly retrain and re-evaluate after changes.
- Document rationale for chosen thresholds.

<strong>Tip:</strong>In high-risk domains (e.g., healthcare, finance), set conservative thresholds and favor confirmation.
## 12. Glossary of Related Terms

- <strong>Natural Language Understanding (NLU):</strong>AI for extracting intent/entities from input.
- <strong>Intent:</strong>The goal/task a user wants (e.g., “ResetPassword”).
- <strong>Utterance:</strong>User’s input phrase.
- <strong>Confidence Score:</strong>NLU’s estimate of intent match.
- <strong>Fallback:</strong>Response when no intent is confidently matched.
- <strong>ROC Curve:</strong>Graph of true positive vs. false positive at thresholds.
- <strong>F1 Score:</strong>Harmonic mean of precision and recall.
- <strong>False Positive:</strong>Model accepts an incorrect intent.
- <strong>False Negative:</strong>Model rejects a correct intent.
- <strong>Intent Overlap:</strong>Similar utterances across intents, reducing confidence.

## 13. References and Further Reading

- [Amazon Lex: Using intent confidence scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)
- [Genesys: Best practices to build and test your natural language understanding](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Genesys: Set bot confidence thresholds](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)
- [Voiceflow: 5 principles for NLU design](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)
- [ServiceNow Community Q&A on NLU Confidence Threshold](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

<strong>Related Keywords:</strong>natural language understanding nlu, confidence thresholds, nlu confidence, machine learning, confidence scores, intents utterances, intent confidence, setting confidence, confidence score threshold, contact center, false positives, confidence interval, threshold set, affect confidence, higher confidence, intents entities, virtual agent, intent user, knowledge base, example intent

For implementation guides, platform details, and up-to-date best practices, consult the references above and your NLU provider’s documentation.

<strong>This page cites and expands upon:</strong>- [Amazon Lex Documentation](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)
- [Genesys Resource Center](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Genesys Blog](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)
- [Voiceflow NLU Design](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)
- [ServiceNow Community Q&A](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

If you want further detail, code samples, or hands-on configuration guides for a specific NLU platform, refer to the linked documentation and community articles above.
