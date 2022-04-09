import requests
import re
import time


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Referer": "http://fund.eastmoney.com/data/fundranking.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
}

url = "http://fund.eastmoney.com/data/rankhandler.aspx"
for page in range(1, 43):
    params = {
        "op": "ph",
        "dt": "kf",
        "ft": "gp",
        "rs": "",
        "gs": "0",
        "sc": "6yzf",
        "st": "desc",
        "sd": "2021-04-08",
        "ed": "2022-04-08",
        "qdii": "",
        "tabSubtype": ",,,,,",
        "pi": f"{page}",
        "pn": "50",
        "dx": "1",
        "v": f"0.38359385261686{page}5"
    }
    cookies = {
        "qgqp_b_id": "a6906bb649195e01a7bb6db16c0b3edc",
        "HAList": "a-sz-002104-%u6052%u5B9D%u80A1%u4EFD",
        "em_hq_fls": "js",
        "intellpositionL": "1010.67px",
        "intellpositionT": "1522.33px",
        "_adsame_fullscreen_16928": "1",
        "st_si": "02250267371185",
        "st_asi": "delete",
        "ASP.NET_SessionId": "emt5ff3viukq43baatgl1y0v",
        "_adsame_fullscreen_18503": "1",
        "EMFUND1": "null",
        "EMFUND2": "null",
        "EMFUND3": "null",
        "EMFUND4": "null",
        "EMFUND5": "null",
        "EMFUND6": "null",
        "EMFUND7": "null",
        "EMFUND8": "null",
        "EMFUND0": "null",
        "EMFUND9": "04-08 14:41:12@#$%u6C47%u6DFB%u5BCC%u4E2D%u8BC1%u4E2D%u836F%u6307%u6570%28LOF%29A@%23%24501011",
        "st_pvi": "39261719988158",
        "st_sp": "2021-08-25%2016%3A00%3A59",
        "st_inirUrl": "https%3A%2F%2Fwww.baidu.com%2Flink",
        "st_sn": f"{page}",
        "st_psi": "20220408144112400-112200305282-7152262518"
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    pattern = re.compile(r'.*?"(?P<items>.*?)".*?', re.S)
    result = re.finditer(pattern, response.text)
    ids = []
    for item in result:
        # print(item.group('items'))
        gp_id = item.group('items').split(',')[0]
        # print(gp_id)
    #     # gp_name = item.group('items').split(',')[1]
    #     # print(gp_id, gp_name)
        ids.append(gp_id)
        print(f"股票：{gp_id}已经生成")

    with open("gp.txt", 'a', encoding='utf-8') as f:
        for id in ids:
            f.write(f"{id}\n")

    print("休息2秒钟...")
    time.sleep(2)


