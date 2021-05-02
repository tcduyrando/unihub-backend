# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UniItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    country = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    imageURL = scrapy.Field()
    logoURL = scrapy.Field()
    tuition = scrapy.Field()
    tuitionUSD = scrapy.Field()
    website = scrapy.Field()

    name2 = scrapy.Field()
    location = scrapy.Field()
    score_ielts = scrapy.Field()
    score_toefl = scrapy.Field()
    score_sat = scrapy.Field()

    program = scrapy.Field()
    school_id = scrapy.Field()


