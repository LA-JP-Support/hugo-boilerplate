---
title: コードブロック（Python/JS）
translationKey: code-block-python-js
description: コードブロックはプログラミングステートメントをまとめて実行するためのグループで、Pythonではインデントによって、JavaScriptでは波括弧によって定義されます。自動化やチャットボットでカスタムロジックを実装するために使用されます。
keywords:
- コードブロック
- Python
- JavaScript
- 自動化
- チャットボット
- 対話型AI
- 会話AI
- ワークフロー自動化
- 業務自動化
- RPA
- API
- API連携
- インターフェース
category: AI Chatbot & Automation
type: glossary
date: 2025-12-02
draft: false
term: コードブロック（Python/JS）
e-title: Code Block (Python/JS)
---

## コードブロックとは何か？

プログラミングにおけるコードブロックとは、言語のインタープリターやコンパイラが単一の実行単位として扱う連続したコードのセクションです。コードブロックはプログラムの構造化において基本的なもので、関数、ループ、条件文、クラスなどのロジックをカプセル化します。

### Python

Pythonプログラムはコードブロックから構成されています。[Python実行モデル](https://docs.python.org/3/reference/executionmodel.html)によると：

> 「ブロックとは、ひとつの単位として実行されるPythonプログラムテキストの一部です。以下はブロックです：モジュール、関数本体、クラス定義。対話的に入力された各コマンドはブロックです。スクリプトファイル（インタープリタに標準入力として与えられるファイル、またはインタープリタのコマンドライン引数として指定されるファイル）はコードブロックです。コマンドラインから `-m` 引数を使用してトップレベルスクリプト（モジュール `__main__` として）として実行されるモジュールもコードブロックです。組み込み関数 `eval()` と `exec()` に渡される文字列引数はコードブロックです。」

各コードブロックは独自の*実行フレーム*で実行され、スコープ、デバッグ情報、完了時の実行フローを管理します。

### JavaScript

JavaScriptでは、[ブロック文](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)は中括弧 `{}` で区切られた0個以上の文をグループ化するために使用されます。これは「複合文」とも呼ばれます。ブロックは `if`、`for`、`while`、関数宣言などの制御フロー構造に不可欠です。ブロックはまた、`let` と `const` で宣言された変数のスコープを定義します。

例：
```javascript
if (condition) {
    // コードブロック：条件がtrueの場合、ここの文が実行される
}
```

---

## 構文と使用法

### Pythonのコードブロック

Pythonのブロックは一貫したインデント（通常、レベルごとに4つのスペース）によって定義されます（[PEP 8](https://peps.python.org/pep-0008/#indentation)）。インデントはブロックの開始と終了を示し、他の言語の中括弧とは異なります。

**正しい構文の例：**
```python
if age >= 18:
    print("Adult")
    print("Can vote")
print("Done")  # ブロックの外
```
**誤った構文の例：**
```python
if age >= 18:
print("Adult")  # IndentationErrorが発生
```
**重要なポイント：**
- ブロック内のすべての行は同じ量だけインデントする必要があります。
- タブとスペースを混在させるとエラーが発生します。[PEP 8](https://peps.python.org/pep-0008/#tabs-or-spaces)に従って、スペースのみを使用してください。
- 空のブロックは無効です。必要に応じて `pass` をプレースホルダーとして使用してください：
```python
if condition:
    pass  # 何もしない
```

### JavaScriptのコードブロック

JavaScriptのブロックは中括弧で示されます：
```javascript
if (age >= 18) {
    console.log("Adult");
    console.log("Can vote");
}
console.log("Done"); // ブロックの外
```
**誤った構文の例：**
```javascript
if (age >= 18)
    console.log("Adult");
    console.log("Can vote"); // if-ブロックの一部ではない！
```
**ベストプラクティス：** 論理エラーを避け、読みやすさを向上させるために、単一文のブロックでも常に中括弧を使用してください（[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#examples)）。

---

## 命名、バインディング、スコープ

### Python

- 名前（変数）は割り当てられたブロック内でバインドされます。
- ローカル変数は、`global` または `nonlocal` と宣言されない限り、関数またはクラスブロック内で定義されます。[詳細](https://docs.python.org/3/reference/executionmodel.html#binding-of-names)
- 自由変数はブロック内で参照されるが、外部で定義されます。

### JavaScript

- `let` と `const` で宣言された変数はブロックスコープです。
- `var` で宣言された変数は関数スコープであり、ブロックスコープではありません。
- ブロックスコープは、意図しない変数の漏洩やシャドーイングを避けるために重要です。

例：
```javascript
var x = 1;
let y = 1;
if (true) {
  var x = 2; // 外側のxを変更
  let y = 2; // ブロックスコープ
}
console.log(x); // 2
console.log(y); // 1
```
[MDN ブロック文：スコープ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#block_scoping_rules_with_var_or_function_declaration_in_non-strict_mode)

---

## 自動化とチャットボットプラットフォームでの使用

### コードブロックノード

[Contentstack](https://www.contentstack.com/docs/developers/automation-hub-connectors/code-block)、[n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.codeなどの自動化プラットフォームは、ユーザーがカスタムPythonやJavaScriptを埋め込むことができる「コードブロック」ノードを提供しています。

#### 機能：
- **カスタムスクリプティング：** データ変換、検証、外部APIコールのためのカスタムロジックを記述。
- **入出力マッピング：** 前のノードからデータを渡し、それを操作し、下流のノードに結果を出力。
- **デバッグ：** トラブルシューティングのためのコンソールログとエラーレポート。
- **統合：** 標準のドラッグアンドドロップノードでは不可能な操作を可能にします。

#### 例：Contentstack
- JavaScriptコードを実行するためのコードブロックアクションを設定。
- 入力は前のノードからマッピングできます（例：ユーザーデータ、APIレスポンス）。
- `console.log` によるインラインデバッグをサポート。
- [Contentstack コードブロックドキュメント](https://www.contentstack.com/docs/developers/automation-hub-connectors/code-block)

#### 例：n8n
- JavaScriptとPython（Pyodide経由）の両方をサポート。
- 2つの実行モード：「すべてのアイテムに対して一度実行」または「各アイテムに対して一度実行」。
- ワークフローデータにアクセスするための組み込みメソッドと変数。
- [n8n コードノードドキュメント](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code

---

## 実用的な例

### Python：コードブロックノード（チャットボット適格性チェック）
```python
age = input_data.get('age', 0)
if age >= 18:
    result = "Eligible"
else:
    result = "Not eligible"
output = {"eligibility": result}
```
- `input_data` は受信データペイロードです。
- 出力は次の自動化ノードに渡されます。

### JavaScript：データの抽出
```javascript
var idcard = input.IDCard;
var birthday = idcard.substr(6, 4) + '-' + idcard.substr(10, 2) + '-' + idcard.substr(12, 2);
var sex = 'Female';
if (idcard.substr(16, 1) % 2 == 1) {
    sex = 'Male';
}
output = { Birthdate: birthday, Gender: sex };
```

### ネストされたコードブロック

**Python：**
```python
x = 10
if x > 5:
    print("x is greater than 5")
    if x % 2 == 0:
        print("x is even")
```
**JavaScript：**
```javascript
let x = 10;
if (x > 5) {
    console.log("x is greater than 5");
    if (x % 2 === 0) {
        console.log("x is even");
    }
}
```

### ブロックごとの複数のステートメント

**Python：**
```python
for i in range(3):
    print(i)
    print(i * 2)
```
**JavaScript：**
```javascript
for (let i = 0; i < 3; i++) {
    console.log(i);
    console.log(i * 2);
}
```

---

## 一般的な問題とトラブルシューティング

### Python

- **IndentationError：** 一貫性のないインデントによって引き起こされます。常にレベルごとに4つのスペースを使用してください。[PEP 8 – インデント](https://peps.python.org/pep-0008/#indentation)
- **タブとスペースの混在：** 隠れたバグにつながる可能性があります。スペースのみを使用してください。
- **空のブロック：** 許可されていません。プレースホルダーブロックには `pass` を使用してください。

### JavaScript

- **中括弧の欠落：** `{}` を省略すると、特に複数の文がある場合、論理エラーが発生する可能性があります。
- **ブロックスコープ：** `let` と `const` はブロックスコープですが、`var` はそうではありません。変数宣言に注意してください。

### 自動化/チャットボットプラットフォーム

- **入出力の処理：** コードノードがワークフロー要件に一致するデータを期待し、出力することを確認してください。
- **デバッグ：** サポートされているプラットフォーム（例：Contentstack、n8n）ではトラブルシューティングに `console.log` を使用してください。
- **コードフォーマット：** チャットボット、特にMicrosoft Teamsでは、コード用にトリプルバッククォートを使用したMarkdownを使用してください：
    ```
    ```python
    print("Hello, world!")
    ```
    ```
    [Microsoft Teams フォーマットドキュメント](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/format-your-bot-messages)

- **フォーマットの制限：** すべてのフォーマットがすべてのプラットフォーム/デバイスでサポートされているわけではありません。徹底的にテストしてください。

---

## チャットボットでのコードブロックのフォーマット

- **Microsoft Teams ボットメッセージ：** コードブロックフォーマットを有効にするには、`TextFormat` プロパティを `markdown` に設定します。
- **サポートされる機能：** 整形済みテキスト（コードブロック）、太字、斜体、ハイパーリンク。
- **すべてのフォーマットがモバイルクライアントでサポートされているわけではありません。デバイス間でテストしてください。**
- [互換性テーブル付きの公式ドキュメント](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/format-your-bot-messages)

---

## ベストプラクティス

### Python

- インデントレベルごとに4つのスペースを使用してください（[PEP 8](https://peps.python.org/pep-0008/#indentation)）。
- タブとスペースを混在させないでください。
- 空のブロックには `pass` を使用してください。
- コードブロックを明確かつ簡潔に保ってください。

### JavaScript

- 単一の文であっても、ブロックには常に中括弧を使用してください（[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#examples)）。
- ブロックスコープ変数には `let`/`const` を使用してください。
- 変数のシャドーイングに注意してください。

### 自動化/チャットボットプラットフォーム

- 入出力オブジェクトの構造を検証してください。
- サポートされている場所では、デバッグに `console.log` を使用してください。
- 複雑なスクリプトには明確にするためのコメントを追加してください。
- ノード設定とサポートされているライブラリについては、プラットフォームのドキュメントに従ってください（[Contentstack ドキュメント](https://www.contentstack.com/docs/developers/automation-hub-connectors/code-block)、[n8n ドキュメント](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code）。

### チャットボットコードフォーマット

- Microsoft Teamsでは、コードブロック用にMarkdownのトリプルバッククォートを使用してください。
-