---
title: Iterator / For-Each
translationKey: iterator-for-each
description: Iterators and For-Each loops are programming features that process items in a list or collection one by one, executing actions on each element.
keywords:
- Iterator
- for-each loop
- collection processing
- programming
- automation
category: Web Development & Design
type: glossary
date: '2025-12-19'
lastmod: 2026-04-02
draft: false
url: /en/glossary/iterator---for-each/
---

## What is an Iterator / For-Each?

**An iterator is a mechanism that checks items in a list (a collection of multiple items) one by one and repeats the same process for each.** A For-Each loop is a language feature that writes this process concisely and is available in virtually all programming languages.

For example, with a list of 100 customers, you would check the 1st, 2nd, 3rd... in order and send an email to each—this type of repetitive processing is where For-Each loops are used.

> **In a nutshell:** A mechanism that automatically repeats the same work on all items in a list.

**Key points:**

- **What it does:** Executes the same processing on each element of a list
- **Why it's needed:** Much more efficient than processing one by one manually, and mistakes decrease
- **Who uses it:** Programmers, automation engineers, data processing specialists

## Why it matters

Without iterators and For-Each loops, programmers would have to manually give instructions to each list element one by one, which is very time-consuming. Additionally, code would need to be rewritten every time the list length changes.

Using a For-Each loop lets you write code like "Whether the list has 100 or 1000 items, it will process automatically." This is the same concept as [workflow automation](Workflow-Automation.md) platforms that automatically adapt as table rows increase.

Also, using iterators correctly reduces bugs. You avoid problems common in manual loops, such as index calculation errors.

## How it works

An iterator is a "mechanism that extracts items from the beginning to the end of a list one by one." It's similar to library staff checking books from a stack one by one at the checkout counter. Staff automatically move to "What's the next book?" and when there are no more books, the work ends.

A For-Each loop is a way to express this process with simple syntax. In many languages, the concept is like:

```
For every item in the list {
  Execute processing on that item
}
```

In Python it's `for item in list:`, in JavaScript it's `for (const item of list)`, with different syntax for each language.

The important part is that the same code works even if the list length or structure changes. If customers increase from 10 to 100, you don't need to rewrite the code.

## Implementation best practices

**Leverage list comprehensions (Python)**
For simple data transformations, using "list comprehensions" is more readable than For-Each loops.

**Avoid modifying lists during iteration**
Running For-Each loops while adding or deleting from the list itself causes unexpected behavior. It's safer to process first, then create a separate list.

**Implement error handling**
When retrieving data from networks and processing it, expect errors on individual items and implement catch mechanisms.

**Log progress with output**
When processing many items, logging like "Currently processing 50 of 100 items" makes troubleshooting easier.

## Workflow automation usage

Tools like [Relay.app](Relay.app.md) and other no-code automation platforms have a visual loop feature called an Iterator Block. You can process multiple items without writing code using just mouse operations.

For example, you can implement reading all rows from Google Sheet one by one and sending each row's data to [Slack](Slack.md) without any code.

## Related terms

- **[Array / List](Array.md)** — A data structure storing multiple values. The target that iterators process
- **[Lambda Expression / Anonymous Function](Lambda-Function.md)** — A way to write concise code combining with For-Each loops
- **[Map Function](Map-Function.md)** — An advanced form of For-Each that transforms each list element
- **[Filter Function](Filter-Function.md)** — A method of iteration extracting only specific elements from a list
- **[Reducer / Aggregation](Reducer.md)** — An iteration method that aggregates multiple elements into one value, such as summing a list

## Frequently asked questions

**Q: What's the difference between For-Each and while loops?**
A: For-Each must process "all elements" in a list. While loops, on the other hand, execute "as long as a condition is true," allowing finer control, but incorrectly written while loops risk infinite loops. Generally, For-Each is safer.

**Q: What if I want to exit the loop midway?**
A: Use keywords like `break` or `continue`. `break` exits completely, while `continue` skips the current element and moves to the next.

**Q: Can I process multiple lists simultaneously?**
A: It depends on the language. Python has `zip()` function to process multiple lists simultaneously. JavaScript can use `map()` to manipulate multiple lists.
