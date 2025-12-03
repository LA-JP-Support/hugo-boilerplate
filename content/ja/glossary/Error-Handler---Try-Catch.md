---
title: エラーハンドラー / Try-Catch
translationKey: error-handler-try-catch
description: エラーハンドラー(多くの場合Try-Catchブロック)は、自動化やAIチャットボットにおける予期しない障害を管理し、クラッシュを防ぎ、制御された復旧やログ記録を可能にします。
keywords:
- エラーハンドラー
- try-catch
- 例外処理
- 自動化
- AIチャットボット
category: General
type: glossary
date: 2025-12-03
draft: false
term: えらーはんどらー / とらい きゃっち
reading: エラーハンドラー / Try-Catch
kana_head: あ
e-title: Error Handler / Try-Catch
---

## 定義

自動化およびAIチャットボット開発において、エラーハンドラー(Error Handler)—多くの場合Try-Catchブロックまたはプラットフォーム固有の同等機能として実装される—は、指定された操作が失敗した場合(つまり例外をスローした場合)にのみ起動する、ワークフローまたはコード実行における専用パスです。このメカニズムはフロー全体のクラッシュを防ぎ、制御された復旧、ログ記録、または修正アクションを可能にします([MDN try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch))。

## 1. はじめに

自動化システムおよび対話型AIプラットフォームは、無効なユーザー入力、統合の障害、またはロジックのバグによる予期しない障害に対して耐性を持つ必要があります。エラーハンドラーは、通常Try-Catchブロックとして実現され、このような実行時例外を予測し管理します。これらがなければ、単一の未処理エラーが自動化プロセスをクラッシュさせたり、チャットボットセッションを未定義の状態に陥らせたりする可能性があります。

**シナリオ:**  
チャットボットが外部APIからデータを読み取り、そのAPIが失敗した場合、Try-Catchブロックはボットが突然終了するのではなく、ユーザーに適切に通知し代替案を提供することを保証します([JavaScript.info: Try-Catch](https://javascript.info/try-catch))。

## 2. エラーハンドラー / Try-Catchとは何か?

### 技術的定義

エラーハンドラー(またはTry-Catchブロック)は、例外—実行中の予期しないイベント—をトラップするプログラミング構造または論理フロー要素であり、コードまたは自動化が制御不能に失敗するのではなく、意図的に応答できるようにします。

- **例外処理(Exception Handling):** 例外の検出、捕捉、および処理。
- **例外(Exception):** 実行中のエラーまたは予期しない状態を表すイベント。
- **Tryブロック:** 例外を生成する可能性のあるコードを含む。
- **Catchブロック:** 関連するtryブロックでスローされた例外を処理する。
- **Finallyブロック(オプション):** 例外がスローされたかどうかに関係なくコードを実行する。

> 「Try-Catchエラーハンドラーは、操作が失敗したときに制御フローを専用ブロックに向け、プロセスをクラッシュさせることなく復旧または報告を可能にします。」

## 3. 主要言語とプラットフォームにおける構文とフロー

### 3.1 JavaScript

**構文:**
```javascript
try {
  // エラーをスローする可能性のあるコード
} catch (error) {
  // エラーを処理
} finally {
  // 常に実行されるコード
}
```
**フロー:**
1. `try`内のコードが実行される。
2. 例外がなければ、`catch`はスキップされる。
3. 例外が発生すると、`try`は停止し制御が`catch`に移る。
4. `finally`は結果に関係なく実行される。

**重要なポイント:**
- 実行時エラーのみが捕捉される(構文エラーは捕捉されない)。
- 非同期コードの場合、エラーは非同期コールバック内で捕捉する必要がある。
- `throw`を使用して、上位レベルのハンドラーに例外を再スローできる([JavaScript.info: Try-Catch](https://javascript.info/try-catch))。

### 3.2 C# (.NET)

**構文:**
```csharp
try
{
    // スローする可能性のあるコード
}
catch (SpecificException ex)
{
    // 特定の例外を処理
}
catch (Exception ex)
{
    // あらゆる例外を処理
}
finally
{
    // 常に実行される
}
```
**機能:**
- 異なる例外タイプに対する複数のcatchブロック。
- 高度な処理のための例外フィルター(`catch (Exception ex) when (condition)`)。
- `throw;`で再スローし、スタックトレースを保持([Microsoft Learn: Exception Handling](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements))。

### 3.3 Java

**構文:**
```java
try {
    // スローする可能性のあるコード
} catch (ExceptionType e) {
    // 例外を処理
} finally {
    // クリーンアップコード
}
```
**機能:**
- 複数のcatchブロック。
- `finally`は必ず実行される。
- カスタム例外を定義してスローできる([W3Schools: Java Try...Catch](https://www.w3schools.com/java/java_try_catch.asp))。

**ベストプラクティス:**
- 特定の例外を最初に捕捉する。  
- 絶対に必要でない限り、`Throwable`や一般的な`Exception`の捕捉は避ける([Stackify Best Practices](https://stackify.com/best-practices-exceptions-java/))。

### 3.4 ロボティックプロセスオートメーション(RPA) – UiPath

**ワークフロー要素:**
- **Try Catchアクティビティ:** アクティビティを囲み、エラー時にCatchにジャンプする。
- **グローバル例外ハンドラー:** 未処理の例外をグローバルに捕捉し、多くの場合ローカルのTry-Catchロジックを上書きする。

**フロー:**
- Tryシーケンス内のアクティビティ。
- アクティビティが失敗すると、Catchシーケンスがトリガーされる。
- `Finally`はTryまたはCatchの後に実行される。

**例(UiPath):**
```
[Try]
    Excelファイルを読み取る
    各行に対して
        [Try]
            ドロップダウンを選択
        [Catch]
            エラーをログ記録、ループを継続
        [Finally]
            フラグを設定、クリーンアップ
[Catch]
    未処理エラーをログ記録
[Finally]
    リソースを閉じる
```
([UiPath Activities: Try Catch](https://docs.uipath.com/activities/docs/try-catch), [UiPath Forum](https://forum.uipath.com/t/best-practices-try-catch/402586))

## 4. ベストプラクティスと落とし穴

### エラーハンドラーを使用するタイミングと理由

- **Try-Catchを使用する場合:**
  - 例外的で予測不可能なシナリオ(ネットワーク障害、ファイルI/O、外部サービスエラー)。
  - ワークフローのクラッシュを防ぎ、ユーザーフレンドリーなエラー処理を保証する。
  - 統合境界、または検証がすべての障害を防げない場所。

- **Try-Catchを避けるべき場合:**
  - 通常の制御フロー(例外でif/elseを置き換えることを避ける)。
  - 検証/チェックによってエラーを防ぐべきコード。
  - 必要でない限り、パフォーマンスクリティカルなコード。

### ベストプラクティス

- **具体的に:** 可能な限り最も具体的な例外タイプを捕捉する([Stackify Java](https://stackify.com/best-practices-exceptions-java/))。
- **Catchブロックを空のままにしない:** 常にログ記録、処理、または再スローを行う。サイレント障害はバグを隠す([Stack Overflow C#](https://stackoverflow.com/questions/14973642/how-using-try-catch-for-exception-handling-is-best-practice))。
- **ログ記録と監視:** トラブルシューティングのために詳細(タイプ、メッセージ、スタックトレース)を記録する。
- **必要に応じて再スロー:** 例外を処理できない場合、C#では`throw;`、Java/JavaScriptでは`throw e;`を使用して上位レイヤーに再スローする。
- **クリーンアップにFinallyを使用:** リークを避けるために`finally`でリソースを解放する。
- **Catchスコープを制限:** 単一のTry-Catchで大きなブロックをラップしない。リスクのある操作を分離する([UiPath Best Practice](https://forum.uipath.com/t/best-practices-try-catch/402586))。

#### プラットフォーム固有のガイダンス

- **JavaScript:**  
  - Try-Catchは構文エラーやコールバック外の非同期エラーを捕捉しない。
  - async/awaitの場合、非同期関数内でTry-Catchを使用する([MDN try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch))。

- **C#/.NET:**  
  - 高度なシナリオには例外フィルターを使用する。
  - 元のスタックトレースを保持するために`throw;`を使用する。
  - トップレベル境界でない限り、`Exception`を捕捉しない([Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements))。

- **Node.js (JavaScript):**  
  - Try-Catchは同期エラーのみを処理する。
  - 非同期コールバックまたはプロミスで適切なエラー処理を使用する。
  - サーバーの安定性のために、プロセスレベルのハンドラーを使用するが、致命的なエラーではプロセスの再起動を優先する([Node.js error handling tips](https://stackoverflow.com/questions/5999373/how-do-i-prevent-node-js-from-crashing-try-catch-doesnt-work))。

- **RPA / UiPath:**
  - **グローバル例外ハンドラー**(GEH)は、適切に構成されていない場合、ローカルのTry-Catchの前に例外をインターセプトできる。
  - 特にループ内で、リスクのあるアクティビティを独自のTry-Catchに配置する。
  - 例外後のフロー制御にログ記録とフラグを使用する。
  - プロジェクトごとに1つのグローバルハンドラーのみがサポートされ、慎重に使用する必要がある—あらゆるエラーがそれをトリガーする([UiPath Forum](https://forum.uipath.com/t/what-is-the-best-approach-for-exception-handling-in-uipath-if-you-have-hundred-of-activities-and-many-workflows-error-handling/529943))。

### 避けるべきこと

> 通常のロジックフロー(例:解析、分岐)にTry-Catchを使用しないでください。パフォーマンスと可読性が低下します([Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/questions/107723/arguments-for-or-against-using-try-catch-as-logical-operators))。

- 報告せずに例外を飲み込まない。
- アプリケーション境界でない限り、広範な例外を捕捉しない。
- リスクのある操作の前にチェックできる検証エラーに例外を使用しない。
- 不必要なTry-Catchブロックでコードを散らかさない—例外を意味のあるハンドラーにバブルアップさせる。

## 5. 例

### 5.1 JavaScript(同期 vs 非同期)

**正しい使用法:**
```javascript
try {
  let user = JSON.parse(data);
  // ユーザーを処理
} catch (err) {
  console.error("データの解析に失敗しました:", err.message);
}
```

**誤った使用法(制御フロー):**
```javascript
// アンチパターン:ルーチン検証に例外を使用
try {
  if (!userInput) throw "入力がありません";
  process(userInput);
} catch (err) {
  // ルーチン検証にtry/catchを使用しない
}
```

**非同期の落とし穴:**
```javascript
// これはエラーを捕捉しません!
try {
  setTimeout(() => { throw new Error("おっと"); }, 1000);
} catch (err) {
  // 実行されない
}
```
**正しい非同期処理:**
```javascript
setTimeout(() => {
  try {
    throw new Error("おっと");
  } catch (err) {
    console.error("非同期で捕捉:", err.message);
  }
}, 1000);
```
([JavaScript.info](https://javascript.info/try-catch))

### 5.2 C#

**正しい使用法:**
```csharp
try
{
    var result = ProcessUserInput(input);
}
catch (FormatException ex)
{
    LogError(ex, "入力形式が無効です");
    ShowUserFriendlyMessage();
}
finally
{
    Cleanup();
}
```
**誤った使用法:**
```csharp
try
{
    // 何らかのコード
}
catch
{
    // アンチパターン:空のcatchはすべてのエラーを隠す
}
```
**ベストプラクティス:例外フィルターを使用**
```csharp
try
{
    // アクション
}
catch (Exception ex) when (ex is IOException || ex is UnauthorizedAccessException)
{
    // 特定のケースを処理
}
```
([Stack Overflow: Try/Catch Best Practices](https://stackoverflow.com/questions/14973642/how-using-try-catch-for-exception-handling-is-best-practice))

### 5.3 Java

**正しい使用法:**
```java
try {
    int value = Integer.parseInt(input);
} catch (NumberFormatException e) {
    logger.error("無効な入力: " + input, e);
    // ユーザーに通知または修正アクションを実行
} finally {
    // 常に実行される
}
```

**誤った使用法:**
```java
try {
    // コード
} catch (Exception e) {
    // 何もしない!(アンチパターン)
}
```

**ベストプラクティス:特定の例外を捕捉**
```java
try {
    // コード
} catch (IOException e) {
    // IOエラーを処理
} catch (NumberFormatException e) {
    // 数値形式エラーを処理
}
```
([Stackify Best Practices](https://stackify.com/best-practices-exceptions-java/), [Baeldung Java Exceptions](https://www.baeldung.com/java-exceptions))

### 5.4 UiPath RPA

**Try-Catchアクティビティの例:**
- **Try:** ドロップダウンから項目を選択
- **Catch:** エラーをログ記録、エラーリストに追加、フラグを設定、ループを継続
- **Finally:** クリーンアップまたはリセット

**グローバル例外ハンドラーとの相互作用:**
- GEHとTry-Catchの両方が存在する場合、アクティビティが適切に分離されていない限り、例外は最初にGEHに行く可能性がある([UiPath Forum](https://forum.uipath.com/t/global-exception-handler-vs-try-catch-when-to-use-which/177630))。

## 6. トラブルシューティングと高度なシナリオ

### 例外のバブルアップ

- 例外は捕捉されるまでコールスタックを伝播する。
- 自動化では、未処理の例外は親ワークフローまたはグローバルハンドラーにエスカレートする可能性がある([Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements))。

### RPAにおけるグローバル vs ローカルハンドラー

- **UiPath:**  
  - グローバル例外ハンドラーは、特にアクティビティが分離されていない場合、ローカルのTry-Catchの前に例外をインターセプトする可能性がある。
  - ローカルのTry-Catchが尊重されることを保証するには、単一のリスクのあるアクティビティを独自のTry-Catchブロックに分離する([UiPath Best Practice](https://forum.uipath.com/t/best-practices-try-catch/402586), [UiPath Forum](https://forum.uipath.com/t/what-is-the-best-approach-for-exception-handling-in-uipath-if-you-have-hundred-of-activities-and-many-workflows-error-handling/529943))。

### Node.js非同期の落とし穴

- Try-Catchはそのコンテキスト外の非同期コードには機能しない。
- エラーファーストコールバックまたはプロミスの`.catch()`ハンドラーを使用する。
- 未処理の例外については、ログ記録のためにプロセスレベルのハンドラーを検討するが、致命的なエラーでは常にプロセスの再起動を優先する([Node.js error handling tips](https://stackoverflow.com/questions/5999373/how-do-i-prevent-node-js-from-crashing-try-catch-doesnt-work))。

### 例外の再スロー

- ハンドラーが例外を解決できない場合、`throw;`(C#)または`throw e;`(Java/JavaScript)を使用して再スローする。
- 再スローはスタックトレースを保持または更新する。C#では元のスタックトレースを保持するために`throw;`を優先する([Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements))。

### パフォーマンスの懸念

- 例外処理には実行時コストがあり、特にJavaやC#などの言語で顕著。
- 高頻度の制御フローに例外を使用しない([Stackify Best Practices](https://stackify.com/best-practices-exceptions-java/))。

## 7. まとめ / 重要なポイント

- エラーハンドラー(Try-Catch)は例外を捕捉することで制御不能なプロセスクラッシュを防ぐ。
- Try-Catchは例外的で予測不可能なイベントに使用し、通常のロジックやフロー制御には使用しない。
- 常にログ記録またはエスカレートする。catchブロックを空のままにしない。
- 具体的に—意味のある処理ができるものだけを捕捉する。
- 自動化プラットフォームでは、グローバルハンドラーがTry-Catchロジックとどのように相互作用するかを理解する。
- 非同期操作では、エラー処理が正しい実行レベルに配置されていることを確認する。
- 処理できない例外は再スローし、リソースのクリーンアップにはfinallyブロックを使用する。
- アンチパターンを避ける:空のcatchブロック、検証に例外を使用、Try-Catchの過剰使用。
- 本番環境のワークフローとチャットボットで信頼性を確保するために、エラー処理をテストおよび監視する。

## 8. 参考文献とさらなる読み物

- [MDN try...catch (JavaScript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
- [JavaScript.info: Error Handling](https://javascript.info/try-catch)
- [Microsoft Learn: Exception Handling in C#](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/exception-handling-statements)
- [StackOverflow: Try/Catch Best Practices (C#)](https://stackoverflow.com/questions/14973642/how-using-try-catch-for-exception-handling-is-best-practice)
- [StackExchange: Try/Catch as Logical Operators](https://softwareengineering.stackexchange.com/questions/107723/arguments-for-or-against-using-try-catch-as-logical-operators)
- [Node.js Cluster & Error Handling](https://stackoverflow.com/questions/5999373/how-do-i-prevent-node-js-from-crashing-try-catch-doesnt-work)
- [W3Schools: Java Try...Catch](https://www.w3schools.com/java/java_try_catch.asp)
- [UiPath Forum: Best Practices Try Catch](https://forum.uipath.com/t/best-practices-try-catch/402586)
- [UiPath Forum: Global Exception Handler vs Try-Catch](https://forum.uipath.com/t/global-exception-handler-vs-try-catch-when-to-use-which/177630)
- [UiPath Forum: Exception Handling in Large Projects](https://forum.uipath.com/t/what-is-the-best-approach-for-exception-handling-in-uipath-if-you-have-hundred-of-activities-and-many-workflows-error-handling/529943)
- [Stackify: 9 Best Practices for Java Exceptions](https://stackify.com/best-practices-exceptions-java/)
- [Baeldung: Java Exceptions](https://www.baeldung.com/java-exceptions)
- [UiPath Official Docs: Try Catch](https://docs.uipath.com/activities/docs/try-catch)

**プラットフォームにおける例外処理の実装詳細については、常に公式ドキュメントとコミュニティのベストプラクティスを参照してください。**