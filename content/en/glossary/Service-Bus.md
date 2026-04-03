---
title: Service Bus
translationKey: service-bus
description: Service Bus is a middleware infrastructure that performs asynchronous messaging between distributed applications. It enables microservice communication.
keywords:
- service bus
- messaging
- microservices
- asynchronous communication
- event-driven
category: Data & Analytics
type: glossary
date: 2026-04-02
lastmod: 2026-04-02
draft: false
url: "/en/glossary/Service-Bus/"
---

## What is Service Bus?

**Service Bus is an infrastructure that safely sends and receives messages between different applications.** Senders and receivers don't need to be directly connected; Service Bus mediates and guarantees reliable message delivery. This allows each application to operate independently while communicating with loose coupling.

> **In a nutshell:** It's like a post office that reliably delivers letters between systems.

**Key points:**

- **What it does:** Receives, routes, and accurately delivers messages
- **Why it's needed:** Enables reliable communication while maintaining system independence
- **Who uses it:** Microservice architectures, enterprise system integration

## Why it matters

When multiple systems need to work together, direct connections cause problems. If the sender goes down, the receiver is affected, and changes ripple through. With Service Bus in between, each system can operate independently.

Additionally, there's no worry about messages being lost. Even if the inventory system is temporarily down when an order system sends a "new order" message, the message waits in a queue and is automatically delivered when the system recovers.

## How it works

Service Bus has several core components.

**Message queues:** Temporarily store messages and wait for the receiver to retrieve them. FIFO (first-in-first-out) order is guaranteed.

**Topics and subscriptions:** A publish-subscribe model where one message is received by multiple subscribers. For example, an "order created" event is received by inventory, shipping, and billing systems all at once.

**Dead-letter queue:** Stores messages that failed delivery for later investigation and reprocessing.

**Execution flow:** Application A sends message → Service Bus receives → routes based on routing rules → Application B retrieves → acknowledges → message deleted

## Real-world use cases

**E-commerce order processing**
When users place orders, an "OrderCreated" message is sent to a topic, and inventory, shipping, and billing all receive that message.

**IoT sensor data processing**
Large volumes of sensor data flow through the service bus, and multiple analytics systems each retrieve the data they need.

**System integration**
Connect legacy mainframes with new cloud systems via [Azure Service Bus](Azure-Service-Bus.md).

## Benefits and considerations

**Benefits:** System independence, improved reliability, scalability, and fault isolation.

**Considerations:** Complexity increases and debugging becomes harder. Additionally, duplicate message delivery must be handled, requiring idempotency design.

## Related terms

- **[Microservices](Microservices.md)** — distributed systems communicating via service bus
- **[Asynchronous Processing](Asynchronous-Processing.md)** — basic operation of service bus
- **[Event-Driven Architecture](Event-Driven-Architecture.md)** — design pattern leveraging service bus
- **[Message Queue](Message-Queue.md)** — core component of service bus
- **[Azure Service Bus](Azure-Service-Bus.md)** — managed service bus

## Frequently asked questions

**Q: Can messages be lost?**
A: Usually not. Messages are retained until acknowledgment is received and stored in persistent storage.

**Q: Is message order guaranteed?**
A: Queues guarantee FIFO order. However, topics may have weaker order guarantees.
