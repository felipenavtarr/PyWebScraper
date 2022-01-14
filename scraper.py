import requests

from bs4 import BeautifulSoup

from string import punctuation

from re import sub


def make_file_name(name):
    punctuation_amp = punctuation + '’' + '—'
    new_name = name.translate(str.maketrans('', '', punctuation_amp))
    new_name = sub(r'\s+', '_', new_name)
    return f'{new_name}.txt'


base_url = 'https://www.nature.com'
url = base_url + '/nature/articles?sort=PubDate&year=2020&page=3'
saved_articles = []

r = requests.get(url)

if r:
    tree = BeautifulSoup(r.content, 'html.parser')

    for item in tree.find_all('article'):
        if item.find('span', class_='c-meta__type').text == 'News':
            a_tag = item.find('a')
            file_name = make_file_name(a_tag.text.strip())
            article_page_tree = BeautifulSoup(requests.get(base_url + a_tag['href']).content, 'html.parser')
            article_body = article_page_tree.find('div', class_='c-article-body')
            file = open(file_name, 'wb')
            file.write(article_body.text.strip().encode('utf-8'))
            file.close()
            saved_articles.append(file_name)

    print('Saved articles:', saved_articles, sep='\n')
else:
    print(f'Error in request; status code: {r.status_code}')
