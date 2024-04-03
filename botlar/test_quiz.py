# import asyncio
# import logging
# import sys
# from time import sleep
#
# from aiogram import Dispatcher, Bot, types, F
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import InlineKeyboardButton, CallbackQuery, PollAnswer
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.methods import SendPoll
# from aiogram.types import Message, Poll, PollAnswer
#
# TOKEN = '6686631791:AAFZ98zLIGfQWoaKxGqzI2uteVRxhdXPu8k'
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def start(message: types.Message, bot: Bot):
#     question = '1. Savol ?'
#     answers = [
#         'A togri',
#         'B notogri',
#         'C A B togri',
#         'D togri'
#     ]
#     result = await message.answer_poll(question, answers, False, 'quiz', open_period=5,
#                                        correct_option_id=2)
#
#
# @dp.poll_answer()
# async def f_answer(poll: PollAnswer, bot: Bot):
#     print(poll.options_ids[0])
#     print(65184531305618416469454684618654062248)
#     question = '2. Savol ?'
#     answers = [
#         'salom',
#         'hayr',
#         'korshguncha',
#         'you mubi'
#     ]
#     result = await poll.answer_poll(question, answers, False, 'quiz', open_period=6, correct_option_id=1)
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
import json

#
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, PollAnswer

TOKEN = '6686631791:AAFZ98zLIGfQWoaKxGqzI2uteVRxhdXPu8k'  # testing_io_bot
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    question = '1. Savol ?'
    answers = [
        'A togri',
        'B notogri',
        'C A B togri',
        'D togri'
    ]
    result = await message.answer_poll(question, answers, False, 'quiz', open_period=5,
                                       correct_option_id=2)


@dp.poll_answer()
async def poll_answer(poll: PollAnswer, bot: Bot):

    print(poll.option_ids[0])
    question = '1. Savol ?'
    answers = [
        'A togri',
        'B notogri',
        'C A B togri',
        'D togri'
    ]
    await bot.send_poll(chat_id=poll.from_user.id, question=question, options=answers)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


# with (open('tests.txt', 'r') as f):
#     t = f.readlines()
#     n = 0
#     l1 = ''
#     l2 = ''
#     l3 = ''
#     l4 = ''
#     l5 = ''
#     d = {}
#     print(t[0])
#     for i in range(0, len(t), 5):
#         n += 1
#         l1 = t[i]
#         l2 = t[i + 1]
#         l3 = t[i + 2]
#         l4 = t[i + 3]
#         l5 = t[i + 4]
#         d[f'{n}. {l1}'] = f'{l2} \n {l3} \n {l4} | '
#     print(d)
#     with open('jjjj.json', 'w') as file:
#         json.dump(d, file, indent=4)
#
#
