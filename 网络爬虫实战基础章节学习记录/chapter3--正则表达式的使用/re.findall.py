# -*- coding: utf-8 -*-

import re

pattern = re.compile(r"\d+")
result1 = pattern.findall("runoob 123 google 456")
result2 = pattern.findall("run88oob123google456", 3, 10)

# findall返回的是一个列表，没有匹配到的话，则返回空列表
print(result1)
print(result2)
