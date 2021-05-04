import scrapy

from ..items import UniItem

class DukeSpider(scrapy.Spider):
    name = 'duke'

    # other info are scraped by goToUniversity

    start_urls = ['https://admissions.duke.edu/academic-possibilities/']
    def parse(self, response):
        programList = response.xpath('//*[@id="main"]/div[6]/section/div/div[1]/div/p/text()').extract()
        for program in programList:
            items = UniItem()
            # remove line break and '*'
            program = program.replace('\n', '')
            program = program.replace('*', '')
            items['program'] = program
            items['school_id'] = 19
            yield items