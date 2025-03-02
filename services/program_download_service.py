import os.path

from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, Message
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


async def arthroscopy(callback: CallbackQuery, button: Button,
                      manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/arthroscopy.pdf')),
        caption='Артроскопия')


async def foot_ankle_surgery(callback: CallbackQuery, button: Button,
                             manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/foot_ankle_surgery.pdf')),
        caption='Хирургия стопы и голеностопного сустава')


async def military_field_surgery(callback: CallbackQuery, button: Button,
                                 manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/military_field_surgery.pdf')),
        caption='Военно-полевая хирургия')


async def hand_wrist_surgery(callback: CallbackQuery, button: Button,
                             manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/hand_wrist_surgery.pdf')),
        caption='Хирургия кисти и кистевого сустава')


async def orthopedic_rehabilitation(callback: CallbackQuery, button: Button,
                                    manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/orthopedic_rehabilitation.pdf')),
        caption='Ортопедическая реабилитация')


async def sports_medicine(callback: CallbackQuery, button: Button,
                          manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/sports_medicine.pdf')),
        caption='Спортивная медицина')


async def joint_replacement(callback: CallbackQuery, button: Button,
                            manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/joint_replacement.pdf')),
        caption='Эндопротезирование суставов')


async def traumatology(callback: CallbackQuery, button: Button,
                       manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/traumatology.pdf')),
        caption='Травматология')


async def childhood_trauma(callback: CallbackQuery, button: Button,
                           manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/childhood_trauma.pdf')),
        caption='Детская травма')


async def polytrauma(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/polytrauma.pdf')),
        caption='Политравма')


async def reconstructive_surgery_of_the_extremities(callback: CallbackQuery, button: Button,
                                                    manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(
            os.path.join(main_config.file_location, 'program/reconstructive_surgery_of_the_extremities.pdf')),
        caption='Реконструктивная хирургия конечностей')


async def spine_surgery(callback: CallbackQuery, button: Button,
                        manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/spine_surgery.pdf')),
        caption='Хирургия позвоночника')


async def orthobiology(callback: CallbackQuery, button: Button,
                       manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/orthobiology.pdf')),
        caption='Ортобиология')


async def oncoorthopedics(callback: CallbackQuery, button: Button,
                          manager: DialogManager):
    await callback.message.answer_document(
        document=FSInputFile(os.path.join(main_config.file_location, 'program/oncoorthopedics.pdf')),
        caption='Онкоортопедия')
