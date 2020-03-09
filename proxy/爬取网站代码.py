import requests
import re
import random

from bs4 import BeautifulSoup

from ProxyBean import ProxyBean

import proxy

'''
pip install beautifulsoup4
'''

def get_headers():

    """ get_headers
    设置常规浏览器 headers， 让网站不会怀疑 
    
    GET https://www.xicidaili.com/nn/ HTTP/1.1
    Host: www.xicidaili.com
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Referer: https://www.xicidaili.com/nn/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cookie: _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTU5ZTc1YTllY2Y2MWZkNzBmZWY2NDQxM2JhYTA4YzYzBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVlxcXRzUTBBRE8rYXFzZ0RPaWpsbkgxVXN2MXcvY3pjb2UwSVFadHpKdk09BjsARg%3D%3D--977f31f8e45ddda18918be11baeddae719bcfb8f; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1561798865; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1561807627
    If-None-Match: W/"d4e66af1ff40395c5bc65815f83cb30d"
    """

    headers = {
        'Host': 'www.xicidaili.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://www.xicidaili.com/nn/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    return headers

def get_cookies():
    cookies = {
        '_free_proxy_session':'BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTU5ZTc1YTllY2Y2MWZkNzBmZWY2NDQxM2JhYTA4YzYzBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVlxcXRzUTBBRE8rYXFzZ0RPaWpsbkgxVXN2MXcvY3pjb2UwSVFadHpKdk09BjsARg%3D%3D--977f31f8e45ddda18918be11baeddae719bcfb8f',
        'Hm_lvt_0cf76c77469e965d2957f0553e6ecf59':'1561798865',
        'Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59':'1561807627',
    }
    return cookies


def get_a_proxy():
    # with open('proxy.txt', 'r') as f:
    #     data = f.read().strip().split('\n')
    # data = [l for l in data]
    # proxy = data[random.randint(0, len(data)-1)]
    # proxies = { 'http': 'http://{}'.format(proxy), 'https':'https://{}'.format(proxy)}
    # print(proxies)
    p = proxy.get_a_proxy()
    # print(p)
    # input()
    return p
    

def scrapy(type='nn', page=1):
    """
    获取id对应的数据
    """
    url = 'https://www.xicidaili.com/{}/{}'.format(type, page)
    try:
        print(1)
        r = requests.get(url, headers=get_headers(), proxies=get_a_proxy(), verify=False, timeout=3)
        print(2)
        if r.status_code != 200:
            print('connect error')
            return None
        
        #print(r.text)
        matchObj = re.search(r'<table id="ip_list">([\S\s]*)</table>', r.text, re.M|re.I)
        data = matchObj.group()
        test(data)
    except Exception as e:
        print(e)
        # input()
        print('proxy error')

def test(data):
    # with open('data.txt', 'r') as f:
    #     data = f.read()

    #创建 Beautiful Soup 对象
    soup = BeautifulSoup(data, features='html.parser')
    class_type = ['odd', '']
    for t in class_type:
        for element in soup.findAll(name='tr', attrs={'class': t}):
            element_str = element.decode()
            # print(help(element))

            # 获取ip
            ipObj = re.search(r'(2[0-5]{2}|[0-1]?\d{1,2})(\.(2[0-5]{2}|[0-1]?\d{1,2})){3}', element_str, re.M|re.I)
            if not ipObj:
                continue
            ip = ipObj.group()
            
            # 获取端口
            portObj = re.search(r'<td>([0-9]+)</td>', element_str, re.M|re.I)
            if not portObj:
                continue
            port = portObj.group(1)

            # 获取位置
            # <a href="/2019-06-29/jiangsu">江苏扬州</a>
            locationObj = re.search(r'<a href="([^>]*)>([^<]*)</a>', element_str, re.M|re.I)
            if not locationObj:
                continue
            location = locationObj.group(2)

            # 获取类型
            typeObj = re.search(r'<td>([A-Za-z]+)</td>', element_str, re.M|re.I)
            if not typeObj:
                continue
            type = typeObj.group(1)

            proxy = ProxyBean(ip, port, location, type)
            print(proxy.to_string())
            with open('result.csv', 'a') as f:
                f.write(proxy.to_string())
                f.write('\n')
            


    # input('?')
    # for i in soup.findAll(name='tr', attrs={'class': ''}):
    #     print(i)
    #     input('?')
    
    

    #print(data)

if __name__ == '__main__':
    #scrapy()
    #test()
    for i in range(1, 100):
        scrapy('nn', i)
        
    pass



