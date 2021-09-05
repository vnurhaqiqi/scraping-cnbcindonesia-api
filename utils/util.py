from flask import request
from app import *
from scraping.scraper import Scraper
from helpers.helpers import *


class CNBCIndonesiaCategories(Resource, APIResponse):
    def get(self):
        res_data = {
            'list_of_category': NEWS_CATEGORIES,
            'examples': {
                'get_all_articles': "/api/v1/cnbc-news-articles",
                'get_article_detail': "/api/v1/cnbc-news-detail?url={link url} -> link url: https://www.cnbcindonesia.com/tech/20210904210634-37-273686/heboh-gb-whatsapp-fakta-dan-bahaya-yang-mengintai-ponselmu",
                'get_articles_by_query': "/api/v1/cnbc-news-search?query={key words} -> key words: vaksin"
            }
        }

        self.set_status(200)
        self.set_content(res_data)

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


class CNBCIndonesiaSearch(Resource, APIResponse, Scraper):
    def get(self):
        query = request.args.get('query')
        content = self.get_data_by_query(query)

        if content:
            self.set_status(200)
            self.set_content(content)

        else:
            self.set_status(404)

        return self.get_response()
