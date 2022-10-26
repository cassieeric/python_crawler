# -*- coding: utf-8 -*-

import re

print(re.search("www", "www.baidu.com").group())  # 在起始位置匹配，输出匹配内容
print(re.search("com", "www.baidu.com").group())  # 不在起始位置匹配，输出匹配内容

print(re.search("www", "www.baidu.com").span())
print(re.search("com", "www.baidu.com").span())

line = "Cats are smaller than dogs"
matchObj = re.match(r'dogs', line)

if matchObj:
    print("match-->matchObj.group()", matchObj.group())
else:
    print("No match!")
