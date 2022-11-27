# 1.导入相关库
from pyecharts.charts import Geo
import pyecharts.options as opts
# 2.准备数据
city_num = [('武汉',105),('成都',70),('北京',99),
            ('西安',80),('杭州',60),('贵阳',34),
            ('上海',65),('深圳',54),('乌鲁木齐',76),
            ('哈尔滨',47),('兰州',56),('信阳',85)]
start_end = [('武汉','成都'),('武汉','北京'),('武汉','西安'),
             ('武汉','杭州'),('武汉','贵阳'),('武汉','上海'),
             ('武汉','深圳'),('武汉','乌鲁木齐'),('武汉','哈尔滨'),
             ('武汉','兰州'),('武汉','信阳')]

map = (
    # 3.初始化地图类
    Geo(init_opts=opts.InitOpts(width="700px", height="300px", theme="blue"))
    .add_schema(maptype='china',
                itemstyle_opts=opts.ItemStyleOpts(color='#323c48', border_color='black'))
    # 4.添加数据
    .add('', data_pair=city_num, color='white')
    .add('', data_pair=start_end, type_="lines", label_opts=opts.LabelOpts(is_show=False),
         effect_opts=opts.EffectOpts(symbol="arrow",
                                     color='gold',
                                     symbol_size=8))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图"),
        visualmap_opts=opts.VisualMapOpts(min_=30, max_=110))
)
# 5.图形展示
map.render("迁徙图.html")


