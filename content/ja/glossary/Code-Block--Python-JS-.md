---
title: コードブロック(Python/JavaScript)
lastmod: 2026-04-02
translationKey: code-block-python-js
description: コードブロックは、プログラミング言語で文をグループ化して実行単位とするもので、Pythonはインデント、JavaScriptは中括弧で定義します。
keywords:
- コードブロック
- Python
- JavaScript
- 自動化
- プログラミング
category: フレームワーク・ツール
type: glossary
date: 2025-12-19
draft: false
e-title: Code Block (Python/JS)
term: こーどぶろっく
url: "/ja/glossary/code-block--python-js-/"
aliases:
- "/ja/glossary/Code-Block--Python-JS-/"
---

## コードブロック(Python/JavaScript)とは?

**コードブロックは、プログラムを構成する単位のひとつで、言語インタープリタが実行する連続したコード群です。** Pythonではインデント(スペース)でブロック構造を示し、JavaScriptは中括弧{}で囲みます。条件分岐、ループ、関数、クラスなどを定義するときに必要です。

> **ひとことで言うと：** 「関連したコードをまとめて、『ここは1つのまとまり』と言語に教える書き方」です。料理のレシピで「①材料を混ぜる→②加熱する」と手順をグループ分けするのに似ています。

**ポイントまとめ:**

- **何をするものか：** コード内で処理のまとまりを作り、スコープ(変数が有効な範囲)を管理する
- **なぜ必要か：** ブロック構造がないと、プログラムがどこからどこまで1つの処理なのかコンピュータに理解させられない
- **誰が使うか：** すべてのプログラマーが日常的に使う基本的な文法要素

## なぜ重要か

コードブロックは、プログラムの構造と論理を定義するための最も基本的な要素です。ブロックなしでは、複数の文の実行を制御できません。条件によって異なる処理を実行したり、複数回繰り返したりするときに、どのコードが対象なのかを明確にします。また、変数のスコープを管理し、予期しない変数値の変更(バグ)を防ぐ重要な役割も果たします。

## 仕組みをわかりやすく解説

プログラムが実行されるとき、インタープリタやコンパイラはコードを順番に読み進めます。ブロック構造により、「この範囲内の文は一体」と認識します。Pythonはインデント(字下げ)でこれを示すため、視覚的に階層構造が明確です。JavaScriptは中括弧で明示的に範囲を示すため、1行だけの処理でも構造が一目瞭然です。

スコープ(変数の有効範囲)はブロックごとに作られます。ブロック内で定義した変数は、通常そのブロック内でのみ使用できます。ブロック外では参照できません。これにより、変数名の衝突を避け、コード全体を管理しやすくします。

## 実際の活用シーン

**カスタム自動化スクリプト**
n8nやContentStackなどの自動化プラットフォームでは、JavaScriptまたはPythonのコードブロックを直接埋め込めます。ユーザーはコードブロック内で前のステップからのデータを処理し、次のステップへ渡す値を定義します。

**チャットボットロジック**
チャットボットが複数の応答パターンを持つとき、条件に応じた異なるブロックが実行されます。ユーザー入力に応じて、サポートへのエスカレーション、自動応答、データベース参照など、異なるコードブロックが動作します。

**データ変換パイプライン**
APIから受け取ったデータを変換するとき、複数の変換ステップをコードブロックで段階的に処理します。各ブロックが特定の変換を担当し、結果を次のブロックに渡します。

## メリットと注意点

コードブロックは、コードの構造を明確にし、再利用性を高めます。同じロジックを何度も書く代わりに、関数というブロック内に処理をまとめて呼び出すだけで済みます。ただし、ネストが深くなりすぎると、可読性が低下します。通常、3段階程度までが推奨です。また、インデント(Python)や括弧(JavaScript)を正しく使わないと、予期しないエラーや動作が生じます。

## 関連用語

- **[スコープ](./Scope.md)** — ブロック内で定義した変数の有効範囲を決める仕組み
- **[インデント](./Indentation.md)** — Pythonでブロック構造を示すための字下げ
- **[関数](./Function.md)** — コードブロックの一種で、再利用可能な処理をまとめたもの
- **[条件分岐](./Conditional.md)** — if文のように条件に応じて異なるブロックを実行する
- **[ループ](./Loop.md)** — 同じブロック内の処理を繰り返し実行する

## よくある質問

**Q: PythonとJavaScriptでブロックの書き方が異なるのはなぜですか?**
A: プログラミング言語の設計思想が異なります。Pythonはインデントで構造を示すことで、読みやすさを重視しました。JavaScriptは他の多くの言語と同じ中括弧方式を採用し、一貫性を取りました。どちらが良いわけではなく、言語の特性です。

**Q: 空のブロックは作れますか?**
A: Pythonでは空のブロックが許可されていないため、プレースホルダーとして`pass`キーワードを使います。JavaScriptでは空の中括弧{}が許可されます。

**Q: ネストされたブロック(ブロック内のブロック)に制限はありますか?**
A: 技術的に制限はありませんが、可読性の観点から3段階までが推奨されます。それ以上深くなる場合は、関数に分割するなど、コード構造を見直すとよいでしょう。

## 参考資料

- [Python Execution Model - Official Documentation](https://docs.python.org/3/reference/executionmodel.html)
- [PEP 8 Indentation Guide](https://peps.python.org/pep-0008/#indentation)
- [MDN: JavaScript Block Statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
- [JavaScript Control Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [n8n Code Node Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/)
- [AWS Glue Python Shell Jobs](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html)
- [Contentstack Code Block Node](https://www.contentstack.com/docs/developers/automation-hub-connectors/code-block)
- [JavaScript Scope Best Practices](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
- [Python Variable Scope Guide](https://www.w3schools.com/python/python_scope.asp)
- [Indentation in Programming](https://en.wikipedia.org/wiki/Indentation_(typesetting))
