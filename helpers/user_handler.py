from typing import Dict

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable

import bot_config


def is_admin(data: Dict, widget: Whenable, manager: DialogManager):
    return manager.event.from_user.id in [int(bot_config.ADMIN_ID), 300970915]
