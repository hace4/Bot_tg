from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_kb_pod = InlineKeyboardMarkup(row_width=2)
urlButtonPod  = InlineKeyboardButton('ll', url='https://t.me/vapedrgash/24')
inline_kb_pod.add(urlButtonPod)
inline_kb_full = InlineKeyboardMarkup(row_width=2)
urlButton  = InlineKeyboardButton('заливочка', url='https://t.me/vapedrgash/24')
urlButton2 = InlineKeyboardButton('Подики', url='https://t.me/vapedrgash/24')
inline_kb_full.add(urlButton)