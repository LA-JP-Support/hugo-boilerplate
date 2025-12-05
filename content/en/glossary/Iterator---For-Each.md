---
title: "Iterator / For-Each"
translationKey: "iterator-for-each"
description: "An iterator or for-each construct processes items in a list or collection one by one, enabling actions like reading, updating, or automating tasks for each element."
keywords: ["iterator", "for-each loop", "collection processing", "workflow automation", "programming concepts"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## What Is an Iterator / For-Each?

**Iterator:**  
An iterator is an object or logic block that enables traversing through a collection (such as a list, array, or map), processing each item one at a time. Iterators are central to handling collections in nearly all modern programming languages. They provide a standardized way to access each item sequentially, regardless of how the collection is structured in memory. For example, in Java, the [Iterator](https://www.w3schools.com/java/java_iterator.asp) interface allows you to loop through `ArrayList`, `HashSet`, and other collections without directly handling indices or internal data structure details.

**For-Each Construct:**  
A for-each construct (also called a for-each loop, foreach statement, or iterator block) executes a block of code for every item in a collection, abstracting away the details of how iteration occurs. Many languages provide this as a built-in statement—`for ... of` in JavaScript, `foreach` in C#, and the enhanced `for` loop in Java. These constructs are also a staple in workflow automation tools, like Relay.app, where an iterator block processes each item in a list step-by-step ([Relay.app Docs](https://docs.relay.app/flow-control/iterators)).

> **Key Point:**  
> Iterators and for-each constructs simplify collection processing, reduce likelihood of off-by-one errors, and make code more readable and maintainable. They are foundational to both programming and workflow automation.

## Technical Explanation of Iterators

### What Makes an Iterator?

An iterator must provide a mechanism to return the next item in a sequence and signal when no more items remain. This is formalized as an *iterator protocol* in many languages:

- **Iterator Protocol:**  
  The object must implement a specific interface, such as a `next()` method (JavaScript, Python, Java) or `MoveNext()`/`Current` (C#).
- **Consumption:**  
  Iterators are typically *consumed* as you process them—once you reach the end, you can't reset or reuse the same iterator object; you must create a new one if you want to traverse the collection again.

#### Language Protocols Overview

- **Python:**  
  Objects that implement the `__iter__()` and `__next__()` methods conform to the iterator protocol. A list or other collection is *iterable*; calling `iter()` on it produces an iterator ([GeeksforGeeks](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/)).  
- **JavaScript:**  
  Objects that implement the `next()` method, returning `{value, done}`, are iterators by the [Iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterators). Many built-in types (Array, String, Set, Map) are iterable, and the `[Symbol.iterator]()` method produces an iterator.  
- **Java:**  
  Objects implementing the `Iterator<E>` interface provide `hasNext()`, `next()`, and optionally `remove()` ([W3Schools](https://www.w3schools.com/java/java_iterator.asp)).  
- **C#:**  
  The [IEnumerator](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerator) and [IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable) interfaces define the protocol.  
- **Workflow Automation (Relay.app):**  
  Iterator blocks visually process each item in a list; the tool handles the iteration logic ([Relay.app Docs](https://docs.relay.app/flow-control/iterators)).

### Iterator vs Iterable

- **Iterable:**  
  An object that can produce an iterator (e.g., a list, array, set).  
- **Iterator:**  
  The object that actually delivers one item at a time from the iterable.

*In Python, every iterator is also an iterable, but not every iterable is an iterator* ([GeeksforGeeks](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/)).

## For-Each Constructs: Purpose and Use

A for-each loop or block allows automatic processing of every item in a collection, one at a time, without manual management of loop counters or indexes. This makes code safer and more readable.

### Advantages

- **Error Reduction:**  
  For-each loops eliminate common bugs like off-by-one errors and accidental skipping of elements.
- **Code Clarity:**  
  Code is often shorter, easier to read, and communicates intent more directly.
- **Safety:**  
  For-each works on any iterable/collection object, reducing coupling to the collection's underlying structure.

For example, in C#, the `foreach` statement works seamlessly with any type that implements `IEnumerable<T>` ([Stackify](https://stackify.com/c-foreach-definition-and-best-practices/)). In JavaScript, the `for...of` loop iterates over all elements of an iterable object ([MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)).

## Iterators and For-Each in Major Programming Languages

### Python

#### Technical Explanation

In Python, an *iterable* is any object that can be passed to `iter()` to obtain an iterator. The iterator then returns items one at a time via `next()`. Lists, tuples, dicts, sets, strings, and many other types are iterable.

- **Iterables:** Implement `__iter__()`, which must return an iterator object.
- **Iterators:** Implement both `__iter__()` (returns self) and `__next__()` (returns next item or raises `StopIteration`).

[GeeksforGeeks: Python Iterables vs Iterators](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/)

#### Using Iterators: Step-by-Step

```python
my_list = [10, 20, 30]
my_iter = iter(my_list)
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
# Next call raises StopIteration
```

The `for` loop implicitly calls `iter()` on the collection and repeatedly calls `next()` on the resulting iterator.

#### Creating a Custom Iterator

```python
class Counter:
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        if self.count < 5:
            self.count += 1
            return self.count
        else:
            raise StopIteration

for number in Counter():
    print(number)  # Output: 1 2 3 4 5
```

#### Practical Notes

- **Best Practice:**  
  Use for loops for most iteration tasks.
- **Pitfall:**  
  Modifying a collection during iteration can cause errors or unexpected results.
  [GeeksforGeeks: Python Iterables vs Iterators](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/)

### JavaScript

#### Technical Explanation

JavaScript supports both built-in and custom iterators. Built-in types (Array, String, Set, Map) are iterable and return iterators via their `[Symbol.iterator]()` method. Iterators must implement the [Iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterators):

- `next()` returns `{ value, done }`
  - `value`: Next value in sequence
  - `done`: Boolean, true if the sequence is finished

#### Using Iterators: Step-by-Step

```javascript
const arr = [1, 2, 3];
const iter = arr[Symbol.iterator]();
console.log(iter.next()); // { value: 1, done: false }
console.log(iter.next()); // { value: 2, done: false }
console.log(iter.next()); // { value: 3, done: false }
console.log(iter.next()); // { value: undefined, done: true }
```

#### For-each Loop (`for...of`)

```javascript
for (const item of arr) {
    console.log(item);
}
```

#### Creating Custom Iterators

```javascript
function makeRangeIterator(start = 0, end = 5, step = 1) {
  let nextIndex = start;
  return {
    next: function() {
      if (nextIndex < end) {
        return { value: nextIndex++, done: false };
      }
      return { done: true };
    }
  };
}

const rangeIter = makeRangeIterator(1, 4);
console.log(rangeIter.next().value); // 1
console.log(rangeIter.next().value); // 2
console.log(rangeIter.next().value); // 3
console.log(rangeIter.next().done);  // true
```

#### Generator Functions

```javascript
function* genNumbers() {
  yield 1;
  yield 2;
  yield 3;
}
for (const num of genNumbers()) {
  console.log(num); // 1 2 3
}
```

#### Practical Notes

- **Pitfall:**  
  Iterators are usually consumed after one complete loop.
- **Best Practice:**  
  Use `for...of` for clean and idiomatic iteration.
  [MDN: Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)

### Java

#### Technical Explanation

Java provides the `Iterator<E>` interface for traversing collections ([W3Schools](https://www.w3schools.com/java/java_iterator.asp)). The interface specifies three primary methods:

- `hasNext()`: Returns true if there are more elements
- `next()`: Returns the next element
- `remove()`: Removes the last element returned by the iterator (optional)

#### Using Iterators: Step-by-Step

```java
import java.util.ArrayList;
import java.util.Iterator;

ArrayList<String> cars = new ArrayList<>();
cars.add("Volvo");
cars.add("BMW");
cars.add("Ford");
cars.add("Mazda");

Iterator<String> it = cars.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

#### For-each Loop (Preferred)

```java
for (String car : cars) {
    System.out.println(car);
}
```

#### Removing Elements During Iteration

```java
Iterator<Integer> it = numbers.iterator();
while (it.hasNext()) {
    if (it.next() < 10) {
        it.remove();
    }
}
```
> Use `remove()` from the iterator, not from the collection, during iteration to avoid `ConcurrentModificationException`. ([W3Schools](https://www.w3schools.com/java/java_iterator.asp))

#### Practical Notes

- **Best Practice:**  
  Use for-each for read-only iteration; use `Iterator` directly only when you need to remove elements while iterating.
- **Pitfall:**  
  Modifying the collection directly during iteration can cause exceptions.

### C#

#### Technical Explanation

C# provides the `foreach` statement to iterate over collections. Behind the scenes, it uses the [IEnumerator](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerator) interface, which supplies the `MoveNext()`, `Current`, and `Reset()` methods.

- Any type that implements `IEnumerable` or `IEnumerable<T>` can be used with `foreach`.
- `foreach` handles all the iteration logic automatically.

#### Using For-Each: Step-by-Step

```csharp
List<string> colors = new List<string> { "Red", "Green", "Blue" };
foreach (var color in colors)
{
    Console.WriteLine(color);
}
```

#### Manual Iteration (Less Common)

```csharp
var enumerator = colors.GetEnumerator();
while (enumerator.MoveNext())
{
    Console.WriteLine(enumerator.Current);
}
```

#### Custom Iterator Using `yield return`

```csharp
IEnumerable<int> GetNumbers()
{
    for (int i = 0; i < 3; i++)
        yield return i;
}
foreach (var n in GetNumbers())
{
    Console.WriteLine(n); // 0 1 2
}
```

#### Asynchronous Iterators

C# supports asynchronous iteration with `await foreach` ([Microsoft Learn - Asynchronous streams](https://learn.microsoft.com/en-us/dotnet/csharp/iterators)).

```csharp
await foreach (var item in asyncSequence)
{
    // process item
}
```

#### Practical Notes

- **Best Practice:**  
  Use `foreach` for readability and safety unless you need to modify the collection or require the index.
- **Pitfall:**  
  Direct modification of a collection during `foreach` iteration is not allowed.
  [Stackify: C# foreach definition and best practices](https://stackify.com/c-foreach-definition-and-best-practices/)

### Workflow Automation Platforms (Relay.app)

#### Technical Explanation

Workflow automation platforms such as Relay.app provide *iterator* or *for-each* blocks to process lists of items (like rows, attachments, or emails) in sequence. These blocks let you define actions to perform on each item without writing code.

#### Using Iterators in Relay.app: Step-by-Step

1. **Add an Iterator Block:**  
   - Select 'Iterator' from the Flow Control menu ([Relay.app Docs](https://docs.relay.app/flow-control/iterators)).
2. **Select the List to Process:**  
   - Choose the output list from a previous step (e.g., a list of spreadsheet rows).
3. **Configure Actions:**  
   - Inside the iterator, add steps to define what should happen for each item (e.g., send email, update a record).
4. **Use Current Item Data:**  

> **Tip:**  
> Iterator blocks allow for visual, no-code processing of collections, ideal for automating repetitive tasks in workflows.

#### Practical Notes

- **Best Practice:**  
  Place all actions that should happen per item inside the iterator block.
- **Pitfall:**  
  Avoid modifying the underlying list during iteration.
  [Relay.app Docs: Looping (Iterators)](https://docs.relay.app/flow-control/iterators)

## Comparison: Iterator vs Iterable, For vs For-Each

| Concept        | Description                                                                               | When to Use                               |
|----------------|------------------------------------------------------------------------------------------|-------------------------------------------|
| **Iterator**   | Object that produces items from a collection one by one                                  | When you need fine control of iteration   |
| **Iterable**   | Object that can return an iterator (e.g., lists, arrays, sets)                           | When you want to loop using for-each      |
| **For Loop**   | Classic loop with control over indexes, conditions, and increments                       | When you need index access or custom steps|
| **For-Each**   | Simplified loop that processes every item in a collection, hides index details            | When you just want to process items       |

**Key Differences:**

- For-each does not expose the current index directly.
- For-each is safer for read-only operations; for loops are needed for custom step sizes, skipping, or reverse order.
- Some languages allow removal of items during iteration (Java's `Iterator.remove()`), others do not (`foreach` in C#).

## Common Pitfalls, Best Practices, and Special Features

### Common Pitfalls

- **Modifying the collection during iteration** can cause errors or unexpected behavior (ConcurrentModificationException in Java, runtime error in C#).
- **Iterators are consumed:**  
  Once finished, you can't restart them without creating a new one.
- **For-each does not provide index:**  
  Use a `for` loop if you need the position.
- **Infinite Iteration:**  
  Custom iterators should raise/return a stop condition (`StopIteration` in Python).

### Best Practices

- Use for-each loops for simple, read-only processing.
- Use iterator methods or `yield` (Python, C#, JavaScript) for custom sequences.
- In workflow automation, keep all per-item actions inside the iterator block.

### Special Features

- **Asynchronous Iteration:**  
  Supported in C# (`await foreach`) and JavaScript (async iterators and `for await...of`).
- **Removing Items:**  
  Only supported in certain languages (e.g., Java's `Iterator.remove()`).

## Use Cases and Examples

### Processing Spreadsheet Rows

- **Python:**  
  ```python
  for row in spreadsheet_rows:
      process(row)
  ```
- **Relay.app:**  
  - Iterator block processes each row for data extraction, notification, etc. ([Relay.app Docs](https://docs.relay
