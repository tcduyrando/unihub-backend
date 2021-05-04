import scrapy

from ..items import UniItem

class UWashingtonSpider(scrapy.Spider):
    name = 'uWashington'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.washington.edu/uaa/advising/degree-overview/majors/majors-by-topic/']
    def parse(self, response):
        for programList in response.css("blockquote.majortopic"):
            topic = programList.css("h5::text").get()
            for sublist in programList.css("li"):
                items = UniItem()
                programName = sublist.css("a::text").get()
                program = topic + ": " + programName
                items['program'] = program
                items['school_id'] = 24
                yield items