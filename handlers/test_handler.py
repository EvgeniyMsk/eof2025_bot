from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import StartMode, DialogManager

from dialogs.main_dialog import MainMenu

main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)
