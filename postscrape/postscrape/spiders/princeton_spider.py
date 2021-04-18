import scrapy

class PrincetonSpider(scrapy.Spider):
    name = 'princeton'

    # other info are scraped by collegeData_commonApp spider

    start_urls = ['https://www.princeton.edu/academics/areas-of-study']
    def parse(self, response):
        for program in response.css("li.row.small-collapse"):
            yield {
                'program' : program.css("a h2::text").get()
            }