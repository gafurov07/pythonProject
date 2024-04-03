import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.methods import SendPoll
from aiogram.types import Message, Poll, PollAnswer, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = '6686631791:AAFZ98zLIGfQWoaKxGqzI2uteVRxhdXPu8k'
dp = Dispatcher()

sanoq = 0
ball_sanoq = 0


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    global sanoq, ball_sanoq
    sanoq = 2
    ball_sanoq = 0

    question = "1.Педагогика-это наука о"
    answers = [
        "А) подготовке учителя к работе в школе ",
        "В)  способах научного познания",
        "С)  психологических особенностях личности",
        "Д)  физиологических закономерностях развития личности",
        "Е)  воспитании человека в современном обществе"
    ]

    await message.answer_poll(question, answers, False, 'quiz', open_period=15,
                              correct_option_id=4)


@dp.message(F.text.startswith('/stop'))
async def command_start_handler(message: Message, bot: Bot) -> None:
    # poll_id = int(message.text.split()[-1])
    # print(message.text.split())
    # await bot.stop_poll(message.chat.id, poll_id)
    global sanoq, ball_sanoq
    print('Poll stop qilindi')
    ikm = InlineKeyboardBuilder()
    ikm.add(InlineKeyboardButton(text='Qayta urinish', callback_data='qayta_urinish'))
    await message.answer(text=f'''🏁 “🎲 “АТТЕСТАЦИЯ_ НОВАЯ БАЗА 001   Подготовила: Нормуродова Эьзоза” testi yakunlandi!

Siz {sanoq - 2} ta savolga javob berdingiz:

✅ Toʻgʻri – {ball_sanoq}
❌ Xato – {(sanoq - 2) - ball_sanoq}
''', reply_markup=ikm.as_markup())
    sanoq = 0


@dp.poll_answer()
async def poll_answer(poll: SendPoll, bot: Bot):
    global sanoq, ball_sanoq
    with open('tests.json') as file:
        read_file = json.load(file)
        test = read_file.get(str(sanoq))
    if poll.option_ids[0] == test[-1]:
        ball_sanoq += 1
    question = test[0]
    answers = test[1:6]
    await bot.send_poll(poll.user.id, question, options=answers, is_anonymous=False, type='quiz', open_period=15,
                        correct_option_id=test[-1])
    sanoq += 1


@dp.callback_query(F.data == 'qayta_urinish')
async def quiz_callback(callback: CallbackQuery):
    global sanoq, ball_sanoq
    sanoq = 2
    ball_sanoq = 0

    question = "1.Педагогика-это наука о"
    answers = [
        "А) подготовке учителя к работе в школе ",
        "В)  способах научного познания",
        "С)  психологических особенностях личности",
        "Д)  физиологических закономерностях развития личности",
        "Е)  воспитании человека в современном обществе"
    ]
    await callback.message.answer_poll(question, options=answers, is_anonymous=False, type='quiz', open_period=15, correct_option_id=4)
    # await message.answer_poll(question, answers, False, 'quiz', open_period=15,
    #                           correct_option_id=4)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
