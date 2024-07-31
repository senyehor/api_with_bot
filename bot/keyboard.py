from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
)

MORE_CATS = 'More cats!'

buttons = [
    [KeyboardButton(text=MORE_CATS)],
]

GET_MORE_CATS_MARKUP = ReplyKeyboardMarkup(keyboard=buttons)
