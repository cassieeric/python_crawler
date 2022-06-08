import os
import re
import requests
from bs4 import BeautifulSoup
import csv 

class HousePrices:
    # dir='c:\\链家房价'#D盘
    dir='d:\\链家房价'  # D盘
    start_url='https://cs.lianjia.com/ershoufang/pg{}/'
    headers={
        'Host':'cs.lianjia.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Cookie':'select_city=110000; lianjia_ssid=74f665ec-d197-4606-8984-13a060a7a339; lianjia_uuid=dcc2c7eb-d4ec-4c91-976e-e47240db8e8f; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1622355363; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1622355363; _jzqa=1.4299380220423246000.1622355363.1622355363.1622355363.1; _jzqb=1.1.10.1622355363.1; _jzqc=1; _jzqckmp=1; UM_distinctid=179bbea4504567-0d4c995a89d9998-1a387940-1aeaa0-179bbea4505537; CNZZDATA1253477573=963747252-1622352689-%7C1622352689; _qzja=1.1539867698.1622355363107.1622355363107.1622355363107.1622355363107.1622355363107.0.0.0.1.1; _qzjb=1.1622355363107.1.0.0.0; _qzjc=1; _qzjto=1.1.0; CNZZDATA1254525948=602998940-1622352085-%7C1622352085; CNZZDATA1255633284=1358575326-1622349996-%7C1622349996; CNZZDATA1255604082=2083114816-1622352761-%7C1622352761; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179bbea4708260-00a97d6b6709128-1a387940-1764000-179bbea470986%22%2C%22%24device_id%22%3A%22179bbea4708260-00a97d6b6709128-1a387940-1764000-179bbea470986%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; _smt_uid=60b32da3.1b302184; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZThkMDBlMzVkN2E3MDg0YTkyYWU5YzhiNzA1NzYxNjQ3YzM3NjY5NDhhNzE3NjdmYmUxM2UyZmM4MmE3ZjUyMzEwNmMyZjU3MzRkNmIzMjM0ZGMxNjkyOWM4MmQ2MzhiNDZlZWMwZGQ0NWYyNGViNjE3M2YyZmQ1ODc1YmVlZjkyN2FiNGU3YTVmOWM5MjEzMmY0ZWQ0M2QxZDU0NmQwMzVlNmUzODk4NTQ5MmI2MzAyNzY5YzIwZmE4ZjQyNzZlM2NjYzI0NjZmMjE4MGZiMWIxOTA2ZjU0ODA2NjIxZWU3NWQ5NWZlMWVmNzZhYWU1ODI5NDhjYjUxYTcyZTM3Y2ZlNTE4OTZjZDg3NGYyNDJlMTExZDhlN2E1Y2YwMWU5NGVmMTlmN2E1ZmI1M2MwZWJkZjgwMzAxOTM4ZjNlNzFkZDE4MjVjZjUxNjgyYWJiOWYwMTM1ZDhiYTJiMzgwYlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIxODE5MDhkYVwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcGcxLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control':'max-age=0'
    }
    

    def __init__(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
            print(self.dir+'文件夹初始化完成')
        self.f = open(self.dir+'\\长沙二手房信息.csv',mode='a+',encoding='utf-8',newline='')

    def get_page(self):
        r=requests.get('https://cs.lianjia.com/ershoufang/pg1/',headers=self.headers).text
        page=re.findall(r'"totalPage":(.*?),',r)[0]
        return int(page)

    def get_house_info(self):
        count=1
        totalpage=self.get_page()
        print('totalpage: ', totalpage)
        for page in range(70,totalpage+1): #
            r=requests.get(self.start_url.format(page),headers=self.headers).text
            house_list=BeautifulSoup(r,'lxml').select('.sellListContent .info')
            for i in house_list:
                try:
                    # 翻页开始
                    house_url=i.select('.title a')[0]['href'] #获取要翻页的url
                    # house_name=i.select('.title a')[0].text.strip()
                    house_flood=i.select('.positionInfo a')[0].text
                    house_res=requests.get(house_url,headers=self.headers).text #请求翻页的url
                    house_info=BeautifulSoup(house_res,'lxml')
                    # build_year = house_info.select('.houseInfo')[0].text
                    # region = house_info.select('.areaName span a')[0].text
                    build_year = house_info.select('div.noHidden')[0].get_text(strip=True)
                    # region = house_info.select('div.areaName')[0].get_text(strip=True)
                    region = house_info.select('.areaName span a')[0].get_text(strip=True)
                    house_price=house_info.select('.total')[0].text+'万'
                    unit_price_value=house_info.select('.unitPriceValue')[0].text
                    house_intro_content=house_info.select('.introContent li')
                    intro_lst=[i.get_text('#',strip=1).split('#')[1] for i in house_intro_content]

                    house_label_list = []
                    try:
                        house_label = house_info.select('.tags')[0].text
                        for i in house_label:
                            i = i.strip()
                            if i != '':
                                house_label_list.append(i)
                        house_label = ''.join(house_label_list)
                    except:
                        house_label = ''

                    house_data=[count, house_flood, house_url, build_year, region, house_price,unit_price_value]+intro_lst+[house_label]
                    count+=1
                    yield house_data
                except Exception as e:
                    print('未获取到', e)
                    continue

    def save_excel(self):
        num=0
        excel_headers=['序号','所在小区','网站链接','总价', '建筑时间', '区域','单价','房屋户型','所在楼层', '建筑面积',
                       '户型结构', '套内面积', '建筑类型', '房屋朝向','建筑结构','装修情况','梯户比例', '供暖方式',
                       '配备电梯','挂牌时间', '交易权属', '上次交易', '房屋用途', '房屋年限', '产权所属', '抵押信息',
                       '房本备件', '标签']
        csv_file = csv.writer(self.f)
        csv_file.writerow(excel_headers)
        house_data=self.get_house_info()
        for item in house_data:
            csv_file.writerow(item)
            num+=1
            # print(item)
            print('第{}条数据写入完成'.format(num))
        print('写入完毕')
        
    def __del__(self):
        self.f.close()


if __name__=='__main__':
    lj=HousePrices()
    lj.save_excel()
