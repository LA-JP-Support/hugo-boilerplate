---
title: "Adaptive Cards"
date: 2025-12-19
translationKey: adaptive-cards
description: "A standardized format that lets developers create interactive content cards once and display them consistently across different apps and platforms without rewriting code."
keywords:
- Adaptive Cards
- UI framework
- cross-platform development
- rich content cards
- Microsoft Bot Framework
- JSON schema
- interactive cards
category: "AI Chatbot & Automation"
type: glossary
draft: false
---

## What is Adaptive Cards?

Adaptive Cards is an open-source, platform-agnostic UI framework developed by Microsoft that enables developers to create and exchange rich, interactive content cards in a standardized JSON format. This innovative framework allows developers to author content once and have it render natively across multiple applications, platforms, and devices without requiring custom code for each target environment. The cards can contain a variety of elements including text, images, input fields, buttons, and complex layouts, making them ideal for creating engaging user experiences in chatbots, productivity applications, and collaborative platforms.

The framework operates on the principle of "write once, render everywhere," addressing a fundamental challenge in modern application development where content needs to be displayed consistently across diverse platforms with varying UI capabilities and design languages. Adaptive Cards achieve this by separating content definition from presentation logic, allowing host applications to apply their own styling and interaction patterns while maintaining the structural integrity and functionality of the card content. This approach ensures that cards feel native to each platform while preserving the intended user experience and data collection capabilities.

At its core, Adaptive Cards represents a paradigm shift from traditional web-based content delivery to a more flexible, declarative approach that prioritizes accessibility, responsiveness, and cross-platform compatibility. The framework has gained significant adoption in enterprise environments, particularly in Microsoft's ecosystem including Teams, Outlook, Power Platform, and Azure services, while also supporting integration with third-party applications through its open-source nature and comprehensive SDK offerings for multiple programming languages and platforms.

## Key Features

**JSON-Based Schema Architecture**
Adaptive Cards utilize a comprehensive JSON schema that defines the structure, content, and behavior of cards in a declarative manner. This schema-driven approach ensures consistency across implementations while providing flexibility for complex layouts and interactive elements. The JSON format makes cards easily serializable, cacheable, and transferable between systems, enabling seamless integration with APIs, databases, and messaging platforms.

**Cross-Platform Native Rendering**
The framework provides native rendering capabilities across multiple platforms including web browsers, mobile applications, desktop software, and messaging platforms. Each host application can implement its own renderer that interprets the JSON schema and produces native UI elements that match the platform's design language and interaction patterns. This native rendering ensures optimal performance and user experience while maintaining accessibility standards specific to each platform.

**Rich Interactive Elements**
Adaptive Cards support a comprehensive set of interactive elements including text inputs, number inputs, date pickers, choice sets (radio buttons, checkboxes, dropdowns), toggle switches, and action buttons. These elements can be combined to create sophisticated forms, surveys, approval workflows, and data collection interfaces that maintain their functionality across all supported platforms. The framework also supports conditional visibility and validation rules for enhanced user experience.

**Templating and Data Binding**
The framework includes powerful templating capabilities that allow developers to separate card structure from data, enabling dynamic content generation and reusable card templates. Data binding features support complex scenarios including loops, conditional rendering, and data transformation, making it possible to create cards that adapt their content based on runtime data. This templating system is particularly valuable for creating cards that display varying amounts of data or need to support multiple languages.

**Accessibility and Internationalization**
Adaptive Cards are designed with accessibility as a core principle, automatically supporting screen readers, keyboard navigation, and other assistive technologies through native platform implementations. The framework includes built-in support for right-to-left languages, localization of text content, and cultural formatting of dates, numbers, and currencies. These features ensure that cards provide inclusive experiences for users with diverse needs and from different geographic regions.

**Action Framework**
The comprehensive action framework enables cards to trigger various types of responses including HTTP requests, opening URLs, submitting form data, and invoking host application functions. Actions can be configured with different execution modes, validation requirements, and confirmation dialogs, providing flexibility for implementing complex business workflows. The framework also supports action chaining and conditional execution based on user inputs or card state.

**Styling and Theming System**
Adaptive Cards implement a sophisticated styling system that allows host applications to apply consistent theming while preserving card functionality. The framework supports color schemes, typography settings, spacing configurations, and container styles that can be customized to match brand guidelines or platform conventions. This theming capability ensures visual consistency within applications while maintaining the cards' adaptive nature.

**Extensibility and Custom Elements**
The framework provides extensibility mechanisms that allow developers to create custom elements and actions beyond the standard schema. This extensibility enables organizations to implement domain-specific components while maintaining compatibility with the core Adaptive Cards ecosystem. Custom elements can be registered with host applications and used alongside standard elements in card definitions.

## How It Works

The Adaptive Cards framework operates through a multi-layered architecture that separates content definition, rendering logic, and host integration. The process begins with developers creating card definitions using the JSON schema, which describes the card's structure, content, and interactive elements. This JSON payload contains all necessary information for rendering the card, including layout specifications, data bindings, styling hints, and action definitions.

When a card needs to be displayed, the host application's Adaptive Cards renderer parses the JSON schema and creates native UI elements corresponding to each defined component. The renderer applies the host's styling and theming rules while preserving the card's structural integrity and functionality. This rendering process is highly optimized to ensure smooth performance even with complex cards containing multiple interactive elements and data sources.

The framework handles user interactions through its action system, which can trigger various responses including data submission, navigation, or host application functions. When users interact with card elements, the renderer captures these interactions and processes them according to the defined action specifications. This can result in HTTP requests being sent to external services, form data being collected and validated, or custom functions being executed within the host application.

Data binding and templating are processed during the rendering phase, allowing cards to display dynamic content based on runtime data sources. The templating engine supports complex scenarios including conditional rendering, loops, and data transformations, enabling cards to adapt their content and structure based on the available data. This dynamic capability makes Adaptive Cards particularly powerful for scenarios requiring personalized or context-sensitive content.

## Benefits

**For Developers**
- **Reduced Development Time**: Developers can create content once and deploy it across multiple platforms without writing platform-specific code, significantly reducing development effort and maintenance overhead. This approach eliminates the need to maintain separate implementations for web, mobile, and desktop environments.
- **Consistent User Experience**: The framework ensures that card content maintains consistent functionality and behavior across all platforms while adapting to each platform's native look and feel. This consistency improves user adoption and reduces confusion when users interact with the same content across different applications.
- **Simplified Integration**: Comprehensive SDKs and tooling make it easy to integrate Adaptive Cards into existing applications and workflows. The framework provides clear APIs, extensive documentation, and sample implementations that accelerate the integration process.
- **Enhanced Productivity**: Rich tooling including designers, validators, and template libraries enable rapid card development and testing. Developers can preview cards across multiple platforms simultaneously and validate their JSON schemas before deployment.

**For Organizations**
- **Cost Efficiency**: Organizations can reduce development and maintenance costs by creating content once instead of developing separate implementations for each platform or application. This approach also reduces the complexity of managing multiple codebases and deployment processes.
- **Improved User Engagement**: Rich, interactive content capabilities enable organizations to create more engaging user experiences that drive higher completion rates for forms, surveys, and workflow processes. The native rendering ensures optimal performance and usability across all platforms.
- **Faster Time-to-Market**: The ability to deploy interactive content quickly across multiple platforms enables organizations to respond rapidly to business needs and market opportunities. Template libraries and reusable components further accelerate the development process.
- **Better Analytics and Insights**: Centralized action handling and data collection capabilities provide organizations with comprehensive insights into user interactions and content performance across all platforms.

**For End Users**
- **Native Platform Experience**: Users benefit from content that feels native to their preferred platforms while maintaining consistent functionality across devices. This native experience ensures optimal performance and familiar interaction patterns.
- **Enhanced Accessibility**: Built-in accessibility features ensure that all users can interact with card content regardless of their abilities or assistive technology requirements. The framework automatically supports screen readers, keyboard navigation, and other accessibility standards.
- **Improved Performance**: Native rendering eliminates the overhead associated with web-based content delivery, resulting in faster loading times and smoother interactions. This performance optimization is particularly beneficial for mobile users and those with limited bandwidth.

## Common Use Cases

**Enterprise Communication and Collaboration**
Adaptive Cards are extensively used in Microsoft Teams, Outlook, and other collaboration platforms to create rich notifications, approval workflows, and interactive messages. Organizations implement cards for expense approval processes, project status updates, meeting summaries, and team announcements that require user interaction or data collection. These cards enable users to take actions directly within their communication tools without switching to external applications, improving productivity and response times.

**Customer Support and Service Automation**
Customer service chatbots and virtual assistants leverage Adaptive Cards to present complex information, collect customer details, and guide users through troubleshooting processes. Cards can display product information with images, create interactive troubleshooting wizards, collect feedback through embedded forms, and present escalation options with contextual information. This rich interaction capability significantly improves the effectiveness of automated customer service while reducing the need for human intervention.

**Business Process Automation**
Organizations use Adaptive Cards to digitize and streamline business processes including employee onboarding, purchase requisitions, leave requests, and compliance workflows. Cards can present multi-step forms with conditional logic, display approval chains with current status, and collect digital signatures or approvals. The cross-platform nature ensures that these processes work consistently whether accessed from desktop applications, mobile devices, or web browsers.

**Data Visualization and Reporting**
Adaptive Cards serve as an effective medium for presenting business intelligence data, performance metrics, and analytical insights in digestible formats. Cards can display charts, key performance indicators, trend summaries, and interactive filters that allow users to explore data without leaving their primary work environment. This capability is particularly valuable for executive dashboards and operational reporting systems.

**E-commerce and Transactional Experiences**
Online retailers and service providers implement Adaptive Cards to create rich product showcases, order confirmations, shipping updates, and customer feedback collection interfaces. Cards can display product images, specifications, pricing information, and purchase options while maintaining consistent branding across different customer touchpoints including email, messaging apps, and mobile notifications.

**Educational and Training Content**
Educational institutions and corporate training programs utilize Adaptive Cards to create interactive learning modules, quizzes, assignment submissions, and progress tracking interfaces. Cards can present multimedia content, collect student responses, provide immediate feedback, and track completion status across various learning management systems and communication platforms.

**Healthcare and Patient Engagement**
Healthcare organizations implement Adaptive Cards for patient appointment scheduling, medication reminders, health surveys, and telehealth interfaces. Cards can collect patient symptoms, display appointment details with location information, present medication instructions with images, and facilitate communication between patients and healthcare providers while maintaining HIPAA compliance requirements.

## Best Practices

**Schema Design and Structure**
- **Follow Semantic Hierarchy**: Organize card content using logical information hierarchies that make sense to users and screen readers. Use container elements appropriately to group related information and maintain clear relationships between different sections of the card.
- **Implement Responsive Design Principles**: Design cards that work effectively across different screen sizes and orientations by using flexible layouts, appropriate spacing, and scalable elements. Test cards on various devices to ensure optimal user experience regardless of the viewing context.
- **Optimize for Performance**: Minimize the JSON payload size by avoiding unnecessary nesting, using efficient data structures, and implementing lazy loading for complex content. Consider the network and processing overhead, especially for mobile users or applications with limited resources.

**User Experience and Accessibility**
- **Prioritize Accessibility Standards**: Ensure all interactive elements have appropriate labels, descriptions, and keyboard navigation support. Test cards with screen readers and other assistive technologies to verify compatibility and usability for users with diverse needs.
- **Provide Clear Visual Hierarchy**: Use consistent typography, spacing, and color schemes to guide user attention and create intuitive navigation paths. Implement sufficient color contrast ratios and avoid relying solely on color to convey important information.
- **Design for Touch and Mouse Interaction**: Ensure interactive elements are appropriately sized for both touch and mouse input, with adequate spacing between clickable areas to prevent accidental interactions. Consider the ergonomics of different input methods when positioning buttons and form elements.

**Data Management and Security**
- **Implement Proper Data Validation**: Use client-side validation for immediate user feedback while maintaining server-side validation for security and data integrity. Provide clear error messages and guidance for correcting invalid inputs.
- **Follow Security Best Practices**: Sanitize all user inputs, implement proper authentication and authorization for sensitive actions, and use HTTPS for all data transmission. Avoid storing sensitive information in card definitions and implement appropriate data retention policies.
- **Design for Offline Scenarios**: Consider how cards should behave when network connectivity is limited or unavailable. Implement appropriate caching strategies and provide meaningful feedback when actions cannot be completed due to connectivity issues.

**Development and Deployment**
- **Use Version Control for Card Templates**: Maintain card definitions in version control systems and implement proper change management processes. Use semantic versioning for card templates to ensure compatibility and facilitate rollback procedures when necessary.
- **Implement Comprehensive Testing**: Test cards across all target platforms and devices before deployment. Use automated testing tools where available and maintain test suites that cover various user scenarios, data conditions, and error states.
- **Monitor Performance and Usage**: Implement analytics and monitoring to track card performance, user interactions, and error rates. Use this data to optimize card designs and identify opportunities for improvement in user experience and functionality.

**Integration and Maintenance**
- **Document Card Specifications**: Maintain comprehensive documentation for card schemas, data requirements, and integration procedures. This documentation should be accessible to both technical and non-technical stakeholders involved in card creation and maintenance.
- **Plan for Scalability**: Design card systems that can handle increasing volumes of content and users without degrading performance. Consider caching strategies, content delivery networks, and load balancing for high-traffic scenarios.
- **Establish Governance Policies**: Implement organizational policies for card creation, approval, and maintenance to ensure consistency, quality, and compliance with brand guidelines and regulatory requirements.

## Challenges and Considerations

**Platform Compatibility and Limitations**
- **Renderer Differences**: Different host applications may implement Adaptive Cards renderers with varying levels of feature support, leading to inconsistent user experiences across platforms. Organizations must test cards thoroughly across all target platforms and implement fallback strategies for unsupported features.
- **Version Compatibility**: Managing compatibility between different versions of the Adaptive Cards schema and various renderer implementations can be complex, especially in enterprise environments with mixed technology stacks. Developers need to carefully consider version dependencies and upgrade paths.
- **Performance Variations**: Card rendering performance can vary significantly between platforms and devices, particularly for complex cards with multiple interactive elements or large datasets. Optimization strategies must account for the lowest common denominator while still providing rich experiences where possible.

**Design and User Experience Challenges**
- **Limited Styling Control**: While Adaptive Cards provide theming capabilities, developers have limited control over detailed styling and visual customization compared to custom UI implementations. This limitation can be challenging for organizations with strict brand guidelines or unique design requirements.
- **Complex Interaction Patterns**: Implementing sophisticated user interaction patterns or multi-step workflows within the constraints of the Adaptive Cards schema can be challenging. Some advanced UI patterns may require creative workarounds or may not be feasible within the framework's limitations.
- **Responsive Design Complexity**: Creating cards that work effectively across dramatically different screen sizes and input methods requires careful planning and testing. The framework's responsive capabilities may not address all scenarios, particularly for very complex layouts or specialized use cases.

**Technical Implementation Challenges**
- **Data Binding Complexity**: Complex data binding scenarios, particularly those involving nested loops, conditional logic, or real-time data updates, can be difficult to implement and debug within the JSON schema format. Developers may need to pre-process data or implement complex templating logic.
- **Error Handling and Debugging**: Debugging card rendering issues and user interaction problems can be challenging, especially when issues occur only on specific platforms or under certain conditions. Limited debugging tools and error reporting capabilities can complicate troubleshooting efforts.
- **Integration Complexity**: Integrating Adaptive Cards with existing systems, particularly legacy applications or those with custom authentication schemes, may require significant development effort and architectural changes.

**Security and Compliance Considerations**
- **Data Privacy and Protection**: Ensuring that sensitive data is properly handled within card definitions and during transmission requires careful attention to security practices. Organizations must implement appropriate data protection measures and comply with relevant privacy regulations.
- **Content Security Policies**: Implementing and maintaining content security policies that allow Adaptive Cards to function properly while maintaining security standards can be complex, particularly in environments with strict security requirements.
- **Audit and Compliance Requirements**: Organizations subject to regulatory compliance requirements may need to implement additional controls and monitoring for card content and user interactions, which can add complexity to implementation and maintenance processes.

**Organizational and Process Challenges**
- **Skill Development and Training**: Teams need to develop new skills and understanding of the Adaptive Cards framework, JSON schema design, and cross-platform considerations. This learning curve can impact project timelines and resource allocation.
- **Governance and Quality Control**: Establishing effective governance processes for card creation, review, and deployment requires organizational commitment and clear policies. Without proper governance, card quality and consistency may suffer.
- **Maintenance and Evolution**: Long-term maintenance of card libraries and templates requires ongoing resource commitment and planning for framework updates, platform changes, and evolving business requirements.

## References


1. Microsoft. (n.d.). Adaptive Cards Official Documentation. Microsoft Docs.
2. Microsoft. (n.d.). Adaptive Cards Schema Explorer. Adaptive Cards.
3. Microsoft. (n.d.). Adaptive Cards Designer Tool. Adaptive Cards.
4. Microsoft. (n.d.). GitHub Repository for Adaptive Cards. GitHub.
5. Microsoft. (n.d.). Adaptive Cards SDK Downloads and Documentation. Microsoft Docs.
6. Microsoft. (n.d.). Bot Framework and Adaptive Cards Integration Guide. Azure Bot Service Documentation.
7. Microsoft. (n.d.). Microsoft Teams Adaptive Cards Development Guide. Microsoft Teams Documentation.
8. Microsoft. (n.d.). Adaptive Cards Community Resources and Samples. Adaptive Cards.
