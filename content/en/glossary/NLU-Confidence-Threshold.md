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

**Example:**A user types "I forgot my password." The NLU model might evaluate:
- ResetPassword: 0.92
- ChangeEmail: 0.12
- AccountLockout: 0.08

The top intent, ResetPassword, has a confidence score of 0.92.

### Confidence Score vs. Statistical Probability

**Confidence Score:**- Internal metric from NLU engine, not true probability
- Not guaranteed to be calibrated or sum to 1 across all intents
- Indicates relative certainty, not absolute likelihood

**Statistical Probability:**- In statistics, confidence interval (e.g., 95%) defines range for result
- Statistical probability is mathematically calibrated; NLU confidence scores are not

**Important:**Do not interpret confidence score of 0.9 as 90% chance of correctness. Treat it as "the model is much more certain about this intent than others right now."

## Role in Chatbot Workflows

The confidence threshold acts as gate in conversational AI decision logic. It determines what happens if model is not confident enough in its classification.

### Typical Workflow

**NLU Model Processes Input:**Model assigns scores to all candidate intents.**Compare to Threshold:**If top intent's score ≥ threshold, proceed with that intent. If not, trigger fallback logic.**Fallback Logic Examples:**- Ask user to confirm detected intent
- Request user to rephrase
- Route to human agent
- Trigger fallback intent (e.g., AMAZON.FallbackIntent in Amazon Lex)

## Types of Confidence Thresholds

NLU systems can implement several thresholds for different behaviors:

**Confirmation Threshold:**If top intent's confidence is below this (but above rejection), bot asks user to confirm, e.g., "Did you mean to reset your password?"**Rejection Threshold:**If confidence is below this value, bot triggers fallback, e.g., "I didn't understand that. Could you rephrase?"**Ambiguity Threshold (Optional):**If top two intents have close scores, bot may prompt user to choose.

### Threshold Type Comparison

| Threshold Type | Confidence Range | Bot Action |
|---------------|------------------|------------|
| **Rejection**| < 0.2 | Fallback/Reject |
| **Confirmation**| 0.2 – 0.4 | Ask for confirmation |
| **Acceptance**| > 0.4 | Proceed with intent |

## Operational Usage

**Intent Filtering:**Intents below threshold are not considered valid.**Fallback Routing:**If no intent exceeds threshold, fallback/default intent is triggered.**User Experience Control:**Thresholds balance strictness (avoiding errors) and user convenience (minimizing unnecessary prompts).**Example (Amazon Lex):**If all intent scores are below threshold, Lex triggers AMAZON.FallbackIntent and prompts user to clarify.

## Selecting and Tuning Thresholds

### Step-by-Step Process

**Gather Annotated Test Data:**Use dataset of real-world user utterances with known intent labels.**Run Model Predictions:**For each utterance, get model's intent confidence scores.**Evaluate at Multiple Thresholds:**For thresholds (e.g., 0.0–1.0 in 0.05 increments), record:
- Correct acceptances (true positives)
- Incorrect acceptances (false positives)
- Correct rejections (true negatives)
- Incorrect rejections (false negatives)

**Plot ROC Curve:**Receiver Operating Characteristic (ROC) curve plots true positive rate vs. false positive rate for different thresholds.**Calculate F1 Score:**F1 combines precision and recall into one metric, especially useful for imbalanced datasets.**Select Threshold(s):**Choose threshold(s) that balance:
- User friction (too many confirmations)
- Accuracy (minimizing misclassifications)
- Business risk (cost of errors vs. interruptions)

**Important:**Criticality of errors can justify higher or lower thresholds. In regulated or high-risk domains, favor higher thresholds and confirmations.

## Evaluation Metrics

### Key Metrics

**Precision:**Proportion of accepted intents that are correct.**Recall:**Proportion of correct intents that are accepted.**F1 Score:**Harmonic mean of precision and recall.

### Visualization

**ROC Curve:**For binary intent classification.**Custom Plots:**For multi-class systems, plot correct/incorrect acceptances and rejections per threshold.**Example Metrics:**- Correct Accept (true positive)
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

**Important:**Thresholds are not portable across engines. Each NLU's scoring is unique and may change over time.

## Monitoring and Adjustment

### Why Continuous Tuning is Necessary

**Model Updates:**Retraining or upgrading NLU can shift score distributions.**Dataset Drift:**User language and patterns evolve, affecting threshold effectiveness.**Engine Changes:**Vendor upgrades may alter optimal thresholds.

### Best Practices

- Periodically re-evaluate thresholds with fresh annotated data
- Monitor metrics (precision, recall, F1) in production
- Adjust thresholds in response to performance changes or business feedback
- Test thresholds after any NLU engine change, even if data/model unchanged

## Practical Examples

### Banking Chatbot with Overlapping Intents

**Scenario:**"Check balance" and "Manage credit card" both have utterances like "What's my credit card balance?"**Issue:**High utterance overlap lowers confidence scores.**Solution:**Refine utterances to minimize overlap and adjust thresholds after retraining.

### Contact Center Virtual Agent

**Scenario:**NLU returns multiple close-scoring intents for "error."**Observed:**"SearchKnowledgeBase" and "ProvideVirtualAgentFeedback" return 85%; "RaiseIncident" returns 70%.**Analysis:**Scoring mechanism may favor certain patterns. Adjust threshold and improve training data.

### Amazon Lex Fallback

**Scenario:**User: "I need help with my bill."**NLU Output:**- "BillingHelp": 0.61
- "AccountHelp": 0.58

**Threshold:**Set at 0.65.**Result:**Both below threshold; Lex triggers AMAZON.FallbackIntent.

## Common Pitfalls

**Overly High Thresholds:**Excessive fallback/confirmation prompts, poor UX.**Overly Low Thresholds:**Accepts incorrect intents, misrouted conversations.**Assuming Threshold Portability:**Thresholds for one engine/dataset won't generalize.**Ignoring Dataset Imbalance:**Skewed training leads to biased scores.**Not Monitoring in Production:**Accuracy can drift unnoticed.

## Best Practices

- Use representative, annotated data for evaluation
- Tune confirmation and rejection thresholds separately
- Visualize performance across thresholds
- Balance intent training data
- Regularly retrain and re-evaluate after changes
- Document rationale for chosen thresholds

**Important:**In high-risk domains (e.g., healthcare, finance), set conservative thresholds and favor confirmation.

## Related Terminology

**Natural Language Understanding (NLU):**AI for extracting intent/entities from input.**Intent:**Goal/task user wants (e.g., "ResetPassword").**Utterance:**User's input phrase.**Confidence Score:**NLU's estimate of intent match.**Fallback:**Response when no intent is confidently matched.**ROC Curve:**Graph of true positive vs. false positive at thresholds.**F1 Score:**Harmonic mean of precision and recall.**False Positive:**Model accepts incorrect intent.**False Negative:**Model rejects correct intent.**Intent Overlap:**Similar utterances across intents, reducing confidence.

## References


1. Amazon Web Services. (n.d.). Amazon Lex: Using Intent Confidence Scores. AWS Documentation.

2. Genesys. (n.d.). Best Practices for Natural Language Understanding. Genesys Help Center.

3. Genesys. (n.d.). Set Bot Confidence Thresholds. Genesys Blog.

4. Voiceflow. (n.d.). 5 Principles for NLU Design. Voiceflow Pathways.

5. ServiceNow. (n.d.). NLU Confidence Threshold. ServiceNow Community Forum.
