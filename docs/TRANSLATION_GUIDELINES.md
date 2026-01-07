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

### 2. Bold Markdown Closure

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

### 3. Proper Nouns and Technical Terms

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

### 4. Line Length and Readability

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

### 5. Hugo Frontmatter

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

### 6. Links and URLs

**IMPORTANT**: Do not translate URLs or link syntax.

✅ **CORRECT**:
```markdown
[ChatGPT](https://chat.openai.com/)の詳細については、こちらをご覧ください。
```

**Rule**: Keep all URLs, anchor links, and Markdown link syntax unchanged.

### 7. Code Blocks and Inline Code

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

2. CLOSURE: Every opening ** must have a closing **
   - WRONG: **トークンと呼ばれます。
   - CORRECT: **トークン**と呼ばれます。

3. PROPER NOUNS: Keep technical terms and brand names in English
   - Keep: ChatGPT, API, Claude, Gemini, GitHub, etc.

4. LINE BREAKS: Break long paragraphs at sentence boundaries for readability

5. FRONTMATTER: Translate only values, keep keys and syntax unchanged

6. LINKS: Do not translate URLs or link syntax

7. CODE: Never translate content in code blocks or inline code

Content to translate:
[PASTE CONTENT HERE]
```

## Quality Checklist

After translation, verify:

- [ ] All bold syntax (`**`) is properly opened and closed
- [ ] Japanese particles are outside bold syntax
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

### Mistake 4: Breaking markdown links
```markdown
❌ [チャットGPT](https://チャット.openai.com/)
✅ [ChatGPT](https://chat.openai.com/)
```

### Mistake 5: Very long lines
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

- **v1.0.0** (2026-01-07): Initial guidelines created
  - Bold syntax rules
  - Proper noun handling
  - Line length recommendations
  - Quality checklist

---

**Last Updated**: 2026-01-07  
**Maintainer**: SmartWeb Team
