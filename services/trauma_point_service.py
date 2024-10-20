import json

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from db.models import EofUser, ProfessionalInterest, NonProfessionalInterest
from db.database import session_factory


def get_people():
    with open("people.json", mode="r", encoding="utf-8") as input_file:
        original_json = input_file.read()
    people = json.loads(original_json)
    return people


def get_people_from_db():
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
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_1").is_checked(),
        dialog_manager.find("check_non_1").is_checked(),
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
