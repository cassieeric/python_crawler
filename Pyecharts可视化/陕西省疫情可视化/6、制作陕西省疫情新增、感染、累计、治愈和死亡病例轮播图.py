from pyecharts.charts import Map, Timeline
from pyecharts import options as opts

# 1. 准数据
shanxi_city = ["西安市", "延安市", "咸阳市", "渭南市", "安康市", "汉中市", "宝鸡市", "铜川市", "商洛市", "榆林市", "韩城市", "杨凌示范区"]
xinzeng = [46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xianyou = [1747, 13, 11, 1, 0, 0, 0, 0, 0, 0, 0, 0]
leiji = [2094, 21, 31, 18, 26, 26, 13, 8, 7, 3, 1, 1]
zhiyu = [304, 8, 20, 17, 26, 26, 13, 8, 7, 3, 1, 1]
siwang = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 2. 绘制新增疫情地图：格式一
map1 = (
    Map(init_opts=opts.InitOpts(width="700px", height="300px", theme="blue"))
    .add('新增病例', [(i, j) for i, j in zip(shanxi_city, xinzeng)], '陕西')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=50))
)

# 3. 绘制现有疫情地图：格式二
map2 = (
    Map()
    .add('现有病例', [(i, j) for i, j in zip(shanxi_city, xianyou)], '陕西')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1750, is_piecewise=True))
)

# 4. 绘制累计疫情地图：格式三
map3 = (
    Map()
    .add('累计病例', [(i, j) for i, j in zip(shanxi_city, leiji)], '陕西')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=2100, is_piecewise=True))
)

# 5. 绘制治愈疫情地图：格式四
map4 = (
    Map()
    .add('治愈病例', [(i, j) for i, j in zip(shanxi_city, zhiyu)], '陕西')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=310, is_piecewise=True))
)

# 6. 绘制死亡疫情地图：格式五
map5 = (
    Map()
    .add('死亡病例', [(i, j) for i, j in zip(shanxi_city, siwang)], '陕西')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=3, is_piecewise=True))
)

# 7. 创建组合类对象
timeline = Timeline(init_opts=opts.InitOpts(width='720px', height='350px'))

# 8. 在组合对象中添加需要组合的图表对象

timeline.add(chart=map1, time_point="陕西省新增病例疫情图")
timeline.add(chart=map2, time_point="陕西省现有病例疫情图")
timeline.add(chart=map3, time_point="陕西省累计病例疫情图")
timeline.add(chart=map4, time_point="陕西省治愈病例疫情图")
timeline.add(chart=map5, time_point="陕西省死亡病例疫情图")
timeline.add_schema(is_auto_play=True, play_interval=2000)

# 9. 渲染数据
timeline.render('陕西省疫情轮播图.html')
