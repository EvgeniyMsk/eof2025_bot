from __future__ import annotations

from typing import Set

from sqlalchemy import Column, MetaData, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from db.database import Base, engine, session_factory

metadata = MetaData()

eof_users_professional_interests = Table(
    "eof_users_professional_interests",
    metadata,
    Column("user_id", ForeignKey("eof_users.id"), primary_key=True),
    Column("professional_interest_id", ForeignKey("professional_interest.id"), primary_key=True),
)

eof_users_non_professional_interests = Table(
    "eof_users_non_professional_interests",
    metadata,
    Column("user_id", ForeignKey("eof_users.id"), primary_key=True),
    Column("non_professional_interest_id", ForeignKey("non_professional_interest.id"), primary_key=True),
)


class EofUser(Base):
    __tablename__ = "eof_users"
    metadata = metadata
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, default=0, unique=True)
    lastname: Mapped[str] = mapped_column(String, default='')
    firstname: Mapped[str] = mapped_column(String, default='')
    email: Mapped[str] = mapped_column(String, default='')
    institute: Mapped[str] = mapped_column(String, default='')
    note: Mapped[str] = mapped_column(String, default='')
    professional_interests: Mapped[Set[ProfessionalInterest]] = relationship(
        secondary=eof_users_professional_interests, back_populates="eof_users",
        lazy="subquery",
    )
    non_professional_interests: Mapped[Set[NonProfessionalInterest]] = relationship(
        secondary=eof_users_non_professional_interests, back_populates="eof_users",
        lazy="subquery",
    )


class ProfessionalInterest(Base):
    __tablename__ = "professional_interest"
    metadata = metadata
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    eof_users: Mapped[Set[EofUser]] = relationship(
        secondary=eof_users_professional_interests, back_populates="professional_interests"
    )


class NonProfessionalInterest(Base):
    __tablename__ = "non_professional_interest"
    metadata = metadata
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    eof_users: Mapped[Set[EofUser]] = relationship(
        secondary=eof_users_non_professional_interests, back_populates="non_professional_interests"
    )


class RaffleUser(Base):
    __tablename__ = "raffle_users"
    metadata = metadata
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, default=0, unique=True)
    lastname: Mapped[str] = mapped_column(String, default='')
    ticket_number: Mapped[int] = mapped_column(Integer, default=0, unique=True)


professional_interests = [
    'Вальгусная деформация стопы',
    'Безоперационное лечение суставов',
    'Эндопротезирование суставов',
    'Артроскопия',
    'Спортивные травмы',
    'Кистевая терапия',
    'Реабилитация после травм или заболевания опорно-двигательного аппарата',
    'Военно-полевая хирургия',
    'Реабилитация'
]

non_professional_interests = [
    'Наука🔭',
    'Спорт⚽',
    'Охота и рыбалка🐟',
    'Автомобили и мотоциклы🛺',
    'Предпринимательство👨‍💼',
    'Психология👨‍️',
    'Искусство и творчество🎨',
    'Технологии и инновации🤖',
]


def create_tables():
    metadata.drop_all(engine)
    metadata.create_all(engine)

    with session_factory() as session:
        for i in professional_interests:
            session.add(ProfessionalInterest(name=i))
        for i in non_professional_interests:
            session.add(NonProfessionalInterest(name=i))
        session.commit()


def create_user(tg_id, lastname, firstname, email, institute, note, professional_arr, non_professional_arr):
    with session_factory() as session:
        professional_interests = set()
        non_professional_interests = set()

        professional_interests_from_db = session.query(ProfessionalInterest).all()
        for i in professional_arr:
            professional_interests.add(professional_interests_from_db[i])

        non_professional_interests_from_db = session.query(NonProfessionalInterest).all()
        for i in non_professional_arr:
            non_professional_interests.add(non_professional_interests_from_db[i])

        user1 = EofUser(
            telegram_id=tg_id,
            lastname=lastname,
            firstname=firstname,
            email=email,
            institute=institute,
            note=note,
            professional_interests=professional_interests,
            non_professional_interests=non_professional_interests,
        )
        session.add(user1)
        session.commit()


# create_user(tg_id=3,
#             lastname='Петров',
#             firstname='Андрей',
#             email='petroff@yandex.ru',
#             institute='СПБГМУ им. Павлова',
#             note='Начинающий врач',
#             professional_arr=[0, 1, 2],
#             non_professional_arr=[2, 3],)

# create_tables()
