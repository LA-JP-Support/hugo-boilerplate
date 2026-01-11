---
title: Finite State Machines (FSM)
lastmod: 2025-12-18
date: 2025-12-18
translationKey: finite-state-machines-fsm
description: "A computational model that represents a system with a fixed number of states and rules for switching between them based on inputs. Used to design predictable behavior in software, games, and devices."
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

A finite state machine (FSM) is a computational model consisting of a finite number of states, transitions between those states, and rules determining state changes based on inputs. FSMs provide a mathematical framework for modeling sequential logic in systems where behavior depends on event sequences or specific conditions.

**Core Principles:**
- System exists in exactly one state at any given time
- Inputs trigger transitions between states
- Rules define valid state changes
- Outputs may depend on states and/or inputs

**Analogy:**  
A door lock operates as a simple FSM with two states: `locked` and `unlocked`. A correct key transitions the lock from `locked` to `unlocked`, while an incorrect key maintains the current state. The lock's behavior is entirely predictable based on its current state and input received.

## Core Components

### States

**Definition:** Distinct configurations or modes in which a system can exist.

**Characteristics:**
- System occupies exactly one state at any moment
- States represent meaningful operational modes
- Each state may have associated outputs or behaviors
- Number of states is finite and predetermined

**Examples:**
- **Vending machine states:** Idle, Waiting for Selection, Dispensing Item, Out of Service
- **Network connection states:** Disconnected, Connecting, Connected, Error
- **Game character states:** Idle, Walking, Running, Jumping, Attacking

### Transitions

**Definition:** Rules governing movement from one state to another based on input conditions.

**Key Properties:**
- Triggered by specific inputs or events
- Instantaneous (no intermediate states)
- May include guard conditions
- Can trigger actions during execution

**Transition Notation:**
```
Current_State + Input → Next_State [/ Action]
```

**Example:**
```
Idle + "Insert Coin" → Waiting_for_Selection / "Display Menu"
```

### Inputs and Outputs

| Component | Description | Examples |
|-----------|-------------|----------|
| **Inputs** | External signals triggering transitions | Button presses, sensor readings, timer events, network packets |
| **Outputs** | Actions or signals produced by FSM | Display updates, motor controls, network responses, status indicators |

**Output Types:**
- **Mealy Machine:** Outputs depend on current state AND input
- **Moore Machine:** Outputs depend ONLY on current state

### State Diagrams

State diagrams provide visual representation of FSM structure and behavior.

**Visual Elements:**
- **Circles/Nodes:** Represent states
- **Arrows/Edges:** Represent transitions
- **Labels:** Show triggering inputs and outputs
- **Initial State:** Arrow from nowhere pointing to starting state
- **Final States:** Double circles (in accepting automata)

**Example State Diagram Elements:**
```
[State A] --input/output--> [State B]
    |                           |
    +--input/output-------------+
```

## Types of Finite State Machines

### 1. Deterministic Finite State Machine (DFSM/DFA)

**Definition:** FSM where each state/input combination leads to exactly one next state—no ambiguity exists.

**Characteristics:**
- Predictable behavior guaranteed
- Single transition per state/input pair
- Easier to implement and debug
- Lower computational complexity

**Applications:**
- Digital circuit design
- Lexical analyzers in compilers
- Protocol implementations
- Password validation systems

**Example - Binary String Validator:**
```
States: {q0, q1}
Input alphabet: {0, 1}
Transitions:
  q0 + 0 → q0
  q0 + 1 → q1
  q1 + 0 → q0
  q1 + 1 → q1
Accept: q0 (strings with even number of 1s)
```

### 2. Non-Deterministic Finite State Machine (NDFSM/NFA)

**Definition:** FSM allowing multiple possible next states for the same state/input combination.

**Key Features:**
- Multiple transition options per state/input
- Epsilon (ε) transitions possible (state changes without input)
- Useful for pattern matching
- Can be converted to equivalent DFA

**Advantages:**
- More compact representation
- Easier initial design for complex patterns
- Natural for certain problem types

**Applications:**
- Regular expression engines
- Pattern matching algorithms
- Parallel state exploration
- Ambiguous language recognition

### 3. Mealy Machine

**Output Generation:** Based on current state AND input.

**Characteristics:**

| Aspect | Details |
|--------|---------|
| Response Time | Immediate (outputs change with inputs) |
| State Count | Generally fewer states needed |
| Output Stability | Less stable (changes during transitions) |
| Hardware | More combinational logic required |

**Example - Turnstile Controller:**
```
State: Locked
Input: Coin → Output: Unlock → Next State: Unlocked

State: Unlocked  
Input: Push → Output: Lock → Next State: Locked
```

**Use Cases:**
- Systems requiring immediate responses
- Communication protocols
- Control systems with feedback
- Event-driven applications

### 4. Moore Machine

**Output Generation:** Based ONLY on current state.

**Characteristics:**

| Aspect | Details |
|--------|---------|
| Response Time | One cycle delay (outputs change on state transitions) |
| State Count | Generally more states needed |
| Output Stability | Highly stable (constant within states) |
| Hardware | More sequential logic (flip-flops) |

**Example - Traffic Light Controller:**
```
State: Red → Output: STOP (constant)
State: Yellow → Output: CAUTION (constant)
State: Green → Output: GO (constant)
```

**Use Cases:**
- Sequential systems
- Safety-critical applications
- Timing-sensitive circuits
- Systems prioritizing output stability

### Mealy vs. Moore Comparison

| Feature | Mealy Machine | Moore Machine |
|---------|--------------|---------------|
| Output depends on | State + Input | State only |
| Response time | Immediate | Next clock cycle |
| Number of states | Fewer | More (typically) |
| Output timing | Asynchronous | Synchronous |
| Glitch susceptibility | Higher | Lower |
| Design complexity | Logic complexity | More states |
| Best for | Fast response | Stable outputs |

## How FSMs Work: Step-by-Step Process

### FSM Construction Workflow

**1. State Identification**
- List all distinct operational modes
- Define meaningful state names
- Identify initial and final states (if applicable)
- Ensure states are mutually exclusive

**2. Input Definition**
- Enumerate all possible inputs/events
- Define input alphabet or event types
- Consider edge cases and invalid inputs
- Document input format and ranges

**3. Transition Mapping**
```
For each state:
  For each possible input:
    Define next_state
    Define action (if any)
    Add guard conditions (if needed)
```

**4. State Table Creation**

| Current State | Input | Next State | Output/Action |
|--------------|-------|------------|---------------|
| State_A | Input_1 | State_B | Action_1 |
| State_A | Input_2 | State_A | Action_2 |
| State_B | Input_1 | State_C | Action_3 |

**5. Implementation**
- Choose representation (table, switch-case, state pattern)
- Initialize to starting state
- Implement transition logic
- Add output generation
- Handle edge cases and errors

**6. Execution Cycle**
```
Loop:
  1. Wait for input
  2. Look up transition: current_state + input
  3. Execute transition action (if any)
  4. Update current_state to next_state
  5. Generate output (Moore: state-based, Mealy: state+input)
  6. Repeat
```

## Implementation Examples

### Example 1: Traffic Light Controller (Python)

**States:** Green, Yellow, Red  
**Trigger:** Timer expiration

```python
class TrafficLight:
    def __init__(self):
        self.state = 'Green'
        self.state_durations = {
            'Green': 30,
            'Yellow': 5,
            'Red': 25
        }
    
    def transition_table(self):
        return {
            'Green': 'Yellow',
            'Yellow': 'Red',
            'Red': 'Green'
        }
    
    def on_timer(self):
        transitions = self.transition_table()
        self.state = transitions[self.state]
        print(f'Light: {self.state}')
        return self.state_durations[self.state]

# Usage
light = TrafficLight()
for _ in range(6):
    duration = light.on_timer()
    print(f'Duration: {duration} seconds\n')
```

### Example 2: String Parser (JavaScript)

**Task:** Validate strings ending with "01"

```javascript
class StringParser {
  constructor() {
    this.state = 'start';
  }
  
  transition(input) {
    const table = {
      'start': {'0': 'got_0', '1': 'start'},
      'got_0': {'0': 'got_0', '1': 'got_01'},
      'got_01': {'0': 'got_0', '1': 'start'}
    };
    
    if (table[this.state] && table[this.state][input]) {
      this.state = table[this.state][input];
      return true;
    }
    return false;
  }
  
  isValid() {
    return this.state === 'got_01';
  }
  
  reset() {
    this.state = 'start';
  }
}

// Test
const parser = new StringParser();
'10101'.split('').forEach(bit => parser.transition(bit));
console.log(parser.isValid()); // true
```

### Example 3: Game Character FSM (C++)

```cpp
enum State {
    STATE_STANDING,
    STATE_JUMPING,
    STATE_DUCKING,
    STATE_DIVING
};

enum Input {
    PRESS_B,
    PRESS_DOWN,
    RELEASE_DOWN
};

class Character {
private:
    State state_;
    
public:
    Character() : state_(STATE_STANDING) {}
    
    void handleInput(Input input) {
        switch (state_) {
            case STATE_STANDING:
                if (input == PRESS_B) {
                    state_ = STATE_JUMPING;
                    yVelocity_ = JUMP_VELOCITY;
                } else if (input == PRESS_DOWN) {
                    state_ = STATE_DUCKING;
                }
                break;
                
            case STATE_JUMPING:
                if (input == PRESS_DOWN) {
                    state_ = STATE_DIVING;
                    yVelocity_ *= 2;
                }
                break;
                
            case STATE_DUCKING:
                if (input == RELEASE_DOWN) {
                    state_ = STATE_STANDING;
                }
                break;
                
            case STATE_DIVING:
                // Can only transition on landing
                break;
        }
    }
    
    void update() {
        switch (state_) {
            case STATE_JUMPING:
            case STATE_DIVING:
                yVelocity_ += GRAVITY;
                yPosition_ += yVelocity_;
                if (yPosition_ <= 0) {
                    state_ = STATE_STANDING;
                    yPosition_ = 0;
                }
                break;
        }
    }
};
```

## Real-World Applications

### Software Engineering

**UI Event Handling**
- Widget states: Idle, Hovered, Focused, Pressed, Dragging
- Transitions based on mouse/touch events
- Output: Visual feedback, callbacks

**Network Protocols**
- TCP connection states: CLOSED, LISTEN, SYN_SENT, ESTABLISHED, FIN_WAIT
- Transitions on packet reception
- Ensures reliable communication

**Compiler Lexical Analysis**
- Token recognition through state traversal
- Each character input triggers transitions
- Accept states indicate valid tokens

### Hardware and Digital Systems

**Application Areas:**

| Domain | FSM Usage |
|--------|-----------|
| **Digital Circuits** | Counters, timers, sequence detectors, control units |
| **Embedded Systems** | Device controllers, power management, mode switching |
| **FPGA/ASIC Design** | Protocol controllers, data path control, synchronization |
| **Microcontrollers** | Interrupt handling, peripheral management, state monitoring |

**Example - Elevator Controller:**
```
States: Idle, Moving_Up, Moving_Down, Door_Open
Inputs: Call_Button, Floor_Sensor, Door_Sensor, Timer
Outputs: Motor_Control, Door_Control, Display
```

### AI, Chatbots, and Automation

**Conversational AI States:**
- Greeting → Information Gathering → Processing → Response → Follow-up → Closing
- Transitions based on user inputs and intent recognition
- Context preservation across states

**Smart Home Automation:**
```
Security System FSM:
States: Disarmed, Armed_Stay, Armed_Away, Alarm_Triggered
Inputs: User_Command, Sensor_Events, Timer
Outputs: Status_Display, Alarm_Sound, Notifications
```

**Process Automation:**
- Workflow states representing process stages
- Transitions on task completion or approval
- Integration with business systems

### Game Development

**Character AI Behaviors:**

| State | Triggers | Actions |
|-------|----------|---------|
| **Idle** | No player detected | Patrol waypoints |
| **Alert** | Player spotted | Face player, play alert sound |
| **Chase** | Player in range | Move toward player |
| **Attack** | In attack range | Execute attack animation |
| **Retreat** | Health low | Move away, seek cover |

**Game Flow Management:**
```
Menu → Loading → Playing ⇄ Paused → Game_Over → Menu
```

## Advanced FSM Concepts

### Hierarchical State Machines (HSM)

**Concept:** States contain nested sub-FSMs, enabling complex behavior composition.

**Benefits:**
- Reduced state explosion
- Better organization of complex systems
- Reusable sub-behaviors
- Clearer logical structure

**Example Structure:**
```
[Combat_Mode]
  ├─ [Attacking]
  │    ├─ Melee_Attack
  │    └─ Ranged_Attack
  └─ [Defending]
       ├─ Block
       └─ Dodge
```

### Parallel State Machines

**Concept:** Multiple independent FSMs running simultaneously.

**Use Cases:**
- Separate concerns (e.g., movement FSM + animation FSM)
- Independent subsystem control
- Concurrent behavior modeling

**Example - Game Character:**
```
Movement_FSM: Standing, Walking, Running, Jumping
Animation_FSM: Idle_Anim, Walk_Anim, Run_Anim, Jump_Anim
Combat_FSM: Unarmed, Armed, Attacking, Reloading
```

### State Explosion Problem

**Challenge:** State count grows exponentially with system complexity.

**Mitigation Strategies:**

| Strategy | Description |
|----------|-------------|
| **Hierarchical FSM** | Group related states into super-states |
| **State Variables** | Use variables to capture dimensions independently |
| **Parallel FSMs** | Separate orthogonal concerns |
| **State Minimization** | Merge equivalent states |
| **Guard Conditions** | Use conditionals instead of separate states |

### State Pattern (OOP)

**Concept:** Encapsulate state-specific behavior in separate classes.

**Structure:**
```python
class State:
    def handle(self, context): pass

class ConcreteStateA(State):
    def handle(self, context):
        # State A behavior
        context.state = ConcreteStateB()

class Context:
    def __init__(self):
        self.state = ConcreteStateA()
    
    def request(self):
        self.state.handle(self)
```

**Benefits:**
- Open/closed principle compliance
- Easy to add new states
- Clear separation of concerns
- Eliminates complex conditionals

## Advantages and Limitations

### Advantages

| Benefit | Description |
|---------|-------------|
| **Clarity** | Visual and conceptual clarity of system behavior |
| **Predictability** | Deterministic behavior with defined transitions |
| **Maintainability** | Easy to modify and extend |
| **Testability** | Clear test cases for each state/transition |
| **Documentation** | State diagrams serve as living documentation |
| **Efficiency** | Minimal computational overhead |
| **Verification** | Formal methods applicable for correctness proofs |

### Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| **State Explosion** | Too many states become unmanageable | Use hierarchical or parallel FSMs |
| **Limited Memory** | No memory beyond current state | Add state variables or use pushdown automata |
| **Expressiveness** | Can only model regular languages | Use more powerful models (Turing machines) for complex grammars |
| **Scalability** | Large systems become complex | Decompose into smaller FSMs |

**Not Suitable For:**
- Problems requiring unbounded memory (e.g., matching nested parentheses)
- Systems with continuous state spaces
- Highly adaptive or learning systems
- Problems outside regular language class

## Best Practices

### Design Guidelines

**State Design:**
- Keep states meaningful and distinct
- Minimize state count while maintaining clarity
- Name states descriptively (verb-noun or adjective-noun)
- Ensure mutual exclusivity

**Transition Design:**
- Make transitions explicit and well-defined
- Handle all inputs for all states (or define error states)
- Avoid circular dependencies without progress
- Document guard conditions clearly

**Implementation:**
- Choose appropriate representation (table, switch, pattern)
- Validate inputs before processing
- Log state transitions for debugging
- Implement timeout mechanisms where needed

### Testing Strategies

**Coverage Types:**

| Test Type | Target |
|-----------|--------|
| **State Coverage** | Exercise every state at least once |
| **Transition Coverage** | Test every transition |
| **Path Coverage** | Test common state sequences |
| **Boundary Testing** | Test edge cases and limits |
| **Error Handling** | Invalid inputs and unexpected conditions |

## Key Terminology

- **Finite State Machine (FSM):** Computational model with finite states and defined transitions
- **State:** Distinct configuration or mode of operation
- **Transition:** Movement from one state to another based on input
- **Input Alphabet:** Set of all possible inputs
- **Output:** Actions or signals produced by FSM
- **Deterministic FSM:** Each state/input pair has exactly one next state
- **Non-Deterministic FSM:** State/input pair may have multiple next states
- **Mealy Machine:** Output depends on state and input
- **Moore Machine:** Output depends only on state
- **State Diagram:** Graphical representation of FSM
- **Transition Table:** Tabular representation of all transitions
- **Accept State:** State indicating valid input sequence (in automata)

## References

- [BLT Inc: A Guide to Finite State Machines](https://bltinc.com/2024/11/04/finite-state-machines-guide/)
- [SiliconVeda: FSM Comprehensive Guide](https://www.siliconveda.com/2024/10/finite-state-machine-fsm-comprehensive.html)
- [Game Programming Patterns: State](https://gameprogrammingpatterns.com/state.html)
- [Software Engineering Stack Exchange: FSM Examples](https://softwareengineering.stackexchange.com/questions/47806/examples-of-finite-state-machines)
- [Quora: Real-world FSM Examples and Code](https://www.quora.com/What-are-some-real-world-examples-of-where-finite-state-machines-can-be-used-Can-you-provide-any-code-examples)
