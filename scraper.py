import requests

url = input()
r = requests.get(url)
load = r.json()
if r.status_code == 200 and 'content' in load:
    print(load['content'])
else:
    print('Invalid quote resource!')
