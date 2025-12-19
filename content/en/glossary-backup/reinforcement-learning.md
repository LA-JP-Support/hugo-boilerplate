---
title: "Reinforcement Learning"
date: 2025-12-17
translationKey: "reinforcement-learning"
description: "Reinforcement learning (RL) is a type of machine learning where an agent learns to make sequential decisions by interacting with an environment and maximizing cumulative rewards through trial and error."
keywords: ["reinforcement learning", "machine learning", "AI", "agent", "Markov Decision Process"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## Definition

Reinforcement learning (RL) is a type of machine learning in which an agent learns to make sequential decisions by interacting with an environment and receiving feedback in the form of rewards or penalties. The agent’s objective is to maximize its cumulative future rewards, adjusting its strategy through trial and error. RL is mathematically formalized by the framework of Markov Decision Processes (MDPs), where an agent’s current decision depends only on the present state, not on the sequence of events that preceded it ([Sutton & Barto, 2018](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf); [Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning); [GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)).

## Key Concepts

RL is built on several foundational elements. Understanding these is crucial for grasping how learning and optimization occur in RL systems.

### Agent

The agent is the learner or decision-maker. It interacts with the environment by taking actions, observing states, and updating its policy (the mapping from states to actions) based on received feedback. The agent’s role is to explore and exploit actions to maximize cumulative rewards.

- *Reference:* [Sutton & Barto, Ch. 3.1: The Agent–Environment Interface](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Further reading:* [GeeksforGeeks: Agent](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

### Environment

The environment is the external system with which the agent interacts. It provides observations (states), receives the agent’s actions, and returns rewards and new states. In RL, environments can be deterministic or stochastic, fully observable or partially observable.

- *Reference:* [Sutton & Barto, Ch. 1.3: Elements of Reinforcement Learning](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

### State

A state is a complete description of the agent’s situation within the environment at a given time. In formal RL, the state represents all information necessary to determine what happens next (the Markov property).

- *Reference:* [Sutton & Barto, Ch. 3.5: The Markov Property](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Further reading:* [Wikipedia: State (RL)](https://en.wikipedia.org/wiki/Reinforcement_learning#Basic_idea)

### Action

An action is a possible move the agent can take in a given state. The set of all possible actions can be discrete (e.g., up/down/left/right in a maze) or continuous (e.g., steering angles in robotics).

- *Reference:* [Sutton & Barto, Ch. 1.3](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

### Reward

A reward is a scalar feedback signal sent from the environment to the agent after each action, indicating the immediate benefit (positive, negative, or zero) of that action. The reward function defines the goal of the RL problem.

- *Reference:* [Sutton & Barto, Ch. 3.2: Goals and Rewards](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Further reading:* [GeeksforGeeks: Reward Signal](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

### Policy

A policy is a strategy or mapping from states to actions. It can be deterministic (always the same action in a given state) or stochastic (probabilistic action selection).

- *Reference:* [Sutton & Barto, Ch. 1.3](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Further reading:* [GeeksforGeeks: Policy](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

### Value Function

The value function estimates the expected cumulative reward (also called return) that the agent can obtain from a given state or state-action pair, considering possible future actions. Value functions are central to evaluating and improving policies.

- *Reference:* [Sutton & Barto, Ch. 3.7: Value Functions](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Further reading:* [GeeksforGeeks: Value Function](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

### Model

A model predicts how the environment will respond to the agent’s actions, including the next state and expected reward. Model-based RL leverages this for planning.

- *Reference:* [Sutton & Barto, Ch. 8.1: Models and Planning](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

## How Reinforcement Learning Works

The RL loop involves the agent repeatedly:

1. Observing the current state of the environment.
2. Selecting and executing an action based on its policy.
3. Receiving a reward and the next state from the environment.
4. Updating its policy and/or value function based on the experience.

This process is typically iterative, with the agent improving its behavior over time through experience, balancing exploration (trying new actions) and exploitation (choosing the best-known action).

### Mathematical Framework: Markov Decision Process (MDP)

An MDP provides a formal definition for RL problems, defined by:

- **S**: Set of states
- **A**: Set of actions
- **P(s'|s, a)**: State transition probability function
- **R(s, a)**: Reward function
- **γ**: Discount factor (0 ≤ γ ≤ 1), controlling the importance of future rewards

The objective is to maximize the expected cumulative discounted reward:

\[
\mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t r_t \right]
\]

where \( r_t \) is the reward at time step \( t \).

- *Reference:* [Sutton & Barto, Ch. 3.6: Markov Decision Processes](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Further reading:* [GeeksforGeeks: Markov Decision Process](https://www.geeksforgeeks.org/machine-learning/markov-decision-process/)

#### Bellman Equation

The Bellman equation relates the value of a state to the expected value of successor states:

\[
V(s) = \mathbb{E}_{a \sim \pi(s)} \left[ R(s, a) + \gamma \mathbb{E}_{s'} [V(s')] \right]
\]

This recursive relationship is foundational for many RL algorithms.

- *Reference:* [Sutton & Barto, Ch. 3.7: Value Functions](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

### Exploration vs. Exploitation

The agent must balance exploring new actions (which may yield higher rewards) and exploiting known actions (which already yield high rewards). Various strategies, such as epsilon-greedy or Upper Confidence Bound (UCB), are used to address this tradeoff.

- *Reference:* [Sutton & Barto, Ch. 2.6: Upper-Confidence-Bound Action Selection](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

## Types of Reinforcement Learning Algorithms

RL algorithms are categorized by whether they use a model of the environment and how they represent the policy.

### 1. Model-Free vs. Model-Based RL

- **Model-Free RL:** The agent learns good actions directly from experience, without building a model of the environment.
  - Algorithms: Q-Learning, SARSA, Policy Gradient
  - *Reference:* [Sutton & Barto, Ch. 6: Temporal-Difference Learning](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)
- **Model-Based RL:** The agent builds and uses a model of the environment for planning.
  - Algorithms: Dyna-Q, Monte Carlo Tree Search
  - *Reference:* [Sutton & Barto, Ch. 8: Planning and Learning](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

### 2. Value-Based vs. Policy-Based vs. Actor-Critic Methods

| Algorithm Type  | Description                                                      | Example Algorithms                      | Typical Use Case                          |
|-----------------|------------------------------------------------------------------|-----------------------------------------|-------------------------------------------|
| Value-Based     | Learns value functions (state or state-action values)            | Q-Learning, SARSA                      | Discrete action spaces                    |
| Policy-Based    | Learns policies directly (parameterized strategies)              | Policy Gradient, REINFORCE              | Continuous or high-dimensional actions    |
| Actor-Critic    | Combines value-based (critic) and policy-based (actor) methods   | Advantage Actor-Critic (A2C), DDPG      | Complex tasks, stable learning            |

#### Example: Q-Learning

Q-Learning is a popular off-policy, model-free, value-based RL algorithm. It maintains a table of Q-values, updating them using:

\[
Q(s, a) \gets Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
\]

- *Reference:* [Sutton & Barto, Ch. 6.5: Q-Learning](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)  
- *Practical tutorial:* [GeeksforGeeks: Q-Learning in Python](https://www.geeksforgeeks.org/machine-learning/q-learning-in-python/)

#### Example: Policy Gradient

Policy gradient methods optimize the policy directly by adjusting its parameters using gradient ascent to maximize expected reward.

- *Reference:* [Sutton & Barto, Ch. 13: Policy Approximation](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

#### Example: Actor-Critic

Actor-critic methods employ two models: an actor (policy estimator) and a critic (value function estimator). The critic evaluates the actions taken by the actor, providing a learning signal.

- *Reference:* [Sutton & Barto, Ch. 11.1: Actor–Critic Methods](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

### Deep Reinforcement Learning

Deep RL integrates deep neural networks as function approximators for value functions or policies, enabling RL to scale to high-dimensional or unstructured environments (e.g., computer vision, games like Go).

- *Reference:* [Nature: AlphaGo](https://www.nature.com/articles/nature16961)  
- *Overview:* [Deep RL with TensorFlow (YouTube)](https://www.youtube.com/watch?v=2pWv7GOvuf0)

## Practical Examples and Use Cases

RL is applied across various domains, from robotics to finance.

### Robotics

- **Navigation:** RL enables robots to move through complex environments by trial and error, receiving rewards for reaching targets and penalties for collisions.  
  - *Reference:* [OpenAI Gym Robotics](https://gym.openai.com/envs/#robotics)
- **Manipulation:** RL trains robotic arms to pick, place, or assemble objects efficiently.

### Gaming

- **AlphaGo:** Deep RL enabled AlphaGo to defeat world-champion Go players, learning strategies via self-play and MCTS ([Nature paper](https://www.nature.com/articles/nature16961)).
- **Atari Games:** RL agents achieve superhuman performance in classic video games, learning solely from pixels ([YouTube: DeepMind Atari](https://www.youtube.com/watch?v=V1eYniJ0Rnk)).

### Autonomous Vehicles

- **Self-Driving Cars:** RL is used for decision-making in lane keeping, path planning, and adaptive cruise control, optimizing long-term safety and efficiency ([Wayve RL for AVs](https://wayve.ai/blog/reinforcement-learning-for-autonomous-driving/)).

### Industrial Control

- **Process Optimization:** RL controls variables like temperature and flow in industrial plants for improved efficiency and safety.

### Marketing Personalization

- **Recommendation Systems:** RL customizes product or content recommendations, learning user preferences to maximize engagement ([Salesforce RL](https://www.salesforce.com/blog/reinforcement-learning/)).

### Financial Prediction

- **Algorithmic Trading:** RL adapts trading strategies in real time, optimizing long-term returns while accounting for transaction costs and volatility ([AWS RL in Finance](https://aws.amazon.com/machine-learning/what-is-reinforcement-learning/)).

### Energy Management

- **Smart Grids:** RL agents manage energy storage and distribution, adapting to fluctuating demand and supply ([Synopsys Energy RL](https://www.synopsys.com/glossary/what-is-reinforcement-learning.html)).

## Benefits of Reinforcement Learning

- **Adaptivity:** Learns optimal strategies in dynamic, uncertain, or partially observable environments.
- **Autonomy:** Learns directly from experience, no labeled training data required.
- **Long-Term Optimization:** Focuses on maximizing cumulative (not just immediate) rewards.
- **Generalization:** Deep RL can generalize across similar but not identical tasks.
- **Innovation:** May discover novel or non-intuitive solutions.

- *Further reading:* [IBM: What is RL?](https://www.ibm.com/topics/reinforcement-learning)

## Challenges and Limitations

- **Sample Inefficiency:** RL often requires millions of interactions, which can be slow or costly in real-world settings.
- **Reward Design:** Poorly specified reward functions can lead to unintended or unsafe behaviors.
- **Exploration Risk:** Unsafe exploratory actions can be hazardous in physical environments.
- **Computational Complexity:** Training RL agents (especially deep RL) is resource-intensive.
- **Interpretability:** The learned policies can be difficult to interpret or explain.
- **Delayed Rewards:** Credit assignment for actions that impact distant future outcomes remains challenging.

- *Reference:* [Sutton & Barto, Ch. 1.4: Limitations and Scope](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)

## Comparison with Other Machine Learning Paradigms

| Aspect                      | Reinforcement Learning                | Supervised Learning                     | Unsupervised Learning                |
|-----------------------------|---------------------------------------|-----------------------------------------|--------------------------------------|
| Learning Data               | Experience from environment           | Labeled input-output pairs              | Unlabeled data                       |
| Objective                   | Maximize cumulative reward            | Minimize prediction error               | Discover patterns/structure          |
| Feedback                    | Delayed, sequential (reward signal)   | Immediate, explicit (correct label)     | None                                 |
| Typical Use Cases           | Sequential decision making, control   | Classification, regression              | Clustering, dimensionality reduction |
| Supervision                 | No explicit supervisor                | Requires supervisor for labeling        | No supervisor                        |
| Exploration-Exploitation    | Essential tradeoff                    | Not required                            | Not required                         |
| Data Efficiency             | Often low (sample inefficient)        | Moderate/high                           | High                                 |
| Model Adaptivity            | High                                  | Moderate                                | High                                 |

- *Further reading:* [Wikipedia: RL vs. other ML](https://en.wikipedia.org/wiki/Reinforcement_learning#Comparison_with_other_machine_learning_paradigms)

## Types of Reinforcement

### Positive Reinforcement

- **Definition:** Increases the frequency or strength of behavior by providing a positive outcome.
- **Example:** A robot receives a reward for successfully reaching a goal location.
- **Advantages:** Maximizes performance, helps sustain change over time.
- **Disadvantages:** Overuse can reduce effectiveness.

### Negative Reinforcement

- **Definition:** Increases behavior by removing an unpleasant outcome or penalty.
- **Example:** An agent avoids actions that lead to negative rewards.
- **Advantages:** Increases minimum performance.
- **Disadvantages:** May only encourage actions to avoid penalty rather than optimize.

- *Reference:* [GeeksforGeeks: Types of Reinforcement](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

## Online vs. Offline Reinforcement Learning

| Aspect            | Online RL                                      | Offline RL                                 |
|-------------------|------------------------------------------------|--------------------------------------------|
| Data Acquisition  | Real-time interaction with environment         | Uses fixed, pre-collected dataset          |
| Adaptivity        | High, learns and adapts continuously           | Limited to the coverage of historical data |
| Suitability       | Feasible when environment access is safe/cheap | Useful when real-world interaction is risky|
| Challenges        | Resource/compute intensive, safety risks       | Distribution shift, limited generalization |

- *Reference:* [GeeksforGeeks: Online vs. Offline RL](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

## Example: RL in Maze Navigation (Q-Learning)

This example demonstrates Q-learning for maze navigation, including full implementation steps, code, and visualization:

- Agent starts at an initial position in a 2D maze.
- At each step, chooses an action (up, down, left, right).
- Receives reward or penalty, updates its Q-value.
- Learns over many episodes, improving its path-finding.

**Code and visualization steps:**  
- [GeeksforGeeks: RL Maze Navigation Python Example](https://www.geeksforgeeks

