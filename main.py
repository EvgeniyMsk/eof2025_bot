import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import (
    setup_dialogs, )

from dialogs.main_dialog import main_dialog
from dialogs import program_dialog as pg_dialog
from dialogs import trauma_point_register_dialog as trp_dialog
from dialogs import raffle_dialog as raf_dialog
from dialogs import quest_dialog as qd_dialog
from dialogs import lesson_dialog as ld_dialog
from dialogs import trauma_point_work_dialog as tw_dialog

from handlers.test_handler import main_router


async def main():
    logging.basicConfig(level=logging.INFO)
    storage = MemoryStorage()
    bot = Bot(token='7622488885:AAFVi9_rE8JjwzsD8EDtxr61Gn9vCQHf7Ys')
    dp = Dispatcher(storage=storage)
    dp.include_router(router=main_router)
    dp.include_router(main_dialog)
    dp.include_router(pg_dialog.program_dialog)
    dp.include_router(trp_dialog.main_dialog)
    dp.include_router(raf_dialog.main_dialog)
    dp.include_router(qd_dialog.main_dialog)
    dp.include_router(ld_dialog.main_dialog)
    dp.include_router(tw_dialog.main_dialog)

    setup_dialogs(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
