主要的文件为：
  微博评论_简.py : 利用python爬取微博评论
  
运行环境：
  Python3.6
  
需要安装的包：
  headers_raw_to_dict
  BeautifulSoup
  requests
  time
  random
  re
注：公众号对应文章为《分析30万条微博评论，看毕业生与翟天临的爱恨情仇》

注：因为爬取微博主页 https://weibo.com/ 或者 https://m.weibo.cn/ 较为困难，所以我爬取了 https://weibo.cn，这是一个落后的塞班年代的网页，没有混淆等等一系列新技术，用户动态等从html里面就可以获取，爬取相对来说比较简单。
希望对大家能够有所参考。 思路参考了这篇文章：https://weibo.cn/comment/HgCfidCUs?uid=1343887012&rl=0&page=1，在此非常感谢作者
