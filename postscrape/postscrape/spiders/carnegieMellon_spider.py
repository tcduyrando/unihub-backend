import scrapy

from ..items import UniItem

class CarnegieMellonSpider(scrapy.Spider):
    name = 'carnegieMellon'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.cmu.edu/academics/interdisciplinary-programs.html']
    def parse(self, response):
        for programList in response.css("div#bachelor-degrees div"):
            for sublist in programList.css("ul li"):
                items = UniItem()
                program = sublist.css("a::text").get()
                if program is None:
                    program = sublist.css("a span::text").get()
                program = program.replace('\xa0', ' ')
                items['program'] = program
                items['school_id'] = 23
                yield items