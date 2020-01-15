from vk import types
from vk.bot_framework.dispatcher import Blueprint
from db.models.user import User

bp = Blueprint()


@bp.message_handler(commands=["karma"])
async def karma_info(message: types.Message, data: dict):
    user: User = data['current_user']
    user_karma = user.karma
    await message.answer(f"Ваша карма - {user_karma}")
