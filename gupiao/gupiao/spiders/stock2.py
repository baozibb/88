import scrapy
import re

class Stock2Spider(scrapy.Spider):
    name = 'stock2'
    #allowed_domains = ['q.10jqka.com.cn']
    start_urls = ['http://q.10jqka.com.cn/']

    def parse(self, response):
        list=[]
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.search(r"/\d{6}/", href).group(0)
                stock = stock.upper()
                list=list.append(stock)
            except:
                continue
        fname = response.url.split('/')[-1]
        with open(fname, 'wb')as f:
            f.write(list)
            self.log('save file %s.' % fname)