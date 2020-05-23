import requests, json
from fake_useragent import UserAgent
import csv


class Doban(object):
    u = 0;

    def __init__(self):
        self.film_list = []
        ua = UserAgent(verify_ssl=False)
        self.url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}"
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random # ua 构造随机请求头
            }

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        if res.status_code == 200:
            return html
        '''解析数据'''

    #
    # '''获取链接函数'''
    def parse_page(self, html):
        # 创建csv文件进行写入
        csv_file = open('scr.csv', 'a', encoding='gbk')
        csv_writer = csv.writer(csv_file)
        # 写入csv标题头内容
        csv_writer.writerow(['电影', '评分', "详情页"])
        data = json.loads(html)['subjects']
        # print(data[0])
        for r in data:
            # print(r)
            rate = r["rate"]
            id = r["title"]
            src = r["url"]
            urll = r["cover"]
            csv_writer.writerow([id, rate, urll])
            html2 = requests.get(url=urll, headers=self.headers).content
            dirname = "./图/" + id + ".jpg"
            with open(dirname, 'wb') as f:
                f.write(html2)
                print("%s 【下载成功！！！！】" % id)

        csv_file.close()

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1, 20):
            url = self.url.format(page)
            # print(url)
            html = self.get_page(url)
            self.u += 1
            self.parse_page(html)
            print("======================第%s页爬取成功！！！！=======================" % str(self.u))


if __name__ == '__main__':
    Siper = Doban()
    Siper.main()
