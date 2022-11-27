from pyecharts.charts import Map, Timeline
from pyecharts import options as opts

# 准数据
guangdong_city = ["深圳市", "广州市", "珠海市", "佛山市", "东莞市", "中山市",
                  "惠州市", "汕头市", "湛江市", "江门市", "肇庆市", "阳江市",
                  "梅州市", "茂名市", "清远市", "揭阳市", "韶关市", "潮州市", "汕尾市", "河源市", "云浮市"]
guangdong_data = [433, 526, 98, 101, 128, 68, 62, 25, 23, 23, 19, 14, 16, 14, 12, 10, 10, 5, 6, 5, 0]

# 绘制广东疫情地图
map = (
    Map()
    .add('广东省', [(i, j) for i, j in zip(guangdong_city, guangdong_data)], '广东')
    .set_global_opts(title_opts=opts.TitleOpts(title='广东省累计病例疫情图'), visualmap_opts=opts.VisualMapOpts(max_=530, is_piecewise=True))
)

# 渲染数据
map.render('广东省累计病例疫情图.html')
