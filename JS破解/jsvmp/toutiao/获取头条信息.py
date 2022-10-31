import execjs
import time
from urllib.parse import urlencode
import requests


def get_sign():
    behot_time = int(time.time())
    url = f'https://www.toutiao.com/api/pc/list/feed?offset=0&channel_id=0&max_behot_time={behot_time}&category=pc_profile_channel&disable_raw_data=true&aid=24&app_name=toutiao_web'
    with open(r'./toutiao_signature.js', 'r', encoding='gbk') as f:
        ctx = execjs.compile(f.read())
        signatrue = ctx.call("get_signature", url)
        return signatrue


headers = {
            "Accept": "application/json, text/plain, */*",
            "referer": "https://www.toutiao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
url = "https://www.toutiao.com/api/pc/list/feed?"
params = {
    "channel_id": 0,
    "max_behot_time": int(time.time()),
    "category": "pc_profile_recommend",
    "aid": 24,
    "app_name": "toutiao_web",
    "_signature": get_sign()
}
print(get_sign())
url = url + urlencode(params)
resp = requests.get(url, headers=headers, params=params, timeout=20)
resp.encoding = resp.apparent_encoding
print(resp.json())
for data in resp.json()['data']:
    print(data)



