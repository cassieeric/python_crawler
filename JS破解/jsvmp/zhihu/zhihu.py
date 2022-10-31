"""
author:时一姐
date:2022/2/24
https://www.zhihu.com/search?type=content&q=python
加密参数：x-zse-96
"""

import requests
import execjs
from urllib.parse import quote
from hashlib import md5


class ZHuSignature:

    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://www.zhihu.com/search?type=content&q=python",
            "x-zse-93": "101_3_2.0",
            "x-api-version": "3.0.91",
            'x-app-za': 'OS=Web',
            "Accept-Language": "zh-CN,zh;q=0.9",
            "x-zse-96": ""
        }
    
    @staticmethod
    def get_signature(param):
        # # 算法的方式
        # with open(r"./zhihu_signature.js", encoding="utf-8") as f:
        #     ctx = execjs.compile(f.read())
        #     signatrue = ctx.call("get_signature",  md5(param.encode('utf8')).hexdigest())
        #     return signatrue
        # 补环境的方式
        with open(r"./jsdom_signature.js", encoding="utf-8") as f:
            ctx = execjs.compile(f.read())
            signatrue = ctx.call("b", md5(param.encode('utf8')).hexdigest())
            return signatrue

    def process(self, keyword):
        keyword = quote(keyword)
        ses = requests.session()
        url = f"https://www.zhihu.com/search?type=content&q={keyword}"
        res = ses.get(url, headers=self.headers, timeout=20)
        cookie_dc0 = res.cookies.get("d_c0", "")
        param = f'101_3_2.0+/api/v4/search_v3?t=general&q={keyword}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+{cookie_dc0}'
        x_zse_96 = self.get_signature(param)
        print(x_zse_96)
        self.headers.update({"x-zse-96": f"2.0_{x_zse_96}"})
        url = f"https://www.zhihu.com/api/v4/search_v3?t=general&q={keyword}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal"
        res = ses.get(url, headers=self.headers, timeout=20)
        print(res.json())


if __name__ == '__main__':
    _object = ZHuSignature()
    _object.process("百度")

