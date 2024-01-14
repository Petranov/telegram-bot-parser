import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, html
from aiogram.filters.command import Command
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from pars import responce, pars
from kb import *
import config
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token, parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message, bot : Bot):
    await message.answer('Для продолжения - нажмите на кнопку продолжить⬇️', reply_markup=builder.as_markup())

@dp.message(F.text.lower() == "вернуться")
async def with_puree(message: types.Message):
    await message.reply('Для нового парсинга, нажмите /start', reply_markup=types.ReplyKeyboardRemove())

@dp.callback_query(F.data == 'Continue')
async def answer_inline(callback: types.CallbackQuery):
    await callback.message.answer('Отправьте ссылку на сайт для парсинга.')

@dp.message(F.text)
async def save_link(message: types.Message):
    link = message.text
    try:
        pars(link)
        result = FSInputFile("Site.zip")
        await message.answer_document(result, caption='⚡️Все спаршено! Йоу!')

        await message.answer('Что делаем дальше?', reply_markup=builder_repl.as_markup(resize_keyboard=True))
    except Exception as ex:
        await message.answer('⛔️Ошибка! Введите верную ссылку на сайт!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())