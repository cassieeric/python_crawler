# -*- coding: utf-8 -*-

from lxml import etree

text = """
    <div>
        <ul>
            <li class="item-0"><a href="www.baidu.com">baidu</a>
            <li class="item-1"><a href="https://blog.csdn.net/">myblog</a>
            <li class="item-2"><a href="https://pdcfighting/">mywebsite</a>
            <li class="item-3"><a href="https://hao123.com/">hao123</a>
"""

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode("utf-8"))
