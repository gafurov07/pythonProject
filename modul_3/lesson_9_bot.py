import asyncio
import json
import logging
import smtplib
import ssl
import sys
from random import randint

from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import CommandStart
from aiogram.fsm import state
from aiogram.types import KeyboardButton, InlineKeyboardButton, InputMediaPhoto, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# TOKEN = '6686631791:AAHRCrNXlVOgImMhRINDj1806a5G46D7sKE'
# dp = Dispatcher()
# l = ['Car', 'Telephone', 'Computer', 'Motorcycles']
# file = json.load(open('product.json'))
# soni = 0
# narxi = 0
# narsani_narxi = 0
# ikkinchi_rasm = ''
# eski_rasm = ''
# eski_caption = ''
# spiska = f'savatda:\nmaxsulot soni : {soni}\nobshiy summa : {narxi}'
#
#
# def _send_email(to_email: str, message: str):
#     port = 465  # For SSL 65535
#     my_email = 'gafurovfaxriddin395@gmail.com'
#     my_password = 'idclrtxgmfiqdtsv'
#     host = 'smtp.gmail.com'
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(host, port, context=context) as server:
#         server.login(my_email, my_password)
#         server.sendmail(my_email, to_email, message)
#
#
# @dp.message(CommandStart())
# async def start2(message: types.Message):
#     global soni, narxi, narsani_narxi
#     soni = 0
#     narxi = 0
#     narsani_narxi = 0
#     rkm = ReplyKeyboardBuilder()
#     for i in l:
#         rkm.row(KeyboardButton(text=i))
#     await message.answer('Quyidagi kategoryalardan birini tanlang.',
#                          reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message(F.text == '⬅️ Orqaga')
# async def start(message: types.Message):
#     rkm = ReplyKeyboardBuilder()
#     for i in l:
#         rkm.row(KeyboardButton(text=i))
#     await message.answer('Quyidagi kategoryalardan birini tanlang.',
#                          reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message(lambda message: message.text in l)
# async def product(message: types.Message):
#     rkm = ReplyKeyboardBuilder()
#     for i in file:
#         r = i['category']
#         if message.text == r:
#             for j in i['brands']:
#                 rkm.add(KeyboardButton(text=j))
#             rkm.row(KeyboardButton(text='⬅️ Orqaga'))
#             break
#     await message.answer('Tanlang!', reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.message()
# async def product2(message: types.Message, bot: Bot):
#     hh = ''
#     hh2 = ''
#     t_text = ''
#     n = 0
#     rkm = InlineKeyboardBuilder()
#     for i in file:
#         r = i['brands']
#         for h in r:
#             if message.text == h:
#                 hh += r[f'{h}']['photo_url']
#                 hh2 += r[f'{h}']['photo_url2']
#                 t_text += r[f'{h}']['text']
#                 n = r[f'{h}']['price']
#     global narsani_narxi, ikkinchi_rasm, eski_rasm, eski_caption
#     eski_rasm = hh
#     eski_caption = t_text
#     ikkinchi_rasm = hh2
#     narsani_narxi = n
#     rkm.add(*[
#         InlineKeyboardButton(text='⬅️', callback_data='orqaga'),
#         InlineKeyboardButton(text='➕', callback_data='plus'),
#         InlineKeyboardButton(text='➡️', callback_data='oldinga')
#     ])
#     rkm.row(InlineKeyboardButton(text=f'savat(soni: {soni}) narxi: {narxi}', callback_data='savat_bosildi'))
#     rkm.row(InlineKeyboardButton(text='Sotib olingan narsalar royxatini gmailga yuborish', callback_data='gmailga_go'))
#     await bot.send_photo(message.from_user.id, hh, caption=t_text, reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.callback_query(F.data == 'plus')
# async def plus(callback: types.CallbackQuery):
#     global narxi, narsani_narxi, soni
#     soni += 1
#     narxi += narsani_narxi
#     await callback.answer('bita maxsulot qoshildi')
#     rkm = InlineKeyboardBuilder()
#     rkm.add(*[
#         InlineKeyboardButton(text='⬅️', callback_data='orqaga'),
#         InlineKeyboardButton(text='➕', callback_data='plus'),
#         InlineKeyboardButton(text='➡️', callback_data='oldinga')
#     ])
#     rkm.row(InlineKeyboardButton(text=f'savat(soni: {soni}) narxi: {narxi}', callback_data='savat_bosildi'))
#     rkm.row(InlineKeyboardButton(text='Sotib olingan narsalar royxatini gmailga yuborish', callback_data='gmailga_go'))
#     await callback.message.edit_reply_markup(callback.inline_message_id,
#                                              reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.callback_query(F.data == 'oldinga')
# async def oldinga_callback(callback: types.CallbackQuery, bot: Bot):
#     global ikkinchi_rasm
#     rkm = InlineKeyboardBuilder()
#     rkm.add(*[
#         InlineKeyboardButton(text='⬅️', callback_data='orqaga'),
#         InlineKeyboardButton(text='➕', callback_data='plus'),
#         InlineKeyboardButton(text='➡️', callback_data='oldinga')
#     ])
#     inputmedia = InputMediaPhoto(media=ikkinchi_rasm, caption=f'2-rasm')
#     rkm.row(InlineKeyboardButton(text=f'savat(soni: {soni}) narxi: {narxi}', callback_data='savat_bosildi'))
#     rkm.row(InlineKeyboardButton(text='Sotib olingan narsalar royxatini gmailga yuborish', callback_data='gmailga_go'))
#     await bot.edit_message_media(inputmedia, callback.from_user.id, callback.message.message_id,
#                                  reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.callback_query(F.data == 'savat_bosildi')
# async def savat(message: types.Message):
#     await message.answer(f'savatda:\nmaxsulot soni : {soni}\nobshiy summa : {narxi}')
#
#
# @dp.callback_query(F.data == 'orqaga')
# async def orqaga(callback: types.CallbackQuery, bot: Bot):
#     rkm = InlineKeyboardBuilder()
#     global eski_rasm, eski_caption
#     rkm.add(*[
#         InlineKeyboardButton(text='⬅️', callback_data='orqaga'),
#         InlineKeyboardButton(text='➕', callback_data='plus'),
#         InlineKeyboardButton(text='➡️', callback_data='oldinga')
#     ])
#     inputmedia = InputMediaPhoto(media=eski_rasm, caption=eski_caption)
#     rkm.row(InlineKeyboardButton(text=f'savat(soni: {soni}) narxi: {narxi}', callback_data='savat_bosildi'))
#     rkm.row(InlineKeyboardButton(text='Sotib olingan narsalar royxatini gmailga yuborish', callback_data='gmailga_go'))
#     await bot.edit_message_media(inputmedia, callback.from_user.id, callback.message.message_id,
#                                  reply_markup=rkm.as_markup(resize_keyboard=True))
#
#
# @dp.callback_query(F.data == 'gmailga_go')
# async def gmailga_go(callback: types.CallbackQuery, bot: Bot):
#     await callback.answer('Pochta manzilingizni kiriting')
#
#
# @dp.message(F.text.endswith('.com'))
# async def com(message: types.Message):
#     data = await state.get_data(gw)
#     code = str(randint(100000, 999999))
#     data['code'] = code
#     users[message.from_user.id] = data
#     rkm = ReplyKeyboardRemove()
#     try:
#         _send_email(data['email'], code)
#         await message.answer('Pochtangizga tasdiqlash uchun kod yuborildi', reply_markup=rkm)
#     except Exception as e:
#         await message.answer('Pochta xato kiritilgan!')
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
#