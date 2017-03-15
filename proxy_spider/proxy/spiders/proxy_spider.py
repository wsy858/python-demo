# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

import re

from proxy.items import ProxyItem

REG_IP = re.compile(
    r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))[^\d]*((\d){1,5})',
    re.M)


# Spider for http proxy
class ProxySpider(CrawlSpider):
    name = "Proxy"
    start_urls = [
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy",
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy&pn=10",
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy&pn=20",
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy&pn=30",
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy&pn=40",
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy&pn=50",
        r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy&pn=60",
        r"https://www.sogou.com/web?query=ip+proxy&cid=&page=1&ie=utf8&p=40040100&dp=1&w=01029901&dr=1",
        r"https://www.sogou.com/web?query=ip+proxy&cid=&page=2&ie=utf8&p=40040100&dp=1&w=01029901&dr=1",
        r"https://www.sogou.com/web?query=ip+proxy&cid=&page=3&ie=utf8&p=40040100&dp=1&w=01029901&dr=1",
        r"https://www.sogou.com/web?query=ip+proxy&cid=&page=4&ie=utf8&p=40040100&dp=1&w=01029901&dr=1",
        r"https://www.sogou.com/web?query=ip+proxy&cid=&page=5&ie=utf8&p=40040100&dp=1&w=01029901&dr=1",
    ]

    # start_urls = [
    #     r"http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip%20proxy"
    # ]

    rules = (
        Rule(LinkExtractor(allow=(r'',)), callback='parse_item'),
    )

    def parse_item(self, response):
        soup = BeautifulSoup(response.body)
        str_list = [tag.string or '' for tag in soup.find_all(True)]
        body_str = ' '.join(str_list)
        items = [ProxyItem(ip=group[0], port=group[7], protocol='HTTP') for group in re.findall(REG_IP, body_str)]
        return items
