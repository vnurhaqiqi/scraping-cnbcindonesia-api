from utils.util import *
from helpers.helpers import *
from app import *

api.add_resource(CNBCIndonesiaCategories, '/')
api.add_resource(CNBCIndonesiaNews, BASE_PATH.format('cnbc-news-articles'))
api.add_resource(CNBCIndonesiaNewsDetail, BASE_PATH.format('cnbc-news-detail'))
api.add_resource(CNBCIndonesiaSearch, BASE_PATH.format('cnbc-news-search'))
