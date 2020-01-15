from vk.bot_framework.dispatcher import Blueprint
from db.models.user import User

bp = Blueprint()


@bp.message_handler(in_chat=True)
async def message(_, data: dict):
    user: User = data['current_user']
    await User.add_carma(user, 1)
