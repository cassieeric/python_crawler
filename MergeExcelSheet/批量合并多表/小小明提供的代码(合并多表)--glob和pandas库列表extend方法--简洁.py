# -*- coding: utf-8 -*-
import glob
import pandas as pd
path = r"E:\PythonCrawler\python_crawler-master\MergeExcelSheet\file"
data = []
# for excel_file in glob.glob(f'{path}/**/[!~]*.xlsx'):
for excel_file in glob.glob(f'{path}/[!~]*.xlsx'):
    dfs = pd.read_excel(excel_file, sheet_name=None).values()
    data.extend(dfs)
print(data)

df = pd.concat(data, ignore_index=True)
df.to_excel("小小明提供的代码(合并多表)--glob和pandas库列表extend方法--简洁--所有表合并.xlsx", index=False)
print("合并完成!")
