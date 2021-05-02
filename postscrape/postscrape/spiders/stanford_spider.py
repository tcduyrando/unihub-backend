import scrapy

from ..items import UniItem

class StanfordSpider(scrapy.Spider):
    name = 'stanford'

    start_urls = ['https://majors.stanford.edu/']
    def parse(self, response):
        for programList in response.xpath("//*[@id='isotope-container']/div"):
            items = UniItem()
            program = programList.css("p::text").get()
            items['program'] = program
            items['school_id'] = 7
            yield items

    # start_urls = ['https://visit.stanford.edu/contact/']
    # def _parse(self, response):
    #     yield {
    #         'name': 'Stanford University',
    #         'phone': response.xpath("//*[@id='main-content']/div[2]/div[2]/p/text()").get(),
    #         'email': response.xpath("//*[@id='main-content']/div[1]/div[2]/p/a/text()").get(),
    #         'location': response.xpath("//*[@id='main-content']/div[3]/div[2]/p/text()")[3:5].extract()
    #     }

    # start_urls = ['https://www.stanford.edu/contact/']
    # def _parse(self, response):
    #     yield {
    #         'location': response.xpath("//*[@id='main']/section/section[1]/div/section[2]/div/ul/li/text()")[1:3].extract()
    #     }

    # start_urls = ['https://majors.stanford.edu/']
    # def _parse(self, response):
    #     for program in response.xpath("//*[@id='isotope-container']/div"):
    #         yield {
    #             'program' : program.css("p::text").get()
    #         }

    # start_urls = ['https://www.collegedata.com/college-search/stanford-university/money-matters']
    # def parse(self, response):
    #     yield {
    #         'tuition' : response.xpath("//*[@id='app-container']/div/div/div[1]/div[3]/div/div/div/div[5]/div[1]/div[2]/text()").get()
    #     }