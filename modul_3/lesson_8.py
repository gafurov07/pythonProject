# import asyncio
# import logging
# import sys
#
# from aiogram import Dispatcher, types, Bot
#
# import smtplib
# import ssl
# from random import random, randint
#
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
#
# TOKEN = '6686631791:AAEjXukAE4L8C2XAF-akYrvMVvQnTs9OHBc'
#
# admin = 5760868166
#
# dp = Dispatcher()
# d = str(randint(999, 10000))
#
# port = 465  # For SSL
# my_email = 'azizbekisaboyev68@gmail.com'
# my_password = 'bakhpafcokimhuxf'
#
#
# class Form(StatesGroup):
#     name = State()
#     email = State()
#     password = State()
#
#
# @dp.message(CommandStart())
# async def start(message: types.Message, state: FSMContext):
#     await state.set_state(Form.name)
#     await message.answer("ismingizni kiriting :")
#
#
# @dp.message(Form.name)
# async def f_i_o(message: types.Message, state: FSMContext):
#     await state.update_data({'F.I.O INGIZ ': message.text})
#     await state.set_state(Form.email)
#     await message.answer("emailingizni kiriting :")
#
#
# @dp.message(Form.email)
# async def f_i_o(message: types.Message, state: FSMContext):
#     await state.update_data({'emailingiz ': message.text})
#     await state.set_state(Form.password)
#     await message.answer("nomeringizni KIRITING  :")
#
# @dp.message(Form.password)
# async def f_i_o(message: types.Message, state: FSMContext):
#     await state.update_data({'passwordingiz ': message.text})
#     data = await state.get_data()
#     await state.clear()
#
#     r_password = d
#
#     context = ssl.create_default_context()
#
#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#         server.login(my_email, my_password)
#         server.sendmail(my_email, data['emailingiz '], r_password)
#         print('pochtaga yuborildi!')
#
#     @dp.message()
#     async def shrfhe(message77: types.Message):
#         await message77.answer('passwordni kiriting:')
#
#
#     @dp.message()
#     async def shrfhe(message77: types.Message):
#         if message77.text == d:
#             await message77.answer('togri')
#         else:
#             await message77.answer('xato')
#
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
import datetime

# import asyncio
# import logging
# import smtplib
# import ssl
# import sys
# from random import randint
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.enums import content_type
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
# from aiogram.utils.keyboard import ReplyKeyboardBuilder
#
# TOKEN = '6686631791:AAEjXukAE4L8C2XAF-akYrvMVvQnTs9OHBc'  # testing_io_bot
# dp = Dispatcher()
# r = ''
# def _send_email(to_email: str, message: str):
#     www = ''
#     try:
#         port = 465  # For SSL 65535
#         my_email = 'xolmomin@gmail.com'
#         my_password = 'eczlqwynvuhwzynq'
#         host = 'smtp.gmail.com'
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL(host, port, context=context) as server:
#             server.login(my_email, my_password)
#             server.sendmail(my_email, to_email, message)
#
#     except Exception as e:
#         ww('xato')
#
#
# class Form(StatesGroup):
#     name = State()
#     phone = State()
#     email = State()
#
#
# users = {}
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message, state: FSMContext) -> None:
#     await state.set_state(Form.name)
#     await message.answer('Ismingiz kiriting')
#
#
# @dp.message(Form.name)
# async def command_start_handler(message: Message, state: FSMContext) -> None:
#     await state.set_data({'name': message.text})
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(KeyboardButton(text='Nomer yuborish📞', request_contact=True))
#
#     await state.set_state(Form.phone)
#     await message.answer('Telefon nomeringizni kiriting', reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message(Form.phone, F.content_type.in_(content_type.ContentType.CONTACT))
# async def command_start_handler(message: Message, state: FSMContext) -> None:
#     await state.set_data({'phone': message.text})
#     await state.set_state(Form.email)
#     await message.answer('Pochtangizni kiriting')
#
#
# @dp.message(Form.email)
# async def command_start_handler(message: Message, state: FSMContext) -> None:
#     await state.set_data({'email': message.text})
#     data = await state.get_data()
#     await state.clear()
#     code = str(randint(100000, 999999))
#     data['code'] = code
#     users[message.from_user.id] = data
#     _send_email(data['email'], code)
#     rkm = ReplyKeyboardRemove()
#     await message.answer('Pochtangizga tasdiqlash uchun kod yuborildi', reply_markup=rkm)
#
#
# @dp.message(F.text.func(lambda text: len(text) == 6 and text.isdigit()))
# async def command_start_handler(message: Message) -> None:
#     code = message.text
#     user = users.get(message.from_user.id)
#     if user and user['code'] == code:
#         await message.answer('Tasdiqlandi ✅')
#     else:
#         await message.answer('Xato qaytadan kiriting')
#
#
# @dp.message()
# async def command_start_handler(message: Message) -> None:
#     await message.answer(r)
#
#
# async def main() -> None:
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())


# d = datetime.date(year=2008, month=5, day=23)
# print(datetime.date.today() - d)
