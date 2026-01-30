---
title: "「コンタクト（顧客情報）」に関する API"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "customer-info-api"
description: "※ LiveAgent version 2.8.2.1 以降に対応します。"
keywords: ["API", "顧客", "情報", "LiveAgent", "メールアドレス"]
category: "settings"
---
## コンタクト（顧客情報）APIの概要

### 目次
- [全ての顧客名の取得](#全ての顧客名の取得)
- [特定の顧客情報の取得](#特定の顧客情報の取得)
- [グループ関連操作](#グループ関連操作)

## 全ての顧客名の取得

### API仕様
※ LiveAgent version 2.8.2.1 以降に対応します。

### APIエンドポイント
GET
  http://example.com/api/customers?apikey=[value]

### 必須パラメータ

| パラメータ名 | 形式 | 内容 |
| --- | --- | --- |
| apikey | text | API キー |

### オプションパラメータ

| パラメータ名 | 形式 | 内容 |
| --- | --- | --- |
| email | text | 指定の文字列を含むメールアドレスを有する顧客情報を呼び出します |
| firstname | text | 指定の文字列を含む名を有する顧客情報を呼び出します |
| lastname | text | 指定の文字列を含む姓を有する顧客情報を呼び出します |
| datecreatedfrom | datetime | 作成日がこの日時より新しい顧客情報を呼び出します |
| datecreatedto | datetime | 作成日がこの日時より古い顧客情報を呼び出します |
| limitcount | text | 指定値を呼び出し件数の最大値とします (デフォルトでは 100、最大 1,000まで値を指定できます) |
| limitfrom | text | Start from specified row number |

### レスポンスフィールド

| フィールド名 | 形式 | 内容 |
| --- | --- | --- |
| customers | list | 顧客のリスト |
| contactid | text | 顧客のコンタクト ID |
| email | text | 顧客のメールアドレス |
| firstname | text | 顧客の名 |
| lastname | text | 顧客の姓 |
| systemname | text | 顧客のシステム名 |
| userid | text | 顧客のユーザー ID |
| role | constlist | 顧客の属性 (有効値： V - Visitor, R - Registered visitor) |
| gender | constlist | 顧客の性別 (有効値： M - 男性, F - 女性) |

### レスポンス例
XML形式とJSON形式のレスポンス例は元の記事と同様です。

## 特定の顧客情報の取得

### API仕様
※ LiveAgent version 2.9.5.0 以降に対応しています。

### APIエンドポイント
GET
  http://example.com/api/customers/[customeridentifier]?apikey=[value]

### 必須パラメータ

| パラメータ名 | 形式 | 内容 |
| --- | --- | --- |
| [customeridentifier] | text | 顧客の識別子 (メールアドレスまたはコンタクト ID) |
| apikey | text | API キー |

### レスポンスフィールド

| フィールド名 | 形式 | 内容 |
| --- | --- | --- |
| contactid | text | 顧客のコンタクト ID |
| email | text | 顧客のメールアドレス |
| firstname | text | 顧客の名 |
| lastname | text | 顧客の姓 |
| systemname | text | 顧客のシステム名 |
| authtoken | text | 顧客のブラウザクッキーの識別子 |
| browsercookiename | constlist | 顧客のブラウザクッキーの名称 |
| role | constlist | 顧客の属性 |

## グループ関連操作
（元の記事の残りの操作に関する説明を追加する）