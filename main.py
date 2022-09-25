from aiogram.utils import executor
from handlers import register_handlers
from cfg import dp


async def start_bot(_):
    register_handlers(dp)
    print('BOT ONLINE')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
