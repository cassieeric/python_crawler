# -*- coding: utf-8 -*-
import os
import pandas as pd
new_excel = pd.DataFrame()
path = r"E:\\PythonCrawler\\python_crawler-master\\MergeExcelSheet\\testfile\\file"
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if name.endswith(".xls") or name.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(root, name), sheet_name=None)
            new_excel.append(df)

new_excel.to_excel("所有表合并--pandas中的append.xlsx", index=False)
print("合并完成!")
