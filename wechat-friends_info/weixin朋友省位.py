# -*- coding: utf-8 -*-
import itchat
import pandas as pd

itchat.login()
friends = itchat.get_friends(update=True)
df_friends = pd.DataFrame(friends)
Province = df_friends.Province
Province_count = Province.value_counts()
# 有一些好友地理信息为空，过滤掉这一部分人。
Province_count = Province_count[Province_count.index != '']
print(Province_count)

