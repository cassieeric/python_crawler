# -*- coding: utf-8 -*-
import requests

keyword = "python"
try:
    kw = {"wd": keyword}
    request = requests.get("https://www.baidu.com/s", params=kw)
    request.raise_for_status()
    request.encoding = request.apparent_encoding
    print(len(request.text))
    print(request.text)
except:
    print("失败")

