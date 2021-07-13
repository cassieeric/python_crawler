#可视化部分
import pandas  as pd
from pyecharts.charts import Map,Page
from pyecharts import options as opts
# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 打开文件
df = pd.read_excel('china.xlsx')
# 对省份进行统计
data2 = df['省份']
data2_list = list(data2)
data3 = df['累计确诊']
data3_list = list(data3)
data4 = df['死亡']
data4_list = list(data4)
data5 = df ['治愈']
data5_list = list(data5)
a = (
    Map()
        .add("累计确诊", [list(z) for z in zip(data2_list, data3_list)], "china")
        .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
)

b = (
    Map()
        .add("死亡", [list(z) for z in zip(data2_list, data4_list)], "china")
        .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
)

c = (
    Map()
        .add("治愈", [list(z) for z in zip(data2_list, data5_list)], "china")
        .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
)

page = Page(layout=Page.DraggablePageLayout)
page.add(
    a,
    b,
    c,
)
# 先生成render.html文件
# page.render()
#完成上一步之后把 page.render()这行注释掉
# 然后循行这下面
Page.save_resize_html("render.html",
	cfg_file="chart_config.json",
 	dest="my_test.html")