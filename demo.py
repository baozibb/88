import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    start_urls = ['http://python123.io/']

    def parse(self, response):
        fname=response.url.split('/')[-1]
        with open ('jj.txt','wb')as f:
            f.write(response.body)

