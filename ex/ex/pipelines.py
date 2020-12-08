# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ExPipeline:
    def process_item(self, item, spider):
        return item
class stockPipeline(object):
    def open_spider(self,spider):#使用爬虫时
        self.f = open('XueQiuStock.txt','w')#打开文件

    def close_spider(self,spider):#爬虫结束时
        self.f.close()#关闭文件

    def process_item(self,item,spider):#处理item
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item
