import nltk
import random
import re
from urllib import request

from bs4 import BeautifulSoup


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

    return n_grams, words


def generate_predictive_text(words, n_gram_model, n=3):
    curr_seq = ' '.join(words[:n])
    output = curr_seq
    seq_words = nltk.word_tokenize(output)
    for i in range(200):
        if curr_seq not in n_grams_model.keys():
            break

        possible_words = n_grams_model[curr_seq]
        next_word = possible_words[random.randrange(len(possible_words))]
        output = output + ' ' + next_word
        seq_words = nltk.word_tokenize(output)
        curr_seq = ' '.join(seq_words[i + 1: len(seq_words)])

    return seq_words


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Tennis"
    article_text = get_text_from_url(URL)
    article_text = clean_text(article_text)

    n_grams_model, words = get_n_grams_model(article_text)
    predictive_text = generate_predictive_text(words, n_grams_model)
    print(predictive_text)
