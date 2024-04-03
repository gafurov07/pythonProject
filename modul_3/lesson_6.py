
# from aiogram import Dispatcher, F
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from telebot.formatting import hbold
#
# token = '6695482833:AAEH5vAe1rcq_-9AlcvdDhIuX-IRdXZ3pTs'
# dp = Dispatcher()
#
# d = {}
# admin = ''
#
#
# @dp.message(CommandStart())
# async def echo_start_handler(message: Message) -> None:
#     await message.answer(f"Hello {hbold(message.from_user.full_name)}, welcome to my bot")
#     d[message.from_user.id] = message.from_user.first_name
#
#
# # @dp.message(F.text == '/admin')
