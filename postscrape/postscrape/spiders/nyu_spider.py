import scrapy

from ..items import UniItem

class NewYorkSpider(scrapy.Spider):
    name = 'nyu'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.nyu.edu/academics/academic-programs.html']
    def parse(self, response):
        for programList in response.css("div.main-content div div.nyurichtexteditor.parbase.section")[2:-3]:
            for sublist in programList.css("div div ul li"):
                items = UniItem()
                program = sublist.css("a::text").get()
                if program is None:
                    program = sublist.css("::text").get()
                items['program'] = program
                items['school_id'] = 22
                yield items