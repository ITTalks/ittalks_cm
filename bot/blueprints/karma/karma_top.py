from vk import types
from vk.bot_framework.dispatcher import Blueprint
from db.models.user import User

bp = Blueprint()


@bp.message_handler(commands=["top"])
async def karma_info(message: types.Message, _):
    result = "Топ по карме:\n"
    users = User.find().sort("karma", -1)
    async for user in users:
        result += f"*id{user.uid}({user.nickname}) - {user.karma}\n"
    await message.answer(result)
