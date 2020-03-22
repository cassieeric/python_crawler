import requests
import json
from selenium import webdriver 

url = 'http://openapi.tuling123.com/openapi/api/v2'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
while True:
    aa = input('我：')
    data ={
        "perception": {
            "inputText": {
                "text": aa
            },
            "selfInfo": {
                "location": {
                "city": "济南"}
            }
        },
        "userInfo": {
            "apiKey": "这里用自己的key",
            "userId": "aaaac"
        }
    }

    res = requests.post(url,headers=headers,data=json.dumps(data))

    try:
        print('机器人:'+res.json()['results'][0]['values']['text'])
        if aa == '退出':
            break
    except:
        print('机器人:' + res.json()['results'][0]['values']['url'])   

        url_1 =res.json()['results'][0]['values']['url']
        driver = webdriver.Chrome() 
        driver.get(url_1) 
