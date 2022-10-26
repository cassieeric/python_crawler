# -*- coding: utf-8 -*-
"""
1. 正则表达式中的三组括号把匹配结果分成三组

group() 同group（0）就是匹配正则表达式整体结果
group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
————————————————
版权声明：本文为CSDN博主「loveWEBmin」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cout__waht/article/details/82756848
"""

import re

print(re.match("www", "www.baidu.com").span())  # 在起始位置匹配，输出(0, 3)
print(re.match("com", "www.baidu.com"))  # 不在起始位置匹配，输出None

line = "Cats are smaller than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
    print("matchObj.group(0, 1, 2): ", matchObj.group(0, 1, 2))
    print("matchObj.groups(): ", matchObj.groups())
else:
    print("No match!")

