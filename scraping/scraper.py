from builtins import Exception

from bs4 import BeautifulSoup
from requests import get
from helpers.helpers import *


class Scraper():
    def scraping_data(self, url):
        web_data = get(url)

        if web_data.status_code == 200:
            soup = BeautifulSoup(web_data.text, 'html.parser')
            contents = soup.find_all('article')
            news_data = {'headline': {}, 'total_news': 0, 'news': []}

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

                    news_data['news'].append({
                        'title': title,
                        'label': news_label,
                        'release_updated': release_updated,
                        'url': news_url,
                        'img_url': img_url
                    })
                except Exception as e:
                    continue

            news_data['total_news'] = len(news_data['news'])

            return news_data

        elif web_data.status_code == 404:
            return False

    def get_data_from_page(self, path=None):
        url_path = SOURCE_URL + path if path else SOURCE_URL
        res = self.scraping_data(url_path)

        return res

    def get_data_by_query(self, query=None):
        url_path = SOURCE_URL + 'search?query={}'.format(query) if query else SOURCE_URL
        res = self.scraping_data(url_path)

        return res

    def scraping_data_detail(self, url):
        web_data = get(url)

        if web_data.status_code == 200:
            soup = BeautifulSoup(web_data.text, 'html.parser')

            try:
                header = soup.find('div', class_='jdl')
                title = header.find('h1').text
                author_class = header.find('div', class_='author').text.split(' ')
                label = author_class[0]
                author = ' '.join(author_class[2:])
                release_date = header.find('div', class_='date').text

                detail_text_class = soup.find('div', class_='detail_text')
                texts = detail_text_class.find_all('p')
                news_content = ' '.join([text.text for text in texts])

                news_content_data = {
                    'title': title,
                    'label': label,
                    'author': author,
                    'release_date': release_date,
                    'content': news_content
                }

                return news_content_data

            except Exception as e:
                return {'status': 400}

        elif web_data.status_code == 404:
            return False
