from vk import types
from vk.bot_framework.dispatcher import Blueprint
from bot.rules.admin import IsAdmin
from db.models.user import User

bp = Blueprint()


@bp.message_handler(IsAdmin(True), commands=["info"])
async def info(message: types.Message, data: dict):
    user: User = data["current_user"]
    result = (
        f"uid - {user.uid}\nnickname - {user.nickname}\n"
        f"karma - {user.karma}\n warns - {user.warns}"
    )
    await message.answer(result)
