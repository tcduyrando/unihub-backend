import scrapy
from ..items import UniItem

class goToUniversity2Spider(scrapy.Spider):
    name = 'gtu2'

    # MAJORS WILL BE SCRAPED SEPARATELY IN OTHER SPIDERS

    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    start_urls = [
        # 0
        'https://www.gotouniversity.com/university/university-of-oxford/application-requirements',
        'https://www.gotouniversity.com/university/california-institute-of-technology/application-requirements',
        'https://www.gotouniversity.com/university/university-of-cambridge/application-requirements',
        'https://www.gotouniversity.com/university/yale-university/application-requirements',
        'https://www.gotouniversity.com/university/massachusetts-institute-of-technology/application-requirements',
        # 5
        'https://www.gotouniversity.com/university/princeton-university/application-requirements',
        'https://www.gotouniversity.com/university/stanford-university/application-requirements',
        'https://www.gotouniversity.com/university/university-of-chicago/application-requirements',
        'https://www.gotouniversity.com/university/lund-university/application-requirements',
        'https://www.gotouniversity.com/university/chung-ang-university/application-requirements',
        # 10
        'https://www.gotouniversity.com/university/university-of-california-berkeley/application-requirements',
        'https://www.gotouniversity.com/university/imperial-college-london/application-requirements',
        'https://www.gotouniversity.com/university/johns-hopkins-university/application-requirements',
        'https://www.gotouniversity.com/university/university-of-pennsylvania/application-requirements',
        'https://www.gotouniversity.com/university/zurich-swiss-federal-institute-of-technology-eth/application-requirements',
        # 15
        'https://www.gotouniversity.com/university/university-of-california-los-angeles/application-requirements',
        'https://www.gotouniversity.com/university/university-college-london/application-requirements',
        'https://www.gotouniversity.com/university/columbia-university/application-requirements',
        'https://www.gotouniversity.com/university/duke-university/application-requirements',
        'https://www.gotouniversity.com/university/university-of-michigan-ann-arbor/application-requirements',
        # 20
        'https://www.gotouniversity.com/university/peking-university/application-requirements',
        'https://www.gotouniversity.com/university/new-york-university/application-requirements',
        'https://www.gotouniversity.com/university/carnegie-mellon-university/application-requirements',
        'https://www.gotouniversity.com/university/university-of-washington/application-requirements'

    ]
    def parse(self, response):
        name2 = response.xpath('/html/body/div[2]/ul/li[3]/a/text()').get()
        location = response.xpath("//*[@id='page-wrapper']/div[2]/div/div/div/div[2]/p/text()").get()
        score_ielts = response.xpath("//*[@id='entrance_score']/div/div[1]/div[2]/div/div[1]/div/div[1]/text()").get()
        score_toefl = response.xpath("//*[@id='entrance_score']/div/div[1]/div[2]/div/div[2]/div/div[1]/text()").get()
        score_sat = response.xpath("//*[@id='entrance_score']/div/div[1]/div[2]/div/div[3]/div/div[1]/text()").get()

        # remove line break in location
        location = location.replace('\n', '')

        # assign 0 to score if null and convert score strings to int
        if score_ielts != None:
            score_ielts = float(score_ielts)
        else:
            score_ielts = 0.0

        if score_toefl != None:
            score_toefl = int(score_toefl)
        else:
            score_toefl = 0

        if score_sat != None:
            score_sat = int(score_sat)
        else:
            score_sat = 0

        items = UniItem()
        items['name2'] = name2
        items['location'] = location
        items['score_ielts'] = score_ielts
        items['score_toefl'] = score_toefl
        items['score_sat'] = score_sat
        yield items

        # unused_urls = [
        #     'https://www.gotouniversity.com/university/university-of-toronto-st-george/application-requirements',
        #     'https://www.gotouniversity.com/university/cornell-university/application-requirements'
        # ]