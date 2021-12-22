# -*- coding: utf-8 -*-
import os
import pandas as pd
result = []
path = r"E:\\PythonCrawler\\python_crawler-master\\MergeExcelSheet\\testfile\\"
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if name.endswith(".xls") or name.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(root, name))
            result.append(df)
df = pd.concat(result)
df.to_excel("hebing.xlsx", index=False)
print("合并完成!")
