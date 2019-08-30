import requests
from lxml import etree
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

post_dict = {
    "channelid": "204408",
    "searchword": "白蚁防治",
    "keyword": "白蚁防治",
    "orderby": "-DocrelTime",
    "was_custom_expr": "doctitle=(白蚁防治)",
    "perpage": "10",
    "outlinepage": "10",
    "searchscope": "doctitle",
    "timescope": "",
    "timescopecolumn": "",
    "andsen": "",
    "total": "",
    "orsen": "",
    "exclude": ""
}

header_d = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

base_url = "http://www.ccgp-jiangsu.gov.cn/was5/web/search"


def writeExcel2():
    wb = Workbook()
    sheet = wb.create_chartsheet("demo_sheet", index=0)
    # 添加一行
    row = [1, 2, 3, 4, 5]
    sheet.append(row)
    wb.save("demo.xlsx")


def sss(data):
    """传入的是一个一个条目"""
    # html = data.xpath("./")
    for tr in data:
        # 链接
        link = tr.xpath(".//a/@href")[0]
        # link = base_url + link
        # 标题
        title = tr.xpath("string(.//a)")
        # 时间
        ctime = tr.xpath(".//div[@class='pubtime']//text()")[0]
        # print(link,title,ctime)
        with open("xx.txt", "a", encoding="utf-8") as f:
            w_str = "===>".join([link, title, ctime])
            f.write(w_str + "\n")


if __name__ == '__main__':
    for i in range(1, 13):
        post_dict["page"] = i
        r1 = requests.get(url=base_url,params=post_dict , headers=header_d)
        # print(r1.text)
        html = etree.HTML(r1.text)
        li_list = html.xpath("//ol/li")
        # print(li_list)
        sss(li_list)
