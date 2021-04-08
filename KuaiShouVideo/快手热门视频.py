import requests

def getData():

    url = 'http://apissl.gifshow.com/rest/n/feed/hot?isp=CMCC&mod=HUAWEI(DUK-AL20)&lon=121.492379&country_code=cn&kpf=ANDROID_PHONE&extId=b31ce9a7bacb2f567efe7aff2b7374b2&did=ANDROID_066f7438a673e208&kpn=KUAISHOU&net=WIFI&app=0&oc=XIAOMI&ud=561252472&hotfix_ver=&c=XIAOMI&sys=ANDROID_5.1.1&appver=6.6.6.10150&ftt=&language=zh-cn&iuid=&lat=31.247192&did_gt=1585204347787&ver=6.6&max_memory=192'

    data = 'type=7&page=1&coldStart=true&count=10&pv=false&id=27&refreshTimes=0&pcursor=&source=1&extInfo=Ql8KhQ1TWK3G%2FBbYoGCWMyeL5iDBfPA%2FidqooiNmt6Sv37LFyINoRqajhRM13g6jvLoVaFQw%2FC3VuLeniF%2Ft5uIEuVPBTdVWblmJF%2FVO%2BF5Li9n6yXafEiuGnWoFc9zvZgr4YkxHP9pltJvuTY410DjWMaCil2VEd36XsCZpmWw%3D&needInterestTag=false&browseType=1&seid=253e59e9-a137-42dd-b291-d957f43c8cf8&volume=0.73&backRefresh=false&__NStokensig=c4cb4271f3211c34c16d5cd834e98ebda150c6d957cb82bdf8e1a95ffeb304e2&kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAG2q0g-deb-tNjkILe6FTBSUwhf_6370CSDML5jTC-YDUhKtu4CRYvHyXm9wwmV1QAfyzb9TzHaVqol-DGyQLQFfZcfDc3IwVQ5lm5sQiaIwzk31MWR_BL6CXpncKcN3jdqNINZ0AEiBBft8RF8OgGRkK4K0Ia3jsH-M8Ur_jajTALiR5BQeEWSDyUtJy1vE48Gheu9i4prF6y3kVkvXJLFGhJey_IdJfJMt4oIXuVy7QAVNNEiIPGtBaWs1gYPdT7lm853QU351FcL0w-RSQ6bwUAxFxSzKAUwAQ&token=abd7df7449c64f46a562a313f74fc72d-561252472&client_key=3c2cd3f3&os=android&sig=29a919db9a8c66aff96c0e1e3dfc9031'

    headers = {
        'User-Agent': 'kwai-android',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    html = requests.post(url, data=data, headers=headers, timeout=5)
    print(html.text)

if __name__ == '__main__':
    getData()
