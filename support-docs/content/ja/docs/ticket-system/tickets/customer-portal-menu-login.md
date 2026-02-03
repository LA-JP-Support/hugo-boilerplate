---
title: "カスタマーポータルメニューから「ログイン」と「マイチケット」のリンクを削除するには"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "customer-portal-menu-login"
description: "カスタマーポータルで「ログイン」および「マイチケット」メニューを非表示にする方法をご案内します。"
keywords: ["カスタマーポータル", "チケット", "ポータル", "LiveAgent", "tickets"]
category: "ticket-system/tickets"
---
## カスタマーポータルのメニューリンクを非表示にする方法

カスタマーポータルで「ログイン」および「マイチケット」メニューを非表示にする方法をご案内します。

### テーマが「Montana」の場合

次のCSSコードをLiveAgentエージェント画面の**「カスタマーポータル」＞「設定」＞「デザインをカスタマイズ」＞「デザイン」＞「カスタムCSS」**&#8203;セクションに配置します。

*.MenuLinkI, .MenuLinkT {
display:none;
}*

*.montana #menu-item-login, .montana #menu-item-mytickets {
display:none;
}*

![](/liveagent/scripts/file.php?view=Y&file=4e0a43663f2d7f33cf8f705c8546f9f8)

![](/liveagent/scripts/file.php?view=Y&file=ad15827eebfc47cc28c5d69ba6821b3a)

![](/liveagent/scripts/file.php?view=Y&file=4fa8dbf6342a504de7efd0016a4f93f1)

#### チケット送信の非表示

「チケットを提出」も非表示にするには、**「カスタマーポータル」＞「設定」＞チケットを提出**&#8203;のところで、チケットの送信を禁止する設定にします。

![](/liveagent/scripts/file.php?view=Y&file=941d96f873b974f9f38e647481e7ecee)

### テーマが「Minimalist」または「Classic」の場合

下記の3行を「カスタムCSS」に追加して、メニュー項目を含むボックスを非表示にします。

*.RightBox:first-child  {
display:none;
}*

## 注意事項

テーマを別のテーマに切り替える場合は、カスタムCSSのコードを再適用する必要があります。テーマごとに独自のカスタムCSSがあるからです。