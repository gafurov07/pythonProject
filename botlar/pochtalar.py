import asyncio
import logging
import smtplib
import ssl
import sys

from aiogram import Dispatcher, Bot, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from redis_dict import RedisDict

d = RedisDict()
TOKEN = '6686631791:AAHRCrNXlVOgImMhRINDj1806a5G46D7sKE'
dp = Dispatcher()
ADMIN = 5760868166
my_email = 'azizbekisaboyev68@gmail.com'
my_password = 'bakhpafcokimhuxf'

def send_gmail_message(pochta: str, message: int):
    port = 465  # For SSL 65535
    host = 'smtp.gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(my_email, my_password)
        server.sendmail(my_email, pochta, str(message))


@dp.message(CommandStart())
async def on_message(message: types.Message):
    await message.answer('Po`chta manzilingizni kiriting')


@dp.message(F.text.endswith('.com'))
async def on_text_command(message: types.Message):
    d[str(message.from_user.id)] = message.text
    await message.answer('muvafaqiyatli')


@dp.message(F.text == '/admin')
async def on_admin(message: types.Message):
    n = 0
    if message.from_user.id == ADMIN:
        for k, v in d.items():
            n += 1
            send_gmail_message(k, v)
        await message.answer(f'TAYYOR AKA, {n} ta po`chta manzilga textlar jo`natildi')
    await message.answer(str(d))


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
