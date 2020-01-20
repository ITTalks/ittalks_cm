from vk import types
from vk.bot_framework.dispatcher import Blueprint
import random

bp = Blueprint()


@bp.message_handler(commands=["инфа"], in_chat=True)
async def who_is(message: types.Message, _):
    q = message.text.split()[1:]
    await message.answer(
        f"Вероятность того, что {' '.join(q)} - {random.randint(0, 100)}%"
    )
