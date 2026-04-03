---
title: AlphaZero
date: 2025-01-11
lastmod: 2026-04-02
translationKey: alphazero-deepmind-game-ai
description: An AI system developed by Google DeepMind that masters chess, shogi, and Go through self-play alone, surpassing the strongest programs in each game without any human training data.
keywords:
- AlphaZero
- DeepMind
- self-play
- reinforcement learning
- chess AI
- game AI
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/alphazero/
---

## What is AlphaZero?

**AlphaZero is an AI system developed by Google DeepMind that masters chess, shogi, and Go through pure self-play with zero human data, surpassing the strongest programs in each game.**

The fundamental difference from AlphaGo is crucial: AlphaGo initially learned from 30 million professional moves, then played against itself. AlphaZero, by contrast, receives only the rules and starts from scratch. From random play to surpassing the world's strongest chess engine in 4 hours. To surpassing the strongest shogi engine in 9 hours. This demonstrated that "AI can become superhuman without human knowledge."

> **In a nutshell:** Give it only the rules, let it play against itself for a few hours, and it becomes far stronger than humans.

**Key points:**
- **What it does:** A general-purpose algorithm that masters complex games through self-play alone
- **Why it matters:** Achieves superhuman performance without human data, demonstrating AI's generalization potential
- **Who uses it:** AI researchers and companies needing AI to work across multiple domains

## Why it matters

Until AlphaGo, people thought "AlphaGo is customized for Go." AlphaZero was shocking because it achieved peak performance in three completely different games—chess, shogi, and Go—using the identical algorithm and parameters.

In other words, AlphaZero is not "game-specific" but "general-purpose." Without tweaking parameters for each game, it becomes unbeatable from the rules alone. This marks AI's shift from a limited-domain "specialist" to a versatile "universal learner" functioning across wide domains.

More remarkably, the process itself is stunning. Strategies and patterns AlphaZero discovers sometimes differ from what humans accumulated over centuries and can be creative. Garry Kasparov, world chess champion, called AlphaZero's play "alien yet effective." This example of AI generating novel knowledge while ignoring human experience is scientifically profound.

## How it works

AlphaZero training is a **self-play loop**.

1. **Game generation** — The current neural network plays millions of games against itself. Monte Carlo tree search carefully selects each move.

2. **Data accumulation** — Game results (win/loss) and the neural network's position predictions are recorded.

3. **Network improvement** — Using this game data, the neural network improves. Winning moves are valued higher; losing moves, lower.

4. **Iteration** — The improved network plays against itself again. The stronger network generates more games. This loop repeats for hours.

The result: within days, play surpassing centuries of human knowledge.

## Real-world use cases

**Replacing chess engines**
Traditional engines like Stockfish used hand-crafted evaluation functions to judge positions. AlphaZero plays stronger and more creatively using neural networks alone.

**Expanding beyond games**
AlphaZero's technology extended beyond games. AlphaFold applied the same principles to protein folding. Progress continues toward real-world complex problem-solving: materials discovery, robot control, financial portfolio optimization.

**Autonomous agent learning**
Successor systems like MuZero aim for learning in environments where rules aren't even given. AlphaZero's "learning from self-play" foundation now supports autonomous agents.

## Benefits and considerations

**Benefits:** The algorithm is general-purpose and applicable across domains. Requiring neither human data nor domain knowledge means powerful AI emerges even in data-scarce fields. The efficient combination of neural networks and search also offers computational efficiency.

**Considerations:** AlphaZero targets perfect information games. Most real business problems involve incomplete information with uncertain opponent intentions and environments. Additionally, generating massive self-play data requires computational resources (TPUs) making it challenging for individual researchers.

## Related terms

- **[AlphaGo](AlphaGo.md)** — AlphaZero's predecessor, initially trained on human data
- **[MuZero](MuZero.md)** — AlphaZero's successor enabling learning in rule-unknown environments
- **[Reinforcement Learning](Reinforcement-Learning.md)** — AlphaZero's training method
- **[Self-Supervised Learning](Self-Supervised-Learning.md)** — Learning approach without human labels
- **[AlphaFold](AlphaFold.md)** — Applies AlphaZero principles to scientific problems

## Frequently asked questions

**Q: Does AlphaZero really become strong from just the rules?**
A: Yes. Only rules and rewards (win/loss). Starting from random play, self-play over hours produces superhuman strength. No initial data is used.

**Q: Can humans understand AlphaZero's discovered strategies?**
A: Some, but many lack clear explanation. AlphaZero may judge "this move has high win probability," yet humans cannot explain why. This reflects AI's "black box" aspect.

**Q: Can AlphaZero technology apply beyond games?**
A: Yes. AlphaFold revolutionized protein structure prediction using the same principles. MuZero targets rule-unknown environments. However, some limitations exist—the technology works best in "easily simulated" environments like games.

## References

1. Silver, D., et al. (2017). Mastering Chess and Shogi by Self-Play. Science.
2. DeepMind Blog. (2018). AlphaZero: Shedding New Light on Chess. DeepMind.
3. Nature. (2018). AlphaZero and the Changing Nature of AI Research. Nature Commentary.
4. Kasparov, G. (2018). How Deep Blue Changed AI and Chess Forever. The Atlantic.
5. Leela Chess Zero. Open Source AlphaZero Implementation. 2024.
