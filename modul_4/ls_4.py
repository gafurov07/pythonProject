# import csv
# import json
#
# l_file_names = ['actor', 'address', 'albums', 'category', 'city', 'comments', 'country', 'customer', 'district', 'film',
#                 'film_actor', 'film_category', 'inventory', 'language', 'payment', 'photos', 'posts', 'prak_users',
#                 'prak_users_export', 'region', 'rental', 'staff', 'store', 'todos']
# for i in l_file_names:
#     with open(f'{i}.csv', 'r') as csvfile:
#         r = list(csv.DictReader(csvfile))
#         res = []
#         for p in r:
#             res.append(p)
#         with open(f'{i}.json', 'w') as file:
#             json.dump(res, file, indent=4)
import csv

import requests
import json

url_user = requests.get('https://jsonplaceholder.typicode.com/users').json()
r = ''
header = url_user[0].keys()
with open('user.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for j in url_user:
        writer.writerow(
            [j['id'], j['name'], j['username'], j['email'], json.dumps(j['address']), j['phone'], j['website'],
             json.dumps(j['company'])])
