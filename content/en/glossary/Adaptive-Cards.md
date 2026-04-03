---
title: Adaptive Cards
date: 2025-12-19
lastmod: 2026-04-02
translationKey: Adaptive-Cards
description: A platform-independent UI framework by Microsoft that creates rich interactive cards in JSON format, rendering consistently across multiple applications and devices.
keywords:
  - Adaptive Cards
  - UI framework
  - Cross-platform development
  - Rich content cards
  - JSON schema
category: Web Development & Design
type: glossary
draft: false
url: /en/glossary/adaptive-cards/
aliases:
  - /en/glossary/Adaptive-Cards/
---

## What is Adaptive Cards?

**Adaptive Cards is an open-source, platform-independent UI framework by Microsoft that enables developers to define cards in JSON format once and have them automatically render natively across multiple applications, platforms, and devices.** Define content once in JSON, and it automatically adapts to Teams, Outlook, Slack, web applications, mobile apps, and more. Create rich card experiences with text, images, input fields, and buttons—without platform-specific coding—dramatically improving development efficiency.

> **In a nutshell:** "Like a magic suit that automatically adjusts to fit anyone's body size. The same JSON definition displays beautifully on Teams, Slack, smartphones, or desktops—each platform adapts it to look native."

**Key points:**

- **What it does:** Single JSON definition renders natively across platforms, automatically adapting to each environment's design language
- **Why it matters:** Dramatically reduces cross-platform development costs, testing overhead, and maintenance burden—resulting in significant cost savings
- **Who uses it:** Frontend developers, web designers, chatbot and automation developers, enterprise application teams

## Why it matters

Traditionally, companies supporting Teams, Slack, and web applications had to write separate code for each platform. The same approval form required Teams-specific code, Slack-specific code, and web code—wasteful, hard to maintain, and fragile. Platform updates required changes everywhere.

Adaptive Cards solves this fundamentally. One JSON definition covers all platforms, with each rendering natively according to its design language. Result: 30-50% development time reduction and dramatically lower testing costs. Complex user interactions—chatbot conversations, approval workflows, notification systems—are implemented uniformly across platforms, improving user experience consistency.

Built on web standards, Adaptive Cards future-proofs investments: JSON definitions remain backward-compatible when platforms update, protecting development investments.

## How it works

Adaptive Cards uses a three-layer architecture. The **definition layer** is where developers declaratively write JSON, describing card structure—headers, text, images, input fields, buttons, and their data structure.

The **renderer layer** contains platform-specific renderers: Teams renderer, Slack renderer, web renderer, etc. Each reads the shared JSON definition and converts it to platform-native UI elements. For example, a JSON "selection list" becomes a Teams dropdown, Slack button group, or mobile picker.

The **interaction layer** handles user actions. When users click buttons or enter form data, actions trigger handlers—sending HTTP requests, opening URLs, invoking host application features. Through these three layers, single JSON creates multi-platform functionality.

Powerful features include templating and data binding: template the card structure and dynamically bind data at runtime to generate multiple variations from one template, enabling easy API integration and database connectivity.

## Implementation patterns

Typical Adaptive Card implementation includes:

**Header section:** Card title, brand logo, metadata—immediate purpose understanding

**Body content:** Text descriptions, images, tables, lists—dense information presentation

**Interactive elements:** Text inputs, date pickers, selection fields, toggles—user input collection

**Action buttons:** Approval/rejection, submit, cancel—clear decision points

Implementation complexity depends on element count and conditional logic. Simple notification cards require ~100 lines JSON; complex forms exceed 1000 lines. Still, code volume stays 1/3 to 1/5 of platform-specific implementations.

## Benefits and use cases

**Enterprise communication**
Microsoft Teams approval, project updates, critical alerts using Adaptive Cards ensure unified, interactive experiences. Multiple departments experience identical card experiences.

**Chatbot and virtual assistants**
Customer service chatbots using Adaptive Cards display consistent multi-step forms across web, mobile apps, and chat platforms with one implementation.

**Workflow automation**
Employee leave requests, purchase orders, compliance declarations using Adaptive Cards provide consistent data entry experience on Outlook, chat, or web.

**Mobile and multi-device**
Same card definition displays fully on desktop, adjusts columns on tablets, becomes responsive single-column on phones—without device-specific code.

## Calculation method

Development cost reduction:

**Development Time Reduction = ((Platforms - 1) / Platforms) × Average Reduction Rate × 100**

Example: 3 platforms, 30% average reduction: ((3-1)/3) × 0.30 × 100 = 20% overall cost savings. More platforms increase savings.

Maintenance cost reduction measured by fix locations:

**Fix Location Reduction = (Platforms - 1) × Locations Needing Fix**

Example: 3 platforms, 10 fix locations needed. Traditional: 30 locations. Adaptive Cards: 10 locations.

## Benchmarks

Adoption impact:

- **Development time reduction:** 30-50% (higher with more platforms)
- **Testing effort reduction:** 40-60% (unified platform)
- **Maintenance cost reduction:** 50-70% (centralized fixes)
- **User adoption time:** 20-30% faster (unified UI learning)

Implementation scale by complexity:

- **Simple cards (notifications only):** 50-200 lines JSON, 1-2 days development
- **Standard cards (input forms):** 200-500 lines JSON, 3-5 days development
- **Complex cards (conditional branches):** 500-1500 lines JSON, 1-2 weeks development

## Related terms

- **[UI Framework](/en/glossary/UI-Framework/)** – Tools simplifying interface development; Adaptive Cards specialize in cross-platform
- **[JSON Schema](/en/glossary/JSON-Schema/)** – International standard for structured data; Adaptive Cards use this standard
- **[Responsive Design](/en/glossary/Responsive-Design/)** – Multi-screen optimal display; Adaptive Cards auto-respond
- **[Web Components](/en/glossary/Web-Components/)** – Reusable UI part standards; Adaptive Cards provide standardized parts
- **[Accessibility](/en/glossary/Accessibility--Web-/)** – All-user usable design; Adaptive Cards automatically support

## Frequently asked questions

**Q: Do Adaptive Cards look identical on all platforms?**
A: No. Each platform renders using its native design language—intentional design philosophy prioritizing "unified experience" over "unified appearance." Functionality and usability remain consistent across platforms.

**Q: Are templates supported?**
A: Yes. Adaptive Cards Designer Tool enables visual template design with data binding for dynamic content generation. Many organizations build and reuse template libraries.

**Q: Is compatibility with older platform versions guaranteed?**
A: Graceful degradation is implemented—cards display on older versions, though some newest features unavailable. Verify platform support status for your target version.
