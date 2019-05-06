# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class MusicDoubanItem(Item):
    title = Field()
    score = Field()
    tag = Field()
    url = Field()
    abstract = Field()
    pic_src = scrapy.Field()
    music_title=scrapy.Field()
    music_content=scrapy.Field()
    pass
