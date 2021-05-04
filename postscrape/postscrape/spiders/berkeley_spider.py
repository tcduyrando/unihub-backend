import scrapy

from ..items import UniItem

class BerkeleySpider(scrapy.Spider):
    name = 'berkeley'

    # other info are scraped by goToUniversity

    start_urls = ['http://guide.berkeley.edu/undergraduate/degree-programs/']
    def parse(self, response):
        for programList in response.css("ul.program-thumb-list li"):
            items = UniItem()
            program = programList.css("a span::text").get()
            items['program'] = program
            items['school_id'] = 11
            yield items