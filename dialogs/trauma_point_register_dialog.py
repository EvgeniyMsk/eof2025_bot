from typing import Any

from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager, Data, ChatEvent, StartMode
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Start, ManagedCheckbox, Next, Checkbox, Back, Cancel, Button
from aiogram_dialog.widgets.text import Const, Jinja

from services.trauma_point_service import register_eof_user
from states import TraumaPointRegister, TraumaPointWork, MainMenu

def get_pre_result() -> str:
    return 'test'

async def check_changed(event: ChatEvent, checkbox: ManagedCheckbox,
                        manager: DialogManager):
    print("Check status changed:", checkbox.is_checked())


async def main_process_result(start_data: Data, result: Any,
                              dialog_manager: DialogManager):
    print("We have result1:", result)


async def go_to_main(callback: CallbackQuery, button: Button,
                     dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def go_clicked(callback: CallbackQuery, button: Button,
                     dialog_manager: DialogManager):
    try:
        register_eof_user(callback, dialog_manager)
        await dialog_manager.start(TraumaPointWork.main_menu, mode=StartMode.RESET_STACK)
    except Exception as e:
        await callback.message.answer(text='Вы уже были зарегистрированы')
        await dialog_manager.start(TraumaPointWork.main_menu, mode=StartMode.RESET_STACK)


async def get_lastname(dialog_manager: DialogManager, **kwargs):
    return {
        "lastname": dialog_manager.find("lastname").get_value(),
        "firstname": dialog_manager.find("firstname").get_value(),
        "email": dialog_manager.find("email").get_value(),
        "institute": dialog_manager.find("institute").get_value(),
        "check_1": dialog_manager.find("check_1").is_checked(),
        "check_2": dialog_manager.find("check_2").is_checked(),
        "check_3": dialog_manager.find("check_3").is_checked(),
        "check_4": dialog_manager.find("check_4").is_checked(),
        "check_5": dialog_manager.find("check_5").is_checked(),
        "check_6": dialog_manager.find("check_6").is_checked(),
        "check_7": dialog_manager.find("check_7").is_checked(),
        "check_8": dialog_manager.find("check_8").is_checked(),
        "check_9": dialog_manager.find("check_9").is_checked(),

        "check_non_1": dialog_manager.find("check_non_1").is_checked(),
        "check_non_2": dialog_manager.find("check_non_2").is_checked(),
        "check_non_3": dialog_manager.find("check_non_3").is_checked(),
        "check_non_4": dialog_manager.find("check_non_4").is_checked(),
        "check_non_5": dialog_manager.find("check_non_5").is_checked(),
        "check_non_6": dialog_manager.find("check_non_6").is_checked(),
        "check_non_7": dialog_manager.find("check_non_7").is_checked(),
        "check_non_8": dialog_manager.find("check_non_8").is_checked(),

        "personal_request": dialog_manager.find("personal_request").get_value(),
    }


professional_interests = [
    'Вальгусная деформация стопы',
    'Безоперационное лечение суставов',
    'Эндопротезирование суставов',
    'Артроскопия',
    'Спортивные травмы',
    'Кистевая терапия',
    'Реабилитация после травм или заболевания опорно-двигательного аппарата',
    'Военно-полевая хирургия',
    'Реабилитация'
]

non_professional_interests = [
    'Наука🔭',
    'Спорт⚽',
    'Охота и рыбалка🐟',
    'Автомобили и мотоциклы🛺',
    'Предпринимательство👨‍💼',
    'Психология👨‍️',
    'Искусство и творчество🎨',
    'Технологии и инновации🤖',
]

main_dialog = Dialog(
    Window(
        Jinja(f'<b>"Trauma-POINT"</b>💬 - это чат-бот для '
              f'профессиональных знакомств травматологов-ортопедов.\r\n'
              f'<b>"Trauma-POINT"</b> помогает быстро находить '
              f'собеседников для профессиональных знакомств или '
              f'просто приятных бесед во время кофе-брейков.\r\n'
              f'\r\n'
              f'<b>Для продолжения введите Вашу фамилию</b>'),
        Button(Const(text="Назад"), id='to_main', on_click=go_to_main),
        TextInput(id="lastname", on_success=Next()),
        state=TraumaPointRegister.main_menu_input_lastname,
        parse_mode="html",
    ),
    Window(
        Const(f'Введите Ваше имя'),
        TextInput(id="firstname", on_success=Next()),
        Row(Back(Const("Назад"))),
        state=TraumaPointRegister.input_firstname,
    ),
    Window(
        Const(f'✉️Введите Ваш email'),
        TextInput(id="email", on_success=Next()),
        Row(Back(Const("Назад"))),
        state=TraumaPointRegister.input_email,
    ),
    Window(
        Const(f'🏬Из какого Вы учреждения?'),
        TextInput(id="institute", on_success=Next()),
        Row(Back(Const("Назад"))),
        state=TraumaPointRegister.input_institute,
    ),
    Window(
        Const(f'Выберите Вашу сферу профессиональных интересов'),
        Row(
            Checkbox(
                Const(f'✅  {professional_interests[0]}'),
                Const(f'{professional_interests[0]}'),
                id="check_1",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {professional_interests[1]}'),
                Const(f'{professional_interests[1]}'),
                id="check_2",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Checkbox(
                Const(f'✅  {professional_interests[2]}'),
                Const(f'{professional_interests[2]}'),
                id="check_3",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {professional_interests[3]}'),
                Const(f'{professional_interests[3]}'),
                id="check_4",
                default=False,
                on_state_changed=check_changed,
            ), ),
        Row(
            Checkbox(
                Const(f'✅  {professional_interests[4]}'),
                Const(f'{professional_interests[4]}'),
                id="check_5",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {professional_interests[5]}'),
                Const(f'{professional_interests[5]}'),
                id="check_6",
                default=False,
                on_state_changed=check_changed,
            ), ),
        Row(
            Checkbox(
                Const(f'✅  {professional_interests[6]}'),
                Const(f'{professional_interests[6]}'),
                id="check_7",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Checkbox(
                Const(f'✅  {professional_interests[7]}'),
                Const(f'{professional_interests[7]}'),
                id="check_8",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {professional_interests[8]}'),
                Const(f'{professional_interests[8]}'),
                id="check_9",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Row(Back(Const("Назад"))),
            Next(Const('Далее')),
        ),
        state=TraumaPointRegister.input_prof_interests,
    ),
    Window(
        Jinja(f'Какие темы для <b>непрофессионального</b> общения Вас интересуют?'),
        Row(
            Checkbox(
                Const(f'✅  {non_professional_interests[0]}'),
                Const(f'{non_professional_interests[0]}'),
                id="check_non_1",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {non_professional_interests[1]}'),
                Const(f'{non_professional_interests[1]}'),
                id="check_non_2",
                default=False,
                on_state_changed=check_changed,
            ),

        ),
        Row(
            Checkbox(
                Const(f'✅  {non_professional_interests[2]}'),
                Const(f'{non_professional_interests[2]}'),
                id="check_non_3",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {non_professional_interests[3]}'),
                Const(f'{non_professional_interests[3]}'),
                id="check_non_4",
                default=False,
                on_state_changed=check_changed,
            ), ),
        Row(
            Checkbox(
                Const(f'✅  {non_professional_interests[4]}'),
                Const(f'{non_professional_interests[4]}'),
                id="check_non_5",
                default=False,
                on_state_changed=check_changed,
            ),
            Checkbox(
                Const(f'✅  {non_professional_interests[5]}'),
                Const(f'{non_professional_interests[5]}'),
                id="check_non_6",
                default=False,
                on_state_changed=check_changed,
            ), ),
        Row(
            Checkbox(
                Const(f'✅  {non_professional_interests[6]}'),
                Const(f'{non_professional_interests[6]}'),
                id="check_non_7",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(
            Checkbox(
                Const(f'✅  {non_professional_interests[7]}'),
                Const(f'{non_professional_interests[7]}'),
                id="check_non_8",
                default=False,
                on_state_changed=check_changed,
            ),
        ),
        Row(Back(Const("Назад")), Next(Const('Далее'))),
        state=TraumaPointRegister.input_non_prof_interests,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Напишите пару слов о себе'),
        TextInput(id="personal_request", on_success=Next()),
        Row(Back(Const("Назад")), Next(Const('Пропустить, просмотр анкеты'))),
        state=TraumaPointRegister.personal_request,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(
            f'<b>🧑‍💼Ваша анкета</b>:\n\n'
            '<b>Фамилия</b>: {{lastname}}\n'
            '<b>Имя</b>: {{firstname}}\n'
            '<b>E-mail</b>: {{email}}\n'
            '<b>Учреждение</b>: {{institute}}\n'
            '{% if check_1 == True %}<b>' + professional_interests[0] + '</b>\n {% endif %}' +
            '{% if check_2 == True %}<b>' + professional_interests[1] + '</b>\n {% endif %}' +
            '{% if check_3 == True %}<b>' + professional_interests[2] + '</b>\n {% endif %}' +
            '{% if check_4 == True %}<b>' + professional_interests[3] + '</b>\n {% endif %}' +
            '{% if check_5 == True %}<b>' + professional_interests[4] + '</b>\n {% endif %}' +
            '{% if check_6 == True %}<b>' + professional_interests[5] + '</b>\n {% endif %}' +
            '{% if check_7 == True %}<b>' + professional_interests[6] + '</b>\n {% endif %}' +
            '{% if check_8 == True %}<b>' + professional_interests[7] + '</b>\n {% endif %}' +
            '{% if check_9 == True %}<b>' + professional_interests[8] + '</b>\n {% endif %}' +

            '{% if check_non_1 == True %}<b>' + non_professional_interests[0] + '</b>\n {% endif %}' +
            '{% if check_non_2 == True %}<b>' + non_professional_interests[1] + '</b>\n {% endif %}' +
            '{% if check_non_3 == True %}<b>' + non_professional_interests[2] + '</b>\n {% endif %}' +
            '{% if check_non_4 == True %}<b>' + non_professional_interests[3] + '</b>\n {% endif %}' +
            '{% if check_non_5 == True %}<b>' + non_professional_interests[4] + '</b>\n {% endif %}' +
            '{% if check_non_6 == True %}<b>' + non_professional_interests[5] + '</b>\n {% endif %}' +
            '{% if check_non_7 == True %}<b>' + non_professional_interests[6] + '</b>\n {% endif %}' +
            '{% if check_non_8 == True %}<b>' + non_professional_interests[7] + '</b>\n {% endif %}' +
            # f'<b>{non_professional_interests[0]}''</b>: {{check_non_1}}\n'
            # f'<b>{non_professional_interests[1]}''</b>: {{check_non_2}}\n'
            # f'<b>{non_professional_interests[2]}''</b>: {{check_non_3}}\n'
            # f'<b>{non_professional_interests[3]}''</b>: {{check_non_4}}\n'
            # f'<b>{non_professional_interests[4]}''</b>: {{check_non_5}}\n'
            # f'<b>{non_professional_interests[5]}''</b>: {{check_non_6}}\n'
            # f'<b>{non_professional_interests[6]}''</b>: {{check_non_7}}\n'
            # f'<b>{non_professional_interests[7]}''</b>: {{check_non_8}}\n'
            '{% if personal_request != None %} <b>О себе:</b> {{personal_request}}\n {% endif %}'
        ),
        Back(Const('Назад')),
        Start(Const('Начать общение'), id='start_chatting', state=TraumaPointWork.main_menu, on_click=go_clicked),
        state=TraumaPointRegister.result,
        getter=get_lastname,
        parse_mode="html",
    ),
    on_process_result=main_process_result
)
