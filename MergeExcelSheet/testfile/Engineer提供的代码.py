# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import glob

root = tk.Tk()
root.withdraw()

# 选择文件夹位置
filelocation = os.path.normpath(filedialog.askdirectory(initialdir=os.getcwd()))
lst = []

# 读取文件夹下所有文件（xls和xlsx都读取）
for i in glob.glob(filelocation + "\\\\" + "*.*"):
    if os.path.splitext(i)[1] in [".xls", ".xlsx"]:
        lst.append(pd.read_excel(i))

# 保存合并后的excel文件
writer = pd.ExcelWriter(filedialog.asksaveasfilename(title="保存", initialdir=filelocation, defaultextension="xlsx",
                                                     filetypes=[("Excel 工作簿", "*.xlsx"),
                                                                ("Excel 97-2003 工作簿", "*.xls")]))
pd.concat(lst).to_excel(writer, 'all', index=False)
writer.save()

print('\n%d个文件已经合并成功！' % len(lst))
