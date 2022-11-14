# coding: utf-8
"""
可以看到是AES-128加密方法，使用的key.key，可以在响应中看得到，这里是：50aa1c78cad9eb8d
有了加密方法和密钥，就可以进行破解了
"""
from Crypto.Cipher import AES
import subprocess


def decrpy_ts_file():
    with open("second.m3u8", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            name = line.split("/")[-1]
            # print(name)
            try:
                decrypt_file(name, key.encode("utf-8"))
            except:
                pass


# 解密数据
def decrypt_file(name, key):
    with open(f"videos/{name}", 'rb') as f1, open(f"temp_videos/temp_{name}", "wb") as f2:
        aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
        decrypted_file = aes.decrypt(f1.read())
        f2.write(decrypted_file)
    print(f"{name}解密完成")


def merge_file():
    command = r"copy/b E:\PythonCrawler\有趣的代码\m3u8视频下载\下载加密的m3u8视频\temp_videos\*.ts " \
              r"E:\PythonCrawler\有趣的代码\m3u8视频下载\下载加密的m3u8视频\movie.mp4"
    subprocess.getoutput(command)
    print("合并完成")


if __name__ == '__main__':
    key = "50aa1c78cad9eb8d"
    decrpy_ts_file()
    # merge_file()

