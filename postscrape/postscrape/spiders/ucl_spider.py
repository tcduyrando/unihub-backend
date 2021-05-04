import scrapy

from ..items import UniItem

class UCollegeLondonSpider(scrapy.Spider):
    name = 'ucl'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.ucl.ac.uk/prospective-students/undergraduate/subject-areas']
    def parse(self, response):
        for programList in response.css("li.degree-list__group"):
            for sublist in programList.css("div table tbody tr"):
                items = UniItem()
                program = sublist.css("td.degree-list__item a::text").get()
                # remove spaces
                program = program.replace('\n', '')
                program = program.replace('                      ', '')
                program = program.replace('                    ', '')
                items['program'] = program
                items['school_id'] = 17
                yield items

    # start_urls = ['https://www.ucl.ac.uk/digital-presence-services/ugdegrees/www/degreesearch.php']
    # def parse(self, response):
    #     for programList in response.css("li.degree-list__group"):
    #         for sublist in programList.css("div table tbody tr"):
    #             tag = sublist.css("td.degree-list__item a span::text").get()
    #             if tag == "BA" or tag == "BASc" or tag == "BEng" or tag == "BFA" or tag == "BSc" or tag == "BSc (Econ)":
    #                 items = UniItem()
    #                 program = sublist.css("td.degree-list__item a::text").get()
    #                 program = program + tag
    #                 items['program'] = program
    #                 items['school_id'] = 17
    #                 yield items