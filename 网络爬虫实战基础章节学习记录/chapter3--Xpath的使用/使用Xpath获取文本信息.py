# -*- coding: utf-8 -*-

from lxml import etree

html = etree.parse("./test.html", etree.HTMLParser())
# //li表述获取所有的li节点，//a表示选择li节点下的子孙子节点a，即所有的a节点
result1 = html.xpath("//li//a//text()")  # 获取文本内容，返回的是一个列表
print(result1)
for item in result1:
    print(item)
