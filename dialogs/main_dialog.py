from typing import Any

from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager, Data
from aiogram_dialog.widgets.kbd import Row, Button, Start, Cancel
from aiogram_dialog.widgets.text import Const

from dialogs.program_dialog import ProgramMenu


class MainMenu(StatesGroup):
    main_menu = State()


async def main_process_result(start_data: Data, result: Any,
                              dialog_manager: DialogManager):
    print("We have result:", result)


main_dialog = Dialog(
    Window(
        Const("Я бот ЕОФ2025. Выберите пункт меню."),

        Row(
            Start(Const("Программа форума"), id="program", state=ProgramMenu.main_menu),
        ),
        Row(
            Start(Const("Trauma-POINT бот для профессиональных знакомств"), id="trauma_point",
                  state=ProgramMenu.main_menu),
        ),
        Start(Const("Участие в розыгрыше"), id="raffle", state=ProgramMenu.main_menu),
        Start(Const("Квест по выставке"), id="quest", state=ProgramMenu.main_menu),
        Start(Const("Стендовые доклады"), id="stand_presentation", state=ProgramMenu.main_menu),
        state=MainMenu.main_menu,
    ),
    on_process_result=main_process_result,
)

