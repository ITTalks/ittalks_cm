from vk import types
from vk.bot_framework.dispatcher import Blueprint
from db.models.user import User
from .config import karma_bad, karma_good, karma_minus, karma_plus

bp = Blueprint()


@bp.message_handler(in_chat=True, with_reply_message=True)
async def add_karma(message: types.Message, _):
    if message.reply_message.from_id < 0:
        return
    if message.text.lower() in karma_good:
        user: User = await User.get_user(message.reply_message.from_id)
        await user.add_carma(user, karma_plus)
        await message.answer(f"Карма {user.nickname} обновлена - {user.karma}")
    elif message.text.lower() in karma_bad:
        user: User = await User.get_user(message.reply_message.from_id)
        await user.add_carma(user, karma_minus)
        await message.answer(f"Карма {user.nickname} обновлена - {user.karma}")
