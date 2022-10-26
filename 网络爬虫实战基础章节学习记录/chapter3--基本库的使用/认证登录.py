import urllib.request

url = "http://tieba.baidu.com"
user = "test_user"
passwd = "test_passwd"
pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None, url, user, passwd)
auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
opener = urllib.request.build_opener(auth_handler)
response = opener.open(url)
print(response.read().decode("utf-8"))
