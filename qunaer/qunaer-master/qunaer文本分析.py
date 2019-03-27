import pandas
import time
import jieba
from pyecharts import Geo,Bar,Map,Page
import echarts_china_cities_pypkg
import echarts_china_provinces_pypkg
import echarts_china_counties_pypkg
import echarts_countries_pypkg
import matplotlib
from bokeh.io import show,output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.palettes import Spectral6
import plotly.plotly
import plotly.graph_objs as go
import json
import matplotlib.pyplot as plt
import numpy
import requests
filename='qunaer.csv'
def read_data(filename):
    qunae=pandas.read_csv(filename,engine='python',encoding='utf-8',header=None)
    pro,city,name,level,price,num,hot,com=[],[],[],[],[],[],[],[]
    for i in zip(qunae[0],qunae[1],qunae[2],qunae[3],qunae[4],qunae[5],qunae[6],qunae[7]):
        pro.append(i[0])
        city.append(i[1])
        name.append(i[2])
        level.append(i[3])
        price.append(i[4])
        num.append(i[5])
        hot.append(i[6])
        com.append(i[7])
    return pro,city,name,level,price,num,hot,com
    #print(qunae)
def comment(com):
    print(len(com))
    df = pandas.DataFrame()
    pl = []
    stopword = ['的', '了', '是', '。', '，', ' ', '？', '！', '就', '\n', '：', '“', '”', '*', '=', '（', '）', '吗', '吧', '(',
                ')', '・', '[', ']', '、', '°', '？', '！', '.', '-', '｀', '；', ',', '《', '》']
    for i in range(len(com)):
        #print(i)
        try:
            cut_list = jieba.cut(com[i], cut_all=False)
            # print(type(cut_list))
            w = '/'.join(cut_list)
            w = w.split('/')
            for j in w:
                if not j in stopword:
                    pl.append(j)
        except AttributeError:
            print(AttributeError)
    print(pl)
    words = []
    for s in set(pl):
        if len(s) > 1:
            if pl.count(s) > 50:
                x = {}
                x['word'] = s.strip('\n')
                x['count'] = pl.count(s)
                print(x)
                df = df.append(x, ignore_index=True)
    print(df)
    df.to_csv('qunacom.csv', encoding='utf-8', index=False, mode='a', header=False)
    #print(df)
def sum_pro(pro,k):#每个省有多少个景点
    p=[]
    c=[]
    for i in set(pro):
        '''
        q={}
        q[i]=pro.count(i)
        p.append(q)'''
        p.append(i)
        c.append(pro.count(i))
    map= Map('各省'+k+'A景点分布', width=1200, height=600)
    map.add("", p,c, is_visualmap=True, visual_range=[min(c), max(c)],
              visual_text_color='#000', is_map_symbol_show=True, is_label_show=True)
    map.render( '各省'+k+'A景点分布.html')
    print(p)
def huati(name,num,k):#看各级的销量
    kk=[]
    for i in range(len(name)):
        if not numpy.isnan(num[i]):
            q = []
            q.append(name[i])
            q.append(num[i])
            # q[name[i]]=hot[i]
            kk.append(q)
    hh=sorted(kk,key=lambda i:i[1],reverse=True)
    page=Page()
    att,val=[],[]
    for i in hh[:20]:
        att.append(i[0])
        val.append(i[1])
    bar1 = Bar("", k+"A景区销量排行", title_pos="center", width=1200, height=600)
    bar1.add("",att,val, is_visualmap=True, visual_text_color='#fff', mark_point=["average"],
            mark_line=["average"],
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    page.add_chart(bar1)
    att, val = [], []
    for i in hh[-20:]:
        att.append(i[0])
        val.append(i[1])
    bar2 = Bar("", k+"A景区销量排行", title_pos="center", width=1200, height=600)
    bar2.add("", att, val, is_visualmap=True, visual_text_color='#fff', mark_point=["average"],
             mark_line=["average"],
             is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    page.add_chart(bar2)
    page.render(k+"A景区销量bar.html")
def hottt(fivhot,fouhot,thrhot):#各级景区人气
    fiv, fou, th = [], [], []
    atts = ['0', '0.7', '0.8', '0.9', '1']
    for i in fivhot:
        fiv.append(round(i, 1))
    for i in fouhot:
        fou.append(round(i, 1))
    for i in thrhot:
        th.append(round(i, 1))
    levels = ['5A', '4A', '3A']
    data = {}
    data['att'] = atts
    data['5A'], data['4A'], data['3A'] = [], [], []
    for i in range(len(atts)):
        data['5A'].append(round(fiv.count(float(atts[i])) / len(fiv) * 100, 3))
        data['4A'].append(round(fou.count(float(atts[i])) / len(fou) * 100, 3))
        data['3A'].append(round(th.count(float(atts[i])) / len(th) * 100, 3))
    print(data)
    output_file("bars.html")  # 输出文件名
    x = [(att, level) for att in atts for level in levels]
    counts = sum(zip(data['5A'], data['4A'], data['3A']), ())
    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=250, title="各等级景区人气值占比",
               toolbar_location=None, tools="")
    p.vbar(x='x', top='counts', width=0.9, source=source)
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    show(p)
def money(name,price,kk):#各级景区价格
    page=Page()
    k = []
    for i in range(len(name)):
        if not numpy.isnan(price[i]):
            q = []
            q.append(name[i])
            q.append(price[i])
            # q[name[i]]=hot[i]
            k.append(q)
    hh = sorted(k, key=lambda i: i[1], reverse=True)
    print(hh)
    att, val = [], []
    for i in hh[:20]:
        att.append(i[0])
        val.append(i[1])
    bar1 = Bar("", kk+"A景区价格排行", title_pos="center", width=1200, height=600)
    bar1.add("", att, val, is_visualmap=True, visual_text_color='#fff', mark_point=["average"],
            mark_line=["average"],
            is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    page.add_chart(bar1)
    att, val = [], []
    for i in hh[-20:]:
        att.append(i[0])
        val.append(i[1])
    bar2 = Bar("", kk+"A景区价格排行", title_pos="center", width=1200, height=600)
    bar2.add("", att, val, is_visualmap=True, visual_text_color='#fff', mark_point=["average"],
             mark_line=["average"],
             is_more_utils=True, is_label_show=True, is_datazoom_show=True, xaxis_rotate=45)
    page.add_chart(bar2)
    page.render(kk+"A景区价格bar.html")
def trans(city,name,pro,level):#高德地图可视化

    for i in range(len(name)):
        x = pandas.DataFrame()
        t={}
        add = name[i]
        chengshi=city[i]
        parameters = { 'address': add, 'key': '','city':chengshi }
       html = requests.get('https://restapi.amap.com/v3/geocode/geo', params=parameters).json()
        print(html)
        try:
            t['jingwei'] = html['geocodes'][0]['location']
        except IndexError:
            t['jingwei']='0,0'
        finally:
            t['n'] = name[i]
            t['level']=level[i]
            t['pro']=pro[i]
            t['city']=city[i]
            x = x.append(t, ignore_index=True)
            x.to_csv('55543.csv', encoding='utf-8', index=False, mode='a', header=False)
def box(q,w,e,l):#箱型图
    a = go.Box(y=q, name='5A景区')
    b = go.Box(y=w, name='4A景区')
    c = go.Box(y=e, name='3A景区')
    g = go.Box(y=l, name='所有景区')
    data = [a, b, c,g]
    layout = go.Layout(legend=dict(font=dict(size=16)), orientation=270)
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(data)
def onebox(q,w,e,l):
    data = [q, w, e, l]
    a,b,c,d=[],[],[],[]
    for i in range(len(q)):
        if not numpy.isnan(q[i])and q[i]<500:
            a.append(q[i])
    for i in range(len(w)):
        if not numpy.isnan(w[i])and int(w[i])<500:
            b.append(w[i])
    for i in range(len(e)):
        if not numpy.isnan(e[i])and int(e[i])<500:
            c.append(e[i])
    for i in range(len(l)):
        if not numpy.isnan(l[i])and int(l[i])<500:
            d.append(l[i])
    print(data)
    # draw
    plt.boxplot([a, b, c, d],labels=['5','4','3','all scenic'],notch=True)
    fig = plt.figure()  # 创建画布
    ax = plt.subplot()  # 创建作图区域
    plt.show()
def twobox(q,w,e,l):
    data = [q, w, e, l]
    a,b,c,d=[],[],[],[]
    for i in range(len(q)):
        if not numpy.isnan(q[i]):
            a.append(q[i])
    for i in range(len(w)):
        if not numpy.isnan(w[i]):
            b.append(w[i])
    for i in range(len(e)):
        if not numpy.isnan(e[i]):
            c.append(e[i])
    for i in range(len(l)):
        if not numpy.isnan(l[i]):
            d.append(l[i])
    print(data)
    plt.boxplot([a, b, c, d],labels=['5','4','3','all scenic'],notch=True)
    fig = plt.figure()  # 创建画布
    ax = plt.subplot()  # 创建作图区域
    plt.show()
def fivea(filename,k):
    qunae = pandas.read_csv(filename, engine='python', encoding='utf-8', header=None)
    pro, city, name, level, price, num, hot, com = [], [], [], [], [], [], [], []
    for i in zip(qunae[0], qunae[1], qunae[2], qunae[3], qunae[4], qunae[5], qunae[6], qunae[7]):
        if i[3]==5 :
            pro.append(i[0])
            city.append(i[1])
            name.append(i[2])
            level.append(i[3])
            price.append(i[4])
            num.append(i[5])
            hot.append(i[6])
            com.append(i[7])
    #print(hot)
    #trans(city,name,pro,level)
    #huati(name,num,k)
    #money(name,price,k)
    #sum_pro(pro,k)
    #print(level)
    return price, num,hot
def foura(filename,k):
    qunae = pandas.read_csv(filename, engine='python', encoding='utf-8', header=None)
    pro, city, name, level, price, num, hot, com = [], [], [], [], [], [], [], []
    for i in zip(qunae[0], qunae[1], qunae[2], qunae[3], qunae[4], qunae[5], qunae[6], qunae[7]):
        if i[3]==4:
            pro.append(i[0])
            city.append(i[1])
            name.append(i[2])
            level.append(i[3])
            price.append(i[4])
            num.append(i[5])
            hot.append(i[6])
            com.append(i[7])
    #print(hot)
    #huati(name,num,k)
    #money(name,price,k)
    #sum_pro(pro,k)
    #trans(city, name, pro, level)
    return price, num, hot
    #print(level)
def threea(filename,k):
    qunae = pandas.read_csv(filename, engine='python', encoding='utf-8', header=None)
    pro, city, name, level, price, num, hot, com = [], [], [], [], [], [], [], []
    for i in zip(qunae[0], qunae[1], qunae[2], qunae[3], qunae[4], qunae[5], qunae[6], qunae[7]):
        if i[3]==3:
            pro.append(i[0])
            city.append(i[1])
            name.append(i[2])
            level.append(i[3])
            price.append(i[4])
            num.append(i[5])
            hot.append(i[6])
            com.append(i[7])
    #print(hot)
    #huati(name,num,k)
    #money(name,price,k)
    #sum_pro(pro,k)
    #trans(city, name, pro, level)
    return price, num, hot
    #print(level)
pro,city,name,level,price,num,hot,com=read_data(filename)
comment(com)
#sum_pro(pro)
#fivprice, fivnum,fivhot=fivea(filename,'5')
#fouprice, founum,fouhot=foura(filename,'4')
#thrprice, thrnum,thrhot=threea(filename,'3')
#hottt(fivhot,fouhot,thrhot)
#box(fivprice,fouprice,thrprice,price)
#box(fivnum,founum,thrnum,num)
#box(fivhot,fouhot,thrhot,hot)
#onebox(fivprice,fouprice,thrprice,price)
#twobox(fivnum,founum,thrnum,num)
#onebox(fivhot,fouhot,thrhot,hot)
#trans(city,name)
