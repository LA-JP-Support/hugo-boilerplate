+++
title = "DTMF（デュアルトーン多重周波数）"
translationKey = "dtmf-dual-tone-multi-frequency"
description = "DTMF（デュアルトーン多重周波数）は、電話ネットワークやデジタルプラットフォームで、キー操作時に発生する固有の音声トーンを利用してコマンド解釈、通話のルーティング、自動メニュー操作、リモート制御、セキュアなデータ入力を行う通信信号システムです。"
keywords = ["DTMF", "通信", "IVR", "VoIP", "PCI DSS"]
category = "AIチャットボット＆自動化, 通信システム"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/DTMF--Dual-Tone-Multi-Frequency-/"

+++
## DTMFとは？

デュアルトーン多重周波数（DTMF）は、通信ネットワークやデジタル通信プラットフォームで使用される信号技術です。キーパッドの各キーを押すと、「低」グループと「高」グループからそれぞれ1つずつ、2つの異なる周波数が組み合わされて伝送されます。これらは電話をダイヤルしたり自動システムを操作したりする際に聞こえるビープ音です。DTMFによって、人と機械の両方がコマンドを伝達し、通話をルーティングし、データを安全に入力できます。

**日常的な利用例：**電話キーパッドで番号を押してメニューを操作したり、電話バンキングでPINを入力したりする際にDTMFトーンが発生します。IVR（自動音声応答）やチャットボットなどの自動化システムは、これらのトーンを検知して入力を処理します。  
- [Sycurio 技術ガイド](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)  
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)

## DTMFの仕組み

### 周波数マトリックスとキーパッドマッピング

DTMFは、各ボタン操作ごとに2つの特定周波数を組み合わせて動作します。電話のキーパッドは以下のようなマトリックス構成です：

- **行：**低周波（697 Hz、770 Hz、852 Hz、941 Hz）が割り当てられる
- **列：**高周波（1209 Hz、1336 Hz、1477 Hz、A～Dキー用1633 Hz）が割り当てられる

**技術的な仕組み：**- キーが押されると、電子回路によって行（低グループ）と列（高グループ）から1つずつトーンが生成されます。
- 2つの周波数が合成された信号が音声チャンネルで送信されます。
- 受信側のデコーダーがトーンを分離し、押されたキーを特定します。

**なぜ2つのトーンを使うのか？**各キーごとに2つの異なる周波数を同時使用することで、偶発的な音や人の声による誤作動をほぼ完全に防止し、信頼性・安全性を確保しています。  
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)

### ビジュアル：DTMF周波数表

**標準12キーDTMFキーパッド周波数マッピング（ITU-T Q.23）：**|        | 1209 Hz | 1336 Hz | 1477 Hz |
|--------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |
| 770 Hz |   4     |   5     |   6     |
| 852 Hz |   7     |   8     |   9     |
| 941 Hz |   *     |   0     |   #     |

**拡張16キー（A～D）キーパッド：**|        | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
|--------|---------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |   A     |
| 770 Hz |   4     |   5     |   6     |   B     |
| 852 Hz |   7     |   8     |   9     |   C     |
| 941 Hz |   *     |   0     |   #     |   D     |

ビジュアル参照:  
![DTMF Frequency Chart](https://www.techtarget.com/rms/onlineimages/ns-dtmf_frequencies-h_half_column_mobile.png)  
- [TechTarget: DTMF Frequency Table](https://www.techtarget.com/searchnetworking/definition/DTMF)

## 歴史的背景

### パルスダイヤルからの置き換え

DTMF導入以前は、**パルスダイヤル方式**（ループディスコネクト）が使われており、ロータリーダイヤルで回線の電流を断続して各番号を表現していました。  
**制限点：**- 特に大きな数字ではダイヤルが遅い
- 直接配線が必要で長距離では不安定
- 機械式部品のため複雑かつ信頼性が低い

DTMFは1963年にBell Systemによって「タッチトーン」として導入され、ダイヤルの高速化、オートメーションの実現、新サービスの提供を可能にしました。世界初のプッシュボタン式電話は1963年11月18日に登場しました。  
- [Twilio: The Introduction of Touch Tone Phones](https://www.twilio.com/docs/glossary/what-is-dtmf#the-introduction-of-touch-tone-phones)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)

## 主な用途と活用例

### カスタマーサービス・コールセンター

- **自動音声応答（IVR）：**発信者は番号を押して自動メニューと対話（「1を押して口座情報」など）
- **機密情報の入力：**キーパッドで口座番号やPIN、注文番号などを安全に入力
- **コールルーティング：**DTMF信号で正しい部署や担当者に通話を振り分け

### その他のDTMF活用例

- **電話バンキング：**バンキングメニュー操作や取引処理
- **遠隔システム制御：**技術者が電話回線を使いゲートやアラーム、機器を制御
- **ボイスメール操作：**キーパッド操作でボイスメールを管理
- **会議通話：**参加者がDTMFでミュート/解除、録音、各種機能を操作
- **アマチュア無線：**DTMFでリピーターや遠隔機器を制御
- **クレジットカード決済：**公衆電話やIVRでカード情報を安全に伝送
- **ホームオートメーション：**旧式システムでは電話回線経由で遠隔操作

- [Sycurio: Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)

## DTMFの現代（VoIP/デジタル）とレガシーシステムにおける活用

### レガシー（アナログ）システム

- DTMFはアナログ音声信号としてPSTN（公衆交換電話網）上で生成・伝送される
- 電話交換機がトーンをデコードして入力を解釈

### デジタル・VoIP（IP電話）システム

- 現代のVoIPネットワークはアナログDTMFトーンをそのまま送信しない
- DTMF信号は次の方法で送信される：
  - **インバンド：**音声ストリーム内で音声信号として送信（例：RTP）
  - **アウトオブバンド：**シグナリングプロトコル内でデジタルイベントとして送信（例：SIP INFO、RFC 2833/4733、KPML）
- **相互運用性：**VoIPプラットフォームは、レガシーおよび現行デジタルシステムと互換性のある形式でDTMF信号を中継する必要がある
- **モバイル（携帯）電話：**現代の携帯端末は番号入力をデジタル送信するが、通話中のメニュー操作用DTMFトーンも生成可能

- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)

## DTMFに関する技術標準

### ITU-T Q.23とキーパッドマッピング

- **ITU-T勧告Q.23：**DTMF信号の周波数ペア、トーン持続時間、キーパッド配置を定義し、世界的な一貫性を担保
- **RFC 2833/4733：**VoIPにおけるDTMF中継（RTPテレフォニーイベント用ペイロード）を規定
- **SIP INFO/KPML：**SIP環境でのDTMF信号送信用の代替方式

- [ITU-T Recommendation Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [Twilio: DTMF Tones & Standards](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)

## DTMF信号：インバンド vs アウトオブバンド

- **インバンド信号：**DTMFトーンが音声オーディオと同じチャンネル（PSTN、アナログ、一部VoIP RTP）で可聴信号として送信される（参加者全員がトーンを聞くことができる）
- **アウトオブバンド信号：**DTMF数字が音声チャンネルの外でシグナリングプロトコル（SIP INFO、RFC 2833/4733等）を使いデジタル送信される
- **セキュリティ注意：**インバンドは盗聴や不正のリスクがあり、デジタルネットワークではアウトオブバンド方式が安全・信頼性の点で推奨される

- [Twilio: In-Band vs. Out-of-Band Signaling](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)

## DTMF、AIチャットボット、自動化

- DTMFは、IVRやチャットボット、バーチャルエージェントなどの自動システムとキーパッド入力で直接対話を可能にします
- AI搭載プラットフォームは、DTMF入力を検知し、メニュー選択・データ収集・通話振り分けを実行
- **利点：**- メニュー操作の高速化
  - 雑音環境下でも音声認識より誤りが少ない
  - PINやカード番号など機密データを口頭で言わず安全に入力
  - オペレーター対応削減によるコストダウン

- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)

## DTMFとPCI DSSコンプライアンス

**なぜDTMFマスキングが重要か：**顧客がキーパッドでカード情報を入力する際、DTMF信号が通話録音やオペレーターに記録されると、セキュリティやコンプライアンスのリスクとなります。

**DTMFマスキング**は、DTMFトーンをエージェントや録音側に届く前に傍受し、アスタリスクや無音で置き換えて秘匿化します。これによりコンタクトセンターがPCI DSS適用外となり、機密データの漏洩防止が可能です。

**主な効果：**- 不正リスクの低減
- PCI DSSコンプライアンス対応の簡略化
- 顧客信頼度の向上
- 録音を止めずにエージェント支援やIVR決済フローが可能

**マスキングの仕組み：**- 顧客が数字を入力した瞬間にシステムがリアルタイムで検知し、トーンを除去
- オンプレミス・クラウド型どちらのコンタクトセンターでも利用可能で、SIP/ISDNインフラにも対応

**デモンストレーション：**NICE CXoneでのDTMFマスキング＆PCI DSS準拠決済の実例動画：  
[YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)

- [Sycurio: What is DTMF Masking?](https://sycurio.com/blog/dtmf-masking)
- [PCI Pal Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)

## 具体例・実践シナリオ

**IVRメニュー操作：**「1を押して残高照会、2で取引明細、3で担当者へ」など、システムが「1」のDTMFを検知して通話を振り分けます。

**安全な決済入力：**顧客がキーパッドでクレジットカード番号を入力し、DTMFトーンがマスキング＆安全に処理されます。

**会議通話のコントロール：**主催者が「*5」を押して全員をミュート、システムがDTMFを検知してコマンドを実行

**リモートアクセス：**施設管理者がセキュリティシステムに電話し、DTMFで開錠コードを入力して遠隔ゲートを開ける

**アマチュア無線リピーターの起動：**オペレーターがDTMFシーケンスでリピーターや機器を遠隔操作

## さらに学ぶ・関連用語

- [自動音声応答（IVR）](https://www.nice.com/products/interactive-voice-response-ivr)
- [セッション開始プロトコル（SIP）](https://www.techtarget.com/searchunifiedcommunications/definition/Session-Initiation-Protocol)
- [パルスダイヤル](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [インバンド vs アウトオブバンド信号](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [ITU-T勧告Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [PCI DSSコンプライアンス](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [SIP INFO, KPML, RFC 2833](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP（IP電話）](https://www.techtarget.com/searchunifiedcommunications/definition/VoIP)

**関連項目：**- タッチトーン電話
- バンド信号
- コールセンター
- 顧客体験自動化
- 通信システム

## 参考文献

- [Sycurio: DTMF Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [Sycurio: DTMF Masking Guide](https://sycurio.com/blog/dtmf-masking)
- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)
- [YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)
- [PCI Pal Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)

### ビジュアル資料案
- 周波数付きDTMFキーパッドマトリックス図
- IVRにおけるDTMF生成・検出のブロック図
- PSTNとVoIPネットワークでのDTMF信号フロー図

**まとめ：**DTMF（デュアルトーン多重周波数）は、キーパッド信号を2つの音声周波数ペアとしてエンコードする世界標準であり、電話、IVRシステム、自動化プラットフォームでの入力解釈を可能にします。DTMFはパルスダイヤルを置き換え、安全なデータ入力とコールセンター自動化を支え、レガシーアナログから最新デジタルVoIP通信まで不可欠な技術です。さらなる技術詳細やプロトコル仕様、コンプライアンス情報については、本グロッサリー内の参考文献やリンクを参照してください。

**技術解説動画：**- [YouTube: DTMF解説動画](https://www.youtube.com/watch?v=bAbNl8O6sSY)
- [YouTube: Sycurio DTMFマスキング＆PCI DSSデモ](https://www.youtube.com/watch?v=-iMrUREflUY)