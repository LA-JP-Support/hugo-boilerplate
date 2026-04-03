---
title: "Next.js"
date: 2025-03-01
lastmod: 2026-04-02
description: "A high-performance React-based framework supporting server-side rendering and static generation"
translationKey: "next-js"
category: "Web Development & Design"
type: glossary
draft: false
url: /en/glossary/Next.js/
keywords:
  - React
  - framework
  - server-side rendering
  - web application
---

## What is Next.js?

**Next.js is a full-stack web application framework built on React.** It supports multiple rendering methods including server-side rendering (SSR), static generation (SSG), and incremental static regeneration (ISR), enabling both performance and development efficiency. Developed and maintained by Vercel, it incorporates modern web development best practices.

> **In a nutshell:** "A tool that automatically optimizes and deploys React pages you've written to production environments at high speed."

**Key points:**

- **What it does:** An efficient framework for building websites and applications using React components
- **Why it matters:** Automatically achieves SEO compatibility and page speed optimization so developers can focus on core logic
- **Who uses it:** Web application developers, startups, enterprise companies

## Why it matters

Traditional React applications execute all JavaScript on the browser side. This prevents search engine crawlers from reading page content, creating SEO penalties. Additionally, initial page load times are lengthy, degrading user experience.

Next.js supports server-side rendering by default, speeding up initial loads and enabling search engine compatibility. Moreover, it lets you choose the optimal rendering method per page, supporting everything from static blog pages to dynamic SaaS platforms. Integration with Vercel enables automatic deployment on GitHub push, dramatically improving development speed.

## How it works

Next.js comprises three main elements: file-based routing, rendering engine, and optimization features.

**File-based routing** automatically generates routes by placing files in specific directory structures. Creating `pages/about.js` makes the path `/about` accessible. It's like organizing a library—by arranging files for easy discovery, routing is automatically completed.

**The rendering engine** flexibly selects page generation methods. SSR generates HTML on the server before sending to the browser, so users see complete pages. SSG generates HTML at build time as completely static files for ultra-fast delivery. ISR periodically regenerates static pages, balancing update freshness with speed.

**Optimization features** include automatic code splitting, image optimization, and font optimization. Bundling only necessary code to each page reduces file size and load time. These optimizations directly improve Core Web Vitals, the international standard for performance measurement, and impact search rankings.

## Real-world use cases

**Fast launch of emerging SaaS startups**
Startups need to get products to market quickly. Next.js lets you manage frontend and backend in one project—API route features even enable simple backend functionality. GitHub push triggers automatic Vercel deployment, eliminating custom infrastructure and enabling rapid production launch.

**SEO enhancement for large media sites**
News sites and blog platforms depend on search engine traffic. Using Next.js SSR pre-renders each article page on the server so search crawlers read complete HTML. Setting ISR based on update frequency balances cache efficiency and freshness.

**High-speed global CDN delivery**
Vercel maintains edge servers worldwide, delivering Next.js-generated static pages to users fastest. Japanese users get served from Japan's nearest server, drastically reducing latency and improving experience.

## Benefits and considerations

Next.js's biggest strength is **combining developer experience with production performance**. Hot Module Replacement (HMR) instantly reflects code changes in the browser, improving development efficiency. Optimization features apply automatically, so default output is fast without deep performance consideration.

However, one consideration is that Node.js environments are required, so static hosting services (GitHub Pages, Netlify free tier) don't work. Separate server hosting compatible with Node.js (like Vercel) may be necessary. The learning curve is somewhat steep—React fundamentals are prerequisites. Additionally, new features like App Router change frequently, requiring careful version management.

## Related terms

- **[React](React.md)** — Next.js's foundation UI library; React component knowledge is prerequisite for learning Next.js.
- **[TypeScript](TypeScript.md)** — Widely used for type safety in Next.js projects.
- **[SEO](SEO.md)** — Search engine optimization achieved through Next.js's SSR feature.
- **[Performance Optimization](Performance-Optimization.md)** — The totality of automatic optimization features built into Next.js.
- **[Vercel](Vercel.md)** — Next.js's creator and optimal hosting platform.

## Frequently asked questions

**Q: Does Next.js replace React?**
A: No, Next.js is a framework built on React. React handles "UI component creation" while Next.js handles "whole-page management and optimization." Code written with Next.js still uses React components, so React knowledge is essential.

**Q: Should small websites use Next.js?**
A: For static websites with low update frequency, Next.js benefits may be limited. However, if SEO compatibility is needed or you might add blog functionality later, Next.js is worthwhile. If learning costs are acceptable, it's recommended for skill growth.

**Q: How does Next.js 13's App Router differ from traditional Pages?**
A: App Router is more intuitive with nested layouts, parallel rendering, and streaming features. However, it's still developing—Pages Router has more documentation and examples. Use App Router for new projects, Pages Router for existing ones practically.
