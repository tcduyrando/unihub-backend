import scrapy

from ..items import UniItem

class ColumbiaSpider(scrapy.Spider):
    name = 'columbia'

    # other info are scraped by goToUniversity

    start_urls = ['https://www.gotouniversity.com/university/columbia-university/programs']
    def parse(self, response):
        for programList in response.css("div.panel.panel-default"):
            items = UniItem()
            program = programList.css("div div div div")[0].css("span a::text").get()
            if "BA" in program:
                items['program'] = program
                items['school_id'] = 18
                yield items
        next_page_number = response.css("li.next a::attr(href)").get()[-1]
        number_int = int(next_page_number)

        if number_int < 9:
            next_page = "https://www.gotouniversity.com/university/columbia-university/programs?page=" + next_page_number
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
