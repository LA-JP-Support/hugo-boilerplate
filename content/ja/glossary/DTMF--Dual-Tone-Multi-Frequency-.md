---
title: DTMF(デュアルトーン多重周波数)
translationKey: dtmf-dual-tone-multi-frequency
description: DTMF(デュアルトーン多重周波数)は、キーパッド押下時に発生する固有の音声トーンを使用してコマンドを解釈し、通話をルーティングし、自動メニューナビゲーション、リモートコントロール、安全なデータ入力を可能にする電気通信シグナリングシステムです。電話網やデジタルプラットフォームで広く活用されています。
keywords: ["DTMF", "電気通信", "IVR", "VoIP", "PCI DSS"]
category: AI Chatbot & Automation, Telecommunication Systems
type: glossary
date: 2025-12-03
draft: false
term: ディーティーエムエフ(デュアルトーンたじゅうしゅうはすう)
reading: DTMF(デュアルトーン多重周波数)
kana_head: その他
e-title: DTMF (Dual-Tone Multi-Frequency)
---
## DTMFとは?

Dual-tone multi-frequency(DTMF)は、通信ネットワークやデジタル通信プラットフォームで使用される信号技術です。キーパッドの各キーを押すと、「低周波」グループと「高周波」グループからそれぞれ1つずつ、合計2つの音声周波数の独特な組み合わせが送信されます。これらのトーンは、電話をかけたり自動システムを操作したりする際に聞こえるビープ音です。DTMFにより、人間と機械の両方がコマンドを伝達し、通話をルーティングし、データを安全に入力することができます。

**日常的な文脈:**  
電話のキーパッドで数字を押してメニューを操作したり、テレフォンバンキングでPINを入力したりすると、DTMFトーンが生成されます。IVR(Interactive Voice Response)やチャットボットなどの自動システムは、これらのトーンを検出して入力を処理します。  
- [Sycurio Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)  
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)

## DTMFの仕組み

### 周波数マトリックスとキーパッドマッピング

DTMFは、各ボタンを押すたびに2つの特定の周波数をペアにすることで動作します。電話のキーパッドはマトリックス状に配置されています:

- **行:** それぞれに低周波数が割り当てられています(697 Hz、770 Hz、852 Hz、941 Hz)
- **列:** それぞれに高周波数が割り当てられています(1209 Hz、1336 Hz、1477 Hz、A-Dキー用に1633 Hz)

**技術的メカニズム:**  
- キーが押されると、電子回路が2つのトーンを生成します:1つは行(低周波グループ)から、もう1つは列(高周波グループ)からです。
- 結果として得られる信号は、これら2つの周波数の組み合わせであり、音声チャネルを通じて単一の音声信号として送信されます。
- 受信側のデコーダーがトーンを分離し、押されたキーを識別します。

**なぜ2つのトーンなのか?**  
各キーに2つの同時周波数を使用することで、ランダムな音や人間の声がコマンドを誤って発動することがほぼ不可能になり、信頼性とセキュリティが確保されます。  
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)

### 図解: DTMF周波数表

**標準12キーDTMFキーパッド周波数マッピング(ITU-T Q.23):**

|        | 1209 Hz | 1336 Hz | 1477 Hz |
|--------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |
| 770 Hz |   4     |   5     |   6     |
| 852 Hz |   7     |   8     |   9     |
| 941 Hz |   *     |   0     |   #     |

**拡張16キー(A–D)キーパッド:**

|        | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
|--------|---------|---------|---------|---------|
| 697 Hz |   1     |   2     |   3     |   A     |
| 770 Hz |   4     |   5     |   6     |   B     |
| 852 Hz |   7     |   8     |   9     |   C     |
| 941 Hz |   *     |   0     |   #     |   D     |

視覚的参照:  
![DTMF Frequency Chart](https://www.techtarget.com/rms/onlineimages/ns-dtmf_frequencies-h_half_column_mobile.png)  
- [TechTarget: DTMF Frequency Table](https://www.techtarget.com/searchnetworking/definition/DTMF)

## 歴史的背景

### パルスダイヤルの置き換え

DTMFが登場する前、電話システムは**パルスダイヤル**(ループ断続)を使用していました。これは、ロータリーダイヤルでローカルループの電流を断続的に遮断する方式でした。各数字は、特定の回数の高速な回線遮断で表現されていました。  
**制限事項:**  
- ダイヤルが遅く、特に大きい数字では顕著でした。
- 直接的な金属リンクに限定され、長距離では信頼性が低い。
- 機械部品のため、より複雑で信頼性が低い。

DTMFは1963年にBell System(「Touch-Tone」として販売)によって導入され、ダイヤル速度を向上させ、自動化を可能にし、新しいサービスをサポートしました。最初の公衆プッシュボタン電話は1963年11月18日に利用可能になりました。  
- [Twilio: The Introduction of Touch Tone Phones](https://www.twilio.com/docs/glossary/what-is-dtmf#the-introduction-of-touch-tone-phones)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)

## 応用と使用例

### カスタマーサービスとコールセンター

- **Interactive Voice Response(IVR):**  
  発信者は数字を押してオプションを選択し、自動メニューと対話します(「アカウント情報は1を押してください」)。
- **機密情報の入力:**  
  キーパッドを使用してアカウント番号、PIN、注文番号を入力し、安全に処理します。
- **通話ルーティング:**  
  DTMF信号により、通話を適切な部門や担当者に振り分けます。

### その他のDTMF使用例

- **テレフォンバンキング:**  
  DTMFトーンでバンキングメニューを操作し、取引を処理します。
- **リモートシステム制御:**  
  技術者が電話回線を通じてゲート、アラーム、機器を制御します。
- **ボイスメール操作:**  
  ユーザーがキーパッドの数字を押してボイスメールを管理します。
- **電話会議:**  
  参加者がDTMFを使用して、電話会議中にミュート/ミュート解除、録音、またはアクションを開始します。
- **アマチュア無線:**  
  DTMFで無線中継器やリモート機器を制御します。
- **クレジットカード処理:**  
  公衆電話やIVRシステムがDTMFを使用して安全にカードデータを送信します。
- **ホームオートメーション:**  
  レガシーシステムが電話回線を通じてDTMFでリモート制御を行います。

- [Sycurio: Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)

## 現代(VoIP/デジタル)およびレガシーシステムにおけるDTMF

### レガシー(アナログ)システム

- DTMFはアナログ音声信号として生成され、公衆交換電話網(PSTN)を通じて送信されます。
- 電話交換機がトーンをデコードして入力を解釈します。

### デジタルおよびVoIP(Voice over IP)システム

- 現代のVoIPネットワークは、ネイティブにアナログDTMFトーンを送信しません。
- DTMF信号は次のように送信される場合があります:
  - **インバンド:** 音声ストリーム内の音声トーンとして(例:RTP)。
  - **アウトオブバンド:** シグナリングプロトコルのデジタルイベントとして(例:SIP INFO、RFC 2833/4733、KPML)。
- **相互運用性:**  
  VoIPプラットフォームは、レガシーおよび現在のデジタルシステムと互換性のある形式でDTMF信号を中継する必要があります。
- **モバイル(携帯)電話:**  
  現代のモバイルデバイスはダイヤルした番号をデジタルで送信しますが、通話中のメニュー操作のためにDTMFトーンを生成できます。

- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)

## DTMFの技術標準

### ITU-T Q.23とキーパッドマッピング

- **ITU-T勧告Q.23:**  
  DTMFシグナリングの周波数ペア、トーン持続時間、キーパッドレイアウトを定義し、グローバルで一貫したシグナリングを保証します。
- **RFC 2833/4733:**  
  VoIPにおけるDTMFリレー(テレフォニーイベント用のRTPペイロード)を規定します。
- **SIP INFO/KPML:**  
  SIP環境でのDTMFシグナリングの代替方法。

- [ITU-T Recommendation Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [Twilio: DTMF Tones & Standards](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)

## DTMFシグナリング:インバンド vs. アウトオブバンド

- **インバンドシグナリング:**  
  DTMFトーンが音声オーディオと同じチャネルで可聴信号として送信されます(PSTN、アナログ、一部のVoIP RTPストリーム)。すべての参加者がトーンを聞くことができます。
- **アウトオブバンドシグナリング:**  
  DTMF桁が音声チャネルの外でデジタルで送信され、シグナリングプロトコルを使用します(例:SIP INFO、RFC 2833/4733)。
- **セキュリティ注意:**  
  インバンドは傍受や詐欺の影響を受けやすく、デジタルネットワークでの安全で信頼性の高い送信にはアウトオブバンドが推奨されます。

- [Twilio: In-Band vs. Out-of-Band Signaling](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)

## DTMF、AIチャットボット、自動化

- DTMFにより、キーパッド入力を通じて自動システム(IVR、チャットボット、仮想エージェント)との直接的な対話が可能になります。
- AI搭載プラットフォームはDTMFを検出して、メニュー選択を処理し、データを収集し、通話をルーティングします。
- **利点:**
  - より速いメニュー操作。
  - 騒音環境での音声認識と比較してエラーが少ない。
  - 機密データ(PIN、カード番号)を口頭で伝えずに安全に入力。
  - ライブエージェントの関与を減らすことで運用コストを削減。

- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)

## DTMFとPCI DSSコンプライアンス

**DTMFマスキングが重要な理由:**  
顧客が電話のキーパッドを使用して支払いカード情報を入力すると、結果として生成されるDTMF信号が通話録音やエージェントによって捕捉される可能性があり、セキュリティとコンプライアンスのリスクとなります。

**DTMFマスキング**は、DTMF信号がエージェントや録音に到達する前に傍受して隠蔽し、トーンをアスタリスクに置き換えるか空白にします。これにより、コンタクトセンターがPCI DSSの範囲外となり、機密データの露出を防ぎます。

**利点:**  
- 詐欺リスクの削減。
- PCI DSSコンプライアンスの簡素化。
- 顧客の信頼向上。
- 録音を一時停止せずにエージェント支援またはIVR決済フローを実現。

**仕組み:**  
- リアルタイム傍受:顧客が桁を入力すると、システムがトーンを検出し、エージェントや録音に到達する前に削除します。
- マスキングは、オンプレミスとクラウドベースの両方のコンタクトセンターで利用可能で、SIP/ISDNインフラストラクチャ全体で機能します。

**デモンストレーション:**  
NICE CXoneでの実際のDTMFマスキングとPCI DSSコンプライアント決済デモをご覧ください:  
[YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)

- [Sycurio: What is DTMF Masking?](https://sycurio.com/blog/dtmf-masking)
- [PCI Pal Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)

## 例と実用的なシナリオ

**IVRメニュー操作:**  
「口座残高は1を、取引履歴は2を、担当者と話すには3を押してください。」システムが「1」のDTMFを検出し、通話をルーティングします。

**安全な支払い入力:**  
顧客が電話のキーパッドを使用してクレジットカード番号を入力します。DTMFトーンはマスキングされ、安全に処理されます。

**電話会議の制御:**  
ホストが「*5」を押してすべての参加者をミュートします。システムがDTMFを検出してコマンドを実行します。

**リモートアクセス:**  
施設管理者がセキュリティシステムに電話し、DTMFでコードを入力してリモートゲートを開きます。

**アマチュア無線中継器の起動:**  
オペレーターがDTMFシーケンスを送信して中継器を起動したり機器を制御したりします。

## 参考文献と関連用語

- [Interactive Voice Response (IVR)](https://www.nice.com/products/interactive-voice-response-ivr)
- [Session Initiation Protocol (SIP)](https://www.techtarget.com/searchunifiedcommunications/definition/Session-Initiation-Protocol)
- [Pulse Dialing](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [In-Band vs. Out-of-Band Signaling](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [ITU-T Recommendation Q.23](https://www.itu.int/rec/T-REC-Q.23/en)
- [PCI DSS Compliance](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [SIP INFO, KPML, RFC 2833](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP (Voice over IP)](https://www.techtarget.com/searchunifiedcommunications/definition/VoIP)

**関連項目:**  
- Touch-Tone電話
- バンドシグナリング
- コールセンター
- カスタマーエクスペリエンス自動化
- 通信システム

## 参考資料

- [Sycurio: DTMF Technology Guide](https://sycurio.com/knowledge/glossaries/dual-tone-multiple-frequency-dtmf)
- [TechTarget: What is DTMF?](https://www.techtarget.com/searchnetworking/definition/DTMF)
- [Wikipedia: DTMF Signaling (PDF)](https://www.ece.iastate.edu/~alexs/classes/2021_Spring_575/code/19_Audio/02_Phone_Digits/Wikipedia-Dual-Tone.pdf)
- [Twilio: What are DTMF Tones?](https://www.twilio.com/docs/glossary/what-is-dtmf)
- [VoIP Nuggets: DTMF in SIP and RFC 2833](https://voipnuggets.com/2023/06/12/different-types-of-dtmf-in-sip-and-why-dtmf-via-rfc2833-is-more-reliable/)
- [Sycurio: DTMF Masking Guide](https://sycurio.com/blog/dtmf-masking)
- [NICE: What is Call Center DTMF?](https://www.nice.com/glossary/what-is-call-center-dual-tone-multi-frequency-dtmf)
- [YouTube: Sycurio DTMF Masking Demo](https://www.youtube.com/watch?v=-iMrUREflUY)
- [PCI Pal Agent Assist for NICE](https://cxexchange.niceincontact.com/apps/197219/pci-pal-agent-assist)

### 視覚補助の提案
- 周波数ラベル付きDTMFキーパッドマトリックス。
- IVRにおけるDTMF生成と検出を示すブロック図。
- PSTNとVoIPネットワークにおけるDTMFシグナリングのフローチャート。

**要約:**  
DTMF(Dual-Tone Multi-Frequency)は、キーパッド信号を音声周波数のペアにエンコードするグローバル標準であり、電話、IVRシステム、自動化プラットフォームが入力を解釈できるようにします。DTMFはパルスダイヤルに取って代わり、安全なデータ入力をサポートし、コールセンターでの自動化を推進し、レガシーアナログと現代のデジタルVoIP通信ネットワークの両方で不可欠な存在であり続けています。さらなる技術的詳細、プロトコル仕様、コンプライアンスガイダンスについては、この用語集全体の参考文献とリンクされたリソースを参照してください。

**詳細な技術ビデオ:**  
- [YouTube: DTMF Explainer Video](https://www.youtube.com/watch?v=bAbNl8O6sSY)
- [YouTube: Sycurio DTMF Masking & PCI DSS Demo](https://www.youtube.com/watch?v=-iMrUREflUY)