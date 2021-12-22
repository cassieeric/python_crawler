# -*- coding: utf-8 -*-
import glob
import pandas as pd
path = "E:\\PythonCrawler\\python_crawler-master\\MergeExcelSheet\\file\\"
data = []
for excel_file in glob.glob(f'{path}/**/[!~]*.xls*'):
# for excel_file in glob.glob(f'{path}/[!~]*.xlsx'):
    excel = pd.ExcelFile(excel_file)
    for sheet_name in excel.sheet_names:
        df = excel.parse(sheet_name)
        data.append(df)
# print(data)

df = pd.concat(data, ignore_index=True)
df.to_excel("小小明提供的代码(合并多表)--glob和pandas库列表append方法--所有表合并.xlsx", index=False)
print("合并完成!")
