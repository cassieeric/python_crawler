# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import pandas
import time
from datetime import datetime
import json
import random
def getTime():
    d1=datetime(1971,1,1)
    print(d1)
    d2=datetime.now()
    print(d2)
    d3 = int((d2 - d1).total_seconds() * 1000)
    print(d3)
    print(time.time()*1000)
#getTime()
#url='https://api.bilibili.com/x/v2/reply?callback=jQuery17202479861083706283_1540867066061&jsonp=jsonp&pn=3&type=1&oid=18089528&sort=0&_='+str(int(time.time()*1000))
#获得整个视频集的相关信息

def get_video_inf(url):
    headers = {
        'Cookie': 'LIVE_BUVID=AUTO6915375856445563; stardustvideo=1; buvid3=EEB30FF5-70B4-4E16-B15A-94FE3F7AF07F163007infoc; rpdid=kmpsximoqmdoskmsqsxqw; finger=edc6ecda; CURRENT_FNVAL=16; sid=4ih3nm1u; fts=1540866975; UM_distinctid=166c2db295180-082aa06c2afa6d-47e1039-100200-166c2db2952110',
        'Host': 'api.bilibili.com',
        'Referer': 'https://www.bilibili.com/video/av18089528?from=search&seid=6372477925428032860',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    html = requests.get(url, headers=headers).json()
    html=html['data']['stat']
    print(html)
    print(html['aid'])
    print(type(html['aid']))
    video_inf={}
    video_inf['id']=html['aid']
    video_inf['投币']=html['coin']
    video_inf['弹幕']=html['danmaku']
    video_inf['dislike']=html['dislike']
    video_inf['收藏']=html['favorite']
    video_inf['点赞']=html['like']
    video_inf['评论']=html['reply']
    video_inf['分享']=html['share']
    video_inf['观看次数']=html['view']
    return video_inf

#获取评论信息
def get_comment(url):
    headers={
        'Cookie': 'LIVE_BUVID=AUTO6915375856445563; stardustvideo=1; buvid3=EEB30FF5-70B4-4E16-B15A-94FE3F7AF07F163007infoc; rpdid=kmpsximoqmdoskmsqsxqw; finger=edc6ecda; CURRENT_FNVAL=16; sid=4ih3nm1u; fts=1540866975; UM_distinctid=166c2db295180-082aa06c2afa6d-47e1039-100200-166c2db2952110',
        'Host': 'api.bilibili.com',
        'Referer': 'https://www.bilibili.com/video/av18089528',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    df=pandas.DataFrame()
    html=requests.get(url,headers=headers).text
    html=(html.split('(',1))[1][:-1]
    html=json.loads(html)
    reps=html['data']['replies']
    for rep in reps:
        inf={}
        inf['评论']=rep['content']['message']
        inf['time']=rep['ctime']
        inf['floor']=rep['floor']
        inf['点赞']=rep['like']
        inf['性别']=rep['member']['sex']
        inf['name'] = rep['member']['uname']
        inf['等级'] = rep['member']['level_info']['current_level']
        inf['回复']=rep['rcount']
        df=df.append(inf,ignore_index=True)
        #print(inf)
    df.to_csv('runningman2017.csv',index=False, mode='a', header=False,columns=['评论','time','floor','点赞','性别','name','等级','回复'],encoding='utf-8')
    
if __name__=='__main__':
    video_url='https://api.bilibili.com/x/web-interface/view?aid=18089528'
    video=get_video_inf(video_url)
    #print(video)
    pages=183
    for page in range(1,pages):
        print('开始抓取第%d页'%page)
        url = 'https://api.bilibili.com/x/v2/reply?callback=jQuery17207334597019735183_1540982500519&jsonp=jsonp&pn='+str(page)+'&type=1&oid=12551207&sort=0&_=' + str(
        int(time.time() * 1000))
        try:
            get_comment(url)
            time.sleep(random.randint(1,5))
        except Exception as e:
            print('重新抓取第%d页' % page)
            get_comment(url)
            time.sleep(30)
