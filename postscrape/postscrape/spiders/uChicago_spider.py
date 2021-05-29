import scrapy

from ..items import UniItem

class UChicagoSpider(scrapy.Spider):
    name = 'uChicago'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.uchicago.edu/academics/programs_of_study/']
    def parse(self, response):
        for programList in response.xpath("//*[@id='undergrad']/table/tbody/tr"):
            items = UniItem()
            program = programList.css("td::text").get()
            items['program'] = program
            items['school_id'] = 8
            yield items

    # start_urls = ['https://www.uchicago.edu/academics/programs_of_study/']
    # def parse(self, response):
    #     for program in response.xpath("//*[@id='undergrad']/table/tbody/tr"):
    #         yield {
    #             'program' : program.css("td::text").get()
    #         }