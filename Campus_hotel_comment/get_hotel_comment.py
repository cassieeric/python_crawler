import requests
import json
import re
import time
import emoji
import threading
from bs4 import BeautifulSoup
from urllib.parse import unquote#乱码转中文
from urllib.parse import quote #中文转乱码
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
urlHttp='http://kuyukuyu.com/agents/get?uuid=1e660236-f391-40ef-929c-5f77dd1f5e1e'
def GetHotel(k):  #获得大学附近的酒店信息
    m = str(k).split(',')
    univesity=quote(m[1],encoding="utf-8")
    n=0
    flag=0  #以下循环的标志
    while flag==0:
        url='https://ihotel.meituan.com/hbsearch/HotelSearch'
        data={
            'utm_medium':'touch', 'version_name':'999.9','platformid':'1',
            'cateId':'20','newcate':'1','limit':'50','offset':'{0}'.format(50*int(n)),
            'cityId':'{0}'.format(m[0]),'ci':'1','startendday':'20200227~20200228',
            'startDay':'20200227','endDay':'20200228',
            'q':'{0}'.format(m[1]),'mypos':'39.735289%2C116.348179','attr_28':129,'sort':'distance',
            'userid':92855137,'uuid':'4498BB1F75C3C462E049855731E27FDEF4F7466C4099B649CE23FD0ECA63DF7B',
            'lat':'39.735289','lng':'116.348179','keyword':'{0}'.format(m[1]),'accommodationType':1
        }
        response=requests.get(url,headers=header,params=data)
        jsons=json.loads(response.text)['data']['searchresult']
        num = 0
        for i in jsons:
            name = i['name']  # 酒店名字
            addr = i['addr']  # 酒店地址
            lowestPrice = i['lowestPrice'] # 最低价
            scoreIntro = i['scoreIntro'] # 评分
            dis=i['dist'] #和大学之间的直线距离
            if dis<=2000: #爬2000米以内的酒店
                #print(name,addr,lowestPrice,scoreIntro,dis)
                num=num+1
                t=threading.Thread(target=get_comment,args=(i['realPoiId'],m[1],)) #get_comment为抓取评论的函数
                #print(i['realPoiId'])
                t.start()
            else:
                flag=1
        n=n+1
        all_num=n*50+num
    print(m[1]+"2000米附近有"+str(all_num)+'酒店')
def get_comment(realPoId,UniverCityName):#爬酒店评论数据，直到IsEnd=True,UniverCityName是大学的名字
    url='https://ihotel.meituan.com/api/v2/comments/biz/reviewCount?poiId={}'.format(realPoId)
    response=requests.get(url,headers=header)
    ReviewNum=json.loads(response.text)['Data']['Total']  #得到酒店最大评论数
    #print(ReviewNum,UniverCityName)
    url='https://ihotel.meituan.com/api/v2/comments/biz/reviewList'
    data={
        'referid':'{0}'.format(format(realPoId)),
        'limit':ReviewNum,#一次爬完所有评论
        'start':0,#本次爬的起始值
        'filterid':800,
        'querytype':1,
        'utm_medium':'touch',
        'version_name':999.9,
    }
    response=requests.get(url,headers=header,params=data)
    jsons=json.loads(response.text)
    CommentCounts=jsons['Data']['List']
    with open('{}.txt'.format(UniverCityName),'a')as f:
        for i in CommentCounts:
            text = str(i['Content']).replace(' ','').replace('\r','')#去掉表情
            Emoji = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF][\u2000-\u2fff]]')#去掉奇怪符号
            text = Emoji.sub('',text)
            text=emoji.demojize(text) #替换表情
            text = re.sub(':\S+?:', '', text)
            text = text.replace('#', '')
            print(text)
            f.write(text)

def main():
    infor = ['1,清华大学', '1,北京大学',
             '57,武汉大学', '50,浙江大学玉泉校区',
             '10,上海交通大学闵行校区', '10,复旦大学',
             '42,西安交通大学', '55,南京大学','20,中山大学','1,中国人民大学']  # 名字前的数字代表CityId
    for k in infor:
        t=threading.Thread(target=GetHotel,args=(k,))
        t.start()
if __name__=='__main__':
    main()