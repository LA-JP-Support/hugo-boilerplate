---
title: Cron スケジュール
date: 2025-12-19
lastmod: 2026-04-02
translationKey: cron-schedule
description: Unix/Linux で定期的なタスク自動実行を指定する時間設定方式。「毎日午前 2 時にバックアップ」など、正確な時刻指定が可能。
keywords:
- cron スケジュール
- タスク自動化
- crontab
- スケジューリング
- Unix/Linux
category: AI・機械学習
type: glossary
draft: false
e-title: Cron Schedule
term: クーロンスケジュール
url: /ja/glossary/cron-schedule/
aliases:
- /ja/glossary/Cron-Schedule/
---

## Cron スケジュールとは?

**Cron スケジュールは、サーバーやクラウドシステムで「何月何日の何時何分に、このコマンドを自動実行する」と指定する仕組みです。** バックアップ、レポート生成、データ同期など、繰り返しタスクを手作業なしで実行。

> **ひとことで言うと：** パソコンの「タスクスケジューラー」の Linux 版。複雑な時間指定が可能で、業務自動化の基本ツール。

**ポイントまとめ：**

- **何をするものか：** 指定時刻にスクリプト・コマンドを自動実行
- **なぜ必要か：** 人手不足対応、ヒューマンエラー削減、24 時間自動運用
- **書き方：** 5 つの数字（分 時 日 月 曜日）+ コマンド

## 重要性

毎日午前 2 時のバックアップ、毎週月曜の営業レポート作成、毎月 1 日の請求書発行…。こうしたルーチンワークが全部自動化できれば、人員を他の仕事に充てられます。また、手作業に比べて「忘れた」「時間を間違えた」といった人為的ミスがゼロになります。

クラウド時代にはますます重要。AWS Lambda、Google Cloud Functions なども cron 互換のスケジューリング機能を提供しており、企業システムの標準となっています。

## 仕組み

Cron は背景で「cron デーモン」というプログラムが動いており、毎分システム時刻をチェック。指定時刻になったら自動的にコマンドを実行します。

**基本形式：**
```
分 時 日 月 曜日 実行するコマンド
```

例えば：
- `0 2 * * *` = 毎日午前 2 時（分:0、時:2、日:すべて、月:すべて、曜日:すべて）
- `0 9 * * 1-5` = 平日午前 9 時（曜日:1-5 は月～金）
- `*/15 * * * *` = 15 分ごと

## 実務例

**バックアップスクリプト：**
```
0 2 * * * /home/user/backup.sh
```
毎日午前 2 時にバックアップスクリプトを実行。

**レポート生成：**
```
0 8 1 * * /usr/local/bin/generate_report.sh
```
毎月 1 日午前 8 時に営業レポートを自動生成。

**ヘルスチェック：**
```
*/5 * * * * /opt/healthcheck.sh
```
5 分ごとにサーバーヘルスチェック実行。

## 設定方法

Linux/Mac ターミナルで以下のコマンドで cron 登録ファイル（crontab）を編集：

```bash
crontab -e
```

すると テキストエディタが開き、上記の形式で記述。保存して終了すると自動登録。

```bash
crontab -l  # 登録済みの cron 一覧表示
crontab -r  # すべて削除
```

## メリットと注意点

**メリット：** 完全自動化、24/7 運用が可能、人員効率化。

**注意点：** 実行に失敗しても自動通知はない（メール転送設定で対応）。また、サーバーが止まると実行されません。重要なタスクは冗長化・監視が必要。

## 関連用語

- **[タスク自動化](Task-Automation.md)** — cron を含む自動化全般の概念
- **[スクリプト](Script.md)** — 実行するプログラム
- **[バックアップ](Backup.md)** — cron で自動実行されることが多い
- **[ジョブスケジューラー](Job-Scheduler.md)** — 複数ステップのタスク管理
- **[DevOps](DevOps.md)** — cron でのシステム自動化は DevOps の基本

## よくある質問

**Q: 5 つの数字の正確な範囲は？**
A: 分（0-59）、時（0-23）、日（1-31）、月（1-12）、曜日（0-6、日曜=0）。

**Q: 実行失敗時の通知は？**
A: crontab 実行結果はデフォルトではログに記録されるだけ。メール送信設定で失敗通知を受け取るか、外部の cron 監視ツール（Cronitor など）を使用。

**Q: クラウドサービスでも使える？**
A: AWS Lambda、Google Cloud Functions、Azure Functions はすべて cron 互換のトリガー設定に対応。

## 参考リンク

1. [Linux man ページ：crontab](https://linux.die.net/man/5/crontab)
2. [Crontab Generator（目視チェック用）](https://crontab-generator.org/)
3. [Cronitor（cron 監視）](https://cronitor.io/)
4. [AWS EventBridge（cron 互換）](https://aws.amazon.com/jp/eventbridge/)
5. [Google Cloud Scheduler](https://cloud.google.com/scheduler)
