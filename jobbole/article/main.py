# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import os
import sys

# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jobbole'])
