from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Row, Button, Cancel
from aiogram_dialog.widgets.text import Const

from services import program_download_service as download_service
from states import ProgramMenu


async def close_program_dialog(callback: CallbackQuery, button: Button,
                               manager: DialogManager):
    await manager.done(result={"program_dialog": "done"})

main_window = Window(
    Const("📋Раздел: Программа форума"),
    Row(Button(Const("Артроскопия"), id="arthroscopy",
               on_click=download_service.arthroscopy), ),
    Row(Button(Const("Хирургия стопы и голеностопного сустава"), id="foot_ankle_surgery",
               on_click=download_service.foot_ankle_surgery), ),
    Row(Button(Const("Военно-полевая хирургия"), id="military_field_surgery",
               on_click=download_service.military_field_surgery), ),
    Row(Button(Const("Хирургия кисти и кистевого сустава"), id="hand_wrist_surgery",
               on_click=download_service.hand_wrist_surgery), ),
    Row(Button(Const("Ортопедическая реабилитация"), id="orthopedic_rehabilitation",
               on_click=download_service.orthopedic_rehabilitation), ),
    Row(Button(Const("Спортивная медицина"), id="sports_medicine",
               on_click=download_service.sports_medicine), ),
    Row(Button(Const("Эндопротезирование суставов"), id="joint_replacement",
               on_click=download_service.joint_replacement), ),
    Row(Button(Const("Травматология"), id="traumatology",
               on_click=download_service.traumatology), ),
    Row(Button(Const("Детская травма"), id="childhood_trauma",
               on_click=download_service.childhood_trauma), ),
    Row(Button(Const("Политравма"), id="polytrauma",
               on_click=download_service.polytrauma), ),
    Row(Button(Const("Реконструктивная хирургия конечностей"), id="reconstructive_surgery_of_the_extremities",
               on_click=download_service.reconstructive_surgery_of_the_extremities), ),
    Row(Button(Const("Хирургия позвоночника"), id="spine_surgery",
               on_click=download_service.spine_surgery), ),
    Row(Button(Const("Ортобиология"), id="orthobiology",
               on_click=download_service.orthobiology), ),
    Row(Button(Const("Онкоортопедия"), id="oncoorthopedics",
               on_click=download_service.oncoorthopedics), ),
    Cancel(Const("Назад")),
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
