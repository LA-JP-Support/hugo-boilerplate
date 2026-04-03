---
title: LangFlow
translationKey: langflow
description: LangChainベースのオープンソースビジュアルフレームワーク。ドラッグ&ドロップでAIアプリケーションを構築・テスト・デプロイできます。
keywords:
- LangFlow
- LLM
- AIアプリケーション
- LangChain
- ローコード
category: AI・機械学習
type: glossary
date: '2025-12-19'
lastmod: 2026-04-02
draft: false
e-title: LangFlow
term: ラングフロー
url: "/ja/glossary/langflow/"
aliases:
- "/ja/glossary/LangFlow/"
---

## LangFlowとは？

**LangFlowは、LangChainベースのオープンソースビジュアルフレームワークで、LLM駆動型アプリケーションをコーディングなしで構築・テスト・デプロイできます。** ドラッグ&ドロップで各コンポーネント（LLM、プロンプト、ベクトルストア、ツール）を接続し、複雑なAIワークフローを直感的に設計できます。

> **ひとことで言うと：** LLMアプリを「ビジュアルで」簡単に作る工具です。

**ポイントまとめ：**

- **何をするものか：** コード不要でAIアプリを設計・構築できるビジュアルエディタ
- **なぜ必要か：** 技術者でなくても、AIワークフローを構築・共有できるから
- **誰が使うか：** データサイエンティスト、非技術者、開発者

## なぜ重要か

LangFlowは、AI開発の民主化を実現します。複雑なコーディングが不要なため、ビジネスチームやデータ分析チームも直接AIソリューションを構築・イテレーションできます。また、LangChainの完全な力を保持しながら、非開発者にもアクセシブルです。ビジュアルワークフローにより、チーム間のコミュニケーション・理解も高まります。

## 主な機能

**ビジュアルキャンバス** - ノードをドラッグして接続し、データフロー・ロジックを定義。複雑なワークフローが直感的に設計できます。

**プリセットコンポーネント** - LLM、データローダー、ベクトルストア、検索機能など、豊富な事前構築ノード。カスタムコンポーネント追加も可能。

**リアルタイムテスト** - プレイグラウンドモードで、デプロイ前にワークフローをインタラクティブにテスト。即座のフィードバックで素早い改善が実現。

**複数モデル統合** - OpenAI、Claude、Llamaなど主要LLMをサポート。モデル間の切り替えが簡単。

**ベクトルストア連携** - Pinecone、FAISS、Weaviateなど主要な埋め込みDB対応。RAG実装が容易です。

## 関連用語

- **[LangChain](LangChain.md)** — LangFlowの基盤となるフレームワーク
- **[RAG（検索拡張生成）](RAG.md)** — LangFlowの典型的なユースケース
- **[ベクトルデータベース](Vector-Database.md)** — LangFlowで使用する技術
- **[プロンプトエンジニアリング](Prompt-Engineering.md)** — LangFlow内の重要なステップ
- **[エージェント](Agent.md)** — LangFlowで構築する高度なワークフロー
- **[OpenAI](OpenAI.md)** — LangFlowが対応するLLMプロバイダー
- **[ノーコード/ローコード](No-Code-Low-Code.md)** — LangFlowの開発パラダイム
- **[API統合](API-Integration.md)** — LangFlowで実装可能な機能

## よくある質問

**Q: LangFlowはLangChainの完全な機能をサポートしていますか？**
A: ほぼ全機能対応ですが、非常に複雑なカスタムワークフローは、コード拡張が必要な場合もあります。

**Q: ビジュアルで設計したフローをコードにエクスポートできますか？**
A: はい。フローをPythonコードにエクスポートし、さらにカスタマイズできます。

**Q: 本番環境にデプロイできますか？**
A: はい。フローをAPIエンドポイントまたは独立したPythonアプリケーションとしてデプロイ可能です。

**Q: チーム開発は可能ですか？**
A: はい。フローの共有、バージョン管理、協調編集が可能です。

## 参考文献

- [LangFlow Official Documentation](https://docs.langflow.org)
- [LangFlow GitHub Repository](https://github.com/langflow-ai/langflow)
- [LangFlow Getting Started](https://docs.langflow.org/get-started-quickstart)
