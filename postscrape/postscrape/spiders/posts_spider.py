import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://thongtintuyensinh.vn/Truong_Dai_hoc_Khoa_hoc_Tu_nhien_DHQG_TPHCM_C51_D825.htm',
        'https://thongtintuyensinh.vn/Truong_Dai_hoc_Bach_khoa-DHQG_TPHCM_C51_D826.htm'
    ]

    def parse(self, response):
        for i in range(4):
            if ("ng" in response.css('tbody tr td')[i].get()):
                for post in response.css('tbody tr'):
                    yield {
                        'major': post.css('td p span::text')[0].get()
                    }
                yield {
                    'address' : response.xpath('//*[@id="tabContent"]/p[5]/span/text()').get()
                }
            