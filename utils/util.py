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

        if content:
            self.set_status(200)
            self.set_content(content)

        else:
            self.set_status(404)

        return self.get_response()


class CNBCIndonesiaNewsDetail(Resource, APIResponse, Scraper):
    def get(self):
        url = request.args.get('url')
        content = self.scraping_data_detail(url)

        if content:
            self.set_status(200)
            self.set_content(content)

        elif content['status'] == 400:
            self.set_status(400)

        else:
            self.set_status(404)

        return self.get_response()
