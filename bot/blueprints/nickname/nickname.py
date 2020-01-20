from vk import types
from vk.bot_framework.dispatcher import Blueprint
from db.models.user import User

bp = Blueprint()


@bp.message_handler(commands=["nickname", "nick"], args_range=(1, 10))
async def change_nick(message: types.Message, data: dict):
    nick = message.text.split()[1:]
    user: User = data["current_user"]
    await User.change_nick(user, " ".join(nick))
    await message.answer(f"Ник успешно сменен на *id{user.uid}({user.nickname})")
