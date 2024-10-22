from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from sqlalchemy.orm import Session

from db.database import engine, session_factory
from db.models import RaffleUser


def is_exists(ticket_number: int) -> bool:
    with session_factory() as session:
        count_users = (session.query(RaffleUser)
                       .filter(RaffleUser.ticket_number == ticket_number).count())
        session.close()
        return count_users > 0


def reg_raffle_user(raffle_user: RaffleUser) -> None:
    with session_factory() as session:
        session.add(raffle_user)
        session.commit()


def register_raffle_user(callback: CallbackQuery, dialog_manager: DialogManager):
    raffle_user = RaffleUser(
        telegram_id=callback.from_user.id,
        lastname=dialog_manager.find("lastname").get_value(),
        ticket_number=dialog_manager.find("ticket_number").get_value(),
    )
    with session_factory() as session:
        session.add(raffle_user)
        session.commit()
