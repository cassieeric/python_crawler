import re
import pandas
from pyecharts import Line,Bar,Pie,TreeMap,Page,Overlap
import jieba
import numpy
import requests
from bs4 import BeautifulSoup
def read_data(filename):
    path=filename+'.csv'
    data=pandas.read_csv(path, engine='python', encoding='gb18030')
    print(data.describe())
    add, price, floor, orien, size, time, type=[],[],[],[],[],[],[]
    for i in zip(data['位置'],data['价格'],data['楼层'],data['朝向'],data['面积'],data['建造时间'],data['zone']):
        add.append(i[0])
        price.append(i[1])
        floor.append(i[2])
        orien.append(i[3])
        size.append(i[4])
        time.append(i[5])
        type.append(i[6])
    return add,price,floor,orien,size,time,type
def size_price(size,price):
    #page=Page()
    overlap=Overlap()
    #print(size)
    k=[]
    attr=['0-30','30-60','60-90','90-120','120-150','150及以上']
    for i in range(len(size)):
        size[i]=float(size[i][:-2])
    n1,n2,n3,n4,n5,n6=[],[],[],[],[],[]
    for i in range(len(size)):
        if size[i]<=30:
            #print(size[i])
            n1.append(price[i])
        #n1.append(size[i])
        if 30<size[i]<=60:
            n2.append(price[i])
        #n2.append(size[i])
        if 60< size[i] <= 90:
            n3.append(price[i])
        # n3.append(size[i])
        if 90<size[i]<=120:
            n4.append(price[i])
        #n4.append(size[i])
        if 120<size[i]<=150:
            n5.append(price[i])
        #n5.append(size[i])
        if 150<size[i]:
            n6.append(price[i])
    #n6.append(size[i])
    l=[len(n1),len(n2),len(n3),len(n4),len(n5),len(n6)]
    ave=[numpy.mean(n1),numpy.mean(n2),numpy.mean(n3),numpy.mean(n4),numpy.mean(n5),numpy.mean(n6)]
    bar = Bar("房屋面积_数量价位分布图", "", title_pos="left", width=1200, height=600)
    bar.add("", attr,ave, is_visualmap=True, visual_text_color='#fff',
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    overlap.add(bar)
    #page.add(bar)
    #bar.render('房屋面积_数量bar.html')
    line = Line('房屋面积_均价图', width=1200, height=600)
    line.add('数量', attr,l, is_stack=True, mark_point=['max', 'min'],line_color='lightblue',
             is_more_utils=True, visual_range=[0, 50])
    #page.add(line)
    overlap.add(line,is_add_yaxis=True,yaxis_index=1)
    #line.render('房屋面积_均价折线图.html')
    overlap.render('房屋面积_数量_均价折线图.html')
    pie=Pie('面积占比', title_pos='center', width=1200, height=600)
    pie.add("", attr, l, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render('面积占比Pie.html')
def get_quyu(url):
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'TY_SESSION_ID=4161343e-3927-4100-9533-5adb529f3e0c; lianjia_uuid=6ed7df6c-ebe5-4568-a5bf-2c21e546ca39; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1540622390; _smt_uid=5bd40836.2c7e9597; UM_distinctid=166b440154b306-06b5d47fe75004-47e1039-100200-166b440154d134; _jzqc=1; _jzqy=1.1540622391.1540622391.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91%E5%8C%97%E4%BA%AC.-; _jzqckmp=1; all-lj=3d8def84426f51ac8062bdea518a8717; _qzjc=1; CNZZDATA1254525948=667635047-1540617091-%7C1540622375; lianjia_ssid=f4217035-ac89-47ee-8799-142aaa2dedf2; _jzqa=1.4383878552266910700.1540622391.1540622391.1540624781.2; select_city=440300; CNZZDATA1255633284=1849769130-1540619624-%7C1540625025; CNZZDATA1255604082=1644370051-1540617480-%7C1540622360; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1540625223; _qzja=1.1426462676.1540622394159.1540622394159.1540625024479.1540625074932.1540625223403.0.0.0.17.2; _qzjb=1.1540625024479.3.0.0.0; _qzjto=17.2.0; _jzqb=1.4.10.1540624781.1; CNZZDATA1255849469=36534003-1540619700-%7C1540625224',
            'Host': 'sz.lianjia.com',
            'Referer': 'https://sz.lianjia.com/zufang/futianqu/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    soup=soup.find('dl',class_='dl-lst clear').find_all('a')
    url_list=[]
    result={}
    h=[]
    for s in soup[1:]:
        h.append(s.get('href').split('/')[2])
        u='https://sz.lianjia.com'+s.get('href')
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'TY_SESSION_ID=4161343e-3927-4100-9533-5adb529f3e0c; lianjia_uuid=6ed7df6c-ebe5-4568-a5bf-2c21e546ca39; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1540622390; _smt_uid=5bd40836.2c7e9597; UM_distinctid=166b440154b306-06b5d47fe75004-47e1039-100200-166b440154d134; _jzqc=1; _jzqy=1.1540622391.1540622391.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91%E5%8C%97%E4%BA%AC.-; _jzqckmp=1; all-lj=3d8def84426f51ac8062bdea518a8717; _qzjc=1; CNZZDATA1254525948=667635047-1540617091-%7C1540622375; lianjia_ssid=f4217035-ac89-47ee-8799-142aaa2dedf2; _jzqa=1.4383878552266910700.1540622391.1540622391.1540624781.2; select_city=440300; CNZZDATA1255633284=1849769130-1540619624-%7C1540625025; CNZZDATA1255604082=1644370051-1540617480-%7C1540622360; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1540625223; _qzja=1.1426462676.1540622394159.1540622394159.1540625024479.1540625074932.1540625223403.0.0.0.17.2; _qzjb=1.1540625024479.3.0.0.0; _qzjto=17.2.0; _jzqb=1.4.10.1540624781.1; CNZZDATA1255849469=36534003-1540619700-%7C1540625224',
            'Host': 'sz.lianjia.com',
            'Referer': 'https://sz.lianjia.com/zufang/futianqu/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        html = requests.get(u, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        soup = soup.find('div', class_='option-list sub-option-list').find_all('a')
        name=[]
        for so in soup[1:]:
            name.append(so.text)
        result[s.get('href').split('/')[2]]=name
    #print(result)
    #print(h)
    return h,result
def floor_price(floor,price):
    attr=['中','低','高']
    for i in range(len(floor)):
        floor[i]=floor[i][0]
    n1, n2, n3 = [], [], []
    for i in range(len(floor)):
        if floor[i]==attr[0]:
            # print(size[i])
            n1.append(price[i])
        # n1.append(size[i])
        if floor[i]==attr[1]:
            n2.append(price[i])
        # n2.append(size[i])
        if floor[i]==attr[2]:
            n3.append(price[i])
    l = [len(n1), len(n2), len(n3)]
    ave = [numpy.mean(n1), numpy.mean(n2), numpy.mean(n3)]
    bar = Bar("楼层_数量价位分布图", "", title_pos="left", width=1200, height=600)
    bar.add("", attr, ave, is_visualmap=True, visual_text_color='#fff',
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    overlap.add(bar)
    line = Line('楼层_数量图', width=1200, height=600)
    line.add('数量', attr, l, is_stack=True, mark_point=['max', 'min'], line_color='lightblue',
             is_more_utils=True, visual_range=[0, 50])
    overlap.add(line, is_add_yaxis=True, yaxis_index=1)
    overlap.render('房屋楼层_数量_均价折线图.html')
    pie = Pie('楼层占比', title_pos='center', width=1200, height=600)
    pie.add("", attr, l, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render('楼层占比Pie.html')
    print(floor)
def Longgang(longgang,price,add):
    overlap=Overlap()
    print(longgang)
    attr=['布吉关', '布吉大芬', '布吉水径', '坂田', '布吉街', '布吉南岭', '丹竹头', '大运新城', '横岗', '龙岗双龙', '龙岗中心城', '龙岗宝荷', '坪地', '平湖']
    n1, n2, n3, n4, n5, n6,n7, n8, n9, n10, n11, n12,n13,n14 = [], [], [], [], [], [],[], [], [], [], [], [],[],[]
    for i in range(len(add)):
        if add[i] == longgang[0]:
            n1.append(price[i])
        if add[i] == longgang[1]:
            n2.append(price[i])
        if add[i] == longgang[2]:
            n3.append(price[i])
        if add[i] == longgang[3]:
            n4.append(price[i])
        if add[i] == longgang[4]:
            n5.append(price[i])
        if add[i] == longgang[5]:
            n6.append(price[i])
        if add[i] == longgang[6]:
            n7.append(price[i])
        if add[i] == longgang[7]:
            n8.append(price[i])
        if add[i] == longgang[8]:
            n9.append(price[i])
        if add[i] == longgang[9]:
            n10.append(price[i])
        if add[i] == longgang[10]:
            n11.append(price[i])
        if add[i] == longgang[11]:
            n12.append(price[i])
        if add[i] == longgang[12]:
            n13.append(price[i])
        if add[i] == longgang[13]:
            n14.append(price[i])
    l = [len(n1), len(n2), len(n3), len(n4), len(n5), len(n6), len(n7),
         len(n8), len(n9), len(n10),len(n11),len(n12),len(n13),len(n14)]
    ave = [round(numpy.mean(n1), 2), round(numpy.mean(n2), 2), round(numpy.mean(n3), 2),
           round(numpy.mean(n4), 2), round(numpy.mean(n5), 2), round(numpy.mean(n6), 2),
           round(numpy.mean(n7), 2), round(numpy.mean(n8), 2), round(numpy.mean(n9), 2),
           round(numpy.mean(n10), 2),round(numpy.mean(n11), 2), round(numpy.mean(n12), 2), round(numpy.mean(n13), 2),round(numpy.mean(n14), 2)]
    bar = Bar("龙岗区房屋数量_均价分布图", "", title_pos="left", width=1200, height=600)
    bar.add("", attr, ave, is_visualmap=True, visual_text_color='#fff',
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    overlap.add(bar)
    line = Line('龙岗区房屋数量_均价图', width=1200, height=600)
    line.add('数量', attr, l, is_stack=True, mark_point=['max', 'min'], line_color='lightblue',
             is_more_utils=True, visual_range=[0, 50])
    overlap.add(line, is_add_yaxis=True, yaxis_index=1)
    overlap.render('龙岗区房屋数量_均价折线图.html')
    pie = Pie('龙岗区房屋数量面积占比', title_pos='center', width=1200, height=600)
    pie.add("", attr, l, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render('龙岗区房屋数量占比Pie.html')
def add_price(add,price):
    overlap=Overlap()
    name,result=get_quyu('https://sz.lianjia.com/zufang/')
    print(result)
    for i in range(len(add)):
        if '租房'in add[i]:
            add[i] = add[i][:-2]
    attr=['罗湖区','福田区','南山区','盐田区','宝安区','龙岗区','龙华区','光明新区','坪山区','大鹏新区']
    luohu,futian,nanshan,yantian,baoan,longgang,longhua,guangmingxinqu,pingshan,dapengxinqu=[],[],[],[],[],[],[],[],[],[]
    for i in range(len(add)):
        if add[i] in result['luohuqu']:
            luohu.append(price[i])
        if add[i] in result['futianqu']:
            futian.append(price[i])
        if add[i] in result['nanshanqu']:
            nanshan.append(price[i])
        if add[i] in result['yantianqu']:
            yantian.append(price[i])
        if add[i] in result['baoanqu']:
            baoan.append(price[i])
        if add[i] in result['longgangqu']:
            longgang.append(price[i])
        if add[i] in result['longhuaqu']:
            longhua.append(price[i])
        if add[i] in result['guangmingxinqu']:
            guangmingxinqu.append(price[i])
        if add[i] in result['pingshanqu']:
            pingshan.append(price[i])
        if add[i] in result['dapengxinqu']:
            dapengxinqu.append(price[i])
    l = [len(luohu),len(futian),len(nanshan),len(yantian),len(baoan),len(longgang),len(longhua),len(guangmingxinqu),len(pingshan),len(dapengxinqu)]
    ave = [round(numpy.mean(luohu),2), round(numpy.mean(futian),2), round(numpy.mean(nanshan),2), round( numpy.mean(yantian),2), round( numpy.mean(baoan),2), round( numpy.mean(longgang),2), round(numpy.mean(longhua), 2), round(numpy.mean(guangmingxinqu), 2), round(numpy.mean(pingshan),2), round( numpy.mean(dapengxinqu),2)]
    bar = Bar("深圳各区房屋数量_均价分布图", "", title_pos="left", width=1200, height=600)
    bar.add("", attr, ave, is_visualmap=True, visual_text_color='#fff',
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    overlap.add(bar)
    line = Line('各区房屋数量_均价图', width=1200, height=600)
    line.add('数量', attr, l, is_stack=True, mark_point=['max', 'min'], line_color='lightblue',
             is_more_utils=True, visual_range=[0, 50])
    overlap.add(line, is_add_yaxis=True, yaxis_index=1)
    overlap.render('深圳各区房屋数量_均价折线图.html')
    pie = Pie('各区房屋数量面积占比', title_pos='center', width=1200, height=600)
    pie.add("", attr, l, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render('各区房屋数量占比Pie.html')
    #Longgang(result['longgangqu'],price,add)
def orien_price(orien,price):
    print(orien)
    attr=['北','南']
    n,s=[],[]
    for i in range(len(orien)):
        if attr[0] in orien[i]:
            n.append(price[i])
        if attr[1] in orien[i]:
            s.append(price[i])
    print(len(n),len(s))
    ave=[round(numpy.mean(n),2),round(numpy.mean(s),2)]
    l=[len(n),len(s)]
    bar = Bar("朝向数量_均价分布图", "", title_pos="left", width=1200, height=600)
    bar.add("", attr, ave, is_visualmap=True, visual_text_color='#fff',
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    overlap.add(bar)
    line = Line('朝向数量_均价图', width=1200, height=600)
    line.add('数量', attr, l, is_stack=True, mark_point=['max', 'min'], line_color='lightblue',
             is_more_utils=True, visual_range=[0, 50])
    overlap.add(line, is_add_yaxis=True, yaxis_index=1)
    overlap.render('朝向数量_均价折线图.html')
    pie = Pie('朝向数量面积占比', title_pos='center', width=1200, height=600)
    pie.add("", attr, l, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render('朝向数量占比Pie.html')
def time_price(time,price):
    print(time)
    attr=['一年','两到三年','三到五年','五到十年','十年及以上']
    n1,n2,n3,n4,n5=[],[],[],[],[]
    for i in range(len(time)):
        try:
            time[i]=time[i][:4]
            if time[i]>='2018':#建房一年
                n1.append(price[i])
            elif '2018'>time[i]>='2016':#建房2~3年
                n2.append(price[i])
            elif '2016'>time[i]>='2014':#建房3~5年
                n3.append(price[i])
            elif '2014'>time[i]>='2009':#建房5~10年
                n4.append(price[i])
            elif '2009' > time[i]:  # 建房10年
                n5.append(price[i])
        except Exception as e:
            continue
    l = [len(n1), len(n2), len(n3), len(n4), len(n5)]
    ave = [numpy.mean(n1), numpy.mean(n2), numpy.mean(n3), numpy.mean(n4), numpy.mean(n5)]
    bar = Bar("房屋新旧程度_数量价位分布图", "", title_pos="left", width=1200, height=600)
    bar.add("", attr, ave, is_visualmap=True, visual_text_color='#fff',
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    overlap.add(bar)
    # page.add(bar)
    # bar.render('房屋面积_数量bar.html')
    line = Line('房屋新旧程度_均价图', width=1200, height=600)
    line.add('数量', attr, l, is_stack=True, mark_point=['max', 'min'], line_color='lightblue',
             is_more_utils=True, visual_range=[0, 50])
    # page.add(line)
    overlap.add(line, is_add_yaxis=True, yaxis_index=1)
    # line.render('房屋面积_均价折线图.html')
    overlap.render('房屋新旧程度_数量_均价折线图.html')
    pie = Pie('新旧占比', title_pos='center', width=1200, height=600)
    pie.add("", attr, l, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render('新旧占比Pie.html')




if __name__=='__main__':
    overlap = Overlap()
    filename='sz_lj'
    add, price, floor, orien, size, time, type=read_data(filename)
    #size_price(size,price)
    #floor_price(floor,price)
    #add_price(add,price)
    #orien_price(orien,price)
    #time_price(time, price)