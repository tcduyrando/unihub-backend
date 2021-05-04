import scrapy

from ..items import UniItem

class CornellSpider(scrapy.Spider):
    name = 'cornell'

    # other info are scraped by goToUniversity

    # NOT USED

    start_urls = ['https://www.cornell.edu/academics/fields.cfm']
    def parse(self, response):
        for programList in response.css("table.cu-table.cu-table-majors tbody tr"):
            items = UniItem()
            program = programList.css("td a::text").get()
            items['program'] = program
            items['school_id'] = 20
            yield items