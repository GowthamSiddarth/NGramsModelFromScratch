from urllib import request
from bs4 import BeautifulSoup


def get_text_from_url(url):
    raw_html = request.urlopen(url).read()
    article_html = BeautifulSoup(raw_html, 'html.parser')
    return ''.join([paragraph.text for paragraph in article_html.find_all('p')])


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Tennis"
    article_text = get_text_from_url(URL)
    print(article_text)
