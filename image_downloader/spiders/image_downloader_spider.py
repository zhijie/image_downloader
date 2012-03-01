from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from image_downloader.items import ImageDownloaderItem

class ImageDownloaderSpider(CrawlSpider):
   name = "image_downloader"
   allowed_domains = ["sina.com.cn"]
   start_urls = [
       "http://www.sina.com.cn/"
   ]
   rules = [Rule(SgmlLinkExtractor(allow=[]), 'parse_item')]
   
   def parse_item(self, response):
       self.log('page: %s' % response.url)
       hxs = HtmlXPathSelector(response)
       images = hxs.select('//img/@src').extract()
       items = []
       for image in images:
           item = ImageDownloaderItem()
           item['image_urls']=[image]
           items.append(item)
       return items
