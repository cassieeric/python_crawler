# -*- coding: utf-8 -*-
import requests
url = "https://b2c.csair.com/portal/flight/direct/query"
data = {
    "depCity": "CAN",
    "arrCity": "PKX",
    "flightDate": "20210423",
    "adultNum": "1",
    "childNum": "0",
    "infantNum": "0",
    "action": "0",
    "airLine": 1,
    "cabinOrder": "0",
    "cache": 0,
    "flyType": 0,
    "international": "0",
    "isMember": "",
    "preUrl": "",
    "segType": "1"
}

response = requests.post(url=url, json=data)
print(response.json())
