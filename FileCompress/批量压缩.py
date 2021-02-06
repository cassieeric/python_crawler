"""
    作者：崔艳飞
    名称：照片管理
    功能：根据照片名，自动移动到按时间分类的文件夹中，更新内容：自动获取目标文件夹名
    版本：V2.0
    日期：2019/12/16
"""
import os as os

import shutil

import zipfile

def del_(rootdir):
    filelist = []
    filelist = os.listdir(rootdir)  # 列出该目录下的所有文件名
    for f in filelist:
        filepath = os.path.join(rootdir, f)  # 将文件名映射成绝对路劲
        if os.path.isfile(filepath):  # 判断该文件是否为文件或者文件夹
            os.remove(filepath)  # 若为文件，则直接删除
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
    shutil.rmtree(rootdir, True)
def zipDir(dirpath,outFullName):
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()

def main():
    path_end = 'D:/a/h/'
    date= os.listdir(path_end)
    # 获取目标文件夹所有文件夹名列表
    for f in date:
        ljbc='D:/a/h/'+f+'/'+'查询信息.zip'
        ljbc2 = 'D:/a/h/' + f + '/' + '下发修改.zip'
        ljcx='D:/a/h/'+f+'/查询信息'
        ljxf = 'D:/a/h/' + f + '/下发修改'
        zipDir(ljcx,ljbc)
        zipDir(ljxf, ljbc2)
        del_(ljcx)
        del_(ljxf)
if __name__ == '__main__':
    main()