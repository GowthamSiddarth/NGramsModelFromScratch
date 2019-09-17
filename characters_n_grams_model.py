import random
import re
from urllib import request

from bs4 import BeautifulSoup


def get_text_from_url(url):
    raw_html = request.urlopen(url).read()
    article_html = BeautifulSoup(raw_html, 'html.parser')
    return ''.join([paragraph.text for paragraph in article_html.find_all('p')]).lower()


def clean_text(text):
    return re.sub(r'[^A-Za-z. ]', '', text)


def get_character_n_gram_model(text, n=3):
    n_grams = {}
    for i in range(len(text) - n):
        seq = text[i: i + n]
        if seq not in n_grams.keys():
            n_grams[seq] = []

        n_grams[seq].append(text[i + n])
    return n_grams


def generate_predictive_text(text, n_grams, n=3):
    curr_seq = text[:n]
    output = curr_seq

    for i in range(200):
        if curr_seq not in n_grams.keys():
            break

        possible_chars = n_grams[curr_seq]
        next_char = possible_chars[random.randrange(len(possible_chars))]
        output = output + next_char
        curr_seq = output[i + 1: len(output)]

    return output


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Tennis"
    article_text = get_text_from_url(URL)
    article_text = clean_text(article_text)

    n_grams = get_character_n_gram_model(article_text)
    predictive_text = generate_predictive_text(article_text, n_grams)
    print(predictive_text)
