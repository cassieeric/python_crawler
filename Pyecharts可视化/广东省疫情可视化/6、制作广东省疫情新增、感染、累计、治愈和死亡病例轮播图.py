from pyecharts.charts import Map, Timeline
from pyecharts import options as opts

# 1. 准数据
guangdong_city = ["深圳市", "广州市", "珠海市", "佛山市", "东莞市", "中山市",
                  "惠州市", "汕头市", "湛江市", "江门市", "肇庆市", "阳江市",
                  "梅州市", "茂名市", "清远市", "揭阳市", "韶关市", "潮州市", "汕尾市", "河源市", "云浮市"]
xinzeng = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xianyou = [2, 3, 0, 0, 26, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
leiji = [433, 526, 98, 101, 128, 68, 62, 25, 23, 23, 19, 14, 16, 14, 12, 10, 10, 5, 6, 5, 0]
zhiyu = [428, 522, 97, 101, 101, 67, 62, 25, 23, 23, 18, 14, 16, 14, 12, 10, 9, 5, 6, 5, 0]
siwang = [3, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]


# 2. 绘制新增疫情地图：格式一
map1 = (
    Map(init_opts=opts.InitOpts(width="700px", height="300px", theme="blue"))
    .add('新增病例', [(i, j) for i, j in zip(guangdong_city, xinzeng)], '广东')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=3))
)

# 3. 绘制现有疫情地图：格式二
map2 = (
    Map()
    .add('现有病例', [(i, j) for i, j in zip(guangdong_city, xianyou)], '广东')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=30, is_piecewise=True))
)

# 4. 绘制累计疫情地图：格式三
map3 = (
    Map()
    .add('累计病例', [(i, j) for i, j in zip(guangdong_city, leiji)], '广东')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=530, is_piecewise=True))
)

# 5. 绘制治愈疫情地图：格式四
map4 = (
    Map()
    .add('治愈病例', [(i, j) for i, j in zip(guangdong_city, zhiyu)], '广东')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=530, is_piecewise=True))
)

# 6. 绘制死亡疫情地图：格式五
map5 = (
    Map()
    .add('死亡病例', [(i, j) for i, j in zip(guangdong_city, siwang)], '广东')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=3, is_piecewise=True))
)

# 7. 创建组合类对象
timeline = Timeline(init_opts=opts.InitOpts(width='720px', height='350px'))

# 8. 在组合对象中添加需要组合的图表对象

timeline.add(chart=map1, time_point="广东省新增病例疫情图")
timeline.add(chart=map2, time_point="广东省现有病例疫情图")
timeline.add(chart=map3, time_point="广东省累计病例疫情图")
timeline.add(chart=map4, time_point="广东省治愈病例疫情图")
timeline.add(chart=map5, time_point="广东省死亡病例疫情图")
timeline.add_schema(is_auto_play=True, play_interval=2000)

# 9. 渲染数据
timeline.render('广东省疫情轮播图.html')
