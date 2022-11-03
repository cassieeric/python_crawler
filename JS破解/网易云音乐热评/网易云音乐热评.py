# coding: utf-8
"""
1、找到未加密的参数
2、想办法把参数进行加密（必须参考网易逻辑），params，encSecKey
3、请求到网页，抓取评论信息
"""
import requests
# 需要安装pycrypto库，用于AES加密，安装命令：pip install pycryptodome
from Crypto.Cipher import AES
from base64 import b64encode
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
songId = 1325905146

# 请求方式：POST
# 经过解析发现：params _-> encText, encSecKey --> encSecKey
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": f"R_SO_4_{songId}",
    "threadId": f"R_SO_4_{songId}"
}

# 这些参数都是服务与加密函数的，window.asrsea，其中i可以在网页中查到，然后写死
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "PvLgW8IKGXQDWBsm"


def get_encSecKey():  # 由于i是固定的，所以encSecKey是固定的
    return "5757f6675f9df72e1d15570d55554f85378efb20855b54670e12b10fbd4339d48ec7156d91f5bc8c62082eba565720c7b1b1c0036589802cd1f884d2cf0cfe9a4070dbb203abd22d9f88dfc60b15ba171098d68431b7f54e65e24dd76a34917180025bf942d128ca281223b4eedca94c008deb0e8352576ae50e3e65e3b6387b"


def get_params(data):  # data默认是字符串
    first_enc = enc_params(data, g)
    second_enc = enc_params(first_enc, i)
    return second_enc  # 返回的就是params


def to_16(data):  # 转化成16的倍数，为下发的加密算法服务
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创建加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密，加密的内容长度必须是16的倍数
    return str(b64encode(bs), "utf-8")  # 转化位字符串返回


# 处理加密过程，window.asrsea
"""
    function a(a) {  # a=16，随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环a次，即16次
            e = Math.random() * b.length,  # 随机数 * b的长度
            e = Math.floor(e),  # 取e的整数，e = "010001"，即1
            c += b.charAt(e);  # 取字符串中的xxx位置 b
        return c
    }
    # AES加密算法要三个参数：原文、密钥和偏移量，其中iv是偏移量，e是原文，所以反推c是加密的密钥，而c由b得到，所以b是密钥
    function b(a, b) {  # a：需要加密的数据
        var c = CryptoJS.enc.Utf8.parse(b) # b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708") 
          , e = CryptoJS.enc.Utf8.parse(a) # 得到的结果e是通过对a进行加密得到的
          , f = CryptoJS.AES.encrypt(e, c, {  # c是加密的密钥
            iv: d,  # AES加密算法中的偏移量
            mode: CryptoJS.mode.CBC  # 模式是：CBC
        });
        return f.toString()
    }
    function c(a, b, c) {  # 函数c()不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d:数据，e:010001，f:很长， g:0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);  # 往上找a，输出16位的随机值，在浏览器里边打短短的，可以找到i的值，"PvLgW8IKGXQDWBsm"，给它写死
        return h.encText = b(d, g), # d是原文，g是密钥
        h.encText = b(h.encText, i),  # 得到的就是params，加密过程，分两次进行加密，第一次是b(d, g)，之后将该加密得到的
        结果再次和i进行b(第一次加密的结果, i)加密，通过b函数分析，可以得到第一次加密的结果是原文，i是密钥
        h.encSecKey = c(i, e, f),  # 得到的就是encSecKey，其中e和f是定值，
        是写死的，唯一变化的是i，即a(16)，里边有随机值，如果将i固定写死，那么c()函数输出的值，也是定值，得到的encSecKey也是定值，以此来破解
        h
    }
    window.asrsea = d,
    var bKf6Z = window.asrsea(JSON.stringify(i8a), bva3x(["流泪", "强"]), bva3x(Tu8m.md), bva3x(["爱心", "女孩", "惊恐", "大笑"]));
    
    把bva3x(["流泪", "强"])丢到浏览器控制台，输出：010001
    把bva3x(Tu8m.md)丢到浏览器控制台，输出：
    00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
    把bva3x(["爱心", "女孩", "惊恐", "大笑"])到浏览器控制台，输出：0CoJUm6Qyw8W8jud
    d: 数据, 010001, 上面那张长的数字和字母组合 , 0CoJUm6Qyw8W8jud
"""

# 发送请求
response = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})
print(response.json())

