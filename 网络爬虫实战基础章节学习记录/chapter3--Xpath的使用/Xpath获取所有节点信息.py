# -*- coding: utf-8 -*-

from lxml import etree

html = etree.parse("./test.html", etree.HTMLParser())
result1 = html.xpath("//*")

# 获取所有标签
for item in result1:
    print(item)

print("**************************")
# 获取所有标签的li标签
result2 = html.xpath("//li")

for item in result2:
    print(item)
