import requests
import json
import datetime
import pymongo
from pymongo import MongoClient
import time
import random
from urllib import parse
collection=MongoClient('localhost',27017)
collection=collection.movie
collection=collection['毒液']
def get_comment(url):
    useragnet=[
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    ]
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': '_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1672650f7e0c8-01f4bc25633d95-47e1039-100200-1672650f7e0c8; _lxsdk=CE5BF450EB1A11E8A47169D6D14683E08BFAA1637E344D4B8B3E18A6540975DE; v=3; __mta=186940695.1542536099924.1542536352540.1542537253364.4',
'upgrade-insecure-requests': '1',
'user-agent':random.choice(useragnet)  }
    html = requests.get(url, headers=headers).json()
    datas = html['cmts']
    com = []
    for data in datas:
        inf = {}
        inf['comment'] = data['content']
        inf['city'] = data['cityName']
        inf['name'] = data['nick']
        inf['score'] = data['score']
        inf['reply'] = data['reply']
        inf['apptime'] = data['startTime']
        inf['urseid'] = data['userId']
        inf['approve'] = data['approve']
        com.append(inf)
    collection.insert_many(com)
    return inf['apptime']
if __name__=='__main__':
    endtime='2018-11-06 00:00:00'
    #apptime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    apptime='2018-11-15 15:02:19'
    while endtime<apptime:
        time.sleep(random.randint(1,2))
        url = 'https://m.maoyan.com/mmdb/comments/movie/42964.json?_v_=yes&offset=0&startTime={}'.format(parse.quote(apptime))
        #print(url)
        apptime=get_comment(url)
        print(apptime)


