from pathlib import Path
import pandas as pd

path = Path(r'E:\PythonCrawler\python_crawler-master\MergeExcelSheet\file\888')
pd.concat([pd.concat(pd.read_excel(i, sheet_name=None)) for i in path.glob("[!~]*.xls*")],
          ignore_index=True).to_excel("result.xlsx", index=False)

print('合并完成!')
