from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const

from states import QuestMenu

main_dialog = Dialog(
    Window(
        Const("🤳Раздел в разработке"),
        Cancel(Const('Назад')),
        state=QuestMenu.main_menu,
    ),
    on_process_result=QuestMenu.main_menu,
)