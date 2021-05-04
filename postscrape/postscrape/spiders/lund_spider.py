import scrapy

from ..items import UniItem

class LundSpider(scrapy.Spider):
    name = 'lund'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.lunduniversity.lu.se/admissions/bachelors-and-masters-studies']
    def parse(self, response):
        for programList in response.xpath("//*[@id='block-lu-theme-content']/div/div/main/div[2]/div/div/div/div[1]/div[2]/div/ul[2]/li"):
            items = UniItem()
            program = programList.css("a::text").get()
            items['program'] = program
            items['school_id'] = 9
            yield items