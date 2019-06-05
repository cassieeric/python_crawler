# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:40:03 2019
@author: 微信公众号：凹凸数读
参考文章：https://www.jianshu.com/p/e7f3bcc19fc1
"""

from bs4 import BeautifulSoup
import requests
import time
import random
import re
from copyheaders import headers_raw_to_dict

headers = b"""
accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
cache-control:max-age=0
cookie:_T_WM=e5b253499ac4c145b32543070ef9be71; SUB=_2A25xt08MDeRhGeNH71ET9CfLzDqIHXVTWFFErDV6PUJbkdAKLWzNkW1NSqW5YkubWy6QHAM0vGRYYx0jztP851_n; SUHB=0mxUEZ38ycHCjE; SCF=AmVHi90xo1EtkU2RnlJp-AHtjZsjKceughYgDgeB8zXNbGboSza02ZYOTyvNcNm0bOom3lVH_--gzdl4wDNQkI8.; SSOLoginState=1555251036; MLOGIN=1
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
"""

# 将请求头字符串转化为字典
headers = headers_raw_to_dict(headers)

for i in range(2, 2800): 
    print('第' + str(i) + '页')
    # 请求网址
    url = 'https://weibo.cn/comment/HgCfidCUs?uid=1343887012&rl=0&page=' + str(i)
    response = requests.get(url=url, headers=headers, verify=False)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    result_1 = soup.find_all(class_='ctt')
    result_2 = soup.find_all(class_='cc')
    result_3 = soup.find_all(class_='ct')
    result_4 = re.findall('id="C_.*?href="/.*?">(.*?)</a>', html)
    result_5 = re.findall('id="C_.*?href="(.*?)">.*?</a>', html)
    time.sleep(3.25 + random.random()) #随机sleep，避免判定爬虫
    
    try:
        for j in range(len(result_1)):
            res = re.findall('(\d+)', result_2[j * 2].get_text())
            if len(res) > 0:
                praise = res[0]
                name = result_4[j]
                urls = 'https://weibo.cn' + result_5[j] + '/info'
                text = result_1[j].get_text().replace(',', '，')
                date = result_3[j].get_text().split(' ')[0]
                time_r = result_3[j].get_text().split(' ')[1].split(' ')[0]
                if '@' in text:   # 去除@及用户信息
                    if ':' in text:   
                        comment = text.split(':')[-1]
                        #微博昵称+评论+时间+日期+用户链接(方便下一步爬取个人信息)
                        print(name, comment, time_r, date, urls) 
                        with open('翟天临微博评论_凹凸数读.csv', 'a+') as f:
                            f.write(name + ',' + comment + ',' + time_r + ',' + date + ',' + urls + '\n')
                        f.close()
                    else:
                        print(name, '无', time_r, date, urls)
                        with open('翟天临微博评论_凹凸数读.csv', 'a+') as f:
                               f.write(name + ',' + '无' + ',' + time_r + ',' + date + ',' + urls +  '\n')
                        f.close()
                else:
                    print(name, text, time_r, date, urls)
                    with open('翟天临微博评论_凹凸数读.csv', 'a+') as f:
                        f.write(name + ',' + text + ',' + time_r + ',' + date + ',' + urls + '\n')
                    f.close()
            else:
                pass
    except:
        continue
