# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose
from w3lib.html import remove_tags


class BarstoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    restaurant = scrapy.Field()
    dave_score = scrapy.Field()
    #city_and_state = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    dave_visit_time = scrapy.Field()