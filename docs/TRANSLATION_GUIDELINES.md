# Translation Guidelines for AI Translation APIs

## Overview
This document provides guidelines for translating English content to Japanese using AI translation APIs (e.g., Claude, GPT-4, DeepL). These guidelines ensure high-quality translations that maintain proper formatting for Hugo static sites and internal linking systems.

## Critical Formatting Rules

### 1. Markdown Bold Syntax (`**text**`)

**IMPORTANT**: Keep bold markdown syntax tight around the actual word, excluding Japanese particles.

❌ **WRONG**:
```markdown
**Anthropicの**Claude
**Googleの**Gemini
**Microsoftの**Copilot
```

✅ **CORRECT**:
```markdown
**Anthropic**のClaude
**Google**のGemini
**Microsoft**のCopilot
```

**Rule**: Japanese particles (の、は、が、を、に、へ、と、から、まで、より、で、や) should NEVER be included inside bold markdown syntax.

### 2. Bold Syntax with Japanese Punctuation (Brackets, Parentheses)

**IMPORTANT**: CommonMark specification causes bold syntax to fail when Japanese punctuation (括弧、句読点) is adjacent to `**`. Use **Zero Width Space** (`&#8203;`) instead of `<strong>` tags.

**Problem**: Japanese punctuation (約物) like `）`、`」`、`。` prevents `**` from being recognized as emphasis markers.

❌ **WRONG** (bold not rendered):
```markdown
**アジアリージョン（シンガポール）**を推奨
**「強調表示」**と**「太字」**で表示
```

✅ **CORRECT** (using Zero Width Space `&#8203;`):
```markdown
**アジアリージョン（シンガポール）**&#8203;を推奨
**「強調表示」**&#8203;と**「太字」**&#8203;で表示
```

**Rule**: Add `&#8203;` (Zero Width Space) immediately after the closing `**` when:
- The bold text ends with Japanese punctuation: `）`、`」`、`】`、`》`、`。`、`、`
- The bold text is followed by Japanese text without space

**Why Zero Width Space instead of `<strong>` tags?**

| Method | Pros | Cons |
|--------|------|------|
| `&#8203;` | Markdown readable, minimal change | Invisible character (may confuse copy-paste) |
| `<strong>` | Always works | Harder to read in Markdown, verbose |

**Recommendation**: Use `&#8203;` for cleaner Markdown source. The zero-width character is invisible in rendered output.

**HTML Entity Reference**:
| Entity | Name | Unicode |
|--------|------|------|
| `&#8203;` | Zero Width Space | U+200B |
| `&#65279;` | Zero Width No-Break Space | U+FEFF |

### 3. Bold Markdown Closure

**IMPORTANT**: Every opening `**` must have a corresponding closing `**`.

❌ **WRONG**:
```markdown
**トークンと呼ばれます。トークンは単語ではありません
```

✅ **CORRECT**:
```markdown
**トークン**と呼ばれます。トークンは単語ではありません
```

**Rule**: Always close bold markdown syntax immediately after the word or phrase that should be bold.

### 4. Proper Nouns and Technical Terms

**IMPORTANT**: Keep proper nouns and technical terms in their original form when they are commonly used in English.

✅ **KEEP IN ENGLISH**:
- ChatGPT
- API
- Claude
- Gemini
- Copilot
- GitHub
- Anthropic
- OpenAI
- Microsoft
- Google
- Meta
- DeepSeek
- Mistral
- LLM (Large Language Model)
- AI
- ML (Machine Learning)
- NLP (Natural Language Processing)
- REST API
- JSON
- YAML
- Markdown
- Hugo
- Git

**Rule**: Do not translate widely-recognized technical terms and brand names.

### 5. Line Length and Readability

**IMPORTANT**: Break long paragraphs into multiple lines for better readability in Markdown editors.

❌ **WRONG** (one very long line):
```markdown
複数の言語モデルが利用可能になったため、特定のニーズに適したものを選択するには、異なるオプションの長所と短所を理解する必要があります。**ChatGPT**は、正当な理由で最も人気のある選択肢であり続けています—機能が豊富で、広く利用可能で、幅広いタスクで優れたパフォーマンスを発揮します。
```

✅ **CORRECT** (broken into readable lines):
```markdown
複数の言語モデルが利用可能になったため、特定のニーズに適したものを選択するには、異なるオプションの長所と短所を理解する必要があります。

**ChatGPT**は、正当な理由で最も人気のある選択肢であり続けています—機能が豊富で、広く利用可能で、幅広いタスクで優れたパフォーマンスを発揮します。
```

**Rule**: Break paragraphs at natural sentence boundaries. Aim for 1-3 sentences per line.

### 6. Hugo Frontmatter

**IMPORTANT**: Preserve the structure and format of Hugo frontmatter.

✅ **CORRECT**:
```yaml
---
title: 大規模言語モデルを効果的に使う方法
description: ChatGPTのような大規模言語モデルの実用的な活用方法を学ぶ
keywords:
  - 大規模言語モデル
  - ChatGPT
  - AI
tags:
  - AI
  - ChatGPT
  - 生産性
---
```

**Rule**: 
- Keep frontmatter keys in English
- Translate only the values
- Maintain YAML/TOML syntax
- Keep array/list formatting intact

### 7. Links and URLs

**IMPORTANT**: Do not translate URLs or link syntax.

✅ **CORRECT**:
```markdown
[ChatGPT](https://chat.openai.com/)の詳細については、こちらをご覧ください。
```

**Rule**: Keep all URLs, anchor links, and Markdown link syntax unchanged.

### 8. Code Blocks and Inline Code

**IMPORTANT**: Never translate content inside code blocks or inline code.

✅ **CORRECT**:
```markdown
`ChatGPT`のようなモデルは、`temperature`パラメータを使用します。

\`\`\`python
model = "gpt-4"
temperature = 0.7
\`\`\`
```

**Rule**: Content between backticks (`` ` ``) or in code fences (` ``` `) should remain unchanged.

## Translation Prompt Template

Use this prompt template when requesting translations from AI APIs:

```
Translate the following English Markdown content to Japanese. Follow these critical rules:

1. BOLD SYNTAX: Keep bold markdown (**) tight around words, excluding Japanese particles
   - WRONG: **Anthropicの**
   - CORRECT: **Anthropic**の

2. JAPANESE PUNCTUATION: Add &#8203; after closing ** when bold ends with brackets/punctuation
   - WRONG: **アジア（シンガポール）**を (bold fails)
   - CORRECT: **アジア（シンガポール）**&#8203;を

3. CLOSURE: Every opening ** must have a closing **
   - WRONG: **トークンと呼ばれます。
   - CORRECT: **トークン**と呼ばれます。

4. PROPER NOUNS: Keep technical terms and brand names in English
   - Keep: ChatGPT, API, Claude, Gemini, GitHub, etc.

5. LINE BREAKS: Break long paragraphs at sentence boundaries for readability

6. FRONTMATTER: Translate only values, keep keys and syntax unchanged

7. LINKS: Do not translate URLs or link syntax

8. CODE: Never translate content in code blocks or inline code

Content to translate:
[PASTE CONTENT HERE]
```

## Quality Checklist

After translation, verify:

- [ ] All bold syntax (`**`) is properly opened and closed
- [ ] Japanese particles are outside bold syntax
- [ ] Bold text ending with Japanese punctuation has `&#8203;` after closing `**`
- [ ] Technical terms and brand names remain in English
- [ ] Frontmatter structure is intact
- [ ] URLs and links are unchanged
- [ ] Code blocks and inline code are unchanged
- [ ] Paragraphs are broken into readable lines
- [ ] No markdown syntax errors

## Common Mistakes to Avoid

### Mistake 1: Including particles in bold
```markdown
❌ **Anthropicの**Claude
✅ **Anthropic**のClaude
```

### Mistake 2: Unclosed bold syntax
```markdown
❌ **トークンと呼ばれます。トークンは...
✅ **トークン**と呼ばれます。トークンは...
```

### Mistake 3: Translating technical terms
```markdown
❌ チャットジーピーティー (ChatGPT)
✅ ChatGPT
```

### Mistake 4: Bold not rendered with Japanese brackets
```markdown
❌ **アジアリージョン（シンガポール）**を推奨
   (Bold syntax ignored because of Japanese parentheses)
✅ **アジアリージョン（シンガポール）**&#8203;を推奨
   (Zero Width Space enables bold rendering)
```

### Mistake 5: Breaking markdown links
```markdown
❌ [チャットGPT](https://チャット.openai.com/)
✅ [ChatGPT](https://chat.openai.com/)
```

### Mistake 6: Very long lines
```markdown
❌ 複数の言語モデルが利用可能になったため、特定のニーズに適したものを選択するには、異なるオプションの長所と短所を理解する必要があります。**ChatGPT**は、正当な理由で最も人気のある選択肢であり続けています—機能が豊富で、広く利用可能で、幅広いタスクで優れたパフォーマンスを発揮します。言語モデルを始めたばかりの場合、安全なデフォルトの選択です。

✅ 複数の言語モデルが利用可能になったため、特定のニーズに適したものを選択するには、異なるオプションの長所と短所を理解する必要があります。

**ChatGPT**は、正当な理由で最も人気のある選択肢であり続けています—機能が豊富で、広く利用可能で、幅広いタスクで優れたパフォーマンスを発揮します。言語モデルを始めたばかりの場合、安全なデフォルトの選択です。
```

## Automated Validation

Consider using these regex patterns to validate translations:

```regex
# Find particles inside bold (should be zero matches)
\*\*[^\*]+[のはがをにへとからまでよりでや]\*\*

# Find unclosed bold syntax (should be zero matches)
\*\*[^\*]+$

# Find very long lines (>500 characters)
^.{500,}$
```

## Version History

- **v1.1.0** (2026-02-03): Added Zero Width Space rule for Japanese punctuation
  - New section: "Bold Syntax with Japanese Punctuation"
  - `&#8203;` as alternative to `<strong>` tags
  - Updated prompt template and quality checklist
  - Added Mistake 4 example

- **v1.0.0** (2026-01-07): Initial guidelines created
  - Bold syntax rules
  - Proper noun handling
  - Line length recommendations
  - Quality checklist

---

**Last Updated**: 2026-02-03  
**Maintainer**: SmartWeb Team
