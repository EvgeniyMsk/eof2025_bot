import os

from aiogram.enums import ContentType, ParseMode
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Jinja

from states import HelpMenu

main_dialog = Dialog(
    Window(
        StaticMedia(
            path=os.path.abspath(os.path.curdir) + '/files/images/help_dialog/help_theme.jpeg',
            type=ContentType.PHOTO,
        ),
        Jinja(
            f'При возникновении вопросов и предложений\n'
            f'обращаться в Telegram @kharlanova_da\n'
        ),
        Cancel(Const('Назад')),
        state=HelpMenu.main_menu,
        parse_mode=ParseMode.HTML,
    ),
)
