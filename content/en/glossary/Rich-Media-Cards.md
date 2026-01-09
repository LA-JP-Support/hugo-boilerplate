---
title: "Rich Media Cards"
translationKey: "rich-media-cards"
description: "Interactive message cards that combine images, videos, and buttons within chat to create engaging, clickable experiences that drive actions like purchases or sign-ups."
keywords: ["rich media cards", "chatbot", "conversational AI", "messaging platforms", "user engagement"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What Are Rich Media Cards?

Rich media cards are structured, interactive UI components embedded within chat streams, enabling delivery of compelling multimedia content and actionable elements directly inside conversations. Unlike plain text messages, rich media cards bundle images, GIFs, videos, titles, subtitles, and buttons—offering users visually engaging and actionable experiences. These cards function like mini landing pages within chat, capable of driving actions, collecting information, and enhancing both usability and conversion rates.

Rich media cards transform conversational interfaces from simple text exchanges into dynamic, interactive experiences supporting product discovery, lead generation, customer support, booking, surveys, and content delivery across web chat, social messaging platforms, and enterprise solutions.

## Anatomy of Rich Media Cards

Rich media cards comprise several standard components serving functional and visual purposes:

<strong>Media Element:</strong>Images (JPEG, PNG, GIF), animations, videos (MP4, M4V, WebM), or PDFs (platform-dependent) attracting attention, illustrating products, or adding character

<strong>Thumbnail:</strong>Custom or default icon preview for media files, especially larger files or PDFs, optimized under 100 KB for fast loading

<strong>Title:</strong>Headline or main label, typically up to 200 characters (platform-dependent), concise and informative

<strong>Subtitle/Description:</strong>Supporting text, often up to 2,000 characters, providing context, benefits, or call-to-action information

<strong>Action Buttons:</strong>Clickable elements triggering actions—web navigation, postbacks, phone calls, downloads—with limits varying by platform

<strong>Suggested Replies:</strong>Predefined user responses as chips or buttons, steering conversation down optimal paths

<strong>Optional Interactive Elements:</strong>Carousels (scrollable card groups), forms (data capture), quick replies, list pickers, custom payloads

## How Rich Media Cards Work

### Conversational Engagement

Rich media cards enhance chatbot interactions by making conversations more actionable, expressive, and visually appealing.

<strong>Common Use Cases:</strong>

<strong>Product Recommendations:</strong>Showcase product imagery, pricing, "Buy Now" buttons for streamlined purchasing

<strong>Lead Generation:</strong>Embed forms capturing user details within chat for frictionless data collection

<strong>Customer Support:</strong>Present step-by-step troubleshooting guides with actionable "Did this help?" buttons

<strong>Booking/Scheduling:</strong>Display available time slots or services as cards with instant booking buttons

<strong>Surveys & Feedback:</strong>Request ratings, comments, or selections directly through card elements

<strong>Interactive FAQs:</strong>Navigable help topics with expandable/collapsible cards for browsing support content

### Multi-Platform Support

Rich media card support varies across messaging platforms:

<strong>Web Chat Widgets:</strong>Full card, carousel, and form support; customizable layouts (Intercom, Drift, Kommunicate)

<strong>Social Messaging:</strong>- <strong>Facebook Messenger:</strong>Card templates, carousels, quick replies, up to 10 cards per carousel
- <strong>WhatsApp:</strong>Limited list and button templates (no carousels), up to 3 buttons per message
- <strong>Apple Business Chat:</strong>Advanced card types, Apple Pay, forms, list pickers
- <strong>Telegram, Viber, Slack:</strong>Varying support for cards, buttons, and media

<strong>Enterprise Solutions:</strong>- <strong>Microsoft Dynamics 365, Salesforce:</strong>Adaptive Cards (JSON-based), carousels, custom data collection
- <strong>Custom APIs:</strong>Programmable payloads and UI rendering

## Technical Implementation

### Card Structure (JSON)

Rich media cards are typically defined in structured formats like JSON:

<strong>Example Product Card:</strong>```json
{
  "type": "card",
  "title": "Wireless Headphones",
  "subtitle": "Noise-cancelling, 20h battery life",
  "image_url": "https://example.com/img/headphones.png",
  "buttons": [
    {
      "type": "web_url",
      "title": "Buy Now",
      "url": "https://example.com/buy/headphones"
    },
    {
      "type": "postback",
      "title": "More Info",
      "payload": "INFO_HEADPHONES"
    }
  ]
}
```

### Carousel Implementation

Carousels present multiple cards horizontally for product discovery or option selection:

**Example Carousel:**```json
{
  "type": "carousel",
  "cards": [
    {
      "title": "Product 1",
      "image_url": "https://example.com/img/p1.png",
      "buttons": [...]
    },
    {
      "title": "Product 2",
      "image_url": "https://example.com/img/p2.png",
      "buttons": [...]
    }
  ]
}
```

### Supported Card Types (Microsoft Bot Framework)

<strong>HeroCard:</strong>Large image, text, and buttons

<strong>ThumbnailCard:</strong>Smaller image, text, and buttons

<strong>AnimationCard/VideoCard/AudioCard:</strong>Embedded media playback

<strong>ReceiptCard:</strong>Structured receipts with items, prices, totals

<strong>SignInCard:</strong>OAuth or third-party authentication flows

<strong>AdaptiveCard:</strong>Highly customizable cards with rich UI elements, layouts, forms

### Platform-Specific Constraints

| Platform | Card Support | Max Cards/Carousel | Image Size | Button Limit | Notable Features |
|----------|--------------|-------------------|------------|--------------|------------------|
| Web Chat Widgets | Full (cards, forms) | Varies (up to 10) | ~1MB | 3–5 | Custom layouts, quick replies |
| WhatsApp | Limited (list, button) | 1–3/row | <1MB | 3 | Simple cards, no carousels |
| Apple Business Chat | Advanced | Varies | ~1MB | 3–5 | Apple Pay, forms, list pickers |
| Facebook Messenger | Full (card, carousel) | 10/carousel | 1MB | 3 | Templates, quick replies |
| Microsoft Dynamics 365 | Full (cards, JSON) | 10/carousel | 1MB | 5 | Adaptive cards, forms, custom JSON |

<strong>Implementation Notes:</strong>- Compress images and videos for mobile performance
- Respect platform-specific character limits
- Test interactivity across devices and channels
- Use analytics for button clicks, card views, user actions

## Key Benefits

### Higher Engagement

Rich media cards consistently outperform text-only messages:
- Image-rich conversations drive 2–3x higher engagement
- Visuals and buttons capture attention and encourage interaction
- Frictionless: users act with single tap (buy, book, reply)

### Improved Conversion Rates

- Chatbots with rich media deliver up to 85% higher conversion rates versus text-only bots
- Interactive forms, carousels, CTAs streamline user journey and reduce drop-off
- Direct action buttons eliminate navigation friction

### Enhanced Brand Experience

- Cards reinforce brand identity through custom images, colors, tone
- More memorable and enjoyable, leading to higher brand recall
- Humanizes chatbot with GIFs, emojis, or video personality

### Operational Efficiency

- Reduces customer support workload by guiding users to self-serve answers
- Standardizes responses ensuring consistency and accuracy
- Automates routine interactions freeing agents for complex issues

### Advanced Tracking

Rich media cards enable comprehensive analytics:
- Button click-through rates
- Card view counts
- Drop-off points and funnel analysis
- Goal completion rates
- User engagement patterns

## Real-World Applications

### E-Commerce Product Discovery

<strong>Implementation:</strong>Messenger bot sends carousel of bestsellers with product images, prices, "Buy Now" buttons

<strong>Results:</strong>Streamlined browsing and purchase boost conversion, reduce cart abandonment

### Lead Generation

<strong>Implementation:</strong>Website chatbot presents service carousel with "Inquire" buttons, captures contact info in-chat

<strong>Results:</strong>Frictionless data capture increases lead volume and quality

### Customer Support

<strong>Implementation:</strong>Bot presents troubleshooting steps as cards with "Did this help?" buttons

<strong>Results:</strong>Reduces agent workload, increases resolution speed, improves CSAT

### Appointment Booking

<strong>Implementation:</strong>Bot displays available time slots as cards; user taps to confirm

<strong>Results:</strong>Simplifies scheduling, reduces abandonment, increases bookings

### Content Delivery

<strong>Implementation:</strong>Media bot sends news articles as cards with thumbnails, headlines, "Read More" buttons

<strong>Results:</strong>Increases content consumption and engagement

## Best Practices

### Design and Content

<strong>Prioritize Clarity:</strong>Limit cards per carousel (3–10 depending on platform), use concise text, high-quality images

<strong>Optimize Performance:</strong>Keep images/videos under 1MB; prefer 50–100KB for thumbnails; host on fast CDNs

<strong>Mobile-First Approach:</strong>Ensure buttons are large and touch-friendly; avoid dense layouts

<strong>Action-Oriented Buttons:</strong>Use clear, specific CTAs (e.g., "Book Now", "Get Quote"); limit to 3–5 actions per card

<strong>Personalization:</strong>Tailor card content based on user context, history, or preferences

### Accessibility and Testing

<strong>Add Accessibility:</strong>Descriptive alt text for images; screen-reader friendly button labels

<strong>A/B Testing:</strong>Experiment with card order, visuals, messaging; iterate based on real usage

<strong>Cross-Platform Testing:</strong>Verify formatting and functionality across all target platforms

### Analytics and Optimization

<strong>Track Comprehensively:</strong>Card impressions, button clicks, drop-offs, goal completions

<strong>Use Dashboards:</strong>Funnel visualization for optimization; identify bottlenecks

<strong>Segment Analysis:</strong>Compare performance across user segments, channels, time periods

### Brand Consistency

<strong>Visual Standards:</strong>Use brand-approved colors, logos, typography

<strong>Tone Alignment:</strong>Ensure messaging matches brand voice

<strong>Quality Control:</strong>Regular content reviews and updates

### Common Pitfalls to Avoid

- Overloading cards with text or too many buttons
- Neglecting image optimization causing slow load times
- Using generic or irrelevant visuals
- Ignoring platform-specific limits and constraints
- Inconsistent branding across cards
- Missing analytics implementation

## Analytics and Measurement

### Key Performance Metrics

<strong>Total Users:</strong>Unique users interacting with bot

<strong>Active/Engaged Users:</strong>Users beyond welcome message interaction

<strong>Card Views:</strong>Times card displayed to users

<strong>Button Clicks/CTA Engagement:</strong>Click-through rate for each action

<strong>Drop-Off Rate:</strong>Points where users abandon conversation

<strong>Goal Completion Rate:</strong>Percentage completing desired action

<strong>Self-Service Rate:</strong>Issues resolved without human intervention

<strong>Deflection Rate:</strong>Inquiries handled by bot reducing human workload

<strong>CSAT/NPS:</strong>Customer satisfaction scores from survey cards

### Optimization Strategies

<strong>Funnel Analysis:</strong>Track user movement through carousels/cards, identify drop-off points

<strong>Content Optimization:</strong>Refine images, titles, CTAs based on card-level analytics

<strong>A/B Testing:</strong>Experiment with card order, button placement, CTA wording

<strong>Personalization:</strong>Leverage analytics to segment users and deliver targeted cards

## Platform-Specific Resources

<strong>Google RCS Business Messaging:</strong>Rich card capabilities, media formats, implementation guides

<strong>Microsoft Bot Framework:</strong>Card types, channel support matrix, adaptive card designer

<strong>Facebook Messenger Platform:</strong>Template documentation, carousel implementation

<strong>WhatsApp Business API:</strong>Message templates, button limitations

<strong>Apple Business Chat:</strong>Advanced features, Apple Pay integration

## Frequently Asked Questions

<strong>What's the difference between rich media cards and standard messages?</strong>Standard messages are plain text. Rich media cards include images, videos, carousels, buttons enabling interactive, visually engaging experiences.

<strong>Do I need design skills to create rich media cards?</strong>Most chatbot platforms offer visual builders with drag-and-drop card creation. Minimal design skills needed, though attention to clarity and branding important.

<strong>Will rich media slow down my chatbot?</strong>Optimized images and videos (preferably under 1MB) prevent slowdowns. Compress all media; use CDN hosting for large files.

<strong>Can I track user interactions with rich media cards?</strong>Yes. Most platforms provide analytics for button clicks, card views, drop-offs, goal completions.

<strong>Are rich media cards supported on all messaging apps?</strong>Support varies by platform. Web chat, Messenger, Apple Business Chat offer robust support; WhatsApp and SMS have limited capabilities.

<strong>How do I choose between carousel and single cards?</strong>Use carousels for product discovery, comparisons, or multiple options. Single cards work better for focused actions or detailed information.

<strong>What's the optimal number of cards in a carousel?</strong>3–10 cards depending on platform. Fewer cards (3–5) typically perform better on mobile.

## References


1. Google. (n.d.). RCS Business Messaging: Rich Cards. Google Developers.

2. Microsoft. (n.d.). Bot Framework: Add Rich Card Attachments. Microsoft Learn.

3. Sprinklr. (n.d.). Chatbot Analytics. Sprinklr Blog.

4. Tars. (n.d.). Improve Chatbot Conversion Rate Using Rich Media. Tars Blog.

5. Kommunicate. (n.d.). Best Chatbot Practices. Kommunicate Blog.

6. Quickchat. (n.d.). Chatbot Analytics Deep Dive. Quickchat Blog.

7. Adaptive Cards. Adaptive Cards Designer. URL: https://adaptivecards.io/designer/

8. Facebook. (n.d.). Messenger Platform Templates. Facebook Developers.

9. Facebook. (n.d.). WhatsApp Business Messaging Templates. Facebook Developers.

10. Sendbird. (n.d.). What is Rich Media?. Sendbird Learn.

11. Madgicx. (n.d.). Rich Media Ads. Madgicx Blog.

12. Conferbot. (n.d.). Rich Media Features. Conferbot Features.
