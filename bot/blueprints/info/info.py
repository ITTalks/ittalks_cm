from vk import types
from vk.bot_framework.dispatcher import Blueprint
from db.models.user import User

bp = Blueprint()


@bp.message_handler(commands=["info"])
async def info(message: types.Message, data: dict):
    user: User = data["current_user"]
    result = (
        f"uid - {user.uid}\nnickname - {user.nickname}\n"
        f"karma - {user.karma}\n warns - {user.warns}"
    )
    await message.answer(result)
