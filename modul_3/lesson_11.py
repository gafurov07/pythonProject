import asyncio
import csv
import json
import logging
import sys

import yaml
from aiogram import dispatcher, Dispatcher, types, F, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from redis_dict import RedisDict

# _22 = RedisDict(host='localhost', port=6322)
# _22['_22'] = '22'
# _77 = RedisDict(host='localhost', port=6377)
# _77['_77'] = '77'
# _79 = RedisDict()
# _79['_79'] = '79'
#
# print(_22['_22'])
# print(_77['_77'])
# print(_79['_79'])


TOKEN = '6686631791:AAHmlBvojKMpcUGh3jrmSJfAue8f1-fn8f4'
dp = Dispatcher()
_redis = RedisDict()
ADMIN = 5760868166
_id = ''


def _csv(jjj):
    with open('kkk_bot2.csv', 'w') as file:
        l = [str(_redis.key())]
        # r = dict(_redis.values())
        for k, v in r.items():
            # l.append(k)
            l.append(str(v))
        h = jjj.key()
        data = csv.DictWriter(file, fieldnames=h)
        data.writeheader()
        data.writerows(l)


def _json(database):
    with open('kkk_bot.json', 'w') as file:
        json.dump(dict(database), file, indent=4)


def _yaml(dic):
    with open('kkk_bot3.yml', 'w') as file:
        l = []
        for k, v in dic.items():
            l.append(k)
            l.append(v)
        yaml.dump(l, file, sort_keys=False)


@dp.message(CommandStart())
async def _start(message: types.Message):
    _redis[str(message.from_user.id)] = {
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
    }
    # _redis.clear()
    # print(_redis)
    rkm = ReplyKeyboardBuilder()
    rkm.row(KeyboardButton(text='📞', request_contact=True))
    await message.answer('button orqali nomeringizni jo`nating!', reply_markup=rkm.as_markup(resize_keyboard=True))


@dp.message(F.content_type.in_({types.ContentType.CONTACT}))
async def _contact(message: types.Message):
    l = _redis.pop(str(message.from_user.id))
    l['phone'] = message.contact.phone_number
    _redis.update({str(message.from_user.id): l})
    rkm = ReplyKeyboardBuilder()
    rkm.row(KeyboardButton(text='🌍📌', request_location=True))
    await message.answer('button orqali lokatsiyangizni jo`nating!', reply_markup=rkm.as_markup(resize_keyboard=True))


@dp.message(F.content_type.in_({types.ContentType.LOCATION}))
async def _location(message: types.Message):
    l = _redis.pop(str(message.from_user.id))
    l['address'] = {
        'longitude': str(message.location.longitude),
        'latitude': str(message.location.latitude)
    }
    _redis.update({str(message.from_user.id): l})


@dp.message(F.text == '/admin')
async def _admin(message: types.Message, bot: Bot):
    if message.from_user.id == ADMIN:
        _json(_redis)
        _csv(_redis)
        _yaml(_redis)
        _file = FSInputFile('kkk_bot.json')
        _file2 = FSInputFile('kkk_bot2.csv')
        _file3 = FSInputFile('kkk_bot3.yml')
        await bot.send_document(message.chat.id, _file)
        await bot.send_document(message.chat.id, _file2)
        await bot.send_document(message.chat.id, _file3)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
