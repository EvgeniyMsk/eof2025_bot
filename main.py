import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.fsm.storage import redis
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    Message
from aiogram_dialog import StartMode
from aiogram_dialog import (
    setup_dialogs, DialogManager, )

import bot_config
from db.database import session_factory
from db.models import BotUser, add_new_user
from dialogs import help_dialog as help_dialog
from dialogs import lesson_dialog as ld_dialog
from dialogs import main_dialog as main_dialog
from dialogs import program_dialog as pg_dialog
from dialogs import quest_dialog as qd_dialog
from dialogs import raffle_dialog as raf_dialog
from dialogs import trauma_point_register_dialog as trp_dialog
from dialogs import trauma_point_work_dialog as tw_dialog
from services import raffle_service

bot = Bot(token=bot_config.main_config.bot_token)
redis_client = redis.Redis(host=bot_config.REDIS_HOST,
                           username=bot_config.REDIS_USERNAME,
                           password=bot_config.REDIS_PASSWORD,
                           port=bot_config.REDIS_PORT,
                           db=bot_config.REDIS_DB)
redis_db = redis.Redis(host=bot_config.REDIS_HOST,
                       username=bot_config.REDIS_USERNAME,
                       password=bot_config.REDIS_PASSWORD,
                       port=bot_config.REDIS_PORT,
                       db='1')
storage = RedisStorage(
    redis_client,
    key_builder=DefaultKeyBuilder(with_destiny=True),
)
dp = Dispatcher(storage=storage)
main_router = Router()


def is_from_admin(message: Message) -> bool:
    return message.from_user.id in [int(bot_config.ADMIN_ID), 300970915]


@main_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    # Добавление нового пользователя при нажатии /start #
    add_new_user(message.from_user.id)
    if is_from_admin(message):
        kb = ReplyKeyboardMarkup(keyboard=[[
            KeyboardButton(text='В начало'),
            KeyboardButton(text='Запуск розыгрыша'),
            KeyboardButton(text='Остановка розыгрыша'),
        ]], resize_keyboard=True)
        await message.reply('/start', reply_markup=kb)
    else:
        kb = ReplyKeyboardMarkup(keyboard=[[
            KeyboardButton(text='В начало'),
        ]], resize_keyboard=True)
        await message.reply('/start', reply_markup=kb)
    await dialog_manager.start(main_dialog.MainMenu.main_menu, mode=StartMode.RESET_STACK)


@main_router.message(F.text == 'Запуск розыгрыша')
async def send_notification(message: Message, dialog_manager: DialogManager):
    # Запуск розыгрыша
    if is_from_admin(message) and message.chat.type == 'private':
        text = message.text[16:]
        if len(text) == 0:
            with session_factory() as session:
                users = session.query(BotUser).all()
        for user in users:
            try:
                await bot.send_message(
                    user.telegram_id,
                    'Информация для участников ЕОФ-2025:\nРозыгрыш автомобиля начался')
                raffle_service.set_raffle_active()
            except Exception as e:
                logging.exception(e)


@main_router.message(F.text == 'Остановка розыгрыша')
async def send_notification(message: Message, dialog_manager: DialogManager):
    # Остановка розыгрыша автомобиля
    if is_from_admin(message) and message.chat.type == 'private':
        text = message.text[19:]
        if len(text) == 0:
            with session_factory() as session:
                users = session.query(BotUser).all()
        for user in users:
            try:
                await bot.send_message(
                    user.telegram_id,
                    'Информация для участников ЕОФ-2025:\nРозыгрыш автомобиля завершен :)')
                raffle_service.set_raffle_inactive()
            except Exception as e:
                logging.exception(e)


@main_router.message(Command('sendAll'))
async def send_notification(message: Message, dialog_manager: DialogManager):
    # Отправка нотификаций всем пользователям
    if is_from_admin(message) and message.chat.type == 'private':
        text = message.text[9:]
        if len(text) > 0:
            with session_factory() as session:
                users = session.query(BotUser).all()
        for user in users:
            try:
                await bot.send_message(user.telegram_id, text)
            except Exception as e:
                logging.exception(e)


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router=main_router)
    dp.include_router(router=main_dialog.main_dialog)
    dp.include_router(router=pg_dialog.program_dialog)
    dp.include_router(router=trp_dialog.main_dialog)
    dp.include_router(router=raf_dialog.main_dialog)
    dp.include_router(router=qd_dialog.main_dialog)
    dp.include_router(router=ld_dialog.main_dialog)
    dp.include_router(router=tw_dialog.main_dialog)
    dp.include_router(router=help_dialog.main_dialog)

    setup_dialogs(dp)
    await dp.start_polling(bot)


async def download_document(message: Message, path: str):
    file_id = message.document.file_id
    file_name = message.document.file_name
    file = await bot.get_file(file_id)
    file_path = file.file_path
    destination = os.path.abspath(os.path.curdir) + path
    await bot.download_file(file_path, destination)
    await message.reply(f"Файл {file_name} успешно сохранен на сервере.")


if __name__ == '__main__':
    asyncio.run(main())
