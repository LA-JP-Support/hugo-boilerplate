---
title: "Linkbuilding Reproduction Test"
date: 2026-01-08
---

# Linkbuilding Reproduction Test

## User Reported Cases

1. <strong>検索拡張生成(RAG)とキャッシュ拡張生成(CAG)</strong>
   - Expect link on: 検索拡張生成, RAG, キャッシュ拡張生成, CAG

2. <strong>これはCAGシナリオです。</strong>
   - Expect link on: CAG

3. <strong>これは明らかにRAGシナリオです。</strong>
   - Expect link on: RAG

## Other Patterns

4. 普通の文中のRAGとCAG。
   - Expect link on: RAG, CAG

5. <strong>機械学習(ML)</strong>は<strong>人工知能(AI)</strong>の一分野です。
   - Expect link on: 機械学習, ML, 人工知能, AI

6. 交通信号と通信信号
   - Expect NO link on: "通信" inside "交通信号" or "通信信号" (unless "交通信号" or "通信信号" themselves are keywords)

## Bold Rendering Issues

<strong>Security Assertion Markup Language(SAML)</strong>は、アイデンティティプロバイダーと... (Paragraph Start)

7. <strong>Security Assertion Markup Language(SAML)</strong>
   - Pattern: Bold text followed immediately by parentheses.

8. <strong>チームの自律性:</strong>小規模なチーム
   - Pattern: Bold text followed immediately by colon and text (no space).

9. <strong>OpenID Connect(OIDC)</strong>
   - Pattern: Bold text followed immediately by parentheses.

10. <strong>Bold Text</strong>WithSuffix
    - Pattern: Bold text followed immediately by text (no space).

11. <strong>Bold</strong>は
    - Pattern: Bold text followed immediately by Japanese text.
