---
title: "カスタマーサポート用語集"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "start-customer-support-glossary"
description: "カスタマーサポート用語集について解説します。"
keywords: ["カスタマーサポート", "サポート", "用語集", "カスタマーポータル", "Automated"]
type: support
category: "getting-started"
e-title: "Customer Support - Glossary"
---

## AI活用

| 日本語 | 英語 | 解説 
| AI回答支援 | AI-Powered Response Suggestion | 顧客の質問文脈を解析し、担当者に最適な回答候補を提示します。LiveAgentの定型応答やナレッジと併用すると、表現の揺れを減らし、対応のスピードと一貫性を向上させます。 
| RAG（検索拡張生成） | Retrieval Augmented Generation, RAG | 外部ナレッジ（FAQ/過去チケット/マニュアル）を検索し根拠文書に基づいて生成。最新性と正確性を向上し、幻覚を抑制。 
| ガードレール | Safety Guardrails | 禁止トピック、PII除外、用語統一、レビュー必須などの安全・品質ルール。監査ログや人手検証と併用してリスクを低減。 
| チャットボット | Chatbot / Virtual Agent | AIが自動で一次対応を行い、営業時間外でもFAQに即時回答。LiveAgent連携で解決不可の内容は担当者へ円滑引き継ぎ。 
| ナレッジギャップ検知 | Knowledge Gap Detection | 未掲載のFAQや繰り返し問合せを検出し、記事追加・更新を促進。自己解決率と一次解決率を底上げ。 
| ナレッジベース自動生成 | Knowledge Base Auto-generation | 過去のチケットやマニュアルから記事を自動起草。更新頻度を高めても運用負荷を抑制。 
| プロンプトエンジニアリング | Prompt Engineering | 生成AIへの指示を設計・最適化。役割/制約/出力形式/評価基準を明記し再現性を高め、テンプレ化して運用へ。 
| 人工知能 | AI, Artificial Intelligence | パターン認識や意思決定を担う技術全般。分類・要約・自動応答・需要予測などで体験を底上げ。 
| 大規模言語モデル（LLM） | Large Language Model, LLM | 大量のテキストから学習し多用途に生成・要約・分類。回答草案、要約、意図推定に活用。ガードレールや社内ナレッジ併用で安定化。 
| 機械学習 | ML, Machine Learning | データから学習し将来の分類や予測を行う手法。再発検出や難易度予測などに応用。 
| 生成AI | Generative AI | テキストや画像、要約、返信文などを自動生成。回答候補、トーン統一、要約、ナレッジ起草などで速度と一貫性を向上。ガバナンスとしてレビューやログ保持、機密管理ルールが重要。 
| 自動化 | Automation / Workflow Automation | AI/ルールで繰り返し作業を機械化。SLA残時間に応じた通知や再割り当て、フォローアップ自動作成で品質維持。 
| 自然言語処理 | NLP, Natural Language Processing | 人間の言葉を理解・分類する基盤技術。意図抽出、要約、要件の自動タグ付けなどでBotや自動振り分けの精度向上。 
| 要約自動化 | Automated Summarization | 長文スレッドや通話記録の要点抽出。引き継ぎ時間短縮と意思決定の加速、SLA前倒し解決に寄与。 
| 意図分類 | Intent Classification | 問い合わせの目的を自動判定。優先度付けや自動ルーティング、エスカレーションの精度向上。 

## 機能

| 日本語 | 英語 | 解説 
| エスカレーション | Escalation / Priority Routing | 難易度の高い案件やSLA違反リスクのあるチケットを上位担当へ自動/手動で引き継ぎ。重要案件の見落としを防止。 
| カスタマーポータル / セルフサービスポータル | Customer Portal / Self-Service Portal | チケット履歴確認、ナレッジ/FAQ/フォーラムへアクセス。営業時間外でも自己解決を促進。 
| タグ | Tags | “支払い”“バグ”“VIP”などのラベル付けで分類・検索・レポートに活用。ルールで自動タグ付けも可能。 
| ダッシュボード | Dashboard / Agent Panel | 日々の対応の基点。一覧、チャット、通話、顧客情報、マクロ操作を集約し教育コストを削減。 
| チケット管理システム / ヘルプデスクソフトウェア | Ticketing System / Help Desk Software | 問い合わせをチケット化し一元管理。割り当て、優先度、SLA追跡で漏れや二重対応を防止。 
| フォーラム | Community Forum / Customer Forum | 情報共有・意見交換の場。コミュニティ主導のサポートで運用負担を軽減。 
| ライブチャット | Live Chat | Webで即時相談。デザイン、トリガー、事前フォーム、オフライン時のメッセージ化まで制御可能。 
| ルール / 自動化 | Rules / Automations | 条件に応じて割り当て、タグ、通知、ステータス変更を自動実行。営業時間や待機時間とも連動。 
| 共有受信トレイ | Shared Inbox / Universal Inbox | 全チャネルの問い合わせを1つの受信箱で処理。引き継ぎや重複返信を防止。 
| 提出フォーム / チケット送信 | Submit Ticket / Create Ticket Form | Webフォームからの起票入口。項目カスタマイズや添付、分岐や自動タグ付けで一次振り分け精度を向上。 
| 提案受付ボード | Suggestion Boards | 要望を収集し投票/コメントで優先度可視化。ロードマップ連携で顧客参加型の価値創造。 
| 定型応答 | Canned Responses / Predefined Replies | 頻出質問の回答をテンプレ化し再利用。表現統一と時間短縮、新人教育に有効。 
| 統合チャネル対応 | Omnichannel Support / Multichannel Support | メール・チャット・電話・SNS・フォームを横断し履歴を一元化。分断体験を解消。 
| ナレッジベース | Knowledge Base | FAQや手順書の記事集。検索性と階層化で自己解決率を向上。 

## 導入・運用

| 日本語 | 英語 | 解説 
| API連携 | API Integration | REST APIで自社システムやデータ基盤と連携。自動登録、状況参照、ワークフロー起動などに対応。 
| エージェント | Agent / Support Agent | 権限・役割・同時チャット数・可用時間を設定し、スキルやシフトに合わせて最適配置。 
| カスタマイズ | Customization | ポータル、フォーム、権限、ルール、SLAなどを調整。現場フローに最適化。 
| コンタクトセンター / コールセンター | Contact Center / Call Center | 通話、IVR連携、録音、発着信履歴のチケット化に対応。少人数でも高密度運用。 
| サービスデスク | Service Desk | ITILに基づく広義の窓口。インシデント、リクエスト、変更管理を包含。 
| サービスレベル合意 | SLA, Service Level Agreement | 応答/解決時間などの基準を定める取り決め。違反前通知や自動エスカレーションで品質担保。 
| システム連携 | Integration | CRM、決済、EC、在庫、Bot、通話、コラボ等と接続し散在情報を統合。 
| ナレッジ同期 | Knowledge Sync | ヘルプセンターやCRM等と双方向同期で最新性を維持。RAG/検索精度を持続。 
| ヘルプデスク | Help Desk | メール/チャット/電話/ポータルを統合し、窓口一本化と品質標準化。 
| 顧客関係管理 | CRM, Customer Relationship Management | 顧客情報・接点履歴・購買データを整理し長期関係を強化。履歴一元表示でパーソナライズを支える。 

## 効果測定

| 日本語 | 英語 | 解説 
| エージェント生産性 | Agent Productivity | 処理数、稼働率、応答/解決時間などの総合指標。偏り把握や教育・配分見直しに活用。 
| ネットプロモータースコア | Net Promoter Score, NPS | 推薦意向でロイヤルティを測定。兆候を早期把握し、戦略改善へ活用。 
| 初回応答時間 | First Response Time, FRT | 最初の返信までの時間。SLAや自動化と組み合わせ即応体制を仕組み化。 
| 初回解決率 | First Contact Resolution, FCR | 最初の接点で解決できた割合。ナレッジや定型応答、権限設計が鍵。 
| 品質評価（AI評価） | AI-based Quality Scoring | 正確性・トーン・方針準拠・SLA順守を自動採点。教育・レビューの効率化。 
| 問い合わせ件数 | Ticket Volume | 期間内の総問い合わせ数。偏り把握で人員計画やチャネル強化に反映。 
| 平均解決時間 | Resolution Time | 受付から解決までの平均。ボトルネック可視化や計画立案に有効。 
| 自動要因分析 | Automated Root Cause Analysis | 苦情・解約兆候の背景や再発要因を自動推定し、改善チケットやバックログへ接続。 
| 顧客努力指標 | Customer Effort Score, CES | 『解決までの手間の少なさ』を測定。UX最適化で低減可能。 
| 顧客満足度 | Customer Satisfaction, CSAT | 解決後の満足度評価。自動サーベイとレポートで改善サイクルを回しやすい。 

## インフラ

| 日本語 | 英語 | 解説 
| オンプレミス | On-Premises | 自社サーバ運用。独自要件や厳格なデータ管理に有効だが、保守負担と初期コストは高め。 
| クラウド / SaaS | Cloud / SaaS | ベンダー運用のクラウドをブラウザで利用。初期投資を抑え、最新機能とセキュリティ更新が適用。 
| スケーラビリティ | Scalability | 利用者数やトラフィック増に応じて段階的に拡張可能。成長に合わせた投資がしやすい。 
| データセキュリティ | Data Security | 暗号化、権限、監査ログ、規制適合などの総合対策で漏洩リスクを低減。 
| データ匿名化 | Data Anonymization | 個人情報・機密をマスキング/トークナイズし、AI処理や外部API連携前に保護。 
| 稼働時間 | Uptime | サービス可用性の割合。高稼働率は機会損失低減と信頼性向上に直結。SLA基礎指標。 

## ユーザー体験

| 日本語 | 英語 | 解説 
| パーソナライゼーション | Personalization | 履歴・属性・購買状況に基づく個別最適対応。履歴一元表示やCRM連携で文脈理解を強化。 
| ユーザーインターフェース | User Interface, UI | 状況を一目で把握できるシンプルなUI。直感的操作で教育コストを低減。 
| ユーザー体験 | User Experience, UX | 応答速度、透明性、自己解決のしやすさなど体験全体を最適化。 
| 多言語対応 | Multilingual Support | 管理画面やウィジェット、ナレッジ記事を多言語で提供。翻訳ワークフローと併用で負荷抑制。 
| 応答トーン統一 | Tone Consistency | ブランドガイドに沿って表現を自動整形。担当者間の文体差を是正し、一貫性を向上。