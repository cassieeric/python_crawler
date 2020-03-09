import cpca
from pyecharts import Geo

# 分析数据
def analysis_data():
    with open('result.csv', 'r') as f:
        data = f.read().split('\n')
    citys = []
    total = 0
    for l in data:
        l = l.strip()
        if l == '':
            continue
        total += 1
        city = l.split(',')[2]
        df = cpca.transform([city])
        if(df.get_values()[0][1] == ''):
            continue
        city = df.get_values()[0][1].replace('市', '')
        print(city)
        no_citys = ['池州', '黔西南布依族苗族自治州'] # 去除pyecharts中未收录的城市
        if city in no_citys : continue 
        #city = city.replace('省','')
        flag = True
        for c in citys:
            if c['name'] == city:
                c['num'] += 1
                flag = False
                break
        if flag:
            citys.append({'name':city, 'num':1})
    
    # 按照数量排个序
    citys = sorted(citys, key=lambda e:e["num"], reverse=True)
    

    print(citys)
    c = [(city['name'], city['num']) for city in citys]
    return (c, total)




data , t = analysis_data()
geo = Geo(
    "全国代理分布", 
    "数据爬取自西刺代理网站： https://www.xicidaili.com", 
    title_color="#fff",
    title_pos="center", 
    width=1000,
    height=800, 
    background_color='#404a59'
)
attr, value = geo.cast(data)
geo.add(
    "", 
    attr, 
    value, 
    visual_range=[0, 200], 
    maptype='china',
    visual_text_color="#fff",
    symbol_size=10, 
    is_visualmap=True
)

geo.render("全国代理分布.html")#生成html文件
