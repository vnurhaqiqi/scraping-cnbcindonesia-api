# SCRAPING-CNBC-INDONESIA

### Introduction

API Indonesia news by scraping data from [cnbc indonesia](https://www.cnbcindonesia.com/). This is unofficial API, feel
free to use or rebuild it again. Here's my reference to build this API
services [rizki4106 / cnnindonesia-news-api](https://github.com/rizki4106/cnnindonesia-news-api).

### Features

- [x] Get all list of news
- [x] Show news content
- [x] Search news by query / keywords

### Try your own

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://flask-scraping-cncbind.herokuapp.com/)

## Installment

#### clone the project

```bash
git clone https://github.com/vnurhaqiqi/scraping-cnbcindonesia-api
```

#### install all dependencies

```bash
pip install -r requirements.txt
```

#### run virtual env

```bash
source /env/bin/activate
```

#### run server using gunicorn

```bash
gunicorn app:app
```

### Usage
#### Documentation
<table>
<thead>
<tr>
  <th>No.</th>
  <th>Description</th>
  <th>Endpoint</th>
  <th>Query Params</th>
  <th>Method</th>
</tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>Return list of the latest news</td>
    <td>/api/v1/cnbc-news-articles</td>
    <td>-</td>
    <td>GET</td>
  </tr>
<tr>
    <td>2</td>
    <td>Return list of the latest news by category</td>
    <td>/api/v1/cnbc-news-articles?category={category}</td>
    <td>category</td>
    <td>GET</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Return specific news content</td>
    <td>/api/v1/cnbc-news-detail?url={url}</td>
    <td>url</td>
    <td>GET</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Search news by given query word</td>
    <td>/api/v1/cnbc-news-search?query={keywords}</td>
    <td>query</td>
    <td>GET</td>
  </tr>
</tbody>
</table>

#### Example
- [x] **Example: [/api/v1/cnbc-news-articles](https://flask-scraping-cncbind.herokuapp.com/api/v1/cnbc-news-articles)**
- [x] **Example: [/api/v1/cnbc-news-articles?category={category}](https://flask-scraping-cncbind.herokuapp.com/api/v1/cnbc-news-articles?category=market)**
- [x] **Example: [/api/v1/cnbc-news-detail?url={url}](https://flask-scraping-cncbind.herokuapp.com/api/v1/cnbc-news-detail?url=https://www.cnbcindonesia.com/tech/20210904210634-37-273686/heboh-gb-whatsapp-fakta-dan-bahaya-yang-mengintai-ponselmu)**
- [x] **Example: [/api/v1/cnbc-news-search?query={keywords}](https://flask-scraping-cncbind.herokuapp.com/api/v1/cnbc-news-search?query=vaksin)**

---
Copyright © 2021 by Viqi Nurhaqiqi