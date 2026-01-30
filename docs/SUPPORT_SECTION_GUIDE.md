# Support Section Implementation Guide

## Overview

The `/support` section uses a custom LotusDocs-inspired layout designed specifically for documentation and knowledge base content. This implementation provides a modern, user-friendly documentation experience without requiring a full theme replacement.

**Version:** 1.0.0  
**Date:** 2026-01-30  
**Status:** Production Ready

---

## Features

### 1. **Three-Column Layout**
- **Left Sidebar:** Hierarchical navigation with collapsible sections
- **Main Content:** Article content with breadcrumbs and prev/next navigation
- **Right Sidebar (XL screens):** Table of contents for current page

### 2. **Responsive Design**
- **Desktop (lg+):** Full three-column layout with fixed sidebars
- **Tablet:** Two-column layout (main + left sidebar)
- **Mobile:** Single column with hamburger menu for navigation

### 3. **Navigation Features**
- Automatic sidebar generation from content structure
- Active page highlighting
- Collapsible category sections
- Previous/Next page navigation at bottom of articles
- Breadcrumb navigation

### 4. **Documentation-Focused Styling**
- Clean, readable typography
- Proper heading hierarchy
- Code block styling
- Hover effects and transitions
- Dark mode support

---

## File Structure

```
layouts/
├── support/
│   ├── single.html          # Individual article layout
│   └── list.html            # Category/section listing layout
└── partials/
    └── support/
        └── sidebar-nav.html # Sidebar navigation component

content/
├── ja/
│   └── support/
│       ├── _index.md
│       ├── getting-started/
│       │   ├── _index.md
│       │   └── *.md
│       ├── ticket-system/
│       ├── settings/
│       └── ...
└── en/
    └── support/
        └── _index.md (ready for content)
```

---

## Content Organization

### Directory Structure

```
content/{lang}/support/
├── _index.md                    # Support home page
├── category-name/
│   ├── _index.md               # Category overview
│   ├── article-1.md            # Individual articles
│   ├── article-2.md
│   └── subcategory/
│       ├── _index.md
│       └── article.md
```

### Front Matter Requirements

#### Section Index (`_index.md`)
```yaml
---
title: "Category Title"
description: "Brief description of this category"
weight: 10                      # Controls order in sidebar
type: support                   # Required for proper layout
---
```

#### Individual Articles
```yaml
---
title: "Article Title"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "unique-key"    # For multilingual linking
description: "Article description"
keywords: ["keyword1", "keyword2"]
type: support                   # Required for proper layout
category: "category-name"       # Optional
---
```

---

## Sidebar Navigation

### How It Works

The sidebar automatically generates navigation from:
1. **Sections:** Subdirectories with `_index.md` files
2. **Pages:** Individual `.md` files within sections
3. **Hierarchy:** Nested sections create collapsible groups

### Ordering

- Sections are ordered by `weight` parameter in front matter
- Lower weight = appears first
- Pages within sections also use `weight`

### Example Structure

```
support/
├── getting-started/     (weight: 10)
│   ├── article-1.md    (weight: 1)
│   └── article-2.md    (weight: 2)
├── ticket-system/      (weight: 20)
│   ├── tickets/        (nested section)
│   └── automation/
└── settings/           (weight: 30)
```

---

## Styling Customization

### Color Scheme

The layout uses Tailwind CSS classes with your existing color scheme:
- **Primary:** Indigo (`indigo-600`, `indigo-400`)
- **Background:** White/Gray (`gray-50`, `gray-900`)
- **Text:** Gray scale (`gray-900`, `gray-600`, etc.)

### Dark Mode

All components support dark mode via Tailwind's `dark:` prefix:
```html
class="text-gray-900 dark:text-white"
```

### Custom Styling

To customize, edit the `<style>` blocks in:
- `layouts/support/single.html`
- `layouts/support/list.html`

---

## Menu Integration

The support section is added to the main navigation menu in `hugo.toml`:

```toml
# Japanese
[[languages.ja.menu.main]]
  identifier = "support"
  name = "サポート"
  url = "/support/"
  weight = 7

# English
[[languages.en.menu.main]]
  identifier = "support"
  name = "Support"
  url = "/support/"
  weight = 7
```

---

## Multilingual Support

### Current Status
- ✅ Japanese (`/ja/support/`) - Fully populated with content
- ✅ English (`/en/support/`) - Structure ready, awaiting content

### Adding Translations

1. Create matching directory structure in `content/en/support/`
2. Use same `translationKey` in front matter for linked articles
3. Translate content while maintaining same structure

Example:
```
content/ja/support/getting-started/start-liveagent-first-time.md
content/en/support/getting-started/start-liveagent-first-time.md
```

Both should have:
```yaml
translationKey: "start-liveagent-first-time"
```

---

## Table of Contents

### Automatic TOC Generation

The right sidebar (XL screens) automatically displays a table of contents based on:
- H2 headings (`##`)
- H3 headings (`###`)
- H4 headings (`####`)

### Configuration

Hugo's built-in TOC is used. Configure in `hugo.toml`:
```toml
[markup.tableOfContents]
  endLevel = 3
  startLevel = 2
```

---

## Mobile Experience

### Hamburger Menu

On mobile devices:
1. Sidebar is hidden by default
2. "Menu" button appears at top
3. Clicking opens overlay sidebar
4. Clicking outside or X closes sidebar

### Touch Optimization

- Large tap targets (44px minimum)
- Swipe-friendly navigation
- Optimized font sizes for mobile

---

## Testing Checklist

- [ ] Desktop layout (1280px+): Three columns visible
- [ ] Tablet layout (1024px): Two columns (main + sidebar)
- [ ] Mobile layout (<1024px): Single column with hamburger menu
- [ ] Sidebar navigation: Categories expand/collapse
- [ ] Active page highlighting works
- [ ] Breadcrumb navigation displays correctly
- [ ] Prev/Next navigation works
- [ ] Table of contents (XL screens) tracks scroll
- [ ] Dark mode styling correct
- [ ] All links functional

---

## Performance Considerations

### Optimizations
- Fixed sidebars use `position: fixed` for smooth scrolling
- JavaScript is minimal and vanilla (no dependencies)
- CSS is inline in templates (no external requests)
- Images should be optimized before upload

### Best Practices
- Keep articles focused (< 3000 words ideal)
- Use proper heading hierarchy
- Optimize images (WebP format, compressed)
- Avoid excessive nesting (max 3 levels)

---

## Troubleshooting

### Sidebar Not Showing
- Check `type: support` in front matter
- Verify `_index.md` exists in category directories
- Check `weight` parameters are set

### Navigation Not Updating
- Clear Hugo cache: `hugo --cleanDestinationDir`
- Check file paths match exactly
- Verify no duplicate `translationKey` values

### Styling Issues
- Check Tailwind CSS is properly configured
- Verify dark mode classes are present
- Test in different browsers

### Mobile Menu Not Working
- Check JavaScript console for errors
- Verify element IDs match in HTML and JS
- Test on actual mobile device (not just browser resize)

---

## Future Enhancements

### Planned Features
- [ ] Search functionality within support section
- [ ] Feedback widget on articles
- [ ] Print-friendly styling
- [ ] Export to PDF option
- [ ] Related articles suggestions
- [ ] Article rating system

### Integration Opportunities
- Internal linking system (already implemented for blog/glossary)
- Analytics tracking for popular articles
- LiveAgent widget integration
- AI chatbot for support queries

---

## Maintenance

### Regular Tasks
1. **Content Updates:** Keep articles current with product changes
2. **Link Checking:** Verify internal/external links periodically
3. **Performance:** Monitor page load times
4. **User Feedback:** Collect and act on user suggestions

### Version Control
- Document major changes in this guide
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Tag releases in Git

---

## Support

For questions or issues with this implementation:
1. Check this guide first
2. Review existing content structure in `content/ja/support/`
3. Examine layout files for reference
4. Test changes locally before deploying

---

## Changelog

### Version 1.0.0 (2026-01-30)
- Initial implementation
- Three-column responsive layout
- Sidebar navigation with collapsible sections
- Table of contents on XL screens
- Breadcrumb navigation
- Prev/Next article navigation
- Mobile hamburger menu
- Dark mode support
- Bilingual structure (JA/EN)
