import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
import operator as op
import time

df_tb = pd.read_excel('./data.xlsx')

locations = [location for location in df_tb['地区']]
values = [value for value in df_tb['2016年']]
datas = list(zip(locations, values))

print(datas)
for data in datas:
    print(data)
    # print(type(data))
print(type(datas))

# print("==============================")

# def func(m):
#     a = []
#     for i in range(0, 35):
#         b = (df_tb['地区'][i], df_tb[m][i])
#         a.append(b)
#     return a


# datas2 = func('2016年')
# for data in datas2:
#     print(data)
#     print(type(data))
# print(datas2)
# print(type(datas2))



map = (
    Map().
        add('gdp', [location for location in datas], 'china')
    # .add('gdp', [list(location) for location in datas], 'china')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='各省贫困县分布图'),
        visualmap_opts=opts.VisualMapOpts(max_=150)
                    )
        )
map.render('各省贫困县分布图.html')
# print(op.eq(datas, func('2016年')))

