# Glossary Article Optimization Guide

## Mission
Optimize all glossary articles in `/content/en/glossary/` to a consistent, content-marketing-friendly format.

## Target Specifications

### Length & Reading Time
- **Word count**: 2,600-2,800 words
- **Reading time**: 13-14 minutes
- **Format balance**: 30% prose, 70% structured content

### Article Structure

#### REQUIRED SECTIONS
1. **What is [Term]?** - Core definition (2-3 paragraphs, prose)
2. **Core Concepts/Key Features** - Main features (bullet points with 1-2 sentence descriptions)
3. **References** - All external links consolidated at end

#### OPTIONAL SECTIONS (include based on content)
- How It Works / Technical Architecture
- Benefits / Advantages
- Use Cases / Examples
- Best Practices
- Challenges / Considerations
- FAQ

### Formatting Rules

**✓ DO:**
- Use **bold subheadings** for scannability
- Bullet points for features, benefits, lists
- Short paragraphs (3-4 sentences) for prose
- Clear, concise language
- Specific examples where relevant
- Maintain technical accuracy
- Keep SEO keywords natural

**✗ DON'T:**
- No inline external links (move to References)
- No redundant explanations
- No over-explanation
- No excessive headers
- Don't remove internal links (handled separately)

### References Section Format
```markdown
## References

- [Title - Source](URL)
- [Title - Source](URL)
```

## Content Optimization Strategy

1. **Cut redundancy** by 25-30%
2. **Combine** related concepts
3. **Use specific examples** where relevant
4. **Maintain** technical accuracy
5. **Preserve** frontmatter exactly as-is

## Reference Examples

### Example 1: AI Chatbot (Technology Article)
See: `/content/en/glossary/AI-chatbot.md`
- Strong definition section (prose)
- Technical concepts with bullet points
- Balanced structure
- Clean References section

### Example 2: RAG (Technical Deep-Dive)
See: `/content/en/glossary/RAG.md`
- Technical architecture explained clearly
- Implementation best practices
- FAQ section

### Example 3: LiveAgent (Product Article)
See: `/content/en/glossary/LiveAgent.md`
- Feature-focused structure
- Use case examples
- Affiliate links in References
- Implementation guide

## Batch Processing Workflow

### For Each Batch (5 files):

1. **Read** all 5 files
2. **Analyze** content structure
3. **Optimize** each following the guide
4. **Write** optimized versions to original filenames
5. **Report** summary (word counts, changes made)

### Quality Checklist (Per Article)

- [ ] Frontmatter preserved exactly
- [ ] Word count: 2,600-2,800
- [ ] Definition section: 2-3 paragraphs prose
- [ ] Structured sections: bullet points
- [ ] No inline external links
- [ ] References section: all links consolidated
- [ ] No redundancy
- [ ] Technical accuracy maintained
- [ ] SEO keywords natural

## Processing Commands

### User Provides:
```
Batch X:
- File1.md
- File2.md
- File3.md
- File4.md
- File5.md
```

### Claude Executes:
1. Read all 5 files
2. Optimize each
3. Write back to original paths
4. Report: "Batch X complete: [word counts]"

## Important Notes

- **Preserve frontmatter** - never modify YAML
- **Backup exists** - original files saved as -OLD
- **No API required** - processing in-session
- **Consistent quality** - use examples as templates
- **LiveAgent URLs** - add `#interworkcorp` to all LiveAgent links

## File Paths

- **Glossary location**: `/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/content/en/glossary/`
- **Reference examples**: AI-chatbot.md, RAG.md, LiveAgent.md
- **Backup pattern**: `{original-name}-OLD.md`

## Success Metrics

- Consistent 2,600-2,800 word count across all articles
- Improved scannability (headers, bullets)
- Reduced redundancy (25-30% shorter than originals)
- Clean References section (no inline links)
- Preserved technical accuracy
- SEO-friendly structure
