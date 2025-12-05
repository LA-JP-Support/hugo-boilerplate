---
title: イテレーター / For-Each
translationKey: iterator-for-each
description: イテレーターまたはfor-each構文は、リストやコレクション内のアイテムを1つずつ処理し、各要素に対して読み取り、更新、タスクの自動化などのアクションを実行できるようにします。
keywords: ["イテレーター", "for-eachループ", "コレクション処理", "ワークフロー自動化", "プログラミング概念"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: いてれーたー / ふぉーいーち
reading: イテレーター / For-Each
kana_head: あ
e-title: Iterator / For-Each
---
## イテレーター / For-Eachとは?

**イテレーター:**  
イテレーターは、コレクション(リスト、配列、マップなど)を走査し、各項目を一つずつ処理できるようにするオブジェクトまたはロジックブロックです。イテレーターは、ほぼすべての現代的なプログラミング言語においてコレクション処理の中核を担っています。コレクションがメモリ内でどのように構造化されているかに関わらず、各項目に順次アクセスする標準化された方法を提供します。例えば、Javaでは、[Iterator](https://www.w3schools.com/java/java_iterator.asp)インターフェースを使用することで、インデックスや内部データ構造の詳細を直接扱うことなく、`ArrayList`、`HashSet`、その他のコレクションをループ処理できます。

**For-Each構文:**  
for-each構文(for-eachループ、foreach文、またはイテレーターブロックとも呼ばれる)は、コレクション内のすべての項目に対してコードブロックを実行し、イテレーションの詳細を抽象化します。多くの言語では、これを組み込みステートメントとして提供しています—JavaScriptの`for ... of`、C#の`foreach`、Javaの拡張`for`ループなどです。これらの構文は、Relay.appのようなワークフロー自動化ツールでも基本機能となっており、イテレーターブロックがリスト内の各項目を段階的に処理します([Relay.app Docs](https://docs.relay.app/flow-control/iterators))。

> **重要ポイント:**  
> イテレーターとfor-each構文は、コレクション処理を簡素化し、オフバイワンエラーの可能性を減らし、コードをより読みやすく保守しやすくします。これらはプログラミングとワークフロー自動化の両方において基礎的な要素です。

## イテレーターの技術的説明

### イテレーターの構成要素

イテレーターは、シーケンス内の次の項目を返すメカニズムと、項目が残っていないことを通知する機能を提供する必要があります。これは多くの言語で*イテレータープロトコル*として形式化されています:

- **イテレータープロトコル:**  
  オブジェクトは、`next()`メソッド(JavaScript、Python、Java)や`MoveNext()`/`Current`(C#)などの特定のインターフェースを実装する必要があります。
- **消費:**  
  イテレーターは通常、処理中に*消費*されます—終端に達すると、リセットや再利用はできません。コレクションを再度走査したい場合は、新しいイテレーターオブジェクトを作成する必要があります。

#### 言語別プロトコル概要

- **Python:**  
  `__iter__()`と`__next__()`メソッドを実装するオブジェクトは、イテレータープロトコルに準拠します。リストやその他のコレクションは*イテラブル*であり、`iter()`を呼び出すとイテレーターが生成されます([GeeksforGeeks](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/))。
- **JavaScript:**  
  `{value, done}`を返す`next()`メソッドを実装するオブジェクトは、[Iteratorプロトコル](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterators)に準拠したイテレーターです。多くの組み込み型(Array、String、Set、Map)はイテラブルであり、`[Symbol.iterator]()`メソッドがイテレーターを生成します。
- **Java:**  
  `Iterator<E>`インターフェースを実装するオブジェクトは、`hasNext()`、`next()`、およびオプションで`remove()`を提供します([W3Schools](https://www.w3schools.com/java/java_iterator.asp))。
- **C#:**  
  [IEnumerator](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerator)と[IEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable)インターフェースがプロトコルを定義します。
- **ワークフロー自動化(Relay.app):**  
  イテレーターブロックは、リスト内の各項目を視覚的に処理します。ツールがイテレーションロジックを処理します([Relay.app Docs](https://docs.relay.app/flow-control/iterators))。

### イテレーター vs イテラブル

- **イテラブル:**  
  イテレーターを生成できるオブジェクト(例:リスト、配列、セット)。
- **イテレーター:**  
  イテラブルから一度に一つの項目を実際に提供するオブジェクト。

*Pythonでは、すべてのイテレーターはイテラブルでもありますが、すべてのイテラブルがイテレーターであるわけではありません*([GeeksforGeeks](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/))。

## For-Each構文:目的と使用方法

for-eachループまたはブロックは、ループカウンターやインデックスの手動管理なしに、コレクション内のすべての項目を一つずつ自動的に処理できるようにします。これにより、コードがより安全で読みやすくなります。

### 利点

- **エラーの削減:**  
  for-eachループは、オフバイワンエラーや要素の誤ったスキップなどの一般的なバグを排除します。
- **コードの明確性:**  
  コードは多くの場合短く、読みやすく、意図をより直接的に伝えます。
- **安全性:**  
  for-eachは任意のイテラブル/コレクションオブジェクトで動作し、コレクションの基礎構造への結合を減らします。

例えば、C#では、`foreach`文は`IEnumerable<T>`を実装する任意の型でシームレスに動作します([Stackify](https://stackify.com/c-foreach-definition-and-best-practices/))。JavaScriptでは、`for...of`ループがイテラブルオブジェクトのすべての要素を反復処理します([MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators))。

## 主要プログラミング言語におけるイテレーターとFor-Each

### Python

#### 技術的説明

Pythonでは、*イテラブル*は`iter()`に渡してイテレーターを取得できる任意のオブジェクトです。イテレーターは`next()`を介して一度に一つの項目を返します。リスト、タプル、辞書、セット、文字列、その他多くの型がイテラブルです。

- **イテラブル:** `__iter__()`を実装し、イテレーターオブジェクトを返す必要があります。
- **イテレーター:** `__iter__()`(selfを返す)と`__next__()`(次の項目を返すか`StopIteration`を発生させる)の両方を実装します。

[GeeksforGeeks: Python Iterables vs Iterators](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/)

#### イテレーターの使用:ステップバイステップ

```python
my_list = [10, 20, 30]
my_iter = iter(my_list)
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
# 次の呼び出しでStopIterationが発生
```

`for`ループは、コレクションに対して暗黙的に`iter()`を呼び出し、結果のイテレーターに対して繰り返し`next()`を呼び出します。

#### カスタムイテレーターの作成

```python
class Counter:
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        if self.count < 5:
            self.count += 1
            return self.count
        else:
            raise StopIteration

for number in Counter():
    print(number)  # 出力: 1 2 3 4 5
```

#### 実用的な注意事項

- **ベストプラクティス:**  
  ほとんどのイテレーションタスクにはforループを使用します。
- **落とし穴:**  
  イテレーション中にコレクションを変更すると、エラーや予期しない結果が発生する可能性があります。
- **参考資料:**  
  [GeeksforGeeks: Python Iterables vs Iterators](https://www.geeksforgeeks.org/python/python-difference-iterable-iterator/)

### JavaScript

#### 技術的説明

JavaScriptは、組み込みとカスタムの両方のイテレーターをサポートしています。組み込み型(Array、String、Set、Map)はイテラブルであり、`[Symbol.iterator]()`メソッドを介してイテレーターを返します。イテレーターは[Iteratorプロトコル](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterators)を実装する必要があります:

- `next()`は`{ value, done }`を返します
  - `value`: シーケンス内の次の値
  - `done`: ブール値、シーケンスが終了した場合はtrue

#### イテレーターの使用:ステップバイステップ

```javascript
const arr = [1, 2, 3];
const iter = arr[Symbol.iterator]();
console.log(iter.next()); // { value: 1, done: false }
console.log(iter.next()); // { value: 2, done: false }
console.log(iter.next()); // { value: 3, done: false }
console.log(iter.next()); // { value: undefined, done: true }
```

#### For-eachループ(`for...of`)

```javascript
for (const item of arr) {
    console.log(item);
}
```

#### カスタムイテレーターの作成

```javascript
function makeRangeIterator(start = 0, end = 5, step = 1) {
  let nextIndex = start;
  return {
    next: function() {
      if (nextIndex < end) {
        return { value: nextIndex++, done: false };
      }
      return { done: true };
    }
  };
}

const rangeIter = makeRangeIterator(1, 4);
console.log(rangeIter.next().value); // 1
console.log(rangeIter.next().value); // 2
console.log(rangeIter.next().value); // 3
console.log(rangeIter.next().done);  // true
```

#### ジェネレーター関数

```javascript
function* genNumbers() {
  yield 1;
  yield 2;
  yield 3;
}
for (const num of genNumbers()) {
  console.log(num); // 1 2 3
}
```

#### 実用的な注意事項

- **落とし穴:**  
  イテレーターは通常、一度の完全なループ後に消費されます。
- **ベストプラクティス:**  
  クリーンで慣用的なイテレーションには`for...of`を使用します。
- **参考資料:**  
  [MDN: Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)

### Java

#### 技術的説明

Javaは、コレクションを走査するための`Iterator<E>`インターフェースを提供します([W3Schools](https://www.w3schools.com/java/java_iterator.asp))。このインターフェースは3つの主要なメソッドを指定します:

- `hasNext()`: さらに要素がある場合にtrueを返します
- `next()`: 次の要素を返します
- `remove()`: イテレーターが返した最後の要素を削除します(オプション)

#### イテレーターの使用:ステップバイステップ

```java
import java.util.ArrayList;
import java.util.Iterator;

ArrayList<String> cars = new ArrayList<>();
cars.add("Volvo");
cars.add("BMW");
cars.add("Ford");
cars.add("Mazda");

Iterator<String> it = cars.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

#### For-eachループ(推奨)

```java
for (String car : cars) {
    System.out.println(car);
}
```

#### イテレーション中の要素削除

```java
Iterator<Integer> it = numbers.iterator();
while (it.hasNext()) {
    if (it.next() < 10) {
        it.remove();
    }
}
```
> `ConcurrentModificationException`を避けるため、イテレーション中はコレクションからではなく、イテレーターから`remove()`を使用してください。([W3Schools](https://www.w3schools.com/java/java_iterator.asp))

#### 実用的な注意事項

- **ベストプラクティス:**  
  読み取り専用のイテレーションにはfor-eachを使用し、イテレーション中に要素を削除する必要がある場合のみ`Iterator`を直接使用します。
- **落とし穴:**  
  イテレーション中にコレクションを直接変更すると例外が発生する可能性があります。

### C#

#### 技術的説明

C#は、コレクションを反復処理するための`foreach`文を提供します。内部的には、`MoveNext()`、`Current`、`Reset()`メソッドを提供する[IEnumerator](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerator)インターフェースを使用します。

- `IEnumerable`または`IEnumerable<T>`を実装する任意の型は、`foreach`で使用できます。
- `foreach`はすべてのイテレーションロジックを自動的に処理します。

#### For-Eachの使用:ステップバイステップ

```csharp
List<string> colors = new List<string> { "Red", "Green", "Blue" };
foreach (var color in colors)
{
    Console.WriteLine(color);
}
```

#### 手動イテレーション(あまり一般的ではない)

```csharp
var enumerator = colors.GetEnumerator();
while (enumerator.MoveNext())
{
    Console.WriteLine(enumerator.Current);
}
```

#### `yield return`を使用したカスタムイテレーター

```csharp
IEnumerable<int> GetNumbers()
{
    for (int i = 0; i < 3; i++)
        yield return i;
}
foreach (var n in GetNumbers())
{
    Console.WriteLine(n); // 0 1 2
}
```

#### 非同期イテレーター

C#は`await foreach`による非同期イテレーションをサポートしています([Microsoft Learn - Asynchronous streams](https://learn.microsoft.com/en-us/dotnet/csharp/iterators))。

```csharp
await foreach (var item in asyncSequence)
{
    // 項目を処理
}
```

#### 実用的な注意事項

- **ベストプラクティス:**  
  コレクションを変更する必要がある場合やインデックスが必要な場合を除き、可読性と安全性のために`foreach`を使用します。
- **落とし穴:**  
  `foreach`イテレーション中のコレクションの直接変更は許可されていません。
- **参考資料:**  
  [Stackify: C# foreach definition and best practices](https://stackify.com/c-foreach-definition-and-best-practices/)

### ワークフロー自動化プラットフォーム(Relay.app)

#### 技術的説明

Relay.appなどのワークフロー自動化プラットフォームは、項目のリスト(行、添付ファイル、メールなど)を順次処理するための*イテレーター*または*for-each*ブロックを提供します。これらのブロックを使用すると、コードを書かずに各項目に対して実行するアクションを定義できます。

#### Relay.appでのイテレーターの使用:ステップバイステップ

1. **イテレーターブロックの追加:**  
   - Flow Controlメニューから「Iterator」を選択します([Relay.app Docs](https://docs.relay.app/flow-control/iterators))。
2. **処理するリストの選択:**  
   - 前のステップからの出力リスト(例:スプレッドシートの行のリスト)を選択します。
3. **アクションの設定:**  
   - イテレーター内に、各項目に対して実行すべき内容を定義するステップを追加します(例:メール送信、レコード更新)。
4. **現在の項目データの使用:**  
   - アクション内で現在のイテレーションからの値を参照します。

> **ヒント:**  
> イテレーターブロックは、コレクションの視覚的でノーコードの処理を可能にし、ワークフロー内の反復的なタスクの自動化に最適です。

#### 実用的な注意事項

- **ベストプラクティス:**  
  項目ごとに実行すべきすべてのアクションをイテレーターブロック内に配置します。
- **落とし穴:**  
  イテレーション中に基礎となるリストを変更しないようにします。
- **参考資料:**  
  [Relay.app Docs: Looping (Iterators)](https://docs.relay.app/flow-control/iterators)

## 比較:イテレーター vs イテラブル、For vs For-Each

| 概念        | 説明                                                                               | 使用するタイミング                               |
|----------------|------------------------------------------------------------------------------------------|-------------------------------------------|
| **イテレーター**   | コレクションから一つずつ項目を生成するオブジェクト                                  | イテレーションの細かい制御が必要な場合   |
| **イテラブル**   | イテレーターを返すことができるオブジェクト(例:リスト、配列、セット)                           | for-eachを使用してループしたい場合      |
| **Forループ**   | インデックス、条件、増分を制御できる古典的なループ                       | インデックスアクセスやカスタムステップが必要な場合|
| **For-Each**   | コレクション内のすべての項目を処理する簡略化されたループ、インデックスの詳細を隠す            | 項目を処理するだけの場合       |

**主な違い:**

- For-eachは現在のインデックスを直接公開しません。
- For-eachは読み取り専用操作に対してより安全です。カスタムステップサイズ、スキップ、または逆順にはforループが必要です。
- 一部の言語では、イテレーション中の項目削除を許可します(Javaの`Iterator.remove()`)が、他の言語では許可しません(C#の`foreach`)。

## 一般的な落とし穴、ベストプラクティス、特殊機能

### 一般的な落とし穴

- **イテレーション中のコレクションの変更**は、エラーや予期しない動作を引き起こす可能性があります(JavaのConcurrentModificationException、C#のランタイムエラー)。
- **イテレーターは消費されます:**  
  終了すると、新しいものを作成せずに再起動することはできません。
- **For-eachはインデックスを提供しません:**  
  位置が必要な場合は`for`ループを使用します。
- **無限イテレーション:**  
  カスタムイテレーターは停止条件を発生/返す必要があります(Pythonの`StopIteration`)。

### ベストプラクティス

- シンプルな読み取り専用処理にはfor-eachループを使用します。
- カスタムシーケンスにはイテレーターメソッドまたは`yield`(Python、C#、JavaScript)を使用します。
- ワークフロー自動化では、すべての項目ごとのアクションをイテレーターブロック内に保持します。

### 特殊機能

- **非同期イテレーション:**  
  C#(`await foreach`)とJavaScript(非同期イテレーターと`for await...of`)でサポートされています。
- **項目の削除:**  
  特定の言語でのみサポートされています(例:Javaの`Iterator.remove()`)。

## ユースケースと例

### スプレッドシート行の処理

- **Python:**  
  ```python
  for row in spreadsheet_rows:
      process(row)
  ```
- **Relay.app:**  
  - イテレーターブロックが各行をデータ抽出、通知などのために処理します([Relay.app Docs](https://docs.relay.app/flow-control/iterators))。