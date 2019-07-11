[Introduction]
This folder is about lichuangshangcheng website, source link:https://www.szlcsc.com/catalog.html.

[Content]
In order to collect all related information or data on the website, a web crawler script is generated.
The website is not easy, in which the first page is loaded in 'get' request, and the other pages is loaded in 'post' request.
In other words, the first page is very easy, but the left pages is loaded in JS status.
Therefore, we should deal with those website pages in different method.
Finally, the collected data is stored in Excel.

[Sugestion]
1. In order to improve the data collection speed, multi-threading and multi-process is developed in the program.
2. The website https://list.szlcsc.com/catalog/439.html contains nearly 35000 piece of data. Thus, a specific program nameed lichuang_439_multi_thread.py is assigned to collect data from the website, in which multi_thread is appied and improved the collect speed.

[remark]
2019/5/22, the website change some tags, the former script cannot be used to collect data from the website.
Thus, script is modified this day and is efficicy to collect data from wenbsite.
