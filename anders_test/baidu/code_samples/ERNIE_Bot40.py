# https://console.bce.baidu.com/tools/#/api?product=AI&project=%E5%8D%83%E5%B8%86%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%B9%B3%E5%8F%B0&parent=ERNIE-Bot%204.0&api=rpc%2F2.0%2Fai_custom%2Fv1%2Fwenxinworkshop%2Fchat%2Fcompletions_pro&method=post

import requests
import json

API_KEY = "v4wc4o9yupwbmVyNJ001Gkbh"
SECRET_KEY = "uvTVKWyss0WlknN9DsMmAGPXO0oPlmOm"

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "1到100的和。只要结果"
            },
            {
                "role": "assistant",
                "content": "1到100的和为：$1+2+...+100 = 5050$"
            },
            {
                "role": "user",
                "content": "2*100等于多少"
            }
        ],
        "disable_search": False,
        "enable_citation": False
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()
