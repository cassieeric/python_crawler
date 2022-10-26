# 爬取三国演义小说所有的章节标题和内容
import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    # 对首页页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers, verify=False).text.encode("latin1").decode("utf-8")
    # 在首页中解析出章节标题和详情页的url
    # 实例化BeatifulSoup对象，需要将野马源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        print(title)
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        # 对详情页发起请求，解出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        # 解析出详情页的相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_="chapter_content").text.encode("latin1").decode("utf-8","ignore")
        print(div_tag)
        # 解析到了章节的内容
        fp.write(title + ':' + div_tag + '\n')
        print(title, '下载成功！！！')
