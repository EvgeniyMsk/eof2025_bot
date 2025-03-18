import json
from typing import List, Dict

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable

from db.models import EofUser, ProfessionalInterest, NonProfessionalInterest
from db.database import session_factory


def get_people():
    with open("people.json", mode="r", encoding="utf-8") as input_file:
        original_json = input_file.read()
    people = json.loads(original_json)
    return people


def get_people_from_db(dialog_manager: DialogManager) -> List[EofUser]:
    with (session_factory() as session):
        people = session.query(EofUser).where(EofUser.telegram_id != dialog_manager.event.from_user.id)
        current_person = session.query(EofUser).where(EofUser.telegram_id == dialog_manager.event.from_user.id).first()
        result = list()
        for person in people:
            if person.suits_by_prof_interests(current_person) or person.suits_by_non_prof_interests(current_person):
                result.append(person)
        return result


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
        if not (session.query(EofUser).where(EofUser.telegram_id == dialog_manager.event.from_user.id)).first():
            session.add(eof_user)
        else:
            updating_person = session.query(EofUser).where(EofUser.telegram_id == dialog_manager.event.from_user.id).first()
            updating_person.lastname = dialog_manager.find("lastname").get_value()
            updating_person.firstname = dialog_manager.find("firstname").get_value()
            updating_person.email = dialog_manager.find("email").get_value()
            updating_person.institute = dialog_manager.find("institute").get_value()
            updating_person.note = dialog_manager.find("personal_request").get_value()
            updating_person.professional_interests = professional_interests
            updating_person.non_professional_interests = non_professional_interests
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
    people = get_people_from_db(dialog_manager)
    if len(people) == 0:
        return {
            "pages": 0,
            "current_page": 0,
            "id": 0,
            "telegram_id": 0,
            "lastname": 0,
            "firstname": 0,
            "email": 0,
            "institute": 0,
            "professional_interests": [],
            "non_professional_interests": [],
            "note": '',
        }
    current_page = await dialog_manager.find("list_scroll").get_page()
    if current_page > len(people):
        current_page = len(people) - 1
    prof_arr: str = '\r\n'
    non_prof_arr: str = '\r\n'
    for i in sorted(people[current_page].professional_interests):
        prof_arr = prof_arr + professional_interests_dict[i.id] + '\r\n'
    for i in sorted(people[current_page].non_professional_interests):
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


def is_users_contains(data: Dict, widget: Whenable, manager: DialogManager):
    return len(get_people_from_db(manager)) > 0


def is_users_not_contains(data: Dict, widget: Whenable, manager: DialogManager):
    return len(get_people_from_db(manager)) == 0


def user_registered(data: Dict, widget: Whenable, manager: DialogManager):
    with session_factory() as session:
        person = session.query(EofUser).where(EofUser.telegram_id == manager.event.from_user.id)
        session.close()
    return person.count() > 0


def user_not_registered(data: Dict, widget: Whenable, manager: DialogManager):
    with session_factory() as session:
        person = session.query(EofUser).where(EofUser.telegram_id == manager.event.from_user.id)
        session.close()
    return person.count() <= 0
