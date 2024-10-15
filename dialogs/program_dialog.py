from typing import Any

from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, FSInputFile
from aiogram_dialog import Window, Dialog, DialogManager, Data
from aiogram_dialog.widgets.kbd import Row, Button, Start, Cancel
from aiogram_dialog.widgets.text import Const


class ProgramMenu(StatesGroup):
    main_menu = State()


async def close_program_dialog(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await manager.done(result={"name": "Tishka17"})


async def download_program(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await callback.message.answer_document(document=FSInputFile("C:\\Users\\logvinov\\PycharmProjects\\tg_test\\requirements.txt"),
                                            caption='Программа ЕОФ2025')

program_dialog = Dialog(
    Window(

        Const("Раздел: Программа форума"),
        Row(Button(Const("Вся программа"), id="all_program", on_click=download_program),),
        Row(Button(Const("19.06"), id="program_19_06", on_click=close_program_dialog),
            Button(Const("20.06"), id="program_20_06", on_click=close_program_dialog),
            Button(Const("21.06"), id="program_21_06", on_click=close_program_dialog)
            ),
        Cancel(Const("Назад")),
        state=ProgramMenu.main_menu,
    ),
)
