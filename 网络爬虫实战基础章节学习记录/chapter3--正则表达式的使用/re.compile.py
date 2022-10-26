# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # 忽略大小写
m = pattern.match("Hello World Wide Web")

print(m)
print(m.group())
print(m.group(0))
print(m.span(0))
print(m.group(1))
print(m.span(1))
print(m.group(2))
print(m.span(2))
print(m.groups())
print(m.group(3))
