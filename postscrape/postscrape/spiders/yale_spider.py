import scrapy

from ..items import UniItem

class YaleSpider(scrapy.Spider):
    name = 'yale'

    # other info are scraped by collegeData_commonApp spider

    start_urls = ['http://catalog.yale.edu/ycps/majors-in-yale-college/']

    def parse(self, response):
        for programList in response.xpath("//*[@id='textcontainer']/p"):
            items = UniItem()
            program = programList.css("a::text").get()
            items['program'] = program
            items['school_id'] = 4
            yield items