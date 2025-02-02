import os
from os.path import join, dirname
from typing import Any

from aiogram.enums import ContentType, ParseMode
from aiogram.fsm.state import State
from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder, ButtonType
from aiogram_dialog import Window, Dialog, DialogManager, Data
from aiogram_dialog.widgets.kbd import Row, Start, Button, Group, Column
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Jinja

from bot_config import main_config
from dialogs.program_dialog import ProgramMenu
from dialogs.trauma_point_register_dialog import TraumaPointRegister
from services import trauma_point_service
from states import MainMenu, RaffleMenu, QuestMenu, LessonMenu, TraumaPointWork


def none():
    return None


builder = InlineKeyboardBuilder()



async def main_process_result(start_data: Data, result: Any,
                              dialog_manager: DialogManager):
    print("We have result:", result)


main_dialog = Dialog(
    Window(
        StaticMedia(
            path=os.path.abspath(os.curdir) + '/files/images/main_theme.jpg',
            type=ContentType.PHOTO,
        ),
        Jinja(
            f'Здравствуй, участник ЕОФ-2025! Я ЕОФ-бот 🤖.\n\n'
            '<b>ЕОФ пройдет 19-21 июня в Москве – в Центральном выставочном зале «Манеж». Мы очень ждем Вас там!</b>\n'
            'С моей помощью Вы сможете:\n'
            '· ознакомиться с программой Форума\n'
            '· познакомиться с коллегами с помощью Trauma-POINT – бота для профессиональных знакомств по интересам\n'
            '· подать доклад в программу и оценить доклады коллег\n'
            '· пройти квест по выставке на ЕОФ\n'
            '· участвовать в розыгрыше ценных призов.\n'
            'Для продолжения выберите пункт меню\n'
        ),
        Row(
            Start(Const("📋Программа форума"), id="program", state=ProgramMenu.main_menu),
        ),
        Row(
            Start(Const("💬Trauma-POINT бот для профессиональных знакомств"), id="trauma_point_register",
                  state=TraumaPointRegister.main_menu_input_lastname),
            when=trauma_point_service.user_not_registered
        ),
        Row(
            Start(Const("💬Trauma-POINT бот для профессиональных знакомств"), id="trauma_point_work",
                  state=TraumaPointWork.main_menu),
            when=trauma_point_service.user_registered
        ),
        # Start(Const("🎲Участие в розыгрыше"), id="raffle", state=RaffleMenu.main_menu_input_lastname),
        # Start(Const("🤳Квест по выставке"), id="quest", state=QuestMenu.main_menu),
        Start(Const("✍️ЕОФ-постеры"), id="stand_presentation", state=LessonMenu.main_menu),
        state=MainMenu.main_menu,
        parse_mode=ParseMode.HTML,
    ),
    on_process_result=main_process_result,
)
