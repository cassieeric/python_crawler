import requests
import parsel
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
def get_page(page):
    url='https://www.kuaidaili.com/free/inha/'+str(page)
    response=requests.get(url,headers=headers)
    # 数据类型转换
    html = parsel.Selector(response.text)
    parse_page(html)

def parse_page(html):
    #XPath的匹配范围
    parse_list = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    for tr in parse_list:
        parse_lists = {}
        http=tr.xpath('./td[@data-title="类型"]//text()').extract_first()
        num=tr.xpath('./td[@data-title="IP"]//text()').extract_first()
        port=tr.xpath('./td[@data-title="PORT"]//text()').extract_first()
        parse_lists[http]=num+':'+port
        time.sleep(0.1)
        print(parse_lists)

if __name__ == '__main__':
    for page in range(1,3):
        get_page(page)
