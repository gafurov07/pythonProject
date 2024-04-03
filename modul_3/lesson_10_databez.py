'''
docker ps
docker ps -a
docker start container_name (id)
docker stop container_name (id)
docker rm container_name (id)


pip install redis-dict


sudo apt install python3-pip
docker run --name redis_container -p 6379:6379 -it -d redis/redis-stack:latest


venv


tlg1
aiogram2 py3.8


tlg2
aiogram3 py3.11


deactivate

source .venv/bin/activate
. .venv/bin/activate
pip freeze
pip uninstall nomi
pip install nomi
rf - recursive force
which pip

python3 -m venv .venv




venv1 (aiogram, requests)
venv2 (httpx, pyyaml)
venv3 (redis-dict)




'''
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from redis_dict import RedisDict

TOKEN = '6686631791:AAHRCrNXlVOgImMhRINDj1806a5G46D7sKE'
dic777 = RedisDict()
dp = Dispatcher()
admin = 5760868166


@dp.message(CommandStart())
async def start(message: types.Message):
    dic777[str(message.from_user.id)] = f'{message.from_user.full_name}'


@dp.message(F.text == '/admin')
async def _admin(message: types.Message):
    if message.from_user.id == admin:
        res = ''
        for k, v in dic777.items():
            res += f'ID ➖ {k}  ' + f'  FULL_NAME ➖ {v}' + '\n'
        await message.answer(res)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


# class Phone():
#     def __init__(self, color, model, year):
#         self.color = color
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         if self == self.color:
#             return self
#         elif self == self.model:
#             return self
#         elif self == self.year:
#             return self
#
#
# p = Phone('red', 'iphoneX', '2018')
# print(p.color)
# print(p.model)
# print(p.year)
