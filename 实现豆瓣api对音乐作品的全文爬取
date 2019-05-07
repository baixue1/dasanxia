# coding=gbk
import re

import scrapy
from scrapy import Request
from doubanmusic.items import DoubanmusicItem  # 引入item
from urllib.request import urlopen  # 用于获取网页
from bs4 import BeautifulSoup  # 用于解析网页


class doubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ['https://www.douban.com/j/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&start=0&cat=1003']
    url1= 'https://www.douban.com/j/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&start=20&cat=1003'
    url2= 'https://www.douban.com/j/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&start=40&cat=1003'

    pageNum = 0

    def start_requests(self):
        yield Request("https://www.douban.com/j/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&start=0&cat=1003",
                      headers={
                          'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
                          'host':'www.douban.com',
                          'cookie':'bid=z98swn3gBkc; douban-fav-remind=1; __yadk_uid=lcJaQGq0UhGWeoFWXYA8WGFslr8LY38f; gr_user_id=8b06bbfd-e386-4ae2-9ee4-7e57a57838ff; _vwo_uuid_v2=DCB2A919BE7C473DB6D631966CA4BA1CB|30132d627e9b705afe1c11cde7c6a7d1; ll="118318"; dbcl2="176460967:Z2H8Ccuwq/8"; push_doumail_num=0; __utmv=30149280.17646; push_noty_num=0; __gads=ID=dd0dcc8fb9e0ce70:T=1556467745:RT=1556467969:S=ALNI_MZkAeBVn5H4OvAhBejpDVQS8xu_VA; __utmz=30149280.1556530531.16.9.utmcsr=music.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/subject_search; __utmc=30149280; viewed="27150869_1851862_1420204_26290565_1401853_1403307_27946814_26332342_27084137"; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1557125267%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject_search%3Fsearch_text%3D%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%26start%3D30%22%5D; _pk_id.100001.8cb4=8b4f8543af45f472.1537762043.20.1557125267.1557068297.; __utma=30149280.90453483.1538316411.1557068201.1557125280.23',
                          'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                          'Accept-Encoding':'gzip, deflate, br',
                          'Accept-Language':'zh,zh-CN;q=0.9,en;q=0.8',
                          'Cache-Control':'max-age=0',
                          'Connection':'keep-alive',
                          'Upgrade-Insecure-Requests':'1'
                      })

    def parse(self, response):
        item=DoubanmusicItem()
        print('爬第：%d 页' % self.pageNum)
        item['title']=str(response.text)
        yield  item


        # 多url， 请求的手动发送
        if self.pageNum ==0:  # 控制！否则无限递归了。。
            self.pageNum += 1
            print('爬第：%d 页' % self.pageNum)
            # callback 回调函数，页面进行解析
            yield scrapy.Request(url=self.url1, callback=self.parse,headers={
                          'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
                          'host':'www.douban.com',
                          'cookie':'bid=z98swn3gBkc; douban-fav-remind=1; __yadk_uid=lcJaQGq0UhGWeoFWXYA8WGFslr8LY38f; gr_user_id=8b06bbfd-e386-4ae2-9ee4-7e57a57838ff; _vwo_uuid_v2=DCB2A919BE7C473DB6D631966CA4BA1CB|30132d627e9b705afe1c11cde7c6a7d1; ll="118318"; dbcl2="176460967:Z2H8Ccuwq/8"; push_doumail_num=0; __utmv=30149280.17646; push_noty_num=0; __gads=ID=dd0dcc8fb9e0ce70:T=1556467745:RT=1556467969:S=ALNI_MZkAeBVn5H4OvAhBejpDVQS8xu_VA; __utmz=30149280.1556530531.16.9.utmcsr=music.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/subject_search; __utmc=30149280; viewed="27150869_1851862_1420204_26290565_1401853_1403307_27946814_26332342_27084137"; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1557125267%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject_search%3Fsearch_text%3D%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%26start%3D30%22%5D; _pk_id.100001.8cb4=8b4f8543af45f472.1537762043.20.1557125267.1557068297.; __utma=30149280.90453483.1538316411.1557068201.1557125280.23',
                          'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                          'Accept-Encoding':'gzip, deflate, br',
                          'Accept-Language':'zh,zh-CN;q=0.9,en;q=0.8',
                          'Cache-Control':'max-age=0',
                          'Connection':'keep-alive',
                          'Upgrade-Insecure-Requests':'1'})

        if self.pageNum ==1:  # 控制！否则无限递归了。。
            self.pageNum += 1
            print('爬第：%d 页' % self.pageNum)
            # callback 回调函数，页面进行解析
            yield scrapy.Request(url=self.url2, callback=self.parse,headers={
                          'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
                          'host':'www.douban.com',
                          'cookie':'bid=z98swn3gBkc; douban-fav-remind=1; __yadk_uid=lcJaQGq0UhGWeoFWXYA8WGFslr8LY38f; gr_user_id=8b06bbfd-e386-4ae2-9ee4-7e57a57838ff; _vwo_uuid_v2=DCB2A919BE7C473DB6D631966CA4BA1CB|30132d627e9b705afe1c11cde7c6a7d1; ll="118318"; dbcl2="176460967:Z2H8Ccuwq/8"; push_doumail_num=0; __utmv=30149280.17646; push_noty_num=0; __gads=ID=dd0dcc8fb9e0ce70:T=1556467745:RT=1556467969:S=ALNI_MZkAeBVn5H4OvAhBejpDVQS8xu_VA; __utmz=30149280.1556530531.16.9.utmcsr=music.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/subject_search; __utmc=30149280; viewed="27150869_1851862_1420204_26290565_1401853_1403307_27946814_26332342_27084137"; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1557125267%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject_search%3Fsearch_text%3D%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%26start%3D30%22%5D; _pk_id.100001.8cb4=8b4f8543af45f472.1537762043.20.1557125267.1557068297.; __utma=30149280.90453483.1538316411.1557068201.1557125280.23',
                          'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                          'Accept-Encoding':'gzip, deflate, br',
                          'Accept-Language':'zh,zh-CN;q=0.9,en;q=0.8',
                          'Cache-Control':'max-age=0',
                          'Connection':'keep-alive',
                          'Upgrade-Insecure-Requests':'1'})
