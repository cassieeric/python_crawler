# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import pandas
import time
import multiprocessing
import threading
import random
def get_ziru_url_lists(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'gr_user_id=deb84ba4-247e-44bc-8d4c-c7bf5c23b3ee; gr_session_id_8da2730aaedd7628=a223bad9-9a28-4cb6-a0f9-fdcc23af4c67; gr_session_id_8da2730aaedd7628_a223bad9-9a28-4cb6-a0f9-fdcc23af4c67=true; CURRENT_CITY_CODE=440300; CURRENT_CITY_NAME=%E6%B7%B1%E5%9C%B3; mapType=%20; Hm_lvt_038002b56790c097b74c818a80e3a68e=1540622747; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1540622979',
        'Host': 'sz.ziroom.com',
        'Referer': 'http://sz.ziroom.com/z/nl/z3-d23008674.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    html=requests.get(url,headers=headers).text
    soup=BeautifulSoup(html,'lxml')
    soup=soup.find('dl', class_="clearfix zIndex6").find('ul', class_="clearfix filterList").find_all('li')
    #r=re.compile(r'href="//sz.ziroom.com/z/nl/z3-d23008672-b611100878.html')
    print(soup)
    url_dic={}
    url_list=[]
    for s in soup[1:]:
        e=s.find_all('a')
        for i in e:
            url_dic[i.text]='http:'+i.get('href')
            url_list.append('http:'+i.get('href'))
    return url_list,url_dict

def Soup(url):
    try:
        headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Cookie': 'lianjia_uuid=6ed7df6c-ebe5-4568-a5bf-2c21e546ca39; _smt_uid=5bd40836.2c7e9597; UM_distinctid=166b440154b306-06b5d47fe75004-47e1039-100200-166b440154d134; _jzqx=1.1540710057.1540713012.2.jzqsr=sz%2Elianjia%2Ecom|jzqct=/zufang/nanshanqu/.jzqsr=sh%2Elianjia%2Ecom|jzqct=/zufang/songjiang/; _jzqy=1.1540622391.1540719866.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91%E5%8C%97%E4%BA%AC.jzqsr=baidu; lianjia_ssid=e7fb8968-5e83-4a68-95fc-0a7e3ef67c0e; select_city=110000; all-lj=ba32fa4540e52c45d4c94b9a16e82078; TY_SESSION_ID=04ce9e2d-919c-431f-99c7-a9ca378bf933; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1540704799,1540719866,1540719893,1540877528; CNZZDATA1253477573=1801209961-1540621782-%7C1540873791; CNZZDATA1254525948=1514267160-1540622375-%7C1540872703; CNZZDATA1255633284=681543997-1540619624-%7C1540873440; CNZZDATA1255604082=1866303294-1540617480-%7C1540876327; _jzqa=1.4383878552266910700.1540622391.1540719866.1540877528.7; _jzqc=1; _jzqckmp=1; _qzjc=1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1540877606; _qzja=1.2028125095.1540622692331.1540719866282.1540877527920.1540877575762.1540877606066.0.0.0.8.4; _qzjb=1.1540877527920.5.0.0.0; _qzjto=5.1.0; _jzqb=1.5.10.1540877528.1',
                'Host': 'bj.lianjia.com',
                'Referer': 'https://bj.lianjia.com/ershoufang/dongcheng/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
    except Exception as e:
        time.sleep(15)
        Soup(url)
    return soup
def get_lianjia_url_lists(url):
    soup=Soup(url)
    soup=soup.find('div',class_='sub_nav section_sub_nav').find_all('a')
    zon=[]
    url_list=[]
    for s in soup:
        u='https://bj.lianjia.com'+s.get('href')
        zon.append(s.text)
        url_list.append(u)
    #print(url_list)
    return zon,url_list

def get_total_num(url):
    soup=Soup(url)
    total=soup.find('div',class_='resultDes clear').find('h2').find('span').text
    pages = int(int(total) / 30) + 1
    total=int(total)
    print(total,pages)
    return total,pages

def get_house(url,total,c):
    df=pandas.DataFrame()
    soup=Soup(url)
    soup=soup.find('ul',class_='sellListContent').find_all('li',class_='clear LOGCLICKDATA')
    for f in soup:
        try:
            inf = {}
            one = f.find('div', class_='houseInfo').text.split('/')
            inf['zon'] = c
            inf['小区'] = f.find('div', class_='houseInfo').find('a').text
            inf['户型'] = one[1]
            inf['面积'] = one[2]
            inf['朝向'] = one[3]
            inf['装修'] = one[4]
            try:
                inf['电梯'] = one[5][0]
            except IndexError:
                inf['电梯'] = '无'
            r = re.compile(r'共(.*?)层')
            t = f.find('div', class_='positionInfo').text.split('/')
            inf['楼层'] = t[0][0]
            try:
                inf['楼高'] = r.findall(t[0])[0]
            except IndexError:
                inf['楼高'] = t[0][0]
            inf['year'] = t[1][:4]
            inf['地址'] = f.find('div', class_='positionInfo').find('a').text
            if f.find('div', class_='tag').find('span', class_='subway'):
                inf['地铁'] = '1'
            else:
                inf['地铁'] = '0'
            inf['price'] = f.find('div', class_='totalPrice').find('span').text
            k = re.compile(r'单价(.*?)元')
            inf['unitprice'] = k.findall(f.find('div', class_='unitPrice').find('span').text)[0]
            g = re.compile(r'(.*?)人')
            inf['关注'] = g.findall(f.find('div', class_='followInfo').text.split('/')[0])[0]
            df=df.append(inf,ignore_index=True)
            #print(df)
        except Exception as e:
            print(e)
            total = total - 1
            print('第%d条信息爬取失败' % total)
    df.to_csv('bj_二手房.csv',index=False, mode='a', header=False,columns=['zon','小区','户型','面积','朝向','装修','电梯','楼层','楼高','year','地址','地铁','price','unitprice','关注'])
def url_inf(url,pages,total,zon):
    z=zon
    for page in range(1,int(pages)+1):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`第%d页'%page)
        q_url=url+'pg'+str(page)+'/'
        get_house(q_url,total,z)
        time.sleep(random.randint(1,10))
    print('一共爬取的%d条房屋信息'%total)

if __name__=='__main__':
    sta_time=time.time()
    print(sta_time)
    url='https://bj.lianjia.com/ershoufang/dongcheng/'
    zons,url_lists=get_lianjia_url_lists(url)
    for zon,url_list in zip(zons[4:5],url_lists[4:5]):
        print('正在爬取%s的房屋信息'%url_list)
        to,pages=get_total_num(url_list)
        url_inf(url_list,pages,to,zon)
    en_time=time.time()
    print(en_time)
    print('一共用时%d'%(en_time-sta_time))
