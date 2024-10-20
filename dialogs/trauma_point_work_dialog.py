from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from aiogram_dialog import Window, Dialog, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Cancel, Button, StubScroll, Row, FirstPage, \
    PrevPage, NextPage, LastPage, Url
from aiogram_dialog.widgets.text import Const, Format

from services import trauma_point_service
from states import TraumaPointWork, MainMenu

people = trauma_point_service.get_people()


async def go_clicked(callback: CallbackQuery, button: Button,
                     dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def people_getter(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find("list_scroll").get_page()
    return {
        "pages": len(people["people"]),
        "current_page": current_page + 1,
        "user_id": people["people"][current_page]["user_id"],
        "lastname": people["people"][current_page]["lastname"],
        "firstname": people["people"][current_page]["firstname"],
        "email": people["people"][current_page]["email"],
        "institute": people["people"][current_page]["institute"],
        "professional_interests": people["people"][current_page]["professional_interests"],
        "non_professional_interests": people["people"][current_page]["non_professional_interests"],
        "note": people["people"][current_page]["note"],
    }


# async def go_clicked(callback: CallbackQuery, button: Button,
#                      manager: DialogManager):
#     await callback.message.answer("Ок")


main_dialog = Dialog(
    Window(
        Const("Trauma-POINT знакомства\n"),
        Format(f"<b>Анкета:</b>\r\n"
               "Имя: {lastname} {firstname}\r\n"
               "email: {email}\r\n"
               "Организация: {institute}\r\n"
               "Профессиональные интересы: {professional_interests}\r\n"
               "Непрофессиональные интересы: {non_professional_interests}\r\n"
               "О себе: {note}\r\n"),
        StubScroll(id="list_scroll", pages="pages"),
        Url(
            Format("Написать"),
            Format("tg://openmessage?user_id={user_id}"),
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
        getter=people_getter,
        parse_mode=ParseMode.HTML,
    )
)
