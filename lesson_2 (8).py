# # task-1
# import asyncio
# import os
# import aiofiles
#
# exclude = ('.idea', 'venv', '.git', '.DS_Store', 'p19-gruppa.db', '.dockerignore', '.gitignore', '__pycache__')
#
#
# async def recursive_check(path: str, l: list):
#     counter = 0
#     if len(l):
#         for i in l:
#             if i in exclude:
#                 continue
#             _path = os.path.join(path, i)
#             print(_path)
#             if os.path.isdir(_path):
#                 counter += await recursive_check(_path, os.listdir(_path))
#             else:
#                 async with aiofiles.open(_path) as f:
#                     counter += len(await f.read())
#     return counter
#
#
# if __name__ == '__main__':
#     os.chdir('..')
#     result = asyncio.run(recursive_check(os.getcwd(), os.listdir()))
#     print(result)


import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect('postgresql://postgres:1@localhost:5432/dvdrental')
    # conn = await asyncpg.connect('postgresql://user:pass@host:port/dbname')
    # conn = await asyncpg.connect(
    #     user='postgres',
    #     password='1',
    #     database='dvdrental',
    #     host='localhost',
    #     port='5432'
    # )
    # Execute a statement to create a new table.
    # query = '''
    #     CREATE TABLE IF NOT EXISTS new_country(
    #         country_id  SERIAL PRIMARY KEY ,
    #         country     varchar(50)                                                   not null,
    #         last_update timestamp default now()
    #     );
    # '''
    # await conn.execute(query)
    #
    # # # CREATE
    # first_name = 'Botirjon'
    # last_name = 'Botirov'
    # query = 'INSERT INTO student(first_name, last_name) VALUES($1, $2) RETURNING *;'
    # result = await conn.fetchrow(query, first_name, last_name)
    # print(result)

    # # READ
    # query = 'SELECT * FROM student WHERE id = 1;'
    # students = await conn.fetch(query)
    # for student in students:
    #     print(student, student['id'], student[1], student[2])

    # # UPDATE
    # _id = 3
    # first_name = 'Tohirjon'
    # query = f'UPDATE student SET first_name=$1 WHERE id=$2'
    # await conn.execute(query, first_name, _id)

    # # DELETE
    # query = 'DELETE FROM student WHERE id = $1;'
    # await conn.execute(query, 2)


    query = 'SELECT * FROM country;'
    countries = await conn.fetch(query)

    vowels = 'auioe'
    results = []
    for country in countries:
        if sum(i in vowels for i in country['country'].lower()) > 3:
            results.append(country)

    await conn.executemany('INSERT INTO new_country VALUES ($1, $2, $3)', results)
    await conn.close()


asyncio.get_event_loop().run_until_complete(main())


'''
1-task
dvdrentaldagi countryni new_country nomli tablega 
(country nomida 3tadan kop unli bolganlarini) asyncpg orqali otkazish kk
vowels = 'oiuea'


2-task create table
jsonplaceholder

/posts	100 posts
/comments	500 comments
/albums	100 albums
/photos	5000 photos
/todos	200 todos
/users	10 users


3-task
jsonplaceholder dagi
auto generate


user_id integer
id integer primary key
title text
body text


post_id integer
id integer primary key
name text
email text
body text
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  
  {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusan
}

  {
    "userId": 1,
    "id": 1,
    "title": "quidem molestiae enim"
  },
'''



