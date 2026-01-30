---
title: "IVR"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "call-ivr"
description: "IVRは、YAMLスクリプトを使用して構成されます。どのように動作するかの下記例をご確認ください："
keywords: ["IVR", "エージェント", "セクション", "オンライン", "オフライン"]
type: support
category: "ticket-system/call-center"
e-title: "Ivr"
---

IVRは、YAMLスクリプトを使用して構成されます。どのように動作するかの下記例をご確認ください：

**⇒「設定」-「通話」-「番号」～使用する番号の「編集」-「IVR」**

 

**基本的な例：**

offline:
  - play: http://offline.message
  - voicemail
online:
  - play: http://welcome.message
  - ring
queue:
  - play: http://in.queue.music

 

3つの必須セクションがあります：

**・オフライン**

　-オンラインのエージェントがいないときに使用されます。

**・オンライン**

　-オンラインのエージェントがいるときに使用されます。

**・キュー**

　-呼び出し側（顧客）がキュー内で待機する必要があるときに呼び出しコマンドの後に使用されます。

上記の例では、オンラインのエージェントが誰もいないときに、オフラインアナウンスhttp://offline.messageが再生され、ボイスメールが記録されます。

エージェントがオンラインになると、http://welcome.messageが再生され、最初に対応可能となったエージェントにコールが鳴ります。すべてのエージェントが占有されている場合、コールはキューに入れられ、キュー内のhttp://in.queue.musicの音声が再生されます。

 

**高度な例：**

start:
  - play: http://welcome.to.our.support
  - choice:
      1:
        name: Sales department
        play: http://press.1.for.sales
        do:
          - transfer:
              to: salesDepartmentID
              if:
                online:
                  - play: http://welcome.to.sales
                  - ring
                offline:
                  - goto: voicemail
      2:
        name: Technical department
        play: http://press.2.for.tech
        do:
          - transfer:
              to: techDepID
              if:
                online:
                  - ring
                offline:
                  - goto: offline
voicemail:
  - play: http://leave.us.a.message
  - voicemail
offline:
  - play: http://call.us.later
queue:   
  - play: http://in.queue.music
  - choice:
      0:
        name: Wait
        play: http://press.0.to.wait.in.queue
        goto: queue
      1:
        name: Leave voicemail
        play: http://press.1.to.leave.voicemail
        goto: voicemail

 

IVRは開始セクションで開始します：

- http://welcome.messageのウェルカムメッセージが再生されます。

- http://press.1.for.salesとhttp://press.2.for.techの選択メッセージはループで再生されます*（ユーザは再生を待たなければなりません）*。

- システムはユーザの選択を待つ

  - 1の場合、コールはSalesチームに転送されます。

    - Salesチームにオンラインのエージェントがいる場合：

      - http://welcome.to.salesのメッセージが再生されます。

      - Salesチームのエージェントにコールが鳴り始めます。

    - Salesチームにオンラインのエージェントがいない場合：

      - コールはボイスメールセクションに移ります。

 

- 2の場合、コールはTechnicalチームに転送されます。

      - Technicalチームにオンラインのエージェントがいる場合 

　　　　- Technicalチームのエージェントにコールが鳴り始めます。

      - Technicalにオンラインのエージェントがいない場合：

        - コールはオフラインセクションに移ります。

オフラインセクションはhttp://call.us.laterを再生し、コールを停止します。

ボイスメールセクションはhttp://leave.us.a.messageを再生し、ユーザにボイスメールを録音させます。

発信者がキューの状態になると、キュー音楽が再生を開始します。

音楽が終了した後、ユーザは待機を続けたりボイスメールを残したりする選択肢が与えられます。

注：

選択コマンドを書く方法は2通りあります。1つは開始セクションに、2つ目はキューセクションに表示されます。より便利なものを選ぶことができます。

 

**ダイナミックIVRの例：**

start:
  - fetch:
      url: http://my.dynamic.script
      onError: offline
      params:
        from: {$from_number}
        to: {$to_number}
        ticket: {$conv_code}
offline:
  - play: http://call.us.later
queue:   
  - play: http://in.queue.music

 

動的に（例えば誰が呼び出しているかに基づいて）IVRスクリプトを生成したい場合、fetchコマンドを使用できます。

IVRはstartセクションで開始します。

- 最初の唯一のステップとして、http://mydomain.com/scripts/ivrというURLからIVRを取得し、この取得したIVRのstartセクションに進みます。

複数のパラメータをスクリプトに渡すことができます。ivrsパラメータは自動的に追加されます。これはgotoコマンドで使用できるように、メインスクリプトのIVR名のリストです（この場合はstart、offline、queue）。

 

start:
  - play: http://hello.peter
  - ring

 

スクリプトが既知の発信者番号であることを検出したので、パーソナライズされたウェルカムメッセージが生成されます。

それを顧客に再生してから、エージェントに電話をかけます。

fetchコマンドは、適切なフォーマット、インデント、スペースなどを使用して、正しいIVRスクリプトでプレーンテキストの返信を返す必要があります。

あるいは、YAMLオブジェクト/ファイルを返して、mimetypeを 'application / yaml'に設定することもできます。

注：

スクリプトが有効なIVRを生成しない場合は、コールが切断されます。

 

**DTMF入力の例：（バージョン5.3.3.4以上）**

start:
  - play: http://enter.your.dtmf.input.and.press.#.to.confirm
  - dtmf:
      url: http://my.dynamic.script
      onError: offline
      params:
        ticket: {$conv_code}
        value: DTMF_VALUE
offline:
  - play: http://call.us.later
queue:   
  - play: http://in.queue.music

 

呼び出し元から何らかの入力を取得する場合は、dtmfコマンドを使用できます。ユーザのDTMF入力が＃記号で終わるのを待ちます。

終了すると、結果は動的ivrスクリプトに渡されます（上記のセクションを参照）。

paramsのDTMF_VALUEプレースホルダは実際のdtmf入力に置き換えられます。