import scrapy

from ..items import UniItem

class JohnsHopkinsSpider(scrapy.Spider):
    name = 'johnsHopkins'

    # other info are scraped by goToUniversity

    start_urls = ['https://e-catalogue.jhu.edu/programs/']
    def parse(self, response):
        for programList in response.css("div.filter-items ul li"):
            for tag in programList.css("a div span"):
                if tag.css("::text").get() == "Bachelor's":
                    items = UniItem()
                    program = programList.css("a div span.title::text").get()
                    items['program'] = program
                    items['school_id'] = 13
                    yield items
                    break
