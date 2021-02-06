
import json
import requests
from lxml import etree

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
def main():
    response = requests.get('https://www.baidu.com/s?wd=粮食习近平&lm=1', headers=headers)
    r = response.text
    html = etree.HTML(r, etree.HTMLParser())
    r1 = html.xpath('//h3')
    r2 = html.xpath('//*[@class="c-abstract"]')
    r3 = html.xpath('//*[@class="t"]/a/@href')
    for i in range(10):
        r11 = r1[i].xpath('string(.)')
        r22 = r2[i].xpath('string(.)')
        r33 = r3[i]
        with open('ok.txt', 'a', encoding='utf-8') as c:
             c.write(json.dumps(r11,ensure_ascii=False) + '\n')
             c.write(json.dumps(r22, ensure_ascii=False) + '\n')
             c.write(json.dumps(r33, ensure_ascii=False) + '\n')
        print(r11, end='\n')
        print('------------------------')
        print(r22, end='\n')
        print(r33)


if __name__ == '__main__':
    main()

