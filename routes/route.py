from ..utils.util import *
from ..helpers.helpers import *
from ..app import *

api.add_resource(CNBCIndonesiaCategories, BASE_PATH.format(''))
api.add_resource(CNBCIndonesiaNews, BASE_PATH.format('cnbc-news-articles'))
