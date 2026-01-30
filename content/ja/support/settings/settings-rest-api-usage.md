---
title: "REST API の利用例 （サンプルコード）"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "settings-rest-api-usage"
description: "LiveAgent の API を利用したサンプルコードをご紹介します。"
keywords: ["REST", "API", "利用", "LiveAgent", "Agent"]
type: support
category: "settings"
e-title: "Rest - Api - Usage"
---

LiveAgent の API を利用したサンプルコードをご紹介します。

コード内の **[API_KEY]** は LiveAgent の API Key、**[CONV_CODE] , [conversationID]** はチケットの固有番号、**[example.com]** は LiveAgent 利用時のドメイン（ [xxx].liveagent.jp など）、を示します。

![](/liveagent/scripts/file.php?view=Y&file=3fc712b8cb1c78be7e8a92fbe175fc0d)

### GET リクエストの例

//next example will recieve all messages for specific conversation
$service_url = 'http://example.com/api/conversations/[CONV_CODE]/messages&apikey=[API_KEY]';
$curl = curl_init($service_url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$curl_response = curl_exec($curl);
if ($curl_response === false) {
    $info = curl_getinfo($curl);
    curl_close($curl);
    die('error occured during curl exec. Additioanl info: ' . var_export($info));
}
curl_close($curl);
$decoded = json_decode($curl_response);
if (isset($decoded->response->status) && $decoded->response->status == 'ERROR') {
    die('error occured: ' . $decoded->response->errormessage);
}
echo 'response ok!';
var_export($decoded->response);

### POST リクエストの例

//next example will insert new conversation
$service_url = 'http://example.com/api/conversations';
$curl = curl_init($service_url);
$curl_post_data = array(
        'message' => 'test message',
        'useridentifier' => 'agent@example.com',
        'department' => 'departmentId001',
        'subject' => 'My first conversation',
        'recipient' => 'recipient@example.com',
        'apikey' => 'key001'
);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_POSTFIELDS, $curl_post_data);
$curl_response = curl_exec($curl);
if ($curl_response === false) {
    $info = curl_getinfo($curl);
    curl_close($curl);
    die('error occured during curl exec. Additioanl info: ' . var_export($info));
}
curl_close($curl);
$decoded = json_decode($curl_response);
if (isset($decoded->response->status) && $decoded->response->status == 'ERROR') {
    die('error occured: ' . $decoded->response->errormessage);
}
echo 'response ok!';
var_export($decoded->response);

### PUT リクエストの例

//next eample will change status of specific conversation to resolve
$service_url = 'http://example.com/api/conversations/cid123/status';
$ch = curl_init($service_url);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
$data = array("status" => 'R');
curl_setopt($ch, CURLOPT_POSTFIELDS,http_build_query($data));
$response = curl_exec($ch);
if ($response === false) {
    $info = curl_getinfo($ch);
    curl_close($ch);
    die('error occured during curl exec. Additioanl info: ' . var_export($info));
}
curl_close($ch);
$decoded = json_decode($response);
if (isset($decoded->response->status) && $decoded->response->status == 'ERROR') {
    die('error occured: ' . $decoded->response->errormessage);
}
echo 'response ok!';
var_export($decoded->response);

### DELETE リクエストの例

$service_url = 'http://example.com/api/conversations/[CONVERSATION_ID]';
$ch = curl_init($service_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
$curl_post_data = array(
        'note' => 'this is spam!',
        'useridentifier' => 'agent@example.com',
        'apikey' => 'key001'
);
curl_setopt($curl, CURLOPT_POSTFIELDS, $curl_post_data);
$response = curl_exec($ch);
if ($curl_response === false) {
    $info = curl_getinfo($curl);
    curl_close($curl);
    die('error occured during curl exec. Additioanl info: ' . var_export($info));
}
curl_close($curl);
$decoded = json_decode($curl_response);
if (isset($decoded->response->status) && $decoded->response->status == 'ERROR') {
    die('error occured: ' . $decoded->response->errormessage);
}
echo 'response ok!';
var_export($decoded->response);