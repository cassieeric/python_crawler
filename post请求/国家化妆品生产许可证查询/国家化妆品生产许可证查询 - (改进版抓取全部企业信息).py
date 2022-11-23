# coding: utf-8
import requests
import json


def request(params):
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"}
    request = requests.post(url=url, params=params, headers=headers)
    response = request.json()
    return response


def get_id(page):
    params = {
        "on": "true",
        "page": page,  # 可以修改，对应页面
        "pageSize": 15,
        "productName": "",
        "conditionType": 1,
        "applyname": "",
        "applysn": ""
    }

    response = request(params=params)
    # print(response)
    for item in response["list"]:
        id = item["ID"]
        get_detail_info(id)
        break  # 这里只是用了一个数据做测试


def get_detail_info(id):
    params = {"id": id}
    response = request(params=params)["list"]
    # print(response)
    save_data(response)


def save_data(response):
    fp = open("./huazhuanpin.json", "w", encoding="utf-8")
    json.dump(response, fp=fp, ensure_ascii=False)


if __name__ == "__main__":
    for page in range(1, 5):
        get_id(page)
        print(f"Page {page} write over!")
