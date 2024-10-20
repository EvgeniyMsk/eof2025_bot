from sqlalchemy.orm import Session

from db.database import engine
from db.schema import RaffleUser


def is_exists(ticket_number: int) -> bool:
    session = Session(bind=engine)
    count_users = (session.query(RaffleUser)
                   .filter(RaffleUser.ticket_number == ticket_number).count())
    session.close()
    return count_users > 0


def reg_raffle_user(raffle_user: RaffleUser) -> None:
    session = Session(bind=engine)
    session.add(raffle_user)
    session.commit()
    session.close()
