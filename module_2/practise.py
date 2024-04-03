# import json
# import requests
#
# users = requests.get('https://jsonplaceholder.typicode.com/users').json()
# posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
# comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
#
# for user in users:
#     user['posts'] = list(filter(lambda post: post['userId'] == user['id'], posts))
#
# for user in users:
#     for post in user['posts']:
#         post['comments'] = list(filter(lambda comment: comment['postId'] == post['id'], comments))
#
# file = open('users.json', 'w')
# json.dump(users, file, indent=4)
# file.close()


# class Photo:
#     def __init__(self, album_id, id_, title, url, thumbnain_url):
#         self.albumId = album_id
#         self.id_ = id_
#         self.url = url
#         self.thumbnain_url = thumbnain_url
#         self.title = title
#     def __str__(self):
#         return f'{self.albumId} \n{self.id_} \n{self.url} \n{self.thumbnain_url} \n{str(self.title)}'
#
#
# data = requests.get('https://jsonplaceholder.typicode.com/photos/1').json()
# a = Photo(data['albumId'], data['id'], data['title'], data['url'], data['thumbnailUrl'])
# print(a)

#
# import json
# import requests
# import yaml
#
# posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
# comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
# albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()
# photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
# todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# users = requests.get('https://jsonplaceholder.typicode.com/users').json()
#
# with open('posts.yaml', 'w') as f:
#     yaml.dump(posts, f, sort_keys=False)
#
# with open('comments.yaml', 'w') as f:
#     yaml.dump(comments, f, sort_keys=False)
#
# with open('albums.yaml', 'w') as f:
#     yaml.dump(albums, f, sort_keys=False)
#
# with

#
# import json
# import requests
# import yaml
# l = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']
# for i in l:
#     u = requests.get(f'https://jsonplaceholder.typicode.com/{i}').json()
#     with open(f'{i}.yaml', 'w') as f:
#         yaml.dump(u, f, sort_keys=False)


# import json
# import yaml
# import csv
# import requests
#
# url = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# r = url[0].keys()
#
# with open('users.json', 'w') as f:
#     json.dump(url, f, indent=4)
#
# with open('resul.yaml', 'w') as f:
#     yaml.dump(url, f, sort_keys=False)
#
# with open('resu.csv', 'w') as f:
#     d = csv.DictWriter(f, fieldnames=r)
#     d.writeheader()
#     d.writerows(url)


import os
# file = open('ddaata.txt', 'r')
# file = file.read().split('https://')

# n = list(input().split())
# d = ''
#
# for i in range(len(n)):
#     if n[+] != n[i+1]:
#         n[i].swapcase()

# for i in range(4):
#     print(i[])
# for i in n:
#     print(n[])
#     if  in d:
    #     d += i
# print(d)