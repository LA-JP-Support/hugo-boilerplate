---
title: "NLU Confidence Threshold"
translationKey: "nlu-confidence-threshold"
description: "A minimum confidence score that determines whether an AI chatbot understood a user's request correctly. If the score falls below this threshold, the system asks for clarification instead of making a wrong guess."
keywords: ["NLU confidence threshold", "natural language understanding", "confidence scores", "chatbot", "intent classification"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is NLU Confidence Threshold?

The NLU (Natural Language Understanding) confidence threshold is the minimum confidence score an NLU engine requires to trigger a specific intent for a user's utterance. If the top intent's confidence score is below this threshold, the NLU typically triggers fallback logic—such as asking the user to rephrase, confirming the intent, or routing to a human agent.

The threshold is tunable (usually 0.0–1.0) and is central to how conversational AI systems interpret input and manage uncertainty. This parameter directly impacts user experience by balancing accuracy (avoiding errors) with convenience (minimizing unnecessary confirmations).

## Understanding Confidence Scores

### What is a Confidence Score?

When an NLU model processes a user utterance, it predicts the most likely intent and assigns a confidence score to each candidate. This score is a scalar (typically 0–1) reflecting how strongly the model believes the input matches a particular intent.

<strong>Example:</strong>A user types "I forgot my password." The NLU model might evaluate:
- ResetPassword: 0.92
- ChangeEmail: 0.12
- AccountLockout: 0.08

The top intent, ResetPassword, has a confidence score of 0.92.

### Confidence Score vs. Statistical Probability

<strong>Confidence Score:</strong>- Internal metric from NLU engine, not true probability
- Not guaranteed to be calibrated or sum to 1 across all intents
- Indicates relative certainty, not absolute likelihood

<strong>Statistical Probability:</strong>- In statistics, confidence interval (e.g., 95%) defines range for result
- Statistical probability is mathematically calibrated; NLU confidence scores are not

<strong>Important:</strong>Do not interpret confidence score of 0.9 as 90% chance of correctness. Treat it as "the model is much more certain about this intent than others right now."

## Role in Chatbot Workflows

The confidence threshold acts as gate in conversational AI decision logic. It determines what happens if model is not confident enough in its classification.

### Typical Workflow

<strong>NLU Model Processes Input:</strong>Model assigns scores to all candidate intents.

<strong>Compare to Threshold:</strong>If top intent's score ≥ threshold, proceed with that intent. If not, trigger fallback logic.

<strong>Fallback Logic Examples:</strong>- Ask user to confirm detected intent
- Request user to rephrase
- Route to human agent
- Trigger fallback intent (e.g., AMAZON.FallbackIntent in Amazon Lex)

## Types of Confidence Thresholds

NLU systems can implement several thresholds for different behaviors:

<strong>Confirmation Threshold:</strong>If top intent's confidence is below this (but above rejection), bot asks user to confirm, e.g., "Did you mean to reset your password?"

<strong>Rejection Threshold:</strong>If confidence is below this value, bot triggers fallback, e.g., "I didn't understand that. Could you rephrase?"

<strong>Ambiguity Threshold (Optional):</strong>If top two intents have close scores, bot may prompt user to choose.

### Threshold Type Comparison

| Threshold Type | Confidence Range | Bot Action |
|---------------|------------------|------------|
| <strong>Rejection</strong>| < 0.2 | Fallback/Reject |
| <strong>Confirmation</strong>| 0.2 – 0.4 | Ask for confirmation |
| <strong>Acceptance</strong>| > 0.4 | Proceed with intent |

## Operational Usage

<strong>Intent Filtering:</strong>Intents below threshold are not considered valid.

<strong>Fallback Routing:</strong>If no intent exceeds threshold, fallback/default intent is triggered.

<strong>User Experience Control:</strong>Thresholds balance strictness (avoiding errors) and user convenience (minimizing unnecessary prompts).

<strong>Example (Amazon Lex):</strong>If all intent scores are below threshold, Lex triggers AMAZON.FallbackIntent and prompts user to clarify.

## Selecting and Tuning Thresholds

### Step-by-Step Process

<strong>Gather Annotated Test Data:</strong>Use dataset of real-world user utterances with known intent labels.

<strong>Run Model Predictions:</strong>For each utterance, get model's intent confidence scores.

<strong>Evaluate at Multiple Thresholds:</strong>For thresholds (e.g., 0.0–1.0 in 0.05 increments), record:
- Correct acceptances (true positives)
- Incorrect acceptances (false positives)
- Correct rejections (true negatives)
- Incorrect rejections (false negatives)

<strong>Plot ROC Curve:</strong>Receiver Operating Characteristic (ROC) curve plots true positive rate vs. false positive rate for different thresholds.

<strong>Calculate F1 Score:</strong>F1 combines precision and recall into one metric, especially useful for imbalanced datasets.

<strong>Select Threshold(s):</strong>Choose threshold(s) that balance:
- User friction (too many confirmations)
- Accuracy (minimizing misclassifications)
- Business risk (cost of errors vs. interruptions)

<strong>Important:</strong>Criticality of errors can justify higher or lower thresholds. In regulated or high-risk domains, favor higher thresholds and confirmations.

## Evaluation Metrics

### Key Metrics

<strong>Precision:</strong>Proportion of accepted intents that are correct.

<strong>Recall:</strong>Proportion of correct intents that are accepted.

<strong>F1 Score:</strong>Harmonic mean of precision and recall.

### Visualization

<strong>ROC Curve:</strong>For binary intent classification.

<strong>Custom Plots:</strong>For multi-class systems, plot correct/incorrect acceptances and rejections per threshold.

<strong>Example Metrics:</strong>- Correct Accept (true positive)
- False Accept (false positive)
- Correct Reject (true negative)
- False Reject (false negative)

## Platform-Specific Implementations

### Amazon Lex

Returns scores per intent. Lets you set custom threshold per language. Fallback is triggered if all scores are below threshold.

### Genesys

Default threshold is 0.4 (40%). If top intent is below threshold, fallback/None intent is used.

### ServiceNow

Confidence thresholds determine which intent is triggered. Upgrades to model may cause score distributions to shift, requiring threshold review.

### Voiceflow

Recommends dataset balance and real-world testing for thresholds.

<strong>Important:</strong>Thresholds are not portable across engines. Each NLU's scoring is unique and may change over time.

## Monitoring and Adjustment

### Why Continuous Tuning is Necessary

<strong>Model Updates:</strong>Retraining or upgrading NLU can shift score distributions.

<strong>Dataset Drift:</strong>User language and patterns evolve, affecting threshold effectiveness.

<strong>Engine Changes:</strong>Vendor upgrades may alter optimal thresholds.

### Best Practices

- Periodically re-evaluate thresholds with fresh annotated data
- Monitor metrics (precision, recall, F1) in production
- Adjust thresholds in response to performance changes or business feedback
- Test thresholds after any NLU engine change, even if data/model unchanged

## Practical Examples

### Banking Chatbot with Overlapping Intents

<strong>Scenario:</strong>"Check balance" and "Manage credit card" both have utterances like "What's my credit card balance?"

<strong>Issue:</strong>High utterance overlap lowers confidence scores.

<strong>Solution:</strong>Refine utterances to minimize overlap and adjust thresholds after retraining.

### Contact Center Virtual Agent

<strong>Scenario:</strong>NLU returns multiple close-scoring intents for "error."

<strong>Observed:</strong>"SearchKnowledgeBase" and "ProvideVirtualAgentFeedback" return 85%; "RaiseIncident" returns 70%.

<strong>Analysis:</strong>Scoring mechanism may favor certain patterns. Adjust threshold and improve training data.

### Amazon Lex Fallback

<strong>Scenario:</strong>User: "I need help with my bill."

<strong>NLU Output:</strong>- "BillingHelp": 0.61
- "AccountHelp": 0.58

<strong>Threshold:</strong>Set at 0.65.

<strong>Result:</strong>Both below threshold; Lex triggers AMAZON.FallbackIntent.

## Common Pitfalls

<strong>Overly High Thresholds:</strong>Excessive fallback/confirmation prompts, poor UX.

<strong>Overly Low Thresholds:</strong>Accepts incorrect intents, misrouted conversations.

<strong>Assuming Threshold Portability:</strong>Thresholds for one engine/dataset won't generalize.

<strong>Ignoring Dataset Imbalance:</strong>Skewed training leads to biased scores.

<strong>Not Monitoring in Production:</strong>Accuracy can drift unnoticed.

## Best Practices

- Use representative, annotated data for evaluation
- Tune confirmation and rejection thresholds separately
- Visualize performance across thresholds
- Balance intent training data
- Regularly retrain and re-evaluate after changes
- Document rationale for chosen thresholds

<strong>Important:</strong>In high-risk domains (e.g., healthcare, finance), set conservative thresholds and favor confirmation.

## Related Terminology

<strong>Natural Language Understanding (NLU):</strong>AI for extracting intent/entities from input.

<strong>Intent:</strong>Goal/task user wants (e.g., "ResetPassword").

<strong>Utterance:</strong>User's input phrase.

<strong>Confidence Score:</strong>NLU's estimate of intent match.

<strong>Fallback:</strong>Response when no intent is confidently matched.

<strong>ROC Curve:</strong>Graph of true positive vs. false positive at thresholds.

<strong>F1 Score:</strong>Harmonic mean of precision and recall.

<strong>False Positive:</strong>Model accepts incorrect intent.

<strong>False Negative:</strong>Model rejects correct intent.

<strong>Intent Overlap:</strong>Similar utterances across intents, reducing confidence.

## References


1. Amazon Web Services. (n.d.). Amazon Lex: Using Intent Confidence Scores. AWS Documentation.

2. Genesys. (n.d.). Best Practices for Natural Language Understanding. Genesys Help Center.

3. Genesys. (n.d.). Set Bot Confidence Thresholds. Genesys Blog.

4. Voiceflow. (n.d.). 5 Principles for NLU Design. Voiceflow Pathways.

5. ServiceNow. (n.d.). NLU Confidence Threshold. ServiceNow Community Forum.
