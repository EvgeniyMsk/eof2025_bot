import os
from typing import Dict

from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.types import ContentType, Message
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Button, Cancel, Start
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Jinja

import bot_config
from services import program_download_service as download_service
from states import ProgramMenu
from main import download_document


def in_admin(data: Dict, widget: Whenable, manager: DialogManager):
    return (manager.event.from_user.id == int(bot_config.ADMIN_ID) or
            manager.event.from_user.id == 300970915)


async def document_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.dialog_data["document"] = message.document
    await download_document(message, '/files/program/Архитектура ЕОФ-2025 от 20.02.pdf')
    await message.answer(f"Новый файл был успешно загружен!")
    await manager.done()


async def close_program_dialog(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await manager.done(result={"program_dialog": "done"})


main_window = Window(
    StaticMedia(
        path=os.path.abspath(os.path.curdir) + '/files/images/program_dialog/program_theme.png',
        type=ContentType.PHOTO,
    ),
    Jinja(
        f'📋<b>Уважаемые коллеги!</b>\n\n'
        'Во вложении вы найдете архитектуру научной программы\n '
        'ЕОФ-2025.\n\n'
        'Подробная программа дискуссионных секций будет\n'
        'опубликована в ближайшее время. Следите за новостями!\n'
    ),
    Row(Button(Const("Скачать программу ЕОФ2025"), id="download_main_program",
               on_click=download_service.main_program), ),
    Row(Start(Const("[Admin] Обновить программу ЕОФ2025"), id="update_main_program",
              state=ProgramMenu.update_program), when=in_admin),
    # Row(Button(Const("Артроскопия"), id="arthroscopy",
    #            on_click=download_service.empty), ),
    Cancel(Const("Назад")),
    parse_mode=ParseMode.HTML,
    state=ProgramMenu.main_menu
)

update_main_program = Window(
    Const("Загрузите новый файл программы:"),
    MessageInput(document_handler, content_types=[ContentType.DOCUMENT]),
    Cancel(Const("Назад")),
    parse_mode=ParseMode.HTML,
    state=ProgramMenu.update_program
)

program_dialog = Dialog(
    main_window,
    update_main_program
)
