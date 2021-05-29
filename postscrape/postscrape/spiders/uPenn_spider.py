import scrapy

from ..items import UniItem

class UPennsylvaniaSpider(scrapy.Spider):
    name = 'uPenn'

    # other info are scraped by goToUniversity

    start_urls = ['https://catalog.upenn.edu/programs/']
    def parse(self, response):
        for programList in response.css("div.filter-items ul li"):
            tags = programList.css("a span.keyword::text")
            if len(tags) == 4:
                if tags[0].get() == "Undergraduate":
                    if tags[1].get() == "Bachelor's":
                        if tags[3].get() == "Major":
                            items = UniItem()
                            program = programList.css("a span.title::text").get()
                            items['program'] = program
                            items['school_id'] = 14
                            yield items

