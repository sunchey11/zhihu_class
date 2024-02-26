import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=v4wc4o9yupwbmVyNJ001Gkbh&client_secret=uvTVKWyss0WlknN9DsMmAGPXO0oPlmOm&grant_type=client_credentials"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()
