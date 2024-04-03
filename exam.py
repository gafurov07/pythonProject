import asyncpg
import asyncio
import requests

jp = 'https://jsonplaceholder.typicode.com/users'


async def auto_create_table(url):
    conn = await asyncpg.connect(
        user='postgres',
        password='1',
        database='dvdrental',
        host='localhost',
        port='5432'
    )

    web = requests.get(url).json()
    _keys = [i for i in web[0].keys()]
    s = ''
    name_table = url.split('/')[-1]
    for i in _keys:
        if i.endswith('id') or i.endswith('Id'):
            if i == 'id':
                s += i + ' INTEGER PRIMARY KEY, '
            elif i != _keys[-1]:
                s += i + ' INTEGER, '
            else:
                s += i + ' INTEGER'
        else:
            if i != _keys[-1]:
                s += i + ' TEXT, '
            else:
                s += i + ' TEXT'

    try:
        query1 = f"""
            DROP TABLE IF EXISTS {name_table}
            """
        await conn.fetch(query1)
    except Exception as e:
        print(e)

    try:
        query = f"""
            CREATE TABLE IF NOT EXISTS {name_table}({s});
            """
        await conn.fetch(query)
    except Exception as e:
        print(e)

    dollar = ''
    for i in range(1, len(web[0]) + 1):
        if i < len(web[0]):
            dollar += ('$' + str(i) + ', ')
        else:
            dollar += ('$' + str(i))
    for i in web:
        lis = []
        for j in i.values():
            if type(j) == bool or type(j) == dict:
                lis.append(str(j))
                continue
            lis.append(j)
        res_query = f"""
            INSERT INTO {name_table} VALUES ({dollar})
            """
        await conn.execute(res_query, *lis)


asyncio.run(auto_create_table(jp))
