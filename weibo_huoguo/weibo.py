from bs4 import BeautifulSoup
import requests
import urllib
import time
from urllib import request
import re
import pandas
headers={
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'SINAGLOBAL=1632522923416.777.1531234272201; _s_tentry=-; Apache=7622149179793.265.1542071073235; ULV=1542071073257:8:2:2:7622149179793.265.1542071073235:1541492142810; login_sid_t=6b2b34ad0958555164fded684ad56393; cross_origin_proto=SSL; UOR=,,www.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5WOoQDxCDgRdySaOWbrDnQ5JpX5K2hUgL.FozESKnXSo.fe0M2dJLoI7UAUgv4IPLy; ALF=1573607522; SSOLoginState=1542071522; SCF=Avlxsnh8v8R5ZTHxknJZcbufsrEmdGvhSwX1mx-hmMLg6XCe-6U1NJEBJEmbpmdP9KYu9Sd7zAVUeHszRZivHeU.; SUB=_2A2527lSyDeRhGeRM7loV9ifJyDuIHXVVmsF6rDV8PUNbmtAKLWLgkW9NU807b5PA1XQ5QjYY6sl3w-g3LR4L1TC5; SUHB=0V50jeuNmVjzD5; un=zuoyiya123@foxmail.com; wvr=6; ECARD-G0=3b12e468e76dbfb55a0adb3de1390008; WBStorage=e8781eb7dee3fd7f|undefined',
'Host': 'event.weibo.com',
'Referer': 'http://event.weibo.com/yae/event/lottery/result?pageid=100140E1198435&id=3436763&f=weibo',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
'''
for page in range(1,39):
    url = 'http://event.weibo.com/yae/aj/event/lottery/result?pageid=100140E1198435&id=3436763&page={}&prizeLevel=1&_t=0&__rnd='.format(str(page)) + str(
        time.time())
    html = requests.get(url, headers=headers).json()
    df=pandas.DataFrame()
    h = html['data']['html']
    soup = BeautifulSoup(h, 'lxml')
    n = soup.find_all('dd', class_='staff_name')
    r = re.compile(r'weibo.com/(.*?)/profile')
    for i in n:
        inf = {}
        inf['name'] = i.find('a').text
        k = i.find('a').get('href')
        inf['id'] = re.findall(r, k)[0]
        df=df.append(inf,ignore_index=True)
    df.to_csv('weibo.csv',encoding='utf-8',header=False,mode='a',index=False,columns=['id','name'])
'''
q='https://api.weibo.cn/2/comments/build_comments?flow=0&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id=141992686212489&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&lcardid=seqid%3A23443762%7Ctype%3A1%7Ct%3A31%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542854023%26&rid=0_0_0_2667276034987506065_0_0&cum=DF372ED1'
w='https://api.weibo.cn/2/comments/build_comments?flow=0&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id=141305493092671&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&lcardid=seqid%3A23443762%7Ctype%3A1%7Ct%3A31%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542854023%26&rid=0_0_0_2667276034987506065_0_0&cum=4FB2AACE'
e='https://api.weibo.cn/2/comments/build_comments?flow=0&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id=141030613576894&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&lcardid=seqid%3A23443762%7Ctype%3A1%7Ct%3A31%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542854023%26&rid=0_0_0_2667276034987506065_0_0&cum=B1FD8B03'
r='https://api.weibo.cn/2/comments/build_comments?flow=0&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id=141030613129300&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&lcardid=seqid%3A23443762%7Ctype%3A1%7Ct%3A31%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542854023%26&rid=0_0_0_2667276034987506065_0_0&cum=78C7E751'
qq=q.split('&')
ww=w.split('&')
for i in zip(qq,ww):
    print(i)
ee=e.split('&')
rr=r.split('&')
import random
from pymongo import MongoClient
collection=MongoClient('localhost',27017)
collection=collection['weibo']['weibo']
user=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
headers={
'Host': 'api.weibo.cn',
'User-Agent':random.choice(user),
'Cookie':'ALF=1544929289; _T_WM=39e20928a39c3b92a9cdd8d71f3e2550; WEIBOCN_FROM=1110006030',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'}
#url='https://api.weibo.cn/2/comments/build_comments?flow=0&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id=141992686212489&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&lcardid=seqid%3A23443762%7Ctype%3A1%7Ct%3A31%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542854023%26&rid=0_0_0_2667276034987506065_0_0&cum=DF372ED1'
#url='https://api.weibo.cn/2/comments/build_comments?flow=0&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id=141992686212489&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D3&lcardid=seqid%3A23443762%7Ctype%3A1%7Ct%3A31%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542854023%26&rid=0_0_0_2667276034987506065_0_0&cum=DF372ED1'
def get_inf(url):
    html = requests.get(url, headers=headers).json()
    max_id = html['max_id']
    print(max_id)
    n=0
    print( html['root_comments'])
    for i in html['root_comments']:
        inf = {}
        inf['text'] = i['text']
        inf['time'] = i['created_at']
        inf['disable_reply'] = i['disable_reply']
        inf['liked']=i['like_counts']
        inf['nick'] = i['user']['name']
        #inf['class'] = i['user']['class']
        inf['sex'] = i['user']['gender']
        inf['city'] = i['user']['city']
        inf['pro'] = i['user']['province']
        inf['location'] = i['user']['location']
        inf['关注'] = i['user']['friends_count']
        inf['fans'] = i['user']['followers_count']
        n=n+1
        collection.insert_one(inf)
        #print(inf)
    return max_id,n
total=0
#url='https://api.weibo.cn/2/comments/build_comments?flow=1&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_reload=1&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D1&uicode=10000002&count=20&trim_level=1&moduleID=feed&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&id=4308928831894875&luicode=10000003&featurecode=10000085&since_id=0&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D1&lcardid=seqid%3A870460522%7Ctype%3A1%7Ct%3A1%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542865414%26&rid=0_0_0_2669675512959047934_0_0&cum=A0D49DDF'
#max_id,num=get_inf(url)
#total=total+num
max_id='0'
zero=15
while zero:
    url ='https://api.weibo.cn/2/comments/build_comments?flow=1&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D1&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id={}&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D1&lcardid=seqid%3A870460522%7Ctype%3A1%7Ct%3A1%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542865414%26&rid=0_0_0_2669675512959047934_0_0&cum=6DD80FF3'.format(max_id)
    max = max_id
    try:
        max_id,num=get_inf(url)
    except Exception as e:
        print(e)
        time.sleep(30)
        max_id,num=get_inf(url)
    if not max_id:
        max_id=max
        zero=zero-1
        time.sleep(60)
    total=total+num
    time.sleep(random.randint(1,2))
    print(total)

