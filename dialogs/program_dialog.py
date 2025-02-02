import os

from aiogram.enums import ContentType, ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Row, Button, Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Text, Jinja

from services import program_download_service as download_service
from states import ProgramMenu


async def close_program_dialog(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await manager.done(result={"program_dialog": "done"})

main_window = Window(
    StaticMedia(
        path=os.path.abspath(os.path.curdir) + '/files/images/program_dialog/program_theme.png',
        type=ContentType.PHOTO,
    ),
    Jinja(
        f'📋<b>Раздел: Программа форума.</b>\n\n'
        '· Артроскопия\n'
        '· Хирургия стопы и голеностопного сустава\n'
        '· Военно-полевая хирургия\n'
        '· Хирургия кисти и кистевого сустава\n'
        '· Ортопедическая реабилитация\n'
        '· Спортивная медицина\n'
        '· Эндопротезирование суставов\n'
        '· Травматология\n'
        '· Детская травма\n'
        '· Политравма\n'
        '· Реконструктивная хирургия конечностей\n'
        '· Хирургия позвоночника\n'
        '· Ортобиология\n'
        '· Онкоортопедия\n'
    ),
    # Row(Button(Const("Артроскопия"), id="arthroscopy",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Хирургия стопы и голеностопного сустава"), id="foot_ankle_surgery",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Военно-полевая хирургия"), id="military_field_surgery",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Хирургия кисти и кистевого сустава"), id="hand_wrist_surgery",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Ортопедическая реабилитация"), id="orthopedic_rehabilitation",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Спортивная медицина"), id="sports_medicine",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Эндопротезирование суставов"), id="joint_replacement",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Травматология"), id="traumatology",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Детская травма"), id="childhood_trauma",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Политравма"), id="polytrauma",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Реконструктивная хирургия конечностей"), id="reconstructive_surgery_of_the_extremities",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Хирургия позвоночника"), id="spine_surgery",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Ортобиология"), id="orthobiology",
    #            on_click=download_service.empty), ),
    # Row(Button(Const("Онкоортопедия"), id="oncoorthopedics",
    #            on_click=download_service.empty), ),
    Cancel(Const("Назад")),
    parse_mode=ParseMode.HTML,
    state=ProgramMenu.main_menu
)

# window_19_06 = Window(
#     Const("📋Раздел: Программа форума на 19.06"),
#     Row(Button(Const("Направление 1"), id="napr_1_19_06", on_click=download_service.download_19_06_napr_1), ),
#     Row(Button(Const("Направление 2"), id="napr_2_19_06", on_click=download_service.download_19_06_napr_2), ),
#     Row(Button(Const("Направление 3"), id="napr_3_19_06", on_click=download_service.download_19_06_napr_3), ),
#     Cancel(Const("Назад")),
#     state=ProgramMenu.program_19_06_menu,
# )


program_dialog = Dialog(
    main_window,
)
