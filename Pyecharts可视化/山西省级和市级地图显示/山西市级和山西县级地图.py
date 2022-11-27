# -*-: coding: utf-8 -*-
# pyecharts版本要求是0.5
# 山西省-市级地图
from pyecharts import Map
city = ['大同市', '朔州市', '忻州市', '阳泉市', '太原市', '晋中市', '吕梁市', '临汾市', '晋城市', '运城市', '长治市']
values = ['50', '35', '5', '20', '8', '23', '42', '12', '65', '52', '46']
map = Map('山西地图', '山西', width=1200, height=600)
map.add('山西', city, values, visual_range=[1, 50], maptype='山西',
        is_visualmap=True, visual_text_color='#000', is_label_show=True)
map.render(path='山西地图.html')

# 山西省长治市-县级地图
from pyecharts import Map
city = ['长治县', '襄垣县', '长子县', '屯留县', '壶关县', '黎城县', '平顺县', '武乡县', '沁县', '沁源县']
values = ['50', '35', '5', '20', '8', '23', '42', '12', '65', '52']
map = Map('长治地图', '长治', width=1200, height=600)
map.add('长治', city, values, visual_range=[1, 50], maptype='长治',
        is_visualmap=True, visual_text_color='#000', is_label_show=True)
map.render(path='长治地图.html')

# 试图直接画山西省长治市-县级地图
from pyecharts import Map
city = ['长治县', '襄垣县', '长子县', '屯留县', '壶关县', '黎城县', '平顺县', '武乡县', '沁县', '沁源县']
values = ['50', '35', '5', '20', '8', '23', '42', '12', '65', '52']
map = Map('山西地图', '山西', width=1200, height=600)
map.add('山西', city, values, visual_range=[1, 50], maptype='山西',
        is_visualmap=True, visual_text_color='#000', is_label_show=True)
map.render(path='山西地图-县级.html')

