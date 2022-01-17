import requests

from bs4 import BeautifulSoup

import os

from string import punctuation

from re import sub


def make_file_name(name):
    punctuation_amp = punctuation + '’' + '—'
    new_name = name.translate(str.maketrans('', '', punctuation_amp))
    new_name = sub(r'\s+', '_', new_name)
    return f'{new_name}.txt'


base_url = 'https://www.nature.com'
saved_articles = []

pages = int(input())
article_type = input()

for num_page in range(1, pages + 1):
    url = base_url + f'/nature/articles?sort=PubDate&year=2020&page={str(num_page)}'
    r = requests.get(url)

    if r:
        dir_name = f'Page_{str(num_page)}'
        os.mkdir(dir_name)

        tree = BeautifulSoup(r.content, 'html.parser')

        for item in tree.find_all('article'):
            if item.find('span', class_='c-meta__type').text == article_type:
                a_tag = item.find('a')
                article_page_tree = BeautifulSoup(requests.get(base_url + a_tag['href']).content, 'html.parser')
                article_body = article_page_tree.find('div', class_='c-article-body')

                file_name = make_file_name(a_tag.text.strip())
                file = open(os.path.join(dir_name, file_name), 'wb')
                file.write(article_body.text.strip().encode('utf-8'))
                file.close()

                saved_articles.append(file_name)
    else:
        print(f'Error in request; status code: {r.status_code}')

print('Saved articles:', saved_articles, sep='\n')
