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
            f'При возникновении вопросов и \n'
            f'предложений обращаться по телефону\n'
            f'горячей линии ЕОФ +79647747202\n'
        ),
        Cancel(Const('Назад')),
        state=HelpMenu.main_menu,
        parse_mode=ParseMode.HTML,
    ),
)
