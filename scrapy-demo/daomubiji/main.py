# _*_ coding:UTF-8 _*_

"""
Created on 2017/3/13 20:52
@author: evan
"""
from scrapy import cmdline

# cmdline.execute("scrapy crawl quotes -o r.json".split())

cmdline.execute("scrapy crawl daomubiji".split())
