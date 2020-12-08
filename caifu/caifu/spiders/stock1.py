import scrapy
import re
from bs4 import BeautifulSoup
import pickle
from scrapy.http import TextResponse


class Stock1Spider(scrapy.Spider):
    name = 'stock1'
   # allowed_domains = ['q.10jqka.com.cn']
    start_urls = ['http://q.10jqka.com.cn/']


    def _parse(self, response):
        list=[]
       #response = TextResponse(url=response.url, body=response.body, encoding='utf-8')
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.search(r"/\d{6}/", href).group(0)
                list.append(stock)
                '''with open('g.txt','a+')as f:
                    f.write(stock)
                    f.write('\n')  # ‘\n’ 表示换行'''
            except:
                continue
        list = ','.join(list)
        with open ('g.txt','w')as f:
            f.write(list)


