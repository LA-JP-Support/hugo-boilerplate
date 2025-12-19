---
title: Finite State Machines (FSM)
date: 2025-12-17
translationKey: finite-state-machines-fsm
description: 'Explore Finite State Machines (FSMs): a computational model with states
  and transitions. Learn about DFSM, NDFSM, Mealy, Moore types, and their applications
  in software, hardware, AI, and game development.'
keywords:
- finite state machine
- FSM
- states
- transitions
- Mealy Moore machines
category: Computer Science
type: glossary
draft: false
---

## What is a Finite State Machine?

A **finite state machine (FSM)** is a computational model comprised of a finite set of states, transitions between these states, and rules that determine how the system changes state in response to inputs. FSMs are used to model sequential logic in engineering, digital circuit design, software development, artificial intelligence, and game development. They excel in systems where behavior changes based on a sequence of events or conditions.

**Analogy:**  
Consider a door lock. The lock can be either `locked` or `unlocked`. A correct key transitions it from `locked` to `unlocked`, while an incorrect key leaves it unchanged. This is a classic FSM: the lock is always in one state, and inputs (keys) dictate valid transitions.

- [BLT Inc: A Guide to Finite State Machines](https://bltinc.com/2024/11/04/finite-state-machines-guide/)
- [SiliconVeda: FSM Comprehensive Guide](https://www.siliconveda.com/2024/10/finite-state-machine-fsm-comprehensive.html)

## Core Concepts and Components

### States

A **state** is a distinct mode or condition in which the system can exist. At any given time, the FSM is in exactly one state from its set of possible states.

- Example: A vending machine might be in states like `Idle`, `Waiting for Selection`, `Dispensing Item`, or `Out of Service`.

### Transitions

A **transition** is a rule or function that describes how the FSM moves from one state to another based on an input.

- Example: The vending machine transitions from `Idle` to `Waiting for Selection` when a user inserts money.

### Inputs and Outputs

**Inputs** are external signals or events (e.g., button presses, sensor triggers) that trigger transitions.  
**Outputs** are actions or signals produced by the FSM. Output behavior is defined by the FSM type:
- **Mealy machine**: Output depends on both current state and input.
- **Moore machine**: Output depends only on the current state.

### State Diagrams

A **state diagram** is a graphical representation of an FSM:
- **Nodes**: Represent states.
- **Edges/arrows**: Represent transitions, labeled with the triggering input (and sometimes output).
- **Initial state**: Marked with an arrow from nowhere.
- **Final/accepting states**: Often shown with double circles.

See [FSM state diagram example](https://bltinc.com/2024/11/04/finite-state-machines-guide/) for illustrations.

## Types of Finite State Machines

### Deterministic Finite State Machine (DFSM/DFA)

A **deterministic FSM** ensures that every combination of current state and input leads to exactly one next state—no ambiguity. These are foundational in digital circuit design and software parsing.

- **Example**: Vending machine, password checker.
- Each state/input pair has only one possible transition.

### Non-Deterministic Finite State Machine (NDFSM/NFA)

A **non-deterministic FSM** allows multiple possible next states for the same input and current state. Useful in scenarios like pattern matching or where parallel state exploration is needed.

- **Example**: Elevator control, regex engines.
- Each state/input pair can have multiple transitions, allowing "branching" behavior.

### Mealy Machine

A **Mealy machine** produces outputs based on both the current state and the input. Outputs can change immediately in response to inputs, allowing faster system responses.

- **Example**: Turnstile—output `unlock` when in `locked` state and receiving `coin` input.
- More efficient in terms of required states but can have less stable outputs.

### Moore Machine

A **Moore machine** produces outputs based solely on the current state, independent of the input. Outputs are stable within a state and change only on state transitions.

- **Example**: Traffic light controller—`Red` state always outputs `STOP`.
- More predictable, but may require more states for nuanced output.

#### Mealy vs. Moore: Comparison Table

| Aspect                | Mealy Machine         | Moore Machine         |
|-----------------------|----------------------|----------------------|
| Output dependency     | State + Input        | State only           |
| Response time         | Immediate            | Next state           |
| Number of states      | Fewer                | More (for same logic)|
| Output stability      | Less stable          | More stable          |
| Hardware complexity   | More logic           | More states          |
| Example               | Turnstile            | Traffic light        |

- [See detailed comparison at SiliconVeda](https://www.siliconveda.com/2024/10/finite-state-machine-fsm-comprehensive.html)

## How Finite State Machines Work: Step-by-Step

1. **Define States**: List all distinct operating modes.
2. **Define Inputs**: Enumerate events/signals that trigger transitions.
3. **Define Transitions**: For each state, specify next state for each input.
4. **Create State Table/Diagram**: Visualize or tabulate the transitions.
5. **Set Initial State**: Define the system’s starting state.
6. **Process Inputs**: System receives or waits for external events.
7. **Lookup Transition**: Consult the table or diagram for the next state.
8. **Execute Actions**: Output (if any) is produced.
9. **Update State**: FSM moves to the new state.
10. **Repeat**: The cycle continues for each new input.

**Summary Table: FSM Workflow**

| Step | Description                    |
|------|--------------------------------|
| 1    | Define states                  |
| 2    | Define inputs                  |
| 3    | Define transitions             |
| 4    | Create state table/diagram     |
| 5    | Initialize FSM                 |
| 6-10 | Process input, transition, repeat |

- [FSM construction strategies at BLT Inc.](https://bltinc.com/2024/11/04/finite-state-machines-guide/)

## FSM Construction: Example and Pseudocode

### Code Example: Traffic Light Controller

**States:** Green, Yellow, Red  
**Transition trigger:** Timer expiry

#### State Diagram:
- Green → (timer) → Yellow
- Yellow → (timer) → Red
- Red → (timer) → Green

#### Python Pseudocode:

```python
class TrafficLightFSM:
    def __init__(self):
        self.state = 'Green'
    
    def on_timer(self):
        if self.state == 'Green':
            self.state = 'Yellow'
        elif self.state == 'Yellow':
            self.state = 'Red'
        elif self.state == 'Red':
            self.state = 'Green'
        print(f'Current state: {self.state}')

# Usage
traffic_light = TrafficLightFSM()
for _ in range(5):
    traffic_light.on_timer()
```

This simple FSM cycles through the three states as the timer event occurs.

- [FSM state diagram and code examples: BLT Inc](https://bltinc.com/2024/11/04/finite-state-machines-guide/)

## Real-World Examples and Use Cases

### Software Engineering

- **UI Event Handling**: FSMs manage widget states (`Idle`, `Hovered`, `Clicked`, `Dragging`) in GUIs.
- **Network Protocols**: TCP connections are managed via states like `CLOSED`, `LISTEN`, `SYN_SENT`, `ESTABLISHED`.
- **Compilers/Tokenizers**: Lexical analyzers are FSMs that identify tokens by traversing state graphs per character.

### Hardware and Digital Systems

- **Digital Circuits**: FSMs define behavior in counters, timers, and control units—core to hardware description languages (HDL).
- **Embedded Controllers**: FSMs manage device logic such as power states (`Sleep`, `Active`, `Error`).

### AI, Chatbots, and Automation

- **Chatbot Flows**: FSMs track conversation state (`Greeting`, `Info Gathering`, `Answering`, `Closing`), ensuring context-aware dialogue.
- **Natural Language Processing**: FSMs parse text by defining valid token sequences.
- **Home Automation**: Smart devices transition between states (`Idle`, `Armed`, `Alert`, `Disarmed`) based on input sensors.

### Game Development

FSMs are foundational in character behavior and game logic:
- **Character State Machines**: Control player/NPC behavior (`Idle`, `Walking`, `Jumping`, `Attacking`).
- **Game Progression**: Manage stages like `Start Screen`, `Playing`, `Paused`, `Game Over`.

#### Example: Game Character FSM

From [Game Programming Patterns](https://gameprogrammingpatterns.com/state.html), managing a platform game character:

```cpp
enum State {
    STATE_STANDING,
    STATE_JUMPING,
    STATE_DUCKING,
    STATE_DIVING
};

void Heroine::handleInput(Input input) {
    switch (state_) {
        case STATE_STANDING:
            if (input == PRESS_B) {
                state_ = STATE_JUMPING;
            } else if (input == PRESS_DOWN) {
                state_ = STATE_DUCKING;
            }
            break;
        case STATE_JUMPING:
            if (input == PRESS_DOWN) {
                state_ = STATE_DIVING;
            }
            break;
        case STATE_DUCKING:
            if (input == RELEASE_DOWN) {
                state_ = STATE_STANDING;
            }
            break;
    }
}
```
- [Full game FSM example and flowchart](https://gameprogrammingpatterns.com/state.html)

## Advanced FSM Topics

### Hierarchical and Parallel FSMs

Large systems often require **hierarchical FSMs** (HSMs), where states themselves contain nested FSMs. For example, a robot’s `Exploring` state may contain its own FSM for navigating corners.

**Parallel FSMs** allow multiple FSMs to run independently, managing separate concerns (e.g., a door and its lock as separate FSMs).

- [FSM decomposition and maintainability](https://bltinc.com/2024/11/04/finite-state-machines-guide/)

### State Explosion and Optimization

Complex systems can suffer **state explosion**, where the number of states grows exponentially due to combinations of sub-states.

**Optimization strategies**:
- Decompose large FSMs into smaller interacting FSMs.
- Use hierarchical FSMs to encapsulate sub-behaviors.
- Minimize states by merging equivalent behaviors where possible.

### State Pattern in Object-Oriented Design

In OOP, the **State pattern** encapsulates state-specific behavior in separate classes, allowing objects to change behavior at runtime by changing their current state object. This enhances maintainability and avoids complex conditional logic.

- [State pattern in games](https://gameprogrammingpatterns.com/state.html)

## Advantages and Limitations

### Advantages

- **Clarity**: FSMs provide a clear, visualizable model for sequential logic.
- **Predictability**: Well-defined transitions ensure predictable behavior.
- **Modularity**: Complex systems can be decomposed into smaller, easier-to-maintain FSMs.
- **Determinism**: Particularly in DFAs, behavior is always unambiguous.
- **Efficiency**: FSMs are resource-efficient, requiring minimal hardware or software overhead.

### Limitations

- **Expressiveness**: FSMs can only model regular languages; they cannot handle problems needing unbounded memory (e.g., nested parentheses in programming languages).
- **State Explosion**: Large systems can quickly become unmanageable without decomposition.
- **Memory**: FSMs have no memory beyond the current state; to track history or counters, external variables or more complex models are needed.

## Key Terms Glossary

- **Finite State Machine (FSM)**: A model describing a system with a finite set of states and transition rules.
- **State**: A unique configuration or mode of operation.
- **Transition**: The rule/process moving the FSM from one state to another based on an input.
- **Input**: External event or signal prompting a transition.
- **Output**: Action or signal produced by the FSM.
- **State Diagram**: A graphical representation of states and transitions.
- **Deterministic FSM (DFA)**: FSM where each state/input pair leads to exactly one next state.
- **Non-Deterministic FSM (NFA)**: FSM where a state/input pair may lead to multiple possible next states.
- **Mealy Machine**: Output depends on current state and input.
- **Moore Machine**: Output depends only on current state.
- **Transition Table**: Tabular format showing all transitions and outputs.

## References

- [BLT Inc: A Guide to Finite State Machines](https://bltinc.com/2024/11/04/finite-state-machines-guide/)
- [SiliconVeda: FSM Comprehensive Guide](https://www.siliconveda.com/2024/10/finite-state-machine-fsm-comprehensive.html)
- [Game Programming Patterns: State](https://gameprogrammingpatterns.com/state.html)
- [Software Engineering Stack Exchange: FSM Examples](https://softwareengineering.stackexchange.com/questions/47806/examples-of-finite-state-machines)
- [Quora: Real-world FSM Examples and Code](https://www.quora.com/What-are-some-real-world-examples-of-where-finite-state-machines-can-be-used-Can-you-provide-any-code-examples)

This glossary and guide distills advanced FSM knowledge, practical design strategies, and real-world use cases directly from leading technical sources. For further study, consult the linked references and explore state diagrams, code examples, and design patterns in each field.

