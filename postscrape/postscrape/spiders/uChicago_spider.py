import scrapy

class UChicagoSpider(scrapy.Spider):
    name = 'uchicago'

    # other info are scraped by collegeData_commonApp spider

    start_urls = ['https://www.uchicago.edu/academics/programs_of_study/']
    def parse(self, response):
        for program in response.xpath("//*[@id='undergrad']/table/tbody/tr"):
            yield {
                'program' : program.css("td::text").get()
            }