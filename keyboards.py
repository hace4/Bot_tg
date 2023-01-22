from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram import types
main_button = ['/roll', '/score', '/board', '/help']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(*main_button)