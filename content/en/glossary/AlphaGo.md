---
title: AlphaGo
date: 2025-01-11
lastmod: 2026-04-02
translationKey: alphago-deepmind-go-ai
description: An AI system developed by Google DeepMind that defeated the world champion Go player, becoming the first program to conquer the ancient game and marking a watershed moment in AI development.
keywords:
- AlphaGo
- DeepMind
- Go
- deep reinforcement learning
- Monte Carlo tree search
- AI milestone
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/alphago/
---

## What is AlphaGo?

**AlphaGo is an AI system developed by Google DeepMind that defeated world Go champion Lee Sedol with a 4-1 victory in 2016, becoming the first program to beat a world-class Go player.**

Why is this so remarkable? Go contains an estimated 10^170 possible board positions compared to chess's 10^47. It's impossible to compute all possibilities to find the "best move." In Go, success requires intuitive judgment like "this shape resembles something I've seen" or "the global strategy matters more than local battles." Expert predictions in 2016 didn't expect AI to acquire such intuition.

AlphaGo's victory proved that deep learning and reinforcement learning could master not just raw computation, but "strategic thinking" and "creative innovation." From that moment, AI was recognized as genuinely entering the realm of human "intellectual capabilities."

> **In a nutshell:** An AI that can play better than humans at a game with nearly infinite possible moves has finally emerged.

**Key points:**
- **What it does:** Combines deep learning with tree search to find optimal Go moves
- **Why it matters:** Proves that AI can acquire creative thinking and strategic reasoning—not just play games
- **Who uses it:** AI researchers, gaming companies, and enterprise AI developers

## Why it matters

Before AlphaGo, computer scientists considered Go "the limit of AI." While computers surpassed humans at chess in the 1980s, Go is different. The complex interactions, difficulty evaluating positions, and importance of intuitive judgment—this combination overwhelmed traditional search algorithms.

AlphaGo shattered this "limit." Deep neural networks learned intuitive value judgment and move selection from millions of professional Go games, while Monte Carlo tree search used these insights to find optimal moves. This combination redirected the entire field of AI.

The impact was immediate. The following year, AlphaGo Zero was announced—proving superhuman play could emerge from self-play without any human data. This technology lineage evolved into AlphaFold, which solves protein folding and contributes to science.

## How it works

AlphaGo operates with two main components.

The **policy network** predicts "what move should be played next." Trained on 30 million professional moves, it learned the human intuition of "looking at the board and suggesting promising moves." Not perfect prediction, but "narrowing down to the most promising candidate moves."

The **value network** evaluates "from this position, who has the advantage?" It converts board positions into numerical evaluations representing current advantage or disadvantage, helping assess different moves.

Finally, **Monte Carlo tree search (MCTS)** uses both networks to find the optimal move. By having the policy network narrow down candidates and the value network evaluate positions, it finds powerful moves with only a computationally manageable number of simulations.

## Real-world use cases

**The secret match with Fan Hui (2015)**
In a test match, AlphaGo defeated European champion Fan Hui 5-0, the first time an AI beat a professional Go player.

**The Lee Sedol match (2016)**
A public championship against the world champion. AlphaGo won 4-1. Move 37 in the second game was so creative that even professional commentators found it unsettling. The world was astonished, and perceptions of AI transformed overnight.

**The decisive match with Ke Jie (2017)**
AlphaGo defeated the world's #1 ranked player Ke Jie 3-0. Ke Jie called AlphaGo's play "godlike." DeepMind subsequently retired AlphaGo from competitive play.

## Benefits and considerations

**Benefits:** AlphaGo demonstrated that AI can make decisions in complex, uncertain environments. It opened doors to AI applications beyond games—in finance, medicine, materials science, and other domains requiring difficult decisions. The Go community has been influenced too, with new strategies and standard patterns discovered through matches against AI.

**Considerations:** AlphaGo is designed for perfect information games (both players see the entire board). Most real-world problems involve incomplete information, uncertainty, and complex interactions, requiring careful adaptation. Additionally, AlphaGo's "decision-making" differs from human strategy—why it makes specific choices remains a "black box."

## Related terms

- **[AlphaZero](AlphaZero.md)** — AlphaGo's successor that masters multiple games with the same algorithm
- **[Deep Reinforcement Learning](Deep-Reinforcement-Learning.md)** — Foundation of AlphaGo's training method
- **[Monte Carlo Tree Search](Monte-Carlo-Tree-Search.md)** — Search algorithm used by AlphaGo
- **[Neural Network](Neural-Network.md)** — The mechanism implementing AlphaGo's "intuition"
- **[AlphaFold](AlphaFold.md)** — Applies AlphaGo's technology to solve protein structure prediction

## Frequently asked questions

**Q: How did AlphaGo learn to be "strong"?**
A: In two stages. First, it learned from 30 million professional moves, then played against itself to improve further. Learning from self-play (reinforcement learning) allowed it to discover strategies more sophisticated than human play.

**Q: Was AlphaGo "taught" Go's rules?**
A: The rules are provided, but strategy, standard patterns, and position evaluation were all learned by the AI. It was given only the rules, then left free to learn everything else.

**Q: Isn't AlphaGo's victory just due to computing power?**
A: No. Pure computation cannot win at Go; calculating all 10^170 positions is impossible. AlphaGo's innovation was combining neural networks—"intuition"—to find near-optimal moves with limited computation. This approach resembles human thinking.

## References

1. DeepMind. (2016). Mastering the game of Go with deep neural networks and tree search. Nature.
2. Silver, D., et al. (2016). Mastering the game of Go without human knowledge. Nature.
3. Google DeepMind. AlphaGo Technical Resources. 2024.
4. The Guardian. (2016). Google's AlphaGo seals 4-1 victory over Lee Sedol.
5. AlphaGo Documentary. (2017). Sundance Film Festival Award Winner.
