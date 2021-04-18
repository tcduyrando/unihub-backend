import scrapy

class collegeData_CommonAppSpider(scrapy.Spider):
    name = 'cd_ca'

    # MAJORS WILL BE SCRAPED SEPARATELY IN OTHER SPIDERS

    start_urls = [
        'https://www.commonapp.org/explore/yale-university',
        'https://www.commonapp.org/explore/princeton-university',
        'https://www.commonapp.org/explore/university-chicago'
    ]
    def parse(self, response):
        yield {
            'name' : response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[1]/div/div/div/h1/text()").get(),
            'email' : response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[2]/div[2]/p/a/text()").get(),
            'phone' : response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[2]/div[3]/p/text()").get(),
            'location' : response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[2]/div[1]/p/text()")[1:].extract(),
            'admissionWeb' : response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[3]/div[1]/p/a/@href").get()
        }

    # start_urls = [
    #   'https://www.collegedata.com/college-search/yale-university/money-matters',
    #   'https://www.collegedata.com/college-search/princeton-university/money-matters',
    #   'https://www.collegedata.com/college-search/university-of-chicago/money-matters'
    # ]
    # def parse(self, response):
    #     yield {
    #         'website' : response.xpath("//*[@id='app-container']/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/a[1]/@href").get(),
    #         'tuition' : response.xpath("//*[@id='app-container']/div/div/div[1]/div[3]/div/div/div/div[5]/div[1]/div[2]/text()").get()
    #     }

    # MAJORS NOT ALLOWED!!!!!!!!!!!!! FUUUUUCCCCCKKKKK!!!!!
    # start_urls = ['https://www.collegedata.com/college-search/yale-university/academics']
    # def parse(self, response):
    #     for program in response.xpath("//*[@id='app-container']/div[2]/div/div/div[1]/text()"):
    #         yield {
    #             'program' : program
    #         }