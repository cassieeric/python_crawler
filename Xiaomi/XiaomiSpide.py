import requests
from threading import Thread
from queue import Queue
import json
import time


class XiaomiSpider(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=15&pageSize=30'
        # 定义队列，用来存放URL地址
        self.url_queue = Queue()

    # URL入队列
    def url_in(self):
        # 拼接多个URL地址,然后put()到队列中
        for i in range(67):
            self.url.format((str(i)))
            self.url_queue.put(self.url)

    # 线程事件函数(请求,解析提取数据)
    def get_page(self):
        # 先get()URL地址,发请求
        # json模块做解析
        while True:
            # 当队列不为空时,获取url地址
            if not self.url_queue.empty():
                url = self.url_queue.get()
                html = requests.get(url, headers=self.headers).text
                self.parse_page(html)
            else:
                break

    # 解析函数
    def parse_page(self, html):
        app_json = json.loads(html)
        for app in app_json['data']:
            # 应用名称
            name = app['displayName']
            # 应用链接
            link = 'http://app.mi.com/details?id={}'.format(app['packageName'])
            d = {'名称': name, '链接': link}
            print(d)

    # 主函数
    def main(self):
        self.url_in()
        # 存放所有线程的列表
        t_list = []

        for i in range(10):
            t = Thread(target=self.get_page)
            t.start()
            t_list.append(t)

        # 统一回收线程
        for p in t_list:
            p.join()


if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end - start))
