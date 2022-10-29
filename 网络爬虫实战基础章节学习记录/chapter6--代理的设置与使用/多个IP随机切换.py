# -*- coding: utf-8 -*-
import random
# 把我们从IP代理网站上得到的IP，用IP地址：端口号格式存入iplist数据
iplist = ["xxx.xxx.xxx.xxx:xxxx", "xxx.xxx.xxx.xxx:xxxx"]
proxies = {'http': random.choice(iplist)}
# 增加爬虫的健壮性
