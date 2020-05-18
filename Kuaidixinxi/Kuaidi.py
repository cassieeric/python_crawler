import urllib.request
import json

kd_dict = {1: 'shentong', 2: 'youzhengguonei', 3: 'yuantong', 4: 'shunfeng', 5: 'yunda', 6: 'zhongtong'}


class YU(object):
    def Check():
        while True:
            print("输入要查询快递公司:")
            print("1.申通  2.EMS邮政  3.圆通 4.顺风5.韵达6.中通0.退出\n ")

            choose = int(input("请选择您的快递公司:"))
            while choose not in range(0, 7):
                choose = int(input("抱歉暂不支持此公司请重新选择:"))
            if choose == 0:
                print("感谢使用!\n")
                break
            kd_num = input("请输入快递单号:")
            url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[choose], kd_num)
            response = urllib.request.urlopen(url)
            html = response.read().decode('utf-8')
            target = json.loads(html)
            status = target['status']
            if status == '200':
                data = target['data']
                # print(data)
                data_len = len(data)
                # print(data_len)
                # print("\n")
                for i in range(data_len):
                    print("\n时间: " + data[i]['time'])
                    print("状态: " + data[i]['context'] + "")
                print("\n感谢使用!\n")
                break
            else:
                print("输入有误请重新输入!\n")
    # print("按任意键结束......")


if __name__ == '__main__':
    while True:
        YU.Check()
        out = input("按任意数字退出(其他键继续).........")
        if out >= '0' and out <= '7':
            break
        else:
            print("\n")
            continue
