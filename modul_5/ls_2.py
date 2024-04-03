import asyncio
import asyncpg


async def main():
    con = await asyncpg.connect(
        user='postgres',
        password='1',
        database='dvdrental',
        host='localhost',
        port='5432'
    )

    # query = '''
    #     CREATE TABLE IF NOT EXISTS country_2
    #     (
    #         country_id  INTEGER PRIMARY KEY,
    #         country     VARCHAR(50),
    #         last_update timestamp
    #     );
    # '''
    # await con.execute(query)
    # await con.execute("")

    q = "SELECT * FROM country"
    s = await con.fetch(q)
    l = []
    unli = 'aouie'
    for i in s:
        n = 0
        for j in i['country']:
            if j in unli:
                n += 1
        if n > 3:
            # query = f"INSERT INTO country_2(country_id, country, last_update) VALUES ($1, $2, $3)"
            # await con.execute(query, i['country_id'], i['country'], i['last_update'])
            l.append(i['country_id'])
            l.append(i['country'])
            l.append(i['last_update'])
    query = f"INSERT INTO country_2(country_id, country, last_update) VALUES ($1, $2, $3)"
    await con.executemany(query, l)
    await con.close()

asyncio.run(main())
