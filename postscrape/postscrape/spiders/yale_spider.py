import scrapy

class YaleSpider(scrapy.Spider):
    name = 'yale'

    # other info are scraped by collegeData_commonApp spider

    start_urls = ['http://catalog.yale.edu/ycps/majors-in-yale-college/']
    def parse(self, response):
        for program in response.xpath("//*[@id='textcontainer']/p"):
            yield {
                'program' : program.css("a::text").get()
            }