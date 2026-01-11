---
title: オートレイアウト
lastmod: '2025-12-19'
translationKey: auto-layout
description: オートレイアウトをマスターしましょう。UI要素を自動的に配置およびリサイズするデザイン機能です。Figma、iOS、Android、Webにおける基本概念、メリット、実装方法を網羅しています。
keywords:
- オートレイアウト
- Figma
- UIデザイン
- レスポンシブデザイン
- 制約
category: General
type: glossary
date: '2025-12-19'
draft: false
e-title: Auto-Layout
term: オートレイアウト
url: "/ja/glossary/auto-layout/"
aliases:
- "/ja/glossary/Auto-Layout/"
---
## Auto-Layoutとは?

Auto-Layoutは、定義したルールや制約に基づいて、インターフェース要素を自動的に配置、整列、リサイズするデザインおよび開発機能です。コンテンツ、画面サイズ、または要素の数が変化すると、Auto-Layoutは要素を再計算して再配置し、インターフェースがクリーンで読みやすく、レスポンシブな状態を維持します。

本を追加または削除するたびに、自動的に本を移動して間隔を調整する本棚を想像してください。Auto-Layoutは、UI要素に対して同じことを行います。挿入または削除する要素の数に関係なく、デザインは整理され、視覚的にバランスが保たれます。

## Auto-Layoutを使用する理由

**主な利点**

**効率性**
- 手動でのリサイズや再配置を大幅に削減
- コンテンツやコンポーネントを一度更新すれば、レイアウトがあらゆる場所で適応

**レスポンシブデザイン**
- 要素がさまざまな画面サイズに適応
- マルチデバイスデザインワークフローに最適

**一貫性**
- プロジェクト全体で均一な間隔、整列、比率を維持

**コラボレーション**
- デザイナーと開発者が同じルールセットに依存
- 引き継ぎを効率化し、誤解を最小限に抑える

**使用例**
- テキストに合わせて拡大または縮小するボタン
- 動的なリストやメニュー
- 製品ギャラリーやダッシュボード
- 適応型ウェブサイトレイアウト

## 基本概念

**制約**
- 要素間のルールを定義
- 例:「ボタンは常にラベルの16px下に配置」

**方向**
- 要素が配置される軸—水平、垂直、折り返し、またはグリッド

**リサイズ**
- コンテナと子要素がコンテンツにフィット、スペースを埋める、または固定されるかを決定

**間隔とパディング**
- 要素間のギャップとコンテナ内のスペースを設定

**整列**
- コンテナ内の位置を指定—中央、左、右など

**ネスト**
- Auto-Layoutフレームを相互に配置して、洗練された構造を作成

## FigmaにおけるAuto-Layout

**Auto-Layoutの追加と削除**
- 追加:レイヤーを選択 → `Shift + A`を押すか、サイドバーの「auto layoutを追加」をクリック
- 削除:フレームを選択 → `Option + Shift + A`(Mac)または`Alt + Shift + A`(Windows)を押す

**方向オプション**
- 水平:子要素を行に配置
- 垂直:要素を列に配置
- 折り返し:スペースが限られている場合、要素が新しい行/列に続くことを許可
- グリッド(ベータ版):要素を行と列の両方に配置

**間隔、パディング、ギャップ**
- ギャップ/間隔:アイテム間のスペース。固定値または「Auto」として設定
- パディング:フレーム内の境界線と子要素の間のスペース
- 例:水平16px、垂直8pxのパディングを持つボタン

**リサイズオプション**
- コンテンツにフィット:フレームが子要素に合わせてリサイズ
- コンテナを埋める:子要素が親の利用可能なスペースを埋めるように拡大
- 固定サイズ:寸法が一定のまま
- 最小/最大制約:要素が縮小または拡大できる最小/最大サイズを設定

**Auto-Layoutのネスト**
- ネストにより、モジュール式で複雑なデザインのために、あるAuto-Layoutフレームを別のフレーム内に配置可能
- 例:垂直Auto-Layoutを持つカードコンポーネント、ヘッダー行(水平)、コンテンツエリア(垂直)

**整列と分配**
- 整列:コンテナ内の位置を制御
- 分配:主軸に沿って要素を均等に配置

**Auto-Layoutを無視(絶対配置)**
- 絶対配置(現在は「Auto-Layoutを無視」と呼ばれる)により、要素をレイアウトフローから除外可能
- 例:アイコンの隅に配置された通知バッジ

## 他のプラットフォームにおけるAuto-Layout

**iOS(SwiftUIとUIKit)**
- UIKit Auto Layout:制約を使用して空間的関係を定義
- SwiftUI:HStack、VStack、ZStack、Spacerを使用してレスポンシブな配置を実現
- ヒント:視覚的な制約編集にはInterface Builderを使用。ノッチに適応するレイアウトには「Safe Area」ガイドを使用

**Android(Jetpack Compose、XML、ConstraintLayout)**
- ConstraintLayout(XML):フラットなビュー階層で柔軟なレイアウトのための制約を定義
- Jetpack Compose:Row、Column、Box、ConstraintLayoutコンポーザブルを使用
- ベストプラクティス:複雑で適応性のあるUIには、深いネストを避けるためにConstraintLayoutを使用

**Web(CSS FlexboxとGrid)**
- Flexbox:一次元レイアウト(行または列)。アイテムがスペースに合わせて拡大/縮小
- CSS Grid:行と列のための二次元レイアウト
- 例:ナビゲーションバーにはFlexbox、製品リストやダッシュボードにはGrid

## 一般的な使用例

**テキストに合わせて拡大するボタン**
- ボタンコンテナを固定パディングで「コンテンツにフィット」に設定

**レスポンシブなリストとメニュー**
- 垂直Auto-Layoutまたは垂直スタックを使用して、アイテムがリフローし、間隔が一貫性を保つ

**カードと複雑なコンポーネント**
- 各領域(ヘッダー、コンテンツ、アクション)にAuto-Layoutフレームをネスト

**通知バッジ**
- アイコンに重ねるバッジには「Auto-Layoutを無視」または絶対配置を使用

**適応型ウェブページ**
- CSS GridまたはFlexboxを使用して、異なる画面サイズに対してコンテンツをリフロー

## ベストプラクティス

**小さく始める**
- スケールアップする前に、小さなコンポーネント(例:ボタン)から始める

**ネストを使用**
- モジュール式で再利用可能なデザインを作成

**一貫した間隔を適用**
- 変数またはトークンを使用

**レイアウトルールを文書化**
- 明確性と将来のメンテナンスのため

**キーボードショートカットを使用**
- 効率性のため

## トラブルシューティング

**要素が重なる、またはリサイズされない**
- リサイズ設定を確認し、親/子に正しい設定がされているか確認

**整列が機能しない**
- 整列のためのスペースがあることを確認。「フィット」フレームは、目に見える整列の変更を制限する可能性がある

**ネストされたフレームが多すぎる**
- 可能な限りレイアウト構造を簡素化

**バッジ/オーバーレイが配置されない**
- 「Auto-Layoutを無視」を使用

**Auto-Layout適用後に間隔がずれる**
- パディングとギャップの値を手動で調整

## よくある質問

**FigmaのAuto-LayoutにおけるHug、Fill、Fixedの違いは何ですか?**
- Hug:コンテナが子要素のサイズに合わせる
- Fill:子要素が親の利用可能なスペースを埋める
- Fixed:要素が同じサイズのまま

**水平と垂直のAuto-Layoutを組み合わせることはできますか?**
- はい、ネストを介して可能:例えば、カードには垂直Auto-Layout、カードのヘッダーには水平

**要素をAuto-Layoutルールから無視させるにはどうすればよいですか?**
- 「Auto-Layoutを無視」(絶対配置)を使用

**Auto-Layoutはレスポンシブデザインに対応していますか?**
- はい、適応型/レスポンシブインターフェース用に設計されています

**Auto-Layoutフレームが予期せず縮小/拡大するのはなぜですか?**
- Figmaはコンテンツに基づいて初期パディングを設定します—必要に応じて右パネルで値を調整してください

## 参考資料

- [Figma Auto-Layout YouTube Tutorial](https://www.youtube.com/watch?v=1odqpkfkDL8)
- [Figma Help Center – Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
- [Figma Handbook – Advanced Auto Layout (Design+Code)](https://designcode.io/figma-handbook-advanced-layout)
- [CSS Flexbox Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
- [CSS Grid Guide (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)
- [Apple Auto Layout Documentation](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)
- [Android ConstraintLayout Guide](https://developer.android.com/develop/ui/views/layout/constraint-layout)
- [ConstraintLayout in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)
- [Apple Developer: Layout](https://developer.apple.com/documentation/appkit/layout?language=objc)
