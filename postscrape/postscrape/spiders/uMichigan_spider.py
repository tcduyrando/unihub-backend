import scrapy

from ..items import UniItem

class UMichiganSpider(scrapy.Spider):
    name = 'uMichigan'

    # other info are scraped by goToUniversity

    start_urls = ['https://admissions.umich.edu/academics-majors/majors-degrees']
    def parse(self, response):
        for programList in response.css("table.views-table.views-view-table"):
            for sublist in programList.css("tbody tr"):
                items = UniItem()
                program = sublist.css("td.views-field a::text").get()
                items['program'] = program
                items['school_id'] = 20
                yield items