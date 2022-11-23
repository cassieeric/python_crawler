# coding: utf-8
import requests
import csv

url = 'http://www.xinfadi.com.cn/getPriceData.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"}
param = {
    "limit": 20,
    "current": 1
}
response = requests.get(url=url, params=param).json()
f = open("vegetable_price.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)
for data in response['list']:
    id = data['id']
    prodName = data['prodName']
    prodCatid = data['prodCatid']
    prodCat = data['prodCat']
    prodPcatid = data['prodPcatid']
    prodPcat = data['prodPcat']
    lowPrice = data['lowPrice']
    highPrice = data['highPrice']
    avgPrice = data['avgPrice']
    place = data['place']
    specInfo = data['specInfo']
    unitInfo = data['unitInfo']
    pubDate = data['pubDate']
    status = data['status']
    userIdCreate = data['userIdCreate']
    userIdModified = data['userIdModified']
    userCreate = data['userCreate']
    userModified = data['userModified']
    gmtCreate = data['gmtCreate']
    gmtModified = data['gmtModified']
    csv_writer.writerow([id, prodName, prodCatid, prodCat, prodPcatid, prodPcat, lowPrice, highPrice, avgPrice, place,
                         specInfo, unitInfo, pubDate, status, userIdCreate, userIdModified, userCreate, userModified,
                         gmtCreate, gmtModified])

print("Writer over!")








