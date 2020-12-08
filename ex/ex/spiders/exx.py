import scrapy
import re
from bs4 import BeautifulSoup

class ExxSpider(scrapy.Spider):
    name = 'exx'
    #allowed_domains = ['xueqiu.com/S/SH600000']
    start_urls = ['http://xueqiu.com/S/']

    def parse(self, response):
        list=['SH600000','SZ300045','SZ300765']
        for i in list:
            url='http://xueqiu.com/S/'+i
            yield  scrapy.Request(url,callback=self.parse_stock)

    def parse_stock(self,response):
        infoDict = {}
        name = re.search(r'<div class="stock-name">(.*?)</div>', response.text).group(1)
        infoDict.update({'股票名称': name.__str__()})
        tableHtml = re.search(r'"tableHtml":"(.*?)",', response.text).group(1)
        soup = BeautifulSoup(tableHtml, "html.parser")
        table = soup.table
        for i in table.find_all("td"):
            line = i.text
            l = line.split("：")  # 这里的冒号为中文的冒号(：)!!!而不是英文的(:)
            infoDict.update({l[0].__str__(): l[1].__str__()})
        yield infoDict
        pass
