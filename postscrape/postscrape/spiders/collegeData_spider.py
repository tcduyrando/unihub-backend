import scrapy

class collegeDataSpider(scrapy.Spider):
    name = 'collegedata'

    start_urls = ['https://www.collegedata.com/college-search/massachusetts-institute-of-technology/academics']