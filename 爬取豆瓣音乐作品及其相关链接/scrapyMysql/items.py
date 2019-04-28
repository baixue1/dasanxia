
import scrapy


class ScrapymysqlItem(scrapy.Item):
    title=scrapy.Field()
    score=scrapy.Field()
    tag=scrapy.Field()
    url=scrapy.Field()
    abstract = scrapy.Field()
    pic_src=scrapy.Field()
    # 名言内容
    pass
