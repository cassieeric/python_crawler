# coding: utf-8

import requests
from Crypto.Cipher import AES
import aiohttp
import aiofiles
import asyncio


async def aio_download():
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("second.m3u8", 'r', encoding="utf-8") as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                # print(line)
                name = line.rsplit("/", 1)[1]  # 从右边开始切, 切一次 取得[1]位置的内容
                task = download_ts(line, name, session)
                tasks.append(asyncio.create_task(task))
            await asyncio.wait(tasks)
        print("所有的ts文件已经下载完成！")


"""
直接使用download()函数进行下载，可以下载成功，但是文件是打不开的，因为该视频是加密过的，需要进行解密
加密方式在m3u8文件中的
#EXT-X-KEY:METHOD=AES-128,URI="https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/key.key"
可以看到是AES-128加密方法，使用的key.key，可以在响应中看得到，这里是：50aa1c78cad9eb8d
有了加密方法和密钥，就可以进行破解了
思路步骤
1、目前我们已经拿到了视频播放路径，接下来就可以下载视频
2、下载密钥，进行解密操作
3、合并所以的ts文件为一个mp4文件
"""


async def download_ts(url, name, session):
    async with session.get(url) as response:
        aes = AES.new(key.encode("utf-8"), AES.MODE_CBC, key.encode("utf-8"))  # 通过秘钥新建解密器
        async with aiofiles.open("temp_videos/%s" % name, "wb") as f:
            content = aes.decrypt(await response.content.read())
            await f.write(content)
        print("%s下载完成" % name)


if __name__ == '__main__':
    key = "50aa1c78cad9eb8d"
    asyncio.run(aio_download())
