# Scrapy settings for image_downloader project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'image_downloader'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['image_downloader.spiders']
NEWSPIDER_MODULE = 'image_downloader.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DEFAULT_ITEM_CLASS = 'image_downloader.items.ImageDownloaderItem'

IMAGES_MIN_HEIGHT = 50
IMAGES_MIN_WIDTH = 50
IMAGES_STORE = 'image-downloaded/'
DOWNLOAD_TIMEOUT = 1200
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline',
'image_downloader.pipelines.ImageDownloaderPipeline']