---
title: "Rich Media Cards"
translationKey: "rich-media-cards"
description: "Rich media cards are interactive UI components in chat streams, delivering multimedia content and actionable elements like images, videos, and buttons for engaging conversations."
keywords: ["rich media cards", "chatbot", "conversational AI", "messaging platforms", "user engagement"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-03
draft: false
---
## Definition

Rich media cards are structured, interactive UI components embedded within chat streams, allowing the delivery of compelling, multimedia content and actionable elements directly inside a conversation. Unlike plain text messages, a rich media card can bundle together images, GIFs, videos, titles, subtitles, and buttons—offering users a visually engaging and actionable experience. These cards act like mini landing pages in chat, capable of driving actions, collecting information, and enhancing both usability and conversion.

**Authoritative References:**  
- [Google RCS Business Messaging: Rich Cards](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards)  
- [Microsoft Bot Framework: Add Rich Card Attachments](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)  
- [Sprinklr: Chatbot Analytics](https://www.sprinklr.com/blog/chatbot-analytics/)  
- [Tars: Rich Media for Chatbots](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)  
- [Kommunicate: Best Chatbot Practices](https://www.kommunicate.io/blog/best-chatbot-practices/)  
- [Quickchat: Chatbot Analytics Deep Dive](https://quickchat.ai/post/chatbot-analytics)  

## Anatomy of a Rich Media Card

Rich media cards are built from a set of standard components, each serving a functional and/or visual purpose. These include:

- **Media Element:** Images (JPEG, PNG, GIF), animations, videos (MP4, M4V, WebM, etc.), or even PDFs (platform-dependent). Media serves to attract attention, illustrate products, or add character.
  - [See supported formats and media heights for Google RCS](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#media)
- **Thumbnail:** Custom or default icon preview for media files, especially for larger files or PDFs. Thumbnails should be under 100 KB for optimal load times.
- **Title:** The headline or main label, typically up to 200 characters (platform-dependent). Should be concise and informative.
- **Subtitle/Description:** Supporting text, often up to 2,000 characters, providing additional context, benefits, or call-to-action (CTA) information.
- **Action Buttons:** Clickable elements triggering immediate actions (web navigation, postbacks, phone calls, downloads, etc.). Button limits and types vary by platform.
- **Suggested Replies:** Predefined user responses presented as chips or buttons, steering the conversation down optimal, bot-friendly paths.
- **Optional Interactive Elements:** Carousels (scrollable groups of cards), forms (for data capture), quick replies, list pickers, and custom payloads.

**Illustrations and references:**  
- [Google: Components of a Rich Card](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#rich-card-components)
- [Microsoft: Card Types](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0#types-of-rich-cards)

## How Rich Media Cards Are Used

### 1. Conversational Engagement

Rich media cards dramatically enhance chatbot interactions by making conversations more actionable, expressive, and visually appealing. Common chatbot use cases include:

- **Product Recommendations:** Showcasing product imagery, pricing, and “Buy Now” buttons.
- **Lead Generation:** Embedding forms for capturing user details within the chat.
- **Customer Support:** Presenting step-by-step troubleshooting guides, each with actionable “Did this help?” buttons.
- **Booking/Scheduling:** Displaying available time slots or services as cards with instant booking buttons.
- **Surveys & Feedback:** Requesting ratings, comments, or selections directly through card elements.
- **Interactive FAQs:** Navigable help topics with expandable/collapsible cards for browsing support content.

**Best Practice:** Use rich media cards to mimic natural conversational flow, providing one-tap options to reduce user friction and increase completion rates. [Tars: How To Improve Your Chatbot Completion Rate Using Rich Media](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)

### 2. Multi-Platform Messaging

Rich media card support and features differ among messaging platforms. Key environments include:

- **Web Chat Widgets:** Full card, carousel, and form support; customizable layouts (e.g., Intercom, Drift, Kommunicate).
- **Social Messaging:**  
  - **Facebook Messenger:** Card templates, carousels, quick replies, up to 10 cards per carousel.
  - **WhatsApp:** Limited list and button templates (no carousels), up to 3 buttons per message.
  - **Apple Business Chat:** Advanced card types, Apple Pay, forms, list pickers.
  - **Telegram, Viber, Slack:** Varying support for cards, buttons, and media.
- **Enterprise Solutions:**  
  - **Microsoft Dynamics 365, Salesforce:** Adaptive Cards (JSON-based), carousels, custom data collection, deep integration.
  - **APIs:** Custom bots with programmable payloads and UI rendering.

**Reference:**  
- [Google: Platform Constraints and Media Guidelines](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#media)
- [Microsoft: Channel Support Matrix](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-channels-reference?view=azure-bot-service-4.0)

## Technical Implementation and Supported Platforms

### Card Structure and Payloads

Rich media cards are typically defined in structured formats such as JSON. Each platform may have its own schema, but common elements appear across most:

**Example: Generic Product Card (JSON)**

```json
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
- [Google: JSON Structure for RCS Rich Cards](https://developers.google.com/business-communications/rcs-business-messaging/guides/build/messages/send)
- [Microsoft: Bot Framework Card Schemas](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0)

### Carousel (Scrollable Card Set)

A carousel presents multiple cards in a horizontally scrollable format, ideal for product discovery or option selection.

**Example: Carousel (JSON)**

```json
{
  "type": "carousel",
  "cards": [
    {
      "title": "Product 1",
      "image_url": "https://example.com/img/p1.png",
      "buttons": [ ... ]
    },
    {
      "title": "Product 2",
      "image_url": "https://example.com/img/p2.png",
      "buttons": [ ... ]
    }
  ]
}
```

### Supported Card Types (Microsoft Bot Framework)

- **HeroCard:** Large image, text, and buttons.
- **ThumbnailCard:** Smaller image, text, and buttons.
- **AnimationCard/VideoCard/AudioCard:** Embedded media playback.
- **ReceiptCard:** Structured receipts with items, prices, and totals.
- **SignInCard:** OAuth or third-party authentication flows.
- **AdaptiveCard:** Highly customizable cards with rich UI elements, layouts, and forms. [Adaptive Cards Designer](https://adaptivecards.io/designer/)

**Detailed Reference:**  
- [Microsoft Bot Framework Card Types](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0#types-of-rich-cards)

### Platform-Specific Constraints

| Platform               | Card Support        | Max Cards/Carousel | Image Size Limits | Button Limit | Notable Features                  |
|------------------------|--------------------|-------------------|------------------|-------------|-----------------------------------|
| Web Chat Widgets       | Full (cards, forms)| Varies (up to 10) | ~1MB per image   | 3–5/button  | Custom layouts, quick replies     |
| WhatsApp               | Limited (list, btn)| 1–3/row           | <1MB             | 3           | Simple cards, no carousels        |
| Apple Business Chat    | Advanced           | Varies            | ~1MB             | 3–5         | Apple Pay, forms, list pickers    |
| Facebook Messenger     | Full (card, carousel)| 10/carousel     | 1MB              | 3           | Templates, quick replies          |
| Microsoft Dynamics 365 | Full (cards, JSON) | 10/carousel       | 1MB              | 5           | Adaptive cards, forms, custom JSON|

**Technical Notes:**
- Always compress images and videos to improve speed, especially for mobile users.
- Respect platform-specific character limits (titles, buttons, etc.).
- Test interactivity and formatting across devices and channels.
- Use analytics and tracking for button clicks, card views, and user actions.
- [Google: Media Upload and Thumbnail Guidelines](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards#thumbnail)

## Key Benefits of Rich Media Cards

### 1. Higher Engagement

Rich media cards consistently outperform text-only messages in terms of engagement. Data shows:
- Image-rich conversations can drive **2–3x higher engagement** ([Conferbot](https://www.conferbot.com/features/rich-media), [Tars](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media))
- Visuals and buttons capture attention and encourage more interaction.
- Frictionless: users can act with a single tap (buy, book, reply).

### 2. Improved Conversion Rates

- Chatbots with rich media elements deliver up to **85% higher conversion rates** compared to simple text bots ([Tars](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)).
- Interactive forms, carousels, and CTAs streamline the user journey and reduce drop-off.

### 3. Enhanced Brand Experience

- Cards reinforce brand identity through custom images, colors, and tone.
- More memorable and enjoyable, leading to higher brand recall.
- Humanizes the chatbot—adding personality with GIFs, emojis, or video.

### 4. Operational Efficiency

- Reduces customer support workload by guiding users to self-serve answers.
- Standardizes responses, ensuring consistency and accuracy.

### 5. Advanced Tracking and Analytics

Rich media cards are trackable, allowing you to measure which cards, buttons, and flows drive engagement. Key analytics include:
- Button click-through rates
- Card view counts
- Drop-off points and funnel analysis
- Goal completion rates

**References:**  
- [Sprinklr: Chatbot Analytics Metrics](https://www.sprinklr.com/blog/chatbot-analytics/)
- [Quickchat: Complete Guide to Chatbot Analytics](https://quickchat.ai/post/chatbot-analytics)

## Use Cases & Real-World Examples

### Lead Generation

**Scenario:** Website chatbot presents a carousel of services, each with an “Inquire” button. Users submit contact info directly in chat.  
**Benefit:** Frictionless data capture increases lead volume and quality.

### E-Commerce Product Discovery

**Scenario:** Messenger bot sends a carousel of bestsellers, each card showing product image, price, and “Buy Now” button.  
**Benefit:** Streamlined browsing and purchase boost conversion.

### Customer Support

**Scenario:** A bot presents troubleshooting steps as cards, each with “Did this help?” buttons.  
**Benefit:** Reduces agent workload and increases resolution speed.

### Appointment Booking

**Scenario:** Bot shows available time slots as cards; user taps to confirm.  
**Benefit:** Simplifies scheduling, reduces abandonment.

### Surveys & Feedback

**Scenario:** After an interaction, a card requests a star rating and optional comments.  
**Benefit:** Boosts survey completion rates and actionable feedback.

### Real Estate & Listings

**Scenario:** Property bot displays available homes as cards, each with images and “Schedule Tour” buttons.  
**Benefit:** Engages buyers and enables instant action.

### Content Delivery

**Scenario:** Media bot sends news articles as cards with thumbnails, headlines, and “Read More” buttons.  
**Benefit:** Increases content consumption and engagement.

**Additional Resources:**  
- [Sendbird: What is Rich Media?](https://sendbird.com/learn/what-is-rich-media)  
- [Madgicx: Rich Media Ads](https://madgicx.com/blog/rich-media)

## Best Practices for Rich Media Cards

1. **Prioritize Clarity and Simplicity**
   - Limit cards per carousel (3–10, depending on platform).
   - Use concise text, high-quality images, and focused actions.
2. **Optimize for Performance**
   - Keep images/videos under 1MB; prefer 50–100KB for thumbnails.
   - Host media on fast CDNs and test load times on slow connections.
3. **Mobile-First Design**
   - Ensure buttons are large and touch-friendly.
   - Avoid dense layouts; keep content readable and actionable.
4. **Action-Oriented Buttons**
   - Use clear, specific CTAs (e.g., “Book Now”, “Get Quote”).
   - Limit to 3–5 actions per card, based on platform.
5. **Personalization**
   - Tailor card content based on user context, history, or preferences.
6. **Accessibility**
   - Add descriptive alt text for images.
   - Ensure button labels are screen-reader friendly.
7. **A/B Testing**
   - Experiment with card order, visuals, and messaging.
   - Use analytics to iterate based on real usage.
8. **Advanced Analytics**
   - Track card impressions, button clicks, drop-offs, and goal completions.
   - Use dashboards and funnel visualization for optimization ([Quickchat AI guide](https://quickchat.ai/post/chatbot-analytics)).
9. **Brand Consistency**
   - Use brand-approved colors, logos, and typography.
   - Ensure messaging matches brand tone.

**Pitfalls to Avoid:**
- Overloading cards with text or too many buttons.
- Neglecting image optimization—slow load times reduce engagement.
- Using generic or irrelevant visuals.
- Ignoring platform-specific card limits and constraints.

**References:**  
- [Kommunicate: Best Chatbot Practices](https://www.kommunicate.io/blog/best-chatbot-practices/)  
- [Tars: When and How To Use Rich Media](https://hellotars.com/blog/improve-chatbot-conversion-rate-rich-media)

## Advanced Analytics and Measurement

### Key Metrics for Rich Media Card Performance

- **Total Users:** Number of unique users who interacted with the bot.
- **Active/Engaged Users:** Users who interacted beyond the welcome message.
- **Card Views:** Number of times a card was displayed.
- **Button Clicks/CTA Engagement:** Click-through rate for each action button.
- **Drop-Off Rate:** Points where users abandon the conversation.
- **Goal Completion Rate:** Percentage of users completing a desired action (form fill, purchase, etc.).
- **Self-Service Rate:** Issues resolved by the bot without human intervention.
- **Deflection Rate:** Percentage of inquiries handled by the bot, reducing human workload.
- **CSAT/NPS:** Customer satisfaction scores, often collected via rich media survey cards.

### Using Analytics to Optimize Results

- **Funnel Analysis:** Track how users move through carousels/cards, identifying drop-off points.
- **Content Optimization:** Use card-level analytics to refine images, titles, or CTAs.
- **A/B Testing:** Experiment with card order, button placement, or CTA wording to improve completion.
- **Personalization:** Leverage analytics to segment users and deliver targeted cards.

**Dashboards and Tools:**  
- [Sprinklr: Chatbot Analytics Dashboard](https://www.sprinklr.com/blog/chatbot-analytics/)
- [Quickchat: AI Agent Analytics](https://quickchat.ai/post/chatbot-analytics)

## Platform-Specific Technical Guides

- [Google: RCS Rich Card Capabilities and Constraints](https://developers.google.com/business-communications/rcs-business-messaging/guides/learn/rich-cards)
- [Microsoft: Bot Framework Card Types and Channel Matrix](https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-add-rich-cards?view=azure-bot-service-4.0)
- [Adaptive Cards Designer](https://adaptivecards.io/designer/)
- [Facebook Messenger Platform Templates](https://developers.facebook.com/docs/messenger-platform/send-messages/template/)
- [WhatsApp Business Messaging Templates](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates)

## Frequently Asked Questions (FAQs)

### What’s the difference between a rich media card and a standard message?
Standard messages are plain text. Rich media cards can include images, videos, carousels, and buttons, enabling interactive and visually engaging experiences.

### Do I need design skills to create rich media cards?
Most chatbot platforms offer visual builders with drag-and-drop card creation (e.g., Kommunicate, Tars, Microsoft Adaptive Cards Designer). Minimal design skills are needed, though attention to clarity and branding is important.

### Will rich media slow down my chatbot?
Optimized images and videos (preferably under 1MB) prevent slowdowns. Compress all media, and use CDN hosting for large files.

### Can I track user interactions with rich media cards?
Yes. Most platforms provide analytics for button clicks, card views, drop-offs, and goal completions (see above for details).

### Are rich media cards supported on all messaging apps?
Support varies by platform. Web chat, Messenger, and Apple Business Chat offer robust support; WhatsApp and SMS are

