from urllib import request
from bs4 import BeautifulSoup
import re


def get_text_from_url(url):
    raw_html = request.urlopen(url).read()
    article_html = BeautifulSoup(raw_html, 'lxml')
    return ''.join(article_html.find_all('p')).lower()


def clean_text(text):
    return re.sub(r'[^A-Za-z. ]', '', text)


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Tennis"
    article_text = get_text_from_url(URL)
    article_text = clean_text(article_text)
