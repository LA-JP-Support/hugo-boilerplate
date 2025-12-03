---
title: グローバル変数
translationKey: global-variables
description: グローバル変数は、プログラムや自動化プラットフォーム内のあらゆるノードからアクセス可能な変数で、フロー、関数、コンテキスト間でデータを共有します。AIチャットボットにおける使用方法について学びましょう。
keywords: ["グローバル変数", "AIチャットボット", "自動化プラットフォーム", "プログラミング変数", "変数スコープ"]
category: AI Chatbot & Automation
type: glossary
date: 2025-12-03
draft: false
term: ぐろーばるへんすう
reading: グローバル変数
kana_head: か
---
## 導入と定義

**グローバル変数**とは、関数、ブロック、またはノードの外部で定義され、プログラムまたは自動化ワークフロー全体からアクセス可能な変数です。CやPythonなどの従来のプログラミング言語、およびAIチャットボットや自動化プラットフォームの両方において、グローバル変数はコードベースやフローのあらゆる部分からアクセスでき、場合によっては変更も可能です。これは、宣言されたスコープ内に限定されるローカル変数とは対照的です。

プログラミングにおける例:
- すべての関数の外部で宣言された変数(通常、Cではソースファイルの先頭、Pythonでは関数の外部)はグローバルと見なされ、プログラム全体でアクセス可能です([GeeksforGeeks: Global Variables in C](https://www.geeksforgeeks.org/c/global-variables-in-c/)、[W3Schools: Python Global Variables](https://www.w3schools.com/python/python_variables_global.asp))。
- AIチャットボットプラットフォームでは、グローバル変数は会話トピック、自動化ステップ、さらにはプラットフォームのアーキテクチャに応じてセッション全体で永続化するように設定できます。

グローバル変数は一般的に以下の用途で使用されます:
- モジュール間での設定の共有
- 会話フロー全体でのユーザーセッションデータの維持
- アプリケーションやボットの異なる部分間でのコンテキスト共有

## グローバル変数の動作原理

### グローバル変数のスコープ

- **グローバルスコープ:**  
  グローバルスコープで定義された変数は、アプリケーション内のすべての関数、ノード、またはトピックからアクセス可能です。
- **ローカルスコープとグローバルスコープ:**
  - ローカル変数は、宣言された関数、ブロック、またはノードに限定されます。
  - グローバル変数は、宣言後にコード内のどこからでもアクセス可能です。

#### Cでの例:
```c
#include <stdio.h>
int x = 5; // global variable

int main() {
    int y = 10; // local variable
    printf("%d", x + y); // x is accessible here
    return 0;
}
```
([GeeksforGeeks: Global Variables in C](https://www.geeksforgeeks.org/c/global-variables-in-c/))

#### Pythonでの例:
```python
x = "awesome"  # Global variable

def myfunc():
    print("Python is " + x)  # Accesses global x

myfunc()
print("Python is " + x)
```
([W3Schools: Python Global Variables](https://www.w3schools.com/python/python_variables_global.asp))

#### チャットボットプラットフォームでの例:
- 「グローバル」として設定された変数は、Microsoft Copilot Studioの`Global.UserName`や`bot.UserName`のように、任意のダイアログノード、トピック、または自動化アクションで参照できます([Microsoft Copilot Studio – Work with Global Variables](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))。

### ライフサイクルと永続性

- **ライフタイム:**  
  グローバル変数のライフタイムは、プログラムの実行全体(C、Python)から、チャットボットにおけるユーザーのセッション期間、外部ストレージによってバックアップされている場合は複数のセッションにわたる永続性まで、さまざまです。
- **初期化:**  
  - Cでは、グローバル変数は明示的に初期化されない場合、デフォルトでゼロに初期化されます([GeeksforGeeks](https://www.geeksforgeeks.org/c/global-variables-in-c/))。
  - Pythonでは、使用前に値を割り当てる必要があります。
  - チャットボットプラットフォームでは、会話の開始時に初期化されるか、外部パラメータから設定される場合があります。
- **永続性:**  
  - 標準的なグローバル変数は、アプリケーションまたはセッションが終了するとリセットされます。
  - セッション間で永続化するには、データベースまたは外部ストレージに値を保存する必要があります。

## グローバル変数の作成、設定、使用

### プログラミング言語での使用

#### Python

- **グローバル変数の定義:**  
  すべての関数の外部で変数を宣言してグローバルにします。
- **グローバル変数へのアクセス:**  
  任意の関数内で読み取ることができます。
- **グローバル変数の変更:**  
  関数内でグローバル変数を変更するには、`global`キーワードを使用します。

**例:**
```python
x = "awesome"  # Global variable

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Output: Python is fantastic
```
([W3Schools: Python Global Variables](https://www.w3schools.com/python/python_variables_global.asp))

- 関数内に同じ名前のローカル変数が存在する場合、その関数のスコープ内でグローバル変数をシャドウします。関数内からグローバル変数を変更するには、`global`キーワードが必要です。

#### C

- **グローバル変数の宣言:**  
  通常、ファイルの先頭で、任意の関数の外部で変数を宣言します。
- **アクセスと変更:**  
  プログラム内の任意の関数からアクセスおよび変更が可能です。
- **デフォルト初期化:**  
  初期化されていないグローバル変数はゼロに初期化されます。

**例:**
```c
#include <stdio.h>
int a, b; // global variables

void add() {
    printf("%d", a + b);
}

int main() {
    a = 10;
    b = 15;
    add(); // Output: 25
    return 0;
}
```
([GeeksforGeeks: Global Variables in C](https://www.geeksforgeeks.org/c/global-variables-in-c/))

### AIチャットボットおよび自動化プラットフォームでの使用

#### 一般的なプロセス

1. **変数の作成:**  
   ほとんどのプラットフォームでは、ローカル(ノード/トピック/ステップ)およびグローバル(ボット/フロー/セッション)スコープでの変数作成が可能です。
2. **スコープをグローバルに設定:**  
   クロスフローアクセスのために、変数のスコープを「グローバル」または「ボットレベル」として設定します。
3. **任意のノードでアクセス:**  
   任意のロジックブロック、トピック、または自動化ステップからグローバル変数を参照します。

#### Microsoft Copilot Studioの例

- グローバル変数を作成するには:
  1. 変数を作成します。
  2. プロパティパネルでスコープを**グローバル(すべてのトピックがアクセス可能)**に設定します。
  3. 変数名にはプレフィックスが付きます(例:`Global.UserName`)。
  4. これで、変数は任意のトピックまたは自動化ノードでアクセスまたは変更できます。
- グローバル変数を使用するには:
  - メッセージ、質問、またはロジック分岐で直接参照します。
  - 変数ピッカーを使用するか、プレフィックス付きの名前を入力します。
- 外部ソースから設定するには:
  - 会話の開始時にクエリ文字列またはAPI呼び出しを介して値を受け入れます。

([Microsoft Copilot Studio – Work with Global Variables](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))

#### ServiceNowの例

- カタログアイテムまたはFlow Designerで変数をグローバルとして設定し、複数のワークフローまたはアイテム間で利用可能にします。
- 注意して使用してください。グローバル変数は任意の関数からアクセスおよび変更可能であり、データの一貫性にリスクをもたらす可能性があります。

([ServiceNow Community – Global Variables Discussion](https://www.servicenow.com/community/developer-forum/global-variables/m-p/2608732#M1014639))

### 外部ソースからの設定

- 多くのチャットボットプラットフォームでは、Webページのクエリパラメータ、ヘッダー、またはAPI呼び出しなどの外部システムからグローバル変数を初期化できます。
- これにより、ボットまたは自動化フローにコンテキスト(例:ユーザーID、セッショントークン)を渡すことができます。

**例(Microsoft Copilot Studio):**
- `https://web.powerva.microsoft.com/webchat/bots/12345?UserName=Ana`のようなURLを使用して、セッション開始前に`Global.UserName`を初期化します。

## 実用例

### プログラミング例:Python

**関数内外でのグローバル変数**
```python
x = "awesome"

def myfunc():
    print("Python is " + x)  # Accesses global x

myfunc()
print("Python is " + x)
```
**出力:**
```
Python is awesome
Python is awesome
```

**関数からグローバル変数を変更**
```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```
**出力:**
```
Python is fantastic
```
([W3Schools: Python Global Variables](https://www.w3schools.com/python/python_variables_global.asp))  
[YouTube: Python Global Variables](https://youtu.be/VZW9CGZymqU&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9)

### プログラミング例:C

**グローバル変数の宣言と使用**
```c
#include <stdio.h>
int x = 5; // global variable

int main() {
    int y = 10; // local variable
    printf("%d", x + y); // x is accessible here
    return 0;
}
```

**関数によって更新されるグローバル変数**
```c
#include <stdio.h>
int a, b; // global variables

void add() {
    printf("%d", a + b);
}

int main() {
    a = 10;
    b = 15;
    add(); // Output: 25
    return 0;
}
```
([GeeksforGeeks: Global Variables in C](https://www.geeksforgeeks.org/c/global-variables-in-c/))

### AIチャットボットプラットフォーム例:Microsoft Copilot Studio

**グローバル変数の作成と使用:**

1. `UserName`という名前の変数を作成します。
2. スコープを**グローバル(すべてのトピックがアクセス可能)**に設定します。
3. 「ウェルカム」トピックで、ユーザーの入力を`UserName`に割り当てます。
4. 後続のトピック(例:「予約」)で、パーソナライズされた応答のために`UserName`を参照します。

**外部ソースからグローバル変数を渡す:**
- 次のようなURLでチャットボットを開始します:
  ```
  https://web.powerva.microsoft.com/webchat/bots/12345?UserName=Ana
  ```
- チャットボットセッションは`Global.UserName`変数を「Ana」に設定します。

**グローバル変数のリセット:**
- **会話のリセット**システムトピックを使用して、すべてのグローバル変数をクリアし、初期状態に復元します。

([Microsoft Copilot Studio – Work with Global Variables](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))

## グローバル変数の使用例

- **ユーザーデータの永続化:**  
  ユーザー情報(名前、メール)を一度保存し、繰り返しプロンプトなしでトピック間で再利用します。
- **セッション管理:**  
  会話またはワークフロー全体で状態またはセッション属性を維持します。
- **設定:**  
  複数のフローからアクセスされる機能フラグまたは環境設定を保持します。
- **コンテキスト共有:**  
  サブフロー、スクリプト、または分岐間でデータを渡します。
- **外部統合:**  
  外部システムまたはWebアプリから初期コンテキストまたはセッションデータを受け入れます。

## 利点と欠点

### 利点

- **アクセシビリティ:**  
  アプリケーションまたはフローのあらゆる部分からアクセスおよび変更が可能です。
- **データ共有:**  
  分離されたモジュールまたはトピック間での情報共有を簡素化します。
- **冗長性の削減:**  
  一度の宣言で済み、繰り返しのユーザープロンプトを回避します。
- **セッションデータの処理:**  
  チャットボットおよび自動化におけるセッションレベルのデータに最適です。

### 欠点

- **副作用のリスク:**  
  アプリケーションまたはワークフローのあらゆる部分がグローバル変数を変更できるため、意図しない動作が発生する可能性があります。
- **デバッグの複雑さ:**  
  大規模なコードベースまたはフローでの変更の追跡が困難です。
- **潜在的な競合:**  
  慎重な命名規則がないと、命名の競合や誤った上書きが発生する可能性があります。
- **リソース使用:**  
  過度のグローバル変数はメモリ使用量を増加させる可能性があります。
- **同時実行の問題:**  
  マルチユーザー環境では、同時アクセスがデータの不整合につながる可能性があります。

## ベストプラクティスと考慮事項

- **使用を制限:**  
  グローバル変数は控えめに使用し、共有されないデータにはローカル変数を優先します。
- **一意の命名:**  
  競合を避けるために、明確で一意の名前を使用します(例:`Global.`または`bot.`プレフィックス付き)。
- **制御された変更:**  
  グローバル変数が変更される場所の数を制限します。
- **初期化:**  
  未定義の状態を避けるために、常にデフォルト値で初期化します。
- **使用の文書化:**  
  各グローバル変数を使用するフローまたはモジュールを明確に文書化します。
- **必要に応じてリセット:**  
  適切なポイント(例:セッション終了)でグローバル変数をリセットするメカニズムを提供します。
- **セキュリティとプライバシー:**  
  適切に保護されていない限り、グローバル変数に機密データを保存しないでください。

## プラットフォーム固有の注意事項

### Microsoft Copilot Studio

- **変数プレフィックス:**  
  グローバル変数は`Global.`または`bot.`プレフィックス付きで表示されます(例:`Global.UserName`)。
- **スコープ設定:**  
  変数プロパティパネルでグローバルを設定します。
- **セッションスコープ:**  
  グローバル変数はユーザーのセッション期間中持続します。
- **外部ソースからの初期化:**  
  URLパラメータまたはプログラムで設定できます。
- **リセット:**  
  「会話のリセット」トピックを使用して、すべてのグローバル変数をクリアします。

([Microsoft Copilot Studio – Work with Global Variables](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))

### ServiceNow

- **カタログアイテム変数:**  
  変数をグローバルとして設定すると、カタログタスクとフロー間で再利用できます。
- **注意:**  
  不適切な使用は、誤った上書きによるリソース使用のスパイクやデータ整合性の問題を引き起こす可能性があります。

([ServiceNow Community – Global Variables Discussion](https://www.servicenow.com/community/developer-forum/global-variables/m-p/2608732#M1014639))

### その他の自動化およびボットプラットフォーム

- **類似の概念:**  
  ほとんどが類似のアクセスおよび変更ルールを持つグローバル変数をサポートしています。
- **プラットフォームドキュメント:**  
  詳細については、各プラットフォームのドキュメントを参照してください。

## 関連概念

- **ローカル変数:**  
  関数、ノード、またはトピックに限定されます。
- **セッション変数:**  
  セッションの期間中のみ永続化します。
- **環境変数:**  
  システムまたは環境レベルで設定され、多くの場合設定に使用されます。
- **定数:**  
  値が変更されない変数。
- **状態管理:**  
  アプリケーションまたは会話の状態を管理する技術で、多くの場合ローカル変数とグローバル変数の両方を使用します。

## 参考文献とさらなる読み物

- [W3Schools Python Global Variables](https://www.w3schools.com/python/python_variables_global.asp)
- [GeeksforGeeks Global Variables in C](https://www.geeksforgeeks.org/c/global-variables-in-c/)
- [Microsoft Copilot Studio – Work with Global Variables](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot)
- [ServiceNow Community – Global Variables Discussion](https://www.servicenow.com/community/developer-forum/global-variables/m-p/2608732#M1014639)
- [YouTube: Python Global Variables](https://youtu.be/VZW9CGZymqU&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9)

**まとめ:**  
グローバル変数は、自動化システム、プログラミング言語、AIチャットボットプラットフォームの複数の部分間で情報を共有および永続化するメカニズムを提供します。動的でコンテキストを認識した効率的なフローを可能にする一方で、副作用を回避しコード品質を維持するには慎重な管理が不可欠です。さらなる技術的な詳細については、リンクされた参考文献とプラットフォームドキュメントを参照してください。