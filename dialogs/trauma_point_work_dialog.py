from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, StubScroll, Row, FirstPage, \
    PrevPage, NextPage, LastPage, Url, Column
from aiogram_dialog.widgets.text import Const, Format

from services import trauma_point_service
from states import TraumaPointWork, MainMenu, TraumaPointRegister


async def go_to_main(callback: CallbackQuery, button: Button,
                     dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def go_to_profile(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    await dialog_manager.start(TraumaPointRegister.main_menu_input_lastname, mode=StartMode.RESET_STACK)


# async def go_clicked(callback: CallbackQuery, button: Button,
#                      manager: DialogManager):
#     await callback.message.answer("Ок")


main_dialog = Dialog(
    Window(
        Format(f"Нет подходящих профилей :(",
               when=trauma_point_service.is_users_not_contains),
        Format(f"<b>Trauma-POINT</b> знакомства\r\n\r\n"
               f"<b>Анкета:</b>\r\n"
               # "<b>id:</b>{id}\r\n"
               # "<b>telegram_id:</b>{telegram_id}\r\n"
               "<b>Имя:</b> {lastname} {firstname}\r\n"
               # "<b>email:</b> {email}\r\n"
               "<b>Организация:</b> {institute}\r\n"
               "<b>Профессиональные интересы:</b> {professional_interests}\r\n"
               "<b>Непрофессиональные интересы:</b> {non_professional_interests}\r\n"
               "<b>О себе:</b> {note}\r\n",
               when=trauma_point_service.is_users_contains),
        StubScroll(id="list_scroll", pages="pages"),
        Row(
            Url(
                Format("Написать"),
                Format("tg://openmessage?user_id={telegram_id}"),
            ),
            when=trauma_point_service.is_users_contains
        ),
        Row(
            FirstPage(
                scroll="list_scroll", text=Format("Начало"),
            ),
            PrevPage(
                scroll="list_scroll", text=Format("◀️"),
            ),
            NextPage(
                scroll="list_scroll", text=Format("▶️"),
            ),
            LastPage(
                scroll="list_scroll", text=Format("Конец"),
            ),
            when=trauma_point_service.is_users_contains
        ),
        Button(Const(text="Изменить профиль"), id='to_change_profile', on_click=go_to_profile),
        Button(Const(text="На главную"), id='to_main', on_click=go_to_main),
        state=TraumaPointWork.main_menu,
        getter=trauma_point_service.people_getter,
        parse_mode=ParseMode.HTML,
    )
)
