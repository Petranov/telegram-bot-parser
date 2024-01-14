from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

builder = InlineKeyboardBuilder()
builder_repl = ReplyKeyboardBuilder()
builder.row(types.InlineKeyboardButton(
        text='Продолжить',
        callback_data='Continue'
    ))

builder_repl.row(types.KeyboardButton(text='Вернуться'))