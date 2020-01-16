from vk import types
from vk.bot_framework.dispatcher import Blueprint
from bot.rules.admin import IsAdmin
from db.models.user import User

bp = Blueprint()


@bp.message_handler(IsAdmin(True), commands=["top"])
async def karma_info(message: types.Message, _):
    result = "Топ по карме:\n"
    users = User.find().sort("karma", -1)
    async for user in users:
        result += f"{user.nickname} - {user.karma}\n"
    await message.answer(result)
