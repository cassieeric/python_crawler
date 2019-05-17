import time

# unix_time1 = int(time.mktime(time.strptime('2016-10-1 00:00:00', '%Y-%m-%d %H:%M:%S')))
# unix_time2 = int(time.mktime(time.strptime('2016-10-2 00:00:00', '%Y-%m-%d %H:%M:%S')))
# print(unix_time1)
# print(unix_time2)


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import netCDF4
from netCDF4 import Dataset
nc_obj = Dataset('D:\\皮皮猫数据\\tem_e0025_2.nc')


#查看nc文件有些啥东东
# print(nc_obj)
# print('---------------------------------------')

#查看nc文件中的变量，结果是：['lon', 'lat', 'lev', 'time', 'tem']
# print(nc_obj.variables.keys())
# for i in nc_obj.variables.keys():
#     print(i)
# print('---------------------------------------')

#查看每个变量的信息
# print(nc_obj.variables['lat'])
# print(nc_obj.variables['lon'])
# print(nc_obj.variables['lev'])
# print(nc_obj.variables['time'])
# print(nc_obj.variables['tem'])
# print('---------------------------------------')

#查看每个变量的属性
# print(nc_obj.variables['lat'].ncattrs())
# print(nc_obj.variables['lon'].ncattrs())
# print(nc_obj.variables['lev'].ncattrs())
# print(nc_obj.variables['time'].ncattrs())
# print(nc_obj.variables['tem'].ncattrs())
#
# print(nc_obj.variables['lat'].units)
# print(nc_obj.variables['lon'].units)
# print('---------------------------------------')


#读取数据值
lat = (nc_obj.variables['lat'][:])
# lon = (nc_obj.variables['lon'][:])
# lev = (nc_obj.variables['lev'][:])
# print(lev)
# time1 = (nc_obj.variables['time'][:])
# tem = (nc_obj.variables['tem'][:])
# lat = (nc_obj.variables['lat'][1:2])
# lon = (nc_obj.variables['lon'][1:2])
# lev = (nc_obj.variables['lev'][1:2])
# time1 = (nc_obj.variables['time'][1:2])
# tem = (nc_obj.variables['tem'][1:2])
print(lat)
print(len(lat))
# print(lon)
# print(lev)
# print(time1)
# print(len(time1))
# print(tem)
# print('---------------******-------------------')
# for i in tem:
#     print(i)
#
file = open('ppm_lat.txt', 'a')
# file.write('lat,lon,time1,tem'+'\n')
# file.write('lat,lon'+'\n')
file.write('lat'+'\n')
for i in range(len(lat)):
    file.write(str(lat[i])+',\n')
#     file.write(str(lon[i])+',')
# #     # file.write(str(lev[i])+',')
#     file.write(str(time1[i])+',')
#     file.write(str(tem[i])+',\n')
file.close()
