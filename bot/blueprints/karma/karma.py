from vk import types
from vk.bot_framework.dispatcher import Blueprint
from bot.rules.admin import IsAdmin
from db.models.user import User

bp = Blueprint()


@bp.message_handler(IsAdmin(True), commands=["karma"])
async def karma_info(message: types.Message, data: dict):
    if message.reply_message is None:
        user: User = data["current_user"]
        await message.answer(f"Ваша карма - {user.karma}")
    else:
        user: User = await User.get_user(uid=message.reply_message.from_id)
        await message.answer(f"Карма {user.nickname} - {user.karma}")
