import os.path

from aiogram.types import CallbackQuery, FSInputFile
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def main_program(callback: CallbackQuery, button: Button,
                       manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.abspath(os.path.curdir) + '/files/program/Архитектура ЕОФ-2025 от 20.02.pdf'),
        caption='Архитектура научной программы ЕОФ 2025')


async def empty(callback: CallbackQuery, button: Button,
                manager: DialogManager):
    return 0
    # await callback.message.answer_document(
    #     document=FSInputFile(os.path.join(main_config.file_location, 'program/arthroscopy.pdf')),
    #     caption='Артроскопия')