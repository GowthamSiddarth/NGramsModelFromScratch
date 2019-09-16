from urllib import request
from bs4 import BeautifulSoup
import re


def get_text_from_url(url):
    raw_html = request.urlopen(url).read()
    article_html = BeautifulSoup(raw_html, 'lxml')
    return ''.join(article_html.find_all('p')).lower()


def clean_text(text):
    return re.sub(r'[^A-Za-z. ]', '', text)


def get_character_n_gram_model(text, n=3):
    n_grams = {}
    for i in range(len(text) - n):
        seq = text[i, i + n]
        if seq not in n_grams.keys():
            n_grams[seq] = []

        n_grams[seq].append(text[i + n])
    return n_grams


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Tennis"
    article_text = get_text_from_url(URL)
    article_text = clean_text(article_text)

    n_grams = get_character_n_gram_model(article_text)
