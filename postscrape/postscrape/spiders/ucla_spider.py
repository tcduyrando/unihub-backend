import scrapy

from ..items import UniItem

class UCLASpider(scrapy.Spider):
    name = 'ucla'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.ucla.edu/academics/departments-and-programs']
    def parse(self, response):
        for programList in response.css("div.dept-list"):
            for sublist in programList.css("ul.link-column"):
                items = UniItem()
                program = sublist.css("li a::text").get()
                items['program'] = program
                items['school_id'] = 16
                yield items
