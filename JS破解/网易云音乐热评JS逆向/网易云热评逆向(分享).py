# coding:utf-8
import requests
from Crypto.Cipher import AES
import json
from base64 import b64encode


e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "YFyUfYPqkwTxJmqw"


def get_encSecKey():
    return "a1d20abe686c0e0ce0f283b38c17a97ef51692de77764772aeebc0b3af425ee8dfa4506b7c208fc4c750f9082854d24dc675589b2e7f698833a79304c71245c25054f41ae71edb670f79eb5001b237f62e73e27dae63166a0b8ad5cfc52f57c6dc469164860702be46cc74d498837eb18d22618fd13d866faaad0df7aa7e9a54"


def to_16(data):
    pad = 16 - len(data) % 16
    data += pad * chr(pad)
    return data


def enc_params(data, key):
    iv = "0102030405060708"
    aes = AES.new(key=key.encode("utf-8"), iv=iv.encode("utf-8"), mode=AES.MODE_CBC)
    data = to_16(data)
    encrypted_data = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(encrypted_data), "utf-8")  # 转化位字符串返回


def get_params(data):
    first_enc = enc_params(data, g)
    second_enc = enc_params(first_enc, i)
    return second_enc


def get_comment(data):
    response = requests.post(url, data={
        "params": get_params(json.dumps(data)),
        "encSecKey": get_encSecKey()
    })
    print(response.json())


if __name__ == '__main__':
    url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
    song_id = 1325905146
    data = {
        "csrf_token": "",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "pageNo": "1",
        "pageSize": "20",
        "rid": f"R_SO_4_{song_id}",
        "threadId": f"R_SO_4_{song_id}"
    }
    get_comment(data)

