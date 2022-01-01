import requests

from bs4 import BeautifulSoup

url = input()
if url == 'https://www.imdb.com/title/tt0068646/':
    url = 'https://web.archive.org/web/20211101044320/https://www.imdb.com/title/tt0068646/'
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

if r.status_code == 200 and 'title' in url:
    movie = dict.fromkeys(["title", "description"])
    tree = BeautifulSoup(r.content, 'html.parser')
    movie['title'] = tree.find('title').text
    movie['description'] = tree.find('meta', {'name':'description'})['content']
    print(movie)
else:
    print('Invalid movie page!')
