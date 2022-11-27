from pyecharts.charts import Map, Timeline
from pyecharts import options as opts

# 1. 准数据
hubei_city = ["武汉市","孝感市","黄冈市","荆州市","鄂州市","随州市",
        "襄阳市","黄石市","宜昌市","荆门市","咸宁市","十堰市",
        "仙桃市","天门市","恩施土家族苗族自治州","潜江市","神农架林区"]
hubei_data = [3214, 628, 722, 287, 224, 304, 321, 202, 269, 217, 206, 177, 97, 82, 103, 27, 7]

guangdong_city = ["深圳市","广州市","珠海市","佛山市","东莞市","中山市",
        "惠州市","汕头市","湛江市","江门市","肇庆市","阳江市",
        "梅州市","茂名市","清远市","揭阳市","韶关市",
        "潮州市","汕尾市","河源市"]
guangdong_data = [375, 317, 86, 70, 62, 58, 53, 25, 21, 20, 15, 13, 13, 11, 10, 8, 7, 5, 5, 3]

# 2. 绘制湖北疫情地图：格式一
map1 = (
    Map(init_opts=opts.InitOpts(width="700px", height="300px", theme="blue"))
    .add('', [(i, j) for i, j in zip(hubei_city,hubei_data)], '湖北')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=4000))
)

# 3. 绘制广东疫情地图：格式二
map2 = (
    Map()
    .add('', [(i,j) for i,j in zip(guangdong_city,guangdong_data)], '广东')
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=400,is_piecewise=True))
)

# 4. 创建组合类对象
timeline = Timeline(init_opts=opts.InitOpts(width='720px', height='350px'))

# 5. 在组合对象中添加需要组合的图表对象

timeline.add(chart=map1, time_point="湖北省疫情地图")
timeline.add(chart=map2, time_point="广东省疫情地图")
timeline.add_schema(is_auto_play=True, play_interval=3000)

# 6. 渲染数据
timeline.render('湖北省疫情和广东省疫情轮播图.html')
