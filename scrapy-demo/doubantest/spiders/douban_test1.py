import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        print response.url
        print response.body
