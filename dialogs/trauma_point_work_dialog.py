from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, StubScroll, Row, FirstPage, \
    PrevPage, NextPage, LastPage, Url
from aiogram_dialog.widgets.text import Const, Format

from services import trauma_point_service
from states import TraumaPointWork, MainMenu

people = trauma_point_service.get_people_from_db()


async def go_clicked(callback: CallbackQuery, button: Button,
                     dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)



# async def go_clicked(callback: CallbackQuery, button: Button,
#                      manager: DialogManager):
#     await callback.message.answer("Ок")


main_dialog = Dialog(
    Window(
        Format(f"<b>Trauma-POINT</b> знакомства\r\n\r\n"
               f"<b>Анкета:</b>\r\n"
               "<b>id:</b>{id}\r\n"
               "<b>telegram_id:</b>{telegram_id}\r\n"
               "<b>Имя:</b> {lastname} {firstname}\r\n"
               "<b>email:</b> {email}\r\n"
               "<b>Организация:</b> {institute}\r\n"
               "<b>Профессиональные интересы:</b> {professional_interests}\r\n"
               "<b>Непрофессиональные интересы:</b> {non_professional_interests}\r\n"
               "<b>О себе:</b> {note}\r\n"),
        StubScroll(id="list_scroll", pages="pages"),
        Url(
            Format("Написать"),
            Format("tg://openmessage?user_id={telegram_id}"),
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
        ),
        Button(Const(text="На главную"), id='to_main', on_click=go_clicked),
        state=TraumaPointWork.main_menu,
        getter=trauma_point_service.people_getter,
        parse_mode=ParseMode.HTML,
    )
)
