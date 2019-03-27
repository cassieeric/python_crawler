import pandas
import time
import jieba
from snownlp import SnowNLP
from datetime import datetime
import matplotlib
from bokeh.io import show,output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.palettes import Spectral6
import plotly.plotly
import plotly.graph_objs as go
import numpy as np
import networkx as nx
import seaborn
import matplotlib.pyplot as pyl
import numpy
def read_data(filepath):
    run=pandas.read_csv(filepath,engine='python',encoding='utf-8',header=None)
    run.fillna('NNN')
    #print(run[11])
    #按行读取
    com,week,day,hour,floor,zan,sex,name,level,reply=[],[],[],[],[],[],[],[],[],[]
    '''
    for index in run.index:
        com.append(run.loc[index][0])
        shijian.append(run.loc[index][1])
        floor.append(run.loc[index][2])
        zan.append(run.loc[index][3])
        sex.append(run.loc[index][4])
        name.append(run.loc[index][5])
        level.append(run.loc[index][6])
        reply.append(run.loc[index][7])
    for s in range(len(shijian)):
        try:
            w = time.localtime(shijian[s])
            day.append(time.strftime("%Y-%m-%d ", w))
            hour.append(time.strftime("%H:%M:%S", w))
        except Exception as e:
            day.append('')
            hour.append('')'''
    for i in zip(run[11],run[13],run[14],run[15],run[16],run[17],run[18],run[19],run[20],run[21]):
        #print(i)
        com.append(i[0])
        floor.append(i[1])
        zan.append(i[2])
        sex.append(i[3])
        name.append(i[4])
        level.append(i[5])
        reply.append(i[6])
        week.append(i[7])
        hour.append(i[9])
        day.append(i[8])
    return com,day,hour,floor,zan,sex,name,level,reply,week
#日评论时间
def ana_hour(hour):
    h,k=[],[]
    for i in range(len(hour)):
        if isinstance(hour[i],str):
            h.append(hour[i][:2])
    for i in sorted(set(h)):
        k.append(h.count(i))
    print(k)
    output_file('hour_line.html')
    p = figure(plot_width=400,title='各小时评论数', plot_height=400)
    p.line(sorted(set(h)), k, line_width=2)
    p.circle(sorted(set(h)), k, fill_color="white", size=8)
    show(p)
#周评论
def ana_week(week):
    weeks=['星期天','星期一','星期二','星期三','星期四','星期五','星期六']
    output_file('week_bar.html')
    count=[]
    for i in sorted(set(week)):
        if not numpy.isnan(i):
            count.append(week.count(i))
    source = ColumnDataSource(data=dict(weeks=weeks, counts=count,color=['orange','yellowgreen','pink','darksalmon','lightgreen','paleturquoise','lightsteelblue']))
    p=figure(x_range=weeks, y_range=(0,4000), plot_height=250, title="Week Counts",
           toolbar_location=None, tools="")
    p.vbar(x='weeks', top='counts', color='color',width=0.9, legend="Week", source=source)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_right"
    show(p)
def write_data(filepath):
    df=pandas.DataFrame()
    run = pandas.read_csv(filepath, engine='python', encoding='utf-8', header=None)
    #按行读取
    com,shijian,floor,zan,sex,name,level,reply=[],[],[],[],[],[],[],[]
    for i in zip(run[0],run[1],run[2],run[3],run[4],run[5],run[6],run[7]):
        r={}
        r[0]=i[0]
        r[1] = i[1]
        r[2] = i[2]
        r[3] = i[3]
        r[4] = i[4]
        r[5]=i[5]
        r[6] = i[6]
        r[7] = i[7]
        try:
            w = time.localtime(i[1])
            r[8] = time.strftime("%w", w)
            r[9] = time.strftime("%Y-%m-%d ", w)
            r[10] = time.strftime("%H:%M:%S", w)
        except Exception as e:
            r[8]=''
            r[9] = ''
            r[10] = ''
        df=df.append(r,ignore_index=True)
    df.to_csv('running.csv', index=False, mode='a', header=False,encoding='utf-8')
#话题度排行
def hot(com):
    #print(com)
    output_file('各成员话题度.html')
    jzg=['金钟国','钟国','能力者']
    gary=['gary','狗哥']
    haha=['haha','HAHA','哈哈']
    qsm=['全昭敏','全妹','全昭body']
    lsz=['梁世赞','世赞','小不点']
    name=['池石镇','刘在石','宋智孝','李光洙','金钟国','gary','haha','全昭敏','梁世赞']
    csz,lzs,szx,lgz,jzg,gary,haha,qsm,lsz=[],[],[],[],[],[],[],[],[]
    for i in com:
        if  '池石镇'in i or'石镇' in i or'鼻子'in i:
            csz.append(i)
        if '刘在石'in i or '在石' in i or '大神' in i or '蚂蚱' in i:
            lzs.append(i)
        if '宋智孝' in i or '智孝'in i or '懵智'in i or '美懵'in i:
            szx.append(i)
        if '李光洙'in i or '光洙'in i or '一筐猪'in i:
            lgz.append(i)
        if '金钟国'in i or '钟国'in i or '能力者'in i:
            jzg.append(i)
        if 'gary'in i or'狗哥'in i:
            gary.append(i)
        if 'haha'in i or 'HAHA'in i or '哈哈'in i:
            haha.append(i)
        if '全昭敏'in i or '全妹'in i or'全昭body'in i:
            qsm.append(i)
        if '梁世赞'in i or'世赞'in i or'小不点'in i:
            lsz.append(i)
    count=[len(csz),len(lzs),len(szx),len(lgz),len(jzg),len(gary),len(haha),len(qsm),len(lsz)]
    print(count)
    source = ColumnDataSource(data=dict(name=name, counts=count,
                                        color=['orange', 'yellowgreen', 'pink', 'darksalmon', 'lightgreen',
                                               'paleturquoise', 'lightsteelblue','hotpink','yellow']))
    p = figure(x_range=name, y_range=(0, 600), plot_height=250, title="话题度排行",
               toolbar_location=None, tools="")
    p.vbar(x='name', top='counts', color='color', width=0.9, source=source)
    p.legend.orientation = "horizontal"
    #p.legend.location = "top_right"
    show(p)
#评论字数和赞的关系
def com_zan(com,zan):
    #print(len(zan))
    #print(len(com))
    q,w,e,r,t=[],[],[],[],[]
    for i in range(len(com)):
        if len(com[i])<10:
            q.append(zan[i])
        if 10<=len(com[i])<50:
            w.append(zan[i])
        if 50<=len(com[i])<100:
            e.append(zan[i])
        if 100<=len(com[i]):
            r.append(zan[i])
    a=go.Box(y=q,name='0-10个字')
    b=go.Box(y=w,name='10-50个字')
    c=go.Box(y=e,name='50-100个字')
    d=go.Box(y=r,name='100以上个字')
    e=go.Box(y=zan,name='所有评论')
    data=[a,b,e,c,d]
    layout = go.Layout(legend=dict(font=dict(size=16)),orientation=270)
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(data)
    print(e)
#词云图
def comment(com):
    df=pandas.DataFrame()
    pl=[]
    stopword=['的','了','是','。','，',' ','？','！','就','\n','：','“','”','*','=','（','）','吗','吧','(',')','・','[',']','、','°','？','！','.','-','｀','；',',','《','》']
    for i in range(len(com)):
        cut_list=jieba.cut(com[i],cut_all=False)
        w='/'.join(cut_list)
        w=w.split('/')
        for j in w:
            if not j in stopword:
                pl.append(j)
    words=[]
    for s in set(pl):
        if len(s)>1:
            if pl.count(s) > 50:
                x = {}
                x['word']=s.strip('\n')
                x['count']=pl.count(s)
                print(x)
                df=df.append(x,ignore_index=True)
                #print(df)
    print(df)
    df.to_csv('1.csv',encoding='utf-8',index=False, mode='a', header=False)
    print(df)
#情感分析
def snownlp(com):
    q=[]
    for i in com:
        s=SnowNLP(i)
        q.append(round(s.sentiments,1))
    print(q)
    emotion=[]
    count=[]
    for i in sorted(set(q)):
        emotion.append(str(i))
        count.append(q.count(i))
    print(count)
    print(emotion)
    print(type(emotion))
    #count=[596, 481, 559, 566, 490, 617, 528, 601, 581, 809, 1685]
    #emotion=['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
    output_file('评论情感分析.html')
    source = ColumnDataSource(data=dict(emotion=emotion, counts=count))
    p = figure(x_range=emotion, y_range=(0, 2000), plot_height=250, title="评论情感分析",
               toolbar_location=None, tools="")
    p.vbar(x='emotion', top='counts', width=0.9, source=source)
    p.legend.orientation = "horizontal"
    show(p)
#成员的相关系数矩阵
def network_edg_csv(com):
    df=pandas.DataFrame(columns=['池石镇','刘在石','宋智孝','李光洙','金钟国','gary','haha','全昭敏','梁世赞'],index=['池石镇','刘在石','宋智孝','李光洙','金钟国','gary','haha','全昭敏','梁世赞'])
    df.loc[:,:]=0.0
    for i in com:
        if  (i in '池石镇'in i or'石镇' in i or'鼻子'in i):
            df['池石镇']['池石镇'] = df['池石镇']['池石镇'] + 1
            if('刘在石'in i or '在石' in i or '大神' in i or '蚂蚱' in i):
                df['池石镇']['刘在石'] = df['池石镇']['刘在石'] + 1
                df['刘在石']['池石镇'] = df['刘在石']['池石镇'] + 1
            if '宋智孝' in i or '智孝' in i or '懵智' in i or '美懵' in i:
                df['池石镇']['宋智孝']=df['池石镇']['宋智孝']+1
                df['宋智孝']['池石镇'] = df['宋智孝']['池石镇'] + 1
            if '李光洙' in i or '光洙' in i or '一筐猪' in i:
                df['池石镇']['李光洙'] = df['池石镇']['李光洙'] + 1
                df['李光洙']['池石镇'] = df['李光洙']['池石镇'] + 1
            if '金钟国' in i or '钟国' in i or '能力者' in i:
                df['池石镇']['金钟国'] = df['池石镇']['金钟国'] + 1
                df['金钟国']['池石镇'] = df['金钟国']['池石镇'] + 1
            if 'gary' in i or '狗哥' in i:
                df['池石镇']['gary'] = df['池石镇']['gary'] + 1
                df['gary']['池石镇'] = df['gary']['池石镇'] + 1
            if 'haha' in i or 'HAHA' in i or '哈哈' in i:
                df['池石镇']['haha'] = df['池石镇']['haha'] + 1
                df['haha']['池石镇'] = df['haha']['池石镇'] +1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['池石镇']['全昭敏'] = df['池石镇']['全昭敏'] + 1
                df['全昭敏']['池石镇'] = df['全昭敏']['池石镇'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['池石镇']['梁世赞'] = df['池石镇']['梁世赞'] + 1
                df['梁世赞']['池石镇'] = df['梁世赞']['池石镇'] + 1
        if '刘在石'in i or '在石' in i or '大神' in i or '蚂蚱' in i:
            df['刘在石']['刘在石'] = df['刘在石']['刘在石'] + 1
            if '宋智孝' in i or '智孝' in i or '懵智' in i or '美懵' in i:
                df['刘在石']['宋智孝']=df['刘在石']['宋智孝']+1
                df['宋智孝']['刘在石'] = df['宋智孝']['刘在石'] + 1
            if '李光洙' in i or '光洙' in i or '一筐猪' in i:
                df['刘在石']['李光洙'] = df['刘在石']['李光洙'] + 1
                df['李光洙']['刘在石'] = df['李光洙']['刘在石'] + 1
            if '金钟国' in i or '钟国' in i or '能力者' in i:
                df['刘在石']['金钟国'] = df['刘在石']['金钟国'] + 1
                df['金钟国']['刘在石'] = df['金钟国']['刘在石'] + 1
            if 'gary' in i or '狗哥' in i:
                df['刘在石']['gary'] = df['刘在石']['gary'] + 1
                df['gary']['刘在石'] = df['gary']['刘在石'] + 1
            if 'haha' in i or 'HAHA' in i or '哈哈' in i:
                df['刘在石']['haha'] = df['刘在石']['haha'] + 1
                df['haha']['刘在石'] = df['haha']['刘在石'] +1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['刘在石']['全昭敏'] = df['刘在石']['全昭敏'] + 1
                df['全昭敏']['刘在石'] = df['全昭敏']['刘在石'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['刘在石']['梁世赞'] = df['刘在石']['梁世赞'] + 1
                df['梁世赞']['刘在石'] = df['梁世赞']['刘在石'] + 1
        if '宋智孝' in i or '智孝'in i or '懵智'in i or '美懵'in i:
            df['宋智孝']['宋智孝'] = df['宋智孝']['宋智孝'] + 1
            if '李光洙' in i or '光洙' in i or '一筐猪' in i:
                df['宋智孝']['李光洙'] = df['宋智孝']['李光洙'] + 1
                df['李光洙']['宋智孝'] = df['李光洙']['宋智孝'] + 1
            if '金钟国' in i or '钟国' in i or '能力者' in i:
                df['宋智孝']['金钟国'] = df['宋智孝']['金钟国'] + 1
                df['金钟国']['宋智孝'] = df['金钟国']['宋智孝'] + 1
            if 'gary' in i or '狗哥' in i:
                df['宋智孝']['gary'] = df['宋智孝']['gary'] + 1
                df['gary']['宋智孝'] = df['gary']['宋智孝'] + 1
            if 'haha' in i or 'HAHA' in i or '哈哈' in i:
                df['宋智孝']['haha'] = df['宋智孝']['haha'] + 1
                df['haha']['宋智孝'] = df['haha']['宋智孝'] +1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['宋智孝']['全昭敏'] = df['宋智孝']['全昭敏'] + 1
                df['全昭敏']['宋智孝'] = df['全昭敏']['宋智孝'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['宋智孝']['梁世赞'] = df['宋智孝']['梁世赞'] + 1
                df['梁世赞']['宋智孝'] = df['梁世赞']['宋智孝'] + 1
        if '李光洙'in i or '光洙'in i or '一筐猪'in i:
            df['李光洙']['李光洙'] = df['李光洙']['李光洙'] + 1
            if '金钟国' in i or '钟国' in i or '能力者' in i:
                df['李光洙']['金钟国'] = df['李光洙']['金钟国'] + 1
                df['金钟国']['李光洙'] = df['金钟国']['李光洙'] + 1
            if 'gary' in i or '狗哥' in i:
                df['李光洙']['gary'] = df['李光洙']['gary'] + 1
                df['gary']['李光洙'] = df['gary']['李光洙'] + 1
            if 'haha' in i or 'HAHA' in i or '哈哈' in i:
                df['李光洙']['haha'] = df['李光洙']['haha'] + 1
                df['haha']['李光洙'] = df['haha']['李光洙'] +1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['李光洙']['全昭敏'] = df['李光洙']['全昭敏'] + 1
                df['全昭敏']['李光洙'] = df['全昭敏']['李光洙'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['李光洙']['梁世赞'] = df['李光洙']['梁世赞'] + 1
                df['梁世赞']['李光洙'] = df['梁世赞']['李光洙'] + 1
        if '金钟国'in i or '钟国'in i or '能力者'in i:
            df['金钟国']['金钟国'] = df['金钟国']['金钟国'] + 1
            if 'gary' in i or '狗哥' in i:
                df['金钟国']['gary'] = df['金钟国']['gary'] + 1
                df['gary']['金钟国'] = df['gary']['金钟国'] + 1
            if 'haha' in i or 'HAHA' in i or '哈哈' in i:
                df['金钟国']['haha'] = df['金钟国']['haha'] + 1
                df['haha']['金钟国'] = df['haha']['金钟国'] +1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['金钟国']['全昭敏'] = df['金钟国']['全昭敏'] + 1
                df['全昭敏']['金钟国'] = df['全昭敏']['金钟国'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['金钟国']['梁世赞'] = df['金钟国']['梁世赞'] + 1
                df['梁世赞']['金钟国'] = df['梁世赞']['金钟国'] + 1
        if 'gary'in i or'狗哥'in i:
            df['gary']['gary'] = df['gary']['gary'] + 1
            if 'haha' in i or 'HAHA' in i or '哈哈' in i:
                df['gary']['haha'] = df['gary']['haha'] + 1
                df['haha']['gary'] = df['haha']['gary'] +1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['gary']['全昭敏'] = df['gary']['全昭敏'] + 1
                df['全昭敏']['gary'] = df['全昭敏']['gary'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['gary']['梁世赞'] = df['gary']['梁世赞'] + 1
                df['梁世赞']['gary'] = df['梁世赞']['gary'] + 1
        if 'haha'in i or 'HAHA'in i or '哈哈'in i:
            df['haha']['haha'] = df['haha']['haha'] + 1
            if '全昭敏' in i or '全妹' in i or '全昭body' in i:
                df['haha']['全昭敏'] = df['haha']['全昭敏'] + 1
                df['全昭敏']['haha'] = df['全昭敏']['haha'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['haha']['梁世赞'] = df['haha']['梁世赞'] + 1
                df['梁世赞']['haha'] = df['梁世赞']['haha'] + 1
        if '全昭敏'in i or '全妹'in i or'全昭body'in i:
            df['全昭敏']['全昭敏'] = df['全昭敏']['全昭敏'] + 1
            if '梁世赞' in i or '世赞' in i or '小不点' in i:
                df['全昭敏']['梁世赞'] = df['全昭敏']['梁世赞'] + 1
                df['梁世赞']['全昭敏'] = df['梁世赞']['全昭敏'] + 1
        if '梁世赞'in i or'世赞'in i or'小不点'in i:
            df['梁世赞']['梁世赞'] = df['梁世赞']['梁世赞'] + 1
    print(df)
    for i in df.index:
        s=df.loc[i][i]
        #print(s)
        for j in ['池石镇','刘在石','宋智孝','李光洙','金钟国','gary','haha','全昭敏','梁世赞']:
            #print(df.loc[i][j]/s*100)
            df.loc[i][j]=df.loc[i][j]/s*100
    print(df)
    #print(df.corr())
    print(df['池石镇']['李光洙'])
    fig=pyl.figure()
    names=['chishizhen','liuzaishi','songzhixiao','liguangzhu','jinzgongguo','gary','haha','quanshaomin','liangshizan']
    ax=fig.add_subplot(figsize=(100, 100)) # 图片大小为20*20  
    ax=seaborn.heatmap(df, cmap='rainbow',linewidths = 0.05, vmax = 100,vmin = 0,annot = True, annot_kws = {
        'size': 6, 'weight': 'bold'})
    # 热力图参数设置（相关系数矩阵，颜色，每个值间隔等）   
    pyl.xticks(np.arange(9) + 0.5, names,rotation=-90)# 横坐标标注点  
    pyl.yticks(np.arange(9) + 0.5, names,rotation=360)
    ax.set_title('Characteristic correlation')  # 标题设置
    #ax.set_xticklabels(ax.get_xticklabels(), rotation=-90)
    #pyl.savefig('cluster.tif', dpi=300)
    pyl.show()
'''
    result={}
    dc=pandas.DataFrame(columns=['one','two','count'])
    for i in df.index:
        result['one']=i
        for j in ['池石镇','刘在石','宋智孝','李光洙','金钟国','gary','haha','全昭敏','梁世赞']:
            if not i==j:
                result['two'] = j
                result['count'] = df[i][j]
                dc = dc.append(result, ignore_index=True)
    dc.to_csv('run_edge.csv',encoding='utf-8')
    large=()'''
#print(df)
#网络分析
def network():
    data=pandas.read_csv('run_edge.csv',encoding='utf-8',engine='python')
    #print(data)
    G = nx.Graph()
    pyl.figure(figsize=(20,20))
    for i in data.index:
        G.add_weighted_edges_from([(data.loc[i]['one'],data.loc[i]['two'],data.loc[i]['count'])])
    n=nx.draw(G)
    pyl.show()
    pos=nx.spring_layout(G)
    print(pos)
    print(G.edges)
    large=[(x,y) for (x,y,z)in G.edges(data=True) if z['weight']>100]
    print(large)
    middle = [(x, y) for (x, y, z) in G.edges(data=True) if 50<z['weight'] <= 100]
    middlev = [(x, y) for (x, y, z) in G.edges(data=True) if 10 < z['weight'] <= 50]
    small=[(x,y)for (x,y,z)in G.edges(data=True) if z['weight']<=10]
    nx.draw_networkx_nodes(G,pos,alpha=0.6)
    nx.draw_networkx_edges(G,pos,edgelist=large,width=3,edge_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=middle, width=2, edge_color='yellow')
    nx.draw_networkx_edges(G, pos, edgelist=middlev, width=1, edge_color='yellowgreen')
    nx.draw_networkx_edges(G, pos, edgelist=small, width=0.5, edge_color='green')
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='simhei')
    pyl.axis('off')
    pyl.show()
from pyecharts import Geo,Bar,Pie,Line,Radar
#男女比例
def male(sex):
    att=['男','女','保密']
    val=[]
    for i in att:
        val.append(sex.count(i))

    pie = Pie("", "性别饼图", title_pos="right", width=1200, height=600)
    pie.add("", att, val, label_text_color=None, is_label_show=True, legend_orient='vertical',
            is_more_utils=True, legend_pos='left')
    pie.render("sexPie.html")
    print(count)
filepath='running.csv'
#write_data(filepath)
com,day,hour,floor,zan,sex,name,level,reply,week=read_data(filepath)#1代表星期一0代表星期天
'''
#snownlp(com)#做情感分析
#network_edg_csv(com)#做相关系数矩阵
#network()#做社交网络图
#ana_week(week)
#ana_hour(hour)
#hot(com)#话题度排行
#com_zan(com,zan)#评论和赞的关系
#comment(com)#出词云图
#'''
