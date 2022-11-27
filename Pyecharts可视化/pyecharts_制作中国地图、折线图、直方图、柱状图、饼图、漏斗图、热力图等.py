#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/28 14:06
# @Author  : April
# Desc: 得到各种 图形

import pyecharts
# 直方图
from pyecharts.charts import Bar
# 饼图
from pyecharts.charts import Pie
# 折线图
from pyecharts.charts import Line
# 漏斗图
from pyecharts.charts import Funnel
# 热力图
from pyecharts.charts import HeatMap
# 地图
from pyecharts.charts import Map
# 选项配置
from pyecharts import options as opts
# 渲染为图片
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
#
from pyecharts.faker import Faker
import random


# --1.输出pyecharts的版本 只支持3.6之后的
def get_version():
    print(pyecharts.__version__)


# --2.输出直方图
def render_zhifangtu():
    # --2.1示例数据
    cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
    data1 = [123, 153, 89, 107, 98, 23]
    data2 = [56, 77, 93, 68, 45, 67]

    # --2.2渲染
    bar = (Bar()
           .add_xaxis(cate)
           .add_yaxis('电商渠道', data1)
           .add_yaxis('门店', data2)
           # 系列配置项使用示例：
           # 设置 每列最高要显示
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"), ]))
           # 全局配置使用示例：
           .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试", subtitle="2022年运势")))
    # 渲染到render.html
    # bar.render()
    # 渲染到图片
    make_snapshot(snapshot, bar.render(), "bar_test.png")


# --3.饼图
def render_bingtu():
    # 示例数据
    cate = ['蹲蹲', '荣荣', '茸茸', '冬冬', "奥运"]
    data = [93, 100, 119, 105, 20]
    pie = (Pie()
           .add('', [list(z) for z in zip(cate, data)],
                radius=["30%", "75%"],
                rosetype="radius")
           .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例", subtitle="2022谁最胖"))
           .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
           )
    make_snapshot(snapshot, pie.render(), "pie_test.png")


# --4.直线图
def render_zhixaintu():
    # 示例数据
    cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
    data1 = [123, 153, 89, 107, 98, 23]
    data2 = [56, 77, 93, 68, 45, 67]
    """
    折线图示例:
    1. is_smooth 折线 OR 平滑
    2. markline_opts 标记线 OR 标记点
    """
    line = (Line()
            .add_xaxis(cate)
            .add_yaxis('电商渠道', data1,
                       markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
            .add_yaxis('门店', data2,
                       is_smooth=True,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="自定义标记点",
                                                                                  coord=[cate[2], data2[2]], value=data2[2])]))
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例", subtitle="我是副标题"))
            )
    make_snapshot(snapshot, line.render(), "line_test.png")


# --5.漏斗图
def render_loudoutu():
    # 示例数据
    cate = ['访问', '注册', '加入购物车', '提交订单', '付款成功']
    data = [30398, 15230, 10045, 8109, 5698]
    """
    漏斗图示例：
    1. sort_控制排序，默认降序；
    2. 标签显示位置
    """
    funnel = (Funnel()
              .add("用户数", [list(z) for z in zip(cate, data)],
                   sort_='ascending',
                   label_opts=opts.LabelOpts(position="inside"))
              .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例", subtitle="我是副标题"))
              )
    make_snapshot(snapshot, funnel.render(), "funnel_test.png")


# --5.热力图
def render_relitu():
    # 示例数据
    # i 为时 j为星期 后面为随机数
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heat = (HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis("访客数",
                   Faker.week,
                   data,
                   label_opts=opts.LabelOpts(is_show=True, position="inside"))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-基本示例", subtitle="我是副标题"),
        visualmap_opts=opts.VisualMapOpts(),
        legend_opts=opts.LegendOpts(is_show=False))
    )
    make_snapshot(snapshot, heat.render(), "heat_test.png")


# --6.地图
def render_ditu():
    province = ['广东', '湖北', '湖南', '四川', '重庆', '黑龙江', '浙江', '山西', '河北', '安徽', '河南', '山东', '西藏']
    data = [(i, random.randint(50, 150)) for i in province]
    _map = (
        Map()
            .add("销售额", data, "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-基本示例"),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        )
    )
    make_snapshot(snapshot, _map.render(), "map_test.png")


if __name__ == "__main__":
    get_version()
    render_zhifangtu()
    render_bingtu()
    render_zhixaintu()
    render_relitu()
    render_ditu()
