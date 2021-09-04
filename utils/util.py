from flask import request
from ..app import *
from ..scraping.scraper import Scraper
from ..helpers.helpers import *


class CNBCIndonesiaCategories(Resource, APIResponse):
    def get(self):
        self.set_status(200)
        self.set_content(NEWS_CATEGORIES)

        return self.get_response()


class CNBCIndonesiaNews(Resource, APIResponse, Scraper):
    def get(self):
        category = request.args.get('category')
        content = self.get_data_from_page(path=category)

        self.set_status(200)
        self.set_content(content)

        return self.get_response()
