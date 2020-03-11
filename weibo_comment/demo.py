import requests
import json
import time
import emoji
import schedule

def job():
    print("当前时间::"+time.strftime("%Y-%m-%d", time.localtime(time.time()))+' '+time.strftime("%H:%M:%S",time.localtime(time.time())))
    with open('1.txt', 'r') as f:
        file = f.read()
    for i in range(1, 17):
        print('第{0}页'.format(i))
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }

        if i == 1:
            url = 'https://m.weibo.cn/comments/hotflow?id=4480264908680491&mid=4480264908680491&max_id_type=0'
        else:
            url = 'https://m.weibo.cn/comments/hotflow?id=4480264908680491&mid=4480264908680491&max_id={0}&max_id_type=0'.format(max_id)
        cookie = {
            'Cookie': ''  #填自己的cookie数据
        }
        response = requests.get(url, headers=header, cookies=cookie)
        text = json.loads(response.text)['data']
        max_id = text['max_id']
        comments = text['data']
        for j in comments:
            comment = j['text']   #评论内容
            name = j['user']['screen_name']   #评论者昵称
            created_at = j['created_at']   #评论时间
            #print(name, created_at, comment)
            if comment in file:
                pass
            else:
                try:
                    with open('1.txt', 'a') as f:
                        f.write(name, created_at, comment+ '\n')
                except:
                    pass

schedule.every(30).minutes.do(job)
job()
while True:
    schedule.run_pending()


