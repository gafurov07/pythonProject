# # import csv
# # import json
# #
# # with open('regions.json', 'w') as f2:
# #     json.dump(list(csv.DictReader(open('regions.csv', encoding='utf-8-sig'))), f2, indent=2)
# # import requests
# # import sqlite3
# #
# # posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
# # print(posts)
# import os
# # con = sqlite3.connect("dvdrental.db")
# # cur = con.cursor()
# # cur.execute("CREATE TABLE posts(user_id integer, id integer unique , title varchar (255), body text)")
#
# # pp = cur.execute("SELECT * FROM posts;")
# # print(pp.fetchall())
#
# # cur.executemany("INSERT INTO posts VALUES (:userId, :id, :title, :body)", posts)
#
# # res = cur.execute("SELECT * FROM posts")
# # res.fetchone()
#
# # con.commit()
#
#
# # HOMEWORK
#
# import sqlite3
#
# # m = os.listdir('/home/faxriddin/PycharmProjects/module_2/pythonProject/')
# # home = '/home/faxriddin/PycharmProjects/module_2/pythonProject/'
# #
# # # print(os.listdir('/home/faxriddin/PycharmProjects/module_2/pythonProject/p19_faxriddin_gafurov.zip/'))
# #
# # for i in m:
# #     print(os.listdir(f'{home}{i}/'))
# #     print(i)
#
#
# # 2
#
# import sqlite3
#
# con = sqlite3.connect("dvdrental.db")
# cur = con.cursor()
# # cur.execute("CREATE TABLE posts(user_id integer, id integer unique , title varchar (255), body text)")
# # cur.executemany("INSERT INTO posts VALUES (:userId, :id, :title, :body)", posts)
# # res = cur.execute("SELECT * FROM posts")
# # res.fetchone()
# # con.commit()
#
# menu = '''    1. table yaratish
#     2. ustun qoshish
#     3. table larni korish
#     4. table ga malumot qoshish
#     5. tabledagi malumotni update qilish
#     6. table dagi malumotni ochirish
#     0. exit
# '''
#
# while True:
#     key = input(menu)
#     if key == '1':
#         name_table = input('Input name of table: ')
#         try:
#             cur.execute(f"CREATE TABLE {name_table}(id integer primary key autoincrement);")
#             print('Table created successfully!')
#         except sqlite3.OperationalError:
#             print('Table already created')
#         con.commit()
#
#     elif key == '2':
#         cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = cur.fetchall()
#         print(tables)
#         con.commit()
#
#     elif key == '4':
#         t_n = input('Input name of table: ')
#         try:
#             cur.execute(f"PRAGMA table_info({t_n});")
#             r = list(cur.fetchall())
#             res = [f":{i[1]}" for i in r]
#             res2 = [input(f"{i[1:]}: ") if i[2] != 'INTEGER' else (int(input(i[1:]))) for i in res]
#             cur.executemany("INSERT INTO {t_n} VALUES ({res})", res2)
#             con.commit()
#         except sqlite3.OperationalError:
#             print('ERROR!!!')
#
#     elif key == '0':
#         break

