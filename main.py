import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_dialog import (
    setup_dialogs, )

import bot_config
from dialogs import lesson_dialog as ld_dialog
from dialogs import program_dialog as pg_dialog
from dialogs import quest_dialog as qd_dialog
from dialogs import raffle_dialog as raf_dialog
from dialogs import help_dialog
from dialogs import trauma_point_register_dialog as trp_dialog
from dialogs import trauma_point_work_dialog as tw_dialog
from dialogs.main_dialog import main_dialog
from handlers.start_handler import main_router

bot = Bot(token=bot_config.main_config.bot_token)


async def main():
    logging.basicConfig(level=logging.INFO)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router=main_router)
    dp.include_router(router=main_dialog)
    dp.include_router(router=pg_dialog.program_dialog)
    dp.include_router(router=trp_dialog.main_dialog)
    dp.include_router(router=raf_dialog.main_dialog)
    dp.include_router(router=qd_dialog.main_dialog)
    dp.include_router(router=ld_dialog.main_dialog)
    dp.include_router(router=tw_dialog.main_dialog)
    dp.include_router(router=help_dialog.main_dialog)

    setup_dialogs(dp)
    await dp.start_polling(bot)


async def download_document(message: Message, path: str):
    file_id = message.document.file_id
    file_name = message.document.file_name
    file = await bot.get_file(file_id)
    file_path = file.file_path
    destination = os.path.abspath(os.path.curdir) + path
    await bot.download_file(file_path, destination)
    await message.reply(f"Файл {file_name} успешно сохранен на сервере.")

if __name__ == '__main__':
    asyncio.run(main())
