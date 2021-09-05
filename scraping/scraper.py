from builtins import Exception

from bs4 import BeautifulSoup
from requests import get
from ..helpers.helpers import *


class Scraper():
    def scraping_data(self, url):
        web_data = get(url)

        if web_data.status_code == 200:
            soup = BeautifulSoup(web_data.text, 'html.parser')
            contents = soup.find_all('article')
            news_data = {'headline': {}, 'list_of_news': []}

            # get headline news
            headline_content = soup.find('article', id='hl')
            try:
                news_data['headline']['title'] = headline_content.find('h1').text
                news_data['headline']['label'] = headline_content.find('span', class_='label').text
                headline_release_updated = headline_content.find('span', class_='date') \
                    .text.replace(news_data['headline']['label'] + ' ', '')
                news_data['headline']['release_updated'] = headline_release_updated
                news_data['headline']['url'] = headline_content.find('a', href=True).get('href')
                news_data['headline']['img_url'] = headline_content.find('img').get('src')

            except Exception as e:
                pass

            # get all news articles
            for content in contents:
                try:
                    title = content.find('h2').text
                    news_label = content.find('span', class_='label').text
                    time_desc = content.find('span', class_='date').text.replace(news_label, '').split(' ')[4:8]
                    release_updated = ' '.join(time_desc)
                    news_url = content.find('a', href=True).get('href')
                    img_url = content.find('img').get('src')

                    news_data['list_of_news'].append({
                        'title': title,
                        'label': news_label,
                        'release_updated': release_updated,
                        'url': news_url,
                        'img_url': img_url
                    })
                except:
                    continue

            return news_data

        elif web_data.status_code == 404:
            return False

    def get_data_from_page(self, path=None):
        url_path = SOURCE_URL.format(path) if path else SOURCE_URL
        res = self.scraping_data(url_path)

        return res
