import requests
from lxml import etree
import time


def get_fund_info(url):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Referer": "http://fund.eastmoney.com/data/fundranking.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
    }
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        selectors = etree.HTML(response.text)
        # fundInfoItem = selectors.xpath('//div[@class="fundInfoItem"]')
        danweijingzhi1 = selectors.xpath('//dl[@class="dataItem02"]/dd[1]/span[1]/text()')[0]
        danweijingzhi2 = selectors.xpath('//dl[@class="dataItem02"]/dd[1]/span[2]/text()')[0]
        leijijingzhi = selectors.xpath('//dl[@class="dataItem03"]/dd[1]/span/text()')[0]
        # jijin_leixing = selectors.xpath('//div[@class="infoOfFund"]//text()')
        lst = selectors.xpath('//div[@class="infoOfFund"]/table//text()')
        leixing = lst[1]
        fengxian = lst[2].replace('|', '').strip()
        guimo = lst[4].replace('：', '')
        jingli = lst[6]
        chengrili = lst[8].replace('：', '').strip()
        guanliren = lst[11]
        pingji = lst[13].replace('：', '')
        genzongbiaodi = lst[-3].replace('|', '')
        genzongwucha = lst[-1]
        with open('jijin_info.csv', 'a', encoding='utf-8') as f:
            f.write(f"{danweijingzhi1}, {danweijingzhi2}, {leijijingzhi}, {leixing}, "
                    f"{fengxian}， {guimo}, {jingli}, {chengrili}, {guanliren}, "
                    f"{pingji}, {genzongbiaodi}, {genzongwucha}\n")
        print(danweijingzhi1, leixing, fengxian, chengrili)
    except:
        print(f'这个链接有点问题：{url}')
        pass


if __name__ == '__main__':
    with open('gp.txt', mode='r', encoding='utf-8') as f:
        for gp_id in f.readlines():
            url = f"http://fund.eastmoney.com/{gp_id.strip()}.html"
            print(f"开始抓取链接:{url}")
            get_fund_info(url)
            print('休息2秒...')
            time.sleep(2)



