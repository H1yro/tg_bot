import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
import config



API_TOKEN = config.H1yro_Bot

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Start")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Вы обратились к справке бота")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
