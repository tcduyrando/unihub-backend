import scrapy

from ..items import UniItem

class CaltechSpider(scrapy.Spider):
    name = 'caltech'

    start_urls = ['https://www.admissions.caltech.edu/explore/academics/majors-minors']

    def parse(self, response):
        for programList in response.xpath("//*[@id='content']/section[2]/div/div/div[2]/section/div/div/ul[2]/li"):
            items = UniItem()
            program = programList.css("a::text").get()
            items['program'] = program
            items['school_id'] = 2
            yield items

    # start_urls = ['https://www.admissions.caltech.edu/inquire']

    # def parse(self, response):
    #     yield {
    #         'name' : 'California Institute of Technology',
    #         'phone': response.xpath("//*[@id='content']/section[2]/div/div/div[2]/section/div/div/p[1]/text()").get(),
    #         'email': response.xpath("//*[@id='content']/section[2]/div/div/div[2]/section/div/div/p[1]/a/text()").get(),
    #         'location': response.xpath("//*[@id='content']/section[2]/div/div/div[2]/section/div/div/p[3]/text()")[
    #                     2: 4].extract()
    #     }

    # start_urls = ['https://www.finaid.caltech.edu/costs']
    # def _parse(self, response):
    #     yield {
    #         'tuition' : response.xpath("//*[@id='content']/div[1]/div/div[2]/div/table/tbody/tr[1]/td[2]/div/text()").get()
    #     }

