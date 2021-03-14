
import pandas as pd

def main():
   # 读入表1
   df1 = pd.read_csv('D:/a/1.csv', encoding='gbk')
   # 读入表2
   df2 = pd.read_excel('D:/a/2.xlsx', encoding='utf-8')
   # 关联数据
   data = df1.merge(df2, on='姓名',left_index=False, right_index=False, sort=False)
   # 保存数据
   data.to_csv('D:/a/result.csv', encoding='gbk', index=False)

if __name__ == '__main__':
    main()
