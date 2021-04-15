import scrapy

class THESpider(scrapy.Spider):
    name = '4icu'

    start_urls = [
        'https://www.4icu.org/reviews/12045.htm',
        'https://www.4icu.org/reviews/4894.htm',
        'https://www.4icu.org/reviews/4905.htm']

    def _parse(self, response):
        yield {
            'uniName' : response.css("title::text").get()
        }
        for major in response.css("div.modal.fade"):

            # print("found major list")
            # if major[9:14] != "pre-Ba" and major[9:14] != "Bachel" and major[9:14] != "Master" and major[9:14] != "Doctor":
            # con = major.css("p.modal-title strong::text")
            # if con != "pre-Bachelor degrees" and con != "Bachelor degrees" \
            #         and con != "Master degrees" and con != "Doctoral degree":
            for major2 in major.css(".modal-body ul li ::text"):
                yield {
                    'majorName' : major2.get(),
                    'category': major.css(".modal-header p.modal-title strong::text").get()
                }
            # else:
            #     print("found excluded stuff")