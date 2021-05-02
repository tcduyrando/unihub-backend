import scrapy

from ..items import UniItem

class PrincetonSpider(scrapy.Spider):
    name = 'princeton'

    start_urls = ['https://www.princeton.edu/academics/areas-of-study']
    def parse(self, response):
        for programList in response.css("li.row.small-collapse"):
            items = UniItem()
            program = programList.css("a h2::text").get()
            items['program'] = program
            items['school_id'] = 6
            yield items

    # start_urls = ['https://www.princeton.edu/academics/areas-of-study']
    # def parse(self, response):
    #     for program in response.css("li.row.small-collapse"):
    #         yield {
    #             'program' : program.css("a h2::text").get()
    #         }