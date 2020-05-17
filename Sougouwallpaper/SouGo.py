import requests, json
from fake_useragent import UserAgent

class ShouGO(object):
    def __init__(self):
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,
            }
    def Shou(self, category, length, path):
        n = length
        cate = category
        imgs = requests.get(
            'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' + cate + '&tag=%E5%85%A8%E9%83%A8&start=0&len=' + str(
                n))
        jd = json.loads(imgs.text)
        jd = jd['all_items']
        imgs_url = []
        for j in jd:
            imgs_url.append(j['pic_url'])
        m = 0
        for img_url in imgs_url:
            # print(img_url)
            print('***** ' + cate + str(m) + '.jpg *****' + '   Downloading...')
            img = requests.get(url=img_url, headers=self.headers).content
            with open(path + cate + str(m) + '.jpg', 'wb') as f:
                f.write(img)
            m = m + 1
        print('Download complete!')

    def main(self):
        self.Shou('汽车', 2000, './壁纸2/')


if __name__ == '__main__':
    Siper = ShouGO()
    Siper.main()
