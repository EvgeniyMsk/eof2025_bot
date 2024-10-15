from typing import Any, Dict

from aiogram.fsm.state import StatesGroup, State
from aiogram_dialog import Window, Dialog, DialogManager, Data, ChatEvent
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Start, ManagedCheckbox, Next, Checkbox, Button, Cancel
from aiogram_dialog.widgets.text import Const, Jinja


class TraumaPointRegister(StatesGroup):
    main_menu = State()
    input_lastname = State()
    input_firstname = State()
    input_email = State()
    input_institute = State()
    input_prof_interests = State()
    result = State()


async def check_changed(event: ChatEvent, checkbox: ManagedCheckbox,
                        manager: DialogManager):
    print("Check status changed:", checkbox.is_checked())


async def main_process_result(start_data: Data, result: Any,
                              dialog_manager: DialogManager):
    print("We have result:", result)

async def get_lastname(dialog_manager: DialogManager, **kwargs):
    return {
        "lastname": dialog_manager.find("lastname").get_value(),
        "firstname": dialog_manager.find("firstname").get_value(),
        "email": dialog_manager.find("firstname").get_value(),
        "institute": dialog_manager.find("firstname").get_value(),
        "check_1": dialog_manager.find("check_1").is_checked(),
        "check_2": dialog_manager.find("check_2").is_checked(),
        "check_3": dialog_manager.find("check_3").is_checked(),
        "check_4": dialog_manager.find("check_4").is_checked(),
        "check_5": dialog_manager.find("check_5").is_checked(),
        "check_6": dialog_manager.find("check_6").is_checked(),
        "check_7": dialog_manager.find("check_7").is_checked(),
        "check_8": dialog_manager.find("check_8").is_checked(),
        "check_9": dialog_manager.find("check_9").is_checked(),
    }

main_dialog = Dialog(
    Window(
        Const(f'"Trauma-POINT" - это чат-бот для '
              f'профессиональных знакомств травматологов-ортопедов\r\n'
              f'"Trauma-POINT" помогает быстро находить '
              f'собеседников для профессиональных знакомств или '
              f'просто приятных бесед во время кофе-брейков.'),
        Row(Start(Const("Регистрация"), id="register", state=TraumaPointRegister.input_lastname)),
        state=TraumaPointRegister.main_menu,
    ),
    Window(
        Const(f'Введите Вашу фамилию'),
        Row(Start(Const("Регистрация1"), id="register", state=TraumaPointRegister.input_lastname)),
        TextInput(id="lastname", on_success=Next()),
        state=TraumaPointRegister.input_lastname,
    ),
    Window(
        Const(f'Введите Ваше имя'),
        TextInput(id="firstname", on_success=Next()),
        state=TraumaPointRegister.input_firstname,
    ),
    Window(
        Const(f'Введите Ваш email'),
        TextInput(id="email", on_success=Next()),
        state=TraumaPointRegister.input_email,
    ),
    Window(
        Const(f'Из какого Вы учреждения?'),
        TextInput(id="institute", on_success=Next()),
        state=TraumaPointRegister.input_institute,
    ),
    Window(
        Const(f'Выберите Вашу сферу профессиональных интересов'),
        Row(
            Checkbox(
                Const("✓  Вальгусная деформация стопы"),
                Const("Вальгусная деформация стопы"),
                id="check_1",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const("✓  Безоперационное лечение суставов"),
                Const("Безоперационное лечение суставов"),
                id="check_2",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Checkbox(
                Const("✓  Эндопротезирование суставов"),
                Const("Эндопротезирование суставов"),
                id="check_3",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const("✓  Артроскопия"),
                Const("Артроскопия"),
                id="check_4",
                default=False,
                on_state_changed=check_changed,
            ),),
        Row(
            Checkbox(
                Const("✓  Спортивные травмы"),
                Const("Спортивные травмы"),
                id="check_5",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const("✓  Кистевая терапия"),
                Const("Кистевая терапия"),
                id="check_6",
                default=False,
                on_state_changed=check_changed,
            ),),
        Row(
            Checkbox(
                Const("✓  Реабилитация после травм или заболевания опорно-двигательного аппарата"),
                Const("Реабилитация после травм или заболевания опорно-двигательного аппарата"),
                id="check_7",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Checkbox(
                Const("✓  Военно-полевая хирургия"),
                Const("Военно-полевая хирургия"),
                id="check_8",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const("✓  Реабилитация"),
                Const("Реабилитация"),
                id="check_9",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Next(),
        ),
        state=TraumaPointRegister.input_prof_interests,
    ),
    Window(
        Jinja(
            "<b>Анкета</b>:\n\n"
            "<b>Фамилия</b>: {{lastname}}\n"
            "<b>Имя</b>: {{firstname}}\n"
            "<b>Учреждение</b>: {{institute}}\n"
            "<b>Интерес 1</b>: {{check_1}}\n"
            "<b>Интерес 2</b>: {{check_2}}\n"
            "<b>Интерес 3</b>: {{check_3}}\n"
            "<b>Интерес 4</b>: {{check_4}}\n"
            "<b>Интерес 5</b>: {{check_5}}\n"
            "<b>Интерес 6</b>: {{check_6}}\n"
            "<b>Интерес 7</b>: {{check_7}}\n"
            "<b>Интерес 8</b>: {{check_8}}\n"
            "<b>Интерес 9</b>: {{check_9}}\n"
        ),
        state=TraumaPointRegister.result,
        getter=get_lastname,
        parse_mode="html",
    ),
    on_process_result=main_process_result
)
