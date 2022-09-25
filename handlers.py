from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from cfg import bot, dp
from aiogram import Dispatcher


async def echo(msg: Message):
    await bot.send_message(msg.from_user.id, msg.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)