import requests
import json
url = "https://appbuilder.baidu.com/rpc/2.0/cloud_hub/v1/ai_engine/agi_platform/v1/instance/integrated"
# app_token = 'bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee'
app_token = 'bce-v3/ALTAK-9UinPsl8K6bcn9lBLcCBb/3e01ada980e7e4d2f736f027482ff4659845b6e7'
payload = json.dumps({
  "query": "开始吧",
  "response_mode": "blocking"
})
headers = {
    'Content-Type': 'application/json',
    'X-Appbuilder-Authorization':'Bearer '+app_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
unicode_text = response.text
# 使用 decode 方法将 Unicode 转换为正常的中文文本
normal_text = unicode_text.encode('utf-8').decode('unicode_escape')
print(normal_text)
data = json.loads(response.text)
conversation_id = data['result']['conversation_id']
print(conversation_id)

payload = json.dumps({
  "query": "30",
  "response_mode": "blocking",
  'conversation_id':conversation_id
})
headers = {
    'Content-Type': 'application/json',
    'X-Appbuilder-Authorization':'Bearer '+app_token
}

response = requests.request("POST", url, headers=headers, data=payload)

unicode_text = response.text
# 使用 decode 方法将 Unicode 转换为正常的中文文本
normal_text = unicode_text.encode('utf-8').decode('unicode_escape')
print(normal_text)
j = response.json()
print(j)