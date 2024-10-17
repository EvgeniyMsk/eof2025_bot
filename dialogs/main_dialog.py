from typing import Any

from aiogram.fsm.state import State
from aiogram_dialog import Window, Dialog, DialogManager, Data
from aiogram_dialog.widgets.kbd import Row, Start
from aiogram_dialog.widgets.text import Const, Progress

from dialogs.program_dialog import ProgramMenu
from dialogs.trauma_point_register_dialog import TraumaPointRegister
from states import MainMenu, RaffleMenu, QuestMenu, LessonMenu


async def main_process_result(start_data: Data, result: Any,
                              dialog_manager: DialogManager):
    print("We have result:", result)


was_raffle_registered = True


def raffle_was_registered() -> State:
    if was_raffle_registered:
        return RaffleMenu.was_registered
    else:
        return RaffleMenu.main_menu_input_lastname


main_dialog = Dialog(
    Window(
        Const("Я бот ЕОФ2025🤖. Выберите пункт меню."),
        Row(
            Start(Const("📋Программа форума"), id="program", state=ProgramMenu.main_menu),
        ),
        Row(
            Start(Const("💬Trauma-POINT бот для профессиональных знакомств"), id="trauma_point",
                  state=TraumaPointRegister.main_menu_input_lastname),
        ),
        Start(Const("🎲Участие в розыгрыше"), id="raffle", state=raffle_was_registered()),
        Start(Const("🤳Квест по выставке"), id="quest", state=QuestMenu.main_menu),
        Start(Const("✍️Стендовые доклады"), id="stand_presentation", state=LessonMenu.main_menu),
        state=MainMenu.main_menu,
    ),
    on_process_result=main_process_result,
)
