import scrapy
from postscrape.postscrape.spiders.goToUniversity_spider import goToUniversitySpider
from postscrape.postscrape.spiders.goToUniversity2_spider import goToUniversity2Spider
from postscrape.postscrape.spiders.caltech_spider import CaltechSpider
from postscrape.postscrape.spiders.cambridge_spider import CambridgeSpider
from postscrape.postscrape.spiders.yale_spider import YaleSpider
from postscrape.postscrape.spiders.mit_spider import MITSpider
from postscrape.postscrape.spiders.princeton_spider import PrincetonSpider
from postscrape.postscrape.spiders.stanford_spider import StanfordSpider
from postscrape.postscrape.spiders.uChicago_spider import UChicagoSpider
from postscrape.postscrape.spiders.lund_spider import LundSpider
from postscrape.postscrape.spiders.berkeley_spider import BerkeleySpider
from postscrape.postscrape.spiders.imperialLondon_spider import ImperialLondonSpider
from postscrape.postscrape.spiders.johnsHopkins_spider import JohnsHopkinsSpider
from postscrape.postscrape.spiders.uPenn_spider import UPennsylvaniaSpider
from postscrape.postscrape.spiders.ucla_spider import UCLASpider
from postscrape.postscrape.spiders.ucl_spider import UCollegeLondonSpider
from postscrape.postscrape.spiders.columbia_spider import ColumbiaSpider
from postscrape.postscrape.spiders.duke_spider import DukeSpider
from postscrape.postscrape.spiders.uMichigan_spider import UMichiganSpider
from postscrape.postscrape.spiders.nyu_spider import NewYorkSpider
from postscrape.postscrape.spiders.carnegieMellon_spider import CarnegieMellonSpider
from postscrape.postscrape.spiders.uWashington_spider import UWashingtonSpider

from scrapy.utils.project import get_project_settings

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# configure_logging()
# runner = CrawlerRunner(settings=get_project_settings())

# @defer.inlineCallbacks
# def crawl():
#     runner.crawl(goToUniversitySpider)
#     runner.crawl(goToUniversity2Spider)
#     yield runner.crawl(CaltechSpider)
#     yield runner.crawl(CambridgeSpider)
#     yield runner.crawl(YaleSpider)
#     yield runner.crawl(MITSpider)
#     yield runner.crawl(PrincetonSpider)
#     yield runner.crawl(StanfordSpider)
#     yield runner.crawl(UChicagoSpider)
#     yield runner.crawl(LundSpider)
#     yield runner.crawl(BerkeleySpider)
#     yield runner.crawl(ImperialLondonSpider)
#     yield runner.crawl(JohnsHopkinsSpider)
#     yield runner.crawl(UPennsylvaniaSpider)
#     yield runner.crawl(UCLASpider)
#     yield runner.crawl(UCollegeLondonSpider)
#     yield runner.crawl(ColumbiaSpider)
#     yield runner.crawl(DukeSpider)
#     yield runner.crawl(UMichiganSpider)
#     yield runner.crawl(NewYorkSpider)
#     yield runner.crawl(CarnegieMellonSpider)
#     yield runner.crawl(UWashingtonSpider)
#     reactor.stop()

# @defer.inlineCallbacks
# def crawl2():
#     # crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
#     crawler.configure()
#     crawler.crawl(goToUniversitySpider)
#     crawler.crawl(goToUniversity2Spider)
#     crawler.crawl(CaltechSpider)
#     crawler.crawl(CambridgeSpider)
#     crawler.crawl(YaleSpider)
#     crawler.crawl(MITSpider)
#     crawler.crawl(PrincetonSpider)
#     crawler.crawl(StanfordSpider)
#     crawler.crawl(UChicagoSpider)
#     crawler.crawl(LundSpider)
#     crawler.crawl(BerkeleySpider)
#     crawler.crawl(ImperialLondonSpider)
#     crawler.crawl(JohnsHopkinsSpider)
#     crawler.crawl(UPennsylvaniaSpider)
#     crawler.crawl(UCLASpider)
#     crawler.crawl(UCollegeLondonSpider)
#     crawler.crawl(ColumbiaSpider)
#     crawler.crawl(DukeSpider)
#     crawler.crawl(UMichiganSpider)
#     crawler.crawl(NewYorkSpider)
#     crawler.crawl(CarnegieMellonSpider)
#     crawler.crawl(UWashingtonSpider)
#     crawler.start()

# crawl()
# reactor.run() # the script will block here until the last crawl call is finished