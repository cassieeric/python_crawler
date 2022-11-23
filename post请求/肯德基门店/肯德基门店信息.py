# coding: utf-8
import requests

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"}
params = {
    "cname": "",
    "pid": "",
    "keyword": "北京",
    "pageIndex": 1,  # 可以修改，代表提取的页面
    "pageSize": 10
}
request = requests.post(url=url, params=params)
response = request.json()
print(response)
