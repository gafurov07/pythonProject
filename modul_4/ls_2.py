import csv
import json

import requests

url = 'https://jsonplaceholder.typicode.com/'
l = ['posts', 'comments', 'albums', 'photos', 'todos']

for i in l:
    with open(f'{i}.csv', 'w') as outfile:
        url_2 = requests.get(f'{url}{i}').json()
        w = csv.DictWriter(outfile, fieldnames=url_2[0].keys(), delimiter=',')
        w.writeheader()
        w.writerows(url_2)
