from vk import types
from vk.bot_framework.dispatcher import Blueprint
from bot.rules.admin import IsAdmin
from db.models.user import User

bp = Blueprint()


@bp.message_handler(IsAdmin(True), commands=["info"])
async def info(message: types.Message, data: dict):
    if message.reply_message is None:
        user: User = data["current_user"]
    else:
        user: User = await User.get_user(uid=message.reply_message.from_id)

    result = (
        f"uid - {user.uid}\nnickname - {user.nickname}\n"
        f"karma - {user.karma}\n warns - {user.warns}"
    )
    await message.answer(result)
