[Introduction]
This folder is mainly designed to process .nc file, a complex file with complex data structure.

reference link:
1. https://blog.csdn.net/showpingzhang/article/details/83384780
2. https://www.cnblogs.com/shoufengwei/p/9068379.html

nc 全称 netCDF（The Network Common Data Form），可以用来存储一系列的数组，就是这么简单（参考https://www.unidata.ucar.edu/software/netcdf/docs/netcdf_introduction.html）。

既然 nc 可以用来一系列的数组，所以经常被用来存储科学观测数据，最好还是长时间序列的。

试想一下一个科学家每隔一分钟采集一次实验数据并存储了下来，如果不用这种格式存储，时间长了可能就需要创建一系列的 csv 或者 txt 等，而采用 nc 一个文件就可以搞定，是不是很方便。

更方便的是如果这个科学实验与气象、水文、温度等地理信息稍微沾点边的，完全也可以用 nc 进行存储， GeoTiff 顶多能多存几个波段（此处波段可以认为是气象、水文等不同信号），而 nc 可以存储不同波段的长时间观测结果，是不是非常方便。
