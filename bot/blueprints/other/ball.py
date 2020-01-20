from vk import types
from vk.bot_framework.dispatcher import Blueprint
import random

bp = Blueprint()

answers = ["Возможно", "Да", "Нет", "Скорее всего", "И не мечтай",
           "Определённо да", "Определённо нет", "Может быть",
           "Только после принятия ислама"]


@bp.message_handler(commands=["шар"], in_chat=True)
async def who_is(message: types.Message, _):
    await message.answer(random.choice(answers))
