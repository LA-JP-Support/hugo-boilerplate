# Reference Section Heading Guidelines

用語集記事の「参考資料」セクションは、英語・日本語ともに固定見出しで統一します。下記ルールを記事作成プロンプトや翻訳手順に必ず組み込んでください。

## Rules

| 言語 | 見出し | 説明 |
|------|--------|------|
| 英語 | `## References` | 参考文献・リソース・Further Reading など名称はすべてこの見出しに統一する。 |
| 日本語 | `## 参考資料` | 「参考文献」「その他のリソース」などは使わず、この見出しに統一する。 |

どちらの言語でも、見出しの下には実際の参照リンクを Markdown リストで並べます。リストの形式は箇条書き（`-`）で構いません。

## Examples

### English

```markdown
## References
- [OpenAI: Alignment Research](https://openai.com/...)
- [NIST: AI Risk Management Framework](https://www.nist.gov/...)
```

### 日本語

```markdown
## 参考資料
- [OpenAI：アラインメント研究](https://openai.com/...)
- [NIST：AIリスクマネジメントフレームワーク](https://www.nist.gov/...)
```

## Usage Tips

- FlowHunt などでプロンプトを作成する際は、「英語記事は `## References`、日本語記事は `## 参考資料` を必ず使う」と明記しておくと、後処理の正規化が不要になる。
- 既存記事を修正する場合は `scripts/normalize_reference_headings.py` を使うと見出しを一括置換できる。
- 新規翻訳直後は `scripts/enrich_glossary.py` を実行して内部リンクと参考資料見出しを整える。
