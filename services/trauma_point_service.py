import json
from typing import List

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from db.models import EofUser, ProfessionalInterest, NonProfessionalInterest
from db.database import session_factory


def get_people():
    with open("people.json", mode="r", encoding="utf-8") as input_file:
        original_json = input_file.read()
    people = json.loads(original_json)
    return people


def get_people_from_db() -> List[EofUser]:
    with session_factory() as session:
        people = session.query(EofUser).all()
        return people


def register_eof_user(callback: CallbackQuery, dialog_manager: DialogManager):
    eof_user = EofUser(
        telegram_id=callback.from_user.id,
        lastname=dialog_manager.find("lastname").get_value(),
        firstname=dialog_manager.find("firstname").get_value(),
        email=dialog_manager.find("email").get_value(),
        institute=dialog_manager.find("institute").get_value(),
        note=dialog_manager.find("personal_request").get_value()
    )
    prof_interests = [
        dialog_manager.find("check_1").is_checked(),
        dialog_manager.find("check_2").is_checked(),
        dialog_manager.find("check_3").is_checked(),
        dialog_manager.find("check_4").is_checked(),
        dialog_manager.find("check_5").is_checked(),
        dialog_manager.find("check_6").is_checked(),
        dialog_manager.find("check_7").is_checked(),
        dialog_manager.find("check_8").is_checked(),
        dialog_manager.find("check_9").is_checked(),
    ]
    non_prof_interests = [
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_2").is_checked(),
        dialog_manager.find("check_non_3").is_checked(),
        dialog_manager.find("check_non_4").is_checked(),
        dialog_manager.find("check_non_5").is_checked(),
        dialog_manager.find("check_non_6").is_checked(),
        dialog_manager.find("check_non_7").is_checked(),
        dialog_manager.find("check_non_8").is_checked(),
    ]
    professional_interests = set()
    non_professional_interests = set()
    j = 0
    for i in prof_interests:
        j = j + 1
        if i is True:
            with session_factory() as session:
                p_i = session.query(ProfessionalInterest).where(ProfessionalInterest.id == j).one()
                professional_interests.add(p_i)
    j = 0
    for i in non_prof_interests:
        j = j + 1
        if i is True:
            with session_factory() as session:
                np_i = session.query(NonProfessionalInterest).where(NonProfessionalInterest.id == j).one()
                non_professional_interests.add(np_i)

    eof_user.professional_interests = professional_interests
    eof_user.non_professional_interests = non_professional_interests

    with session_factory() as session:
        session.add(eof_user)
        session.commit()


professional_interests_dict = {
    1: 'Вальгусная деформация стопы',
    2: 'Безоперационное лечение суставов',
    3: 'Эндопротезирование суставов',
    4: 'Артроскопия',
    5: 'Спортивные травмы',
    6: 'Кистевая терапия',
    7: 'Реабилитация после травм или заболевания опорно-двигательного аппарата',
    8: 'Военно-полевая хирургия',
    9: 'Реабилитация'
}

non_professional_interests_dict = {
    1: 'Наука🔭',
    2: 'Спорт⚽',
    3: 'Охота и рыбалка🐟',
    4: 'Автомобили и мотоциклы🛺',
    5: 'Предпринимательство👨‍💼',
    6: 'Психология👨️',
    7: 'Искусство и творчество🎨',
    8: 'Технологии и инновации🤖',
}


async def people_getter(dialog_manager: DialogManager, **_kwargs):
    people = get_people_from_db()
    current_page = await dialog_manager.find("list_scroll").get_page()
    if current_page > len(people):
        current_page = len(people) - 1
    prof_arr: str = '\r\n'
    non_prof_arr: str = '\r\n'
    for i in people[current_page].professional_interests:
        prof_arr = prof_arr + professional_interests_dict[i.id] + '\r\n'
    for i in people[current_page].non_professional_interests:
        non_prof_arr = non_prof_arr + non_professional_interests_dict[i.id] + '\r\n'
    return {
        "pages": len(people),
        "current_page": current_page + 1,
        "id": people[current_page].id,
        "telegram_id": people[current_page].telegram_id,
        "lastname": people[current_page].lastname,
        "firstname": people[current_page].firstname,
        "email": people[current_page].email,
        "institute": people[current_page].institute,
        "professional_interests": prof_arr,
        "non_professional_interests": non_prof_arr,
        "note": people[current_page].note,
    }