#爬取王者荣耀的皮肤
#先使用通用爬虫
import requests
from lxml import etree
import os
url = 'https://pvp.qq.com/web201605/herolist.shtml'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
response = requests.get(url=url,headers=headers)
#手动设定响应数据的编码格式
#response.encoding = 'utf-8'
response = response.text
#数据解析：href的属性值    以及alt的

tree = etree.HTML(response)
li_list = tree.xpath('//ul[@class="herolist clearfix"]/li')
new_url_list= []
#创建一个文件夹
if not os.path.exists('./王者荣耀英雄'):
    os.mkdir('./王者荣耀英雄')
for li in li_list:
    # 获取每个英雄的url
    new_url = 'https://pvp.qq.com/web201605/'+li.xpath('./a/@href')[0]  # 保留没啥作用
    img_src = 'https:'+li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    # 通用处理中文乱码的解决方案
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_data = requests.get(url=img_src, headers=headers).content
    img_path = '王者荣耀英雄/'+img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, '下载成功！！！！')
