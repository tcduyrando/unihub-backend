import scrapy
from ..items import UniItem

class BachKhoaSpider(scrapy.Spider):
    name = 'bachKhoa'

    # MAJORS WILL BE SCRAPED SEPARATELY IN OTHER SPIDERS

    custom_settings = {
        'CONCURRENT_REQUESTS' : 1
    }

    start_urls = [
        'http://www.aao.hcmut.edu.vn/index.php?route=information/contact'
    ]
    def parse(self, response):
        items = UniItem()
        name = response.xpath("/html/body/div[2]/div[1]/div[2]/p[2]/text()[2]").get()
        country = "Vietnam"
        email = response.xpath("/html/body/div[2]/div[1]/div[2]/p[5]/a/text()").get()
        phone = response.xpath("/html/body/div[2]/div[1]/div[2]/p[6]/text()").get()
        imageURL = ""
        logoURL = "http://www.aao.hcmut.edu.vn/" + response.xpath("/html/body/div[1]/div/nav/div/div[1]/a/img[2]/@src").get()
        tuition = ""
        tuitionUSD = 0
        website = "http://www.aao.hcmut.edu.vn/"
        location = response.xpath('/html/body/div[2]/div[1]/div[2]/p[3]/text()').get()
        score_ielts = 0.0
        score_toefl = 0
        score_sat = 0

        name = name.replace('\r\n\t', '')
        phone = phone.replace('\r\n\tĐiện thoại: ', '')
        phone = phone.replace('\xa0\xa0\xa0\xa0 ;Số Fax: (02) 838 637 002', '')
        location = location.replace('\r\n\tĐịa chỉ: ', '')

        items['name'] = name
        items['country'] = country
        items['email'] = email
        items['phone'] = phone
        items['imageURL'] = imageURL
        items['logoURL'] = logoURL
        items['tuition'] = tuition
        items['tuitionUSD'] = tuitionUSD
        items['website'] = website
        items['location'] = location
        items['score_ielts'] = score_ielts
        items['score_toefl'] = score_toefl
        items['score_sat'] = score_sat
        yield items