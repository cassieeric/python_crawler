import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random

class TianTangWebsite(object):
    def __init__(self):

        self.url = "https://www.ivsky.com/bizhi/1920x1080/index_{}.html"
        # 初始化url地址 重构构造头
        self.film_list = []
        ua = UserAgent(verify_ssl=False)

        for i in range(1, 50):
                self.headers = {
                    'User-Agent': ua.random
                }
        # print(self.headers)

    def get_home(self, url):
            html = requests.get(url=url, headers=self.headers).content.decode("utf-8")
            # print(html)
            self.xiap(html)

    def xiap(self,html):
        h = etree.HTML(html)
        ha = h.xpath("//ul[@class='ali']//li/div//a//@href")
        for a in ha:
         q="https://www.ivsky.com" + a
         #print(q)# 一级页面的网站
         self.tow(q)

    def tow(self,q):
        html1 = requests.get(url=q, headers=self.headers).content.decode("utf-8")
        #print(html1)#请求二级页面
        self.tow_get(html1)

    def tow_get(self,html1):
        qe= etree.HTML(html1)
        #print(qe)
        ha =qe.xpath("//ul[@class='pli']//li/div//a//@href")

        for i in ha:
            w = "https://www.ivsky.com"+i
            # print(w)
            # 二级页面获取
            self.teree_get(w)

    def teree_get(self,w):
        html1 = requests.get(url=w, headers=self.headers).content.decode("utf-8")
        #print(html1)
        self.tetee_xp(html1)

    def tetee_xp(self,html1):
        qe = etree.HTML(html1)
        # print(qe)
        ha = qe.xpath("//img[@id='imgis']/@src")
        he = qe.xpath("//img[@id='imgis']/@alt")
        # print(he)
        for q in he:
            # print(q)
             pass
        for i in ha:
           r="https:/" +i[1:]
           #print(r)
           html2 = requests.get(url=r, headers=self.headers).content
           filename = "./天堂网爬的图片/" + q[:-5]+r[-6:]
           print(filename)
           with open(filename, 'wb') as f:
               f.write(html2)
               print("%s下载成功" % filename)

    def main(self):
        for i in range(1,2):  #页数随机客户随便 设置
          url=self.url.format(i)
          #print(url)
          html=self.get_home(url)
          time.sleep(random.randint(1, 3))
          print('第%d提取成功！！！' % i)


if __name__ == '__main__':
    spider =TianTangWebsite()
    spider.main()
