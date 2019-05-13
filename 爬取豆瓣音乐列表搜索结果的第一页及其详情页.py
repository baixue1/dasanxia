# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.utils.response import get_base_url
from urllib.parse import urljoin

from MusicDouban.items import MusicDoubanItem  # 引入item


class InputmysqlSpider(scrapy.Spider):
    name = "a"
    allowed_domains = ["douban.com"]
    start_urls = ['https://www.douban.com/search?cat=1003&q=%E5%BC%A0%E6%83%A0%E5%A6%B9']

    def start_requests(self):
        yield Request("https://www.douban.com/search?cat=1003&q=%E5%BC%A0%E6%83%A0%E5%A6%B9",
                      headers={
                          'User-Agent': "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"})

    def parse(self, response):
        #total = response.css("div.result")
        for v in response.css("div.result"): # 循环获取每一条名言里面的：名言内容、作者、标签
            item = MusicDoubanItem()  # 实例化item类
            item["abstract"]=v.css("div.content>p::text").extract_first()
            item["title"]=v.css("div.content>div.title>h3>a::text").extract_first()
            item["score"]=v.css("div.content>div.title>div.rating-info>span.rating_nums::text").extract_first()
            item["tag"]=v.css("div.content>div.title>div.rating-info>span.subject-cast::text").extract_first()
            item["url"]=str(v.css('h3>a').extract()).split(';')[0].split('"')[1].split('&')[0]
            #url=v.css("div.content>div.title>h3>a::attr(herf)").extract_first()
            item["pic_src"]=v.css("div.pic>a>img::attr(src)").extract_first()
            item["numbers"]=v.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[8]/div[2]/div/div/span[3]/text()').extract_first()
            #items.append(item)
            #base_url = get_base_url(response)
            #abs_url = urljoin(base_url, item['url'])
            yield scrapy.Request(item["url"], callback=self.parse_detail, meta={"item":item},
                    headers={
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}) # 把取到的数据提交给pipline处理
            #yield item
    def parse_detail(self,response):
        item=response.meta["item"]
        item["music_content"]=response.xpath('//*[@id="link-report"]/span[2]/text()').extract()
        item["music_song"]=response.xpath('//*[@id="content"]/div/div[1]/div[3]/div[3]/div/div/div/text()').extract()
        yield  item
