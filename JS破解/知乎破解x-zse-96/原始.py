import requests
import execjs
import hashlib

x_zse_93 = "101_3_2.0"
url = "/api/v4/search_v3?t=general&q=%E6%80%8E%E4%B9%88%E8%BF%BD%E5%A5%B3%E4%BA%BA&correction=1&offset=60&limit=20&filter_fields=&lc_idx=60&show_all_topics=0&search_hash_id=81c19f67a763a1f0b65713b8137bb7d5&vertical_info=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0"
d_c0 = '"AKAe53MC8RKPTgO1uWOMLu15ReaRphJjaes=|1618191524"'
x_zst_81 = "3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7AuyE8FxS_FZ16PqbL_BJvxOiqXTt4S1Fve97LO_DrxTxQLYLhSfiRPp26kqBL2ZeqefnCOsgrxM1wXTD6Uq6ufXe8FmtGwTdiUZQXFPLbXTBGomH9L1VUnPQ6fqwXxmAqHK-cXPjTf08hkKFHRhHRH1F0k80CY1ChLGk7xBaDOq4GpYoUVO-rx1IgNByq2Ljcr0AbeOZwCm8hF0XvO9F0kwhuCKthS0Ccx0Oq2uc9e1ywS82egLSJOmWDpO49FLcbU99Cw_6HeYcgLqVhxBoBoBDDoYhcO0LhSMkGNBwCNGJUYCcJS9UUeYQTpBtDL1EueYChXseQNC"

referer = "https://www.zhihu.com/topic/19731651/hot"

f = "+".join([x_zse_93, url, d_c0, x_zst_81])
fmd5 = hashlib.new('md5', f.encode()).hexdigest()

with open('g_encrypt.js', 'r', encoding='utf-8') as f:
    ctx1 = execjs.compile(f.read(), cwd=r'D:\soft\Install Packages\node-v12.16.1-win-x64\node-v12.16.1-win-x64\node_modules')
encrypt_str = "2.0_%s" % ctx1.call('b', fmd5)

print(encrypt_str)

headers = {
    # ":authority": "www.zhihu.com",
    # ":method": "GET",
    # ":path": "/api/v4/search_v3?t=general&q=%E6%80%8E%E4%B9%88%E8%BF%BD%E5%A5%B3%E4%BA%BA&correction=1&offset=60&limit=20&filter_fields=&lc_idx=60&show_all_topics=0&search_hash_id=81c19f67a763a1f0b65713b8137bb7d5&vertical_info=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0",
    # ":scheme": "https",
    # "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br",
    # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "referer": "https://www.zhihu.com/search?type=content&q=%E6%80%8E%E4%B9%88%E8%BF%BD%E5%A5%B3%E4%BA%BA",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "cookie": '_xsrf=EKWAOiwYsl5bULDhtEdNhRXgkwhRrO1G; _zap=753540a5-d865-4152-a372-8ccdec51f118; d_c0="AKAe53MC8RKPTgO1uWOMLu15ReaRphJjaes=|1618191524"; captcha_session_v2="2|1:0|10:1633860255|18:captcha_session_v2|88:ekRVams1UXBhbG9DWUFwbmt6c0pqc2YyOWR3Wm9IM0tCRDhHSWcwUnJhTm5rUU5Cd0FXZmk4VFdvWDZkMlBVQQ==|0495fb1dcd0983306ba6e4561d64017e104148e9a08a551abdda3e0ec96d5559"; gdxidpyhxdE=cX6N%2F2EBg%2BLDymvvRo%2FNXYavpHWtrVu7PH%2FUn9yXL8%2Bhys6rxJjQSM4ZU5sO6t5LcZZdequK5QQyXXaGI5XZQEe33OVNTdeg03h3CARuC5AOoudpTJCP2jE1i3Bm%5CKVZCJLj5h76bxxdm7osPdrN4ALzTO9eVt1Dp%2Bp1M56rpw3ak9Ht%3A1633861160031; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=0AP145MgFBs0BP2MHy5iVc2XyfvBMiwQ6SyUg04ZEbxf%2Bj6DKmO%2FvlYYfXxSaMnf0tMGzgh1MY0Fp0ezbbkDNtjGiL4Jr31jdNDtix2D6vwySYEc8X0K5LO9u8F%2BvNMPYVM%3D; YD00517437729195%3AWM_TID=F3azwRqesi1EEAARFEdqsGmT2dcW0Qv6; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb6e521abafa986e26bb7b48aa7d15f969e9babae7988b69c8fe74388a89e96b52af0fea7c3b92af49fa0d2b73f8fb98aa3f23c8290feaecb73f7b79a84b154bbbabaa3d063b58ffab4fc5fa5f0fcbbc86abcbae58bb55089b381d0f5689b87aab9fb59a393a287b3808f99b688eb3b8f8700a7f33ca7a6ae83ea508eaca6a8ec48f896bed4b462a8928c95ec74f29cfa97f67391878b84bb54f495fbadce33b7e88accf5468f9097b7d037e2a3; captcha_ticket_v2="2|1:0|10:1633860587|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfc3FZNjBfTVdGU3g5bllDNUF1MlBHWjl1SzE5VGhDOFdGVER4YUJERWhxb0pvVWcwUFlfTFZtZE1YRnZ5Uld5bFhCekg4R3BMR0xXdUlCYTBZWEY1QThRWXZ2blRzVVlJc0hReE5wYk9LMGJUNVd5NzhQbnJPempGSUctQm9MbTJLT0lGRGJTRXhPNXhqQ3IxR1oyVW9kVHo4Z3M5WU92WlBXcDc5RHQ5TDJkZDJ5aGcubU9jYVRVWm1fU1U1bDR6OC5xWVBHOGtaR041Zy5YZ3d6NlJ5bDZSU2Rxc2JLa0p0MEtxLUNIVXdXLUxrN3IxNjUtVlc1WGxWN0N4dkloVlFQU2NfZGRGUk5IQTU5bHNzVFktY19sV1IyZHMuSTRJRVVmS0R3UVhHVi1zczl5MUlsejhoa29LSzhNQUhIeC5FeGsyMUVTTGZyai1JU0xUbHJ0WW9xSHpKUTZlVEVMcnNRU0JHNmdFLngtS2FoSEZWWmZzekpoVzJ1Q1lDY1ctSV9wSVZSYnB2d2VMeXcwTFBMcGI4RzYxeGpsUEJqenltLWtHbzZfWXg2YU1KMXB4Q3FGam9jNHdtTEJRd01sejE1UFRQSFNiamgta3FsNEl3TzgwekxYZEFwbmEyNHAxb1NaWDlRTkhrSE13b2tmRllCLi5lMUJJSTJxMyJ9|cb69363fc103244bead9823346688dcd30c81d52e8b8c6a781efae7e56ff330c"; z_c0="2|1:0|10:1633860636|4:z_c0|92:Mi4xcHU5UEJRQUFBQUFBb0I3bmN3THhFaVlBQUFCZ0FsVk5Hd3BRWWdEUFJtakx4WUhYczhwVnBjX2p1M1dQVm81M2V3|74aefe61a0fd1e437572b9d780467a0e60b51a678e1e9c05729769f6248364be"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1635145288,1635256615,1635316550,1635494606; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1635507940; NOT_UNREGISTER_WAITING=1; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1635507941|1635494605',
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
