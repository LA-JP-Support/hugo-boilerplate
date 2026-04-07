# SmartWeb Design System

> Extends: `interwork-ops/DESIGN.md`（エコシステム共通トークン）

Hugo + Gulp + Tailwind CSS v3

---

## General Rules

- 絵文字は原則禁止（ユーザーから明示的に依頼がある場合のみ使用可）
- 日本語テキストにイタリック体を使用しない
- エコシステム共通ルールを継承

---

## Primary Color

Base: `#2563eb` (blue-600) with 11-step CSS variable scale (RGB format)

```
--color-primary:     37 99 235;   /* #2563eb DEFAULT */
--color-primary-50:  239 246 255; /* #eff6ff */
--color-primary-600: 37 99 235;   /* #2563eb */
--color-primary-700: 29 78 216;   /* #1d4ed8 */
--color-primary-950: 23 37 84;    /* #172554 */
```

Tailwind: `bg-primary-600`, `text-primary-500`, `border-primary-300`

---

## Typography

| Role | Stack |
|------|-------|
| Sans (default) | `Inter` (Variable), `Hiragino Kaku Gothic ProN`, `Hiragino Sans`, `Yu Gothic`, `Meiryo`, sans-serif |
| Serif | `Hiragino Mincho ProN`, `Yu Mincho`, serif |
| Mincho class | `.font-mincho` — `Noto Serif JP`, `Yu Mincho`, `Hiragino Mincho ProN`, serif |

Inter is loaded as Variable Font from `/fonts/inter/Inter-VariableFont_opsz,wght.woff2`

---

## Button Color System

3 types, each with light/dark variants:

### Primary

| State | Light | Dark |
|-------|-------|------|
| Default | `#2563eb` | `#3b82f6` |
| Hover | `#1d4ed8` | `#60a5fa` |

### Secondary

| State | Light | Dark |
|-------|-------|------|
| Background | white | - |
| Text | `#111827` | white |
| Border | `#d1d5db` | `#4b5563` |

### Text

| State | Light | Dark |
|-------|-------|------|
| Default | `#111827` | white |
| Hover | `#6b7280` | `#60a5fa` |

---

## Brand Semantic Tokens

| Token | Light | Dark |
|-------|-------|------|
| `brand-surface` | primary-600 | primary-500 |
| `brand-border` | primary-500 | primary-400 |
| `brand-text` | primary-600 | primary-300 |

---

## Dark Mode

- Trigger: `<html class="dark">` (Tailwind `darkMode: 'class'`)
- Backgrounds: `dark:bg-gray-900` (main), `dark:bg-gray-800` (alternate)
- Text: `dark:text-gray-100`

---

## Blockquote

```css
border-left: 4px solid #3b82f6;
background-color: #f9fafb;
border-radius: 0.5rem;
```

Dark: `background: linear-gradient(135deg, #1e293b, #334155)`, border `#60a5fa`

---

## Tailwind Plugins

- `@tailwindcss/typography`
- `@tailwindcss/forms`
- `@tailwindcss/aspect-ratio`

---

## Product Gradient

```
from-[#1a1a2e] via-[#16213e] to-[#0f3460]
```
