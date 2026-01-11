---
title: "AlphaZero"
date: 2025-01-11
translationKey: "alphazero-deepmind-game-ai"
description: "AlphaZero is DeepMind's AI system that mastered chess, shogi, and Go through self-play alone, achieving superhuman performance without human knowledge or game-specific tuning."
keywords: ["AlphaZero", "DeepMind", "self-play", "reinforcement learning", "chess AI", "game AI"]
category: "AI Chatbot & Automation"
type: "glossary"
draft: false
---

## What Is AlphaZero?

AlphaZero is a groundbreaking artificial intelligence system developed by [Google DeepMind](Google-DeepMind.md) that achieved superhuman performance in chess, shogi (Japanese chess), and Go using a single general-purpose algorithm. Unlike its predecessor [AlphaGo](AlphaGo.md), which was trained on millions of human expert games, AlphaZero learned entirely through self-play, starting from random play and discovering optimal strategies without any human knowledge beyond the basic rules of each game.

Published in December 2017 and expanded in a 2019 Science paper, AlphaZero demonstrated that a single algorithm could master multiple complex games without game-specific modifications. The system defeated the world's strongest specialized programs in each domain: Stockfish in chess, Elmo in shogi, and AlphaGo Zero in Go. Most remarkably, AlphaZero achieved this mastery in mere hours of training, developing novel strategies that surprised human experts and challenged centuries of accumulated chess theory.

AlphaZero represents a significant step toward more general artificial intelligence, showing that deep reinforcement learning combined with Monte Carlo tree search can discover superhuman strategies across diverse domains without relying on human expertise. The system's elegant simplicity—a single neural network learning from self-play—demonstrated that general learning algorithms could match or exceed specialized, hand-crafted approaches that had been refined over decades.

## Core Innovation: Tabula Rasa Learning

AlphaZero's most revolutionary aspect is its ability to learn from scratch:

**No Human Knowledge**
- Starts with zero knowledge beyond game rules
- No opening books, endgame tables, or strategic heuristics
- No training on human expert games
- Discovers all strategies through self-generated experience
- Proves human knowledge unnecessary for superhuman performance

**Self-Play Training**
- Plays millions of games against itself
- Both players share the same neural network
- Earlier versions serve as opponents for current version
- Continuously improves through competition with itself
- Generates own training data without external input

**Single Algorithm for Multiple Games**
- Same architecture and hyperparameters for chess, shogi, and Go
- Only the game rules differ between domains
- Demonstrates generality of the approach
- No game-specific tuning or modifications
- Proves fundamental algorithmic principles apply broadly

**Comparison with Traditional Approaches**

| Aspect | Traditional Game AI | AlphaZero |
|--------|---------------------|-----------|
| Knowledge Source | Human expertise, databases | Self-play only |
| Evaluation | Hand-crafted features | Learned neural network |
| Search | Alpha-beta with extensions | MCTS with neural guidance |
| Tuning | Game-specific optimization | General algorithm |
| Development Time | Decades of refinement | Hours of training |

## Technical Architecture

AlphaZero employs a streamlined architecture combining neural networks with tree search:

**Neural Network Design**

*Input Representation*
- Board state encoded as multi-channel image
- Includes piece positions, castling rights, move history
- Consistent representation across games
- 8×8×119 planes for chess, different sizes for other games

*Network Architecture*
- Deep residual convolutional neural network
- 20 residual blocks (40 convolutional layers)
- Batch normalization and ReLU activations
- Dual output heads for policy and value

*Policy Head*
- Outputs probability distribution over legal moves
- Guides search toward promising moves
- Learned entirely from self-play outcomes
- Replaces opening books and strategic heuristics

*Value Head*
- Outputs predicted game outcome (-1 to +1)
- Evaluates positions for tree search
- Replaces hand-crafted evaluation functions
- Provides accurate position assessment

**Monte Carlo Tree Search (MCTS)**

*Search Process*
- Builds tree of possible game continuations
- Uses neural network to evaluate positions and select moves
- Balances exploration (new moves) and exploitation (known good moves)
- Runs thousands of simulations per move decision

*Move Selection*
- PUCT formula balances prior policy and visit counts
- Temperature parameter controls exploration
- Final move selection based on visit counts
- Ensures robust decisions even with limited search

**Training Process**

*Game Generation*
- Plays games against itself using current network
- MCTS with added exploration noise for move selection
- Games continue until termination (checkmate, draw, etc.)
- Stores game data for training

*Network Updates*
- Mini-batch training on recent self-play games
- Loss combines policy accuracy and value prediction
- Continuous improvement through gradient descent
- No separate training phases or curriculum

## Performance and Results

**Chess Results**

*Defeating Stockfish*
- Won 28-0 (72 draws) in 100-game match
- Stockfish given full opening book and 64 threads
- AlphaZero used single TPU for search
- Achieved superhuman level in 4 hours of training

*Novel Chess Understanding*
- Developed unique playing style prioritizing activity
- Willing to sacrifice material for dynamic compensation
- Created new opening variations
- Challenged conventional chess theory

*Expert Assessment*
- Former world champion Garry Kasparov praised creative play
- Chess experts noted "alien" but effective strategies
- Influenced human chess understanding and training
- Games studied extensively by professionals

**Shogi Results**

*Defeating Elmo*
- Won 90-8 (2 draws) against 2017 computer champion
- Achieved superhuman level in 2 hours of training
- First general algorithm to master shogi at expert level
- Demonstrated applicability to larger game spaces

*Shogi Complexity*
- Larger board (9×9) than chess
- Captured pieces can be reused (drops)
- Average game length ~115 moves
- More complex than chess in some respects

**Go Results**

*Defeating AlphaGo Zero*
- Won decisively against previous DeepMind system
- Achieved comparable performance with less computation
- Same algorithm used for chess and shogi
- Confirmed generality of approach

*Comparison with AlphaGo*
- No human game training data
- Simpler architecture
- Faster training time
- Stronger ultimate performance

**Training Efficiency**

| Game | Training Time | Games Played | Performance |
|------|---------------|--------------|-------------|
| Chess | 4 hours | 44 million | Defeated Stockfish |
| Shogi | 2 hours | 24 million | Defeated Elmo |
| Go | 8 hours | 21 million | Defeated AlphaGo Zero |

## Key Differences from Traditional Chess Engines

AlphaZero's approach differs fundamentally from conventional chess programs:

**Evaluation Philosophy**

*Traditional Engines*
- Hand-crafted evaluation with hundreds of features
- Material counting as primary component
- King safety, pawn structure, piece activity metrics
- Refined over decades by human programmers

*AlphaZero*
- Learned evaluation from self-play
- Single neural network output
- No explicit feature engineering
- Discovers relevant factors automatically

**Search Strategy**

*Traditional Engines*
- Alpha-beta search with pruning
- Deep, focused search trees
- Millions of positions per second
- Heavy reliance on search depth

*AlphaZero*
- Monte Carlo tree search with neural guidance
- Selective, intuition-guided search
- Fewer positions but better evaluations
- Quality over quantity in search

**Playing Style**

*Traditional Engines*
- Conservative, materialistic play
- Risk-averse decision making
- Emphasis on concrete calculation
- Predictable strategic choices

*AlphaZero*
- Dynamic, activity-focused play
- Willing to sacrifice for initiative
- Long-term positional understanding
- Creative and unexpected strategies

## Impact and Significance

**Scientific Impact**

*Proof of General Learning*
- Demonstrated single algorithm can master multiple domains
- Showed human knowledge unnecessary for superhuman performance
- Validated deep reinforcement learning approach
- Inspired research into more general AI systems

*Methodological Contributions*
- Established self-play as powerful training paradigm
- Showed value of combining neural networks with search
- Demonstrated efficiency of tabula rasa learning
- Influenced approaches to other AI challenges

**Impact on Chess**

*Changed Understanding*
- Revealed new strategic concepts
- Challenged long-held positional principles
- Showed value of dynamic piece activity
- Influenced opening theory and preparation

*Professional Adoption*
- Chess professionals study AlphaZero games
- Training methods influenced by AI insights
- Opening preparation incorporating AI ideas
- Philosophical discussion about chess understanding

**Impact on AI Development**

*Successor Systems*
- MuZero: Extended approach to games without known rules
- AlphaFold: Similar principles applied to protein folding
- Influenced robotics and control applications
- Inspired general game-playing research

*Industry Influence*
- Demonstrated potential of self-supervised learning
- Influenced development of other AI systems
- Showed importance of scale and compute
- Validated neural network approaches to planning

## Limitations and Context

**Computational Requirements**
- Training requires significant TPU resources
- Not easily replicable by individual researchers
- Industrial-scale compute necessary
- Environmental and cost considerations

**Domain Specificity**
- Limited to perfect-information games
- Rules must be known and fixed
- Self-play requires deterministic simulation
- Not directly applicable to real-world uncertainty

**Comparison Caveats**
- Hardware advantages over opponents (TPU vs CPU)
- Different search paradigms difficult to compare fairly
- Opening book access varies by opponent
- Time control affects relative performance

**Open Questions**
- How to extend to imperfect information games
- Applicability to continuous action spaces
- Transfer learning between related domains
- Combining with human knowledge when beneficial

## Legacy and Evolution

**Direct Successors**

*MuZero (2019)*
- Learned game rules through experience
- No explicit game model required
- Extended to Atari games and other domains
- Further generalization of AlphaZero

*Open Source Implementations*
- Leela Chess Zero: Community chess implementation
- KataGo: Open-source Go implementation
- Various research implementations
- Democratized access to techniques

**Broader Influence**

*Scientific Applications*
- AlphaFold protein structure prediction
- Materials discovery
- Mathematical theorem proving
- Drug design optimization

*Robotics and Control*
- Self-play for robotic manipulation
- Autonomous vehicle planning
- Industrial optimization
- Game-theoretic reasoning

**Philosophical Impact**
- Questions about nature of intelligence
- Debate over human vs. machine creativity
- Implications for AI development strategy
- Discussion of AI alignment and safety

## Technical Comparison with Related Systems

| Feature | AlphaGo | AlphaGo Zero | AlphaZero | MuZero |
|---------|---------|--------------|-----------|--------|
| Human Data | Yes | No | No | No |
| Game Rules | Known | Known | Known | Learned |
| Games Supported | Go only | Go only | Chess, Shogi, Go | Atari + Board games |
| Architecture | Separate policy/value | Combined network | Combined network | World model + prediction |
| Training | SL + RL | RL only | RL only | RL only |
| Search | MCTS | MCTS | MCTS | MCTS (learned model) |

## Significance for AI Research

AlphaZero represents a landmark achievement in artificial intelligence for several reasons:

**Generality Demonstration**
- Single algorithm mastering multiple complex domains
- No game-specific engineering required
- Proves fundamental principles apply broadly
- Step toward more general AI systems

**Learning Efficiency**
- Superhuman performance from hours of self-play
- More efficient than decades of human refinement
- Demonstrates power of modern compute and algorithms
- Questions assumptions about AI development

**Human Knowledge Obsolescence**
- Proves AI can exceed human understanding without learning from humans
- Challenges assumptions about knowledge acquisition
- Implications for education and expertise
- Questions about AI-human collaboration

AlphaZero's elegant demonstration that a single learning algorithm could discover superhuman strategies across multiple complex domains marked a significant milestone in AI research, influencing subsequent developments in game AI, scientific applications, and the broader pursuit of artificial general intelligence.

## References

- [DeepMind: AlphaZero](https://deepmind.google/discover/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/)
- [Science: A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](https://www.science.org/doi/10.1126/science.aar6404)
- [arXiv: Mastering Chess and Shogi by Self-Play](https://arxiv.org/abs/1712.01815)
- [Chess.com: What is AlphaZero?](https://www.chess.com/terms/alphazero-chess-engine)
- [Nature: AlphaZero and the changing nature of AI research](https://www.nature.com/articles/d41586-018-07733-0)
- [The Atlantic: What Garry Kasparov Thinks About AlphaZero](https://www.theatlantic.com/technology/archive/2018/01/garry-kasparov-alphazero/549396/)
- [Leela Chess Zero](https://lczero.org/)
- [Wikipedia: AlphaZero](https://en.wikipedia.org/wiki/AlphaZero)
