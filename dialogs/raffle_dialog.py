import os
from typing import Dict, Any

from aiogram.enums import ParseMode, ContentType
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager, Data, StartMode
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Next, Back, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Jinja, Multi

from services import raffle_service
from states import RaffleMenu, MainMenu


def is_contains(data: Dict, widget: Whenable, manager: DialogManager):
    return raffle_service.is_exists(manager.find("ticket_number").get_value())


def is_not_contains(data: Dict, widget: Whenable, manager: DialogManager):
    return not raffle_service.is_exists(manager.find("ticket_number").get_value())


async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        "lastname": dialog_manager.find("lastname").get_value(),
        "ticket_number": dialog_manager.find("ticket_number").get_value(),
    }


async def raffle_process_result(start_data: Data, result: Any,
                                dialog_manager: DialogManager):
    print(dialog_manager.find("ticket_number").get_value())
    print(dialog_manager.find("lastname").get_value())


async def close_subdialog(callback: CallbackQuery, button: Button,
                          dialog_manager: DialogManager):
    try:
        raffle_service.register_raffle_user(callback, dialog_manager)
        await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)
    except Exception as e:
        await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


main_dialog = Dialog(
    Window(
        Jinja(f'Для участия в розыгрыше автомобиля введите Вашу фамилию\r\n'),
        Cancel(Const("Назад")),
        TextInput(id="lastname", on_success=Next()),
        state=RaffleMenu.main_menu_input_lastname,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        StaticMedia(
            path=os.path.abspath(os.curdir) + '/files/raffle/eof_raffle_pic.jpg',
            type=ContentType.PHOTO,
        ),
        Multi(
            Jinja(
                f'Введите номер билета.\n\n'
                '<b>Номер билета Вы можете посмотреть в личном кабинете\n '
                'на сайте https://2025.eoforum.ru  в разделе «Мои билеты»</b>'
            ),
            #Const(f'Введите номер билета'),
        ),
        TextInput(id="ticket_number", on_success=Next()),
        Back(Const("Назад")),
        state=RaffleMenu.input_number,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Multi(
            Jinja(f'Введенный билет уже был зарегистрирован ранее.'),
            when=is_contains
        ),
        Multi(
            Jinja(f'Поздравляем! Вы участвуете в розыгрыше автомобиля <b>Москвич</b>🚘.\r\n'
                  f'Розыгрыш состоится <b>21 июня в 12:45 в зоне Города Мастеров</b> на\r\n'
                  f'-1 этаже ЦВЗ «Манеж».\r\n'
                  f'🚨<b>Для получения приза обязательно личное'
                  f'присутствие на розыгрыше!</b>\n\n'),
            when=is_not_contains
        ),
        Button(Const("На главную"), id='end_dialog', on_click=close_subdialog),
        getter=getter,
        state=RaffleMenu.result,
        parse_mode=ParseMode.HTML,
    ),
    on_process_result=raffle_process_result,
)
