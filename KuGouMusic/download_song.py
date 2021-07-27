import requests
import json

res = "https:\/\/webfs.yun.kugou.com\/202006040913\/734fff99fbcf7ab914c4b2a6e2e30f34\/G098\/M05\/17\/15\/og0DAFkFT32AYczCAEEg0_QmDU0558.mp3"
req_song_url = res.replace("\\", "")
song = requests.get(req_song_url, timeout=4)
with open("不谓侠.mp3", "wb") as f:
	f.write(song.content)
print("歌曲已经下载完成！")
