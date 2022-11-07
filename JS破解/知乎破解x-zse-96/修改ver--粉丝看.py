# coding: utf-8
import requests
import execjs
import hashlib
from urllib import parse

key_word = "怎么追女人"
x_zse_93 = "101_3_2.0"
url = f"/api/v4/search_v3?t=general&q={parse.quote(key_word)}&correction=1&offset=20&limit=20&filter_fields=&lc_idx=20&show_all_topics=0&search_hash_id=81c19f67a763a1f0b65713b8137bb7d5&vertical_info=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0"
d_c0 = '你自己cookie上的d_c0'
x_zst_81 = "3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7AuyE8FxS_FZ16PqbL_BJvxOiqXTt4S1Fve97LO_DrxTxQLYLhSfiRPp26kqBL2ZeqefnCOsgrxM1wXTD6Uq6ufXe8FmtGwTdiUZQXFPLbXTBGomH9L1VUnPQ6fqwXxmAqHK-cXPjTf08hkKFHRhHRH1F0k80CY1ChLGk7xBaDOq4GpYoUVO-rx1IgNByq2Ljcr0AbeOZwCm8hF0XvO9F0kwhuCKthS0Ccx0Oq2uc9e1ywS82egLSJOmWDpO49FLcbU99Cw_6HeYcgLqVhxBoBoBDDoYhcO0LhSMkGNBwCNGJUYCcJS9UUeYQTpBtDL1EueYChXseQNC"

f = "+".join([x_zse_93, url, d_c0, x_zst_81])
fmd5 = hashlib.new('md5', f.encode()).hexdigest()

with open('g_encrypt.js', 'r', encoding='utf-8') as f:
    ctx1 = execjs.compile(f.read(), cwd=r'你自己的nodejs安装路径\node_modules')
encrypt_str = "2.0_%s" % ctx1.call('b', fmd5)
print(encrypt_str)

referer = f"https://www.zhihu.com/search?type=content&q={parse.quote(key_word)}"
headers = {
    "referer": referer,
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "cookie": "你自己完整的cookie",
    "x-ab-param": "tp_topic_style=0;zr_slotpaidexp=1;qap_question_author=0;se_ffzx_jushen1=0;tp_contents=1;tp_dingyue_video=0;pf_noti_entry_num=2;top_test_4_liguangyi=1;qap_question_visitor= 0;pf_adjust=1;tp_zrec=1;zr_expslotpaid=5",
    "x-ab-pb": "CsIBzALHAjMEjQQ3BVYF2AWMArQAOwLKArcD2gSABfQDpgSeBVADVQU3DNEEVwTgBH8FjAVPA6ID5wXsCuAL5Ap9ArkCMwW1C0AB1gTcC1IFiwWxBcEEQwB0AVYMmwvpBAsEFAWyBQ8LiQyMBBUFUQUOBYQCnwLXAjIDoAMKBGQEUgvjBEIEEgW0CjQEMgXXCykFGQXYAvgD9As0DD8AagFyA6EDQwXjBQcMEQVFBFcDdQTPC0cAGwD2AvMDwgVpAQELYAsSYQMAAAAAAAAAAQIAAAAAAAAAAAABBQEAAAAAAAABAAABFQEDAQAAAAADABUAAQIBAAIAAQAEAgEAAAEAAAABAQECAgEAAAAAAAAAAQAAAAABAAAAAQABAAALAAAAAAACAQA=",
    "x-api-version": "3.0.91",
    "x-app-za": "OS=Web",
    "x-requested-with": "fetch",
    "x-zse-93": x_zse_93,
    "x-zse-96": encrypt_str,
    "x-zst-81": x_zst_81
}
r = requests.get("https://www.zhihu.com" + url, headers=headers)
print(r.json())
