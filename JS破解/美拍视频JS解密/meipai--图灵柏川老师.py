# coding:utf-8
import requests
from lxml import etree


# url = 'https://www.meipai.com/medias/hot'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
# response = requests.get(url=url, headers=headers).text
# html = etree.HTML(response)
# selector = html.xpath('//*[@id="mediasList"]/li')
# new_url_list = html.xpath('//div[@itemprop="name"]/a/@href')
# for url in new_url_list:
#     detail_video_url = 'https://www.meipai.com' + url
#
"""
心得：查找encode或者decode，如果在前端源码中都找不到的话，
试试看通过右上角的搜索框搜索：decodeMp4.decode，就可以找到JS了，打断点调试。
"""


"""
define("tool", function(a, b, c) {
    var d = a("jquery")
      , e = a("support")
      , f = a("constants")
      , g = a("base64")
      , h = "substring"
      , i = "split"
      , j = "replace"
      , k = "substr";
    b.decodeMp4 = {
        getHex: function(a) {
            return {
                str: a[h](4),
                hex: a[h](0, 4)[i]("").reverse().join("")
            }
        },
        getDec: function(a) {
            var b = parseInt(a, 16).toString();  # 对应Python中的str(int(a, 16))
            return {
                pre: b[h](0, 2)[i](""),
                tail: b[h](2)[i]("")
            }
        },
        substr: function(a, b) {
            var c = a[h](0, b[0])
              , d = a[k](b[0], b[1]);
            return c + a[h](b[0])[j](d, "")
        },
        getPos: function(a, b) {
            return b[0] = a.length - b[0] - b[1],
            b
        },
        decode: function(a) {
            var b = this.getHex(a)
              , c = this.getDec(b.hex)
              , d = this[k](b.str, c.pre);
            return g.atob(this[k](d, this.getPos(d, c.tail)))
        }
    };
"""
import base64


def getHex(a):
    return {
        "str": a[4:],  # JS中的substring(4)指的是从4开始取值到字符串末尾
        "hex": "".join(list(a[0:4])[::-1])  # [::-1]代表的是反向取值
    }


def getDec(a):
    b = str(int(a, 16))
    print(b)
    return {
        "pre": list(b[:2]),
        "tail": list(b[2:])
    }


def substr(a, b):
    c = a[0: int(b[0])]
    print(c)
    d = a[int(b[0]):int(b[0])+int(b[1])]
    print(d)
    return c + a[int(b[0]):].replace(d, '')


def getPos(a, b):
    b[0] = len(a) - int(b[0]) - int(b[1])
    print(b[0])
    return b


def decode(a):
    b = getHex(a)
    # print(b)
    c = getDec(b['hex'])
    print(c)
    # d = k(str(b), c.pre)
    d = substr(b['str'], c['pre'])
    # print(d)
    return base64.b64decode(substr(d, getPos(d, c['tail'])))


str1 = 'c0b1Ly9tdnPflQ3cQpPZpZGVvMTAubWVpdHVkYXRhLmNvbS82MWM0NDNlOGI1MmFmMTYzMi5tcDkBOyQ='
print(decode(str1).decode())
