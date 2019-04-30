# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import random
import time
import pandas
from urllib import parse
def get_inf(url):
    dd=pandas.DataFrame()
    html = t(url)
    '''
    c = '您操作的行为好像机器人哦～'
    if c in html:
        cap(html)'''
    soup = BeautifulSoup(html, 'lxml')
    s = soup.find('div', class_='result_list')
    try:
        for i in s:
            inf = {}
            try:
                inf['level'] = i.find('span', class_='level').text[0]
            except Exception as e:
                inf['level'] = '0'
            try:
                inf['price'] = i.find('span', class_='sight_item_price').find('em').text
            except Exception as e:
                inf['price'] = ''
            try:
                inf['name'] = i.find('a', class_='name').text
            except Exception as e:
                inf['name'] = ''
            try:
                inf['num'] = i.find('span', class_='hot_num').text
            except Exception as e:
                inf['num'] = ''
            try:
                inf['add_pro'] = i.find('span', class_='area').find('a').text.split('·')[0]
                inf['add_city'] = i.find('span', class_='area').find('a').text.split('·')[1]
            except  Exception as e:
                inf['add_pro'] = i.find('span', class_='area').find('a').text
                inf['add_city'] = i.find('span', class_='area').find('a').text
            try:
                inf['hot'] = i.find('span', class_='product_star_level').find('em').get('title').split(':')[1]
            except  Exception as e:
                inf['hot'] = ''
            try:
                inf['descri'] = i.find('div', class_='intro color999').text
            except Exception as e:
                inf['descri'] = ''
            dd = dd.append(inf, ignore_index=True)
        return dd
    except Exception as e:
        get_inf(url)
        
def cap(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        scr = soup.find('img', class_='mp-captchaimg').get('src')
        print(scr)
        with open('img.png', 'wb')as f:
            img = requests.get(scr, headers=headers).content
            f.write(img)
            f.close()
        captcha = input('输入验证码')
        cap_url = 'http://piao.qunar.com/captcha/check/pc.json?captchaRequestURL=http%3A%2F%2Fpiao.qunar.com%2Fticket%2Flist.htm%3Fkeyword%3D' + parse.quote(
            p) + 'captchaRequestURI=%2Fticket%2Flist.htm&captchaAnswer=' + captcha
        z = requests.get(cap_url)
        print('验证成功继续爬虫')
    except z.status_code == 403:
        cap(html)
        
'''
    try:
        r = requests.get(url, headers=headers, proxies=proxies).text
        soup = BeautifulSoup(r, 'lxml')
        s = soup.find('div', class_='result_list')
        if not s == None:
            return s
        else:
            r = requests.get(url, headers=headers).text
            soup = BeautifulSoup(r, 'lxml')
            s = soup.find('div', class_='result_list')
            return s
    except Exception as e:
        t(url)
'''

def t(url):
    s=time.time()
    proxies_list = [{'http': 'http://1.196.160.101:9999'}, {'http': 'http://112.115.57.20:3128'},
                    {'http': 'http://222.221.11.119:3128'}, {'http': 'http://1.196.160.101:9999'},
                    {'http': 'http://116.182.1.194:808'}, {'http': 'http://60.191.134.165:9999'},
                    {'http': 'http://39.89.253.212:1080'}, {'http': 'http://180.106.16.118:3128'},
                    {'http': 'http://58.53.128.83:3128'}, {'http': 'http://112.115.57.20:3128'},
                    {'http': 'http://112.115.57.20:3128'}, {'http': 'http://60.191.134.165:9999'},
                    {'http': 'http://60.191.134.165:9999'}, {'http': 'http://1.196.160.101:9999'},
                    {'http': 'http://1.196.160.101:9999'}, {'http': 'http://218.14.115.211:3128'},
                    {'http': 'http://58.53.128.83:3128'}
                    ]
    proxies = random.choice(proxies_list)
    coo = [
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; _jzqckmp=1; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; csrfToken=1qCtsqgMFimWdjttDWANGl7jicWRG5er; QN163=0; QN71="MjIzLjY1LjE5MC4xMjE65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723; _vi=7ZCUp7J4Mr2Svknyoz7JXSP5JogmM1_aFu2OPZtsX4srClaTnKqMaLB2OejH-KhDtP-ERWc6ABWU1pQ7NH7QOBlzguucyfzjDddhCr8Z5XhECB2eqZoohDI-J93nZ_E4PAgapF9OgxjHOfRdkMqXHqBHzsThZNJGDSSjqhyd6xA9; QN63=%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%9B%9B%E5%B7%9D%7C%E5%AE%89%E5%BE%BD%7C%E5%90%89%E6%9E%97%7C%E7%A6%8F%E5%BB%BA%7C%E8%B4%B5%E5%B7%9E; QN58=1540885939823%7C1540888573855%7C72; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1540888574; QN271=31dc5735-ee3f-4e15-b5fa-b8051fda2cd9; JSESSIONID=2302A0917F580F739F189BBCC271C5F9; Request-Node=a1ecad762a42f81dc1192f44e0f55432; QN267=1952087195922289f6',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; _jzqckmp=1; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; csrfToken=1qCtsqgMFimWdjttDWANGl7jicWRG5er; QN163=0; QN71="MjIzLjY1LjE5MC4xMjE65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723; QN63=%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%9B%9B%E5%B7%9D%7C%E5%AE%89%E5%BE%BD%7C%E5%90%89%E6%9E%97%7C%E7%A6%8F%E5%BB%BA%7C%E8%B4%B5%E5%B7%9E; QN267=1952087195cab757cb; _vi=gksuVNuLTNukH21uB-z6uuuuoMxITP-7SkjqUtJN2HkGaNzN6GeKKy3l3kcs75_PR4vvgbI0AVjXlKvkb68E4daTRRICaSofpbzQR66XaB1-g5F-mYMt4obVSmvttkxvz3QiM9yF95juxTuBHgBZs8uinwcL_EVASjnkOjDXBmtf; QN58=1540885939823%7C1540889608413%7C73; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1540889609; QN271=cf1eec55-bc2e-4e0f-b042-5e20f83bbf80; JSESSIONID=7D0A32C809BEE55C4DD02261C08E0CF0; Request-Node=998b38c4107c40f8120f978f41015b76',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; _jzqckmp=1; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; csrfToken=1qCtsqgMFimWdjttDWANGl7jicWRG5er; QN163=0; QN71="MjIzLjY1LjE5MC4xMjE65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723; QN63=%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%9B%9B%E5%B7%9D%7C%E5%AE%89%E5%BE%BD%7C%E5%90%89%E6%9E%97%7C%E7%A6%8F%E5%BB%BA%7C%E8%B4%B5%E5%B7%9E; _vi=gksuVNuLTNukH21uB-z6uuuuoMxITP-7SkjqUtJN2HkGaNzN6GeKKy3l3kcs75_PR4vvgbI0AVjXlKvkb68E4daTRRICaSofpbzQR66XaB1-g5F-mYMt4obVSmvttkxvz3QiM9yF95juxTuBHgBZs8uinwcL_EVASjnkOjDXBmtf; QN267=195208719590351314; QN58=1540885939823%7C1540889683164%7C74; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1540889684; QN271=5c843cae-6d14-4e37-b461-f5cb7074c5ef; JSESSIONID=878E3F1B510F70C931D21576E3EC829F; Request-Node=bb85bb52c3587faf987b4994aef8e559',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; _jzqckmp=1; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; csrfToken=1qCtsqgMFimWdjttDWANGl7jicWRG5er; QN163=0; QN71="MjIzLjY1LjE5MC4xMjE65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723; QN63=%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%9B%9B%E5%B7%9D%7C%E5%AE%89%E5%BE%BD%7C%E5%90%89%E6%9E%97%7C%E7%A6%8F%E5%BB%BA%7C%E8%B4%B5%E5%B7%9E; _vi=gksuVNuLTNukH21uB-z6uuuuoMxITP-7SkjqUtJN2HkGaNzN6GeKKy3l3kcs75_PR4vvgbI0AVjXlKvkb68E4daTRRICaSofpbzQR66XaB1-g5F-mYMt4obVSmvttkxvz3QiM9yF95juxTuBHgBZs8uinwcL_EVASjnkOjDXBmtf; QN267=19520871956f062f25; QN58=1540885939823%7C1540889701800%7C75; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1540889702; QN271=053e9263-bd49-4121-8206-ca67d017e54a; JSESSIONID=A967A120262FA0E28B56B10EAA4C367E; Request-Node=a674525dbbbd41c33c2f601ff94a230e',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; _jzqckmp=1; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; csrfToken=1qCtsqgMFimWdjttDWANGl7jicWRG5er; QN163=0; QN71="MjIzLjY1LjE5MC4xMjE65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723; QN63=%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%9B%9B%E5%B7%9D%7C%E5%AE%89%E5%BE%BD%7C%E5%90%89%E6%9E%97%7C%E7%A6%8F%E5%BB%BA%7C%E8%B4%B5%E5%B7%9E; _vi=gksuVNuLTNukH21uB-z6uuuuoMxITP-7SkjqUtJN2HkGaNzN6GeKKy3l3kcs75_PR4vvgbI0AVjXlKvkb68E4daTRRICaSofpbzQR66XaB1-g5F-mYMt4obVSmvttkxvz3QiM9yF95juxTuBHgBZs8uinwcL_EVASjnkOjDXBmtf; QN267=19520871953205ac98; QN58=1540885939823%7C1540889720576%7C76; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1540889721; QN271=3f9f06f3-28ca-41a4-aa2d-21bfdec2efa0; JSESSIONID=E5DCE902CCED4FB281B0682BD05CDFB2; Request-Node=32ac165cc6f2ebaac4f13a85e20efca3',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; QN63=%E5%9B%9B%E5%B7%9D%7C%E9%BB%91%E9%BE%99%E6%B1%9F%7C%E5%B9%BF%E8%A5%BF%7C%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%AE%89%E5%BE%BD%7C%E5%90%89%E6%9E%97; QN205=organic; QN277=organic; csrfToken=8FsIHF1UkES6qtY6Jv3rZYwPnstV4lcC; _vi=J76VgFZuW5xjFTWCG5PbXv5SsSyWsIE6YaSpPX8dZe_3ly7Xxu4lu1AER_0DvNCc_WsmZ9wpaZIsscMHq4yTC6V_bXbWmN573xCRiXZ-Ij51cc1FVus8Cgeexuv3cKUcJKeU6cKWBQHvLm0KxhxcLXckN8HOJxCFNjS55kS-5-iY; QN163=0; QN71="MjIzLjY1LjE4OC4xMDU65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723,1541418695,1541578932; QN58=1541578932026%7C1541578935068%7C2; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1541578935; QN271=4ce8c38f-0b31-4b40-8953-7d4a296468bf; QN267=1952087195fab0b2fe; JSESSIONID=30700EDBCA5AF4FF94638EF500633212; Request-Node=d26f37e86593d0c60bd36b50560ad0c9',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; QN205=organic; QN277=organic; csrfToken=8FsIHF1UkES6qtY6Jv3rZYwPnstV4lcC; _vi=J76VgFZuW5xjFTWCG5PbXv5SsSyWsIE6YaSpPX8dZe_3ly7Xxu4lu1AER_0DvNCc_WsmZ9wpaZIsscMHq4yTC6V_bXbWmN573xCRiXZ-Ij51cc1FVus8Cgeexuv3cKUcJKeU6cKWBQHvLm0KxhxcLXckN8HOJxCFNjS55kS-5-iY; QN163=0; QN71="MjIzLjY1LjE4OC4xMDU65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723,1541418695,1541578932; QN58=1541578932026%7C1541579446047%7C3; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1541579446; QN271=6de97e9c-e1c1-46c5-8d66-dae3e1ca950d; QN267=1952087195be89784c; JSESSIONID=C082A34027C8F6620E53B789F9F6A4E8; Request-Node=a27caae61c3198f7bb304955a14a8aae; QN63=%E4%BA%94%E6%8C%87%E5%B1%B1%7C%E5%9B%9B%E5%B7%9D%7C%E9%BB%91%E9%BE%99%E6%B1%9F%7C%E5%B9%BF%E8%A5%BF%7C%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F%7C%E5%AE%89%E5%BE%BD',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; QN205=organic; QN277=organic; csrfToken=8FsIHF1UkES6qtY6Jv3rZYwPnstV4lcC; QN163=0; QN71="MjIzLjY1LjE4OC4xMDU65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723,1541418695,1541578932; QN267=19520871953b9bc9e6; QN58=1541578932026%7C1541580394312%7C4; _vi=UHwM1GeuKHUlPThfFGTdmypChNnDt7UANSJ4z3X0XSvb5dEz8FaEx19j1s4xnm0jaGDv-zp7UnalfAoYIKdkJwYaZMeYgluEioo56jpJmbtFp8e3OJmq9Y8d6hLXpyCM7cGIrlW15Tvxb3GyTddDe_PpB-gr37MJsISeabzWBYsb; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1541580395; QN271=67f8e923-9814-424e-93db-9daf7ee164cb; JSESSIONID=C655F5434D7DF3DFA4D921C47164A4E2; Request-Node=ff0e8931e1e8a595e16744b67e3a57e0; QN63=%E6%B1%9F%E8%8B%8F%7C%E4%BA%94%E6%8C%87%E5%B1%B1%7C%E5%9B%9B%E5%B7%9D%7C%E9%BB%91%E9%BE%99%E6%B1%9F%7C%E5%B9%BF%E8%A5%BF%7C%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F%7C%E8%A5%BF%E8%97%8F',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; QN205=organic; QN277=organic; csrfToken=8FsIHF1UkES6qtY6Jv3rZYwPnstV4lcC; QN163=0; QN71="MjIzLjY1LjE4OC4xMDU65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723,1541418695,1541578932; _vi=UHwM1GeuKHUlPThfFGTdmypChNnDt7UANSJ4z3X0XSvb5dEz8FaEx19j1s4xnm0jaGDv-zp7UnalfAoYIKdkJwYaZMeYgluEioo56jpJmbtFp8e3OJmq9Y8d6hLXpyCM7cGIrlW15Tvxb3GyTddDe_PpB-gr37MJsISeabzWBYsb; QN267=1952087195106c25f0; QN58=1541578932026%7C1541580421358%7C5; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1541580422; QN271=cb124819-9e78-415c-afcd-e2120907a227; JSESSIONID=3799017F25409A95E8753F858574A17D; Request-Node=afa452cef48c72dbb9cc78b724a8c11b; QN63=%E6%B1%9F%E9%97%A8%7C%E6%B1%9F%E8%8B%8F%7C%E4%BA%94%E6%8C%87%E5%B1%B1%7C%E5%9B%9B%E5%B7%9D%7C%E9%BB%91%E9%BE%99%E6%B1%9F%7C%E5%B9%BF%E8%A5%BF%7C%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81%7C%E5%AE%81%E5%A4%8F',
        'QN99=8160; QN300=auto_4e0d874a; QunarGlobal=10.86.213.147_-30bb2686_166bfb00815_-19b5|1540814755802; QN601=b5d12dd73f46034503857d50a0e8fb14; _i=VInJOvrfcd1Csll1Zlj0BL3fC03q; QN269=71BEBCEDD21211E8B5A2FA163E9DCB6D; QN48=tc_bb074d08887cbc6c_166bfb75eda_f79e; fid=bc876364-7518-413f-bf90-99061e3b65b3; QN73=3316-3317; QN1=O5cv5lvW+jIG6w2ILVbGAg==; QN57=15408155768660.87091959049805; cto_lwid=6ffedf39-c8e0-4abb-9679-59a4036bae28; QN67=35176%2C460734; __utma=183398822.1027256419.1540814762.1540814762.1540820470.2; __utmz=183398822.1540820470.2.2.utmcsr=hotel.qunar.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqa=1.1157585471331556400.1540814763.1540814763.1540820473.2; _jzqx=1.1540814763.1540820473.2.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.jzqsr=hotel%2Equnar%2Ecom|jzqct=/render/ga_new%2Ejsp; QN205=organic; QN277=organic; csrfToken=8FsIHF1UkES6qtY6Jv3rZYwPnstV4lcC; QN163=0; QN71="MjIzLjY1LjE4OC4xMDU65rGf6IuPOjE="; Hm_lvt_15577700f8ecddb1a927813c81166ade=1540815577,1540861723,1541418695,1541578932; _vi=UHwM1GeuKHUlPThfFGTdmypChNnDt7UANSJ4z3X0XSvb5dEz8FaEx19j1s4xnm0jaGDv-zp7UnalfAoYIKdkJwYaZMeYgluEioo56jpJmbtFp8e3OJmq9Y8d6hLXpyCM7cGIrlW15Tvxb3GyTddDe_PpB-gr37MJsISeabzWBYsb; QN267=1952087195d7368a97; QN58=1541578932026%7C1541580444807%7C6; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1541580445; QN271=693db26f-e770-4040-9b8f-9cec7ae4d00a; JSESSIONID=593FE41CD6EFB237A646E1E0BDB480BD; Request-Node=d1a745dffdf82e1ac1545f9ecd9137ea; QN63=%E5%A8%81%E6%B5%B7%7C%E6%B1%9F%E9%97%A8%7C%E6%B1%9F%E8%8B%8F%7C%E4%BA%94%E6%8C%87%E5%B1%B1%7C%E5%9B%9B%E5%B7%9D%7C%E9%BB%91%E9%BE%99%E6%B1%9F%7C%E5%B9%BF%E8%A5%BF%7C%E6%B5%B7%E5%8D%97%7C%E5%8F%B0%E6%B9%BE%7C%E5%86%85%E8%92%99%E5%8F%A4%7C%E9%99%95%E8%A5%BF%7C%E5%B1%B1%E8%A5%BF%7C%E7%94%98%E8%82%83%7C%E9%9D%92%E6%B5%B7%7C%E8%BE%BD%E5%AE%81'
    ]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': random.choice(coo),
        'Host': 'piao.qunar.com',
        'Referer': 'http://piao.qunar.com/ticket/list.htm?keyword=%E6%88%90%E9%83%BD&region=null&from=mpl_search_suggest',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(url, headers=headers).text
    c = '您操作的行为好像机器人哦～'
    if c in r:
        cap(r)
    soup = BeautifulSoup(r, 'lxml')
    s = soup.find('div', class_='result_list')
    return s

if __name__=='__main__':
    start=time.time()

    #pages=[57,98,52,97,41,87,143,24,18,106,21,41,88,59,70,50]
    pro = ['湖南', '湖北', '广东', '广西', '河南', '河北', '山东', '山西', '江苏', '浙江', '江西', '黑龙江', '新疆', '云南', '贵州', '福建', '吉林', '安徽',
           '四川', '西藏', '宁夏', '辽宁', '青海', '甘肃', '陕西', '内蒙古', '台湾', '海南']

    pages = [92, 104, 150, 84, 112, 136, 150, 81, 150, 150, 67, 63, 57, 98, 52, 97, 41, 87, 143, 24, 18, 106, 21, 41,
             88,59, 70, 50]
    for p,pagess in zip(pro[21:],pages[21:]):
        print('开始抓取%s' % p)
        df = pandas.DataFrame()
        for page in range(1,pagess+1):
            print('开始抓取%d' % page)
            time.sleep(random.randint(2,5))
            #print(page)
            url = 'http://piao.qunar.com/ticket/list.htm?keyword=' + parse.quote(p) + '&region=null&from=mpl_search_suggest&page=' + str(page)
            #print(url)
            s = t(url)
            #s=s.find_all('div',class_='sight_item')
            #v=s.find_all('div',class_='sight_item sight_itempos')

            try:
                for i in s:
                    inf = {}
                    try:
                        inf['level'] = i.find('span', class_='level').text[0]
                    except Exception as e:
                        inf['level'] = '0'
                    try:
                        inf['price'] = i.find('span', class_='sight_item_price').find('em').text
                    except Exception as e:
                        inf['price'] = ''
                    try:
                        inf['name'] = i.find('a', class_='name').text
                    except Exception as e:
                        inf['name'] = ''
                    try:
                        inf['num'] = i.find('span', class_='hot_num').text
                    except Exception as e:
                        inf['num'] = ''
                    try:
                        inf['add_pro'] = i.find('span', class_='area').find('a').text.split('·')[0]
                        inf['add_city'] = i.find('span', class_='area').find('a').text.split('·')[1]
                    except  Exception as e:
                        inf['add_pro'] = i.find('span', class_='area').find('a').text
                        inf['add_city'] = i.find('span', class_='area').find('a').text
                    try:
                        inf['hot'] = i.find('span', class_='product_star_level').find('em').get('title').split(':')[1]
                    except  Exception as e:
                        inf['hot'] = ''
                    try:
                        inf['descri'] = i.find('div', class_='intro color999').text
                    except Exception as e:
                        inf['descri'] = ''
                    df = df.append(inf, ignore_index=True)
            except Exception as e:
                get_inf(url)
            print(df)
        df.to_csv('qunaer.csv', index=False, mode='a', header=False,columns=['add_pro','add_city','name','level','price','num','hot','descri'],encoding='utf-8')
        time.sleep(60)
    end=time.time()
    print('一共用时%d'%(end-start))
