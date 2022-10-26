import urllib.request

url = "http://tieba.baidu.com/"
headers = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"}

proxy_hander = urllib.request.ProxyHandler(
    {"http": "172.12.24.45:8080",
     "https": "120.34.5.46: 8080"
    }
)
opener = urllib.request.build_opener(proxy_hander)
urllib.request.install_opener(opener)

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode("GBK"))
