import pandas as pd

from pyecharts import Map

df_tb = pd.read_excel('data.xlsx')


provinces = []
values = []

for i in range(0, 35):
    location = df_tb['地区'][i]
    value = df_tb['2016年'][i]
    provinces.append(location)
    values.append(value)


map = Map("中国地图", width=1200, height=600)
map.add("中国地图", provinces, values, visual_range=[0, 50], maptype='china', is_visualmap=True,
visual_text_color='#600', is_label_show=True)
map.render(path="中国地图.html")
