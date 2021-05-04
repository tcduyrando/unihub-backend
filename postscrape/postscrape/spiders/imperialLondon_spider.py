import scrapy

from ..items import UniItem

class ImperialLondonSpider(scrapy.Spider):
    name = 'imperialLondon'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.imperial.ac.uk/study/ug/courses/']
    def parse(self, response):
        for programList in response.css("li.link-list.drop-cap"):
            for sublist in programList.css("ol li.course"):
                items = UniItem()
                program = sublist.css("a h4::text").get()
                items['program'] = program
                items['school_id'] = 12
                yield items