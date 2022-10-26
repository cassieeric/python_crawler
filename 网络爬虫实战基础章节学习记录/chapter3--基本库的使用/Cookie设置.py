import http.cookiejar
import urllib.request

url = "http://tieba.baidu.com"
fileName = "cookie.txt"

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(url)
print(cookie)
f = open(fileName, 'a')
for item in cookie:
    f.write(item.name + "=" + item.value + "\n")
f.close()
