from urllib import request
from bs4 import BeautifulSoup
import re, nltk


def get_text_from_url(url):
    raw_html = request.urlopen(url).read()
    article_html = BeautifulSoup(raw_html, 'html.parser')
    return ''.join([paragraph.text for paragraph in article_html.find_all('p')])


def clean_text(text):
    return re.sub(r'[^A-Za-z. ]', '', text)


def get_n_grams_model(text, n=3):
    n_grams = {}
    words = nltk.word_tokenize(text)
    for i in range(len(words) - n):
        seq = ' '.join(words[i: i + n])
        if seq not in n_grams.keys():
            n_grams[seq] = []

        n_grams[seq].append(words[i + n])

    return n_grams


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Tennis"
    article_text = get_text_from_url(URL)
    article_text = clean_text(article_text)

    n_grams_model = get_n_grams_model(article_text)
    print(n_grams_model)
