import os.path

import xlsxwriter
from aiogram.types import CallbackQuery, FSInputFile
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from services import raffle_service


async def main_program(callback: CallbackQuery, button: Button,
                       manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.abspath(os.path.curdir) + '/files/program/Архитектура ЕОФ-2025 от 20.02.pdf'),
        caption='Архитектура научной программы ЕОФ 2025')


async def user_data(callback: CallbackQuery, button: Button,
                    manager: DialogManager):
    people = raffle_service.get_all_users()
    workbook = xlsxwriter.Workbook(os.path.abspath(os.path.curdir) + '/files/raffle/eof_users.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'id')
    worksheet.write(0, 1, 'telegram_id')
    worksheet.write(0, 2, 'lastname')
    worksheet.write(0, 3, 'ticket_number')
    for index, user in enumerate(people):
        worksheet.write(index + 1, 0, user.id)
        worksheet.write(index + 1, 1, user.telegram_id)
        worksheet.write(index + 1, 2, user.lastname)
        worksheet.write(index + 1, 3, user.ticket_number)
    workbook.close()
    await callback.message.answer_document(
        document=FSInputFile(os.path.abspath(os.path.curdir) + '/files/raffle/eof_users.xlsx'),
        caption='Данные пользователей')


async def empty(callback: CallbackQuery, button: Button,
                manager: DialogManager):
    return 0
    # await callback.message.answer_document(
    #     document=FSInputFile(os.path.join(main_config.file_location, 'program/arthroscopy.pdf')),
    #     caption='Артроскопия')
