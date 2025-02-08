import os

from aiogram.enums import ParseMode, ContentType
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Cancel, Row, Start, Next
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Jinja

from states import QuestMenu

main_dialog = Dialog(
    Window(
        StaticMedia(
            path=os.path.abspath(os.path.curdir) + '/files/images/quest_dialog/quest_theme.jpg',
            type=ContentType.PHOTO,
        ),
        Jinja(
            f'Привет, дорогой участник!\n\n'
            'Наступил первый день Евразийского ортопедического форума - самое\n'
            'долгожданное событие этого года. А значит, настало время отправляться в \n'
            'путешествие по увлекательному травматологическому квесту «ЕОФ»:\n'
            '· посетить стенды партнеров Форума\n'
            '· получить много полезной информации\n'
            '· найти ответы на все вопросы\n'
            '· получить мини-призы от партнеров Форума на память об этом дне!\n\n'
            'Мы предлагаем идти последовательно и в общем темпе: передвигаться по\n'
            'указанным станциям, выполнять мини-задания и получать подарки. Так будет\n'
            'интереснее и результативнее!\n\n'
            'Но! Если вам хочется, всегда можно пропустить точку и перейти к той\n'
            'станции, которая вам будет более интересна. Все только по вашему желанию.\n'
            'Если готовы, то пора начинать!\n'
        ),
        Row(
            Next(Const("📋Начать"), id="start_quest"),
        ),
        Row(
            Cancel(Const("Начну позже"), id="skip_quest"),
        ),
        Cancel(Const('Назад')),
        state=QuestMenu.main_menu,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Первое задание'),
        Row(Next(Const("Задание выполнил(а)")), Next(Const('Перейти к другой станции'))),
        state=QuestMenu.task_1,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Второе задание'),
        Row(Next(Const("Задание выполнил(а)")), Next(Const('Перейти к другой станции'))),
        state=QuestMenu.task_2,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Третье задание'),
        Row(Next(Const("Задание выполнил(а)")), Next(Const('Перейти к другой станции'))),
        state=QuestMenu.task_3,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Четвертое задание'),
        Row(Next(Const("Задание выполнил(а)")), Next(Const('Перейти к другой станции'))),
        state=QuestMenu.task_4,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(f'Пятое задание'),
        Row(Next(Const("Задание выполнил(а)")), Next(Const('Перейти к другой станции'))),
        state=QuestMenu.task_5,
        parse_mode=ParseMode.HTML,
    ),
    Window(
        Jinja(
            f'Поздравляем, вы прошли непростой путь и наконец-то посетили последнюю\n'
            f'станцию. Мы восхищаемся вашей сообразительностью, ловкостью и \n'
            f'упорством - такие качества присущи только настоящим профессионалам\n'
            f'своего дела!\n\n'
            f'Надеемся, вы получили много положительных эмоций и теперь на площадке \n'
            f'будет легче ориентироваться. До встречи в 2027 году!\n'
        ),
        Row(Cancel(Const('Главное меню'))),
        state=QuestMenu.finish,
        parse_mode=ParseMode.HTML,
    ),
    on_process_result=QuestMenu.main_menu,

)