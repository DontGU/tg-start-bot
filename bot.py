import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_URL = os.getenv("CHANNEL_URL")

async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🚀 Перейти в канал",
                url=CHANNEL_URL
            )]
        ]
    )

    await message.answer(
        "Привет 👋\n\n"
        "Играешь в казино?\n"
        "У меня есть что предложить! Я готов вернуть твой первый депозит\n"
        "от 10$ до 50$ в случае неудачи.\n\n"
        "👇 Все условия — в канале",
        reply_markup=keyboard
    )

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.message.register(start_handler, CommandStart())
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
