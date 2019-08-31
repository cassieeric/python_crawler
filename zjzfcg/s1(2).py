import requests
import time
url = "http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?pageSize=100&pageNo=1&sourceAnnouncementType=3001&keyword=%E7%99%BD%E8%9A%81&url=http%3A%2F%2Fnotice.zcygov.cn%2Fnew%2FnoticeSearch"
r1 = requests.get(url=url)

data_json = r1.json()
data_list = data_json["articles"]
for row in data_list:#type:dict
    link = row.get("url")
    title = row.get("title")
    ctime = time.strftime("%Y-%m-%d", time.localtime(int(int(row.get("pubDate"))/1000)))
    with open("xx.txt", "a", encoding="utf-8") as f:
        w_str = "===>".join([link, title, ctime])
        f.write(w_str + "\n")
    # print(link,title,ctime)