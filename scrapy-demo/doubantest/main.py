# _*_ coding:UTF-8 _*_

"""
Created on 2017/3/13 20:52
@author: evan
"""
from scrapy import cmdline

# cmdline.execute("scrapy crawl quotes -o r.json".split())

# douban 指douban_test1.py文件中DoubanSpider类的name属性值
cmdline.execute("scrapy crawl douban".split())
