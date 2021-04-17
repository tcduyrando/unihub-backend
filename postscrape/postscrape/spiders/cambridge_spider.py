import scrapy

class CambridgeSpider(scrapy.Spider):
    name = 'cambridge'

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

