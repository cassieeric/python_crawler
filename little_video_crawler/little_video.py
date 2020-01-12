import requests
from bs4 import BeautifulSoup
import re
import json
import threading

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }

def get_href(url): # 提取每个视频所在网页的href,交给get_video_url（）函数
    response = requests.get(url, headers=header)
    items=json.loads(response.text)
    for item in items['data']['data']:
        title=item['title']
        VideoHtmlUrl='http:'+item['url']
        Guid=item['guid']
        print(title,url,Guid)
        down_load_video(title, VideoHtmlUrl, Guid)
        
def down_load_video(title, VideoHtmlUrl, Guid): # 下载视频
    url='https://shankapi.ifeng.com/feedflow/getVideoAuthUrl/{0}/getVideoAuthPath_1'.format(Guid)
    response=requests.get(url, headers=header)
    results=json.loads(response.text.replace('getVideoAuthPath_1(','').replace(')', ''))
    results=results['data']
    vid = results['authUrl']   # 得到除Vkey外的参数
    video_url='https://60-28-123-129.ksyungslb.com/video19.ifeng.com/video09/2020/01/08/p26275262-102-9987636-172625/index.m3u8?reqtype=tsl&'+vid
    response=requests.get(video_url, headers=header)
    IndexTs=response.text.split('\n')[5:][::2]
    for i in IndexTs:
        TsUrl='https://60-28-123-129.ksyungslb.com/video19.ifeng.com/video09/2020/01/08/p26275262-102-9987636-172625/'+i
        res = requests.get(TsUrl, stream=True, headers=header)  # 根据视频原始地址获得视频数据流
        with open('{0}.mp4'.format(title.replace('|', '')), 'ab')as f:  # 保存数据流为MP4格式
            f.write(res.content)
            f.flush()
def main():
    pagenum=3
    for i in range(1,pagenum):
        url='https://shankapi.ifeng.com/shanklist/getVideoStream/{0}/24/27-95288-/1'.format(i)
        t=threading.Thread(target=get_href,args=(url,))
        t.start()
if __name__=='__main__':
    main()
