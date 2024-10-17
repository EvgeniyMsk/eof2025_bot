from aiogram.enums import ParseMode
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Row, Next, Back, SwitchTo
from aiogram_dialog.widgets.text import Const, Jinja, Multi, Progress

from states import RaffleMenu, MainMenu

main_dialog = Dialog(
    Window(
        Jinja(f'Вы уже были зарегистрированы ранее.'),
        Cancel(Const("На главную")),
        state=RaffleMenu.was_registered,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Для участия в розыгрыше автомобиля введите Вашу фамилию\r\n'),
        Cancel(Const("Назад")),
        TextInput(id="lastname", on_success=Next()),
        state=RaffleMenu.main_menu_input_lastname,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Multi(
            Const(f'Введите номер билета'),
        ),
        TextInput(id="firstname", on_success=Next()),
        Back(Const("Назад")),
        state=RaffleMenu.input_number,
    ),
    Window(
        Multi(
            Jinja(f'Поздравляем! Вы участвуете в розыгрыше автомобиля <b>Москвич 3</b>.\r\n'
                  f'Розыгрыш состоится <b>21 июня в 12:00 в главном зале.</b>\r\n'
                  f'Для получения приза <b>обязательно</b> личное присутствие.'),
        ),
        TextInput(id="firstname", on_success=Next()),
        Cancel(Const("На главную")),
        state=RaffleMenu.result,
        parse_mode=ParseMode.HTML,
    )
)
