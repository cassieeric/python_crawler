import requests
from lxml import etree


class ImageSpider(object):
    def __init__(self):
        self.firsr_url = "http://www.netbian.com/s/wangzherongyao/index.htm"
        self.url = "http://www.netbian.com/s/wangzherongyao/index_{}.htm"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("gbk")
        return html

    '''解析数据'''

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//div[@class="list"]/ul/li/a//@href')

        for image_src in image_src_list:
            fa = "http://www.netbian.com" + image_src
            # print(fa)
            html1 = self.get_page(fa)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)

            bimg_url = parse_html1.xpath('//div[@class="pic-down"]/a/@href')
            for i in bimg_url:
                diet = "http://www.netbian.com" + i
                # print(diet)
                html2 = self.get_page(diet)
                parse_html2 = etree.HTML(html2)
                # print(parse_html2)
                url2 = parse_html2.xpath('//table[@id="endimg"]//tr//td//a/img/@src')
                for r in url2:
                    pass
                    # print(r)
                filename = parse_html2.xpath('//table[@id="endimg"]//tr//td//a/@title')
                # print(url2)
                for e in filename:
                    # print(e)
                    dirname = "./王者荣耀/" + e + '.jpg'
                    html2 = requests.get(url=r, headers=self.headers).content
                    # print(html2)
                    print(dirname)
                    with open(dirname, 'wb') as f:
                        f.write(html2)
                        print("%s下载成功" % filename)

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            if page == 1:
                url = self.firsr_url

            else:
                url = self.url.format(page)
            # print(url)
            html = self.get_page(url)
            print("第%s页爬取成功！！！！" % page)
            # print(html)
            self.parse_page(html)


if __name__ == '__main__':
    imageSpider = ImageSpider()
    imageSpider.main()
