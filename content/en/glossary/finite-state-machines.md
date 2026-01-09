---
title: Finite State Machines (FSM)
lastmod: 2025-12-18
date: 2025-12-18
translationKey: finite-state-machines-fsm
description: "A computational model that represents systems with a fixed number of states and predefined rules for switching between them based on inputs. Used to create predictable behavior in software, games, and devices."
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

<strong>Core Principles:</strong>- System exists in exactly one state at any given time
- Inputs trigger transitions between states
- Rules define valid state changes
- Outputs may depend on states and/or inputs

<strong>Analogy:</strong>A door lock operates as a simple FSM with two states: `locked` and `unlocked`. A correct key transitions the lock from `locked` to `unlocked`, while an incorrect key maintains the current state. The lock's behavior is entirely predictable based on its current state and input received.

## Core Components

### States

<strong>Definition:</strong>Distinct configurations or modes in which a system can exist.

<strong>Characteristics:</strong>- System occupies exactly one state at any moment
- States represent meaningful operational modes
- Each state may have associated outputs or behaviors
- Number of states is finite and predetermined

<strong>Examples:</strong>- <strong>Vending machine states:</strong>Idle, Waiting for Selection, Dispensing Item, Out of Service
- <strong>Network connection states:</strong>Disconnected, Connecting, Connected, Error
- <strong>Game character states:</strong>Idle, Walking, Running, Jumping, Attacking

### Transitions

<strong>Definition:</strong>Rules governing movement from one state to another based on input conditions.

<strong>Key Properties:</strong>- Triggered by specific inputs or events
- Instantaneous (no intermediate states)
- May include guard conditions
- Can trigger actions during execution

<strong>Transition Notation:</strong>```
Current_State + Input → Next_State [/ Action]
```

**Example:**```
Idle + "Insert Coin" → Waiting_for_Selection / "Display Menu"
```

### Inputs and Outputs

| Component | Description | Examples |
|-----------|-------------|----------|
| <strong>Inputs</strong>| External signals triggering transitions | Button presses, sensor readings, timer events, network packets |
| <strong>Outputs</strong>| Actions or signals produced by FSM | Display updates, motor controls, network responses, status indicators |

<strong>Output Types:</strong>- <strong>Mealy Machine:</strong>Outputs depend on current state AND input
- <strong>Moore Machine:</strong>Outputs depend ONLY on current state

### State Diagrams

State diagrams provide visual representation of FSM structure and behavior.

<strong>Visual Elements:</strong>- <strong>Circles/Nodes:</strong>Represent states
- <strong>Arrows/Edges:</strong>Represent transitions
- <strong>Labels:</strong>Show triggering inputs and outputs
- <strong>Initial State:</strong>Arrow from nowhere pointing to starting state
- <strong>Final States:</strong>Double circles (in accepting automata)

<strong>Example State Diagram Elements:</strong>```
[State A] --input/output--> [State B]
    |                           |
    +--input/output-------------+
```

## Types of Finite State Machines

### 1. Deterministic Finite State Machine (DFSM/DFA)

**Definition:**FSM where each state/input combination leads to exactly one next state—no ambiguity exists.

**Characteristics:**- Predictable behavior guaranteed
- Single transition per state/input pair
- Easier to implement and debug
- Lower computational complexity

**Applications:**- Digital circuit design
- Lexical analyzers in compilers
- Protocol implementations
- Password validation systems

**Example - Binary String Validator:**```
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

<strong>Definition:</strong>FSM allowing multiple possible next states for the same state/input combination.

<strong>Key Features:</strong>- Multiple transition options per state/input
- Epsilon (ε) transitions possible (state changes without input)
- Useful for pattern matching
- Can be converted to equivalent DFA

<strong>Advantages:</strong>- More compact representation
- Easier initial design for complex patterns
- Natural for certain problem types

<strong>Applications:</strong>- Regular expression engines
- Pattern matching algorithms
- Parallel state exploration
- Ambiguous language recognition

### 3. Mealy Machine

<strong>Output Generation:</strong>Based on current state AND input.

<strong>Characteristics:</strong>| Aspect | Details |
|--------|---------|
| Response Time | Immediate (outputs change with inputs) |
| State Count | Generally fewer states needed |
| Output Stability | Less stable (changes during transitions) |
| Hardware | More combinational logic required |

<strong>Example - Turnstile Controller:</strong>```
State: Locked
Input: Coin → Output: Unlock → Next State: Unlocked

State: Unlocked  
Input: Push → Output: Lock → Next State: Locked
```

**Use Cases:**- Systems requiring immediate responses
- Communication protocols
- Control systems with feedback
- Event-driven applications

### 4. Moore Machine

**Output Generation:**Based ONLY on current state.

**Characteristics:**| Aspect | Details |
|--------|---------|
| Response Time | One cycle delay (outputs change on state transitions) |
| State Count | Generally more states needed |
| Output Stability | Highly stable (constant within states) |
| Hardware | More sequential logic (flip-flops) |

**Example - Traffic Light Controller:**```
State: Red → Output: STOP (constant)
State: Yellow → Output: CAUTION (constant)
State: Green → Output: GO (constant)
```

<strong>Use Cases:</strong>- Sequential systems
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

<strong>1. State Identification</strong>- List all distinct operational modes
- Define meaningful state names
- Identify initial and final states (if applicable)
- Ensure states are mutually exclusive

<strong>2. Input Definition</strong>- Enumerate all possible inputs/events
- Define input alphabet or event types
- Consider edge cases and invalid inputs
- Document input format and ranges

<strong>3. Transition Mapping</strong>```
For each state:
  For each possible input:
    Define next_state
    Define action (if any)
    Add guard conditions (if needed)
```

**4. State Table Creation**| Current State | Input | Next State | Output/Action |
|--------------|-------|------------|---------------|
| State_A | Input_1 | State_B | Action_1 |
| State_A | Input_2 | State_A | Action_2 |
| State_B | Input_1 | State_C | Action_3 |

**5. Implementation**- Choose representation (table, switch-case, state pattern)
- Initialize to starting state
- Implement transition logic
- Add output generation
- Handle edge cases and errors

**6. Execution Cycle**```
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

<strong>States:</strong>Green, Yellow, Red  
<strong>Trigger:</strong>Timer expiration

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

<strong>Task:</strong>Validate strings ending with "01"

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

<strong>UI Event Handling</strong>- Widget states: Idle, Hovered, Focused, Pressed, Dragging
- Transitions based on mouse/touch events
- Output: Visual feedback, callbacks

<strong>Network Protocols</strong>- TCP connection states: CLOSED, LISTEN, SYN_SENT, ESTABLISHED, FIN_WAIT
- Transitions on packet reception
- Ensures reliable communication

<strong>Compiler Lexical Analysis</strong>- Token recognition through state traversal
- Each character input triggers transitions
- Accept states indicate valid tokens

### Hardware and Digital Systems

<strong>Application Areas:</strong>| Domain | FSM Usage |
|--------|-----------|
| <strong>Digital Circuits</strong>| Counters, timers, sequence detectors, control units |
| <strong>Embedded Systems</strong>| Device controllers, power management, mode switching |
| <strong>FPGA/ASIC Design</strong>| Protocol controllers, data path control, synchronization |
| <strong>Microcontrollers</strong>| Interrupt handling, peripheral management, state monitoring |

<strong>Example - Elevator Controller:</strong>```
States: Idle, Moving_Up, Moving_Down, Door_Open
Inputs: Call_Button, Floor_Sensor, Door_Sensor, Timer
Outputs: Motor_Control, Door_Control, Display
```

### AI, Chatbots, and Automation

**Conversational AI States:**- Greeting → Information Gathering → Processing → Response → Follow-up → Closing
- Transitions based on user inputs and intent recognition
- Context preservation across states

**Smart Home Automation:**```
Security System FSM:
States: Disarmed, Armed_Stay, Armed_Away, Alarm_Triggered
Inputs: User_Command, Sensor_Events, Timer
Outputs: Status_Display, Alarm_Sound, Notifications
```

<strong>Process Automation:</strong>- Workflow states representing process stages
- Transitions on task completion or approval
- Integration with business systems

### Game Development

<strong>Character AI Behaviors:</strong>| State | Triggers | Actions |
|-------|----------|---------|
| <strong>Idle</strong>| No player detected | Patrol waypoints |
| <strong>Alert</strong>| Player spotted | Face player, play alert sound |
| <strong>Chase</strong>| Player in range | Move toward player |
| <strong>Attack</strong>| In attack range | Execute attack animation |
| <strong>Retreat</strong>| Health low | Move away, seek cover |

<strong>Game Flow Management:</strong>```
Menu → Loading → Playing ⇄ Paused → Game_Over → Menu
```

## Advanced FSM Concepts

### Hierarchical State Machines (HSM)

**Concept:**States contain nested sub-FSMs, enabling complex behavior composition.

**Benefits:**- Reduced state explosion
- Better organization of complex systems
- Reusable sub-behaviors
- Clearer logical structure

**Example Structure:**```
[Combat_Mode]
  ├─ [Attacking]
  │    ├─ Melee_Attack
  │    └─ Ranged_Attack
  └─ [Defending]
       ├─ Block
       └─ Dodge
```

### Parallel State Machines

<strong>Concept:</strong>Multiple independent FSMs running simultaneously.

<strong>Use Cases:</strong>- Separate concerns (e.g., movement FSM + animation FSM)
- Independent subsystem control
- Concurrent behavior modeling

<strong>Example - Game Character:</strong>```
Movement_FSM: Standing, Walking, Running, Jumping
Animation_FSM: Idle_Anim, Walk_Anim, Run_Anim, Jump_Anim
Combat_FSM: Unarmed, Armed, Attacking, Reloading
```

### State Explosion Problem

**Challenge:**State count grows exponentially with system complexity.

**Mitigation Strategies:**| Strategy | Description |
|----------|-------------|
| **Hierarchical FSM**| Group related states into super-states |
| **State Variables**| Use variables to capture dimensions independently |
| **Parallel FSMs**| Separate orthogonal concerns |
| **State Minimization**| Merge equivalent states |
| **Guard Conditions**| Use conditionals instead of separate states |

### State Pattern (OOP)

**Concept:**Encapsulate state-specific behavior in separate classes.

**Structure:**```python
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

<strong>Benefits:</strong>- Open/closed principle compliance
- Easy to add new states
- Clear separation of concerns
- Eliminates complex conditionals

## Advantages and Limitations

### Advantages

| Benefit | Description |
|---------|-------------|
| <strong>Clarity</strong>| Visual and conceptual clarity of system behavior |
| <strong>Predictability</strong>| Deterministic behavior with defined transitions |
| <strong>Maintainability</strong>| Easy to modify and extend |
| <strong>Testability</strong>| Clear test cases for each state/transition |
| <strong>Documentation</strong>| State diagrams serve as living documentation |
| <strong>Efficiency</strong>| Minimal computational overhead |
| <strong>Verification</strong>| Formal methods applicable for correctness proofs |

### Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| <strong>State Explosion</strong>| Too many states become unmanageable | Use hierarchical or parallel FSMs |
| <strong>Limited Memory</strong>| No memory beyond current state | Add state variables or use pushdown automata |
| <strong>Expressiveness</strong>| Can only model regular languages | Use more powerful models (Turing machines) for complex grammars |
| <strong>Scalability</strong>| Large systems become complex | Decompose into smaller FSMs |

<strong>Not Suitable For:</strong>- Problems requiring unbounded memory (e.g., matching nested parentheses)
- Systems with continuous state spaces
- Highly adaptive or learning systems
- Problems outside regular language class

## Best Practices

### Design Guidelines

<strong>State Design:</strong>- Keep states meaningful and distinct
- Minimize state count while maintaining clarity
- Name states descriptively (verb-noun or adjective-noun)
- Ensure mutual exclusivity

<strong>Transition Design:</strong>- Make transitions explicit and well-defined
- Handle all inputs for all states (or define error states)
- Avoid circular dependencies without progress
- Document guard conditions clearly

<strong>Implementation:</strong>- Choose appropriate representation (table, switch, pattern)
- Validate inputs before processing
- Log state transitions for debugging
- Implement timeout mechanisms where needed

### Testing Strategies

<strong>Coverage Types:</strong>| Test Type | Target |
|-----------|--------|
| <strong>State Coverage</strong>| Exercise every state at least once |
| <strong>Transition Coverage</strong>| Test every transition |
| <strong>Path Coverage</strong>| Test common state sequences |
| <strong>Boundary Testing</strong>| Test edge cases and limits |
| <strong>Error Handling</strong>| Invalid inputs and unexpected conditions |

## Key Terminology

- <strong>Finite State Machine (FSM):</strong>Computational model with finite states and defined transitions
- <strong>State:</strong>Distinct configuration or mode of operation
- <strong>Transition:</strong>Movement from one state to another based on input
- <strong>Input Alphabet:</strong>Set of all possible inputs
- <strong>Output:</strong>Actions or signals produced by FSM
- <strong>Deterministic FSM:</strong>Each state/input pair has exactly one next state
- <strong>Non-Deterministic FSM:</strong>State/input pair may have multiple next states
- <strong>Mealy Machine:</strong>Output depends on state and input
- <strong>Moore Machine:</strong>Output depends only on state
- <strong>State Diagram:</strong>Graphical representation of FSM
- <strong>Transition Table:</strong>Tabular representation of all transitions
- <strong>Accept State:</strong>State indicating valid input sequence (in automata)

## References


1. BLT Inc. (2024). A Guide to Finite State Machines. BLT Inc.

2. SiliconVeda. (2024). FSM Comprehensive Guide. SiliconVeda.

3. Game Programming Patterns. (n.d.). State. Game Programming Patterns.

4. Software Engineering Stack Exchange. (n.d.). FSM Examples. Stack Exchange.

5. Quora. (n.d.). Real-world FSM Examples and Code. Quora.
