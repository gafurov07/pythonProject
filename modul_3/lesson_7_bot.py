# import asyncio
# import logging
# import sys
#
# from aiogram import Dispatcher, Bot, types, F
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import InlineKeyboardButton, CallbackQuery
# from aiogram.utils.keyboard import InlineKeyboardBuilder
#
# TOKEN = '6686631791:AAHprCMPnW9nUwgRFaY2y4qgh2aNjvmGg2Y'
# dp = Dispatcher()
# admin = 5760868166
#
#
# class Form(StatesGroup):
#     name = State()
#     age = State()
#     job = State()
#     programming_leng = State()
#     hour = State()
#
#
# @dp.message(CommandStart())
# async def start(message9: types.Message, state: FSMContext):
#     await state.set_state(Form.name)
#     await message9.answer('Ismingizni kirting!')
#
#
# @dp.message(Form.name)
# async def ism_fun(message8: types.Message, state: FSMContext):
#     await state.update_data({'ism ': message8.text})
#     await state.set_state(Form.age)
#     await message8.answer('Yoshingizni kiriting!')
#
#
# @dp.message(Form.age)
# async def age_fun(message0: types.Message, state: FSMContext):
#     await state.update_data({"yosh ": message0.text})
#     await state.set_state(Form.job)
#     await message0.answer('Kasbingizni kiriting!')
#
#
# @dp.message(Form.job)
# async def job_fun(message1: types.Message, state: FSMContext):
#     await state.update_data({"kasb ": message1.text})
#     await state.set_state(Form.programming_leng)
#     await message1.answer('Qaysi dasturlash tillarini bilasiz ?')
#
#
# @dp.message(Form.programming_leng)
# async def programming_length_fun(message2: types.Message, state: FSMContext):
#     await state.update_data({"siz biladigan dasturlash tillari ": message2.text})
#     await state.set_state(Form.hour)
#     await message2.answer('Qaysi vaqt sizga maqul ?')
#
#
# @dp.message(Form.hour)
# async def hour_fun(message3: types.Message, state: FSMContext):
#     await state.update_data({"sizga maqul vaqt ": message3.text})
#     data = await state.get_data()
#     await state.clear()
#
#     res = f"MALUMOTLAR TO'G'RIMI:\n"
#     for k, v in data.items():
#         res += k + ' : ' + v + '\n'
#
#     rr = InlineKeyboardBuilder()
#     rr.add(InlineKeyboardButton(text='XA', callback_data='xa'), InlineKeyboardButton(text="YO'Q", callback_data='yoq'))
#     await message3.answer(res, reply_markup=rr.as_markup())
#
#
# @dp.callback_query(F.data == 'xa')
# async def xa_callback(callback: CallbackQuery, bot: Bot):
#     await bot.copy_message(admin, callback.message.chat.id, callback.message.message_id)
#
#
# @dp.callback_query(F.data == 'yoq')
# async def yoq_callback(callback: CallbackQuery):
#     await callback.answer("Dastur tugatildi!\nboshidan boshlash uchun /start camandasini yozing!")
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
