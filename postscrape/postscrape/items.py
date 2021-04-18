# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UniItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    location = scrapy.Field()
    admissionWeb = scrapy.Field()
    name2 = scrapy.Field()
    tuition = scrapy.Field()
    website = scrapy.Field()

