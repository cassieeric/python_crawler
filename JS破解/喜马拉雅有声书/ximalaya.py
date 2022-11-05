# coding:utf-8
"""
校验：验证方式，某一个参数或者请求头中的某一个字段进行加密
采集数据过多，可能会出现验证码、加密等等
xm-sign: da9b3b7de5cc127d9857766df9a6ca5e(4)1640760212977(87)1640760212832
逆向 解析 它是怎么生成的？
三种方式：
    1、接口参数
    t[s("0x27")][s("0x34")] = function() {
                            var t, e, r, n = 0;
                            return n = u() ? Date[s("0x31")]() : window[s("0x39")] || 0,
                            t = this[s("0x5")],
                            e = n,
                            r = Date[s("0x31")](),
                            ("{" + t + e + "}(" + l(100) + ")" + e + "(" + l(100) + ")" + r)[s("0x48")](/{([\w-]+)}/, (function(t, e) {
                                return a(e)
                            }
                            ))
                        }

    {himalaya-1640762327955}(100以内的随机数)时间戳(100以内的随机数)类似时间戳(https://www.ximalaya.com/revision/time, 1640763829826)
    ("{" + t + e + "}(" + l(100) + ")" + e + "(" + l(100) + ")" + r)[s("0x48")](/{([\w-]+)}/, (function(t, e) {
    xm-sign: da9b3b7de5cc127d9857766df9a6ca5e(4)1640760212977(87)1640760212832

    2、
    3、
"""
import requests
import time
import hashlib
import random

# 浏览器类型
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
# 服务器时间戳生成地址
serverTime_url = 'https://www.ximalaya.com/revision/time'
serverTime = requests.get(serverTime_url, headers=headers).text  # 返回服务器的时间戳
nowTime = str(round(time.time() * 1000))
# print(response, nowTime)
randomNumber1 = str(round(random.random() * 100))
randomNumber2 = str(round(random.random() * 100))
# {himalaya-服务器时间戳} + 100以内随机数 + 时间戳 + 100以内随机数
xm_sign = str(hashlib.md5(f'himalaya-{0}'.format(serverTime).encode()).hexdigest()) + \
          "({})".format(randomNumber1) + serverTime + "({})".format(randomNumber2) + nowTime
print(xm_sign)
headers['xm_sign'] = xm_sign
print(headers)
# 请求地址
url = 'https://www.ximalaya.com/revision/play/v1/audio?id=487063404&ptype=1'
# id是小说的身份标识
# 获取响应，
response = requests.get(url=url, headers=headers).json()
print(response)



