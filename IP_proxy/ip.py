import requests
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
def GetIp(n):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    url = 'http://www.89ip.cn/index_{0}.html'.format(n)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('td')
    for i, j in zip(items[::5], items[1::5]):
        ip = i.text.replace('\t', '').replace('\n', '') + ':' + j.text.replace('\n', '').replace('\t', '')
        # print(ip)
        proxies = {'https': ip}
        # print(proxies)
        try:
            response = requests.get('https://kyfw.12306.cn/otn/leftTicket/init', headers=header, proxies=proxies,
                                    timeout=3)
            if response.status_code == 200:
                print(ip)
                return ip
        except:
            pass
def getcity():
    with open('CityDic.txt','r') as f:
        trainName=eval(f.read())
    n=10
    ip = GetIp(n)
    #print(ip)
    proxies = {'https': ip}
    for i in trainName.keys():
        while True:
            url = 'https://baike.baidu.com/item/{0}'.format(i+'站')
            try:
                response=requests.get(url, headers=header, proxies=proxies,timeout=1)
                response.encoding='utf-8'
                soup=BeautifulSoup(response.text, 'html.parser')
                items=soup.find_all(class_='basicInfo-item')
                for j in items:
                    if '省' in j.text or '市' in j.text:
                        print(i+'站', j.text.replace('\n', ''))
                        break
                break  #
            except:
                n += 1
                ip = GetIp(n)  #上个ip被禁了，重新请求1个新ip
                proxies = {'https': ip}
getcity()