import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboard import GET_MORE_CATS_MARKUP, MORE_CATS
from logic import format_cats, query_cats

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Cats?', reply_markup=GET_MORE_CATS_MARKUP)


@dp.message(F.text == MORE_CATS)
async def more_cats(message: Message):
    cats = await query_cats()
    cats_html = format_cats(cats)
    await message.answer(
        cats_html,
        parse_mode=ParseMode.HTML
    )


@dp.message
async def fallback(message: Message):
    await message.answer('I do not know how to react to this :(·')


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
