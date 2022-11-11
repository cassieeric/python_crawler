import requests

# 只需要批量获取主页中的filecode进行替换即可实现批量下载
'''
js模型
versionOnClick("初稿", "20200609152829294C29C52C", "1")

function versionOnClick(version, filecode,versioncode)
{
	var page = new pageDefine("/txn210008.do", "下载文件");
	page.addValue( 20200609152829294C29C52C,"record:filecode");
	page.addValue( 初稿,"record:version");
	page.addValue( 1,"record:versioncode");
	page.downFile();
}

http://zhuce-original.nafmii.org.cn/txn210008.do?record:filecode=20200609152829294C29C52C&record:version=初稿&record:versioncode=1   #‘初稿’需要编码后，才可以访问，编码格式‘gbk’
'''

print(requests.utils.quote('初稿', encoding='gbk'))
headers = {
    'Cookie':'JSESSIONID=tXVGyyqlFLPHZmjRVPvw1tcX_YEtsb_-zGKjhsNnJPu01LN4BOFJ!-1183117201; SF_cookie_16=93462546; UM_distinctid=17e46ce9feb3a0-0aebc12f83d9c1-3b39580e-1fa400-17e46ce9fec6d1; CNZZDATA4530832=cnzz_eid%3D2012262324-1641862474-http%253A%252F%252Fzhuce-original.nafmii.org.cn%252F%26ntime%3D1641862474',
}
url = 'http://zhuce-original.nafmii.org.cn/txn210008.do?record:filecode=20200609152829294C29C52C&record:version=%B3%F5%B8%E5&record:versioncode=1'
r = requests.get(url, headers=headers, timeout=15)
# print(r.content)
with open("666.pdf", 'wb') as f:
    f.write(r.content)

print('down!')
