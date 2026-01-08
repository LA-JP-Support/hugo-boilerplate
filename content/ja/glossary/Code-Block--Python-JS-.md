---
title: コードブロック(Python/JS)
lastmod: '2025-12-19'
translationKey: code-block-python-js
description: コードブロックは、統一された実行のためにプログラミング文をグループ化したもので、Pythonではインデント、JavaScriptでは中括弧によって定義されます。自動化やチャットボットにおいて、カスタムロジックの実装に使用されます。
keywords:
- コードブロック
- Python
- JavaScript
- 自動化
- チャットボット
category: AI Chatbot & Automation
type: glossary
date: '2025-12-19'
draft: false
e-title: Code Block (Python/JS)
term: こーどぶろっく(ぱいそん/じぇいえす)
url: "/ja/glossary/Code-Block--Python-JS-/"
---
## コードブロックとは?

プログラミングにおけるコードブロックとは、言語のインタープリタまたはコンパイラが単一の実行可能な単位として扱う、連続したコードのセクションです。コードブロックは、関数、ループ、条件文、クラスなどのロジックをカプセル化し、プログラムを構造化する上で基礎となるものです。

### Python

Pythonプログラムはコードブロックから構成されます。各コードブロックは独自の実行フレーム内で実行され、スコープ、デバッグ情報、および完了時の実行フローを管理します。

Python実行モデルによると:「ブロックとは、単位として実行されるPythonプログラムテキストの一部です。以下がブロックです:モジュール、関数本体、クラス定義。対話的に入力される各コマンドはブロックです。スクリプトファイルはコードブロックです。`-m`引数を使用してコマンドラインからトップレベルスクリプトとして実行されるモジュールもコードブロックです。」

### JavaScript

JavaScriptでは、ブロック文は0個以上の文をグループ化するために使用され、中括弧`{}`で区切られます。これは「複合文」と呼ばれることもあります。ブロックは、`if`、`for`、`while`、関数宣言などの制御フロー構造において不可欠です。ブロックは、`let`および`const`で宣言された変数のスコープも定義します。

<strong>例:</strong>```javascript
if (condition) {
    // code block: statements here are executed if condition is true
}
```

## 構文と使用法

### Pythonのコードブロック

Pythonのブロックは、一貫したインデント(通常はレベルごとに4つのスペース)によって定義されます。インデントは、他の言語の中括弧とは異なり、ブロックの開始と終了を示します。

**正しい構文の例:**```python
if age >= 18:
    print("Adult")
    print("Can vote")
print("Done")  # Outside the block
```

<strong>誤った構文の例:</strong>```python
if age >= 18:
print("Adult")  # Raises IndentationError
```

**重要なポイント:**- ブロック内のすべての行は同じ量だけインデントする必要があります
- タブとスペースを混在させるとエラーが発生します。スペースのみを使用してください
- 空のブロックは無効です。必要に応じて`pass`をプレースホルダーとして使用してください:
```python
if condition:
    pass  # Do nothing
```

### JavaScriptのコードブロック

JavaScriptのブロックは中括弧で示されます:

```javascript
if (age >= 18) {
    console.log("Adult");
    console.log("Can vote");
}
console.log("Done"); // Outside the block
```

**誤った構文の例:**```javascript
if (age >= 18)
    console.log("Adult");
    console.log("Can vote"); // Not part of the if-block!
```

<strong>ベストプラクティス:</strong>単一文のブロックであっても、常に中括弧を使用してください。これにより、ロジックエラーを回避し、可読性が向上します。

## 命名、バインディング、スコープ

### Python

- 名前(変数)は、割り当てられたブロック内でバインドされます
- ローカル変数は、`global`または`nonlocal`として宣言されない限り、関数またはクラスブロック内で定義されます
- 自由変数は、ブロック内で参照されますが、その外部で定義されます

### JavaScript

- `let`および`const`で宣言された変数はブロックスコープです
- `var`で宣言された変数は関数スコープであり、ブロックスコープではありません
- ブロックスコープは、意図しない変数のリークやシャドーイングを回避するために重要です

<strong>例:</strong>```javascript
var x = 1;
let y = 1;
if (true) {
  var x = 2; // modifies outer x
  let y = 2; // block-scoped
}
console.log(x); // 2
console.log(y); // 1
```

## 自動化およびチャットボットプラットフォームでの使用

### コードブロックノード

Contentstack、n8nなどの自動化プラットフォームは、ユーザーがカスタムPythonまたはJavaScriptを埋め込むことができる「コードブロック」ノードを提供しています。

**機能:**- **カスタムスクリプティング:**データ変換、検証、または外部API呼び出しのための独自のロジックを記述
- **入出力マッピング:**前のノードからデータを渡し、それを操作し、下流のノードに結果を出力
- **デバッグ:**トラブルシューティングのためのコンソールログとエラーレポート
- **統合:**標準的なドラッグアンドドロップノードでは不可能な操作を可能にします

**例: Contentstack**JavaScriptコードを実行するためのCode Blockアクションを設定します。入力は、ユーザーデータやAPIレスポンスなど、前のノードからマッピングできます。`console.log`を使用したインラインデバッグをサポートしています。

**例: n8n**JavaScriptとPython(Pyodide経由)の両方をサポートしています。2つの実行モード:「すべてのアイテムに対して1回実行」または「各アイテムに対して1回実行」。ワークフローデータアクセスのための組み込みメソッドと変数があります。

## 実用的な例

### Python: コードブロックノード(チャットボットの適格性チェック)
```python
age = input_data.get('age', 0)
if age >= 18:
    result = "Eligible"
else:
    result = "Not eligible"
output = {"eligibility": result}
```
`input_data`は受信データペイロードです。出力は次の自動化ノードに渡されます。

### JavaScript: データの抽出
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

**Python:**```python
x = 10
if x > 5:
    print("x is greater than 5")
    if x % 2 == 0:
        print("x is even")
```

<strong>JavaScript:</strong>```javascript
let x = 10;
if (x > 5) {
    console.log("x is greater than 5");
    if (x % 2 === 0) {
        console.log("x is even");
    }
}
```

### ブロックごとの複数の文

**Python:**```python
for i in range(3):
    print(i)
    print(i * 2)
```

<strong>JavaScript:</strong>```javascript
for (let i = 0; i < 3; i++) {
    console.log(i);
    console.log(i * 2);
}
```

## 一般的な問題とトラブルシューティング

### Python

**IndentationError**一貫性のないインデントによって引き起こされます。常にレベルごとに4つのスペースを使用してください。

**タブとスペースの混在**隠れたバグにつながる可能性があります。スペースのみを使用してください。

**空のブロック**許可されていません。プレースホルダーブロックには`pass`を使用してください。

### JavaScript

**中括弧の欠落**`{}`を省略すると、特に複数の文がある場合にロジックエラーが発生する可能性があります。

**ブロックスコープ**`let`および`const`はブロックスコープです。`var`はそうではありません。変数宣言には注意してください。

### 自動化/チャットボットプラットフォーム

**入出力の処理**コードノードがワークフロー要件に一致するデータを期待し、出力することを確認してください。

**デバッグ**サポートされているプラットフォーム(Contentstack、n8nなど)では、トラブルシューティングに`console.log`を使用してください。

**コードのフォーマット**チャットボット、特にMicrosoft Teamsでは、コードにトリプルバッククォートを使用したMarkdownを使用してください:
````
```python
print("Hello, world!")
```
````

**フォーマットの制限**すべてのフォーマットがすべてのプラットフォーム/デバイスでサポートされているわけではありません。徹底的にテストしてください。

## チャットボットでのコードブロックのフォーマット

**Microsoft Teams Botメッセージ:**`TextFormat`プロパティを`markdown`に設定して、コードブロックのフォーマットを有効にします。

**サポートされている機能:**整形済みテキスト(コードブロック)、太字、斜体、ハイパーリンク。

**注意:**すべてのフォーマットがモバイルクライアントでサポートされているわけではありません。デバイス間でテストしてください。

## ベストプラクティス

### Python

- インデントレベルごとに4つのスペースを使用
- タブとスペースを決して混在させない
- 空のブロックには`pass`を使用
- コードブロックを明確かつ簡潔に保つ

### JavaScript

- 単一文であっても、ブロックには常に中括弧を使用
- ブロックスコープ変数には`let`/`const`を使用
- 変数のシャドーイングに注意

### 自動化/チャットボットプラットフォーム

- 入出力オブジェクトの構造を検証
- サポートされている場合は、デバッグに`console.log`を使用
- 複雑なスクリプトには明確性のためにコメントを追加
- ノード構成とサポートされているライブラリについては、プラットフォームのドキュメントに従う

### チャットボットのコードフォーマット

- Microsoft Teamsでは、コードブロックにMarkdownトリプルバッククォートを使用
- 単一のメッセージでHTMLとMarkdownの両方を使用することを避ける
- ターゲットクライアント(デスクトップ、iOS、Android)でフォーマットをテスト

## 参考文献


1. Python Software Foundation. (n.d.). Python Execution Model. Python Documentation.
2. Python Software Foundation. (n.d.). PEP 8: Python Style Guide. Python Enhancement Proposals.
3. Python Software Foundation. (n.d.). PEP 8: Indentation. Python Enhancement Proposals.
4. Python Software Foundation. (n.d.). PEP 8: Tabs or Spaces. Python Enhancement Proposals.
5. Mozilla. (n.d.). JavaScript Block Statement. MDN Web Docs.
6. Mozilla. (n.d.). Block Statement Examples. MDN Web Docs.
7. Mozilla. (n.d.). Block Scoping Rules with var. MDN Web Docs.
8. Mozilla. (n.d.). JavaScript Control Flow. MDN Web Docs.
9. Contentstack. (n.d.). Code Block Documentation. Contentstack Docs.
10. n8n. (n.d.). Code Node Documentation. n8n Documentation.
11. Microsoft. (n.d.). Bot Message Formatting. Microsoft Teams Documentation.
12. Stack Overflow. (n.d.). Python Blocks. Stack Overflow.
13. Mimo. (n.d.). Python Glossary - Code Block. Mimo Learning Platform.
