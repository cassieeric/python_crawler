import requests
import json
import urllib.parse

songid = '1908392914'
data = {
    "rid": f"R_SO_4_{songid}",
    "threadId": f"R_SO_4_{songid}",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}
song_info = str(data)
param = (urllib.parse.quote(song_info))
param_url = f"http://127.0.0.1:12080/go?group=para&name=wangyiyun&action=get_para&param={param}"
response = requests.get(url=param_url).text
response_json = json.loads(response)
get_para = json.loads(response_json["get_para"])
encText = get_para["encText"]
encSecKey = get_para["encSecKey"]
# print(encText)
# print(encSecKey)


data = {
    'params': encText,
    'encSecKey': encSecKey
}

response = requests.post('https://music.163.com/weapi/comment/resource/comments/get?csrf_token=', data=data)
print(response.text)
