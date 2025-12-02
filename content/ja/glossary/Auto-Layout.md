---
title: オートレイアウト：完全用語集
translationKey: auto-layout-the-complete-glossary
description: UIエレメントを自動的に配置・サイズ変更するデザイン機能であるオートレイアウトをマスターしましょう。Figma、iOS、Android、Webでの主要概念、メリット、実装方法を網羅しています。
keywords:
- オートレイアウト
- Figma
- UIデザイン
- レスポンシブデザイン
- 制約
category: General
type: glossary
date: 2025-12-02
draft: false
term: オートレイアウト：完全用語集
---

## オートレイアウトとは？

オートレイアウトは、定義したルールや制約に基づいてインターフェイス要素を自動的に配置、整列、サイズ変更するデザインおよび開発機能です。コンテンツ、画面サイズ、または要素の数が変更されると、オートレイアウトは要素を再計算して再配置し、インターフェイスが常に整理され、読みやすく、レスポンシブであることを確保します。

**例え：**  
本を追加したり取り除いたりするたびに自動的に本を移動させ、間隔を調整する本棚を想像してください。オートレイアウトはUI要素に対して同じことを行います：要素を追加または削除しても、デザインは整理され視覚的にバランスが保たれます。

**Figma公式ガイド：**  
[Guide to auto layout – Figma Help Center](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)

---

## オートレイアウトを使用する理由

**主なメリット：**

- **効率性：** 手動でのサイズ変更や再配置が大幅に減少。コンテンツやコンポーネントを一度更新すれば、レイアウトはどこでも適応します。
- **レスポンシブデザイン：** 要素が様々な画面サイズに適応するため、マルチデバイスのデザインワークフローに最適です。
- **一貫性：** プロジェクト全体で均一な間隔、整列、比率を維持します。
- **コラボレーション：** デザイナーと開発者が同じルールセットに依存するため、引き継ぎがスムーズになり、誤解が最小限に抑えられます。

**ユースケース：**  
- テキストに合わせて拡大・縮小するボタン  
- 動的なリストやメニュー  
- 製品ギャラリーやダッシュボード  
- 適応型ウェブサイトレイアウト

**さらなる読み物：**  
- [A Guide to Auto Layout: Best Practices, Tips & Tricks | Figma (YouTube)](https://www.youtube.com/watch?v=1odqpkfkDL8)
- [Figma Handbook: Advanced Auto Layout by Design+Code](https://designcode.io/figma-handbook-advanced-layout)

---

## オートレイアウトの仕組み

### 基本概念

オートレイアウトはレイアウトルール、つまり**制約**を使用してUI要素の空間的関係を管理します。以下がその動作方法です：

- **制約：** 要素間のルールを定義します。例：「ボタンは常にラベルの下に16px」。
- **方向：** 要素が配置される軸—水平、垂直、折り返し、またはグリッド。
- **サイズ変更：** コンテナと子要素がコンテンツに合わせるか、スペースを埋めるか、固定されるかを決定します。
- **間隔とパディング：** 要素間の隙間とコンテナ内のスペースを設定します。
- **整列：** コンテナ内の位置—中央、左、右などを指定します。
- **ネスト：** 複雑な構造のために、オートレイアウトフレーム内に別のオートレイアウトフレームを配置します。

**例：**  
ラベルに「フィット」する幅を持つボタンは、テキストが変更されると自動的にサイズが変更され、一貫したパディングが維持されます。

**公式ドキュメント：**  
- [Figma: Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
- [Understanding Auto Layout – Apple Developer](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853-CH7-SW1)

### 主な機能

- **自動配置：** ピクセル単位の調整は不要。構造は自動的に処理されます。
- **コンテンツ駆動のサイズ変更：** 要素はコンテンツや利用可能なスペースに合わせて拡大/縮小します。
- **柔軟な整列：** 要素を整列（左、中央、右、上、下）または均等に分配します。
- **ネスト：** 複数のオートレイアウトを組み合わせて複雑なレイアウトを作成します。
- **絶対配置：** 必要に応じて特定の子要素をオートレイアウトルールから除外します。

---

## プラットフォーム固有：Figmaのオートレイアウト

Figmaのオートレイアウトは、インターフェースデザインとプロトタイピングのための最も強力なツールの一つです。

### オートレイアウトの追加と削除

- **追加：** レイヤーを選択 → `Shift + A`を押すか、サイドバーの**オートレイアウトを追加**をクリックします。
- **削除：** フレームを選択 → `Option + Shift + A`（Mac）または`Alt + Shift + A`（Windows）を押すか、右クリックして**オートレイアウトを削除**を選択します。

まだフレーム内にないオブジェクトを選択すると、Figmaはオートレイアウトが適用された新しいフレームを作成します。

[Figma公式の手順](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)

---

### 方向：水平、垂直、折り返し、グリッド

- **水平：** 子要素を行に配置します。
- **垂直：** 要素を列に配置します。
- **折り返し：** スペースが限られている場合、要素が新しい行/列に続くことを許可します。
- **グリッド（ベータ）：** 要素を行と列の両方に配置します。

**切り替え方法：**  
Figmaの右パネルにある方向コントロールを使用します。

**詳細：**  
[Auto layout flow in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#flow)

---

### 間隔、パディング、ギャップ

- **ギャップ/間隔：** アイテム間のスペース。固定値または「自動」として設定します。
- **パディング：** フレーム内の境界線とその子要素の間のスペース。均一に設定するか、各辺ごとに設定できます。

**調整：**  
右サイドバーで値を設定するか、キャンバス上のハンドルをドラッグします。

**例：**  
水平方向に16px、垂直方向に8pxのパディングを持つボタン。

**詳細：**  
[Advanced spacing and alignment – Figma Handbook](https://designcode.io/figma-handbook-advanced-layout)

---

### サイズ変更オプション：フィット、フィル、固定、最小/最大

- **コンテンツにフィット：** フレームは子要素に合わせてサイズが変更されます。
- **コンテナを埋める：** 子要素は親の利用可能なスペースを埋めるように拡大します。
- **固定サイズ：** コンテンツや親のサイズに関係なく、寸法は一定のままです。
- **最小/最大制約：** 要素が縮小または拡大できる最小/最大サイズを設定します。

**設定方法：**  
Figmaの右パネルの幅/高さドロップダウンを使用します。

**例：**  
幅が「フィット」に設定され、最小幅が100pxのボタンは、小さくなりすぎるのを防ぎます。

[Resizing and constraints in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#resize)

---

### オートレイアウトのネスト

**ネスト**により、モジュール式で複雑なデザインのために、あるオートレイアウトフレーム内に別のオートレイアウトフレームを配置できます。

**例：**  
垂直オートレイアウトのカードコンポーネントで、ヘッダー行（水平）とコンテンツエリア（垂直）を持つ。

**ショートカット：**  
`Ctrl + Shift + A`（Mac）または`Ctrl + Alt + Shift + A`（Windows）で「オートレイアウトを提案」。

[Building complex layouts – Figma Help Center](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#nest)

---

### 整列と分配

- **整列：** コンテナ内の位置を制御します。
- **分配：** 主軸に沿って要素を均等に配置します。

**設定方法：**  
サイドバーの整列コントロール（「グラムクラッカー」アイコン）を使用します。

**トラブルシューティング：**  
整列の変更は、整列するためのスペースがある場合にのみ効果があります。「フィット」フレームでは目に見える変化がない場合があります。

[Alignment and distribution in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#align)

---

### オートレイアウトを無視する（絶対配置）

**絶対配置**（現在は「オートレイアウトを無視」と呼ばれる）により、バッジなどのオーバーレイのために要素をレイアウトフローから除外できます。

**使用方法：**  
要素を選択 → デザインパネル → 「オートレイアウトを無視」をクリックするか、`Ctrl`を押しながらドラッグします。

**例：**  
アイコンの角に配置された通知バッジ。

[Absolute positioning in Figma](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout#absolute)

---

## 他のプラットフォームでのオートレイアウト

### iOS（SwiftUIとUIKit）

- **UIKit Auto Layout：** 空間的関係を定義するために制約を使用します。レイアウトはデバイスの向きとサイズに自動的に適応します。
- **SwiftUI：** レスポンシブな配置のためにHStack、VStack、ZStack、Spacerを使用します。

**Appleのドキュメント：**
- [Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)
- [Layout | Apple Developer Documentation](https://developer.apple.com/documentation/appkit/layout?language=objc)

**ヒント：**  
- 視覚的な制約編集にはInterface Builderを使用します。
- ノッチや丸い角に適応するレイアウトには「Safe Area」ガイドを使用します。

---

### Android（Jetpack Compose、XML、ConstraintLayout）

- **ConstraintLayout（XML）：** 柔軟なレイアウトのために制約（上、下、ベースラインなど）を定義します。フラットなビュー階層で、ネストされたビューグループは不要です。
- **Jetpack Compose：** Row、Column、Box、ConstraintLayoutコンポーザブルを使用してプログラムでレイアウトを構築します。

**Androidのドキュメント：**
- [ConstraintLayout (XML) Guide](https://developer.android.com/develop/ui/views/layout/constraint-layout)
- [ConstraintLayout in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)

**ベストプラクティス：**  
複雑で適応性のあるUIには、深いネストを避けるためにConstraintLayoutを使用します。

---

### Web（CSS Flexbox、Grid）

- **Flexbox：** 一次元レイアウト（行または列）。アイテムはスペースに合わせて拡大/縮小します。
- **CSS Grid：** 行と列の二次元レイアウト。高度に適応性があり、レスポンシブなデザインを可能にします。

**MDNドキュメント：**
- [Basic concepts of flexbox – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
- [Relationship of grid layout to other layout methods – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)

**例：**  
- ナビゲーションバーやツールバーにはFlexbox。
- 製品リストやダッシュボードにはGrid。

---

## 一般的なユースケースと例

### テキストに合わせて拡大するボタン

ボタンコンテナを固定パディングで「コンテンツにフィット」に設定すると、ボタンは常にラベルに合わせます—クリッピングや過剰な余白がありません。