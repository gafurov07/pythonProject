import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, InputMediaPhoto
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

TOKEN = '6768662481:AAHSZ51j7LkZvYGgbd2SJeiLUab5-mExMfQ'
dp = Dispatcher()


# await bot.send_photo(message01.from_user.id, 'https://media.express24.uz/r/600/600/upload/iblock/482/4829117e14db69b3e29be266eee3a1f4.jpg', caption='Pastdagi information')  botga rasm tashalsh uchun
# await bot.send_message(1130086828, message01.text)
# await message01.answer('hello')

# @dp.message(F.content_type._in({types.ContentType.LOCATION})) kelayotgan kantakt yoki lakatsiyani va boshqalarni anqilash uchun
# async def on_text_message(message: types.Message):
#

@dp.message(CommandStart())
async def on_message(message: Message):
    pp = ReplyKeyboardBuilder()
    pp.row(KeyboardButton(text='Меню'))
    pp.row(KeyboardButton(text='Мои заказы'))
    pp.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
    await message.answer('Выберите одно из следующих', reply_markup=pp.as_markup())


@dp.message(F.text == 'Меню')
async def on_text_message(message: types.Message):
    rm = ReplyKeyboardBuilder()
    rm.row(KeyboardButton(text='Мои адреса'))
    rm.row(KeyboardButton(text='отправить геолокацию', request_location=True))
    rm.row(KeyboardButton(text='Назад'))
    await message.answer('Отправьте геолокацию или выберите адрес доставки', reply_markup=rm.as_markup())

    @dp.message(F.text == 'Назад')
    async def on_message_p90(message999: types.Message):
        pp = ReplyKeyboardBuilder()
        pp.row(KeyboardButton(text='Меню'))
        pp.row(KeyboardButton(text='Мои заказы'))
        pp.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
        await on_message_p90.answer('Выберите одно из следующих', reply_markup=pp.as_markup())


@dp.message(F.content_type.in_({types.ContentType.LOCATION}))
async def on_location(message777: types.Message):
    mmm = ReplyKeyboardBuilder()
    mmm.row(KeyboardButton(text='Да'), KeyboardButton(text='Нет'))
    mmm.row(KeyboardButton(text='Назад'))
    await message777.answer('Адрес, по которому вы хотите заказать: Узбекистан?', reply_markup=mmm.as_markup())

    @dp.message(F.text == 'Да')
    async def da_message(message1: types.Message):
        kkk = ReplyKeyboardBuilder()
        kkk.row(KeyboardButton(text='lavash'), KeyboardButton(text='trindwich'))
        kkk.row(KeyboardButton(text='shaurma'), KeyboardButton(text='burger'))
        kkk.row(KeyboardButton(text='sub'), KeyboardButton(text='kartoshka'))
        kkk.row(KeyboardButton(text='hot-dog'), KeyboardButton(text='sneklar'))
        kkk.row(KeyboardButton(text='salat, garnir, non'), KeyboardButton(text='souslar'))
        kkk.row(KeyboardButton(text='setlar'), KeyboardButton(text='desertlar'))
        kkk.row(KeyboardButton(text='issiq ichimliklar'), KeyboardButton(text='sovuq ichimliklar'))
        kkk.row(KeyboardButton(text='combo'))
        kkk.row(KeyboardButton(text='Мои заказы'), KeyboardButton(text='Назад'))
        await message1.answer('Выберите категорию.', reply_markup=kkk.as_markup())

        @dp.message(F.text == 'Назад')
        async def _(message: Message):
            rm = ReplyKeyboardBuilder()
            rm.row(KeyboardButton(text='Мои адреса'))
            rm.row(KeyboardButton(text='отправить геолокацию', request_location=True))
            rm.row(KeyboardButton(text='Назад'))
            await message.answer('Отправьте геолокацию или выберите адрес доставки', reply_markup=rm.as_markup())

            @dp.message(F.text == 'Назад')
            async def nazad(message888: Message):
                pp = ReplyKeyboardBuilder()
                pp.row(KeyboardButton(text='Меню'))
                pp.row(KeyboardButton(text='Мои заказы'))
                pp.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
                await message888.answer('Выберите одно из следующих', reply_markup=pp.as_markup())


@dp.message(F.text == 'Нет')
async def net_message(message111: types.Message):
    rm = ReplyKeyboardBuilder()
    rm.row(KeyboardButton(text='Мои адреса'))
    rm.row(KeyboardButton(text='отправить геолокацию', request_location=True))
    rm.row(KeyboardButton(text='Назад'))
    await message111.answer('Отправьте геолокацию или выберите адрес доставки', reply_markup=rm.as_markup())

    @dp.message(F.text == 'Назад')
    async def on_reply_message(message2: types.Message):
        rmm = ReplyKeyboardBuilder()
        rmm.row(KeyboardButton(text='Меню'))
        rmm.row(KeyboardButton(text='Мои заказы'))
        rmm.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
        await message2.answer('Выберите одно из следующих', reply_markup=rmm.as_markup())


@dp.message(F.text == 'lavash')
async def lavash(message01: types.Message, bot: Bot):
    mmm = ReplyKeyboardBuilder()
    mmm.row(KeyboardButton(text="To'vuq go'shtidan lavash"),
            KeyboardButton(text="Mol go'shtidan pishloqli lavash"))
    mmm.row(KeyboardButton(text="Mol go'shtidan qalampir lavash"),
            KeyboardButton(text="To'vuq go'shtidan qalampir lavash"))
    mmm.row(KeyboardButton(text="To'vuq go'shtidan pishloqli lavash"), KeyboardButton(text="Fitter"))
    mmm.row(KeyboardButton(text="Mol go'shtidan lavash"))
    mmm.row(KeyboardButton(text="Назад"))
    await bot.send_photo(message01.from_user.id,
                         'https://media.express24.uz/r/600/600/upload/iblock/482/4829117e14db69b3e29be266eee3a1f4.jpg')
    await message01.answer('lavash', reply_markup=mmm.as_markup())

    @dp.message(F.text == "To'vuq go'shtidan lavash")
    async def tovuq(message: types.Message):
        rka = InlineKeyboardBuilder()
        rka.row(InlineKeyboardButton(text="Mini 21 000 so'm"), InlineKeyboardButton(text="Big 26 000 so'm"))
        await bot.send_photo(message.from_user.id,
                             'https://media.express24.uz/r/600/600y/upload/iblock/482/4829117e14db69b3e29be266eee3a1f4.jpg')
        await message.answer('Quyidagilardan birini tanlang', reply_markup=rka.as_markup())


@dp.message(F.text == "Назад")
async def _(message11: types.Message):
    kkk = ReplyKeyboardBuilder()
    kkk.row(KeyboardButton(text='lavash'), KeyboardButton(text='trindwich'))
    kkk.row(KeyboardButton(text='shaurma'), KeyboardButton(text='burger'))
    kkk.row(KeyboardButton(text='sub'), KeyboardButton(text='kartoshka'))
    kkk.row(KeyboardButton(text='hot-dog'), KeyboardButton(text='sneklar'))
    kkk.row(KeyboardButton(text='salat, garnir, non'), KeyboardButton(text='souslar'))
    kkk.row(KeyboardButton(text='setlar'), KeyboardButton(text='desertlar'))
    kkk.row(KeyboardButton(text='issiq ichimliklar'), KeyboardButton(text='sovuq ichimliklar'))
    kkk.row(KeyboardButton(text='combo'))
    kkk.row(KeyboardButton(text='Мои заказы'), KeyboardButton(text='Назад'))
    await message11.answer('Выберите категорию.', reply_markup=kkk.as_markup())


@dp.message(F.text == 'trindwich')
async def trindwich(message01: Message, bot: Bot):
    await bot.send_photo(message01.from_user.id, 'https://media.express24.uz/r/600/600/Qpu4SRYAPRxIFMdVh0Q7o.jpg')
    rkm = ReplyKeyboardBuilder()
    rkm.row(KeyboardButton(text="Trindwich to'vuq go'shtidan"), KeyboardButton(text="Trindwich mol go'shtidan"))
    rkm.row(KeyboardButton(text="Назад"))
    await message01.answer('trindwich', reply_markup=rkm.as_markup())

    @dp.message(F.text == "Назад")
    async def _(message: types.Message):
        kkk = ReplyKeyboardBuilder()
        kkk.row(KeyboardButton(text='lavash'), KeyboardButton(text='trindwich'))
        kkk.row(KeyboardButton(text='shaurma'), KeyboardButton(text='burger'))
        kkk.row(KeyboardButton(text='sub'), KeyboardButton(text='kartoshka'))
        kkk.row(KeyboardButton(text='hot-dog'), KeyboardButton(text='sneklar'))
        kkk.row(KeyboardButton(text='salat, garnir, non'), KeyboardButton(text='souslar'))
        kkk.row(KeyboardButton(text='setlar'), KeyboardButton(text='desertlar'))
        kkk.row(KeyboardButton(text='issiq ichimliklar'), KeyboardButton(text='sovuq ichimliklar'))
        kkk.row(KeyboardButton(text='combo'))
        kkk.row(KeyboardButton(text='Мои заказы'), KeyboardButton(text='Назад'))
        await message.answer('Выберите категорию.', reply_markup=kkk.as_markup())


@dp.message(F.text == 'shaurma')
async def shaurma(message01: Message, bot: Bot):
    await bot.send_photo(message01.from_user.id, 'https://media.express24.uz/r/600/600/17a62d7f507.jpg')
    www = ReplyKeyboardBuilder()
    www.row(KeyboardButton(text="Mol go'shtidan qalampir shaurma"), KeyboardButton(text="To'vuq go'shtidan shaurma"))
    www.row(KeyboardButton(text="To'vuq go'shtidan qalampir shaurma"), KeyboardButton(text="Mol go'shtidan shaurma"))
    www.row(KeyboardButton(text="Назад"))
    await message01.answer('shaurma', reply_markup=www.as_markup())

    @dp.message(F.text == "Назад")
    async def _(message: types.Message):
        kkk = ReplyKeyboardBuilder()
        kkk.row(KeyboardButton(text='lavash'), KeyboardButton(text='trindwich'))
        kkk.row(KeyboardButton(text='shaurma'), KeyboardButton(text='burger'))
        kkk.row(KeyboardButton(text='sub'), KeyboardButton(text='kartoshka'))
        kkk.row(KeyboardButton(text='hot-dog'), KeyboardButton(text='sneklar'))
        kkk.row(KeyboardButton(text='salat, garnir, non'), KeyboardButton(text='souslar'))
        kkk.row(KeyboardButton(text='setlar'), KeyboardButton(text='desertlar'))
        kkk.row(KeyboardButton(text='issiq ichimliklar'), KeyboardButton(text='sovuq ichimliklar'))
        kkk.row(KeyboardButton(text='combo'))
        kkk.row(KeyboardButton(text='Мои заказы'), KeyboardButton(text='Назад'))
        await message.answer('Выберите категорию.', reply_markup=kkk.as_markup())


@dp.message(F.text == 'Мои адреса')
async def on_reply_message2(message3: types.Message):
    await message3.answer('Пусто')


@dp.message(F.text == 'Мои заказы')
async def on_message222(message: types.Message):
    await message.answer('Вы совсем ничего не заказали.')


@dp.message(F.text == 'Оставить отзыв')
async def on_message_asd(message: types.Message):
    rm = ReplyKeyboardBuilder()
    rm.row(KeyboardButton(text='Мой номер', request_contact=True))
    rm.row(KeyboardButton(text='Назад'))
    await message.answer('Поделитесь контактом для дальнейшего связи с Вами', reply_markup=rm.as_markup())

    @dp.message(F.text == 'Назад')
    async def on_reply_message3(message74: types.Message):
        pp = ReplyKeyboardBuilder()
        pp.row(KeyboardButton(text='Меню'))
        pp.row(KeyboardButton(text='Мои заказы'))
        pp.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
        await message74.answer('Выберите одно из следующих', reply_markup=pp.as_markup())


@dp.message(F.content_type.in_({types.ContentType.CONTACT}))
async def on_reply_message333(message159: types.Message):
    rrr = ReplyKeyboardBuilder()
    rrr.row(KeyboardButton(text='Назад', callback_data="you"))
    await message159.answer('Отправьте ваши отзывы', reply_markup=rrr.as_markup())

    @dp.message(F.text == 'Назад')
    async def on_reply_message0963(message74: types.Message):
        pp = ReplyKeyboardBuilder()
        pp.row(KeyboardButton(text='Меню'))
        pp.row(KeyboardButton(text='Мои заказы'))
        pp.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
        await message74.answer('Выберите одно из следующих', reply_markup=pp.as_markup())


@dp.message(F.text == 'Настройки')
async def on_m(message: types.Message):
    rm = ReplyKeyboardBuilder()
    rm.row(KeyboardButton(text='Изменить язык'))
    rm.row(KeyboardButton(text='Назад'))
    await message.answer('Выберите действие:', reply_markup=rm.as_markup())


@dp.message(F.text == 'Изменить язык')
async def on_r(message2: types.Message):
    rm2 = ReplyKeyboardBuilder()
    rm2.row(KeyboardButton(text='Русский'), KeyboardButton(text="O'zbekcha"))
    await message2.answer('Выберите язык:', reply_markup=rm2.as_markup())


@dp.message((F.text == 'Русский') | (F.text == "O'zbekcha"))
async def on_q(message: types.Message):
    rm = ReplyKeyboardBuilder()
    rm.row(KeyboardButton(text='Изменить язык'))
    rm.row(KeyboardButton(text='Назад'))
    await message.answer('Готово', reply_markup=rm.as_markup())

    @dp.message(F.text == 'Назад')
    async def on_u(message2: types.Message):
        rm2 = ReplyKeyboardBuilder()
        rm2.row(KeyboardButton(text='Меню'))
        rm2.row(KeyboardButton(text='Мои заказы'))
        rm2.row(KeyboardButton(text='Оставить отзыв'), KeyboardButton(text='Настройки'))
        await message2.answer('Выберите одно из следующих', reply_markup=rm2.as_markup())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
