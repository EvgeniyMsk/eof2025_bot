from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const

from states import RaffleMenu

main_dialog = Dialog(
    Window(
        Const("🎲️Раздел в разработке"),
        Cancel(Const('Назад')),
        state=RaffleMenu.main_menu_input_lastname,
    ),
)
