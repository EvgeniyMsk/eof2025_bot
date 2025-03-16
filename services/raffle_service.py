from typing import List

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from db.database import session_factory
from db.models import RaffleUser, Status


def is_exists(ticket_number: int) -> bool:
    with session_factory() as session:
        count_users = (session.query(RaffleUser)
                       .filter(RaffleUser.ticket_number == ticket_number).count())
        session.close()
        return count_users > 0


def set_raffle_active():
    with session_factory() as session:
        session.query(Status).filter(Status.type_of_status == 'raffle').update({Status.value: 1})
        session.commit()


def set_raffle_inactive():
    with session_factory() as session:
        session.query(Status).filter(Status.type_of_status == 'raffle').update({Status.value: 0})
        session.commit()


def is_raffle_active() -> int:
    with session_factory() as session:
        result = (session.query(Status)
                  .filter(Status.type_of_status == 'raffle')
                  .filter(Status.value == 1).count())
        return result


def get_all_users() -> List[RaffleUser]:
    with session_factory() as session:
        result = (session.query(RaffleUser)).all()
        session.close()
    return result


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
