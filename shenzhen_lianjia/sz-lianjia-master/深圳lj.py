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
            'Cookie': 'TY_SESSION_ID=4161343e-3927-4100-9533-5adb529f3e0c; lianjia_uuid=6ed7df6c-ebe5-4568-a5bf-2c21e546ca39; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1540622390; _smt_uid=5bd40836.2c7e9597; UM_distinctid=166b440154b306-06b5d47fe75004-47e1039-100200-166b440154d134; _jzqc=1; _jzqy=1.1540622391.1540622391.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91%E5%8C%97%E4%BA%AC.-; _jzqckmp=1; all-lj=3d8def84426f51ac8062bdea518a8717; _qzjc=1; CNZZDATA1254525948=667635047-1540617091-%7C1540622375; lianjia_ssid=f4217035-ac89-47ee-8799-142aaa2dedf2; _jzqa=1.4383878552266910700.1540622391.1540622391.1540624781.2; select_city=440300; CNZZDATA1255633284=1849769130-1540619624-%7C1540625025; CNZZDATA1255604082=1644370051-1540617480-%7C1540622360; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1540625223; _qzja=1.1426462676.1540622394159.1540622394159.1540625024479.1540625074932.1540625223403.0.0.0.17.2; _qzjb=1.1540625024479.3.0.0.0; _qzjto=17.2.0; _jzqb=1.4.10.1540624781.1; CNZZDATA1255849469=36534003-1540619700-%7C1540625224',
            'Host': 'nj.lianjia.com',
            'Referer': 'https://nj.lianjia.com/zufang/pudong/',
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
    soup=soup.find('div',class_='option-list').find_all('a')
    url_list=[]
    for s in soup[1:]:
        u='https://nj.lianjia.com'+s.get('href')
        url_list.append(u)
    #print(url_list)
    return url_list
def get_total_num(url):
    soup=Soup(url)
    total=soup.find('div',class_='list-head clear').find('h2').find('span').text
    pages = int(int(total) / 30) + 1
    total=int(total)
    print(total,pages)
    return total,pages

def get_house(url,total):
    df=pandas.DataFrame()
    soup=Soup(url)
    soup=soup.find('ul',class_='house-lst').find_all('li')
    for f in soup:
        try:
            inf = {}
            f = f.find('div', class_='info-panel')
            one = f.find('div', class_='where')
            two = f.find('div', class_='other').find('div', class_='con').text.split('/')
            inf['price'] = f.find('div', class_='price').find('span').text
            inf['name'] = one.find('a').find('span').text[:-2]
            inf['zone'] = one.find('span', class_='zone').find('span').text[:-2]
            inf['size'] = one.find('span', class_='meters').text[:-2]
            inf['朝向'] = one.find_all('span')[-1].text
            inf['add'] = two[0]
            inf['楼层'] = two[1]
            inf['year'] = two[2]
            # print(inf)
            df = df.append(inf, ignore_index=True)
            #print(df)
        except Exception as e:
            total=total-1
            print('第%d条信息爬取失败'%total)
    df.to_csv('nj1_lj.csv',index=False, mode='a', header=False)
def url_inf(url,pages,total):
    for page in range(1,int(pages)+1):
        q_url=url+'pg'+str(page)+'/'
        get_house(q_url,total)
        time.sleep(random.randint(1,10))
    print('一共爬取的%d条房屋信息'%total)

if __name__=='__main__':
    sta_time=time.time()
    print(sta_time)
    url='https://nj.lianjia.com/zufang/'
    url_lists=get_lianjia_url_lists(url)
    for url_list in url_lists:
        print('正在爬取%s的房屋信息'%url_list)
        to,pages=get_total_num(url_list)
        url_inf(url_list,pages,to)
    en_time=time.time()
    print(en_time)
    print('一共用时%d'%(en_time-sta_time))