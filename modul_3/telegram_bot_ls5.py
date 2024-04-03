# from aiogram.fsm.state import StatesGroup, State
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
# import asyncio
# import logging
# import sys
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.enums import ParseMode
# from aiogram.types import Message, KeyboardButton
# from aiogram.filters import CommandStart
# from aiogram.utils.markdown import hbold
#
# TOKEN = '6695482833:AAEH5vAe1rcq_-9AlcvdDhIuX-IRdXZ3pTs'
#
# admin = 5760868166
#
# dp = Dispatcher()
# d = {}
#
#
# class Form(StatesGroup):
#     name = State()
#     email = State()
#     phone_number = State()
#
#
# @dp.message(CommandStart())
# async def start(message: types.Message):
#
#
# async def main() -> None:
#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
