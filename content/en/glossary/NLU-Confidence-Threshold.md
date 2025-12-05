---
title: "NLU Confidence Threshold"
translationKey: "nlu-confidence-threshold"
description: "The NLU confidence threshold is the minimum confidence score an NLU engine requires to trigger a specific intent for a user’s utterance. It's central to conversational AI."
keywords: ["NLU confidence threshold", "natural language understanding", "confidence scores", "chatbot", "intent classification"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-03
draft: false
---
## Definition

**NLU Confidence Threshold:**  
The NLU (Natural Language Understanding) [confidence threshold](/en/glossary/confidence-threshold/) is the minimum confidence score an NLU engine requires to trigger a specific intent for a user’s [utterance](/en/glossary/utterance/). If the top intent’s confidence score is below this threshold, the NLU typically triggers fallback logic—such as asking the user to rephrase, confirming the intent, or routing to a human agent. The threshold is tunable (usually 0.0–1.0), and is central to how [conversational AI](/en/glossary/conversational-ai/) systems interpret input and manage uncertainty.

## 1. What is an NLU Confidence Score?

When an NLU model processes a user utterance, it predicts the most likely intent and assigns a confidence score to each candidate. This score is a scalar (typically 0–1) reflecting how strongly the model believes the input matches a particular intent.

**Example:**  
A user types “I forgot my password.” The NLU model might evaluate:
- `ResetPassword` — 0.92
- `ChangeEmail` — 0.12
- `AccountLockout` — 0.08

The top intent, `ResetPassword`, has a confidence score of 0.92.

**Key Point:**  
The confidence score expresses the model’s internal certainty about its prediction. It is not a calibrated probability, but rather a comparative value for choosing between intents.

**Further Reading:**  
- [Amazon Lex: Using intent confidence scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

## 2. Distinction: Confidence Score vs. Statistical Probability

**Confidence Score:**  
- An internal metric from the NLU engine, not a true probability.
- Not guaranteed to be calibrated or to sum to 1 across all intents.
- Indicates relative certainty, not absolute likelihood.

**Statistical Confidence/Probability:**  
- In statistics, a confidence interval (e.g., 95%) defines the range for a result.
- Statistical probability is mathematically calibrated; NLU confidence scores are not.

**Caution:**  
Do not interpret a confidence score of 0.9 as a 90% chance of correctness. Treat it as “the model is much more certain about this intent than others right now.”

**Reference:**  
- [Best practices to build and test your natural language understanding — Genesys](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)

## 3. Role of Confidence Threshold in Chatbot Workflows

The confidence threshold acts as a gate in conversational AI decision logic. It determines what happens if the model is not confident enough in its classification.

### Typical Workflow

1. **NLU Model Processes Input:**  
   The model assigns scores to all candidate intents.

2. **Compare to Threshold:**  
   If the top intent’s score ≥ threshold, proceed with that intent.  
   If not, trigger fallback logic.

3. **Fallback Logic Examples:**
   - Ask the user to confirm the detected intent.
   - Request the user to rephrase.
   - Route to a human agent.
   - Trigger a fallback intent (e.g., `AMAZON.FallbackIntent` in Amazon Lex).

**Diagram (Described):**  
User Input → NLU Model → [Is Top Confidence ≥ Threshold?] → (Yes: Proceed with Intent) / (No: Fallback/Confirmation)

**Reference:**  
- [Amazon Lex: Using intent confidence scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

## 4. Types of Confidence Thresholds

NLU systems can implement several thresholds for different behaviors:

- **Confirmation Threshold:**  
  If the top intent’s confidence is below this (but above rejection), the bot asks the user to confirm, e.g., “Did you mean to reset your password?”

- **Rejection Threshold:**  
  If the confidence is below this value, the bot triggers fallback, e.g., “I didn’t understand that. Could you rephrase?”

- **Ambiguity Threshold (Optional):**  
  If top two intents have close scores, the bot may prompt the user to choose.

**Example Table:**

| Threshold Type | Confidence Range | Bot Action           |
|---------------|------------------|----------------------|
| Rejection     | < 0.2            | Fallback/Reject      |
| Confirmation  | 0.2 – 0.4        | Ask for confirmation |
| Acceptance    | > 0.4            | Proceed with intent  |

**Reference:**  
- [Genesys: Set bot confidence thresholds](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)

## 5. How Confidence Thresholds Are Used

**Operational Usage:**
- **Intent Filtering:**  
  Intents below the threshold are not considered valid.
- **Fallback Routing:**  
  If no intent exceeds the threshold, fallback/default intent is triggered.
- **User Experience Control:**  
  Thresholds balance strictness (avoiding errors) and user convenience (minimizing unnecessary prompts).

**Example (Amazon Lex):**  
If all intent scores are below the threshold, Lex triggers `AMAZON.FallbackIntent` and prompts the user to clarify ([docs](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)).

## 6. Selecting and Tuning Confidence Thresholds

### Step-by-Step Process

1. **Gather Annotated Test Data:**  
   Use a dataset of real-world user utterances with known intent labels.

2. **Run Model Predictions:**  
   For each utterance, get the model’s intent confidence scores.

3. **Evaluate at Multiple Thresholds:**  
   For thresholds (e.g., 0.0–1.0 in 0.05 increments), record:
   - Correct acceptances (true positives)
   - Incorrect acceptances (false positives)
   - Correct rejections (true negatives)
   - Incorrect rejections (false negatives)

4. **Plot ROC Curve:**  
   Receiver Operating Characteristic (ROC) curve plots true positive rate vs. [false positive](/en/glossary/false-positive/) rate for different thresholds.

5. **Calculate F1 Score:**  
   F1 combines [precision and recall](/en/glossary/precision-and-recall/) into one metric, especially useful for imbalanced datasets.

6. **Select Threshold(s):**  
   Choose threshold(s) that balance:
   - User friction (too many confirmations)
   - Accuracy (minimizing misclassifications)
   - Business risk (cost of errors vs. interruptions)

**Tip:**  
The criticality of errors can justify higher or lower thresholds. In regulated or high-risk domains, favor higher thresholds and confirmations.

**Reference:**  
- [Genesys: Best practices to build and test your natural language understanding](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)

## 7. Technical Evaluation: Metrics and Tools

**Metrics:**
- **Precision:**  
  Proportion of accepted intents that are correct.
- **Recall:**  
  Proportion of correct intents that are accepted.
- **F1 Score:**  
  Harmonic mean of precision and recall.

**Visualization:**
- **ROC Curve:**  
  For binary intent classification.
- **Custom Plots:**  
  For multi-class systems, plot correct/incorrect acceptances and rejections per threshold.

**Example Graph (Described):**  
Line graphs showing:
- Correct Accept (true positive)
- False Accept (false positive)
- Correct Reject (true negative)
- False Reject ([false negative](/en/glossary/false-negative/))

**References:**  
- [Genesys: Set bot confidence thresholds](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)

## 8. Variations Across NLU Engines

Different NLU engines have unique approaches to confidence scores and thresholds:

- **Amazon Lex:**  
  Returns scores per intent. Lets you set a custom threshold per language. Fallback is triggered if all scores are below threshold. [Amazon Lex docs](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

- **Genesys:**  
  Default threshold is 0.4 (40%). If the top intent is below threshold, fallback/None intent is used.
  [Genesys best practices](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)

- **ServiceNow:**  
  Confidence thresholds determine which intent is triggered. Upgrades to the model may cause score distributions to shift, requiring threshold review.
  [ServiceNow Community Q&A](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

- **Voiceflow:**  
  Recommends dataset balance and real-world testing for thresholds.
  [Voiceflow NLU design principles](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)

**Caution:**  
Thresholds are not portable across engines. Each NLU's scoring is unique and may change over time.

## 9. Ongoing Monitoring and Adjustment

**Why Continuous Tuning Is Necessary:**
- **Model Updates:**  
  Retraining or upgrading NLU can shift score distributions.
- **Dataset Drift:**  
  User language and patterns evolve, affecting threshold effectiveness.
- **Engine Changes:**  
  Vendor upgrades may alter optimal thresholds.

**Best Practices:**
- Periodically re-evaluate thresholds with fresh annotated data.
- Monitor metrics (precision, recall, F1) in production.
- Adjust thresholds in response to performance changes or business feedback.
- Test thresholds after any NLU engine change, even if data/model are unchanged.

**References:**  
- [Genesys: Best practices to build and test your natural language understanding](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Amazon Lex: Using intent confidence scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

## 10. Practical Examples and Use Cases

### Example 1: Banking Chatbot with Overlapping Intents

- **Scenario:**  
  “Check balance” and “Manage credit card” both have utterances like “What’s my credit card balance?”
- **Issue:**  
  High utterance overlap lowers confidence scores.
- **Solution:**  
  Refine utterances to minimize overlap and adjust thresholds after retraining.

### Example 2: Contact Center Virtual Agent

- **Scenario:**  
  NLU returns multiple close-scoring intents for “error.”
- **Observed:**  
  “SearchKnowledgeBase” and “ProvideVirtualAgentFeedback” return 85%; “RaiseIncident” returns 70%.
- **Analysis:**  
  Scoring mechanism may favor certain patterns. Adjust threshold and improve training data.

### Example 3: Amazon Lex Fallback

- **Scenario:**  
  User: “I need help with my bill.”
- **NLU Output:**  
  - “BillingHelp” — 0.61
  - “AccountHelp” — 0.58
- **Threshold:**  
  Set at 0.65.
- **Result:**  
  Both below threshold; Lex triggers `AMAZON.FallbackIntent`.

**References:**  
- [Amazon Lex: Using intent confidence scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)

## 11. Common Pitfalls and Best Practices

### Pitfalls

- **Overly High Thresholds:**  
  Excessive fallback/confirmation prompts, poor UX.
- **Overly Low Thresholds:**  
  Accepts incorrect intents, misrouted conversations.
- **Assuming Threshold Portability:**  
  Thresholds for one engine/dataset won’t generalize.
- **Ignoring Dataset Imbalance:**  
  Skewed training leads to biased scores.
- **Not Monitoring in Production:**  
  Accuracy can drift unnoticed.

### Best Practices

- Use representative, annotated data for evaluation.
- Tune confirmation and rejection thresholds separately.
- Visualize performance across thresholds.
- Balance intent training data.
- Regularly retrain and re-evaluate after changes.
- Document rationale for chosen thresholds.

**Tip:**  
In high-risk domains (e.g., healthcare, finance), set conservative thresholds and favor confirmation.

**References:**  
- [Genesys: Best practices to build and test your natural language understanding](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)

## 12. Glossary of Related Terms

- **Natural Language Understanding (NLU):**  
  AI for extracting intent/entities from input.
- **Intent:**  
  The goal/task a user wants (e.g., “ResetPassword”).
- **Utterance:**  
  User’s input phrase.
- **Confidence Score:**  
  NLU’s estimate of intent match.
- **Fallback:**  
  Response when no intent is confidently matched.
- **ROC Curve:**  
  Graph of true positive vs. false positive at thresholds.
- **F1 Score:**  
  Harmonic mean of precision and recall.
- **False Positive:**  
  Model accepts an incorrect intent.
- **False Negative:**  
  Model rejects a correct intent.
- **Intent Overlap:**  
  Similar utterances across intents, reducing confidence.

## 13. References and Further Reading

- [Amazon Lex: Using intent confidence scores](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)
- [Genesys: Best practices to build and test your natural language understanding](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Genesys: Set bot confidence thresholds](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)
- [Voiceflow: 5 principles for NLU design](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)
- [ServiceNow Community Q&A on NLU Confidence Threshold](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

**Related Keywords:**  
natural language understanding nlu, confidence thresholds, nlu confidence, machine learning, confidence scores, intents utterances, intent confidence, setting confidence, confidence score threshold, contact center, false positives, confidence interval, threshold set, affect confidence, higher confidence, intents entities, virtual agent, intent user, knowledge base, example intent

For implementation guides, platform details, and up-to-date best practices, consult the references above and your NLU provider’s documentation.

**This page cites and expands upon:**

- [Amazon Lex Documentation](https://docs.aws.amazon.com/lexv2/latest/dg/using-intent-confidence-scores.html)
- [Genesys Resource Center](https://help.mypurecloud.com/articles/best-practices-to-build-and-test-your-natural-language-understanding/)
- [Genesys Blog](https://www.genesys.com/blog/post/set-bot-confidence-thresholds)
- [Voiceflow NLU Design](https://www.voiceflow.com/pathways/5-principles-for-good-natural-language-understanding-nlu-design)
- [ServiceNow Community Q&A](https://www.servicenow.com/community/developer-forum/how-is-the-nlu-confidence-threshold-calculated/m-p/2142617#M799543)

If you want further detail, code samples, or hands-on configuration guides for a specific NLU platform, refer to the linked documentation and community articles above.

