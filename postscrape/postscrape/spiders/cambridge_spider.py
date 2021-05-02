import scrapy

from ..items import UniItem

class CambridgeSpider(scrapy.Spider):
    name = 'cambridge'

    start_urls = ['https://www.undergraduate.study.cam.ac.uk/courses']

    def parse(self, response):
        for programList in response.xpath("//*[@id='block-system-main']/div/div/div/div"):
            for sublist in programList.css("div.view-content div"):
                items = UniItem()
                program = sublist.css("a::text").get()
                items['program'] = program
                items['school_id'] = 3
                yield items

    # start_urls = ['https://www.undergraduate.study.cam.ac.uk/courses']
    #
    # def _parse(self, response):
    #     yield {
    #         'name' : 'University of Cambridge',
    #         'phone' : response.xpath("//*[@id='block-block-5']/div/ul/li[2]/span/text()").get(),
    #         'email' : response.xpath("//*[@id='block-block-5']/div/ul/li[3]/span/a/text()").get()
    #     }
    #     for list in response.xpath("//*[@id='block-system-main']/div/div/div/div"):
    #         for program in list.css("div.view-content div"):
    #             yield {
    #                 'program' : program.css("a::text").get()
    #             }

    # start_urls = ['https://www.undergraduate.study.cam.ac.uk/fees-and-finance/tuition-fees']
    # def parse(self, response):
    #     yield {
    #         'tuition' : response.xpath("//*[@id='node-138']/div/div/div/div/p[3]/text()").get()
    #     }

