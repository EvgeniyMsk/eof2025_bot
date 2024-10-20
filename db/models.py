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
        secondary=eof_users_professional_interests, back_populates="eof_users"
    )
    non_professional_interests: Mapped[Set[NonProfessionalInterest]] = relationship(
        secondary=eof_users_non_professional_interests, back_populates="eof_users"
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

create_tables()
