import scrapy

class MITSpider(scrapy.Spider):
    name = 'mit'

    start_urls = ['https://gradadmissions.mit.edu/programs']

    def _parse(self, response):
        # i = 1
        # repeat = True
        # while (repeat == True):

        # i = 1
        for program in response.css("div.views-row"):
            yield {
                'program' : program.css("div.views-field.views-field-title.program_list_column span.field-content a::text").get()
                # 'deadline' : program.css("div div.field-content span::text").get()
            }



