import scrapy
from scrapy import Request

from MusicDouban.items import MusicDoubanItem  # 引入item


class InputmysqlSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ['https://www.douban.com/search?cat=1003&q=%E5%91%A8%E6%9D%B0%E4%BC%A6']

    def start_requests(self):
        yield Request("https://www.douban.com/search?cat=1003&q=%E5%91%A8%E6%9D%B0%E4%BC%A6",
                      headers={
                          'User-Agent': "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"})

    def parse(self, response):
        total = response.css('div.result')
        item = MusicDoubanItem()  # 实例化item类
        for v in total:  # 循环获取每一条名言里面的：名言内容、作者、标签
            item['abstract']=v.css('p::text').extract()
            item['title']=v.css('a::text').extract()
            item['score']=v.css('span.rating_nums::text').extract()
            item['tag']=v.css('span.subject-cast::text').extract()
            item['url']=str(v.css('h3>a').extract()).split(';')[0].split('"')[1]
            item['pic_src']=str(v.css('a>img').extract()).split('"')[1]

            yield scrapy.Request(item['url'],callback=self.parse_detail,meta={'item':item},headers={
                          'User-Agent': "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}) # 把取到的数据提交给pipline处理

    def parse_detail(self,response):
        item=response.meta['item']
        item['music_title']=response.xpath('//*[@id="wrapper"]/h1/span').extract()
        item['music_content']=response.xpath('//*[@id="link-report"]/span[2]/text()').extract_first()
        yield  item