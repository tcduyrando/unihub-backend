import scrapy
from ..items import UniItem

class goToUniversitySpider(scrapy.Spider):
    name = 'gtu2'

    # MAJORS WILL BE SCRAPED SEPARATELY IN OTHER SPIDERS

    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    start_urls = [
        'https://www.gotouniversity.com/university/university-of-oxford/application-requirements',
        'https://www.gotouniversity.com/university/lund-university/application-requirements',
        'https://www.gotouniversity.com/university/california-institute-of-technology/application-requirements',
        'https://www.gotouniversity.com/university/chung-ang-university/application-requirements',
        'https://www.gotouniversity.com/university/university-of-cambridge/application-requirements',
        'https://www.gotouniversity.com/university/yale-university/application-requirements',
        'https://www.gotouniversity.com/university/massachusetts-institute-of-technology/application-requirements',
        'https://www.gotouniversity.com/university/princeton-university/application-requirements',
        'https://www.gotouniversity.com/university/stanford-university/application-requirements',
        'https://www.gotouniversity.com/university/university-of-chicago/application-requirements'
    ]
    def parse(self, response):
        name2 = response.xpath('/html/body/div[2]/ul/li[3]/a/text()').get()
        location = response.xpath("//*[@id='page-wrapper']/div[2]/div/div/div/div[2]/p/text()").get()
        score_ielts = response.xpath("//*[@id='entrance_score']/div/div[1]/div[2]/div/div[1]/div/div[1]/text()").get()
        score_toefl = response.xpath("//*[@id='entrance_score']/div/div[1]/div[2]/div/div[2]/div/div[1]/text()").get()
        score_sat = response.xpath("//*[@id='entrance_score']/div/div[1]/div[2]/div/div[3]/div/div[1]/text()").get()

        # remove line break in location
        location = location.replace('\n', '')

        score_ielts = float(score_ielts)
        score_toefl = int(score_toefl)
        score_sat = int(score_sat)

        items = UniItem()
        items['name2'] = name2
        items['location'] = location
        items['score_ielts'] = score_ielts
        items['score_toefl'] = score_toefl
        items['score_sat'] = score_sat
        yield items