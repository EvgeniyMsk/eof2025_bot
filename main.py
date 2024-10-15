from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import (
    setup_dialogs, )

from dialogs.main_dialog import main_dialog
from dialogs import program_dialog as pg_dialog
from dialogs import trauma_point_dialog as trp_dialog
from handlers.test_handler import main_router

storage = MemoryStorage()
bot = Bot(token='5347821122:AAFHGgIptiIV9kEIXeAERZNpi1sUBGj0KKw')

dp = Dispatcher(storage=storage)
dp.include_router(router=main_router)
dp.include_router(main_dialog)
dp.include_router(pg_dialog.program_dialog)
dp.include_router(trp_dialog.main_dialog)


# dp.include_router(program_20_06_dialog)
# dp.include_router(program_21_06_dialog)


setup_dialogs(dp)

if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)
