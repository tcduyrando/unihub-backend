import scrapy
from ..items import UniItem

class goToUniversitySpider(scrapy.Spider):
    name = 'gtu'

    # MAJORS WILL BE SCRAPED SEPARATELY IN OTHER SPIDERS

    custom_settings = {
        'CONCURRENT_REQUESTS' : 1
    }

    start_urls = [
        # 0
        # 'https://www.gotouniversity.com/university/university-of-oxford',
        # 'https://www.gotouniversity.com/university/california-institute-of-technology',
        # 'https://www.gotouniversity.com/university/university-of-cambridge',
        # 'https://www.gotouniversity.com/university/yale-university',
        # 'https://www.gotouniversity.com/university/massachusetts-institute-of-technology',
        # 5
        # 'https://www.gotouniversity.com/university/princeton-university',
        # 'https://www.gotouniversity.com/university/stanford-university',
        # 'https://www.gotouniversity.com/university/university-of-chicago',
        # 'https://www.gotouniversity.com/university/lund-university',
        # 'https://www.gotouniversity.com/university/chung-ang-university',
        # 10
        # 'https://www.gotouniversity.com/university/university-of-california-berkeley',
        # 'https://www.gotouniversity.com/university/imperial-college-london',
        # 'https://www.gotouniversity.com/university/johns-hopkins-university',
        # 'https://www.gotouniversity.com/university/university-of-pennsylvania',
        # 'https://www.gotouniversity.com/university/zurich-swiss-federal-institute-of-technology-eth',
        # 15
        # 'https://www.gotouniversity.com/university/university-of-california-los-angeles',
        # 'https://www.gotouniversity.com/university/university-college-london',
        # 'https://www.gotouniversity.com/university/columbia-university',
        # 'https://www.gotouniversity.com/university/duke-university',
        # 'https://www.gotouniversity.com/university/university-of-michigan-ann-arbor',
        # 20
        # 'https://www.gotouniversity.com/university/peking-university',
        # 'https://www.gotouniversity.com/university/new-york-university',
        # 'https://www.gotouniversity.com/university/carnegie-mellon-university',
        # 'https://www.gotouniversity.com/university/university-of-washington'
    ]
    def parse(self, response):
        items = UniItem()
        name = response.xpath("/html/body/div[2]/ul/li[3]/span/text()").get()
        country = response.css("p.univ-state::text").get()
        email = response.xpath("//*[@id='page-wrapper']/div/div[3]/div/div/div[1]/div[3]/p/text()").get()
        phone = response.xpath("//*[@id='page-wrapper']/div/div[3]/div/div/div[1]/div[4]/p/text()").get()
        imageURL = response.css("div.uni-img-info img::attr(src)").get()
        logoURL = response.css("img.logo_univ_12120::attr(data-src)").get()
        tuition = response.css("div.col-sm-6 p::text").get()
        tuitionUSD = response.css("div.col-sm-6 p::text").get()
        # tuition = response.xpath("//*[@id='tab-about']/div[4]/div[2]/div/div/p[2]/text()").get()
        # tuitionUSD = response.xpath("//*[@id='tab-about']/div[4]/div[2]/div/div/p[2]/text()").get()
        website = response.css("div.univ-btn-block a::attr(href)").get()

        # remove line break " " from country, email, phone
        country = country.replace('\n', '')
        email = email.replace('\n', '')
        phone = phone.replace('\n', '')

        # remove space "Bachelors:" from tuition
        tuition = tuition.replace('Bachelors:', '')

        # remove "" from tuitionUSD
        tuitionUSD = tuitionUSD.replace(' ', '')
        # remove "," from tuitionUSD
        tuitionUSD = tuitionUSD.replace(',', '')
        # remove space "Bachelors:" from tuitionUSD
        tuitionUSD = tuitionUSD.replace('Bachelors:', '')
        # remove currency symbols and convert native tuition string to tuitionUSD int
        if "$" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('$', '')
            tuitionUSD = int(tuitionUSD)
        elif "£" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('£', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 1.38)
        elif "€" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('€', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 1.2)
        elif "RMB" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('RMB', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 0.15)
        elif "TRY" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('TRY', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 0.12)
        elif "INR" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('INR', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 0.013)
        elif "KRW" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('KRW', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 0.00089)
        elif "CHF" in tuitionUSD:
            tuitionUSD = tuitionUSD.replace('CHF', '')
            tuitionUSD = int(tuitionUSD)
            tuitionUSD = int(tuitionUSD * 1.1)


        items['name'] = name
        items['country'] = country
        items['email'] = email
        items['phone'] = phone
        items['imageURL'] = imageURL
        items['logoURL'] = logoURL
        items['tuition'] = tuition
        items['tuitionUSD'] = tuitionUSD
        items['website'] = website
        yield items

    # # MAJORS NOT ALLOWED!!!!!!!!!!!!! FUUUUUCCCCCKKKKK!!!!!
    # start_urls = ['https://www.collegedata.com/college-search/yale-university/academics']
    # def parse(self, response):
    #     for program in response.xpath("//*[@id='app-container']/div[2]/div/div/div[1]/text()"):
    #         yield {
    #             'program' : program
    #         }

    # unused_urls = [
    #     'https://www.gotouniversity.com/university/university-of-toronto-st-george',
    #     'https://www.gotouniversity.com/university/cornell-university'
    # ]