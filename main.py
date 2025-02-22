import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import (
    setup_dialogs, )

import bot_config
from dialogs import lesson_dialog as ld_dialog
from dialogs import program_dialog as pg_dialog
from dialogs import quest_dialog as qd_dialog
from dialogs import raffle_dialog as raf_dialog
from dialogs import trauma_point_register_dialog as trp_dialog
from dialogs import trauma_point_work_dialog as tw_dialog
from dialogs.main_dialog import main_dialog
from handlers.start_handler import main_router


async def main():
    logging.basicConfig(level=logging.INFO)
    storage = MemoryStorage()
    print(bot_config.BOT_TOKEN)
    bot = Bot(token=bot_config.main_config.bot_token)
    dp = Dispatcher(storage=storage)
    dp.include_router(router=main_router)
    dp.include_router(router=main_dialog)
    dp.include_router(router=pg_dialog.program_dialog)
    dp.include_router(router=trp_dialog.main_dialog)
    dp.include_router(router=raf_dialog.main_dialog)
    dp.include_router(router=qd_dialog.main_dialog)
    dp.include_router(router=ld_dialog.main_dialog)
    dp.include_router(router=tw_dialog.main_dialog)

    setup_dialogs(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
