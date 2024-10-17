from sqlalchemy import Column, Integer, String

from database.database import Base


class RaffleUser(Base):
    __tablename__ = 'raffle_users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    last_name = Column(String(50))
    ticket_number = Column(Integer)