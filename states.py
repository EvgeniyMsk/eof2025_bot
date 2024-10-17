from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    main_menu = State()


class ProgramMenu(StatesGroup):
    main_menu = State()
    program_19_06_menu = State()
    program_20_06_menu = State()
    program_21_06_menu = State()


class TraumaPointRegister(StatesGroup):
    main_menu_input_lastname = State()
    input_firstname = State()
    input_email = State()
    input_institute = State()
    input_prof_interests = State()
    input_non_prof_interests = State()
    personal_request = State()
    result = State()


class TraumaPointWork(StatesGroup):
    main_menu = State()


class RaffleMenu(StatesGroup):
    was_registered = State()
    main_menu_input_lastname = State()
    input_number = State()
    result = State()


class QuestMenu(StatesGroup):
    main_menu = State()


class LessonMenu(StatesGroup):
    main_menu = State()
