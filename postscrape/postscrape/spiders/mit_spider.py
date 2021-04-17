import scrapy

class MITSpider(scrapy.Spider):
    name = 'mit'

    start_urls = [
        'https://gradadmissions.mit.edu/programs'
    ]

    # def parse(self, response):
    #     yield {
    #         'name' : 'Massachusetts Institute of Technology',
    #         'phone' : response.xpath("//*[@id='block-block-12']/div/div/ul[1]/li[2]/a/text()").get(),
    #         'email' : response.xpath("//*[@id='block-block-12']/div/div/ul[1]/li[1]/a/text()").get(),
    #         'location': response.xpath("//*[@id='block-block-12']/div/div/ul[1]/li[3]/a/text()").get(),
    #     }
    #
    #     for program in response.css("div.views-row"):
    #         yield {
    #             'program' : program.css("div.views-field.views-field-title.program_list_column span.field-content a::text").get()
    #             # 'deadline' : program.css("div div.field-content span::text").get()
    #         }

    start_urls = ['https://gradadmissions.mit.edu/costs-funding/cost-of-attendance']

    def parse(self, response):
        yield {
            'tuition': response.xpath("//*[@id='docs-internal-guid-013c85db-7fff-d830-0015-ef077a3b2274']/text()").get()
        }







