import scrapy
from ..items import UniItem

class collegeData_CommonAppSpider(scrapy.Spider):
    name = 'cd_ca'

    # MAJORS WILL BE SCRAPED SEPARATELY IN OTHER SPIDERS

    # start_urls = [
    #     'https://www.commonapp.org/explore/yale-university',
    #     'https://www.commonapp.org/explore/princeton-university',
    #     'https://www.commonapp.org/explore/university-chicago'
    # ]
    # def parse(self, response):
    #     items = UniItem()
    #     name = response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[1]/div/div/div/h1/text()").get()
    #     email = response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[2]/div[2]/p/a/text()").get()
    #     phone = response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[2]/div[3]/p/text()").get()
    #     locationList = response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[2]/div[1]/p/text()")[1:].extract()
    #     # convert location list into string
    #     location = ''
    #     for i in locationList:
    #         location = location + i
    #     admissionWeb = response.xpath("//*[@id='gatsby-focus-wrapper']/div/div/section[2]/div/div[2]/div/div[2]/div[3]/div[1]/p/a/@href").get()
    #
    #     items['name'] = name
    #     items['email'] = email
    #     items['phone'] = phone
    #     items['location'] = location
    #     items['admissionWeb'] = admissionWeb
    #     yield items

    start_urls = [
      'https://www.collegedata.com/college-search/yale-university/money-matters',
      'https://www.collegedata.com/college-search/princeton-university/money-matters',
      'https://www.collegedata.com/college-search/university-of-chicago/money-matters'
    ]
    def parse(self, response):
        name2 = response.xpath("//*[@id='app-container']/div/div/div[1]/div[1]/div/div/div/div/div[1]/h1/text()").get()
        website = response.xpath("//*[@id='app-container']/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/a[1]/@href").get()
        tuition = response.xpath("//*[@id='app-container']/div/div/div[1]/div[3]/div/div/div/div[5]/div[1]/div[2]/text()").get()
        # remove , from tuition
        tuition = tuition.replace(',', '')
        # remove $ from tuition
        tuition = tuition.replace('$', '')
        # convert tuition from string to int
        tuition = int(tuition)

        items = UniItem()
        items['name2'] = name2
        items['website'] = website
        items['tuition'] = tuition
        yield items

    # # MAJORS NOT ALLOWED!!!!!!!!!!!!! FUUUUUCCCCCKKKKK!!!!!
    # start_urls = ['https://www.collegedata.com/college-search/yale-university/academics']
    # def parse(self, response):
    #     for program in response.xpath("//*[@id='app-container']/div[2]/div/div/div[1]/text()"):
    #         yield {
    #             'program' : program
    #         }