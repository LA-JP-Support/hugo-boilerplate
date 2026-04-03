---
title: Tree of Thoughts
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Tree-of-Thoughts
description: An AI reasoning framework that enables systematic exploration of multiple solution paths. Applied to complex problem solving.
keywords:
- Tree of Thoughts
- AI Reasoning
- Problem Solving
- Language Models
- Deliberate Exploration
category: AI & Machine Learning
type: glossary
draft: false
url: /en/glossary/Tree-of-Thoughts/
---

## What is Tree of Thoughts?

**Tree of Thoughts is a method where AI solves complex problems by considering multiple approaches simultaneously and selecting the most promising direction while working through the problem.** Normally, AI operates as "given a question, produce an answer in one straight line." But for challenging problems like difficult math or creative tasks, you need to try multiple approaches, backtrack when one fails, and try an alternative. Tree of Thoughts enables this "trial and error process" for AI.

> **In a nutshell:** "AI exploring multiple 'lines of thinking' simultaneously and selecting the best one."

**Key points:**

- **What it does:** Track multiple solutions simultaneously and find the optimal path
- **Why it's needed:** Linear thinking sometimes fails to find optimal solutions for complex problems
- **Who uses it:** AI engineers, R&D teams, companies dealing with complex problems

## Why It Matters

Traditional AI works "left to right"—proceeding in one straight line to produce an answer. This works for simple questions but fails with complex problems. For example, in a math word problem, there may be multiple solution methods, but if the AI's first choice is wrong, everything fails.

With Tree of Thoughts, AI can consider "Method A, Method B, Method C—which should I try?" simultaneously. If Method A reaches a dead end, it can backtrack and try Method B. Through this trial and error, it finds the optimal solution. This dramatically expands the range of problems AI can solve.

## How It Works

Tree of Thoughts literally takes the shape of a tree. The root is the starting point of the problem. Multiple branches extend from it, each representing a different approach. Each branch itself has further choices.

For example, with a math problem like "5 apples and 3 oranges cost 780 yen. 1 apple and 2 oranges cost 350 yen. What are the prices?", the AI might explore three branches simultaneously: "solve algebraically," "use a graph," or "solve by trial and error." For each method, it performs calculations and evaluates which is most reliable and fastest.

Importantly, the AI can decide "this branch looks like it will fail, so stop exploring this part." This is called "pruning." Rather than continuing all branches to completion, only promising branches are explored deeply, making computation efficient.

## Real-World Use Cases

**Math Problem Solving:** A difficult college entrance exam problem is solved by AI using multiple methods simultaneously. It might notice "the vector approach would be faster" and explore that method more deeply.

**Game AI:** Chess and Go AIs consider multiple strategies simultaneously. They explore "what if I make this move?" and "what about that move?" looking many moves ahead using Tree of Thoughts.

**Code Generation:** Code generation AI considers multiple implementation approaches. It finds optimal solutions across different conditions—efficient code, readable code, concise code.

## Benefits and Considerations

The benefit of Tree of Thoughts is more accurate answers for complex problems. Additionally, it becomes easier for AI to explain "why it reached this answer"—it can trace which path was explored and which branch was ultimately chosen.

However, computation increases. Exploring multiple paths simultaneously takes more time than simple linear thinking. Also, effectiveness varies by problem type. For simple problems, it may actually slow things down.

## Related Terms

- **[Large Language Models (LLM)](large-language-models.md)** — Tree of Thoughts is a technique that extends the reasoning capabilities of LLMs.
- **[Chain-of-Thought](Chain-of-Thought.md)** — The predecessor to Tree of Thoughts. A method for showing a linear "path of thinking."
- **[Reasoning](Reasoning.md)** — The overall process of AI thinking logically. Tree of Thoughts is one type of reasoning.
- **[Prompt Engineering](Prompt-Engineering.md)** — Correct prompts are important for unlocking Tree of Thoughts effectiveness.
- **[Search Algorithm](Search-Algorithm.md)** — The core technology of Tree of Thoughts. A method for finding optimal paths.

## Frequently Asked Questions

**Q: Should Tree of Thoughts be used for all AI tasks?**

A: No. For simple tasks like classification or translation, it would actually slow things down. It's suited for math, code generation, and tasks requiring complex reasoning.

**Q: How much computation time increases?**

A: It depends on problem complexity, but typically 3-10 times slower than linear thinking. In exchange, accuracy increases significantly.

**Q: Does Tree of Thoughts always find the optimal solution?**

A: It increases the likelihood, but not to 100%. Computational resources are limited, so the search may be cut off partway through.
