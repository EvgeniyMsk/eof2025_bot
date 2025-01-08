from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Cancel, Url
from aiogram_dialog.widgets.link_preview import LinkPreview
from aiogram_dialog.widgets.text import Const

from states import LessonMenu

main_dialog = Dialog(
    Window(
    Const("Подать ЕОФ-постер в программу"),

        Url(
            Const("Подать ЕОФ-постер в программу"),
            Const('https://docs.google.com/forms/d/e/1FAIpQLSeG8QnPhj3u-y-pjj1C8VMcwUZXXh2-VuoSvNA79MWOGFqBDw/viewform'),
        ),
        Cancel(Const('Назад')),
        state=LessonMenu.main_menu,
    ),
)
