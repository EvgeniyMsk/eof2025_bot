from typing import Any

from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, FSInputFile
from aiogram_dialog import Window, Dialog, DialogManager, Data
from aiogram_dialog.widgets.kbd import Row, Button, Start, Cancel
from aiogram_dialog.widgets.text import Const
from services import download_service as download_service


class ProgramMenu(StatesGroup):
    main_menu = State()
    program_19_06_menu = State()
    program_20_06_menu = State()
    program_21_06_menu = State()


async def close_program_dialog(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await manager.done(result={"name": "Tishka17"})


program_dialog = Dialog(
    Window(
        Const("Раздел: Программа форума"),
        Row(Button(Const("Вся программа"), id="all_program", on_click=download_service.download_all_program), ),
        Row(Start(Const("19.06"), id="program_19_06", state=ProgramMenu.program_19_06_menu),
            Start(Const("20.06"), id="program_20_06", state=ProgramMenu.program_20_06_menu),
            Start(Const("21.06"), id="program_21_06", state=ProgramMenu.program_21_06_menu)),
        Cancel(Const("Назад")),
        state=ProgramMenu.main_menu,
    ),
    Window(
        Const("Раздел: Программа форума на 19.06"),
        Row(Button(Const("Направление 1"), id="napr_1_19_06", on_click=download_service.download_19_06_napr_1), ),
        Row(Button(Const("Направление 2"), id="napr_2_19_06", on_click=download_service.download_19_06_napr_2), ),
        Row(Button(Const("Направление 3"), id="napr_3_19_06", on_click=download_service.download_19_06_napr_3), ),
        Cancel(Const("Назад")),
        state=ProgramMenu.program_19_06_menu,
    ),
    Window(
        Const("Раздел: Программа форума на 20.06"),
        Row(Button(Const("Направление 1"), id="napr_1_20_06", on_click=download_service.download_20_06_napr_1), ),
        Row(Button(Const("Направление 2"), id="napr_2_20_06", on_click=download_service.download_20_06_napr_2), ),
        Row(Button(Const("Направление 3"), id="napr_3_20_06", on_click=download_service.download_20_06_napr_3), ),
        Cancel(Const("Назад")),
        state=ProgramMenu.program_20_06_menu,
    ),
    Window(
        Const("Раздел: Программа форума на 21.06"),
        Row(Button(Const("Направление 1"), id="napr_1_21_06", on_click=download_service.download_21_06_napr_1), ),
        Row(Button(Const("Направление 2"), id="napr_2_21_06", on_click=download_service.download_21_06_napr_2), ),
        Row(Button(Const("Направление 3"), id="napr_3_21_06", on_click=download_service.download_21_06_napr_3), ),
        Cancel(Const("Назад")),
        state=ProgramMenu.program_21_06_menu,
    )
)
