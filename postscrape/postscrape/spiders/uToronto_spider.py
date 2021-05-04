import scrapy

from ..items import UniItem

class UTorontoSpider(scrapy.Spider):
    name = 'uToronto'

    # other info are scraped by goToUniversity

    # NOT USED

    start_urls = ['https://www.utm.utoronto.ca/programs-departments/undergraduate-programs-departments']
    def parse(self, response):
        for programList in response.css("div.field-item.even ul")[0].css("li"):
            items = UniItem()
            program = programList.css("a::text").get()
            items['program'] = program
            items['school_id'] = 19
            yield items