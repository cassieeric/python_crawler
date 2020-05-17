import requests, json, os
from lxml import etree
from fake_useragent import UserAgent


class wzry(object):
    def __init__(self):
        os.mkdir("王者")  # 创建王者荣耀这个文件夹 记住只有第一次运行加上，如果多次运行请注释掉本行
        # 随机UserAgent，防止反爬。
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }

    def wzry(self):
        response = requests.get('https://pvp.qq.com/web201605/js/herolist.json', headers=self.headers)
        content = response.text  # 这里后获取的是json数据类型需要 转换成Python对应类型
        data = json.loads(content)
        for i in data:
            hero_number = i['ename']  # 获取英雄名字编号
            hero_name = i['cname']  # 获取英雄名字
            os.mkdir("././王者/{}".format(hero_name))  # 创建英雄对应的文件夹
            response_src = requests.get("https://pvp.qq.com/web201605/herodetail/{}.shtml".format(hero_number),
                                        headers=self.headers)
            hero_content = response_src.content.decode('gbk')  # 返回相应的html页面
            hero_data = etree.HTML(hero_content)  # xpath解析对象
            hero_img = hero_data.xpath('//div[@class="pic-pf"]/ul/@data-imgname')  # 提取每个英雄的皮肤名字
            hero_src = hero_img[0].split('|')
            print(hero_src)  # 去掉每个皮肤名字中间的分隔符
            # 遍历英雄src处理图片名称。
            for i in range(len(hero_src)):
                i_num = hero_src[i].find("&")

                skin_name = hero_src[i][:i_num]
                #print(skin_name)
                # 皮肤图片地址请求
                response_skin = requests.get(
                    "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg".format(
                        hero_number, hero_number, i + 1))
                skin_img = response_skin.content  # 获取每个皮肤图片
                # 把皮肤图片存储到对应名字的文件里
                with open("./王者/{}/{}.jpg".format(hero_name, skin_name), "wb")as f:
                    f.write(skin_img)  # 把皮肤图片存储到对应名字的文件里
                    print("%s.jpg 下载成功！！" % (skin_name))

    def main(self):
        self.wzry()

if __name__ == '__main__':
    Siper = wzry()
    Siper.main()
