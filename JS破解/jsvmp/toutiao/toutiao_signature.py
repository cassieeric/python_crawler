"""
@author/github: Shirmay1
@time: 2022/1/6 0006 上午 7:02
@desc: 头条signature
https://www.toutiao.com/?wid=1641423780855
滚动加载的方式会生成signature
"""


import logging
import requests
import time
import random
import execjs
from urllib.parse import urlencode
import socket


class TouTiaoSignature:

    def __init__(self):
        self.proxy = None
        self._options = None
        self.key_word = None
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "referer": "https://www.toutiao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.url = "https://www.toutiao.com/api/pc/list/feed?"
        self.params = {
            "channel_id": 0,
            "max_behot_time": 1641416108,
            "category": "pc_profile_recommend",
            "aid": 24,
            "app_name": "toutiao_web",
            "_signature": "_02B4Z6wo00901aZ2lPgAAIDBJnRuuEew5qWmUpBAAAhMxZHhD9qTa3cupN2Urq8zB0lCCUBhfGX7cZ-qjlLMQqCvMnq2Vh8C4fiHMrLFD0pIMV7vlhNfg6kz6kfY9rjfmo5UEULTjdQJcHQX56"
        }

    def url_requests(self, url, form_data=None):
        for i in range(5):
            try:
                if form_data:
                    resp = requests.post(url, headers=self.headers, data=form_data, proxies=self.proxy, timeout=20)
                else:
                    resp = requests.get(url, headers=self.headers, proxies=self.proxy, timeout=20)
                if resp.status_code != 200:
                    if resp.status_code in [404, 422]:
                        return
                    raise Exception(f'{url} {resp.status_code}')
                resp.encoding = resp.apparent_encoding
            except socket.error as err:
                logging.warning(f"socket timeout {err} ")
                self.proxy = None
            except Exception as _e:
                time.sleep(random.uniform(1, 2.5))
                logging.exception(f'requests_error:{_e}')
                self.proxy = None
            else:
                if not resp:
                    self.proxy = None
                    continue
                return resp

    def get_signature(self, suffix):
        with open(r"./signature.js", encoding="utf-8") as f:
            ctx = execjs.compile(f.read())
            signatrue = ctx.call("get_signature", suffix)
            return signatrue

    def process(self):
        behot_time = int(time.time())
        self.params.update({
            "max_behot_time": behot_time,  # 要么为0 要么为上一篇文章的最后一条的behot_time
            "_signature": self.get_signature(f"https://www.toutiao.com/api/pc/list/feed?channel_id=0&max_behot_time={behot_time}&category=pc_profile_recommend&aid=24&app_name=toutiao_web")
        })
        url = self.url + urlencode(self.params)
        res = self.url_requests(url)
        res.encoding = "GB232"
        print(res.json())
        for data in res.json()['data']:
            print(data)


if __name__ == '__main__':
    _object = TouTiaoSignature()
    _object.process()
