import requests
from lxml import etree
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

post_dict = {
    "searchKey": "%E7%99%BD%E8%9A%81%E9%98%B2%E6%B2%BB",
    "title": "",
    "str1": "undefined",
    "str2": "undefined",
    "cmsNews.title": "",
    "cmsNews.buyerName": "",
    "cmsNews.str2": "",
    "cmsNews.str3": "undefined",
    "cmsNews.str1": "",
    "cmsNews.str5": "",
    "cmsNews.str6": "",
    "cmsNews.str8": "undefined",
    "cmsNews.agentName": "",
    "cmsNews.startPubdate": "undefined",
    "cmsNews.endPubdate": "undefined",
    "cmsNews.district_id": "undefined"
}

header_d = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

base_url = "http://222.216.4.8"

def writeExcel2():
    wb = Workbook()
    sheet = wb.create_chartsheet("demo_sheet",index=0)
    # 添加一行
    row = [1,2,3,4,5]
    sheet.append(row)
    wb.save("demo.xlsx")

def sss(data):
    """传入的是一个一个条目"""
    # html = data.xpath("./")
    for tr in data:
        # 链接
        link = tr.xpath(".//a/@href")[0]
        link = base_url + link
        # 标题
        title = tr.xpath(".//a/@title")[0]
        # 时间
        ctime = tr.xpath(".//span//text()")[0]
        with open("xx.txt","a",encoding="utf-8") as f:
            w_str = "===>".join([link, title, ctime])
            f.write(w_str+"\n")


if __name__ == '__main__':
    for i in range(1, 26):
        url = f"http://222.216.4.8/CmsNewsController/search/chnlCodes-/distin-/beginDate-0/endDate-0/p-20/c-{i}/0-0.html"
        r1 = requests.post(url=url, data=post_dict, headers=header_d)
        # print(r1.text)
        html = etree.HTML(r1.text)
        li_list = html.xpath("//div[@id='channelBody']/div/ul/li")
        # print(li_list)
        sss(li_list)