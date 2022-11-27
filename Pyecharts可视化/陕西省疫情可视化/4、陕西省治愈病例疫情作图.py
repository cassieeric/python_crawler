from pyecharts.charts import Map, Timeline
from pyecharts import options as opts

# 准数据
shanxi_city = ["西安市", "延安市", "咸阳市", "渭南市", "安康市", "汉中市",
               "宝鸡市", "铜川市", "商洛市", "榆林市", "韩城市", "杨凌示范区"
               ]
shanxi_data = [304, 8, 20, 17, 26, 26, 13, 8, 7, 3, 1, 1]

# 绘制陕西疫情地图
map = (
    Map()
    .add('陕西省', [(i, j) for i, j in zip(shanxi_city, shanxi_data)], '陕西')
    .set_global_opts(title_opts=opts.TitleOpts(title='陕西省治愈病例疫情图'),
                     visualmap_opts=opts.VisualMapOpts(max_=310, is_piecewise=True))
)

# 渲染数据
map.render('陕西省治愈病例疫情图.html')
