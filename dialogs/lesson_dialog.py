import os

from aiogram.enums import ContentType, ParseMode
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Cancel, Url
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Jinja

from states import LessonMenu

main_dialog = Dialog(
    Window(
        StaticMedia(
            path=os.path.abspath(os.path.curdir) + '/files/images/lesson_dialog/lesson_theme.png',
            type=ContentType.PHOTO,
        ),
        Jinja(
            f'Программа ЕОФ-2025 будет состоять из дискуссий, кейс-марафонов,\n'
            f'баттлов и других интерактивных форматов, позволяющих наиболее \n'
            f'продуктивно вести профессионально-образовательную дискуссию.\n\n'
            f'<b>Все доклады мы представим в программе отдельным блоком</b>\n'
            f'✔️на сайте ЕОФ\n'
            f'✔️в программе\n'
            f'✔️в специальных зонах на выставке на мультимедиа-экранах\n'
            f'✔️в лаунж-зоне ЕОФ\n'
            f'✔️<b>здесь в ЕОФ-боте</b>!\n'
            f'За месяц до Форума мы откроем доступ к просмотру и изучению ЕОФ-постеров.\n'
            f'Участники смогут не только изучить Ваши доклады, но и задать вопросы через бот, \n'
            f'назначить личную встречу и проголосовать за понравившийся постер.\n\n'
            f'🎁Авторам лучших докладов вручат ценные призы на церемонии закрытия ЕОФ-2025.\n'
        ),
        Url(
            Const("Подать ЕОФ-постер в программу"),
            Const('https://docs.google.com/forms/d/e/1FAIpQLSeG8QnPhj3u-y-pjj1C8VMcwUZXXh2-VuoSvNA79MWOGFqBDw/viewform'),
        ),
        Cancel(Const('Назад')),
        state=LessonMenu.main_menu,
        parse_mode=ParseMode.HTML,
    ),
)
