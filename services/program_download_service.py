import os.path

from aiogram.types import CallbackQuery, FSInputFile
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot_config import main_config


async def download_all_program(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_19_06_napr_1(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_19_06_napr_2(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_19_06_napr_3(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_20_06_napr_1(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_20_06_napr_2(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_20_06_napr_3(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_21_06_napr_1(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_21_06_napr_2(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')


async def download_21_06_napr_3(callback: CallbackQuery, button: Button,
                                manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile(os.path.join(main_config.file_location, 'all_program.pdf')),
                                           caption='Программа ЕОФ2025')