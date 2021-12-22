# -*- coding: utf-8 -*-
import os
import pandas as pd
result = []
path = r"E:\\PythonCrawler\\python_crawler-master\\MergeExcelSheet\\testfile\\file"
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if name.endswith(".xls") or name.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(root, name), sheet_name=None)
            result.append(df)

data_list = []
for data in result:
    # print(data.values())
    data_list.extend(data.values())  # 注意这里是extend()函数而不是append()函数

df = pd.concat(data_list)
df.to_excel("testfile所有表合并.xlsx", index=False)
print("合并完成!")
