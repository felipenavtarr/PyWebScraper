import requests

url = input()
file = open('source.html', 'wb')
r = requests.get(url)

if r.status_code == 200:
    file.write(r.content)
    file.close()
    print('Content saved')
else:
    print(f'The URL returned {r.status_code}')
